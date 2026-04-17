---
kind: examples
id: bld_examples_team_charter
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of team_charter artifacts
quality: 9.1
title: "Examples Team Charter"
version: "1.0.0"
author: n06_wave8
tags: [team_charter, builder, examples, governance]
tldr: "Golden and anti-examples of team_charter artifacts"
domain: "team_charter construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```markdown
---
id: p12_tc_brand_launch_v1.md
kind: team_charter
pillar: P12
charter_id: "tc_brand_launch_2026q2"
crew_template_ref: "P12/crew_templates/tpl_brand_launch_crew.md"
mission_statement: "This crew will produce a complete brand identity package (logo, KC, landing page, pricing) by 2026-05-01 to enable public launch of [BRAND] with >= 9.0 quality across all artifacts."
deadline: "2026-05-01T23:59:00-03:00"
quality: null
---

## Mission Statement
This crew will produce a complete brand identity package by 2026-05-01 to enable public launch.

## Deliverables
| # | Kind | Pillar Path | Owner Nucleus | Due |
|---|------|-------------|---------------|-----|
| 1 | knowledge_card | P01/brand/ | N04 | 2026-04-25 |
| 2 | landing_page | P05/brand/ | N02 | 2026-04-28 |
| 3 | content_monetization | P11/brand/ | N06 | 2026-04-30 |

## Success Metrics (OKR)
**Objective**: Launch brand with production-ready digital assets.

| Key Result | Threshold | Metric Type | Owner |
|------------|-----------|-------------|-------|
| All artifacts at quality >= 9.0 | >= 9.0 | cex_score.py | N03 |
| Landing page conversion rate | >= 3.5% | analytics | N06 |
| Brand KC passes 12LP checklist | 12/12 | validator | N04 |

## Budget
| Resource | Allocated | Hard Ceiling | Notes |
|----------|-----------|--------------|-------|
| Tokens | 400,000 | 600,000 | Per nucleus total |
| Time (hours) | 4.0 | 8.0 | Wall-clock |
| Cost (USD) | $12.00 | $20.00 | API + infra |

## Termination Criteria
| Condition | Trigger | State |
|-----------|---------|-------|
| SUCCESS | All 3 deliverables >= 9.0, all KRs met | COMPLETE |
| FAILURE | 2x retry below floor on any deliverable | FAILED |
| TIMEOUT | 2026-05-01T23:59 with < 80% complete | EXPIRED |
```

## Anti-Example 1: Missing Budget and Termination
```markdown
---
kind: team_charter
mission_statement: "Build something for the brand."
---
## Deliverables
- landing page
- knowledge card
```
## Why it fails:
No `charter_id`, no `crew_template_ref`, no `deadline`, no `budget`, no `success_metrics`, no `escalation_protocol`, no `termination_criteria`. The charter is a stub -- N07 cannot dispatch autonomously from this because there are no governance constraints to enforce.

## Anti-Example 2: Charter Conflated with Handoff
```markdown
---
kind: team_charter
mission_statement: "N04 should read archetypes/builders/knowledge_card-builder/ and produce kc_brand.md using the 8F pipeline, writing to P01/brand/kc_brand.md."
---
```
## Why it fails:
The mission_statement describes HOW (implementation steps), not WHAT (mission outcome). A charter defines the contract (goals, metrics, budget, termination). Implementation steps belong in the nucleus handoff. Mixing the two makes both the charter and the handoff ambiguous.

## Anti-Example 3: OKR Without Numeric Thresholds
```markdown
## Success Metrics
**Objective**: Make the brand look good.
| Key Result | Threshold |
|------------|-----------|
| Artifacts are high quality | high |
| User is happy | yes |
```
## Why it fails:
Key Results must have numeric thresholds (e.g., score >= 9.0, conversion >= 3.5%) so N07 can evaluate them algorithmically. "High" and "yes" are not machine-evaluable -- the escalation protocol cannot trigger on them.
