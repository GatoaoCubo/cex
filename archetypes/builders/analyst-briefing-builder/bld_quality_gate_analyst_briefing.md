---
kind: quality_gate
id: p05_qg_analyst_briefing
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for analyst_briefing
quality: 9.0
title: "Quality Gate Analyst Briefing"
version: "1.0.0"
author: n01_wave6
tags: [analyst_briefing, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for analyst_briefing"
domain: "analyst_briefing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| Metric | Threshold | Operator | Scope |
|---|---|---|---|
| Analyst briefing completeness | 100% | equals | All required sections present |
| Quantified proof points | >=3 | min_count | Product strengths section |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches pattern ^p05_ab_[a-z][a-z0-9_]+.md$ | ID format mismatch |
| H03 | kind field = analyst_briefing | Kind field incorrect or missing |
| H04 | analyst_firm field present and valid | Missing or invalid firm (gartner, forrester, idc, etc.) |
| H05 | research_track field present | Missing track (magic-quadrant, wave, marketscape, etc.) |
| H06 | vendor field present and non-empty | Missing vendor name |
| H07 | Product strengths section has >=3 quantified claims | Unquantified or fewer than 3 strengths listed |
| H08 | Competitive landscape names >=2 competitors | Missing or single competitor only |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Proof point density (Gartner/Forrester evidence standards) | 0.30 | >=5 quantified points = 1.0, 3-4 = 0.7, <3 = 0 |
| D02 | Framework alignment (Magic Quadrant axes or Wave criteria explicitly cited) | 0.25 | Framework explicitly mapped = 1.0, partial = 0.5, absent = 0 |
| D03 | Competitive differentiation quality (named vendors, factual delta) | 0.20 | >=3 named competitors with diff table = 1.0, 2 = 0.7, <2 = 0 |
| D04 | Analyst question preparedness (IDC/Gartner briefing-style probes covered) | 0.15 | >=8 Q+A pairs = 1.0, 5-7 = 0.7, <5 = 0 |
| D05 | Roadmap credibility (concrete milestones, NDA flag if needed) | 0.10 | Specific milestones + NDA handling = 1.0, vague = 0.5, absent = 0 |

## Actions
| Label | Score | Action |
|---|---|---|
| GOLDEN | >=9.5 | Auto-publish to analyst relations portal |
| PUBLISH | >=8.0 | Publish after AR team review |
| REVIEW | >=7.0 | Require senior AR review before use |
| REJECT | <7.0 | Reject and rebuild with additional proof points |

## Bypass
| Conditions | Approver | Audit Trail |
|---|---|---|
| Emergency analyst briefing request (<24h deadline) | VP Analyst Relations | Escalation log + post-mortem |
