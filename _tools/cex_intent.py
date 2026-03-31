#!/usr/bin/env python3
"""
cex_intent.py -- The Steering Wheel
Natural language intent -> governed artifact prompt.

Uses Motor 8F to classify intent, loads builder ISOs + KC-Domains,
and composes a GOVERNED PROMPT ready for LLM execution.

Usage:
  python cex_intent.py "cria knowledge card sobre RAG chunking"
  python cex_intent.py "cria agente de vendas para ML" --dry-run
  python cex_intent.py "melhora knowledge card de eval" --execute
  python cex_intent.py --list-kinds
  python cex_intent.py "cria agent" --kind agent --dry-run
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

import argparse
import json
from pathlib import Path

# Import Motor 8F
sys.path.insert(0, str(Path(__file__).resolve().parent))
from cex_8f_motor import (
    CEX_ROOT,
    OBJECT_TO_KINDS,
    classify_objects,
    fan_out,
    generate_output,
    load_builder_map,
    load_kc_library,
    parse_intent,
)
from cex_shared import find_builder_dir

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BUILDERS_ROOT = CEX_ROOT / "archetypes" / "builders"

# Builder ISO file prefixes in compose_prompt order
# Order: system_prompt, instruction, KC-Domain (injected), schema, output_template
COMPOSE_ORDER = [
    "bld_system_prompt",
    "bld_instruction",
    # KC-Domain injection point (handled separately)
    "bld_schema",
    "bld_output_template",
]

# All 13 ISO prefixes for reference
ALL_ISO_PREFIXES = [
    "bld_manifest",
    "bld_system_prompt",
    "bld_instruction",
    "bld_knowledge_card",
    "bld_examples",
    "bld_schema",
    "bld_output_template",
    "bld_quality_gate",
    "bld_tools",
    "bld_config",
    "bld_memory",
    "bld_architecture",
    "bld_collaboration",
]


# find_builder_dir imported from cex_shared


def load_builder_iso(builder_dir: Path, prefix: str, kind_slug: str) -> str | None:
    """Load a single builder ISO file by prefix.

    Looks for: {prefix}_{kind_slug}.md
    Falls back to any file starting with {prefix}.
    """
    target = builder_dir / f"{prefix}_{kind_slug}.md"
    if target.exists():
        return target.read_text(encoding="utf-8")

    # Fallback: any file matching prefix
    for f in builder_dir.glob(f"{prefix}_*.md"):
        return f.read_text(encoding="utf-8")
    return None


def load_all_builder_isos(builder_dir: Path, kind: str) -> dict[str, str]:
    """Load all 13 builder ISOs into a dict keyed by prefix."""
    kind_slug = kind.replace("-", "_")
    isos = {}
    for prefix in ALL_ISO_PREFIXES:
        content = load_builder_iso(builder_dir, prefix, kind_slug)
        if content:
            isos[prefix] = content
    return isos


# ---------------------------------------------------------------------------
# KC-Domain Loading
# ---------------------------------------------------------------------------


def load_kc_domain_content(kc_matches: list[dict]) -> str:
    """Load KC-Domain markdown content from matched KCs."""
    parts = []
    for kc in kc_matches[:3]:  # Max 3 KCs to stay within token budget
        kc_path = CEX_ROOT / kc["path"]
        if kc_path.exists():
            text = kc_path.read_text(encoding="utf-8")
            # Strip frontmatter for prompt injection
            body = _strip_frontmatter(text)
            if body.strip():
                parts.append(f"### KC: {kc.get('title', kc.get('id', 'unknown'))}\n\n{body}")
    return "\n\n---\n\n".join(parts) if parts else ""


def _strip_frontmatter(text: str) -> str:
    """Remove YAML frontmatter from markdown."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end > 0:
            return text[end + 3 :].strip()
    return text


# ---------------------------------------------------------------------------
# Prompt Composition
# ---------------------------------------------------------------------------


def compose_prompt(
    intent: str,
    kind: str,
    builder_isos: dict[str, str],
    kc_content: str,
    parsed: dict,
    plan: dict,
) -> str:
    """Compose a GOVERNED PROMPT from builder ISOs + KC-Domain + intent.

    Order:
      1. bld_system_prompt  — identity and role
      2. bld_instruction    — step-by-step production process
      3. KC-Domain content  — domain knowledge injection
      4. bld_schema         — output schema/contract
      5. bld_output_template — expected output format
      6. User intent        — the actual request
    """
    sections = []

    # -- Section 1: System Prompt (identity)
    sp = builder_isos.get("bld_system_prompt")
    if sp:
        sections.append(f"# SYSTEM PROMPT (Builder Identity)\n\n{_strip_frontmatter(sp)}")

    # -- Section 2: Instructions (how to produce)
    instr = builder_isos.get("bld_instruction")
    if instr:
        sections.append(f"# INSTRUCTIONS (Production Process)\n\n{_strip_frontmatter(instr)}")

    # -- Section 3: KC-Domain (knowledge injection)
    if kc_content:
        sections.append(f"# DOMAIN KNOWLEDGE (KC Injection)\n\n{kc_content}")

    # -- Section 4: Schema (output contract)
    schema = builder_isos.get("bld_schema")
    if schema:
        sections.append(f"# SCHEMA (Output Contract)\n\n{_strip_frontmatter(schema)}")

    # -- Section 5: Output Template (expected format)
    tpl = builder_isos.get("bld_output_template")
    if tpl:
        sections.append(f"# OUTPUT TEMPLATE (Expected Format)\n\n{_strip_frontmatter(tpl)}")

    # -- Section 6: User Intent (the actual task)
    intent_block = _format_intent_block(intent, kind, parsed, plan)
    sections.append(f"# USER INTENT\n\n{intent_block}")

    return "\n\n---\n\n".join(sections)


def _format_intent_block(intent: str, kind: str, parsed: dict, plan: dict) -> str:
    """Format the user intent with parsed context."""
    lines = [
        f"**Intent**: {intent}",
        f"**Kind**: {kind}",
        f"**Verb**: {parsed.get('verb', 'cria')} ({parsed.get('verb_action', 'create')})",
        f"**Domain**: {parsed.get('domain', 'generic')}",
        f"**Quality Target**: {parsed.get('quality', 9.0)}",
    ]

    # Active builders summary
    active = []
    for fn in plan.get("functions", []):
        for b in fn.get("builders", []):
            if b.get("active"):
                active.append(f"{b['id']} ({fn['name']})")
    if active:
        lines.append(f"\n**Active Builders** ({len(active)}):")
        for a in active:
            lines.append(f"  - {a}")

    # Warnings
    warnings = plan.get("warnings", [])
    if warnings:
        lines.append("\n**Warnings**:")
        for w in warnings:
            lines.append(f"  ! {w}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# List Kinds
# ---------------------------------------------------------------------------


def list_kinds():
    """Print all available kinds grouped by pillar."""
    by_pillar: dict[str, list[tuple[str, str]]] = {}
    seen = set()
    for _keyword, kinds_list in sorted(OBJECT_TO_KINDS.items()):
        for kind, pillar, fn in kinds_list:
            key = (kind, pillar)
            if key not in seen:
                seen.add(key)
                by_pillar.setdefault(pillar, []).append((kind, fn))

    print("\n=== CEX Kinds (Motor 8F) ===\n")
    for pillar in sorted(by_pillar.keys()):
        kinds = sorted(by_pillar[pillar], key=lambda x: x[0])
        print(f"\n  {pillar}:")
        for kind, fn in kinds:
            builder_dir = find_builder_dir(kind)
            has_builder = "+" if builder_dir else " "
            print(f"    {has_builder} {kind:<30s} [{fn}]")
    print(f"\n  Total: {len(seen)} kinds")
    print("  + = builder exists in archetypes/builders/\n")


# ---------------------------------------------------------------------------
# Execution (--execute)
# ---------------------------------------------------------------------------


def execute_prompt(prompt: str) -> str:
    """Send composed prompt to LLM via available provider.

    Tries (in order):
      1. Anthropic SDK (claude)
      2. OpenAI SDK (gpt-4)
      3. Ollama local

    Returns the LLM response text.
    """
    # Try Anthropic
    try:
        import anthropic

        client = anthropic.Anthropic()
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8192,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text
    except (ImportError, Exception) as e:
        anthropic_err = str(e)

    # Try OpenAI
    try:
        import openai

        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o",
            max_tokens=8192,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
    except (ImportError, Exception) as e:
        openai_err = str(e)

    # Try Ollama
    try:
        import urllib.request

        data = json.dumps(
            {
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False,
            }
        ).encode("utf-8")
        req = urllib.request.Request(
            "http://localhost:11434/api/generate",
            data=data,
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result.get("response", "")
    except Exception as e:
        ollama_err = str(e)

    print("ERRO: Nenhum LLM provider disponivel.", file=sys.stderr)
    print(f"  Anthropic: {anthropic_err}", file=sys.stderr)
    print(f"  OpenAI: {openai_err}", file=sys.stderr)
    print(f"  Ollama: {ollama_err}", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Main Pipeline
# ---------------------------------------------------------------------------


def run_intent(
    intent: str,
    kind_override: str | None = None,
    dry_run: bool = True,
    quality: float | None = None,
) -> dict:
    """Full pipeline: intent -> Motor 8F -> builder ISOs -> governed prompt."""

    # Step 1: Motor 8F — parse + classify
    parsed = parse_intent(intent, quality_override=quality)

    if kind_override:
        # Override classification with explicit kind
        classified = classify_objects([kind_override])
    else:
        classified = classify_objects(parsed["objects"])

    # Step 2: Fan-out builders
    builder_map = load_builder_map()
    kc_library = load_kc_library()

    functions = fan_out(
        classified=classified,
        intent_lower=intent.lower(),
        quality=parsed["quality"],
        builder_map=builder_map,
        verb_action=parsed["verb_action"],
        kc_library=kc_library,
    )

    plan = generate_output(intent, parsed, classified, functions)

    # Step 3: Find primary kind and its builder
    primary_kind = classified[0]["kind"] if classified else "generic"
    builder_dir = find_builder_dir(primary_kind)

    if not builder_dir:
        print(f"AVISO: Builder nao encontrado para kind '{primary_kind}'", file=sys.stderr)
        print("  Tentando fallback: knowledge-card-builder", file=sys.stderr)
        builder_dir = find_builder_dir("knowledge_card")

    # Step 4: Load builder ISOs
    builder_isos = {}
    if builder_dir:
        builder_isos = load_all_builder_isos(builder_dir, primary_kind)

    # Step 5: Load KC-Domain content
    kc_content = ""
    for fn in plan.get("functions", []):
        if fn["name"] == "INJECT":
            kc_matches = fn.get("kc_injections") or []
            if kc_matches:
                kc_content = load_kc_domain_content(kc_matches)
            break

    # Step 6: Compose governed prompt
    prompt = compose_prompt(
        intent=intent,
        kind=primary_kind,
        builder_isos=builder_isos,
        kc_content=kc_content,
        parsed=parsed,
        plan=plan,
    )

    # Step 7: Execute or dry-run
    result = {
        "intent": intent,
        "kind": primary_kind,
        "builder_dir": str(builder_dir) if builder_dir else None,
        "isos_loaded": list(builder_isos.keys()),
        "kc_injected": bool(kc_content),
        "plan": plan,
        "prompt_tokens": len(prompt.split()),
        "prompt": prompt,
    }

    if not dry_run:
        print(f"\n>>> Executing prompt ({result['prompt_tokens']} words)...\n", file=sys.stderr)
        response = execute_prompt(prompt)
        result["response"] = response
        result["executed"] = True
    else:
        result["executed"] = False

    return result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="cex_intent.py -- Natural language to governed prompt (The Steering Wheel)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cex_intent.py "cria knowledge card sobre RAG"
  python cex_intent.py "cria agente de vendas" --dry-run
  python cex_intent.py "melhora eval de qualidade" --execute
  python cex_intent.py "cria agent" --kind agent
  python cex_intent.py --list-kinds
        """,
    )
    parser.add_argument("intent", nargs="?", help="Natural language intent string")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="Show composed prompt without executing (default)",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Send composed prompt to LLM and show response",
    )
    parser.add_argument("--kind", help="Override kind classification (e.g. agent, knowledge_card)")
    parser.add_argument("--quality", type=float, help="Quality target override (default: 9.0)")
    parser.add_argument("--list-kinds", action="store_true", help="List all available CEX kinds")
    parser.add_argument(
        "--json", action="store_true", help="Output full result as JSON (plan + prompt)"
    )
    parser.add_argument("--output", "-o", help="Write prompt to file instead of stdout")

    args = parser.parse_args()

    if args.list_kinds:
        list_kinds()
        return

    if not args.intent:
        parser.print_help()
        sys.exit(1)

    dry_run = not args.execute

    result = run_intent(
        intent=args.intent,
        kind_override=args.kind,
        dry_run=dry_run,
        quality=args.quality,
    )

    # Output
    if args.json:
        # Full JSON output (exclude prompt body for readability unless piped)
        output = {k: v for k, v in result.items() if k != "prompt"}
        output["prompt_preview"] = (
            result["prompt"][:500] + "..." if len(result["prompt"]) > 500 else result["prompt"]
        )
        print(json.dumps(output, indent=2, ensure_ascii=False, default=str))
        return

    # Header
    print(f"\n{'=' * 70}")
    print("  CEX Intent -> Governed Prompt")
    print(f"{'=' * 70}")
    print(f"  Intent:    {result['intent']}")
    print(f"  Kind:      {result['kind']}")
    print(f"  Builder:   {result['builder_dir'] or 'NONE'}")
    print(f"  ISOs:      {len(result['isos_loaded'])} loaded: {', '.join(result['isos_loaded'])}")
    print(f"  KC Domain: {'injected' if result['kc_injected'] else 'none matched'}")
    print(f"  Tokens:    ~{result['prompt_tokens']} words")
    print(f"  Mode:      {'EXECUTE' if result['executed'] else 'DRY-RUN'}")

    plan = result["plan"]
    print(f"  Builders:  {plan['total_builders']} active, ~{plan['estimated_tokens']} est. tokens")
    if plan.get("warnings"):
        for w in plan["warnings"]:
            print(f"  ! {w}")
    print(f"{'=' * 70}\n")

    if args.output:
        out_path = Path(args.output)
        out_path.write_text(result["prompt"], encoding="utf-8")
        print(f"  Prompt written to: {out_path}")
    else:
        if result.get("executed") and result.get("response"):
            print("--- LLM RESPONSE ---\n")
            print(result["response"])
        else:
            print("--- GOVERNED PROMPT ---\n")
            print(result["prompt"])
            print(f"\n--- END ({result['prompt_tokens']} words) ---")


if __name__ == "__main__":
    main()
