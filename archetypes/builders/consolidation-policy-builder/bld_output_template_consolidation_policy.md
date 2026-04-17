---
kind: output_template
id: bld_output_template_consolidation_policy
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for consolidation_policy production
quality: 9.1
title: "Output Template: consolidation_policy"
version: "2.0.0"
author: n06_commercial
tags: [consolidation_policy, builder, output_template]
tldr: "Template for LLM agent memory consolidation policy artifacts: promotion rules, eviction strategy, importance scoring, tier matrix, compliance"
domain: "LLM agent memory consolidation"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
---

```yaml
---
id: p10_cp_{{agent_slug}}
kind: consolidation_policy
pillar: P10
title: "Consolidation Policy: {{agent_name}}"
version: "1.0.0"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{agent_domain}}"
quality: null
tags: [consolidation_policy, {{agent_slug}}, {{tier}}]
tldr: "{{one_sentence_summary}}"
tier: "{{tier}}"
eviction_strategy: "{{strategy}}"
consolidation_async: true
importance_floor: {{importance_floor}}
retention_days: {{retention_days}}
promotion_threshold: {{promotion_threshold}}
audit_trail: {{true_or_false}}
---
```

<!-- id: Unique identifier following ^p10_cp_[a-z][a-z0-9_]+ -->
<!-- agent_slug: snake_case agent name (e.g., customer_support_v2) -->
<!-- tier: free | pro | enterprise -->
<!-- strategy: lru | lfu | ttl | importance | generational | hybrid -->
<!-- importance_floor: float 0-1, below this = evict (e.g., 0.3) -->
<!-- retention_days: integer, TTL for episodic memory (e.g., 90) -->
<!-- promotion_threshold: float 0-1, above this = promote to semantic (e.g., 0.7) -->

## Overview

{{agent_name}} memory consolidation policy for {{agent_domain}}. Tier: {{tier}}.
Strategy: {{strategy}}. Reference: MemGPT/Letta pipeline with importance scoring.

## Promotion Rules

| Trigger | Source Layer | Target Layer | Condition | Action |
|---------|-------------|-------------|-----------|--------|
| Session end | Working | Episodic | Always | Save conversation to episodic store |
| Importance > {{promotion_threshold}} | Episodic | Semantic | importance_score > {{promotion_threshold}} | Extract facts, write to semantic store |
| Merge check | Episodic | Episodic | Similarity > 0.92 with existing entry | Merge into canonical record |

<!-- Add/remove rows based on active layers. Free tier: no rows needed. -->

## Eviction Rules

| Layer | Strategy | Trigger | Action |
|-------|----------|---------|--------|
| Working | FIFO + summarize | Token budget > 80% | Summarize oldest 20% out of context |
| Episodic | TTL + importance | Age > {{retention_days}}d OR importance < {{importance_floor}} | Archive to cold storage, then delete after {{archive_hold_days}}d |
| Semantic | LRU + staleness | Last accessed > 180d AND no entity links | Soft-delete + audit log entry |

<!-- Remove rows for layers not active in this tier. -->

## Importance Scoring

```
importance_score = (
    recency_weight * recency_score(entry) +
    frequency_weight * access_frequency(entry) +
    user_signal_weight * explicit_feedback(entry)
)
```

- `recency_score`: 1.0 for today, decays by Ebbinghaus forgetting curve over {{decay_days}} days
- `access_frequency`: normalized count of retrievals in last 30 days
- `explicit_feedback`: 1.0 if user explicitly referenced, 0.0 if never accessed
- Weights: recency={{recency_weight}}, frequency={{frequency_weight}}, signal={{user_signal_weight}}

## Consolidation Job

- Trigger: async, fires on session end
- Schedule: also runs nightly at {{nightly_schedule}} for replay sweep
- Timeout: {{consolidation_timeout_seconds}}s per batch of {{batch_size}} entries
- Failure handling: log error, skip failed entry, retry next cycle (max {{max_retries}} retries)
- Concurrency: single-threaded per agent instance; multi-agent safe via distributed lock

## Commercial Tier Matrix

| Feature | Free | Pro | Enterprise |
|---------|------|-----|------------|
| Consolidation | None | Session-end async | Session-end + nightly sweep |
| Episodic retention | None | {{pro_retention_days}} days | Custom (1y / indefinite) |
| Semantic promotion | None | Auto (importance > {{promotion_threshold}}) | Scheduled + audited |
| Importance scoring | None | Recency + frequency | Recency + frequency + user signals |
| Merge/dedup | None | Similarity-based | LLM-driven + manual review queue |
| Compliance | N/A | Basic TTL | GDPR + HIPAA + data residency |
| Audit trail | None | Read-only | Full write + export + GDPR Art. 17 |

## Compliance Config

<!-- Required for enterprise tier. Remove section for free/pro. -->

```yaml
compliance:
  retention_days: {{retention_days}}
  data_residency: "{{region}}"
  gdpr_erasure:
    enabled: true
    hard_delete: true
    audit_log: true
    max_erasure_latency_hours: 24
  audit_trail:
    enabled: true
    log_promotions: true
    log_evictions: true
    export_format: "jsonl"
    retention_days: 365
```
