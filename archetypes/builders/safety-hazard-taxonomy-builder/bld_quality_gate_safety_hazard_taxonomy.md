---
kind: quality_gate
id: p11_qg_safety_hazard_taxonomy
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for safety_hazard_taxonomy
quality: 9.0
title: "Quality Gate Safety Hazard Taxonomy"
version: "1.0.0"
author: n01_wave7
tags: [safety_hazard_taxonomy, builder, quality_gate, MLCommons, AILuminate, Llama-Guard, hazard-category, CBRN, severity-level, response-template, taxonomy]
tldr: "Quality gate with HARD and SOFT scoring for safety_hazard_taxonomy"
domain: "safety_hazard_taxonomy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| Hazard taxonomy completeness | 100% | equals | All declared categories in taxonomy-scope |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|---------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches pattern ^p11_sht_[a-z][a-z0-9_]+\.md$ | ID format mismatch |
| H03 | kind field equals 'safety_hazard_taxonomy' | Kind field incorrect or missing |
| H04 | taxonomy_scope field declares full-12 or subset with justification | Missing or undeclared scope |
| H05 | All declared categories have Llama Guard 4 label mapped | Category without label mapping |
| H06 | CBRN category (S8) includes Chemical/Biological/Radiological/Nuclear sub-categories | CBRN treated as single undifferentiated category |
| H07 | Each category has 4 severity levels defined (low/medium/high/critical) | Any category missing severity levels |
| H08 | HARD_REFUSE response template defined for critical severity on all categories | Critical severity without HARD_REFUSE template |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|--------------|
| D01 | Category definition completeness (definition + boundary + false-positive) | 0.25 | All 3 sub-fields per category = 1.0, 2 = 0.6, 1 = 0.3 |
| D02 | Severity level criteria specificity | 0.25 | Specific criteria for all 4 levels = 1.0, generic = 0.5 |
| D03 | Response template coverage | 0.20 | All 4 templates defined + per-category assignment = 1.0, partial = 0.5 |
| D04 | Cross-category boundary documentation | 0.15 | Boundaries for adjacent pairs documented = 1.0, partial = 0.5, none = 0 |
| D05 | Regulatory mapping per category | 0.15 | Laws cited for >= 50% of categories = 1.0, < 50% = 0.5, none = 0 |

## Actions
| Score | Action |
|-------|--------|
| GOLDEN | >= 9.5 | Approved for production safety system integration |
| PUBLISH | >= 8.0 | Approved after safety team sign-off |
| REVIEW | >= 7.0 | Return to AI safety team for revision |
| REJECT | < 7.0 | Reject -- insufficient for safety system use |

## Bypass
| Condition | Approver | Audit Trail |
|-----------|---------|-------------|
| Partial taxonomy for domain-restricted system | Head of AI Safety | Scope restriction documented |
