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
related:
  - bld_examples_analyst_briefing
  - bld_knowledge_card_analyst_briefing
  - p03_sp_analyst_briefing_builder
  - bld_instruction_analyst_briefing
  - analyst-briefing-builder
  - bld_schema_analyst_briefing
  - p10_mem_analyst_briefing_builder
  - bld_output_template_analyst_briefing
  - bld_knowledge_card_competitive_matrix
  - bld_collaboration_analyst_briefing
---

## Quality Gate

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

## Examples

## Golden Example
```markdown
---
kind: analyst_briefing
analyst_firm: gartner
research_track: magic-quadrant
vendor: Acme DataOps Inc.
briefing_date: 2026-06-15
embargo_flag: false
---

## Company Overview
Acme DataOps Inc. (founded 2019, HQ: Austin TX) provides cloud-native data pipeline orchestration to mid-market and enterprise customers. ARR: $48M. Employees: 312. YoY ARR growth: 67%.

## Market Position
Gartner Magic Quadrant -- Data Integration Tools (2026). Claimed position: Visionary.
Completeness of Vision score: 8.2/10. Ability to Execute: 7.4/10.

## Product Strengths
1. **Real-time CDC latency <50ms** -- P99 latency 42ms across 1,200 production pipelines (internal telemetry Q1 2026).
2. **NPS 72** -- measured across 380 customers (Medallia, Q4 2025); 94% retention rate.
3. **Connector library: 340 native connectors** -- highest in Gartner peer comparison set as of Jan 2026.

## Competitive Landscape
| Vendor | Our Advantage | Their Advantage |
|--------|---------------|-----------------|
| FivetranCo | 40% lower TCO (Forrester TEI 2025) | Larger connector ecosystem (380 vs 340) |
| AlteryxPro | Native ML-pipeline integration; no-code UI | More mature enterprise sales motion |

Win rate vs FivetranCo: 58%. Win rate vs AlteryxPro: 44%.

## Anticipated Analyst Questions
**Q1: How do you differentiate from Fivetran in the mid-market?**
Our CDC latency advantage (42ms vs 180ms P99) translates to a 40% TCO reduction for real-time analytics use cases. Three Fortune 500 customers switched from FivetranCo in H2 2025 (references available under NDA).
```

## Anti-Example 1: Unquantified Claims
```markdown
---
kind: analyst_briefing
analyst_firm: gartner
vendor: GenericSoft Inc.
---
## Product Strengths
1. We have the best performance in the market.
2. Customers love our product.
3. Our roadmap is exciting and innovative.
```
## Why it fails:
No quantified proof points. "Best performance" and "customers love" are unverifiable marketing claims. A Gartner analyst will reject a briefing without numeric evidence. Missing briefing_date, research_track, and competitive landscape.

## Anti-Example 2: Sales Pitch Confusion
```markdown
---
kind: analyst_briefing
vendor: SalesForcePro
---
## Why You Should Buy SalesForcePro
- 50% discount for new customers
- Free trial available
- Award-winning customer success team
```
## Why it fails:
This is a sales pitch, not an analyst briefing. The audience is an industry analyst (Gartner, Forrester, IDC), not a buyer. No framework alignment (no Magic Quadrant axes, no Wave criteria). Missing analyst_firm and research_track fields entirely.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
