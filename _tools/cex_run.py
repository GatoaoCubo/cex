#!/usr/bin/env python3
"""CEX Run — Unified entry point: intent → plan → prompt → clipboard.

Chains the real tools:
  1. cex_query.py     → discover best builder(s)
  2. cex_8f_motor.py  → parse intent + classify + fan-out + plan
  3. cex_retriever.py → find similar artifacts (dedup check)
  4. cex_crew_runner   → compose full prompt with ISOs + memory
  5. cex_hooks.py     → validate output post-build

Usage:
  python _tools/cex_run.py "create a knowledge card about RAG patterns"
  python _tools/cex_run.py "cria agente de vendas" --quality 9.5
  python _tools/cex_run.py "build webhook handler" --dry-run
  python _tools/cex_run.py --status
"""

import argparse
import json
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
)
from _tools.cex_crew_runner import (
    load_builder_context, compose_prompt, RunState,
)
from _tools.cex_memory_select import select_relevant_memories, format_memory_injection
from _tools.cex_compile import compile_file
from _tools.cex_hooks import validate_artifact


# ── Status ──────────────────────────────────────────────────────────────────

def show_status():
    """Show system status summary."""
    from _tools.cex_doctor import main as doctor_main
    import subprocess

    print("╔══════════════════════════════════════╗")
    print("║        CEX System Status             ║")
    print("╠══════════════════════════════════════╣")

    # Builder count
    builder_dir = ROOT / "archetypes" / "builders"
    builders = [d for d in builder_dir.iterdir()
                if d.is_dir() and not d.name.startswith(("_", "."))]
    print(f"║  Builders:    {len(builders):>4}                  ║")

    # Kind count
    kinds_file = ROOT / ".cex" / "kinds_meta.json"
    if kinds_file.exists():
        with open(kinds_file, encoding="utf-8") as f:
            kinds = json.load(f)
        print(f"║  Kinds:       {len(kinds):>4}                  ║")

    # Nucleus artifacts
    total_nuc = 0
    for n in range(1, 8):
        ndir = list(ROOT.glob(f"N0{n}_*"))
        if ndir:
            count = len(list(ndir[0].rglob("*.md"))) - len(list(ndir[0].rglob("*/compiled/*.md")))
            total_nuc += count
    print(f"║  Nucleus .md: {total_nuc:>4}                  ║")

    # Tests
    test_dir = ROOT / "_tools" / "tests"
    test_count = len(list(test_dir.glob("test_*.py")))
    print(f"║  Test files:  {test_count:>4}                  ║")

    # Compiled
    compiled = len(list(ROOT.rglob("compiled/*.yaml"))) + len(list(ROOT.rglob("compiled/*.json")))
    print(f"║  Compiled:    {compiled:>4}                  ║")

    # Git
    try:
        r = subprocess.run(["git", "log", "--oneline", "-1"],
                          capture_output=True, text=True, cwd=ROOT)
        last_commit = r.stdout.strip()[:50]
        print(f"║  Last commit: {last_commit:<22}║")
    except Exception:
        pass

    print("╚══════════════════════════════════════╝")


# ── Discovery ───────────────────────────────────────────────────────────────

def discover(intent: str, top_k: int = 5) -> list[dict]:
    """Step 1: Find best builders for intent."""
    results = query_builders(intent, top_k=top_k)
    return results


# ── Plan ────────────────────────────────────────────────────────────────────

def plan(intent: str, quality: float = 9.0) -> dict:
    """Step 2: Parse intent → execution plan."""
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


# ── Compose ─────────────────────────────────────────────────────────────────

def compose(intent: str, builder_id: str, quality: float = 9.0) -> str:
    """Step 3: Compose full prompt with ISOs + memory + context."""
    parsed_dict = {
        "verb": intent.split()[0],
        "object": builder_id.replace("-builder", ""),
        "domain": "generic",
        "multi_object": False,
    }
    state = RunState(intent=intent, plan={})
    prompt = compose_prompt(
        builder_id=builder_id,
        function_name="create",
        intent=intent,
        parsed=parsed_dict,
        quality_target=quality,
        state=state,
    )
    return prompt


# ── Full Run ────────────────────────────────────────────────────────────────

def run(intent: str, quality: float = 9.0, dry_run: bool = False,
        verbose: bool = False) -> dict:
    """Full pipeline: intent → discover → plan → compose prompt."""
    t0 = time.time()
    result = {"intent": intent, "quality_target": quality, "steps": []}

    # Step 1: Discover
    if verbose:
        print(f"\n[1/4] Discovering builders for: \"{intent}\"")
    builders = discover(intent, top_k=3)
    result["steps"].append({
        "step": "discover",
        "builders": [{"id": b["builder_id"], "score": round(b["score"], 3)} for b in builders],
    })
    if verbose:
        for b in builders:
            print(f"  → {b['builder_id']} (score={b['score']:.3f})")

    if not builders:
        result["error"] = "No builders found for intent"
        return result

    # Step 2: Plan
    if verbose:
        print(f"\n[2/4] Planning execution...")
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
        print(f"  → {execution_plan['total_builders']} builder(s), "
              f"~{execution_plan['estimated_tokens']:,} tokens")
        for w in execution_plan.get("warnings", []):
            print(f"  ⚠ {w}")

    # Step 3: Compose prompt for primary builder
    primary_builder = builders[0]["builder_id"]
    if verbose:
        print(f"\n[3/4] Composing prompt for: {primary_builder}")
    prompt = compose(intent, primary_builder, quality)
    result["steps"].append({
        "step": "compose",
        "builder_id": primary_builder,
        "prompt_length": len(prompt),
        "prompt_tokens_est": len(prompt) // 4,
    })
    if verbose:
        print(f"  → {len(prompt):,} chars (~{len(prompt)//4:,} tokens)")

    # Step 4: Similar artifacts check (dedup)
    if verbose:
        print(f"\n[4/4] Checking for similar existing artifacts...")
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
                print(f"  ⚠ {len(dupes)} similar artifact(s) found:")
                for s in dupes:
                    print(f"    {s['score']:.3f} {s['path']}")
            else:
                print(f"  ✅ No duplicates detected")
    except Exception as e:
        result["steps"].append({"step": "dedup_check", "error": str(e)})

    result["elapsed_seconds"] = round(time.time() - t0, 2)
    result["primary_builder"] = primary_builder
    result["prompt"] = prompt if not dry_run else f"[DRY-RUN] {len(prompt)} chars"

    if verbose:
        print(f"\n{'='*60}")
        print(f"Done in {result['elapsed_seconds']}s")
        print(f"Builder: {primary_builder}")
        print(f"Prompt: {len(prompt):,} chars")
        if not dry_run:
            print(f"\nPrompt saved to: .cex/runtime/last_prompt.md")

    # Save prompt for consumption
    if not dry_run:
        prompt_path = ROOT / ".cex" / "runtime" / "last_prompt.md"
        prompt_path.parent.mkdir(parents=True, exist_ok=True)
        prompt_path.write_text(prompt, encoding="utf-8")

    return result


# ── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="CEX Run — Unified entry point: intent → plan → prompt",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python _tools/cex_run.py "create a knowledge card about RAG patterns"
  python _tools/cex_run.py "cria agente de vendas" --quality 9.5
  python _tools/cex_run.py "build webhook handler" --dry-run
  python _tools/cex_run.py --status
  python _tools/cex_run.py --discover "payment processing"
  python _tools/cex_run.py --plan "create agent for sales"
        """,
    )
    parser.add_argument("intent", nargs="?", help="Natural language intent")
    parser.add_argument("--quality", "-q", type=float, default=9.0,
                       help="Quality target (default: 9.0)")
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

    args = parser.parse_args()

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
    import logging
    if args.json:
        logging.disable(logging.WARNING)
        import io, contextlib
        with contextlib.redirect_stderr(io.StringIO()):
            result = run(args.intent, args.quality,
                        dry_run=args.dry_run, verbose=False)
    else:
        result = run(args.intent, args.quality,
                    dry_run=args.dry_run, verbose=True)

    if args.json:
        # Remove prompt from JSON output (too large)
        output = {k: v for k, v in result.items() if k != "prompt"}
        output["prompt_length"] = len(result.get("prompt", ""))
        print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
