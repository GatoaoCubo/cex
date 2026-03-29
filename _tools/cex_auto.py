#!/usr/bin/env python3
"""CEX Auto: Autonomous intent-to-artifact pipeline.
Chains: Motor (decompose) -> Runner (build) -> Save -> Index -> Validate
Usage:
    python _tools/cex_auto.py "create a knowledge card about RAG"
    python _tools/cex_auto.py "build agent" --nucleus N01
    python _tools/cex_auto.py --list-kinds
"""
import argparse, json, subprocess, sys
from pathlib import Path

CEX_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(CEX_ROOT / "_tools"))

NUCLEUS_FOR_DOMAIN = {
    "research": "N01_intelligence", "intelligence": "N01_intelligence",
    "marketing": "N02_marketing", "copy": "N02_marketing",
    "engineering": "N03_engineering", "build": "N03_engineering",
    "knowledge": "N04_knowledge", "indexing": "N04_knowledge",
    "operations": "N05_operations", "deploy": "N05_operations",
    "commercial": "N06_commercial", "monetization": "N06_commercial",
    "admin": "N07_admin", "orchestration": "N07_admin",
}

KIND_TO_SUBDIR = {
    "agent_card": "architecture", "agent": "agents", "system_prompt": "prompts",
    "dispatch_rule": "orchestration", "knowledge_card": "knowledge",
    "workflow": "orchestration", "quality_gate": "feedback",
    "rag_source": "knowledge", "chunk_strategy": "knowledge",
    "prompt_template": "prompts", "skill": "tools",
    "scoring_rubric": "quality", "few_shot_example": "quality",
    "pattern": "architecture", "signal": "orchestration",
    "dag": "orchestration", "spawn_config": "orchestration",
    "learning_record": "memory", "boot_config": "config",
    "response_format": "output", "health_check": "feedback",
}

def motor_decompose(intent):
    from cex_8f_motor import parse_intent, classify_objects
    parsed = parse_intent(intent)
    classified = classify_objects(parsed["objects"])
    if not classified:
        return {"error": f"No kind for: {parsed['objects']}"}
    return {"kind": classified[0]["kind"], "pillar": classified[0]["pillar"],
            "domain": parsed.get("domain", "generic"), "intent": intent}

def runner_build(kind, context="", dry_run=False, output_dir=None):
    cmd = [sys.executable, str(CEX_ROOT / "_tools" / "cex_8f_runner.py"), "--kind", kind]
    if context: cmd.extend(["--context", context])
    if dry_run: cmd.append("--dry-run")
    if output_dir: cmd.extend(["--output-dir", output_dir])
    r = subprocess.run(cmd, cwd=str(CEX_ROOT), capture_output=True, text=True)
    return {"success": "PASS" in r.stdout, "output": r.stdout[-300:]}

def resolve_output(kind, nucleus=None, domain=None):
    nuc_dir = None
    if nucleus:
        m = list(CEX_ROOT.glob(f"{nucleus}*"))
        if m: nuc_dir = m[0]
    elif domain:
        n = NUCLEUS_FOR_DOMAIN.get(domain.lower())
        if n: nuc_dir = CEX_ROOT / n
    sub = KIND_TO_SUBDIR.get(kind, "output")
    return (nuc_dir / sub) if nuc_dir else (CEX_ROOT / "_output")

def main():
    ap = argparse.ArgumentParser(description="CEX Auto: intent to artifact")
    ap.add_argument("intent", nargs="?", help="Natural language intent")
    ap.add_argument("--nucleus", help="Target nucleus (N01-N07)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--context", default="")
    ap.add_argument("--list-kinds", action="store_true")
    args = ap.parse_args()

    if args.list_kinds:
        from cex_8f_motor import OBJECT_TO_KINDS
        for k in sorted(OBJECT_TO_KINDS.keys()):
            v = OBJECT_TO_KINDS[k]
            kinds = [x[0] if isinstance(x, tuple) else x for x in v]
            print(f"  {k:25s} -> {', '.join(kinds)}")
        return

    if not args.intent:
        ap.error("Provide intent or --list-kinds")

    print("  [1/3] MOTOR: decomposing...")
    d = motor_decompose(args.intent)
    if "error" in d:
        print(f"  ERROR: {d['error']}"); sys.exit(1)
    kind, domain = d["kind"], d["domain"]
    print(f"         Kind={kind} Pillar={d['pillar']} Domain={domain}")

    out = resolve_output(kind, args.nucleus, domain)
    out.mkdir(parents=True, exist_ok=True)
    print(f"         Output: {out.relative_to(CEX_ROOT)}")

    print(f"  [2/3] RUNNER: building {kind}...")
    ctx = args.context or args.intent
    r = runner_build(kind, ctx, args.dry_run, str(out))
    print(f"         {'PASS' if r['success'] else 'FAIL'}")

    print(f"  [3/3] DONE: {kind} -> {out.relative_to(CEX_ROOT)}/")

if __name__ == "__main__":
    main()
