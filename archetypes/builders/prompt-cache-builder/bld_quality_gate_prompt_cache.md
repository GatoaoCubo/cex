---
id: p11_qg_prompt_cache
kind: quality_gate
pillar: P11
title: "Gate: Prompt Cache"
version: "1.0.0"
created: "2026-04-07"
updated: "2026-04-07"
author: "n04_knowledge"
domain: "prompt_cache — TTL, eviction, and invalidation for cached LLM prompt/completion pairs"
quality: 9.0
tags: [quality-gate, prompt-cache, ttl, eviction, caching]
tldr: "Gates ensuring prompt_cache artifacts have valid TTL, eviction, key method, invalidation, and storage config."
density_score: 0.90
llm_function: GOVERN
---
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
