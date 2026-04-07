---
kind: output_template
id: bld_output_template_prompt_cache
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for prompt_cache production
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: prompt_cache
```yaml
---
id: p10_pc_{{name_slug}}
kind: prompt_cache
pillar: P10
title: "{{Name}} Prompt Cache Config"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{builder_name}}"
ttl_seconds: {{seconds}}
eviction_strategy: {{lru|lfu|fifo}}
max_entries: {{count}}
cache_key_method: {{hash_full|hash_prefix|semantic}}
invalidation_trigger: {{ttl_expire|content_change|manual}}
storage_backend: {{memory|redis|sqlite}}
domain: {{domain_name}}
quality: null
tags: [prompt_cache, {{tag1}}, {{tag2}}]
tldr: "{{Dense <=160ch cache config summary}}"
---

# {{Name}} Prompt Cache Config

## Cache Strategy
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| TTL | {{seconds}}s | {{freshness justification}} |
| Eviction | {{strategy}} | {{workload justification}} |
| Max entries | {{count}} | {{memory budget justification}} |
| Expected hit rate | {{percentage}}% | {{based on query repetition}} |

## Key Method
- **Method**: {{cache_key_method}}
- **Hash input**: {{what gets hashed — full prompt, prefix, embedding}}
- **Namespace**: {{agent_id or domain for isolation}}
- **Collision handling**: {{strategy}}

## Invalidation Rules
| Trigger | Condition | Action |
|---------|-----------|--------|
| TTL expire | entry age > {{ttl}}s | evict |
| Content change | {{knowledge artifact version changes}} | flush affected |
| Manual | {{operator command}} | flush namespace |

## Storage Backend
| Property | Value |
|----------|-------|
| Backend | {{memory/redis/sqlite}} |
| Scaling | {{single-process/multi-agent/persistent}} |
| Memory budget | {{estimated MB}} |

## Integration
- Consumed by: agent_card, runtime_state, model_provider
- Provider caching: {{provider-specific notes (Anthropic explicit, OpenAI auto)}}
```
