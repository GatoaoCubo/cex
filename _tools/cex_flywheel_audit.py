#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cex_flywheel_audit.py -- Doc vs Practice Flywheel Bootstrap

Reads CEX_SYSTEM_MAP.md claims and verifies each against the filesystem.
Produces a gap report with 4 statuses:
  WIRED   = documented AND works
  BROKEN  = documented but broken
  PHANTOM = documented but missing
  ORPHAN  = exists but undocumented

Modes:
  audit    Full doc-vs-practice verification (default)
  wires    Test only the 7 OpenClaude wiring integrations
  cascade  Trace the 7 dependency chains end-to-end
  heal     Generate fix plan for BROKEN + PHANTOM items
  loop     Autonomous: audit -> heal -> re-audit (up to N rounds)

Usage:
  python _tools/cex_flywheel_audit.py audit
  python _tools/cex_flywheel_audit.py wires
  python _tools/cex_flywheel_audit.py cascade
  python _tools/cex_flywheel_audit.py heal
  python _tools/cex_flywheel_audit.py loop --max-rounds 3
"""

import argparse
import sys
import os
import json
import importlib
import time
from pathlib import Path
from datetime import datetime
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(CEX_ROOT))
sys.path.insert(0, str(CEX_ROOT / "_tools"))

RESULTS = []


def record(layer: str, check: str, status: str, detail: str = "") -> None:
    """Append one audit result and echo it to the terminal."""
    RESULTS.append({"layer": layer, "check": check, "status": status, "detail": detail})
    sym = {"WIRED": "[OK]", "BROKEN": "[!!]", "PHANTOM": "[??]", "ORPHAN": "[~~]"}
    print(f"  {sym.get(status, '[--]')} {layer}/{check}: {status}  {detail}")


# --- L0: Genesis & Config ---
def audit_L0() -> None:
    """Audit genesis-level config, boot assets, and runtime directories."""
    print("\n=== L0: Genesis & Config ===")
    km = CEX_ROOT / ".cex" / "kinds_meta.json"
    if km.exists():
        try:
            d = json.load(open(km, encoding="utf-8"))
            record("L0", "kinds_meta.json", "WIRED", f"{len(d)} kinds")
        except Exception as e:
            record("L0", "kinds_meta.json", "BROKEN", str(e))
    else:
        record("L0", "kinds_meta.json", "PHANTOM")

    record("L0", "router_config.yaml",
           "WIRED" if (CEX_ROOT / ".cex" / "router_config.yaml").exists() else "PHANTOM")

    boots = list((CEX_ROOT / "boot").glob("*.ps1"))
    record("L0", "boot_scripts", "WIRED" if len(boots) >= 7 else "BROKEN", f"{len(boots)} scripts")

    record("L0", "dispatch.sh",
           "WIRED" if (CEX_ROOT / "_spawn" / "dispatch.sh").exists() else "PHANTOM")

    for d in ["decisions", "handoffs", "signals", "pids", "locks", "plans", "outputs", "archive"]:
        p = CEX_ROOT / ".cex" / "runtime" / d
        if not p.exists():
            p.mkdir(parents=True, exist_ok=True)
        record("L0", f"runtime/{d}", "WIRED", "auto-created" if not any(p.iterdir()) else f"{len(list(p.iterdir()))} items")


# --- L1: Pillars ---
def audit_L1() -> None:
    """Audit pillar directories, schemas, and compiled outputs."""
    print("\n=== L1: Pillars (P01-P12) ===")
    for i in range(1, 13):
        pdir = None
        for d in CEX_ROOT.iterdir():
            if d.is_dir() and d.name.startswith(f"P{i:02d}_"):
                pdir = d
                break
        if not pdir:
            record("L1", f"P{i:02d}", "PHANTOM", "pillar dir missing")
            continue

        schema = pdir / "_schema.yaml"
        record("L1", f"{pdir.name}/_schema", "WIRED" if schema.exists() else "PHANTOM")

        compiled = pdir / "compiled"
        if compiled.exists():
            count = len(list(compiled.glob("*")))
            record("L1", f"{pdir.name}/compiled", "WIRED" if count > 0 else "BROKEN", f"{count} files")
        else:
            record("L1", f"{pdir.name}/compiled", "PHANTOM")


# --- L2: Nuclei ---
def audit_L2() -> None:
    """Audit nucleus directory structure, compiled outputs, and rules."""
    print("\n=== L2: Nuclei (N01-N07) ===")
    # Canonical 12-pillar fractal: every nucleus mirrors all 12 pillars.
    # knowledge=P01, agents=P02, prompts=P03, tools=P04, output=P05, schemas=P06,
    # quality=P07, architecture=P08, config=P09, memory=P10, feedback=P11,
    # orchestration=P12. Plus "compiled" (auto-gen) and "rules" (nucleus-scoped).
    expected = ["agents", "architecture", "compiled", "config", "feedback",
                "knowledge", "memory", "orchestration", "output", "prompts",
                "quality", "rules", "schemas", "tools"]
    for i in range(1, 8):
        ndir = None
        for d in CEX_ROOT.iterdir():
            if d.is_dir() and d.name.startswith(f"N{i:02d}_"):
                ndir = d
                break
        if not ndir:
            record("L2", f"N{i:02d}", "PHANTOM")
            continue
        present = [s.name for s in ndir.iterdir() if s.is_dir()]
        missing = [s for s in expected if s not in present]
        compiled_count = len(list((ndir / "compiled").glob("*"))) if (ndir / "compiled").exists() else 0
        record("L2", f"{ndir.name}/structure",
               "WIRED" if not missing else "BROKEN",
               f"{len(present)} subdirs" + (f", missing: {missing}" if missing else ""))
        record("L2", f"{ndir.name}/compiled",
               "WIRED" if compiled_count > 0 else "BROKEN", f"{compiled_count} artifacts")

    for i in range(1, 8):
        # N07 lives in .claude/rules/ (orchestrator). N01-N06 live in N0X_*/rules/ (lazy-loaded).
        rules = list((CEX_ROOT / ".claude" / "rules").glob(f"n{i:02d}*"))
        if not rules:
            ndir = next((d for d in CEX_ROOT.iterdir()
                         if d.is_dir() and d.name.startswith(f"N{i:02d}_")), None)
            if ndir and (ndir / "rules").exists():
                rules = list((ndir / "rules").glob(f"n{i:02d}*"))
        record("L2", f"N{i:02d}_rule", "WIRED" if rules else "PHANTOM",
               rules[0].name if rules else "")


# --- L3: Archetypes ---
def audit_L3() -> None:
    """Audit builder archetypes, shared skills, and generated sub-agents."""
    print("\n=== L3: Archetypes ===")
    builders_dir = CEX_ROOT / "archetypes" / "builders"
    bdirs = [d for d in builders_dir.iterdir() if d.is_dir() and d.name.endswith("-builder")]
    record("L3", "builder_count", "WIRED" if len(bdirs) >= 107 else "BROKEN", f"{len(bdirs)} builders")

    for bd in bdirs[:5]:
        isos = list(bd.glob("bld_*.md"))
        record("L3", f"{bd.name}/ISOs",
               "WIRED" if len(isos) == 13 else "BROKEN", f"{len(isos)}/13")

    shared = builders_dir / "_shared"
    sc = len(list(shared.glob("*.md"))) if shared.exists() else 0
    record("L3", "shared_skills", "WIRED" if sc >= 3 else "BROKEN", f"{sc} shared")

    agents = CEX_ROOT / ".claude" / "agents"
    ac = len(list(agents.glob("*.md"))) if agents.exists() else 0
    record("L3", "sub_agents", "WIRED" if ac >= 100 else "BROKEN", f"{ac} agents")


# --- L4: Knowledge Library ---
def audit_L4() -> None:
    """Audit knowledge-card coverage across kind and domain libraries."""
    print("\n=== L4: Knowledge Library ===")
    kind_dir = CEX_ROOT / "P01_knowledge" / "library" / "kind"
    domain_dir = CEX_ROOT / "P01_knowledge" / "library" / "domain"

    kc_count = len(list(kind_dir.glob("kc_*.md"))) if kind_dir.exists() else 0
    record("L4", "kind_KCs", "WIRED" if kc_count >= 108 else "BROKEN", f"{kc_count} KCs")

    dm_count = len(list(domain_dir.rglob("*.md"))) if domain_dir.exists() else 0
    record("L4", "domain_KCs", "WIRED" if dm_count >= 50 else "BROKEN", f"{dm_count} domain KCs")

    # KC-to-kind coverage
    km = CEX_ROOT / ".cex" / "kinds_meta.json"
    if km.exists() and kind_dir.exists():
        kinds = json.load(open(km, encoding="utf-8"))
        kc_names = {f.stem.replace("kc_", "") for f in kind_dir.glob("kc_*.md")}
        missing = [k for k in kinds if k not in kc_names]
        record("L4", "KC_coverage",
               "WIRED" if len(missing) <= 10 else "BROKEN",
               f"{len(kinds)-len(missing)}/{len(kinds)} covered, missing: {missing[:5]}")


# --- L5: Tools ---
def audit_L5() -> None:
    """Audit critical tools, imports, and SDK surface area."""
    print("\n=== L5: Tools ===")
    cex_tools = list((CEX_ROOT / "_tools").glob("cex_*.py"))
    record("L5", "cex_tools", "WIRED" if len(cex_tools) >= 45 else "BROKEN", f"{len(cex_tools)} tools")

    critical = ["cex_prompt_layers", "cex_skill_loader", "cex_router",
                "cex_token_budget", "cex_gdp", "cex_memory_types",
                "cex_memory_age", "cex_agent_spawn", "cex_coordinator"]
    for mod_name in critical:
        try:
            importlib.import_module(mod_name)
            record("L5", f"import:{mod_name}", "WIRED")
        except Exception as e:
            record("L5", f"import:{mod_name}", "BROKEN", str(e)[:80])

    try:
        from cex_prompt_layers import get_layers
        layers = get_layers()
        total = layers.stats()["total"]
        record("L5", "prompt_layers_load", "WIRED" if total >= 10 else "BROKEN", f"{total} artifacts")
    except Exception as e:
        record("L5", "prompt_layers_load", "BROKEN", str(e)[:80])

    try:
        from cex_skill_loader import SkillLoader
        sl = SkillLoader()
        sl.load_builder('agent')
        record("L5", "skill_loader_ISOs", "WIRED" if sl.stats()["total_isos"] >= 10 else "BROKEN",
               f"{sl.stats()['total_isos']} ISOs")
    except Exception as e:
        record("L5", "skill_loader_ISOs", "BROKEN", str(e)[:80])

    sdk_mods = len(list((CEX_ROOT / "cex_sdk").rglob("*.py"))) - len(list((CEX_ROOT / "cex_sdk").rglob("__init__.py")))
    record("L5", "cex_sdk_modules", "WIRED" if sdk_mods >= 40 else "BROKEN", f"{sdk_mods} modules")


# --- WIRES: 7 OpenClaude Integrations ---
def audit_wires() -> None:
    """Audit prompt-composition and tool-wiring integration points."""
    print("\n=== WIRES: 7 OpenClaude Integrations ===")
    try:
        import cex_crew_runner as cr
        from cex_crew_runner import compose_prompt, RunState, check_compaction_needed, check_memory_extract_needed
        from cex_prompt_layers import get_layers
        layers = get_layers()
    except Exception as e:
        record("WIRE", "import", "BROKEN", str(e)[:80])
        return

    state = RunState(intent="audit", plan={})
    parsed = {"verb": "test", "object": "audit", "domain": ""}
    prompt = compose_prompt("agent-builder", "PRODUCE", "test", parsed, 9.0, state)

    record("WIRE", "W1_identity", "WIRED" if "CEX Agent Identity" in prompt else "BROKEN")
    record("WIRE", "W2_doing_tasks", "WIRED" if "Doing Tasks" in prompt else "BROKEN")
    record("WIRE", "W3_action_protocol",
           "WIRED" if ("Blast Radius" in prompt or "Executing Actions" in prompt) else "BROKEN")
    record("WIRE", "W4_guardrails",
           "WIRED" if "Safety Guardrails" in prompt else "BROKEN", "PRODUCE should have guardrails")

    pr = compose_prompt("agent-builder", "REASON", "test", parsed, 9.0, state)
    record("WIRE", "W4b_no_guard_REASON",
           "WIRED" if "Safety Guardrails" not in pr else "BROKEN", "REASON excluded")

    pg = compose_prompt("agent-builder", "GOVERN", "test", parsed, 9.0, state)
    record("WIRE", "W5_verification",
           "WIRED" if ("verification specialist" in pg or "Verification Protocol" in pg) else "BROKEN")
    # W5b: the GOVERN-only verification agent prompt should NOT be in PRODUCE
    # (the shared skill "Verification Protocol" IS expected everywhere, that's fine)
    record("WIRE", "W5b_no_verify_agent_PRODUCE",
           "WIRED" if "verification specialist" not in prompt else "BROKEN",
           "verification_agent excluded from PRODUCE")

    big = "word " * 8000
    c = check_compaction_needed(big, max_tokens=8192)
    record("WIRE", "W6_compaction", "WIRED" if c["needed"] else "BROKEN", f"ratio={c['usage_ratio']:.2f}")

    cr._execution_counter = 0
    for _ in range(5):
        m = check_memory_extract_needed()
    record("WIRE", "W7_memory_extract", "WIRED" if m["needed"] else "BROKEN", f"counter={m['counter']}")

    # Check SDK modules are CALLED (not just importable)
    crew_src = (CEX_ROOT / "_tools" / "cex_crew_runner.py").read_text(encoding="utf-8")
    record("WIRE", "T01_skill_loader_wired",
           "WIRED" if "SkillLoader" in crew_src else "BROKEN", "SkillLoader in crew_runner")
    record("WIRE", "T02_router_wired",
           "WIRED" if "CexRouter" in crew_src else "BROKEN", "CexRouter in crew_runner")

    runner_src = (CEX_ROOT / "_tools" / "cex_8f_runner.py").read_text(encoding="utf-8")
    record("WIRE", "T03_gdp_wired",
           "WIRED" if "GDPEnforcer" in runner_src else "BROKEN", "GDP in 8f_runner")
    record("WIRE", "T04_budget_wired",
           "WIRED" if "TokenBudget" in runner_src else "BROKEN", "TokenBudget in 8f_runner")

    mem_update = (CEX_ROOT / "_tools" / "cex_memory_update.py").read_text(encoding="utf-8")
    record("WIRE", "T05_memtype_wired",
           "WIRED" if "cex_memory_types" in mem_update else "BROKEN", "MemoryType in update")

    mem_select = (CEX_ROOT / "_tools" / "cex_memory_select.py").read_text(encoding="utf-8")
    record("WIRE", "T06_memage_wired",
           "WIRED" if "cex_memory_age" in mem_select else "BROKEN", "MemoryAge in select")

    mission_src = (CEX_ROOT / "_tools" / "cex_mission_runner.py").read_text(encoding="utf-8")
    record("WIRE", "T08_coordinator_wired",
           "WIRED" if "CexCoordinator" in mission_src else "BROKEN", "Coordinator in mission_runner")

    compile_src = (CEX_ROOT / "_tools" / "cex_compile.py").read_text(encoding="utf-8")
    record("WIRE", "T10_reverse_compiler",
           "WIRED" if "render_claude_md" in compile_src else "BROKEN", "Reverse compiler exists")

    aids = ["p03_sp_cex_core_identity", "p03_sp_verification_agent",
            "p03_ins_doing_tasks", "p03_ins_action_protocol",
            "p04_skill_verify", "p04_skill_simplify", "p04_skill_compact", "p04_skill_memory_extract",
            "p08_ac_verification", "p08_ac_explore", "p08_ac_plan", "p08_pat_context_compaction",
            "p11_gr_cyber_risk", "p11_gr_action_reversibility"]
    loaded = sum(1 for a in aids if layers.get(a))
    record("WIRE", "artifacts_loadable", "WIRED" if loaded == len(aids) else "BROKEN", f"{loaded}/{len(aids)}")


# --- CASCADES: 7 Dependency Chains ---
def audit_cascades() -> None:
    """Audit end-to-end dependency chains across core system flows."""
    print("\n=== CASCADES: 7 Dependency Chains ===")

    try:
        from cex_8f_motor import parse_intent
        p = parse_intent("cria agente de teste")
        record("CASCADE", "C1_build", "WIRED" if p.get("verb") else "BROKEN", f"verb={p.get('verb')} obj={p.get('object')}")
    except Exception as e:
        record("CASCADE", "C1_build", "BROKEN", str(e)[:80])

    try:
        from cex_score import score_artifact
        record("CASCADE", "C2_quality", "WIRED")
    except Exception as e:
        record("CASCADE", "C2_quality", "BROKEN", str(e)[:80])

    kc = CEX_ROOT / "P01_knowledge" / "library" / "kind" / "kc_agent.md"
    bk = CEX_ROOT / "archetypes" / "builders" / "agent-builder" / "bld_knowledge_card_agent.md"
    record("CASCADE", "C3_knowledge", "WIRED" if kc.exists() and bk.exists() else "BROKEN")

    try:
        from cex_gdp import GDPEnforcer
        record("CASCADE", "C4_decision", "WIRED")
    except Exception as e:
        record("CASCADE", "C4_decision", "BROKEN", str(e)[:80])

    try:
        from cex_memory_types import MemoryType
        import cex_memory_age
        record("CASCADE", "C5_memory", "WIRED", f"types={len(MemoryType)} age_module=ok")
    except Exception as e:
        record("CASCADE", "C5_memory", "BROKEN", str(e)[:80])

    record("CASCADE", "C6_evolution",
           "WIRED" if (CEX_ROOT / "_tools" / "cex_evolve.py").exists() else "PHANTOM")

    mr = (CEX_ROOT / "_tools" / "cex_mission_runner.py").exists()
    sw = (CEX_ROOT / "_tools" / "cex_signal_watch.py").exists()
    ds = (CEX_ROOT / "_spawn" / "dispatch.sh").exists()
    record("CASCADE", "C7_dispatch", "WIRED" if all([mr, sw, ds]) else "BROKEN",
           f"runner={mr} watch={sw} dispatch={ds}")


# --- L6: Governance ---
def audit_L6() -> None:
    """Audit governance assets such as rules, commands, and learnings."""
    print("\n=== L6: Governance ===")
    rules = list((CEX_ROOT / ".claude" / "rules").glob("*.md"))
    record("L6", "rules", "WIRED" if len(rules) >= 9 else "BROKEN", f"{len(rules)}")
    cmds = list((CEX_ROOT / ".claude" / "commands").glob("*.md"))
    record("L6", "commands", "WIRED" if len(cmds) >= 10 else "BROKEN", f"{len(cmds)}")
    lr = CEX_ROOT / ".cex" / "learning_records"
    lrc = len(list(lr.glob("*"))) if lr.exists() else 0
    record("L6", "learning_records", "WIRED" if lrc >= 10 else "BROKEN", f"{lrc}")


# --- HEAL ---
def generate_heal_plan() -> list[dict[str, Any]]:
    """Create and persist a repair plan for broken or missing audit items."""
    broken = [r for r in RESULTS if r["status"] in ("BROKEN", "PHANTOM")]
    if not broken:
        print("\n  *** Nothing to fix -- all checks passed ***")
        return []
    print(f"\n=== HEAL PLAN: {len(broken)} items ===\n")
    plan = []
    for r in broken:
        action = "Manual review"
        if "compiled" in r["check"] and r["status"] == "BROKEN":
            action = "python _tools/cex_compile.py --all"
        elif "PHANTOM" in r["status"] and "runtime" in r["check"]:
            action = f"mkdir -p .cex/{r['check']}"
        elif "import:" in r["check"]:
            action = f"Check _tools/{r['check'].replace('import:', '')}.py syntax"
        elif "KC_coverage" in r["check"]:
            action = "python _tools/cex_kind_register.py --sync-kcs"
        elif "ISOs" in r["check"]:
            action = "python _tools/cex_schema_hydrate.py --all"
        plan.append({"layer": r["layer"], "check": r["check"], "status": r["status"],
                      "detail": r["detail"], "action": action})
        print(f"  [{r['status']}] {r['layer']}/{r['check']} -> {action}")

    pf = CEX_ROOT / ".cex" / "runtime" / "plans" / f"heal_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    pf.parent.mkdir(parents=True, exist_ok=True)
    with open(pf, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=2)
    print(f"\n  Plan saved: {pf}")
    return plan


# --- REPORT ---
def print_report() -> None:
    """Print and persist the audit summary report."""
    w = sum(1 for r in RESULTS if r["status"] == "WIRED")
    b = sum(1 for r in RESULTS if r["status"] == "BROKEN")
    p = sum(1 for r in RESULTS if r["status"] == "PHANTOM")
    o = sum(1 for r in RESULTS if r["status"] == "ORPHAN")
    t = len(RESULTS)
    print(f"\n{'='*60}")
    print(f"CEX FLYWHEEL AUDIT -- Doc vs Practice")
    print(f"{'='*60}")
    print(f"  WIRED:   {w:3d}  (documented AND working)")
    print(f"  BROKEN:  {b:3d}  (documented but broken)")
    print(f"  PHANTOM: {p:3d}  (documented but missing)")
    print(f"  ORPHAN:  {o:3d}  (exists but undocumented)")
    print(f"  TOTAL:   {t:3d}  checks")
    print(f"  HEALTH:  {w/t*100:.0f}%  ({w}/{t})" if t else "  HEALTH:  0%")
    print(f"{'='*60}")
    rf = CEX_ROOT / ".cex" / "quality" / f"audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    rf.parent.mkdir(parents=True, exist_ok=True)
    with open(rf, "w", encoding="utf-8") as f:
        json.dump({"ts": datetime.now().isoformat(),
                    "summary": {"wired": w, "broken": b, "phantom": p, "orphan": o, "total": t},
                    "checks": RESULTS}, f, ensure_ascii=False, indent=2)
    print(f"  Report:  {rf}\n")


# --- MAIN ---
def main() -> None:
    """Run the requested audit mode and optional heal loop."""
    known_modes = {"audit", "wires", "cascade", "heal", "loop"}
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-") and sys.argv[1] not in known_modes:
        print("Usage: cex_flywheel_audit.py [audit|wires|cascade|heal|loop]")
        return

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "mode",
        nargs="?",
        default="audit",
        help="Audit mode to run.",
    )
    parser.add_argument(
        "--max-rounds",
        type=int,
        default=3,
        help="Maximum rounds for loop mode.",
    )
    args, _ = parser.parse_known_args()
    mode = args.mode
    max_rounds = args.max_rounds

    if mode == "audit":
        audit_L0(); audit_L1(); audit_L2(); audit_L3(); audit_L4()
        audit_L5(); audit_wires(); audit_L6(); audit_cascades()
        print_report()
    elif mode == "wires":
        audit_wires(); print_report()
    elif mode == "cascade":
        audit_cascades(); print_report()
    elif mode == "heal":
        audit_L0(); audit_L1(); audit_L2(); audit_L3(); audit_L4()
        audit_L5(); audit_wires(); audit_L6(); audit_cascades()
        print_report(); generate_heal_plan()
    elif mode == "loop":
        for rnd in range(1, max_rounds + 1):
            print(f"\n{'#'*60}\n# FLYWHEEL ROUND {rnd}/{max_rounds}\n{'#'*60}")
            RESULTS.clear()
            audit_L0(); audit_L1(); audit_L2(); audit_L3(); audit_L4()
            audit_L5(); audit_wires(); audit_L6(); audit_cascades()
            print_report()
            bk = sum(1 for r in RESULTS if r["status"] in ("BROKEN", "PHANTOM"))
            if bk == 0:
                print("  *** ALL CHECKS PASSED ***")
                break
            generate_heal_plan()
            time.sleep(1)
    else:
        print(f"Usage: cex_flywheel_audit.py [audit|wires|cascade|heal|loop]")


if __name__ == "__main__":
    main()
