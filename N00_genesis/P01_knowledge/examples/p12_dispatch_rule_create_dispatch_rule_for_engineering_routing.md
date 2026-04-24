---
id: p12_dr_engineering
kind: dispatch_rule
8f: F8_collaborate
pillar: P12
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: dispatch-rule-builder
domain: engineering
quality: 9.0
tags: [dispatch, engineering, builder, coding, development]
tldr: Route engineering, development and coding tasks to builder agent_group with opus model
scope: engineering
keywords: [engenharia, engineering, codigo, code, desenvolver, develop, programar, program, build, construir, implementar, implement, software, app]
agent_group: builder
model: opus
priority: 8
confidence_threshold: 0.75
fallback: executor
conditions:
  exclude_domains: [research_papers, marketing_copy]
routing_strategy: hybrid
density_score: 0.79
title: "P12 Dispatch Rule Create Dispatch Rule For Engineering Routing"
related:
  - p12_dr_test
  - p12_dr_creation
  - p12_dr_orchestration
  - dispatch-rule-builder
  - bld_collaboration_dispatch_rule
  - bld_architecture_kind
  - bld_architecture_dispatch_rule
  - p03_sp_engineering_nucleus
  - kind-builder
  - p10_lr_dispatch_rule_builder
---
# engineering Dispatch Rule

## Purpose
Routes software engineering, development, and coding tasks to the builder agent_group. The builder specializes in artifact creation, code implementation, and technical scaffolding with access to opus model for complex engineering reasoning and multi-step development tasks.

## Keyword Rationale
Bilingual PT/EN coverage captures both Portuguese operator commands ("desenvolver app") and English technical descriptions ("implement authentication"). Keywords span the full engineering lifecycle from high-level "engenharia" to specific actions like "programar" and "implementar". Generic terms like "software" and "app" catch domain-adjacent requests.

## Fallback Logic
Routes to executor when builder is unavailable. Executor handles operational aspects of engineering like testing, deployment, and code review, providing complementary engineering capabilities when primary builder agent_group cannot accept the task.

## Cross-References

- **Pillar**: P12 (Orchestration)
- **Kind**: `dispatch rule`
- **Artifact ID**: `p12_dr_engineering`
- **Tags**: [dispatch, engineering, builder, coding, development]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P12 | Orchestration domain |
| Kind `dispatch rule` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Artifact Metadata

```yaml
kind: dispatch_rule
pillar: P12
pipeline: 8F
scoring: hybrid_3_layer
compilation: cex_compile
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_dr_test]] | sibling | 0.41 |
| [[p12_dr_creation]] | sibling | 0.40 |
| [[p12_dr_orchestration]] | sibling | 0.35 |
| [[dispatch-rule-builder]] | related | 0.31 |
| [[bld_collaboration_dispatch_rule]] | related | 0.29 |
| [[bld_architecture_kind]] | upstream | 0.27 |
| [[bld_architecture_dispatch_rule]] | upstream | 0.27 |
| [[p03_sp_engineering_nucleus]] | upstream | 0.25 |
| [[kind-builder]] | upstream | 0.24 |
| [[p10_lr_dispatch_rule_builder]] | upstream | 0.24 |
