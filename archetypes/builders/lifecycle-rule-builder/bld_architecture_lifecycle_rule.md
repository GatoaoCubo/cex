---
kind: architecture
id: bld_architecture_lifecycle_rule
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of lifecycle_rule — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Lifecycle Rule"
version: "1.0.0"
author: n03_builder
tags: [lifecycle_rule, builder, examples]
tldr: "Golden and anti-examples for lifecycle rule construction, demonstrating ideal structure and common pitfalls."
domain: "lifecycle rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_lifecycle_rule
  - bld_manifest_lifecycle_rule
  - bld_collaboration_lifecycle_rule
  - p03_sp_lifecycle_rule_builder
  - p11_qg_lifecycle_rule
  - bld_memory_lifecycle_rule
  - bld_knowledge_card_lifecycle_rule
  - bld_architecture_quality_gate
  - bld_schema_lifecycle_rule
  - p01_kc_lifecycle_rule
---

# Architecture: lifecycle_rule in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 21-field metadata header (id, kind, pillar, domain, target_kind, etc.) | lifecycle-rule-builder | active |
| state_definitions | Enumerated states an artifact can occupy (draft, active, deprecated, sunset) | author | active |
| transitions | Rules governing movement between states with criteria and triggers | author | active |
| temporal_triggers | Time-based conditions that initiate state changes (freshness, expiry) | author | active |
| review_cycles | Periodic review schedule with ownership and frequency | author | active |
| ownership_rules | Who is responsible for approving each state transition | author | active |
| scope_definition | Which artifact kinds and domains this lifecycle rule governs | author | active |
## Dependency Graph
```
artifact (any)  --governed_by-->  lifecycle_rule  --consumed_by-->  scheduler
quality_gate    --depends-->      lifecycle_rule  --signals-->      state_change_event
```
| From | To | Type | Data |
|------|----|------|------|
| lifecycle_rule | artifact (any) | dependency | artifacts must comply with lifecycle state rules |
| lifecycle_rule | scheduler | consumes | scheduler reads freshness triggers to schedule reviews |
| quality_gate (P11) | lifecycle_rule | dependency | gate scores may trigger promotion or demotion |
| scoring_rubric (P07) | lifecycle_rule | data_flow | score thresholds define promotion criteria |
| lifecycle_rule | state_change_event (P12) | signals | emitted when artifact transitions between states |
| hook (P04) | lifecycle_rule | dependency | hooks may execute actions on state transitions |
## Boundary Table
| lifecycle_rule IS | lifecycle_rule IS NOT |
|-------------------|----------------------|
| A declarative state machine for artifact lifecycle | An executable hook that fires on events (hook P04) |
| Defines states, transitions, and temporal triggers | A runtime behavior parameter (runtime_rule P09) |
| Governs freshness, promotion, deprecation, sunset | A pass/fail quality barrier (quality_gate P11) |
| Owned by a domain steward with review responsibility | A safety restriction on agent behavior (guardrail P11) |
| Applied to specific artifact kinds via scope | A universal operational mandate (law P08) |
| Evaluated periodically based on time or score | An on-demand validation check (validator P06) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Scope | frontmatter, scope_definition | Define which artifacts and domains are governed |
| States | state_definitions, ownership_rules | Enumerate valid states and who owns transitions |
| Transitions | transitions, temporal_triggers | Specify criteria and timing for state changes |
| Scheduling | review_cycles, scheduler | Periodic evaluation of artifact freshness |
| Events | state_change_event, hook | Notify downstream systems when transitions occur |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_lifecycle_rule]] | upstream | 0.47 |
| [[bld_manifest_lifecycle_rule]] | related | 0.46 |
| [[bld_collaboration_lifecycle_rule]] | downstream | 0.43 |
| [[p03_sp_lifecycle_rule_builder]] | upstream | 0.43 |
| [[p11_qg_lifecycle_rule]] | downstream | 0.42 |
| [[bld_memory_lifecycle_rule]] | downstream | 0.41 |
| [[bld_knowledge_card_lifecycle_rule]] | downstream | 0.38 |
| [[bld_architecture_quality_gate]] | sibling | 0.35 |
| [[bld_schema_lifecycle_rule]] | upstream | 0.31 |
| [[p01_kc_lifecycle_rule]] | downstream | 0.29 |
