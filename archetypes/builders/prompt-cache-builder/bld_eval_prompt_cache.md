---
kind: quality_gate
id: p11_qg_prompt_cache
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of prompt_cache artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: Prompt Cache"
version: "1.0.0"
author: "n04_knowledge"
tags: [quality-gate, prompt-cache, ttl, eviction, caching]
tldr: "Gates ensuring prompt_cache artifacts have valid TTL, eviction, key method, invalidation, and storage config."
domain: "prompt_cache — TTL, eviction, and invalidation for cached LLM prompt/completion pairs"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_prompt_cache
  - p01_kc_prompt_cache
  - bld_output_template_prompt_cache
  - bld_instruction_prompt_cache
  - prompt-cache-builder
  - p03_sp_prompt_cache_builder
  - bld_schema_prompt_cache
  - bld_knowledge_card_prompt_cache
  - bld_collaboration_prompt_cache
  - bld_architecture_prompt_cache
---

## Quality Gate

# Gate: Prompt Cache
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: prompt_cache` |
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | ID matches `^p10_pc_[a-z][a-z0-9_]+$` | Wrong prefix |
| H03 | Kind equals literal `prompt_cache` | Wrong kind |
| H04 | Quality field is `null` | Non-null value |
| H05 | ttl_seconds is positive integer | Zero, negative, or non-integer |
| H06 | eviction_strategy is valid enum | Not in lru/lfu/fifo |
| H07 | cache_key_method is valid enum | Not in hash_full/hash_prefix/semantic |
| H08 | invalidation_trigger is valid enum | Not in ttl_expire/content_change/manual |
| H09 | storage_backend is valid enum | Not in memory/redis/sqlite |
| H10 | Total file <= 2048 bytes | Exceeds limit |
## SOFT Scoring
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | TTL justification | 1.0 | TTL matched to freshness needs | Reasonable default | Arbitrary value |
| S02 | Eviction rationale | 1.0 | Strategy matched to workload | Default LRU | No rationale |
| S03 | Hit rate estimate | 0.5 | Expected rate documented | Mentioned | Not present |
| S04 | Invalidation detail | 1.0 | Trigger + conditions + actions | Trigger only | No rules |
| S05 | Namespace isolation | 0.5 | Agent/domain namespacing | Partial | No isolation |
| S06 | Provider integration | 0.5 | Provider-specific caching notes | Mentioned | Not addressed |

## Cross-References

- **Pillar**: P11 (Feedback)
- **Kind**: `quality gate`
- **Artifact ID**: `p11_qg_prompt_cache`
- **Tags**: [quality-gate, prompt-cache, ttl, eviction, caching]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P11 | Feedback domain |
| Kind `quality gate` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Examples

# Examples: prompt-cache-builder
## Golden Example
INPUT: "Create prompt cache config for RAG agent with shared system prompts"
OUTPUT:
```yaml
---
id: p10_pc_rag_agent_shared
kind: prompt_cache
pillar: P10
title: "RAG Agent Shared Prompt Cache"
version: "1.0.0"
created: "2026-04-07"
updated: "2026-04-07"
author: "prompt-cache-builder"
ttl_seconds: 3600
eviction_strategy: lru
max_entries: 5000
cache_key_method: hash_prefix
invalidation_trigger: content_change
storage_backend: redis
domain: rag_pipeline
quality: null
tags: [prompt_cache, rag, shared, prefix-caching]
tldr: "RAG shared cache: prefix hashing, 1h TTL, LRU eviction, Redis backend for multi-agent reuse"
---
# Prefix caching: system_prompt + few-shot cached (stable), RAG context varies.
# Expected hit rate: ~60% (shared system prefix across agents).
# Invalidation: content_change triggers flush when KB artifacts update.
```
WHY THIS IS GOLDEN:
1. quality: null
2. All required fields present with valid enum values
3. cache_key_method=hash_prefix matches use case (shared system prompts)
4. storage_backend=redis for multi-agent sharing
5. invalidation_trigger=content_change (accurate for RAG)

## Anti-Example
BAD OUTPUT:
```yaml
id: cache_config
ttl_seconds: 999999
eviction_strategy: random
cache_key_method: whatever
quality: 9.5
```
FAILURES:
1. id: no p10_pc_ prefix
2. ttl: unreasonably high (11.5 days)
3. eviction: "random" not valid enum
4. cache_key_method: "whatever" not valid enum
5. quality: not null

## Properties

| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P07 |
| Domain | prompt cache construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
