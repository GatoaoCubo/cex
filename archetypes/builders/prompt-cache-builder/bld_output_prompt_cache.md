---
kind: output_template
id: bld_output_template_prompt_cache
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for prompt_cache production
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.1
title: "Output Template Prompt Cache"
version: "1.0.0"
author: n03_builder
tags: [prompt_cache, builder, examples]
tldr: "Golden and anti-examples for prompt cache construction, demonstrating ideal structure and common pitfalls."
domain: "prompt cache construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p01_kc_prompt_cache
  - p11_qg_prompt_cache
  - prompt-cache-builder
  - bld_schema_prompt_cache
  - bld_examples_prompt_cache
  - bld_knowledge_card_prompt_cache
  - p03_sp_prompt_cache_builder
  - bld_architecture_prompt_cache
  - bld_instruction_prompt_cache
  - bld_collaboration_prompt_cache
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_prompt_cache]] | downstream | 0.50 |
| [[p11_qg_prompt_cache]] | downstream | 0.45 |
| [[prompt-cache-builder]] | downstream | 0.45 |
| [[bld_schema_prompt_cache]] | downstream | 0.43 |
| [[bld_examples_prompt_cache]] | downstream | 0.42 |
| [[bld_knowledge_card_prompt_cache]] | upstream | 0.42 |
| [[p03_sp_prompt_cache_builder]] | upstream | 0.41 |
| [[bld_architecture_prompt_cache]] | downstream | 0.40 |
| [[bld_instruction_prompt_cache]] | upstream | 0.37 |
| [[bld_collaboration_prompt_cache]] | downstream | 0.35 |
