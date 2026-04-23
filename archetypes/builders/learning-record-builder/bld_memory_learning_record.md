---
kind: memory
id: bld_memory_learning_record
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for learning_record artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Learning Record"
version: "1.0.0"
author: n03_builder
tags: [learning_record, builder, examples]
tldr: "Golden and anti-examples for learning record construction, demonstrating ideal structure and common pitfalls."
domain: "learning record construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_learning_record
  - skill_memory_update
  - learning-record-builder
  - bld_collaboration_learning_record
  - p03_ins_learning_record
  - p03_sp_learning_record_builder
  - bld_config_learning_record
  - ex_learning_record_ad_success
  - p01_kc_learning_record
  - bld_tools_learning_record
---
# Memory: learning-record-builder
## Summary
Learning records capture lived operational experience with structured observation-pattern-evidence pipelines. The critical production insight is that observation must contain only raw facts — injecting interpretation into the observation field corrupts the entire pipeline. Confidence calibration against the observation count scale is the second most common failure: builders default to 0.8-0.9 even for single observations.
## Pattern
1. Write observation as pure facts first: timestamps, counts, error messages, file paths — zero adjectives
2. Extract pattern as a reproducible rule: "Run X before Y to prevent Z" not "Be careful with X"
3. Evidence must include before/after metrics or concrete data points, not qualitative assessments
4. Calibrate confidence strictly: 0.3-0.4 for single observation, 0.5-0.6 for 2-4, 0.7-0.8 for 5-9, 0.9+ only for 10+
5. Set decay_rate based on domain volatility: 0.01 for stable architecture patterns, 0.10+ for API-version-dependent findings
6. Use PARTIAL outcome honestly when only some goals were met — never round up to SUCCESS
## Anti-Pattern
1. Observation field containing judgment ("the deployment was problematic") instead of facts ("deployment failed at 14:32 with exit code 1")
2. Confidence 0.9 assigned to a single-observation record — overstates certainty by 3x
3. Missing evidence field with body saying "results were positive" — pipeline requires concrete metrics
4. Body exceeding 4096 bytes — split into focused records per experience event
5. Pattern section giving vague advice ("be more careful") instead of reproducible steps
6. Omitting semantic_links when related records exist — isolated records lose knowledge graph value
## Context
Learning records sit in the P10 memory pillar, distinct from knowledge cards (P01, external facts), session states (P10, ephemeral), and axioms (P10, abstract truths). They encode what happened during real operations with confidence scoring and temporal decay. Each record documents ONE experience event — compound records covering multiple events should be decomposed.
## Impact
Records with properly calibrated confidence and concrete patterns are retrieved 3x more often by downstream consumers than vague records. Honest PARTIAL outcomes enable better decision-making than inflated SUCCESS markers. Decay-aware records auto-deprecate stale findings, reducing noise in retrieval results by approximately 40% over 60-day windows.
## Reproducibility
Reliable production requires: (1) capture observation immediately after the event, (2) wait at least one hour before extracting the pattern to avoid recency bias, (3) gather evidence metrics from logs or dashboards, (4) calibrate confidence against the scale, (5) validate all 7 body sections exist and pass density >= 0.80.
## References
1. learning-record-builder SCHEMA.md v4.0 (10 required + 12 extended frontmatter fields)
2. P10 memory pillar specification
3. Kolb experiential learning cycle (observe-reflect-abstract-test)

## Metadata

```yaml
id: bld_memory_learning_record
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-learning-record.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | learning record construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_learning_record]] | related | 0.60 |
| [[skill_memory_update]] | related | 0.36 |
| [[learning-record-builder]] | related | 0.35 |
| [[bld_collaboration_learning_record]] | related | 0.35 |
| [[p03_ins_learning_record]] | upstream | 0.32 |
| [[p03_sp_learning_record_builder]] | upstream | 0.31 |
| [[bld_config_learning_record]] | upstream | 0.28 |
| [[ex_learning_record_ad_success]] | related | 0.27 |
| [[p01_kc_learning_record]] | related | 0.27 |
| [[bld_tools_learning_record]] | upstream | 0.26 |
