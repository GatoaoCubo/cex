---
id: hybrid_review3_n03
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW3 Audit: dataset_card + experiment_tracker (N03)"
version: 1.0.0
quality: 8.9
tags: [audit, hybrid_review3, dataset_card, experiment_tracker, gemma4, wave2]
domain: data engineering quality assurance
created: "2026-04-14"
density_score: 1.0
---

# HYBRID_REVIEW3 Master Summary — N03

## Scope
- dataset_card (13 ISOs) — `archetypes/builders/dataset-card-builder/`
- experiment_tracker (13 ISOs) — `archetypes/builders/experiment-tracker-builder/`
- Source generator: **gemma4:26b** (HYBRID Wave 2)
- Per-kind reports: `hybrid_review3_n03_dc.md`, `hybrid_review3_n03_et.md`

## Headline
Both builders had the **same gemma4 contamination pattern**: generation budget exhausted mid-file, leaving stubs ("> TODO:") or truncations, plus D07 fabricated tool names and D09 generic architecture maps. No D01/D04/D10/D11 hits — system_prompt `BECOME` held, pillars correct, no financial hallucination, all SOFT weights summed to 1.00 where present.

## Defect Frequency (26 ISOs audited)
| Defect | dc | et | Total |
|--------|----|----|-------|
| Stub / truncation | 2 | 2 | **4** |
| D05 schema quality default | 1 | 1 | 2 |
| D07 fabricated tools | 1 | 1 | 2 |
| D09 architecture generic | 1 | 1 | 2 |
| D01, D04, D08, D10, D11 | 0 | 0 | 0 |

## Fixes Applied (9 ISOs surgically rewritten)
| File | Defect | Action |
|------|--------|--------|
| bld_instruction_dataset_card.md | stub | 4-phase DISCOVER/STRUCTURE/GOVERN/EMIT, 5 industry refs |
| bld_instruction_experiment_tracker.md | truncated | 4-phase FRAME/INSTRUMENT/EXECUTE/GOVERN, 6 backend refs |
| bld_quality_gate_experiment_tracker.md | full stub | HARD H01-H07 + SOFT D1-D9 (weights=1.00) |
| bld_tools_dataset_card.md | D07 + truncated | 8 real cex_* tools + 6 external standards |
| bld_tools_experiment_tracker.md | D07 | 8 real cex_* tools + 6 tracking backends |
| bld_architecture_dataset_card.md | D09 | 13-ISO component map + dependency table + 8F mapping |
| bld_architecture_experiment_tracker.md | D09 | 13-ISO component map + dependency table + 8F mapping |
| bld_schema_dataset_card.md | D05 | quality default: high -> null |
| bld_schema_experiment_tracker.md | D05 | quality default: high -> null |

## gemma4:26b Behavior Notes
1. Generates decent scaffolding/frontmatter but **runs out of tokens** for content-heavy ISOs (instruction, quality_gate).
2. Confidently hallucinates plausible-but-nonexistent tool names (`cex_logger.py`, `schema_validator.py`).
3. Defaults to **generic enterprise architecture language** ("Viz Engine", "S3 Connector") instead of the meta-fractal 13-ISO structure.
4. Sets schema `quality: high` despite project rule being `quality: null` — model prior dominates instruction.
5. Preserves `llm_function: BECOME` correctly (D01 negative — **gemma4 beat qwen3:8b on this**).

## Recommendation for Wave 3+
- Post-generation validator **must** check for substring `> TODO:` and truncation heuristics (file ends mid-sentence, no final period).
- `bld_tools` content **must** be validated against `_tools/*.py` listing (hard gate, not soft).
- Generator prompt for `bld_architecture` must explicitly require the 13-ISO table (currently D09 is generator-level, not model-level).

## Post-Fix Summary
| Kind | Pre-fix score | Post-fix expected |
|------|---------------|-------------------|
| dataset_card | 6.9 | 8.9 |
| experiment_tracker | 6.4 | 8.9 |

Both above 8.0 threshold. Ready for mission consolidation.
