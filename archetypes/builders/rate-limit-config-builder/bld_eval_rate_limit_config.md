---
kind: quality_gate
id: p11_qg_rate_limit_config
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of rate_limit_config artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: rate_limit_config"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, rate-limit-config, P09, rpm, tpm, budget, tier]
tldr: "Pass/fail gate for rate_limit_config artifacts: numeric limit completeness, tier validity, budget cap presence, and provider identification."
domain: "rate limiting configuration — RPM, TPM, budget, and tier management for LLM API providers"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 0.90
related:
  - bld_examples_rate_limit_config
  - p03_sp_rate_limit_config_builder
  - rate-limit-config-builder
  - bld_instruction_rate_limit_config
  - bld_output_template_rate_limit_config
  - bld_architecture_rate_limit_config
  - bld_knowledge_card_rate_limit_config
  - bld_collaboration_rate_limit_config
  - bld_tools_rate_limit_config
  - p01_kc_rate_limit_config
---

## Quality Gate

# Gate: rate_limit_config

This ISO encodes a rate limit policy -- throttle bounds, quota windows, and backoff behavior.
## Definition
| Field | Value |
|---|---|
| metric | rate_limit_config artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: rate_limit_config` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p09_rl_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, or missing prefix |
| H03 | ID equals filename stem | `id: p09_rl_foo` but file is `p09_rl_bar.md` |
| H04 | Kind equals literal `rate_limit_config` | `kind: config` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing `provider`, `rpm`, `tpm`, `tier`, or `tags` |
| H07 | rpm is a positive integer | rpm: 0, rpm: -1, rpm: "50", or absent |
| H08 | tpm is a positive integer | tpm: 0, tpm: -1, tpm: "80000", or absent |
| H09 | tags includes "rate_limit_config" | tags list does not contain "rate_limit_config" |
| H10 | Body has all 4 required sections | Missing ## Overview, ## Limits, ## Tier, or ## Budget |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Limit completeness | 1.0 | RPM, TPM, RPD, and concurrent all documented |
| Tier description | 1.0 | Tier named, described, and upgrade path provided |
| Budget cap | 1.0 | budget_usd present with alert_threshold and overage policy |
| Model overrides | 0.5 | Per-model rpm/tpm overrides present when provider supports them |
| Retry policy | 0.5 | retry_after documented for 429 handling |
| Provider accuracy | 1.0 | Limits match known provider documentation for stated tier |
| Alert threshold | 0.5 | alert_threshold in [0.0, 1.0], actionable value (e.g. 0.8) |
| tldr quality | 1.0 | tldr <= 160ch, includes provider + tier + key limits |
| Boundary clarity | 1.0 | Explicitly not runtime_rule (timeouts/retries) or env_config |
| Domain specificity | 1.0 | Numbers are real provider limits, not placeholders |
| Testability | 1.0 | Each limit value verifiable against provider dashboard/docs |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Internal placeholder used only during development with fictional limits |
| approver | Author self-certification noting placeholder status |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 7d — placeholder configs must be replaced with real limits or removed |
| never_bypass | H01 (unparseable YAML), H05 (self-scored gates corrupt quality metrics), H07/H08 (zero/negative limits break all consumers) |

## Examples

# Examples: rate-limit-config-builder

This ISO encodes a rate limit policy -- throttle bounds, quota windows, and backoff behavior.
## Golden Example
INPUT: "Create rate limit config for Anthropic Build tier"
OUTPUT:
```yaml
id: p09_rl_anthropic_build
kind: rate_limit_config
pillar: P09
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "Anthropic Build Tier Rate Limits"
provider: "anthropic"
rpm: 50
tpm: 80000
quality: null
tags: [rate_limit_config, anthropic, build-tier]
tldr: "Anthropic Build tier: 50 RPM, 80K TPM, 1K RPD, $100/mo cap at 80% alert"
description: "Rate limits for Anthropic API Build tier — standard production tier after $5 spend"
budget_usd: 100.0
tier: "build"
rpd: 1000
concurrent: 10
retry_after: 60
alert_threshold: 0.8
model_overrides:
  claude-3-5-sonnet-20241022:
    rpm: 50
    tpm: 80000
  claude-3-haiku-20240307:
    rpm: 50
    tpm: 100000
```
## Overview
Declares rate limits for the Anthropic API Build tier — the default production tier
activated after $5 cumulative spend. Used by all Claude API integrations at this tier.
## Limits
| Dimension | Limit | Notes |
|-----------|-------|-------|
| RPM | 50 | Requests per minute, all models |
| TPM | 80,000 | Tokens per minute, all models |
| RPD | 1,000 | Requests per day hard cap |
| Concurrent | 10 | Max parallel in-flight requests |
## Tier
**Tier**: build
Standard production tier. Requires $5 cumulative API spend to activate.
Includes all Claude models. Upgrade to Scale tier requires costm agreement with Anthropic sales.
## Budget
Monthly cap: $100.00
Alert threshold: 80% — trigger notification at $80 spend
Overage policy: Requests blocked when budget_usd exceeded; reset at billing cycle start.
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches ^p09_rl_ pattern (H02 pass)
- kind: rate_limit_config (H04 pass)
- rpm: 50 and tpm: 80000 are positive integers (H07+H08 pass)
- all 4 body sections present (H10 pass)
- tags: 3 items, includes "rate_limit_config" (H09 pass)
- model_overrides with real Anthropic model IDs (SOFT bonus)
- budget_usd + alert_threshold + overage policy (Budget gate pass)
- tldr: 67 chars <= 160 (tldr gate pass)
- retry_after: 60 matches Anthropic 429 Retry-After header value
## Anti-Example
INPUT: "Create rate limit config for OpenAI"
BAD OUTPUT:
```yaml
id: openai-limits
kind: config
provider: openai
rpm: unlimited
tpm: lots
quality: 9.5
tags: [openai]
```
Rate limits for OpenAI. Use when calling GPT.
FAILURES:
1. id: "openai-limits" has hyphens and no `p09_rl_` prefix -> H02 FAIL
2. kind: "config" not "rate_limit_config" -> H04 FAIL
3. quality: 9.5 (not null) -> H05 FAIL
4. rpm: "unlimited" is not a positive integer -> H07 FAIL
5. tpm: "lots" is not a positive integer -> H08 FAIL
6. tags: only 1 item, missing "rate_limit_config" -> H09 FAIL
7. Missing required fields: pillar, version, created, updated, author, name, tier, tldr -> H06 FAIL
8. Body missing ## Overview, ## Limits, ## Tier, ## Budget sections -> H10 FAIL
9. No tier specified — cannot verify limits against provider docs -> SOFT FAIL
10. No budget_usd or alert_threshold — cost unbounded -> SOFT FAIL

## Golden Example 2 -- Per-Tier SaaS API Rate Limits
INPUT: "Create a rate limit config for our SaaS API: free=100 req/day, pro=10k/day, enterprise=unlimited with burst"
OUTPUT:
```yaml
id: p09_rl_saas_api_tiered
kind: rate_limit_config
pillar: P09
version: "1.0.0"
created: "2026-04-18"
updated: "2026-04-18"
author: "builder_agent"
name: "SaaS API Per-Tier Rate Limits"
provider: "internal"
rpm: 10
tpm: null
quality: null
tags: [rate_limit_config, saas, tiered, monetization, P09]
tldr: "SaaS API tiers: free=100 RPD, pro=10k RPD, enterprise=unlimited; burst=2x for 60s"
description: "Per-subscription-tier rate limits for the SaaS REST API; enforced at the API gateway layer"
budget_usd: null
tier: "tiered"
rpd: 100
concurrent: 2
retry_after: 3600
alert_threshold: 0.9
tier_overrides:
  free:
    rpd: 100
    rpm: 10
    concurrent: 2
    burst_multiplier: 1.0
    burst_window_sec: 0
    overage_action: block
  pro:
    rpd: 10000
    rpm: 200
    concurrent: 20
    burst_multiplier: 2.0
    burst_window_sec: 60
    overage_action: block
  enterprise:
    rpd: null
    rpm: null
    concurrent: 100
    burst_multiplier: 3.0
    burst_window_sec: 300
    overage_action: warn
```
## Overview
Declares per-subscription-tier rate limits for the SaaS REST API.
Enforced at the API gateway (e.g., Kong, AWS API Gateway, or custom middleware).
Limits protect infrastructure cost and create hard differentiation between pricing tiers,
making plan upgrades the only path to higher throughput -- a direct revenue lever.
Default values (rpm: 10, rpd: 100, concurrent: 2) apply to any unauthenticated or
unrecognized plan; tier_overrides win when plan context is available.

## Limits
| Tier | RPD | RPM | Concurrent | Burst Multiplier | Burst Window | Overage |
|------|-----|-----|-----------|-----------------|--------------|---------|
| free | 100 | 10 | 2 | 1.0x (no burst) | 0s | block |
| pro | 10,000 | 200 | 20 | 2.0x | 60s | block |
| enterprise | unlimited | unlimited | 100 | 3.0x | 300s | warn only |

Burst allowance: pro tier may exceed rpm by 2x for up to 60 seconds before throttling.
Enterprise burst is advisory -- warn is logged but requests are not blocked.

## Tier
**Tier**: tiered (multi-plan SaaS differentiation)
Free tier enforces hard blocks to create upgrade pressure.
Pro tier uses 2x burst to reward paying customers during legitimate traffic spikes.
Enterprise tier is warn-only -- SLA commitments prohibit hard blocks; escalate to ops instead.
Upgrade path: free -> pro upgrade unlocks 100x throughput; key conversion trigger.

## Budget
Revenue-protection notes:
- Free tier cap (100 RPD) is set below the marginal infrastructure cost of a free user at scale.
  Exceeding 100 RPD without upgrade = revenue-negative; hard block is non-negotiable.
- Pro tier (10k RPD at $X/mo) is priced so that 95th-percentile usage remains margin-positive.
  Monitor: if p95 pro users hit >8k RPD consistently, reprice or add an overage fee.
- Enterprise tier: no RPD cap but concurrent=100 acts as a soft infrastructure guard.
  Alert threshold: 90% of concurrent slots used -> notify sales for capacity planning.
- alert_threshold: 0.9 triggers at 90% RPD consumption; webhook to growth team for upsell outreach.
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches ^p09_rl_ pattern (H02 pass)
- kind: rate_limit_config (H04 pass)
- rpm: 10 and rpd: 100 are positive integers (defaults for unknown plan) (H07+H08 pass)
- tier_overrides with 3 named tiers matching business pricing model (SOFT bonus)
- burst_multiplier + burst_window_sec per tier (burst gate pass)
- overage_action: block for free/pro, warn for enterprise (revenue-protection design)
- all 4 body sections present (H10 pass)
- tags: 5 items, includes "rate_limit_config" and "monetization" (H09 pass)
- alert_threshold: 0.9 enables upsell outreach before hard block (Strategic Greed lens)
- tldr: 71 chars <= 160 (tldr gate pass)
- retry_after: 3600 (1 hour) chosen to create upgrade friction, not just backoff

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
