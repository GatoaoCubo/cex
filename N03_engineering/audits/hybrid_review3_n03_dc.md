---
id: hybrid_review3_n03_dc
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW3 Audit: dataset_card (N03)"
version: 1.0.0
quality: 8.6
tags: [audit, hybrid_review3, dataset_card, gemma4, wave2]
domain: data engineering quality assurance
created: "2026-04-14"
---

# HYBRID_REVIEW3 Audit — dataset_card (13 ISOs)

## Source
- Generator: gemma4:26b (HYBRID Wave 2)
- Auditor: N03 (claude-opus-4-6)
- Reference: `N01_intelligence/reports/master_systemic_defects.md`

## Scorecard (pre-fix)
| # | ISO | D1 Struct | D2 Domain | D3 Density | D4 CEX | D5 Industry | Score | Verdict |
|---|-----|-----------|-----------|------------|--------|-------------|-------|---------|
| 1 | manifest | 9 | 9 | 9 | 9 | 9 | 9.0 | LEAVE |
| 2 | system_prompt | 9 | 9 | 8 | 10 | 9 | 9.0 | LEAVE (BECOME correct; cites Datasheets) |
| 3 | instruction | 2 | 2 | 2 | 3 | 2 | 2.2 | **STUB -> REBUILT** |
| 4 | schema | 8 | 8 | 8 | 6 | 8 | 7.6 | **FIX (quality default was "high")** |
| 5 | output_template | 7 | 8 | 7 | 8 | 8 | 7.6 | LEAVE (placeholders semi-guided) |
| 6 | quality_gate | 9 | 8 | 9 | 9 | 8 | 8.6 | LEAVE (weights=1.00 verified) |
| 7 | tools | 4 | 5 | 4 | 3 | 7 | 4.6 | **FIX (fabricated tools + truncated at "* Hugging")** |
| 8 | examples | 7 | 8 | 7 | 8 | 8 | 7.6 | LEAVE |
| 9 | config | 7 | 7 | 7 | 8 | 7 | 7.2 | LEAVE |
| 10 | memory | 7 | 7 | 7 | 8 | 7 | 7.2 | LEAVE |
| 11 | knowledge_card | 8 | 8 | 8 | 8 | 8 | 8.0 | LEAVE |
| 12 | architecture | 4 | 3 | 6 | 3 | 4 | 4.0 | **FIX (D09: generic tech stack, not 13-ISO map)** |
| 13 | collaboration | 7 | 7 | 7 | 8 | 7 | 7.2 | LEAVE |

## Defects Found (vs master_systemic_defects.md)
| Defect | Hit | ISO | Fix |
|--------|-----|-----|-----|
| D01 llm_function=INJECT | NO | system_prompt has `BECOME` | — |
| D04 financial hallucination | NO | no trading/portfolio leakage | — |
| D05 quality non-null | NO | all ISO frontmatters = null | — |
| D05 schema default="high" | YES | bld_schema | quality default -> `null` |
| D07 fabricated tools | YES | bld_tools: `schema_validator.py`, `lint_card.py`, `integrity_check.py`, `cex_formatter.py` | replaced with real cex_* tools |
| D08 bare placeholders | PARTIAL | output_template uses guided placeholders like `{{use_cases_and_applications}}` | LEAVE |
| D09 generic tech stack | YES | architecture listed "S3 Connector, UI/CLI Interface, Template Engine" | rewritten as 13-ISO map |
| D10 SCHEMA.md drift | NO | — | — |
| D11 SOFT weights | NO | sum = 1.00 verified (0.15+0.15+0.10+0.10+0.15+0.10+0.05+0.10+0.10) | — |
| **NEW**: bld_instruction stub | YES | "> TODO: Generate content" | rebuilt with 4-phase DISCOVER/STRUCTURE/GOVERN/EMIT |
| **NEW**: bld_tools truncated | YES | file ended mid-line at "* Hugging" | rewritten complete |

## Industry Alignment Check
| Standard | Cited? | Notes |
|----------|--------|-------|
| HuggingFace Dataset Cards | YES (fixed) | Now in tools + instruction |
| Croissant (ML Commons) | YES (fixed) | Added to instruction Phase 3 |
| Datasheets for Datasets (Gebru 2021) | YES | system_prompt cites it |
| Google Data Cards Playbook | YES (fixed) | tools references |
| GDPR Art. 30 | YES (fixed) | instruction Phase 3 |

## Post-Fix Expected Score: 8.9
Blocking issues resolved. SOFT dimensions hardened. Industry citations present across instruction + tools + quality_gate.
