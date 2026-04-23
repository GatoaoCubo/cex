---
id: ex_learning_record_ad_success
kind: learning_record
pillar: P10
title: Ad Campaign Success Record
tags: [memory, learning, feedback, success]
references:
  - tpl_learning_record
  - ex_agent_copywriter
  - ex_quality_gate_copy
quality: 9.0
tldr: "Learning record: ad campaign that worked well. Captures what, why, and reuse conditions."
updated: "2026-04-07"
domain: "memory and state"
version: "1.0.0"
author: n03_builder
created: "2026-04-07"
density_score: 0.94
related:
  - learning-record-builder
  - bld_manifest_memory_type
  - memory-scope-builder
  - bld_collaboration_memory_type
  - bld_memory_learning_record
  - bld_architecture_learning_record
  - bld_tools_learning_record
  - p01_kc_learning_record
  - bld_config_learning_record
  - p01_kc_memory_scope
---

# Ad Campaign Success Record

> Skeleton: learning_record kind (the brain learns)

| Field | Value |
|-------|-------|
| Task | "ad for Python course" |
| Result | 42 sales in 3 days |
| Score | 9.2 (real, not estimated) |
| Lesson | AIDA + social proof + urgency = high conversion |

Next compilation will inject THIS as few_shot evidence.

## Links

1. Agent: [[ex_agent_copywriter]]
2. Gate used: [[ex_quality_gate_copy]]
3. Function: INJECT (memory feeds future hydration)

## Cross-References

1. **Pillar**: P10 (Memory)
2. **Kind**: `learning record`
3. **Artifact ID**: `ex_learning_record_ad_success`
4. **Tags**: [memory, learning, feedback, success]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P10 | Memory domain |
| Kind `learning record` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Artifact Metadata

```yaml
kind: learning_record
pillar: P10
pipeline: 8F
scoring: hybrid_3_layer
compilation: cex_compile
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[learning-record-builder]] | related | 0.31 |
| [[bld_manifest_memory_type]] | upstream | 0.29 |
| [[memory-scope-builder]] | upstream | 0.28 |
| [[bld_collaboration_memory_type]] | downstream | 0.28 |
| [[bld_memory_learning_record]] | related | 0.27 |
| [[bld_architecture_learning_record]] | upstream | 0.26 |
| [[bld_tools_learning_record]] | upstream | 0.25 |
| [[p01_kc_learning_record]] | related | 0.24 |
| [[bld_config_learning_record]] | upstream | 0.23 |
| [[p01_kc_memory_scope]] | upstream | 0.22 |
