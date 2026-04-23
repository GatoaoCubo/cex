---
kind: quality_gate
id: p05_qg_user_journey
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for user_journey
quality: 9.0
title: "Quality Gate User Journey"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [user_journey, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for user_journey"
domain: "user_journey construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_user_journey
  - p03_sp_user_journey_builder
  - p05_qg_pricing_page
  - bld_instruction_user_journey
  - p05_qg_integration_guide
  - p05_qg_product_tour
  - p07_qg_eval_metric
  - p11_qg_usage_report
  - p03_qg_prompt_technique
  - p02_qg_customer_segment
---

## Quality Gate

## Definition
(Table: metric, threshold, operator, scope)
| metric | threshold | operator | scope |
|---|---|---|---|
| User journey map completeness | 100% | >= | Awareness to conversion |

## HARD Gates
(Table: ID | Check | Fail Condition)
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Invalid or missing YAML |
| H02 | ID matches pattern ^p05_uj_[a-z][a-z0-9_]+.md$ | ID format mismatch |
| H03 | kind field matches 'user_journey' | Kind field incorrect |
| H04 | Journey map includes all 5 stages (awareness, interest, decision, purchase, retention) | Missing stage |
| H05 | User personas defined and aligned with journey | No personas or misalignment |
| H06 | Touchpoints mapped with >90% coverage | <90% coverage |
| H07 | Conversion rate benchmarks included | No benchmarks |

## SOFT Scoring
(Table: Dim | Dimension | Weight | Scoring Guide)
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Journey completeness | 0.15 | 1.0 (complete) to 0.0 (incomplete) |
| D02 | Persona alignment | 0.15 | 1.0 (aligned) to 0.0 (misaligned) |
| D03 | Touchpoint coverage | 0.15 | 1.0 (90%+) to 0.0 (<50%) |
| D04 | Conversion benchmarks | 0.15 | 1.0 (realistic) to 0.0 (invalid) |
| D05 | Consistency across channels | 0.10 | 1.0 (consistent) to 0.0 (inconsistent) |
| D06 | Feedback integration | 0.10 | 1.0 (included) to 0.0 (missing) |
| D07 | Visual clarity | 0.10 | 1.0 (clear) to 0.0 (unclear) |
| D08 | Stakeholder alignment | 0.10 | 1.0 (aligned) to 0.0 (disaligned) |

## Actions
(Table: Score | Action)
| Score | Action |
|---|---|
| GOLDEN (>=9.5) | Auto-publish to production |
| PUBLISH (>=8.0) | Publish with brief UX review |
| REVIEW (>=7.0) | Require stakeholder review |
| REJECT (<7.0) | Reject; rework required |

## Bypass
(Table: conditions, approver, audit trail)
| conditions | approver | audit trail |
|---|---|---|
| Critical feature launch with senior PM approval | Senior Product Manager | Email + Slack notification |

## Examples

## Golden Example
---
title: "User Journey for CRM Platform Adoption"
kind: user_journey
author: A. Smith, UX Researcher
date: 2023-10-15
tools: CRM Platform, Chat Tool, Payment Gateway, Video Conferencing
---
**Awareness**
- Touchpoint: LinkedIn ad (CRM Platform)
- User Action: Clicks "Start Free Trial"
- Emotion: Curiosity
- Pain Point: No clear ROI from current tools

**Consideration**
- Touchpoint: Demo request via chat (Support Widget)
- User Action: Schedules video call with sales
- Emotion: Skepticism
- Pain Point: Unclear integration with existing workflows

**Conversion**
- Touchpoint: Payment gateway checkout page
- User Action: Completes 30-day trial
- Emotion: Excitement
- Pain Point: No immediate value visible

**Retention**
- Touchpoint: Weekly onboarding emails (CRM Platform)
- User Action: Completes 70% of tutorial
- Emotion: Frustration
- Pain Point: Missing key features

**Advocacy**
- Touchpoint: NPS survey (Survey Tool)
- User Action: Recommends to peers
- Emotion: Satisfaction
- Pain Point: None

## Anti-Example 1: Confusing journey with workflow
---
**Awareness**
- Touchpoint: Website homepage
- User Action: Clicks "Sign Up"
- Emotion: None
- Pain Point: None

**Why it fails**: Focuses only on a single action ("Sign Up") without mapping emotional states, touchpoints across channels, or long-term engagement. It’s a workflow, not a journey.

## Anti-Example 2: Generic placeholders
---
**Awareness**
- Touchpoint: "ProviderA ad"
- User Action: "Clicks link"
- Emotion: "Curiosity"
- Pain Point: "No clear value"

**Why it fails**: Uses vague terms like "ProviderA" and "no clear value" without context. Fails to specify real tools, user emotions, or actionable insights for improvement.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
