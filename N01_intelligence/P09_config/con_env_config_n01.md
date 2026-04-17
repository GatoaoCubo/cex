---
id: con_env_config_n01
kind: env_config
pillar: P09
nucleus: n01
title: N01 Environment Config
version: 1.0
quality: 9.0
tags: [env_config, runtime, research, governance]
density_score: 1.0
---

<!-- 8F: F1 constrain=P09/env_config F2 become=env-config-builder F3 inject=nucleus_def_n01+n01-intelligence+kc_env_config+P09_schema+env template F4 reason=runtime variables for research operations and evidence discipline F5 call=apply_patch+cex_compile F6 produce=5142 bytes F7 govern=frontmatter+ascii+80-line+self-check F8 collaborate=N01_intelligence/P09_config/con_env_config_n01.md -->

## Purpose

| Item | Decision |
|------|----------|
| Scope | N01 research runtime and evidence governance |
| Environment | all |
| Lens | Analytical Envy uses env config to bias research runs toward explicit comparison and source quality |
| Override rule | environment variable > local file > default |
| Secret policy | sensitive values appear as refs only, never literal secrets |

## Values

| Variable | Type | Required | Default | Sensitive | Validation |
|---------|------|----------|---------|-----------|------------|
| `N01_DEFAULT_PROVIDER` | string | yes | `openai` | no | enum `openai|anthropic|router` |
| `N01_DEFAULT_MODEL` | string | yes | `gpt-5.4` | no | non-empty |
| `N01_RESEARCH_MODE` | string | yes | `comparative` | no | enum `comparative|paper|market|audit` |
| `N01_MIN_PRIMARY_SOURCES` | integer | yes | `2` | no | range `1..10` |
| `N01_EVIDENCE_TARGET` | string | yes | `triangulated` | no | enum from research evidence state |
| `N01_MAX_RESULTS_PER_SCAN` | integer | no | `12` | no | range `3..50` |
| `N01_TIME_HORIZON_DAYS` | integer | no | `90` | no | range `1..365` |
| `N01_BUDGET_TOKENS_DAY` | integer | no | `120000` | no | range `10000..500000` |
| `N01_ENABLE_COUNTER_SIGNALS` | boolean | no | `true` | no | boolean only |
| `N01_RUN_CONTEXT_PATH` | string | no | `.cex/runtime` | no | relative path |
| `N01_PROVIDER_API_KEY_REF` | string | yes | `sec_n01_llm_provider` | yes | `^sec_[a-z0-9_]+$` |
| `N01_TRACING_ENABLED` | boolean | no | `true` | no | boolean only |

## Variable Roles

| Variable | Runtime Role | Competitive Effect |
|---------|--------------|--------------------|
| `N01_DEFAULT_PROVIDER` | chooses base provider | affects speed and comparative cost |
| `N01_DEFAULT_MODEL` | default model route | affects depth of synthesis |
| `N01_RESEARCH_MODE` | sets task posture | determines whether envy is broad or narrow |
| `N01_MIN_PRIMARY_SOURCES` | proof floor | reduces vanity analysis |
| `N01_EVIDENCE_TARGET` | stopping threshold | keeps output from pretending certainty |
| `N01_MAX_RESULTS_PER_SCAN` | breadth control | balances coverage vs noise |
| `N01_TIME_HORIZON_DAYS` | freshness bound | prevents stale benchmark worship |
| `N01_BUDGET_TOKENS_DAY` | cost cap | stops deep research from becoming waste |
| `N01_ENABLE_COUNTER_SIGNALS` | contradiction search toggle | makes envy rigorous instead of one-sided |
| `N01_RUN_CONTEXT_PATH` | runtime path anchor | keeps tool state predictable |
| `N01_PROVIDER_API_KEY_REF` | secret pointer | clean separation from secret config |
| `N01_TRACING_ENABLED` | audit logging | supports post hoc governance |

## Override Precedence

| Priority | Source | Why |
|---------|--------|-----|
| 1 | process environment | deploy-time truth |
| 2 | `.env.local` or runner file | developer convenience |
| 3 | frontmatter default in this artifact | documented baseline |

## Sensitive Handling

| Variable | Exposure Rule | Storage Guidance |
|---------|---------------|------------------|
| `N01_PROVIDER_API_KEY_REF` | log pointer only | resolve via `con_secret_config_n01.md` |
| `N01_DEFAULT_PROVIDER` | safe to log | useful for debugging routes |
| `N01_DEFAULT_MODEL` | safe to log | useful for benchmark audits |

## Rationale

| Design Choice | Why | Analytical Envy Interpretation |
|--------------|-----|--------------------------------|
| Evidence target in env | lets runtime bias all requests upward | environment can institutionalize proof pressure |
| Counter-signal toggle | contradiction search should be a first-class behavior | envy must test itself against rival evidence |
| Model and provider split | route quality and cost independently | lets N01 compare depth and spend cleanly |
| Secret as ref only | keeps config auditable and non-leaky | rigor includes operational hygiene |
| Daily token budget | depth must answer to cost | disciplined envy spends where advantage matters |

## Example

```env
N01_DEFAULT_PROVIDER=openai
N01_DEFAULT_MODEL=gpt-5.4
N01_RESEARCH_MODE=comparative
N01_MIN_PRIMARY_SOURCES=3
N01_EVIDENCE_TARGET=benchmark_mapped
N01_MAX_RESULTS_PER_SCAN=10
N01_TIME_HORIZON_DAYS=45
N01_BUDGET_TOKENS_DAY=180000
N01_ENABLE_COUNTER_SIGNALS=true
N01_RUN_CONTEXT_PATH=.cex/runtime
N01_PROVIDER_API_KEY_REF=sec_n01_llm_provider
N01_TRACING_ENABLED=true
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `env_config` |
| Pillar | `P09` |
| Nucleus | `n01` |
| Environment | `all` |
| Variable Count | `12` |
| Sensitive Count | `1` |
| Override Model | `env > file > default` |
| Quality Field | `null` |
