#!/usr/bin/env python3
"""cex_fractal_fill.py -- Gap audit for the 8 x 12 nucleus/pillar matrix.

For every (nucleus, pillar) pair, this tool:
  1. Scans the pillar dir for .md artifacts
  2. Parses frontmatter to resolve each artifact's `kind`
  3. Compares with the canonical kind list for that pillar (kinds_meta.json)
  4. Emits a gap matrix + prioritized fill list

No dispatch. Read-only audit. Output:
  - stdout: coverage matrix (rows=nuclei, cols=pillars, cells=present/total)
  - --detail: per-nucleus gap list sorted by (core-first, pillar-order)
  - --json:   machine-readable gap report to .cex/P07_evals/fractal_fill_*.json

Usage:
  python _tools/cex_fractal_fill.py                 # summary matrix
  python _tools/cex_fractal_fill.py --detail        # + per-nucleus gap list
  python _tools/cex_fractal_fill.py --nucleus n06   # focus one nucleus
  python _tools/cex_fractal_fill.py --json out.json # dump machine report
  python _tools/cex_fractal_fill.py --core-only     # gaps for core kinds only
  python _tools/cex_fractal_fill.py --plan          # emit fill plan (core+affinity
                                                    #   minus per-nucleus exclusions)
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Pillar subdir -> canonical pillar id
PILLAR_SUBDIRS = [
    ("knowledge", "P01"),
    ("agents", "P02"),
    ("prompts", "P03"),
    ("tools", "P04"),
    ("output", "P05"),
    ("schemas", "P06"),
    ("quality", "P07"),
    ("architecture", "P08"),
    ("config", "P09"),
    ("memory", "P10"),
    ("feedback", "P11"),
    ("orchestration", "P12"),
]

NUCLEI = [
    "N00_genesis",
    "N01_intelligence",
    "N02_marketing",
    "N03_engineering",
    "N04_knowledge",
    "N05_operations",
    "N06_commercial",
    "N07_admin",
]

# Sin lens per nucleus (for priority hints in --detail output)
SIN = {
    "N00_genesis":      "pre-sin archetype",
    "N01_intelligence": "Analytical Envy",
    "N02_marketing":    "Creative Lust",
    "N03_engineering":  "Inventive Pride",
    "N04_knowledge":    "Knowledge Gluttony",
    "N05_operations":   "Gating Wrath",
    "N06_commercial":   "Strategic Greed",
    "N07_admin":        "Orchestrating Sloth",
}

# Sin affinity: which kinds are "on sin" for each nucleus (bonus priority).
# Keep narrow -- only kinds that obviously align.
SIN_AFFINITY: dict[str, set[str]] = {
    "N01_intelligence": {
        "knowledge_card", "research_pipeline", "citation", "benchmark",
        "competitive_matrix", "analyst_briefing", "ontology",
    },
    "N02_marketing": {
        "landing_page", "tagline", "press_release", "prompt_template",
        "social_publisher", "multimodal_prompt", "onboarding_flow",
    },
    "N03_engineering": {
        "agent", "system_prompt", "skill", "workflow", "pattern",
        "chain", "interface", "function_def",
    },
    "N04_knowledge": {
        "knowledge_card", "knowledge_index", "knowledge_graph",
        "chunk_strategy", "retriever", "rag_source", "embedding_config",
        "entity_memory", "memory_summary",
    },
    "N05_operations": {
        "quality_gate", "e2e_eval", "unit_eval", "smoke_eval",
        "env_config", "secret_config", "incident_report",
        "rate_limit_config", "feature_flag",
    },
    "N06_commercial": {
        "content_monetization", "subscription_tier", "pricing_page",
        "sales_playbook", "customer_segment", "roi_calculator",
        "referral_program", "expansion_play", "nps_survey",
    },
    "N07_admin": {
        "workflow", "dispatch_rule", "schedule", "crew_template",
        "role_assignment", "capability_registry", "team_charter",
        "dag", "handoff_protocol",
    },
}

# Per-nucleus kind EXCLUSIONS (applicability filter for --plan).
# A kind is excluded when it's semantically irrelevant to the nucleus's
# domain. N03 owns build/training/voice infra; other nuclei don't need
# their own copies of those kinds. Keep conservative -- better to keep
# a borderline kind than lose coverage.
EXCLUSIONS: dict[str, set[str]] = {
    "N00_genesis": set(),  # archetype: gets everything (template stubs)
    "N01_intelligence": {
        "rl_algorithm", "reward_model", "reward_signal", "finetune_config",
        "quantization_config", "tts_provider", "stt_provider", "vad_config",
        "prosody_config", "voice_pipeline", "realtime_session", "audio_tool",
        "code_executor", "sandbox_spec", "sandbox_config",
        "c2pa_manifest", "prosody_config",
    },
    "N02_marketing": {
        "rl_algorithm", "reward_model", "reward_signal", "finetune_config",
        "quantization_config", "code_executor", "sandbox_spec", "sandbox_config",
        "tts_provider", "stt_provider", "vad_config", "prosody_config",
        "voice_pipeline", "realtime_session", "audio_tool",
        "model_architecture", "training_method", "rl_algorithm",
    },
    "N03_engineering": {
        # N03 is build-central; almost nothing is off-limits. Only remove
        # clearly commercial-domain kinds.
        "subscription_tier", "pricing_page", "sales_playbook",
        "customer_segment", "roi_calculator", "referral_program",
        "expansion_play", "nps_survey", "churn_prevention_playbook",
        "cohort_analysis", "renewal_workflow", "content_monetization",
    },
    "N04_knowledge": {
        "rl_algorithm", "reward_model", "reward_signal", "finetune_config",
        "quantization_config", "tts_provider", "stt_provider", "vad_config",
        "prosody_config", "voice_pipeline", "realtime_session", "audio_tool",
        "subscription_tier", "pricing_page", "sales_playbook",
        "customer_segment", "roi_calculator", "referral_program",
        "expansion_play", "nps_survey", "churn_prevention_playbook",
    },
    "N05_operations": {
        "rl_algorithm", "reward_model", "finetune_config",
        "tagline", "press_release", "landing_page", "pitch_deck",
        "subscription_tier", "pricing_page", "sales_playbook",
        "customer_segment", "roi_calculator", "referral_program",
        "expansion_play", "nps_survey", "churn_prevention_playbook",
    },
    "N06_commercial": {
        "rl_algorithm", "reward_model", "reward_signal", "finetune_config",
        "quantization_config", "code_executor", "sandbox_spec", "sandbox_config",
        "tts_provider", "stt_provider", "vad_config", "prosody_config",
        "voice_pipeline", "realtime_session", "audio_tool",
        "model_architecture", "training_method",
    },
    "N07_admin": {
        "rl_algorithm", "reward_model", "reward_signal", "finetune_config",
        "quantization_config", "tts_provider", "stt_provider", "vad_config",
        "prosody_config", "voice_pipeline", "realtime_session", "audio_tool",
        "model_architecture", "training_method",
        "tagline", "press_release", "landing_page",
        "subscription_tier", "pricing_page", "sales_playbook",
        "customer_segment", "referral_program", "expansion_play",
        "nps_survey", "churn_prevention_playbook",
    },
}


def load_kinds_meta() -> dict:
    path = ROOT / ".cex" / "kinds_meta.json"
    return json.loads(path.read_text(encoding="utf-8"))


def kinds_by_pillar(meta: dict) -> dict[str, list[str]]:
    """Group kind names by pillar id (e.g. 'P01' -> ['knowledge_card', ...])."""
    grouped: dict[str, list[str]] = {}
    for kname, kmeta in meta.items():
        p = kmeta.get("pillar")
        if p:
            grouped.setdefault(p, []).append(kname)
    for p in grouped:
        grouped[p].sort()
    return grouped


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_kind(path: Path) -> str | None:
    """Extract `kind:` from YAML frontmatter. Returns None if absent."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    for line in m.group(1).splitlines():
        line = line.strip()
        if line.startswith("kind:"):
            val = line.split(":", 1)[1].strip().strip('"').strip("'")
            return val or None
    return None


def scan_pillar(nucleus_dir: Path, pillar_subdir: str) -> dict[str, int]:
    """Return {kind: count} for all .md artifacts in {nucleus}/{pillar_subdir}."""
    counts: dict[str, int] = {}
    pdir = nucleus_dir / pillar_subdir
    if not pdir.exists():
        return counts
    for p in pdir.glob("*.md"):
        if p.name.lower() == "readme.md":
            continue
        kind = parse_kind(p)
        if kind:
            counts[kind] = counts.get(kind, 0) + 1
    return counts


def build_matrix(meta: dict, core_only: bool = False) -> dict:
    """Build the gap matrix for all nuclei x pillars."""
    pillar_kinds = kinds_by_pillar(meta)
    if core_only:
        pillar_kinds = {
            p: [k for k in kinds if meta[k].get("core")]
            for p, kinds in pillar_kinds.items()
        }

    result: dict = {"nuclei": {}, "totals": {}}
    for n in NUCLEI:
        ndir = ROOT / n
        if not ndir.exists():
            continue
        node: dict = {"sin": SIN.get(n, ""), "pillars": {}}
        for subdir, pid in PILLAR_SUBDIRS:
            canonical = set(pillar_kinds.get(pid, []))
            present = scan_pillar(ndir, subdir)
            present_kinds = set(present.keys()) & canonical
            # track unknown kinds (frontmatter `kind:` that isn't in the pillar's canonical list)
            unknown = sorted(k for k in present if k not in canonical)
            missing = sorted(canonical - present_kinds)
            node["pillars"][pid] = {
                "subdir": subdir,
                "canonical_count": len(canonical),
                "present_count": len(present_kinds),
                "present_kinds": sorted(present_kinds),
                "missing_kinds": missing,
                "unknown_kinds": unknown,
                "coverage": (
                    round(len(present_kinds) / len(canonical), 2)
                    if canonical else 1.0
                ),
            }
        result["nuclei"][n] = node

    # global totals per pillar
    for _, pid in PILLAR_SUBDIRS:
        canonical_total = len(pillar_kinds.get(pid, []))
        sum_present = sum(
            result["nuclei"][n]["pillars"][pid]["present_count"]
            for n in result["nuclei"]
        )
        result["totals"][pid] = {
            "canonical_per_nucleus": canonical_total,
            "sum_present_across_nuclei": sum_present,
            "max_possible": canonical_total * len(result["nuclei"]),
        }
    return result


def render_matrix(matrix: dict) -> str:
    """Plain-text coverage matrix: rows=nuclei, cols=pillars, cells=N/T."""
    lines = []
    header = ["nucleus       "] + [pid for _, pid in PILLAR_SUBDIRS] + ["  avg"]
    lines.append(" | ".join(f"{h:>6}" if h != header[0] else h for h in header))
    lines.append("-" * len(lines[0]))
    for n, node in matrix["nuclei"].items():
        cells = []
        covs = []
        for _, pid in PILLAR_SUBDIRS:
            p = node["pillars"][pid]
            cells.append(f"{p['present_count']:>2}/{p['canonical_count']:<2}")
            covs.append(p["coverage"])
        avg = sum(covs) / len(covs) if covs else 0
        row = f"{n:<14}| " + " | ".join(f"{c:>5}" for c in cells) + f" | {avg:>5.0%}"
        lines.append(row)

    # totals row
    total_cells = []
    total_covs = []
    for _, pid in PILLAR_SUBDIRS:
        t = matrix["totals"][pid]
        total_cells.append(
            f"{t['sum_present_across_nuclei']:>2}/{t['max_possible']:<2}"
        )
        if t["max_possible"]:
            total_covs.append(
                t["sum_present_across_nuclei"] / t["max_possible"]
            )
    lines.append("-" * len(lines[0]))
    total_avg = sum(total_covs) / len(total_covs) if total_covs else 0
    lines.append(
        f"{'TOTAL':<14}| "
        + " | ".join(f"{c:>5}" for c in total_cells)
        + f" | {total_avg:>5.0%}"
    )
    return "\n".join(lines)


def render_gaps(matrix: dict, meta: dict, focus: str | None = None) -> str:
    """Per-nucleus gap list, core-kinds first, then sin-affinity, then alpha."""
    lines = []
    for n, node in matrix["nuclei"].items():
        if focus and not n.lower().startswith(focus.lower()):
            continue
        affinity = SIN_AFFINITY.get(n, set())
        lines.append(f"\n== {n}  ({node['sin']}) ==")
        for _, pid in PILLAR_SUBDIRS:
            p = node["pillars"][pid]
            if not p["missing_kinds"]:
                continue
            sortkey = lambda k: (
                not meta.get(k, {}).get("core", False),  # core first (False sorts before True... wait)
                k not in affinity,                        # affinity next
                k,                                        # alpha
            )
            # Fix: want core=True to sort BEFORE core=False, so invert
            sortkey = lambda k: (
                0 if meta.get(k, {}).get("core", False) else 1,
                0 if k in affinity else 1,
                k,
            )
            sorted_missing = sorted(p["missing_kinds"], key=sortkey)
            lines.append(
                f"  {pid} {p['subdir']:<14} "
                f"[{p['present_count']}/{p['canonical_count']}]  "
                f"missing: {len(sorted_missing)}"
            )
            for k in sorted_missing:
                core = "*" if meta.get(k, {}).get("core") else " "
                affn = "!" if k in affinity else " "
                desc = meta.get(k, {}).get("description", "")[:60]
                lines.append(f"      {core}{affn} {k:<36} {desc}")
            if p["unknown_kinds"]:
                lines.append(
                    "      [?] unknown kinds in this pillar dir: "
                    f"{', '.join(p['unknown_kinds'])}"
                )
    if not lines:
        return "(no gaps found)"
    lines.append("")
    lines.append("Legend:  * = core kind (priority)   ! = sin-affinity (priority)")
    return "\n".join(lines)


def build_plan(meta: dict, focus_nucleus: str | None = None) -> dict:
    """Build a fill plan: per-nucleus applicable kinds minus what's already present.

    Applicability rule per (nucleus, pillar):
        applicable = core_kinds(pillar) + sin_affinity(nucleus)
        applicable -= EXCLUSIONS[nucleus]
    Every nucleus always has all 12 pillar dirs; only the KINDS inside vary.

    Returns:
        {
          "nuclei": {
            "N06_commercial": {
              "sin": "Strategic Greed",
              "applicable_total": 48,
              "present_total": 14,
              "to_create_total": 34,
              "pillars": {
                "P01": {"applicable": [...], "present": [...], "missing": [...]},
                ...
              }
            }
          },
          "grand_total_to_create": 234
        }
    """
    pillar_kinds = kinds_by_pillar(meta)
    out: dict = {"nuclei": {}, "grand_total_to_create": 0}

    for n in NUCLEI:
        if focus_nucleus and not n.lower().startswith(focus_nucleus.lower()):
            continue
        ndir = ROOT / n
        if not ndir.exists():
            continue
        excl = EXCLUSIONS.get(n, set())
        affinity = SIN_AFFINITY.get(n, set())
        node: dict = {
            "sin": SIN.get(n, ""),
            "applicable_total": 0,
            "present_total": 0,
            "to_create_total": 0,
            "pillars": {},
        }
        for subdir, pid in PILLAR_SUBDIRS:
            core_kinds = [
                k for k in pillar_kinds.get(pid, [])
                if meta[k].get("core")
            ]
            # applicable = core + affinity kinds that belong to this pillar
            applicable = set(core_kinds)
            for k in affinity:
                if meta.get(k, {}).get("pillar") == pid:
                    applicable.add(k)
            applicable -= excl

            present_counts = scan_pillar(ndir, subdir)
            present = set(present_counts.keys()) & applicable
            missing = sorted(applicable - present)

            node["pillars"][pid] = {
                "subdir": subdir,
                "applicable": sorted(applicable),
                "present": sorted(present),
                "missing": missing,
                "missing_count": len(missing),
            }
            node["applicable_total"] += len(applicable)
            node["present_total"] += len(present)
            node["to_create_total"] += len(missing)

        out["nuclei"][n] = node
        out["grand_total_to_create"] += node["to_create_total"]

    return out


def render_plan(plan: dict, meta: dict, verbose: bool = False) -> str:
    """Human-readable plan: per-nucleus tally + optional per-kind list."""
    lines = []
    lines.append("=== Fractal Fill PLAN  (core + sin-affinity minus exclusions) ===")
    lines.append("")
    lines.append(f"{'nucleus':<18} {'sin':<24} {'present':>8} {'applicable':>11} {'to_create':>10} {'cov':>6}")
    lines.append("-" * 82)
    for n, node in plan["nuclei"].items():
        cov = node["present_total"] / node["applicable_total"] if node["applicable_total"] else 0
        lines.append(
            f"{n:<18} {node['sin']:<24} "
            f"{node['present_total']:>8} {node['applicable_total']:>11} "
            f"{node['to_create_total']:>10} {cov:>5.0%}"
        )
    lines.append("-" * 82)
    lines.append(f"{'GRAND TOTAL':<18} {'':<24} {'':>8} {'':>11} "
                 f"{plan['grand_total_to_create']:>10}")
    lines.append("")

    if verbose:
        for n, node in plan["nuclei"].items():
            lines.append(f"\n== {n}  ({node['sin']}) ==")
            for _, pid in PILLAR_SUBDIRS:
                p = node["pillars"][pid]
                if not p["missing"]:
                    continue
                lines.append(f"  {pid} {p['subdir']:<14} "
                             f"[{len(p['present'])}/{len(p['applicable'])}]  "
                             f"to create: {p['missing_count']}")
                for k in p["missing"]:
                    desc = meta.get(k, {}).get("description", "")[:56]
                    lines.append(f"      - {k:<34} {desc}")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--detail", action="store_true",
                    help="Print per-nucleus gap list (kinds missing, sorted by priority)")
    ap.add_argument("--nucleus", help="Focus on one nucleus (e.g. 'n06')")
    ap.add_argument("--json", dest="json_out",
                    help="Write machine-readable report to this path")
    ap.add_argument("--core-only", action="store_true",
                    help="Only count core kinds (ignores non-core extensions)")
    ap.add_argument("--plan", action="store_true",
                    help="Emit fill plan: applicable = core + sin-affinity - EXCLUSIONS")
    ap.add_argument("--verbose", action="store_true",
                    help="With --plan: list every kind to create per pillar")
    args = ap.parse_args()

    meta = load_kinds_meta()

    # --plan mode: applicability-filtered fill list (not raw canonical gap)
    if args.plan:
        plan = build_plan(meta, focus_nucleus=args.nucleus)
        print(render_plan(plan, meta, verbose=args.verbose))
        if args.json_out:
            out = Path(args.json_out)
            out.parent.mkdir(parents=True, exist_ok=True)
            payload = {
                "generated_at": _dt.datetime.now().isoformat(),
                "mode": "plan",
                "plan": plan,
            }
            out.write_text(json.dumps(payload, indent=2, ensure_ascii=True),
                           encoding="utf-8")
            print(f"\n[OK] Plan JSON -> {out}")
        return 0

    # Default: raw audit matrix
    matrix = build_matrix(meta, core_only=args.core_only)

    scope = "CORE KINDS ONLY" if args.core_only else "ALL KINDS"
    print(f"=== Fractal Fill Audit  [{scope}]  ({len(meta)} kinds in taxonomy) ===\n")
    print(render_matrix(matrix))

    if args.detail or args.nucleus:
        print(render_gaps(matrix, meta, focus=args.nucleus))

    if args.json_out:
        out = Path(args.json_out)
        out.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "generated_at": _dt.datetime.now().isoformat(),
            "scope": scope,
            "matrix": matrix,
        }
        out.write_text(json.dumps(payload, indent=2, ensure_ascii=True),
                       encoding="utf-8")
        print(f"\n[OK] JSON report -> {out}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
