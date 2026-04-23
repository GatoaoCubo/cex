---
kind: knowledge_card
id: bld_knowledge_card_learning_record
pillar: P10
llm_function: INJECT
purpose: Domain knowledge for learning_record production — atomic searchable facts
sources: learning-record-builder MANIFEST.md + SCHEMA.md v1.0.0
quality: 9.1
title: "Knowledge Card Learning Record"
version: "1.0.0"
author: n03_builder
tags: [learning_record, builder, examples]
tldr: "Golden and anti-examples for learning record construction, demonstrating ideal structure and common pitfalls."
domain: "learning record construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_memory_learning_record
  - p03_ins_learning_record
  - skill_memory_update
  - p03_sp_learning_record_builder
  - bld_schema_learning_record
  - bld_collaboration_learning_record
  - p11_qg_learning_record
  - bld_knowledge_card_reasoning_trace
  - p01_kc_learning_record
  - p03_sp_reasoning_trace_builder
---

# Domain Knowledge: learning_record
## Executive Summary
Learning records are persistent experience captures — structured retrospectives that codify what worked, what failed, and under what conditions the outcome is reproducible. Each record documents ONE experience event with raw observation, extracted pattern, and supporting evidence scored by confidence. They differ from knowledge cards (external facts), session state (ephemeral context), and axioms (abstract truths) by encoding lived operational experience with confidence scoring and temporal decay.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P10 (memory) |
| Kind | `learning_record` (exact literal) |
| ID pattern | `p10_lr_{slug}` |
| Required frontmatter | 10 fields |
| Extended frontmatter | 12 (confidence, outcome, impact_score, decay_rate, etc.) |
| Body sections | 7 required |
| Max body | 4096 bytes |
| Density minimum | >= 0.80 |
| Confidence range | 0.0-1.0 |
| Outcome values | SUCCESS, PARTIAL, FAILURE |
| Default decay_rate | 0.03 (half-life ~23 days) |
## Patterns
| Pattern | Application |
|---------|-------------|
| Three-field pipeline | observation (raw facts) -> pattern (reproducible rule) -> evidence (metrics) |
| Confidence calibration | 0.9+ only with 10+ observations; 0.3 for single observation |
| Concrete patterns | Replicable steps, not vague advice ("run X before Y" not "be careful") |
| Decay-aware records | High decay (0.10+) for time-sensitive; 0.01 for stable patterns |
| Semantic links | Typed relations: caused_by, refines, contradicts, enables, depends_on |
| Outcome honesty | PARTIAL when some goals met — never round up to SUCCESS |
### Confidence Scale
| Score | Basis |
|-------|-------|
| 0.9-1.0 | 10+ observations, consistent |
| 0.7-0.8 | 5-9 observations |
| 0.5-0.6 | 2-4 observations |
| 0.3-0.4 | 1 observation |
| 0.0-0.2 | Theoretical only |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Vague pattern ("be more careful") | Non-reproducible; fails density gate |
| Observation contains judgment | Observation = raw facts only |
| confidence: 0.9 for single event | Overstated; use 0.3-0.4 |
| Missing evidence field | Pipeline incomplete without before/after metrics |
| outcome: SUCCESS when partial | Inflates confidence; downstream routing breaks |
| Body > 4096 bytes | Exceeds max_bytes; split into focused records |
## Application
1. Capture `observation` as raw facts only — no interpretation
2. Extract `pattern`: the reproducible rule or mechanism discovered
3. Add `evidence`: concrete metrics, before/after data
4. Set `outcome`: SUCCESS / PARTIAL / FAILURE
5. Calibrate `confidence` against the scale (observations count)
6. Set `impact_score` (0.0-10.0) and `decay_rate` (default 0.03)
7. Write all 7 body sections; validate 9 HARD + 12 SOFT gates
## References
- learning-record-builder SCHEMA.md v1.0.0
- P10 memory pillar
- Experiential learning theory (Kolb cycle)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_learning_record]] | related | 0.61 |
| [[p03_ins_learning_record]] | upstream | 0.40 |
| [[skill_memory_update]] | related | 0.35 |
| [[p03_sp_learning_record_builder]] | upstream | 0.35 |
| [[bld_schema_learning_record]] | upstream | 0.32 |
| [[bld_collaboration_learning_record]] | related | 0.29 |
| [[p11_qg_learning_record]] | downstream | 0.28 |
| [[bld_knowledge_card_reasoning_trace]] | sibling | 0.26 |
| [[p01_kc_learning_record]] | sibling | 0.25 |
| [[p03_sp_reasoning_trace_builder]] | upstream | 0.23 |
