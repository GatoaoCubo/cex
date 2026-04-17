---
id: con_rate_limit_config_n01
kind: rate_limit_config
pillar: P09
nucleus: n01
title: N01 Rate Limit Config
version: 1.0
quality: 9.0
tags: [rate_limit_config, budget, throughput, research]
density_score: 1.0
---

<!-- 8F: F1 constrain=P09/rate_limit_config F2 become=rate-limit-config-builder F3 inject=nucleus_def_n01+n01-intelligence+kc_rate_limit_config+P09_schema+rate examples F4 reason=internal ceilings for deep research cost and throughput F5 call=apply_patch+cex_compile F6 produce=3528 bytes F7 govern=frontmatter+ascii+80-line+self-check F8 collaborate=N01_intelligence/P09_config/con_rate_limit_config_n01.md -->

## Purpose

| Item | Decision |
|------|----------|
| Config name | `n01_research_ceiling` |
| Provider | `internal_router` |
| Tier | `research` |
| Lens | Analytical Envy can consume large context quickly, so throttles must preserve depth without letting one investigation starve the wave |
| Nature | Internal control limit, not an external vendor promise |

## Values

| Dimension | Value | Notes |
|----------|-------|-------|
| `rpm` | `24` | limit simultaneous curiosity bursts |
| `tpm` | `180000` | enough for deep comparative synthesis |
| `rpd` | `720` | keeps day-long scans bounded |
| `concurrent` | `4` | avoids queue collapse and noisy retries |
| `budget_usd` | `18.0` | daily-equivalent monthly ceiling for this nucleus slice |
| `retry_after` | `30` | cool-down after local throttle |
| `alert_threshold` | `0.75` | warn early before budget panic |

## Model Overrides

| Model | RPM | TPM | Why |
|------|-----|-----|-----|
| `gpt-5.4` | `12` | `90000` | deep synthesis, expensive but strong |
| `gpt-5.4-mini` | `24` | `180000` | faster benchmark passes |
| `o4-mini` | `30` | `120000` | cheap contradiction sweeps |

## Budget Policy

| Threshold | Action |
|----------|--------|
| 50 percent | annotate traces with spend posture |
| 75 percent | reduce non-critical scans and notify orchestrator |
| 90 percent | only decision-critical research continues |
| 100 percent | block new work until reset or override |

## Retry Policy

| Event | Response |
|------|----------|
| local throttle hit | wait `retry_after` seconds plus jitter |
| repeated burst within 5 minutes | halve concurrency for next window |
| budget threshold breach | downgrade to lighter model if mission allows |

## Rationale

| Design Choice | Why | Analytical Envy Interpretation |
|--------------|-----|--------------------------------|
| modest RPM | deep research should not spray shallow requests | envy needs thoughtful passes, not spam |
| large TPM | comparative synthesis benefits from richer context windows | depth is a competitive advantage worth preserving |
| concurrency capped at 4 | parallel work is useful until evidence quality collapses | too much simultaneous curiosity creates thin outputs |
| internal router provider label | this config governs local policy, not vendor SLAs | precision avoids false assumptions |
| budget thresholds step down gradually | hard stops alone create brittle behavior | disciplined envy should degrade gracefully |

## Example

```yaml
name: n01_research_ceiling
provider: internal_router
rpm: 24
tpm: 180000
budget_usd: 18.0
tier: research
rpd: 720
concurrent: 4
retry_after: 30
alert_threshold: 0.75
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `rate_limit_config` |
| Pillar | `P09` |
| Nucleus | `n01` |
| Provider | `internal_router` |
| Tier | `research` |
| Model Overrides | `3` |
| Alert Threshold | `0.75` |
| Quality Field | `null` |
