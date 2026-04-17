#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Run -- Full autonomous pipeline: intent -> artifact on disk.

This is the PRIMARY entry point for artifact production.
For system-level operations (health, providers, missions), see cex_auto_run.py.

Chains:
  1. cex_query.py       -> discover best builder
  2. cex_8f_motor.py    -> parse intent + classify + plan
  3. cex_crew_runner    -> compose full prompt with specs + memory
  4. claude CLI (-p)    -> execute via subscription (no API key needed)
  5. cex_hooks.py       -> validate artifact
  6. cex_compile.py     -> .md -> .yaml
  7. cex_memory_update  -> record observation
  8. cex_score.py       -> peer-review score

Usage:
  python _tools/cex_run.py "create a knowledge card about RAG patterns"
  python _tools/cex_run.py "cria agente de vendas" --quality 9.5
  python _tools/cex_run.py "build webhook handler" --dry-run
  python _tools/cex_run.py "create a workflow for code review" --execute
  python _tools/cex_run.py --status

See also:
  cex_auto_run.py  -- system health, provider discovery, multi-nucleus missions
  cex_8f_runner.py -- low-level 8F pipeline with F1-F8 step control
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from _tools.cex_query import query_builders
from _tools.cex_8f_motor import (
    parse_intent, classify_objects, fan_out, generate_output,
    load_builder_map, load_kc_library, rebuild_kc_index,
    resolve_effort_model,
)
from _tools.cex_crew_runner import (
    load_builder_context, compose_prompt, RunState,
)
from _tools.cex_compile import compile_file
from _tools.cex_hooks import validate_artifact


# -- Config ------------------------------------------------------------------

# Use short aliases (subscription auth) -- NOT full model IDs (API credits).
# "sonnet" / "opus" / "haiku" -> subscription. "claude-sonnet-4-6" -> API billing.
EFFORT_TO_MODEL = {
    "low": "haiku",
    "medium": "sonnet",
    "high": "sonnet",
    "max": "opus",
}
DEFAULT_MODEL = "sonnet"
MAX_RETRIES = 2
QUALITY_GATE = 8.0
OUTPUT_DIR = ROOT / ".cex" / "runtime" / "outputs"


# -- Status ------------------------------------------------------------------

def show_status():
    """Show system status summary."""
    print("+======================================+")
    print("|        CEX System Status             |")
    print("+======================================+")

    builder_dir = ROOT / "archetypes" / "builders"
    builders = [d for d in builder_dir.iterdir()
                if d.is_dir() and not d.name.startswith(("_", "."))]
    print(f"|  Builders:    {len(builders):>4}                  |")

    kinds_file = ROOT / ".cex" / "kinds_meta.json"
    if kinds_file.exists():
        with open(kinds_file, encoding="utf-8") as f:
            kinds = json.load(f)
        print(f"|  Kinds:       {len(kinds):>4}                  |")

    total_nuc = 0
    for n in range(1, 8):
        ndir = list(ROOT.glob(f"N0{n}_*"))
        if ndir:
            count = len(list(ndir[0].rglob("*.md"))) - len(list(ndir[0].rglob("*/compiled/*.md")))
            total_nuc += count
    print(f"|  Nucleus .md: {total_nuc:>4}                  |")

    compiled = len(list(ROOT.rglob("compiled/*.yaml"))) + len(list(ROOT.rglob("compiled/*.json")))
    print(f"|  Compiled:    {compiled:>4}                  |")

    try:
        r = subprocess.run(["git", "log", "--oneline", "-1"],
                          capture_output=True, text=True, cwd=ROOT)
        last_commit = r.stdout.strip()[:50]
        print(f"|  Last: {last_commit:<29}|")
    except Exception:
        pass

    print("+======================================+")


# -- Step 1: Discovery ------------------------------------------------------

def discover(intent: str, top_k: int = 5) -> list[dict]:
    """Find best builders for intent via TF-IDF."""
    return query_builders(intent, top_k=top_k)


# -- Step 2: Plan ------------------------------------------------------------

def plan(intent: str, quality: float = 9.0) -> dict:
    """Parse intent -> execution plan."""
    builder_map = load_builder_map()
    kc_library = load_kc_library()
    rebuild_kc_index()

    parsed = parse_intent(intent, quality)
    if parsed.get("error"):
        return {"error": parsed["error"]}

    classified = classify_objects(parsed["objects"])
    functions = fan_out(
        classified, intent.lower(), parsed["quality"],
        builder_map, parsed["verb_action"], kc_library=kc_library,
    )
    return generate_output(intent, parsed, classified, functions)


# -- Step 3: Compose ---------------------------------------------------------

def compose(intent: str, builder_id: str, quality: float = 9.0) -> str:
    """Compose full prompt with builder specs + memory + context."""
    parsed_dict = {
        "verb": intent.split()[0],
        "object": builder_id.replace("-builder", ""),
        "domain": "generic",
        "multi_object": False,
    }
    state = RunState(intent=intent, plan={})
    return compose_prompt(
        builder_id=builder_id,
        function_name="create",
        intent=intent,
        parsed=parsed_dict,
        quality_target=quality,
        state=state,
    )


# -- Step 4: Execute via claude CLI ------------------------------------------

def execute_via_cli(prompt: str, model: str = DEFAULT_MODEL,
                    timeout: int = 120) -> tuple[str, bool]:
    """Call `claude -p` with the composed prompt. Uses subscription auth.

    Returns (response_text, success).
    """
    # Append output-only instruction so LLM returns raw artifact, no meta-commentary
    execution_prompt = prompt + """

## CRITICAL OUTPUT INSTRUCTION
You are running in non-interactive print mode. You CANNOT use tools or write files.
Your ONLY job: output the COMPLETE artifact as raw markdown.
Start with the YAML frontmatter (---) and end with the last line of content.
Do NOT include explanations, apologies, or commentary before or after the artifact.
Do NOT say "I need permissions" or "I cannot write files".
Just output the artifact content directly. START WITH --- NOW:
"""

    prompt_file = OUTPUT_DIR / "current_prompt.md"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    prompt_file.write_text(execution_prompt, encoding="utf-8")

    cmd = [
        "claude", "-p",
        "--model", model,
        "--no-chrome",
    ]

    try:
        result = subprocess.run(
            cmd,
            input=execution_prompt,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(ROOT),
            encoding="utf-8",
        )
        if result.returncode != 0:
            error_msg = result.stderr[:500] or result.stdout[:500]
            return f"[CLI-ERROR] Exit code {result.returncode}: {error_msg}", False
        return result.stdout, True
    except subprocess.TimeoutExpired:
        return f"[TIMEOUT] claude -p exceeded {timeout}s", False
    except FileNotFoundError:
        return "[CLI-NOT-FOUND] 'claude' not in PATH. Install Claude Code CLI.", False
    except Exception as e:
        return f"[ERROR] {e}", False


# -- Step 5: Extract artifact from LLM response -----------------------------

def extract_artifact(response: str, kind: str, intent: str) -> tuple[str, dict]:
    """Extract the markdown artifact from LLM response.

    Returns (artifact_content, metadata).
    """
    # Strategy 1: Find frontmatter-bounded content (--- ... --- ... body)
    fm_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n(.+)', re.DOTALL | re.MULTILINE)
    match = fm_pattern.search(response)
    if match:
        artifact = f"---\n{match.group(1)}\n---\n{match.group(2)}"
        return artifact.strip(), {"extraction": "frontmatter_match"}

    # Strategy 2: Find code block with frontmatter
    block_pattern = re.compile(r'```(?:markdown|md|yaml)?\s*\n(---\s*\n.*?\n---\s*\n.+?)```',
                               re.DOTALL)
    match = block_pattern.search(response)
    if match:
        return match.group(1).strip(), {"extraction": "code_block"}

    # Strategy 3: The response IS the artifact (starts with ---)
    if response.strip().startswith("---"):
        return response.strip(), {"extraction": "raw_response"}

    return response.strip(), {"extraction": "fallback_raw"}


# -- Step 6: Determine output path ------------------------------------------

def resolve_output_path(kind: str, domain: str, intent: str) -> Path:
    """Determine where to save the artifact based on kind + pillar."""
    kinds_file = ROOT / ".cex" / "kinds_meta.json"
    pillar = "P01"
    naming = ""

    if kinds_file.exists():
        with open(kinds_file, encoding="utf-8") as f:
            kinds = json.load(f)
        meta = kinds.get(kind, {})
        pillar = meta.get("pillar", "P01")
        naming = meta.get("naming", "")

    # Map pillar to directory
    _n00 = ROOT / "N00_genesis"
    pillar_dirs = {p.name: p for p in _n00.iterdir()
                   if p.is_dir() and re.match(r'P\d{2}_', p.name)}
    target_dir = pillar_dirs.get(pillar, _n00 / "P01_knowledge")

    # If no target dir, find by prefix
    if not target_dir.exists():
        matches = list(_n00.glob(f"{pillar}_*"))
        target_dir = matches[0] if matches else _n00 / "P01_knowledge"

    # Generate filename
    slug = re.sub(r'[^a-z0-9]+', '_', intent.lower())[:60].strip('_')
    filename = f"{pillar.lower()}_{kind}_{slug}.md"

    # Put in examples/ subdirectory
    output_path = target_dir / "examples" / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)

    return output_path


# -- Step 7: Validate + Compile + Memory -------------------------------------

def post_process(artifact_path: Path, builder_id: str, intent: str,
                 quality_score: float, verbose: bool = False) -> dict:
    """Validate, compile, score, update memory."""
    results = {"path": str(artifact_path)}

    # Validate
    issues = validate_artifact(str(artifact_path))
    results["validation"] = {
        "issues": len(issues),
        "details": [i.get("message", str(i)) for i in issues[:5]],
    }
    if verbose:
        status = "[OK] PASS" if not issues else f"[WARN] {len(issues)} issue(s)"
        print(f"  Validate: {status}")

    # Compile
    try:
        ok = compile_file(Path(artifact_path))
        results["compiled"] = ok
        if verbose:
            print(f"  Compile:  {'[OK]' if ok else '[FAIL]'}")
    except Exception as e:
        results["compiled"] = False
        if verbose:
            print(f"  Compile:  [FAIL] {e}")

    # Evolve (AutoResearch: heuristic free + agent via SDK if score < threshold)
    try:
        from _tools.cex_evolve import evolve_auto
        ev = evolve_auto(
            Path(artifact_path),
            threshold=8.5,          # heuristic-only above this
            agent_budget=30000,     # max tokens for agent mode
            agent_target=9.0,       # agent tries to reach this
            agent_max_rounds=5,     # max LLM calls per artifact
            verbose=False,
        )
        results["evolved"] = ev
        results["scored"] = True
        if verbose:
            q = ev.get("quality", "?")
            mode = ev.get("mode_used", "?")
            tokens = ev.get("tokens_used", 0)
            tok_str = f", {tokens:,} tokens" if tokens > 0 else ""
            print(f"  Evolve:   q={q} (mode={mode}{tok_str})")
    except Exception:
        # Fallback to plain scoring if evolve fails
        try:
            from _tools.cex_score import score_file
            score_file(str(artifact_path), apply=True)
            results["scored"] = True
            if verbose:
                print(f"  Score:    [OK] applied (evolve fallback)")
        except Exception:
            results["scored"] = False

    # Memory update
    try:
        from _tools.cex_memory_update import update_builder_memory
        update_builder_memory(
            builder_id=builder_id,
            observation=f"Built '{intent}' -> {artifact_path.name} (q={quality_score:.1f})",
            confidence=0.8 if quality_score >= QUALITY_GATE else 0.5,
        )
        results["memory_updated"] = True
        if verbose:
            print(f"  Memory:   [OK] observation recorded")
    except Exception:
        results["memory_updated"] = False

    return results


# -- Full Run ----------------------------------------------------------------

def run(intent: str, quality: float = 9.0, dry_run: bool = False,
        execute: bool = False, verbose: bool = False) -> dict:
    """Full pipeline: intent -> discover -> plan -> compose -> [execute -> save]."""
    t0 = time.time()
    result = {"intent": intent, "quality_target": quality, "steps": []}

    # Step 1: Discover
    if verbose:
        print(f"\n{'='*60}")
        print(f"  CEX Run: \"{intent}\"")
        print(f"{'='*60}")
        print(f"\n[1/{'7' if execute else '4'}] Discovering builders...")
    builders = discover(intent, top_k=3)
    result["steps"].append({
        "step": "discover",
        "builders": [{"id": b["builder_id"], "score": round(b["score"], 3)} for b in builders],
    })
    if verbose:
        for b in builders[:3]:
            print(f"  -> {b['builder_id']} (score={b['score']:.3f})")

    if not builders:
        result["error"] = "No builders found for intent"
        return result

    primary_builder = builders[0]["builder_id"]

    # Step 2: Plan
    if verbose:
        print(f"\n[2/{'7' if execute else '4'}] Planning execution...")
    execution_plan = plan(intent, quality)
    if execution_plan.get("error"):
        result["error"] = execution_plan["error"]
        return result

    result["steps"].append({
        "step": "plan",
        "total_builders": execution_plan.get("total_builders", 0),
        "estimated_tokens": execution_plan.get("estimated_tokens", 0),
        "warnings": execution_plan.get("warnings", []),
    })
    if verbose:
        print(f"  -> {execution_plan['total_builders']} builder(s), "
              f"~{execution_plan['estimated_tokens']:,} tokens")

    # Step 3: Compose prompt
    if verbose:
        print(f"\n[3/{'7' if execute else '4'}] Composing prompt for: {primary_builder}")
    prompt = compose(intent, primary_builder, quality)
    result["steps"].append({
        "step": "compose",
        "builder_id": primary_builder,
        "prompt_length": len(prompt),
        "prompt_tokens_est": len(prompt) // 4,
    })
    if verbose:
        print(f"  -> {len(prompt):,} chars (~{len(prompt)//4:,} tokens)")

    # Step 4: Dedup check
    if verbose:
        print(f"\n[4/{'7' if execute else '4'}] Checking for duplicates...")
    try:
        from _tools.cex_retriever import build_index, find_similar
        idx = build_index()
        similar = find_similar(intent, top_k=3, index=idx)
        dupes = [s for s in similar if s["score"] > 0.4]
        result["steps"].append({
            "step": "dedup_check",
            "similar_found": len(dupes),
            "similar": [{"score": round(s["score"], 3), "path": s["path"]} for s in dupes],
        })
        if verbose:
            if dupes:
                print(f"  [WARN] {len(dupes)} similar artifact(s):")
                for s in dupes:
                    print(f"    {s['score']:.3f} {s['path']}")
            else:
                print(f"  [OK] No duplicates")
    except Exception as e:
        result["steps"].append({"step": "dedup_check", "error": str(e)})

    # Save prompt
    prompt_path = ROOT / ".cex" / "runtime" / "last_prompt.md"
    prompt_path.parent.mkdir(parents=True, exist_ok=True)
    prompt_path.write_text(prompt, encoding="utf-8")

    if not execute:
        result["elapsed_seconds"] = round(time.time() - t0, 2)
        result["primary_builder"] = primary_builder
        result["prompt"] = prompt if not dry_run else f"[DRY-RUN] {len(prompt)} chars"
        if verbose:
            print(f"\n{'='*60}")
            print(f"  Prompt ready ({len(prompt):,} chars)")
            print(f"  Saved to: .cex/runtime/last_prompt.md")
            print(f"  Add --execute to send to claude CLI")
            print(f"{'='*60}")
        return result

    # -- EXECUTE MODE: Steps 5-7 -----------------------------------------

    # Resolve model from builder effort config
    try:
        import yaml
        config_path = ROOT / "archetypes" / "builders" / primary_builder / f"bld_config_{primary_builder.replace('-builder','')}.md"
        if config_path.exists():
            text = config_path.read_text(encoding="utf-8")
            if text.startswith("---"):
                fm = yaml.safe_load(text[3:text.index("---", 3)])
                effort = fm.get("effort", "medium")
            else:
                effort = "medium"
        else:
            effort = "medium"
    except Exception:
        effort = "medium"

    model = EFFORT_TO_MODEL.get(effort, DEFAULT_MODEL)

    # Auto-discover best available provider
    try:
        from _tools.cex_provider_discovery import discover_providers, get_best_provider
        providers = discover_providers()
        nucleus = os.environ.get("CEX_NUCLEUS", "n03").lower()
        best = get_best_provider(nucleus, providers)
        if best and best != model:
            if verbose:
                print(f"  Auto-routed to {best} (discovery override)")
            model = best
    except Exception:
        pass  # discovery failure = use configured default

    # Step 5: Execute
    if verbose:
        print(f"\n[5/7] Executing via claude -p (model={model}, effort={effort})...")

    response, success = execute_via_cli(prompt, model=model)
    if not success:
        result["error"] = response
        result["steps"].append({"step": "execute", "success": False, "error": response})
        return result

    result["steps"].append({
        "step": "execute",
        "success": True,
        "response_length": len(response),
        "model": model,
    })
    if verbose:
        print(f"  -> {len(response):,} chars response")

    # Extract artifact
    kind = primary_builder.replace("-builder", "").replace("-", "_")
    artifact_content, extract_meta = extract_artifact(response, kind, intent)
    result["steps"].append({
        "step": "extract",
        "method": extract_meta["extraction"],
        "artifact_length": len(artifact_content),
    })

    # Determine output path and save
    output_path = resolve_output_path(kind, "generic", intent)
    output_path.write_text(artifact_content, encoding="utf-8")

    if verbose:
        print(f"  -> Saved: {output_path.relative_to(ROOT)}")

    # Step 6-7: Post-process (validate + compile + score + memory)
    if verbose:
        print(f"\n[6/7] Post-processing...")
    pp_result = post_process(output_path, primary_builder, intent, quality, verbose)
    result["steps"].append({"step": "post_process", **pp_result})

    # Quality check -- retry if below gate
    quality_score = quality  # placeholder until we parse from artifact
    fm_match = re.search(r'quality:\s*([\d.]+)', artifact_content)
    if fm_match:
        quality_score = float(fm_match.group(1))

    if quality_score < QUALITY_GATE and not dry_run:
        if verbose:
            print(f"\n[7/7] Quality {quality_score:.1f} < {QUALITY_GATE} -- retrying...")
        retry_prompt = (
            prompt + f"\n\n## RETRY FEEDBACK\n"
            f"Previous attempt scored {quality_score:.1f}, below gate {QUALITY_GATE}.\n"
            f"Issues: {pp_result.get('validation', {}).get('details', [])}\n"
            f"Improve quality and density. Target >= {quality}."
        )
        response2, success2 = execute_via_cli(retry_prompt, model=model)
        if success2:
            artifact2, _ = extract_artifact(response2, kind, intent)
            output_path.write_text(artifact2, encoding="utf-8")
            post_process(output_path, primary_builder, intent, quality, verbose)
            result["retried"] = True
    else:
        if verbose:
            print(f"\n[7/7] Quality gate: [OK] PASS")

    result["elapsed_seconds"] = round(time.time() - t0, 2)
    result["primary_builder"] = primary_builder
    result["output_path"] = str(output_path.relative_to(ROOT))

    if verbose:
        print(f"\n{'='*60}")
        print(f"  [OK] Artifact created: {output_path.relative_to(ROOT)}")
        print(f"  Builder: {primary_builder}")
        print(f"  Elapsed: {result['elapsed_seconds']}s")
        print(f"{'='*60}")

    return result


# -- CLI ---------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="CEX Run -- Full pipeline: intent -> artifact on disk",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Discover + plan + compose prompt (no execution):
  python _tools/cex_run.py "create a knowledge card about RAG patterns"

  # Full autonomous: compose -> claude CLI -> validate -> compile -> save:
  python _tools/cex_run.py "create a knowledge card about RAG" --execute

  # Dry run (plan only):
  python _tools/cex_run.py "build webhook handler" --dry-run

  # Discovery only:
  python _tools/cex_run.py --discover "payment processing"

  # System status:
  python _tools/cex_run.py --status
        """,
    )
    parser.add_argument("intent", nargs="?", help="Natural language intent")
    parser.add_argument("--quality", "-q", type=float, default=9.0,
                       help="Quality target (default: 9.0)")
    parser.add_argument("--execute", "-x", action="store_true",
                       help="Execute via claude CLI (subscription auth)")
    parser.add_argument("--dry-run", action="store_true",
                       help="Plan without saving prompt")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Show step-by-step progress")
    parser.add_argument("--status", action="store_true",
                       help="Show system status")
    parser.add_argument("--discover", metavar="QUERY",
                       help="Discover builders for a query")
    parser.add_argument("--plan", metavar="INTENT",
                       help="Generate execution plan only")
    parser.add_argument("--json", action="store_true",
                       help="Output as JSON")
    parser.add_argument("--bare", action="store_true",
                       help="Skip config search + heavy context load (10x startup). Use for hot-loop dispatch.")

    args = parser.parse_args()

    if args.bare:
        os.environ["CEX_BARE"] = "1"
        os.environ["CEX_SKIP_KC_INDEX"] = "1"
        os.environ["CEX_SKIP_MEMORY_LOAD"] = "1"

    if args.status:
        show_status()
        return

    if args.discover:
        results = discover(args.discover)
        if args.json:
            print(json.dumps([{"id": r["builder_id"], "score": round(r["score"], 3)}
                             for r in results], indent=2))
        else:
            print(f'\nBuilders for: "{args.discover}"\n')
            for i, r in enumerate(results, 1):
                print(f"  {i}. {r['builder_id']} (score={r['score']:.3f})")
        return

    if args.plan:
        result = plan(args.plan, args.quality)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    if not args.intent:
        parser.error("intent is required (or use --status, --discover, --plan)")

    # Suppress WARN output when --json
    if args.json:
        import io, contextlib
        with contextlib.redirect_stderr(io.StringIO()):
            result = run(args.intent, args.quality,
                        dry_run=args.dry_run, execute=args.execute, verbose=False)
    else:
        result = run(args.intent, args.quality,
                    dry_run=args.dry_run, execute=args.execute,
                    verbose=True)

    if args.json:
        output = {k: v for k, v in result.items() if k != "prompt"}
        output["prompt_length"] = len(result.get("prompt", ""))
        print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
