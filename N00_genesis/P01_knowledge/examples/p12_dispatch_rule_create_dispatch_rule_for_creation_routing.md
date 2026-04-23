---
id: p12_dr_creation
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: dispatch-rule-builder
domain: creation
quality: 9.0
tags: [dispatch, creation, build, builder, artifact, scaffold, P12]
tldr: Route artifact creation and build tasks to builder nucleus via keyword and intent matching
scope: creation
keywords: [create, build, construct, scaffold, generate, implement, criar, construir, gerar, montar, produzir, implementar]
agent_group: builder
model: opus
priority: 8
confidence_threshold: 0.75
fallback: executor
conditions:
  exclude_domains: [research, marketing, deploy, monetization, knowledge_indexing]
load_balance: false
routing_strategy: hybrid
density_score: 0.78
title: "P12 Dispatch Rule Create Dispatch Rule For Creation Routing"
related:
  - p12_dr_test
  - p12_dr_orchestration
  - p12_dr_engineering
  - p10_lr_dispatch_rule_builder
  - p02_agent_creation_nucleus
  - p12_dr_builder_nucleus
  - bld_collaboration_dispatch_rule
  - agent_card_engineering_nucleus
  - p02_agent_builder_nucleus
  - agent_card_n03
---
# creation Dispatch Rule

## Purpose
Routes all artifact creation, build, and scaffolding tasks to the builder nucleus (N03).
Builder carries the full 8F pipeline, 114 builder archetypes, and CEX construction toolkit.
Any task requesting a new artifact, schema, template, component, or structured output routes here.
N03 is the authoritative executor for `create`, `build`, and `scaffold` intent signals.

## Keyword Rationale
Bilingual PT/EN coverage fires on both Portuguese operator commands and English task descriptions.
Verb forms (`create`, `build`, `construct`) capture direct construction intent.
`scaffold` and `generate` catch code-generation and template-instantiation sub-tasks.
PT variants (`criar`, `construir`, `gerar`, `montar`, `produzir`, `implementar`) ensure
multi-language operator commands route without fallback degradation.
Generic query verbs (`get`, `fetch`, `run`) deliberately excluded to avoid false matches
on read, query, or execution tasks that belong to executor or knowledge-engine.

## Fallback Logic
`executor` handles tasks at the intersection of build and run phases (e.g., code generation
followed by immediate execution, or artifact instantiation from existing templates).
Below 0.75 confidence, the router evaluates adjacent rules before activating fallback.
`executor` is preferred over `knowledge-engine` because partially-built artifacts need
execution capability, not indexing or retrieval.

## Cross-References

- **Pillar**: P12 (Orchestration)
- **Kind**: `dispatch rule`
- **Artifact ID**: `p12_dr_creation`
- **Tags**: [dispatch, creation, build, builder, artifact, scaffold, P12]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P12 | Orchestration domain |
| Kind `dispatch rule` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_dr_test]] | sibling | 0.42 |
| [[p12_dr_orchestration]] | sibling | 0.39 |
| [[p12_dr_engineering]] | sibling | 0.37 |
| [[p10_lr_dispatch_rule_builder]] | upstream | 0.35 |
| [[p02_agent_creation_nucleus]] | upstream | 0.33 |
| [[p12_dr_builder_nucleus]] | sibling | 0.31 |
| [[bld_collaboration_dispatch_rule]] | related | 0.30 |
| [[agent_card_engineering_nucleus]] | upstream | 0.25 |
| [[p02_agent_builder_nucleus]] | upstream | 0.25 |
| [[agent_card_n03]] | upstream | 0.25 |
