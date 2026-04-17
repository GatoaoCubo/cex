---
id: con_rate_limit_config_n03
kind: rate_limit_config
pillar: P09
nucleus: n03
title: Engineering Rate Limit Config
version: 1.0
quality: null
tags: [config, rate_limit, budget, engineering, n03]
---


<!-- 8F: F1 constrain=P09/rate_limit_config F2 become=rate-limit-config-builder F3 inject=nucleus_def_n03, kc_rate_limit_config, P09_config, builder runtime context
     F4 reason=protect build throughput, token budget, and mission spend for N03 work F5 call=rg, Get-Content, apply_patch F6 produce=4384 bytes
     F7 govern=frontmatter+sections+tables+ascii+self-check F8 collaborate=save N03_engineering/P09_config/con_rate_limit_config_n03.md -->

# Engineering Rate Limit Config

## Purpose

| Field | Value |
|-------|-------|
| Mission fit | Throughput and spend control for N03 artifact generation and validation work |
| Pride lens | A proud builder does not confuse intensity with waste; limits preserve precision under load |
| Primary use | Constrain request rate, token rate, and budget during local and orchestrated execution |
| Boundary | Provider quotas and spend only; retry tactics beyond quota response live in runtime policy |
| Scope | `n03` mission execution across local and shared provider pools |
| Failure prevented | Burst failures, runaway cost, and unfair pool contention |

## Values

| Profile | Provider | RPM | TPM | Daily budget USD | Monthly budget USD | Use case |
|---------|----------|----:|----:|-----------------:|-------------------:|----------|
| `draft_local` | shared | 20 | 120000 | 3 | 30 | Iterative local drafting |
| `mission_standard` | shared | 40 | 240000 | 8 | 120 | Normal wave execution |
| `review_heavy` | shared | 25 | 180000 | 6 | 90 | Dense validation and review loops |
| `compile_only` | local tools | 120 | 0 | 0 | 0 | File compilation, no LLM spend |

## Model Overrides

| Model key | RPM | TPM | Budget share | Rule |
|-----------|----:|----:|-------------:|------|
| `gpt-5-codex` | 30 | 180000 | 0.60 | Default high-capability authoring lane |
| `gpt-5.4-mini` | 60 | 240000 | 0.20 | Lower-cost validation or summarization lane |
| `fallback_shared` | 15 | 90000 | 0.20 | Conservative fallback lane |

## Budget Rules

| Rule ID | Statement | Why it matters |
|---------|-----------|----------------|
| `R01` | `mission_standard` is the default for production-like N03 work | One baseline keeps cost behavior predictable |
| `R02` | No profile may exceed the monthly budget without an explicit orchestrator override | Spend must be visible, not accidental |
| `R03` | `compile_only` never consumes provider budget | Local tooling should not distort quota data |
| `R04` | When daily budget hits `80%`, switch to `review_heavy` or `gpt-5.4-mini` | Graceful degradation beats abrupt stall |
| `R05` | Any `429` or equivalent limit response triggers temporary rate reduction on the active profile | Throughput adapts instead of thrashing |
| `R06` | Profiles are named by workload, not by person or machine | Reuse beats personalization drift |

## Rationale

| Design choice | Why it exists | Pride expression |
|---------------|---------------|------------------|
| Four workload profiles | Enough nuance for real use, not enough for chaos | Controlled variety |
| Budget split by model | Capability and cost should be designed together | Performance with fiscal discipline |
| Explicit zero-budget compile lane | Tool work should stay measurable and separate | Honest accounting |
| 80 percent conservation trigger | Strong systems prepare before failure | Anticipation is craftsmanship |
| Shared-provider framing | N03 often operates in mixed environments | Config should survive deployment context shifts |
| Workload names over user names | Policies should scale beyond one operator | Foundation over preference |

## Example

```yaml
provider: shared
default_profile: mission_standard
profiles:
  mission_standard:
    rpm: 40
    tpm: 240000
    daily_budget_usd: 8
    monthly_budget_usd: 120
model_overrides:
  gpt-5-codex:
    rpm: 30
    tpm: 180000
conservation_trigger:
  budget_percent: 80
  fallback_profile: review_heavy
```

## Properties

| Property | Value |
|----------|-------|
| Nucleus | `n03` |
| Pillar | `P09` |
| Kind | `rate_limit_config` |
| Profiles | `4` |
| Model overrides | `3` |
| Default profile | `mission_standard` |
| Conservation trigger | `80%` |
| Lens | `Inventive Pride` |
