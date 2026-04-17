"""Generate FRACTAL_FILL wave handoffs (W4/W5/W6) from plan.

Reads: .cex/runtime/plans/plan_fractal_fill_waves.md
Reads: .cex/kinds_meta.json
Writes: .cex/runtime/handoffs/FRACTAL_FILL_W{N}_n0{X}.md
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / ".cex" / "runtime" / "plans" / "plan_fractal_fill_waves.md"
KINDS = json.loads((ROOT / ".cex" / "kinds_meta.json").read_text(encoding="utf-8"))
OUT = ROOT / ".cex" / "runtime" / "handoffs"

SIN = {
    "n00": "Pre-sin Archetype",
    "n01": "Analytical Envy",
    "n02": "Creative Lust",
    "n03": "Inventive Pride",
    "n04": "Knowledge Gluttony",
    "n05": "Gating Wrath",
    "n06": "Strategic Greed",
    "n07": "Orchestrating Sloth",
}
NUC_DIR = {
    "n00": "N00_genesis",
    "n01": "N01_intelligence",
    "n02": "N02_marketing",
    "n03": "N03_engineering",
    "n04": "N04_knowledge",
    "n05": "N05_operations",
    "n06": "N06_commercial",
    "n07": "N07_admin",
}
PILLAR_TO_SUBDIR = {
    "P01": ("knowledge", "kno"),
    "P02": ("agents", "age"),
    "P03": ("prompts", "pro"),
    "P04": ("tools", "tol"),
    "P05": ("output", "out"),
    "P06": ("schemas", "sch"),
    "P07": ("evals", "eva"),
    "P08": ("architecture", "arc"),
    "P09": ("config", "con"),
    "P10": ("memory", "mem"),
    "P11": ("feedback", "fbk"),
    "P12": ("orchestration", "orc"),
}

WAVE_META = {
    "W4": ("W4_EXECUTION", "tools + output", ["P04", "P05"]),
    "W5": ("W5_META", "architecture + quality", ["P08", "P07"]),
    "W6": ("W6_SELF_IMPROVE", "feedback + orchestration", ["P11", "P12"]),
}


def parse_plan() -> dict[str, dict[str, list[str]]]:
    """Parse wave plan markdown -> {wave: {nucleus: [kinds]}}."""
    text = PLAN.read_text(encoding="utf-8")
    waves: dict[str, dict[str, list[str]]] = {}
    current_wave: str | None = None
    for line in text.splitlines():
        m = re.match(r"^## (W[1-6])_", line)
        if m:
            current_wave = m.group(1)
            waves[current_wave] = {}
            continue
        if not current_wave:
            continue
        m = re.match(r"^\| N0(\d)_[a-z]+ \| +\d+ \| (.+) \|$", line)
        if m:
            nuc = f"n0{m.group(1)}"
            kinds = [k.strip() for k in m.group(2).split(",")]
            waves[current_wave][nuc] = kinds
    return waves


def kind_meta(kind: str) -> tuple[str, str]:
    """Return (pillar, description) for kind."""
    meta = KINDS.get(kind, {})
    return meta.get("pillar", "?"), meta.get("description", "")[:90]


def render_handoff(wave: str, nuc: str, kinds: list[str]) -> str:
    wave_name, wave_purpose, pillars = WAVE_META[wave]
    nuc_dir = NUC_DIR[nuc]
    sin = SIN[nuc]
    count = len(kinds)
    # Group by pillar
    by_pillar: dict[str, list[str]] = {}
    for k in kinds:
        p, _ = kind_meta(k)
        by_pillar.setdefault(p, []).append(k)
    # Deliverables block
    lines: list[str] = []
    idx = 1
    for pillar in pillars:
        sub = PILLAR_TO_SUBDIR[pillar][0]
        pref = PILLAR_TO_SUBDIR[pillar][1]
        items = by_pillar.get(pillar, [])
        if not items:
            continue
        lines.append(f"\n### {pillar} ({sub}) -- {len(items)} artifacts\n")
        for k in items:
            _, desc = kind_meta(k)
            lines.append(
                f"{idx}. `{nuc_dir}/{sub}/{pref}_{k}_{nuc}.md` -- kind=`{k}` -- {desc}"
            )
            idx += 1
    deliverables = "\n".join(lines)
    pillar_schemas = "\n".join(
        f"4. `P{p[1:]}_{PILLAR_TO_SUBDIR[p][0]}/_schema.yaml`" if False else f"- `P{p[1:]}_*/_schema.yaml`"
        for p in pillars
    )
    # Bases to read in context
    prior_waves = {
        "W4": "schemas, config, knowledge, memory, agents, prompts",
        "W5": "schemas, config, knowledge, memory, agents, prompts, tools, output",
        "W6": "all prior waves (schemas, config, knowledge, memory, agents, prompts, tools, output, architecture, evals)",
    }[wave]
    body = f"""---
mission: FRACTAL_FILL_{wave}
nucleus: {nuc}
wave: {wave_name}
created: 2026-04-16
model: gpt-5-codex
pillars: {pillars}
artifact_count: {count}
---

# {nuc.upper()} -- Wave {wave[1]} {wave_name.split('_',1)[1]} ({count} artifacts: {wave_purpose})

## Mission

You are {nuc_dir} ({sin}). Fill pillars {', '.join(pillars)} of your nucleus: {count} artifacts via 8F.
Sin lens drives every choice: be coherent with your nucleus's identity.

## Context (READ FIRST)

1. `{nuc_dir}/P08_architecture/nucleus_def_{nuc}.md` -- your identity + sin lens
2. Prior waves in `{nuc_dir}/` -- {prior_waves}
3. `archetypes/builders/{{kind}}-builder/` per kind (13 ISOs each)
4. Pillar schemas: {', '.join(pillars)} under `P*/`
5. `P01_knowledge/library/kind/kc_{{kind}}.md` when present
6. Sibling artifacts in `N0*/` (2-3 as shape references)

## Deliverables
{deliverables}

## Format

Standard frontmatter (id/kind/pillar/nucleus/title/version/quality:null/tags) + structured body.
Min 80 lines, density >= 0.85. Use tables over prose. Sin lens in tone/choices.

## 8F trace (HTML comment IMMEDIATELY BELOW the closing `---` of frontmatter, NEVER above it)

Format: `<!-- 8F: F1 constrain=... F2 become=... F3 inject=... F4 reason=... F5 call=... F6 produce=... F7 govern=... F8 collaborate=... -->`

## ASCII rule

Unaccented PT identifiers; no emoji in code fields. See `.claude/rules/ascii-code-rule.md`.

## On completion

1. Save all files.
2. Print exactly: `=== COMPLETE === nucleus={nuc} wave={wave} count={count} ===`
3. DO NOT `git commit` -- N07 handles commits.
4. Exit.
"""
    return body


def main() -> None:
    waves = parse_plan()
    OUT.mkdir(parents=True, exist_ok=True)
    total = 0
    for wave in ["W4", "W5", "W6"]:
        nuc_kinds = waves.get(wave, {})
        for nuc in ["n00", "n01", "n02", "n03", "n04", "n05", "n06", "n07"]:
            kinds = nuc_kinds.get(nuc)
            if not kinds:
                continue
            target = OUT / f"FRACTAL_FILL_{wave}_{nuc}.md"
            target.write_text(render_handoff(wave, nuc, kinds), encoding="utf-8")
            total += 1
    print(f"[OK] generated {total} handoffs across W4+W5+W6")


if __name__ == "__main__":
    main()
