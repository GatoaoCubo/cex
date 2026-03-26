#!/usr/bin/env python3
"""
lp_completeness.py — CEX LP Completeness Scorer
Calculates completeness score per LP based on schema, templates, examples, generators.

Score formula:
  score = (templates_pct * 0.3) + (examples_pct * 0.4) + (golden_pct * 0.2) + (generator * 0.1)

Usage:
  python _tools/lp_completeness.py
  python _tools/lp_completeness.py --json
  python _tools/lp_completeness.py --md
"""

import os
import re
import sys
import json
import yaml
from pathlib import Path
from datetime import datetime

# Force UTF-8 on Windows stdout — prevents UnicodeEncodeError in autonomous runs
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ── Config ────────────────────────────────────────────────────────────────────

CEX_ROOT = Path(__file__).parent.parent
TYPE_TO_TEMPLATE_PATH = CEX_ROOT / "_meta" / "TYPE_TO_TEMPLATE.yaml"

LP_DIRS = [
    ("P01", "P01_knowledge",    "knowledge"),
    ("P02", "P02_model",        "model"),
    ("P03", "P03_prompt",       "prompt"),
    ("P04", "P04_tools",        "tools"),
    ("P05", "P05_output",       "output"),
    ("P06", "P06_schema",       "schema"),
    ("P07", "P07_evals",        "evals"),
    ("P08", "P08_architecture", "architecture"),
    ("P09", "P09_config",       "config"),
    ("P10", "P10_memory",       "memory"),
    ("P11", "P11_feedback",     "feedback"),
    ("P12", "P12_orchestration","orchestration"),
]

GOLDEN_THRESHOLD = 9.0

# ── Helpers ───────────────────────────────────────────────────────────────────

def load_type_to_template():
    """Load TYPE_TO_TEMPLATE.yaml -> dict of type_name -> path_or_null."""
    if not TYPE_TO_TEMPLATE_PATH.exists():
        return {}
    with open(TYPE_TO_TEMPLATE_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def get_schema_types(lp_path: Path) -> list:
    """Return list of type names defined in _schema.yaml."""
    schema_path = lp_path / "_schema.yaml"
    if not schema_path.exists():
        return []
    with open(schema_path, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return list(data.get("kinds", {}).keys())


def count_examples(lp_path: Path) -> tuple[int, int]:
    """Return (total_examples, golden_examples) from examples/ directory."""
    ex_dir = lp_path / "examples"
    if not ex_dir.exists():
        return 0, 0
    total = 0
    golden = 0
    for fpath in ex_dir.glob("*.md"):
        total += 1
        content = fpath.read_text(encoding="utf-8", errors="ignore")
        scores = re.findall(r'\bquality[:\s]+(\d+\.?\d*)', content, re.I)
        scores += re.findall(r'\bscore[:\s]+(\d+\.?\d*)', content, re.I)
        numeric = [float(s) for s in scores if float(s) <= 10.0]
        if numeric and max(numeric) >= GOLDEN_THRESHOLD:
            golden += 1
    return total, golden


def has_generator(lp_path: Path) -> bool:
    return (lp_path / "_generator.md").exists()


def templates_covered(types: list, type_to_tpl: dict) -> int:
    """Count how many types have a non-null template entry."""
    covered = 0
    for t in types:
        val = type_to_tpl.get(t)
        if val is not None and val != "null":
            covered += 1
    return covered


def score_lp(types_count, tpl_covered, tpl_total,
             ex_count, golden_count, generator) -> float:
    """Compute weighted completeness score (0.0 – 1.0)."""
    templates_pct = (tpl_covered / types_count) if types_count > 0 else 0.0
    examples_pct  = min(ex_count / types_count, 1.0) if types_count > 0 else 0.0
    golden_pct    = (golden_count / ex_count) if ex_count > 0 else 0.0
    gen           = 1.0 if generator else 0.0
    return round(
        (templates_pct * 0.3) + (examples_pct * 0.4) +
        (golden_pct    * 0.2) + (gen          * 0.1),
        4
    )


# ── Main ──────────────────────────────────────────────────────────────────────

def run():
    type_to_tpl = load_type_to_template()
    results = []

    for code, dirname, name in LP_DIRS:
        lp_path = CEX_ROOT / dirname
        if not lp_path.exists():
            continue

        types      = get_schema_types(lp_path)
        n_types    = len(types)
        n_tpl      = templates_covered(types, type_to_tpl)
        n_ex, n_gld = count_examples(lp_path)
        gen         = has_generator(lp_path)

        templates_pct = round(n_tpl / n_types * 100, 1) if n_types else 0.0
        examples_pct  = round(min(n_ex / n_types, 1.0) * 100, 1) if n_types else 0.0
        golden_pct    = round(n_gld / n_ex * 100, 1) if n_ex else 0.0
        final_score   = score_lp(n_types, n_tpl, len([1 for _ in types]),
                                 n_ex, n_gld, gen)

        results.append({
            "pillar":           code,
            "name":         name,
            "dirname":      dirname,
            "kinds":        n_types,
            "templates_pct": templates_pct,
            "examples_pct": examples_pct,
            "golden_pct":   golden_pct,
            "generator":    gen,
            "score":        final_score,
            # raw counts for reporting
            "_tpl_covered": n_tpl,
            "_ex_count":    n_ex,
            "_gld_count":   n_gld,
            "_type_list":   types,
        })

    # Sort by score desc
    results.sort(key=lambda x: x["score"], reverse=True)
    return results


def print_table(results):
    print(f"\n{'='*78}")
    print(f" CEX LP COMPLETENESS REPORT — {datetime.now():%Y-%m-%d %H:%M}")
    print(f"{'='*78}")
    header = f"{'LP':<4} {'Name':<16} {'Types':>5} {'Tpl%':>6} {'Ex%':>5} {'Gld%':>6} {'Gen':>4} {'Score':>6}"
    print(header)
    print("-" * 78)
    for r in results:
        gen_flag = "YES" if r["generator"] else "NO"
        print(
            f"{r['pillar']:<4} {r['name']:<16} {r['kinds']:>5} "
            f"{r['templates_pct']:>5.1f}% {r['examples_pct']:>4.1f}% "
            f"{r['golden_pct']:>5.1f}% {gen_flag:>4} {r['score']:>6.4f}"
        )
    print("-" * 78)
    avg = round(sum(r["score"] for r in results) / len(results), 4)
    print(f"{'AVG':>26}{'':>20}{avg:>6.4f}")
    print(f"{'='*78}\n")

    print("RANKING (by score):")
    for i, r in enumerate(results, 1):
        bar = "#" * int(r["score"] * 20)
        print(f"  #{i:>2}  {r['pillar']} {r['name']:<16} {r['score']:.4f}  {bar}")

    print("\nGAP ANALYSIS (bottom 5):")
    for r in results[-5:]:
        missing_tpl = r["kinds"] - r["_tpl_covered"]
        print(f"  {r['pillar']} {r['name']:<16} — {missing_tpl} types missing templates, "
              f"{r['_ex_count']} examples ({r['_gld_count']} golden)")
    print()


def print_json(results):
    output = {
        "generated": datetime.now().isoformat(),
        "lps": [
            {k: v for k, v in r.items() if not k.startswith("_")}
            for r in results
        ],
        "avg_score": round(sum(r["score"] for r in results) / len(results), 4),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))


def print_md(results):
    """Output markdown suitable for archetypes/LP_COMPLETENESS.md."""
    lines = []
    lines.append(f"# LP Completeness Report")
    lines.append(f"")
    lines.append(f"Generated: {datetime.now():%Y-%m-%d %H:%M} | "
                 f"Avg score: {sum(r['score'] for r in results)/len(results):.4f}")
    lines.append(f"")
    lines.append(f"## Scores")
    lines.append(f"")
    lines.append(f"| LP | Name | Types | Tpl% | Ex% | Gld% | Gen | Score |")
    lines.append(f"|-----|------|-------|------|-----|------|-----|-------|")
    for r in results:
        gen_flag = "YES" if r["generator"] else "NO"
        lines.append(
            f"| {r['pillar']} | {r['name']} | {r['kinds']} | "
            f"{r['templates_pct']:.1f}% | {r['examples_pct']:.1f}% | "
            f"{r['golden_pct']:.1f}% | {gen_flag} | **{r['score']:.4f}** |"
        )
    lines.append(f"")
    lines.append(f"## Ranking")
    lines.append(f"")
    for i, r in enumerate(results, 1):
        lines.append(f"{i}. **{r['pillar']} {r['name']}** — {r['score']:.4f}")
    lines.append(f"")
    lines.append(f"## Gap Analysis")
    lines.append(f"")
    for r in sorted(results, key=lambda x: x["score"]):
        missing_tpl = r["kinds"] - r["_tpl_covered"]
        if missing_tpl > 0:
            lines.append(f"- **{r['pillar']} {r['name']}**: {missing_tpl}/{r['kinds']} types missing templates")
    lines.append(f"")
    lines.append(f"## Priority Recommendations")
    lines.append(f"")
    bottom3 = results[-3:][::-1]
    for i, r in enumerate(bottom3, 1):
        missing_tpl = r["kinds"] - r["_tpl_covered"]
        lines.append(f"{i}. **{r['pillar']} {r['name']}** (score {r['score']:.4f}) — "
                     f"add {missing_tpl} templates + more examples")
    print("\n".join(lines))


if __name__ == "__main__":
    results = run()
    mode = sys.argv[1] if len(sys.argv) > 1 else "--table"
    if mode == "--json":
        print_json(results)
    elif mode == "--md":
        print_md(results)
    else:
        print_table(results)
