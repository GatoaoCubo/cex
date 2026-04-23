---
kind: quality_gate
id: p12_qg_team_charter
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for team_charter
quality: 9.0
title: "Quality Gate Team Charter"
version: "1.0.0"
author: n06_wave8
tags: [team_charter, builder, quality_gate, governance]
tldr: "Quality gate with HARD and SOFT scoring for team_charter"
domain: "team_charter construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_team_charter
  - bld_output_template_team_charter
  - bld_instruction_team_charter
  - p08_qg_capability_registry
  - bld_schema_team_charter
  - p11_qg_audit_log
  - team-charter-builder
  - p11_qg_brand_artifacts
  - p11_qg_ai_rmf_profile
  - bld_knowledge_card_team_charter
---

## Quality Gate

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| Charter governance completeness | 100% required fields | equals | All team_charter artifacts |

## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches pattern ^p12_tc_[a-z][a-z0-9_]+_v[0-9]+\\.md$ | ID format mismatch |
| H03 | kind field equals "team_charter" | Kind field incorrect or missing |
| H04 | charter_id present and unique | Missing or duplicate charter_id |
| H05 | crew_template_ref resolves to existing file | Dangling reference or missing |
| H06 | mission_statement includes deadline | No temporal anchor in mission statement |
| H07 | budget.tokens, budget.time_hours, budget.cost_usd all present | Any budget sub-field missing |
| H08 | termination_criteria covers SUCCESS, FAILURE, TIMEOUT | Any termination condition missing |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | Mission statement quality (action + object + deadline + outcome) | 0.25 | All 4 elements present = 1.0, 3 = 0.75, 2 = 0.5, < 2 = 0 |
| D02 | OKR completeness (1 Objective + >= 2 numeric Key Results) | 0.25 | Full OKR with numeric thresholds = 1.0, prose only = 0.5, absent = 0 |
| D03 | Budget specificity (all 3 sub-fields + ceiling ratio >= 1.5x) | 0.20 | All fields + ratio = 1.0, all fields no ratio = 0.7, partial = 0.3 |
| D04 | Stakeholder RACI completeness (all 4 roles assigned) | 0.15 | All 4 RACI roles = 1.0, 3 = 0.75, < 3 = 0 |
| D05 | Escalation protocol coverage (>= 3 IF-THEN rules) | 0.15 | >= 3 rules = 1.0, 2 = 0.75, 1 = 0.5, 0 = 0 |

## Actions
| Label | Score | Action |
|-------|-------|--------|
| GOLDEN | >= 9.5 | Archive as gold example + auto-authorize for dispatch |
| PUBLISH | >= 8.0 | Authorize for N07 dispatch |
| REVIEW | >= 7.0 | Require N07 manual review before dispatch |
| REJECT | < 7.0 | Reject; rebuild from output_template |

## Bypass
| Condition | Approver | Audit Trail |
|-----------|----------|-------------|
| Emergency GDP override (time-critical mission) | User explicit approval | Charter v1 flagged as emergency; review post-mission |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
