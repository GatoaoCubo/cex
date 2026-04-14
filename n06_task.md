---
mission: COMMERCIAL_REFRESH
nucleus: n06
wave: single
created: 2026-04-14
model: claude-opus-4-6
---

# N06 -- Refresh commercial readiness post Wave 4

## Context

Wave 4 (18 commercial/growth/multi-tenant kinds) just shipped + audited at 9.0-9.2.
Current commercial readiness report (N06_commercial/reports/commercial_readiness_20260413.md) is STALE — written before Wave 4.

System snapshot (2026-04-14):
- 202 kinds (was 184)
- 207 builders (was 189)
- 2666 ISOs (100% validator PASS)

Wave 4 adds (already registered in kinds_meta.json):
- PRO: ab_test_config, course_module, subscription_tier, user_journey, onboarding_flow, pricing_page, cohort_analysis, referral_program, usage_quota, customer_segment
- ENTERPRISE: compliance_checklist, usage_report, rbac_policy, audit_log, enterprise_sla, data_residency, sso_config, white_label_config

## Your task

1. Read the current commercial_readiness_20260413.md fully
2. Read 2-3 Wave 4 builder KCs to confirm what shipped (e.g. kc_pricing_page.md, kc_subscription_tier.md, kc_rbac_policy.md)
3. Produce refreshed report: `N06_commercial/reports/commercial_readiness_20260414.md`

## Deliverable structure

```markdown
---
id: commercial_readiness_20260414
kind: content_monetization
pillar: P11
title: CEX commercial readiness (post Wave 4)
version: 2.0.0
quality: null
tags: [commercial, tiers, roadmap, wave4]
---

# Commercial Readiness -- 2026-04-14 (post Wave 4)

## What changed since 2026-04-13

Deltas: +18 kinds, +18 builders, +234 ISOs. 5 audit cycles complete.

## Updated Pricing Tier Map

### FREE (attract) -- K kinds
| Kind | Why free | Conversion hook |

### PRO (convert) -- K kinds (was X, now Y)
| Kind | Value prop | Anchor feature |
[include new: ab_test_config, pricing_page, subscription_tier, onboarding_flow, ...]

### ENTERPRISE (retain + expand) -- K kinds (was X, now Y)
| Kind | Compliance/scale feature | ACV lift |
[include new: rbac_policy, sso_config, audit_log, compliance_checklist, enterprise_sla, data_residency, white_label_config, usage_report]

## Wave 4 GTM Gap Closures

| Dimension | Before (36% overall) | After Wave 4 | New Score |
| Taxonomy completeness | 75% | ? | ? |
| Quality baseline | 90% | ? | ? |
| Developer docs | 40% | ? | ? |
| Pricing page | 5% | now have pricing_page builder | ? |
| Enterprise features | 35% | now have rbac + sso + audit_log + sla | ? |
| Demo assets | 10% | ? | ? |
| Sales enablement | 5% | ? | ? |
| Open source story | 25% | ? | ? |

**Overall GTM readiness after Wave 4: N%**

## Remaining Gaps for Wave 5

Identify 18 new kinds that unlock the next tier of GTM readiness.
Candidates to evaluate:
- Developer: quickstart_guide, api_reference, sdk_example, integration_guide, changelog
- Demo: playground_config, interactive_demo, sandbox_spec, case_study
- Sales: pitch_deck, roi_calculator, competitive_matrix, sales_playbook, discovery_questions
- Industries: healthcare_vertical, fintech_vertical, legal_vertical (if high-ACV targets)

Recommend top 18 with rationale.

## Revenue Projection Update

Based on 202 kinds now available:
- Addressable buyer personas: PM, engineer, compliance officer, PLG lead, enterprise architect
- Estimated TAM expansion from Wave 4: X%

## Commit

git add N06_commercial/reports/commercial_readiness_20260414.md
git commit -m "[N06] COMMERCIAL_REFRESH: updated readiness assessment post Wave 4 (N% GTM)"
```

## ON COMPLETION

```
python -c "from _tools.signal_writer import write_signal; write_signal('n06', 'complete', 9.0)"
```
