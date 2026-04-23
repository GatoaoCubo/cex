---
kind: quality_gate
id: p11_qg_feature_flag
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of feature_flag artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: feature_flag"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, feature-flag, toggle, rollout, P11]
tldr: "Validates feature_flag artifacts: toggle semantics, rollout strategy completeness, and kill switch safety."
domain: "feature_flag — on/off toggles with rollout percentage, cohort targeting, and kill switch behavior"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.91
related:
  - p11_qg_formatter
  - bld_examples_feature_flag
  - p11_qg_fallback_chain
  - p11_qg_guardrail
  - p11_qg_golden_test
  - p11_qg_glossary_entry
  - bld_output_template_feature_flag
  - p11_qg_few_shot_example
  - p11_qg_input_schema
  - p11_qg_quality_gate
---

## Quality Gate

# Gate: feature_flag
## Definition
| Field     | Value |
|-----------|-------|
| metric    | composite score across SOFT dimensions |
| threshold | >= 7.0 to publish; >= 9.5 for golden |
| operator  | weighted average after all HARD gates pass |
| scope     | all artifacts where `kind: feature_flag` |
All HARD gates are AND-logic: one failure rejects the artifact regardless of SOFT score.
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Any YAML syntax error |
| H02 | ID matches `^p09_ff_[a-z][a-z0-9_]+$` | Wrong format or namespace |
| H03 | ID equals filename stem (no extension) | Mismatch between id field and file name |
| H04 | Kind equals literal `feature_flag` | Any other value |
| H05 | `quality` field is null | Any non-null value |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, flag_name, default_state, category, rollout_percentage, quality, tags, tldr | Any missing field |
| H07 | Body has sections: `## Flag Specification`, `## Rollout Strategy`, `## Lifecycle` | Any required section absent |
| H08 | `default_state` is one of: `on`, `off` | Any other value |
| H09 | `rollout_percentage` is integer 0–100 | Out of range or non-integer |
| H10 | `category` is one of: `release`, `experiment`, `ops`, `permission` | Any unlisted value |
## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| S01 | `tldr` <= 160 chars, names flag and toggle behavior | 0.10 | Accurate=1.0, vague=0.4, absent=0.0 |
| S02 | Tags list len >= 3, includes `feature_flag` | 0.05 | Met=1.0, partial=0.5 |
| S03 | `flag_name` is snake_case and descriptive | 0.07 | Snake_case+descriptive=1.0, generic=0.3 |
| S04 | Rollout strategy has stages with explicit percentages | 0.12 | All stages=1.0, partial=0.5, absent=0.0 |
| S05 | Kill switch behavior documented | 0.10 | Explicit=1.0, implied=0.4, absent=0.0 |
| S06 | Cohort targeting rules defined when `rollout_percentage` < 100 | 0.10 | Defined=1.0, missing when needed=0.0, N/A=1.0 |
| S07 | Lifecycle section includes retire or sunset date | 0.08 | Present=1.0, absent=0.0 |
| S08 | Rollback procedure described step-by-step | 0.10 | Step-by-step=1.0, brief=0.5, absent=0.0 |
| S09 | Observability hook defined (metric or log emitted on toggle change) | 0.10 | Present=1.0, absent=0.0 |
| S10 | Boundary from `env_config` and `permission` stated | 0.08 | Both stated=1.0, one=0.5, absent=0.0 |
| S11 | `density_score` >= 0.80 | 0.07 | Met=1.0, below=0.0 |
| S12 | No filler phrases ("designed to enable", "various use cases") | 0.03 | Clean=1.0, filler present=0.0 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — reference artifact for feature_flag calibration |
| >= 8.0 | PUBLISH — pool-eligible; rollout strategy and kill switch documented |
| >= 7.0 | REVIEW — usable but missing sunset date or observability hook |
| < 7.0  | REJECT — redo; likely missing rollback procedure or cohort rules |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Hotfix rollout only; flag controls an active incident mitigation with no time to complete all gates |
| approver | Product owner or on-call engineer |
| audit trail | Required: incident ticket, timestamp, approver handle |
| expiry | 24 hours; must be replaced with compliant artifact |
| never bypass | H01 (corrupt YAML), H05 (self-scored quality is invalid), H08 (boolean semantics must be exact for runtime evaluation) |

## Examples

# Examples: feature-flag-builder
## Golden Example
INPUT: "Create a feature flag for the new search algorithm with gradual rollout"
OUTPUT:
```yaml
id: p09_ff_enable_vector_search
kind: feature_flag
pillar: P09
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
flag_name: "enable_vector_search"
default_state: off
category: release
rollout_percentage: 0
quality: null
tags: [feature_flag, search, release, P09, vector]
tldr: "Vector search release flag: off by default, 4-stage rollout to 100% over 2 weeks"
description: "Controls activation of vector-based search replacing keyword search"
owner: "search_team"
expires: "2026-05-01"
targeting: "percentage-based, all users"
```
## Flag Specification
Enables vector-based semantic search to replace legacy keyword search.
Default OFF — legacy keyword search serves all users until flag ramps.
Kill switch: set rollout_percentage to 0 to instantly revert to keyword search.
## Rollout Strategy
| Stage | Percentage | Duration | Criteria |
|-------|-----------|----------|----------|
| canary | 5% | 3 days | error rate < 0.1%, latency < 200ms |
| early | 25% | 4 days | no regressions, user feedback positive |
| broad | 50% | 3 days | metrics stable, no support tickets |
| full | 100% | permanent | retire flag after 2 weeks stable |
## Lifecycle
- Created: 2026-03-26 (flag defined, code deployed behind flag)
- Test: internal QA with flag ON in staging
- Ramp: canary 5% -> early 25% -> broad 50% -> full 100%
- Retire: 2026-05-01 (remove flag, vector search becomes default)
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p09_ff_ pattern (H02 pass)
- kind: feature_flag (H04 pass)
- 19 required+recommended fields present (H06 pass)
- body has all 3 sections: Flag Specification, Rollout Strategy, Lifecycle (H07 pass)
- default_state: off (valid enum) (H08 pass)
- rollout_percentage: 0 (integer 0-100) (H09 pass)
- category: release (valid enum) (H10 pass)
- tldr: 74 chars <= 160 (S01 pass)
- tags: 5 items, includes "feature_flag" (S02 pass)
## Anti-Example
INPUT: "Add a feature flag for dark mode"
BAD OUTPUT:
```yaml
id: dark-mode
kind: flag
pillar: config
flag_name: Dark Mode Toggle
default_state: maybe
rollout_percentage: half
quality: 9.0
tags: [ui]
```
Turn on dark mode for users.
FAILURES:
1. id: "dark-mode" uses hyphens, no `p09_ff_` prefix -> H02 FAIL
2. kind: "flag" not "feature_flag" -> H04 FAIL
3. pillar: "config" not "P09" -> H06 FAIL
4. default_state: "maybe" not in enum [on, off] -> H08 FAIL
5. rollout_percentage: "half" not integer 0-100 -> H09 FAIL
6. quality: 9.0 (not null) -> H05 FAIL
7. Missing fields: version, created, updated, author, category, tldr -> H06 FAIL
8. tags: only 1 item, missing "feature_flag" -> S02 FAIL
9. Body missing ## Flag Specification, ## Rollout Strategy, ## Lifecycle -> H07 FAIL
10. flag_name uses spaces and uppercase (should be snake_case slug) -> S04 FAIL
11. No rollout strategy or lifecycle plan defined -> S05 FAIL

## Golden Example 2 -- Pricing Tier Gate (Pro Feature Gating)
INPUT: "Create a feature flag to gate the AI report export feature behind the Pro tier only"
OUTPUT:
```yaml
id: p09_ff_pro_ai_report_export
kind: feature_flag
pillar: P09
version: "1.0.0"
created: "2026-04-18"
updated: "2026-04-18"
author: "builder_agent"
flag_name: "pro_ai_report_export"
default_state: off
category: entitlement
rollout_percentage: 100
quality: null
tags: [feature_flag, entitlement, pro-tier, monetization, P09]
tldr: "AI report export gated to Pro tier only; free users see upgrade prompt instead"
description: "Controls access to AI-generated PDF/CSV export in the Reports module; free users blocked at evaluation time"
owner: "growth_team"
expires: null
targeting: "segment-based: plan=pro OR plan=enterprise"
```
## Flag Specification
Enables AI-powered report export (PDF and CSV with AI summaries) exclusively for Pro and Enterprise
plan subscribers. Free-tier users who trigger the export action receive an upgrade prompt
(not an error) to preserve conversion opportunity.
Default OFF for free users, ON for pro/enterprise -- evaluated at request time via segment check.
Kill switch: set default_state to off to disable for ALL tiers instantly (emergency rollback).

## Rollout Strategy
| Stage | Target Segment | Duration | Gate Criteria |
|-------|---------------|----------|---------------|
| internal | staff accounts only | 3 days | feature functional, no data leaks |
| pro-only | plan=pro segment | permanent | upgrade funnel live, export count tracked |
| enterprise | plan=enterprise added | permanent | SLA reporting verified |
| free-prompt | free users | permanent | upgrade CTA A/B variant chosen |

This flag does NOT use percentage rollout -- it uses segment targeting.
rollout_percentage: 100 means the flag evaluator runs for 100% of requests;
segment check (plan=pro/enterprise) is the actual access gate.

## Lifecycle
- Created: 2026-04-18 (flag defined, export code behind flag, upgrade prompt deployed)
- Activation: immediate -- no ramp needed (entitlement flags are binary by design)
- Review: quarterly -- evaluate if feature should expand to free tier (freemium trade-off)
- Retire: only if feature is removed entirely or merged into base plan
- expires: null -- entitlement flags are permanent until pricing model changes

## Multi-Runtime Compatibility Note
This flag is evaluated by cex_token_budget.py (runtime enforcement) and must be present in
.cex/config/ on ALL runtimes (Claude, Codex, Gemini, Ollama). Entitlement flags with
segment targeting require the runtime to pass user.plan context at evaluation time:
- Claude runtime: injected via brand_config.yaml + session context
- Codex/Gemini: passed as env var CEX_USER_PLAN at boot
- Ollama (local): defaults to plan=enterprise (single-user assumption)
Never hard-code the plan check in application logic -- always delegate to the flag evaluator.

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p09_ff_ pattern (H02 pass)
- kind: feature_flag (H04 pass)
- category: entitlement (valid enum, distinct from release) (H10 pass)
- default_state: off (valid enum) (H08 pass)
- rollout_percentage: 100 (integer 0-100, semantics explained in body) (H09 pass)
- expires: null (acceptable for permanent entitlement flags) (H11 pass)
- body has all 4 sections: Flag Specification, Rollout Strategy, Lifecycle, Multi-Runtime (H07 pass)
- targeting uses segment-based model -- revenue-protective design (Strategic Greed lens)
- upgrade prompt strategy preserves conversion opportunity (monetization gate, not hard block)
- tldr: 79 chars <= 160 (S01 pass)
- tags: 5 items, includes "feature_flag" and "monetization" (S02 pass)

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
