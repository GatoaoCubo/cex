---
id: con_rate_limit_config_n04
kind: rate_limit_config
pillar: P09
nucleus: n04
title: Knowledge Rate Limit Config
version: 1.0
quality: null
tags: [config, rate-limit, knowledge, budget, embeddings]
name: embeddings_default
provider: openai
rpm: 180
tpm: 900000
---
<!-- 8F: F1 constrain=P09/rate_limit_config F2 become=rate-limit-config-builder F3 inject=n04-knowledge+kc_rate_limit_config+P09 examples+N04 embedding usage F4 reason=throughput and budget guardrails for indexing-heavy knowledge work F5 call=shell,apply_patch F6 produce=4735 bytes F7 govern=frontmatter+ascii+density+80-line self-check F8 collaborate=N04_knowledge/config/con_rate_limit_config_n04.md -->
# Knowledge Rate Limit Config
## Purpose
N04 can generate large indexing bursts: embeddings, reranking, metadata enrichment, and freshness sweeps all compete for provider quota.
The Knowledge Gluttony lens means the nucleus would happily consume every source it sees, so this config defines the ceilings that keep appetite aligned with provider limits and budget.
This artifact governs request throughput, token flow, and spend for knowledge operations.
## Values
| Scope | Provider | RPM | TPM | Daily budget usd | Concurrency | Priority |
|-------|----------|-----|-----|------------------|-------------|----------|
| embeddings_default | openai | 180 | 900000 | 18 | 6 | high |
| rerank_default | anthropic | 40 | 180000 | 8 | 2 | medium |
| freshness_audit | anthropic | 20 | 90000 | 4 | 1 | medium |
| emergency_backfill | openai | 60 | 300000 | 6 | 2 | low unless approved |
| local_fallback | local | 9999 | 9999999 | 0 | 4 | reserve |
## Model Overrides
| Model | Provider | RPM | TPM | Usage |
|-------|----------|-----|-----|-------|
| text-embedding-3-large | openai | 180 | 900000 | primary embedding path |
| text-embedding-3-small | openai | 240 | 1200000 | cheaper recovery mode |
| claude-sonnet-4-6 | anthropic | 40 | 180000 | rerank and synthesis |
| claude-haiku-4-5 | anthropic | 80 | 220000 | lightweight audits |
## Backoff Policy
| Event | Action | Retry rule |
|-------|--------|------------|
| rpm >= 80 percent | warn and slow queue intake | wait 2-5s jitter |
| rpm >= 95 percent | stop admitting non-critical jobs | wait until rolling window clears |
| tpm >= 90 percent | reduce chunk fanout and use smaller model when allowed | exponential backoff |
| daily_budget >= 85 percent | restrict to freshness and user-requested jobs | manual review for backfills |
| provider 429 | honor provider retry-after if present | no blind immediate retry |
## Budget Allocation
| Workload | Budget usd | Why N04 spends here |
|----------|------------|---------------------|
| embeddings | 18 | gluttony for recall depends on vectors |
| reranking | 8 | high-value relevance correction |
| freshness audits | 4 | keeps stored knowledge from rotting |
| emergency backfill | 6 | reserve for sudden corpus updates |
| human-approved experiments | 2 | controlled exploration of better pipelines |
## Example
```yaml
provider: openai
name: embeddings_default
rpm: 180
tpm: 900000
daily_budget_usd: 18
concurrency: 6
backoff: exponential_with_jitter
budget_mode: restrict_noncritical_at_85_percent
```
## Rationale
| Decision | Knowledge Gluttony angle | Benefit |
|----------|--------------------------|---------|
| separate embeddings and reranking budgets | N04 craves both breadth and precision, but they have different value density | cost is allocated intentionally |
| preserve emergency reserve | appetite spikes during large imports | avoids total freeze when surprises land |
| local fallback lane | hunger for knowledge should not stop when paid APIs choke | continuity during outages |
| priority-aware slowdowns | gluttony needs triage, not total shutdown | important freshness jobs still run |
| explicit model overrides | different tasks digest different token volumes | better spend-performance balance |
## Monitoring Signals
| Metric | Alert threshold | Response |
|--------|-----------------|----------|
| openai embedding rpm | 150 | slow new backfills |
| anthropic rerank tpm | 160000 | reduce rerank batch size |
| daily spend | 85 percent | freeze experiments |
| queue age | 10 minutes | investigate provider or chunking pressure |
| 429 count | 3 in 15 min | switch to fallback mode |
## Properties
| Property | Value |
|----------|-------|
| Config scope | N04 provider usage |
| Workload classes | 5 |
| Paid providers | 2 |
| Local fallback present | yes |
| Budgeted workloads | 5 |
| Priority levels | 3 |
| Default backoff | exponential with jitter |
| Hard stop threshold | provider hard fail or budget exhaustion |
| Primary protected path | embeddings |
| Governance owner | N04 with N07 oversight for overruns |
