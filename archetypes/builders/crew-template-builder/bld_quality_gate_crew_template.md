---
kind: quality_gate
id: p11_qg_crew_template
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for crew_template
quality: 9.0
title: "Quality Gate Crew Template"
version: "1.0.0"
author: n03_wave8_builder
tags: [crew_template, builder, quality_gate, composable, crewai]
tldr: "Quality gate with HARD and SOFT scoring for crew_template"
domain: "crew_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.88
---

## Definition
| Metric | Threshold | Operator | Scope |
|---|---|---|---|
| Crew blueprint completeness | 100% | equals | All composable-crew templates |
| Role reference validity | 100% | equals | Every role_assignment reference |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches ^p12_ct_[a-z][a-z0-9_]+\.md$ | ID pattern mismatch |
| H03 | kind field == 'crew_template' | Kind field incorrect or missing |
| H04 | process in {sequential, hierarchical, consensus} | Invalid process topology |
| H05 | All role refs resolve to existing role_assignment artifacts | Broken role_assignment reference |
| H06 | memory_scope declared per role | Missing memory_scope for any role |
| H07 | success_criteria measurable (threshold / count / gate_id) | Subjective or missing success_criteria |
| H08 | handoff_protocol specified and consistent | Missing or mixed handoff-protocols |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Role composition coherence (roles cover task boundary) | 0.25 | Full coverage = 1.0, gaps = 0.5, mismatched = 0 |
| D02 | Process topology fit (matches dependency graph) | 0.20 | Optimal = 1.0, workable = 0.5, wrong = 0 |
| D03 | Memory-scope precision (least-privilege per role) | 0.15 | Minimal scope = 1.0, over-shared = 0.5, leaky = 0 |
| D04 | Handoff-protocol portability (A2A / Swarm / native) | 0.15 | Industry-standard = 1.0, adapted = 0.5, ad-hoc = 0 |
| D05 | Success-criteria measurability and specificity | 0.25 | Gate-IDs + thresholds = 1.0, counts only = 0.5, vague = 0 |

## Actions
| Score | Action |
|---|---|
| GOLDEN | >=9.5 | Auto-register as reusable crew template |
| PUBLISH | >=8.0 | Publish to crew-template library |
| REVIEW | >=7.0 | Request peer review from N03 |
| REJECT | <7.0 | Rebuild per 8F F6 |

## Bypass
| Conditions | Approver | Audit Trail |
|---|---|---|
| Experimental crew pattern (research) | N01 lead | .cex/experiments/results.tsv |
