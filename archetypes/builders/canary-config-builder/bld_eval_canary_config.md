---
id: bld_quality_gate_canary_config
kind: quality_gate
pillar: P07
title: "Gate: canary_config"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: canary_config
quality: 8.7
tags: [quality_gate, canary_config, P09]
llm_function: GOVERN
tldr: "Validates canary configs for gradual rollout, rollback triggers, and analysis configuration."
density_score: null
related:
  - p10_lr_e2e_eval_builder
  - p11_qg_e2e_eval
  - p01_kc_cicd_llm_pipeline
  - bld_instruction_research_pipeline
  - bld_instruction_e2e_eval
  - p11_qg_instruction
  - p05_output_rollback_plan
  - p11_qg_boot_config
  - p04_qg_tts_provider
  - p11_qg_quality_gate
---

## Quality Gate

## Definition
A canary_config must ensure gradual traffic exposure with defined automatic rollback. Any config that jumps directly to 100% or lacks rollback triggers is not a canary -- it is a direct deploy.

## HARD Gates
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML valid |
| H02 | ID matches namespace | `^p09_cc_[a-z][a-z0-9_]+$` |
| H03 | Kind matches literal | `kind` is exactly `canary_config` |
| H04 | Quality is null | `quality: null` |
| H05 | canary_version and stable_version set | Both non-empty, different values |
| H06 | stages_count matches list | frontmatter count = actual stages |
| H07 | rollback_trigger_metric set | Non-empty rollback metric |
| H08 | Last stage is 100% | Traffic progression completes at 100% |
| H09 | First stage < 50% | Gradual start required |

## SOFT Scoring
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Analysis interval per stage | 1.0 | analysis_interval_minutes present on each stage |
| Provider specified | 0.5 | provider is one of known values |
| Rollback threshold is numeric | 0.5 | threshold is float, not null |
| Pause duration per stage | 0.5 | pause_duration_minutes present on each non-final stage |

Sum of weights: 2.5. `soft_score = sum / 2.5 * 10`

## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | PUBLISH |
| >= 7.0 | REVIEW |
| < 7.0 | REJECT |

## Examples

# Examples: canary_config

## Golden Example 1 -- CEX API Progressive Delivery
INPUT: "Canary rollout for cex-api 2.1.0 with auto rollback on error rate"
OUTPUT:
```yaml
---
id: p09_cc_cex_api_v210
kind: canary_config
pillar: P09
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
service_name: "cex-api"
canary_version: "2.1.0"
stable_version: "2.0.3"
stages_count: 4
rollback_trigger_metric: "error_rate"
rollback_trigger_threshold: 0.01
provider: argo_rollouts
domain: cex-api
quality: null
tags: [canary_config, cex-api, production, P09]
tldr: "cex-api v2.1.0: 4-stage canary 5->25->50->100%; rollback if error_rate > 1% or p99 > 500ms"
---
## Traffic Stages
| Stage    | Canary % | Pause (min) | Analysis Interval | Pass Criteria                         |
|----------|----------|-------------|-------------------|---------------------------------------|
| initial  | 5        | 10          | 2 min             | error_rate < 1%, p99_latency < 200ms  |
| phase_1  | 25       | 15          | 5 min             | error_rate < 1%, p99_latency < 250ms  |
| phase_2  | 50       | 20          | 5 min             | error_rate < 0.5%, p99_latency < 300ms|
| complete | 100      | --          | --                | stable 30 min, then retire canary      |

## Rollback Triggers
| Trigger         | Threshold       | Action                           |
|-----------------|-----------------|----------------------------------|
| error_rate      | > 0.01 (1%)     | Instant rollback to v2.0.3       |
| p99_latency     | > 500ms         | Instant rollback to v2.0.3       |
| manual_override | --              | On-call engineer triggers via CLI|

## Analysis Configuration
- Provider: argo_rollouts
- Metric backend: Prometheus
- Success condition: `result[0] < 0.01`
- Failure condition: `result[0] >= 0.01`
- Interval: 60s per analysis run
- Count: 5 consecutive passes required per stage
```
WHY THIS IS GOLDEN:
- 4 progressive stages (not 1-shot) -- real progressive delivery
- Distinct SLO thresholds per stage (tightens as blast radius grows)
- 2 rollback triggers (error_rate + latency) -- defense in depth
- Rollback points to exact version (v2.0.3, not "previous")
- Analysis config specifies backend, condition, interval, count
- quality: null (H05 pass)

## Golden Example 2 -- E-Commerce Checkout Feature Canary
INPUT: "Safe rollout of new checkout flow for peak season -- payment errors are revenue-critical"
OUTPUT:
```yaml
---
id: p09_cc_checkout_v3_peak
kind: canary_config
pillar: P09
version: 1.0.0
created: "2026-04-18"
updated: "2026-04-18"
service_name: "checkout-service"
canary_version: "3.0.0"
stable_version: "2.9.1"
stages_count: 5
rollback_trigger_metric: "payment_error_rate"
rollback_trigger_threshold: 0.001
provider: flagger
domain: ecommerce-checkout
quality: null
tags: [canary_config, checkout, payment, peak-season, revenue-critical, P09]
tldr: "Checkout v3: ultra-conservative 5-stage canary (1%->5%->15%->40%->100%); rollback if payment errors > 0.1% -- peak season revenue protection"
---
## Traffic Stages (Revenue-Conservative)
| Stage    | Canary % | Pause      | Analysis     | Pass Criteria                              |
|----------|----------|------------|--------------|--------------------------------------------|
| probe    | 1        | 30 min     | 5 min        | payment_error < 0.1%, conversion_rate > 3% |
| validate | 5        | 60 min     | 10 min       | payment_error < 0.1%, p99 < 400ms          |
| expand   | 15       | 90 min     | 10 min       | payment_error < 0.1%, no revenue anomaly   |
| broad    | 40       | 120 min    | 15 min       | all SLOs stable, support tickets baseline  |
| full     | 100      | --         | --           | 4h stable window, retire canary            |

## Rollback Triggers
| Trigger                | Threshold                   | Rationale                         |
|------------------------|-----------------------------|-----------------------------------|
| payment_error_rate     | > 0.001 (0.1%)              | 10x tighter -- every failure = $  |
| conversion_rate        | < 2.5% (vs 3.1% baseline)   | Funnel degradation = lost revenue |
| p99_checkout_latency   | > 2000ms                    | UX cliff: cart abandonment spikes |
| manual_override        | --                          | On-call + RevOps can halt anytime |

## Analysis Configuration
- Provider: flagger
- Metric backend: Datadog
- Payment metric: `sum:checkout.payment.errors{env:prod}.as_count() / sum:checkout.payment.attempts{env:prod}.as_count()`
- Conversion metric: `sum:checkout.completed{env:prod}.as_count() / sum:checkout.initiated{env:prod}.as_count()`
- Interval: 60s, Count: 10 consecutive passes per stage

## Revenue Protection Notes
- Peak season: do NOT advance stages during business hours 18:00-23:00 UTC
- Rollback SLA: < 2 minutes to full revert (automated via Flagger webhook)
- Post-canary: promote during 06:00-08:00 UTC (lowest traffic window)
```
WHY THIS IS GOLDEN:
- Revenue-critical service gets tighter thresholds (0.1% vs 1%)
- 5 stages instead of 4 (extra caution for payment flow)
- Business metrics (conversion_rate) added alongside technical SLOs
- Time constraints encoded (no stage advance during peak hours)
- Rollback SLA specified (< 2 minutes)
- Multi-trigger defense: technical + business + manual

## Anti-Example 1: Single-Stage "Canary" (REJECTED)
```yaml
stages_count: 1
stages:
  - traffic_percent: 100  # FAIL: 100% is not a canary, it's a full deploy
rollback_trigger_metric: null  # FAIL: no rollback trigger = no safety net
provider: "deploy tool"  # FAIL: vague, not a specific provider
```
WHY REJECTED: A single 100% stage is a full deploy with no rollback. This is not progressive delivery -- it eliminates the canary's purpose. No rollback trigger means a bad deploy has to be caught and reverted manually (MTTR > 30min vs < 2min automated).

## Anti-Example 2: Vague Thresholds (REJECTED)
```yaml
rollback_trigger_metric: "errors"    # FAIL: which errors? rate or count?
rollback_trigger_threshold: "high"   # FAIL: "high" is not a number
stages:
  - traffic: "some"   # FAIL: percentage must be a specific integer
    pause: "a while"  # FAIL: duration must be specific (minutes)
```
WHY REJECTED: Canary configs execute in automated pipelines. "High", "some", "a while" cannot be evaluated by Argo Rollouts or Flagger. The rollout will either fail to parse or use defaults, both of which defeat the canary's revenue protection purpose.

## Anti-Example 3: Missing Rollback Target (REJECTED)
```yaml
rollback_trigger_metric: "error_rate"
rollback_trigger_threshold: 0.05
# FAIL: rollback_to is missing
# FAIL: no stable_version specified
```
WHY REJECTED: Auto-rollback without a target version is undefined behavior. The system cannot roll back to "the previous version" if that version is not pinned. In a CI/CD pipeline with multiple deploys per day, "previous" is ambiguous. Always specify `rollback_to: "vX.Y.Z"`.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
