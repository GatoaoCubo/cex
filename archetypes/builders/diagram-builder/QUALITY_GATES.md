---
id: diagram-builder-quality-gates
kind: quality_gates
builder: diagram-builder
version: 1.0.0
---

# diagram-builder — QUALITY GATES

## HARD Gates (9) — All must pass

| Gate | Check | Fail = |
|------|-------|--------|
| H01 | YAML frontmatter parses without error | Broken artifact — reject |
| H02 | id matches `^p08_diag_[a-z][a-z0-9_]+$` | Namespace violation — reject |
| H03 | id == filename stem (without .md) | Brain search breaks — reject |
| H04 | kind == "diagram" (exact literal) | Type integrity — reject |
| H05 | quality == null (not a number, not missing) | Self-score violation — reject |
| H06 | All 15 required fields present and non-empty | Incomplete artifact — reject |
| H07 | tags is list, len >= 3 | Unsearchable — reject |
| H08 | scope is non-empty string | Unknown what is visualized — reject |
| H09 | notation in [ascii, mermaid] | Invalid format — reject |

## SOFT Gates (10) — Target 8+ for pool eligibility

| Gate | Check | Weight | Score |
|------|-------|--------|-------|
| S01 | tldr <= 160 chars, non-empty, dense | 1.0 | 10 |
| S02 | zoom_level specified and valid | 1.0 | 10 |
| S03 | components list len >= 2, all labeled | 1.0 | 10 |
| S04 | Legend section present, explains all symbols | 1.0 | 10 |
| S05 | Diagram section contains actual visual (not prose) | 1.0 | 10 |
| S06 | Connections table present with labeled relationships | 1.0 | 10 |
| S07 | Body has all 7 required sections | 1.0 | 10 |
| S08 | density >= 0.80 (no filler phrases) | 1.0 | 10 |
| S09 | Annotations present for non-obvious decisions | 0.5 | 10 |
| S10 | keywords present, len >= 2 | 0.5 | 10 |

## Scoring

SOFT score = sum(weight * 10 for each passing gate) / sum(all weights) * 10

| Score | Tier | Action |
|-------|------|--------|
| 9.5+ | Golden | Pool as golden artifact |
| 8.0+ | Skilled | Pool + remember() |
| 7.0+ | Learning | Experimental use |
| < 7.0 | Rejected | Revise before output |

## Common Failure Modes

| Gate | Most Common Cause |
|------|------------------|
| H02 | id missing `p08_diag_` prefix |
| H05 | Builder self-assigned a score |
| H06 | Missing notation, zoom_level, or components |
| S05 | Diagram body is prose description, not visual |
| S04 | No legend — reader cannot decode symbols |
| S07 | Missing Annotations or References section |
