---
id: p10_lr_context_map_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
observation: "Context maps without explicit pattern labels (ACL/OHS/Conformist) become obsolete within 6 months -- teams add integrations without updating the map. Conformist relationships without ACL planning become painful coupling over time. Maps that omit team ownership leave architectural governance gaps."
pattern: "Label every relationship with DDD pattern. Flag Conformist as temporary -- plan ACL migration. Include team ownership per BC. Review map quarterly."
evidence: "6 architecture reviews: 4 had unlabeled relationships causing confusion; 3 Conformist without ACL plan became blocking dependencies within 12 months."
confidence: 0.87
outcome: SUCCESS
domain: context_map
tags: [context-map, ddd, bounded-context, ACL, conformist, team-coupling]
tldr: "Labeled DDD patterns + team ownership + Conformist-to-ACL migration plan = maintainable context map. Unlabeled maps decay within months."
impact_score: 8.0
decay_rate: 0.03
agent_group: edison
keywords: [context map, DDD, ACL, conformist, OHS, bounded context, team coupling, strategic design]
memory_scope: project
observation_types: [feedback, project]
quality: 8.9
title: "Memory Context Map"
density_score: 0.90
llm_function: INJECT
related:
  - bld_schema_sandbox_spec
  - bld_schema_integration_guide
  - bld_schema_safety_policy
  - bld_schema_ai_rmf_profile
  - bld_schema_reranker_config
  - bld_schema_pitch_deck
  - bld_collaboration_white_label_config
  - bld_schema_sandbox_config
  - bld_collaboration_contributor_guide
  - bld_schema_search_strategy
---

## Summary

Context maps without DDD pattern labels become useless documentation within months.
The key discipline: every relationship gets a named pattern, every BC gets a team owner,
and every Conformist relationship gets an ACL migration plan.

## Pattern

**Named pattern + team owner + Conformist migration plan.**

Relationship discipline:
1. Every relationship labeled with: ACL / OHS / Conformist / Partnership / Shared_Kernel
2. Direction explicit: upstream (U) vs downstream (D)
3. Integration_type declared: sync / async / batch

Team ownership discipline:
1. Every BC has one owning team
2. Team coupling risk documented per relationship
3. Conformist relationships flagged with "MIGRATION RISK" annotation

ACL discipline:
1. Prefer ACL over Conformist for any non-trivial integration
2. ACL translation layer owned by downstream team
3. OHS preferred when upstream can formalize their API

## Anti-Pattern

1. Unlabeled "integration" relationships -- no pattern insight, map becomes stale
2. Conformist everywhere -- upstream changes cascade to all downstream
3. No team ownership -- governance gap, nobody updates the map
4. Shared Kernel for everything -- tight coupling across teams, joint release trains
5. Missing integration_type -- sync vs async matters for fault isolation strategy

## Evidence Table

| Issue | Impact | Fix |
|-------|--------|-----|
| 4/6 reviews: unlabeled relationships | Confusion after 6 months | Label every relationship with DDD pattern |
| 3 Conformist w/o ACL plan | Blocking dependencies in 12 months | Flag + plan ACL migration |
| No team ownership | Nobody updates the map | Assign owning team per BC |

## Pattern Migration Guide

| From | To | When | Steps |
|------|----|------|-------|
| Conformist | ACL | Models diverging | 1. Define ACL translator, 2. Gradual migration, 3. Update map |
| Customer/Supplier | OHS | Upstream stabilizes | 1. Formalize API, 2. Publish language, 3. Update pattern |
| Partnership | OHS | Teams scaling independently | 1. Define formal protocol, 2. Add versioning, 3. Update pattern |

## Application Checklist

| Check | Question | Pass Condition |
|-------|----------|----------------|
| Pattern labels | Every relationship labeled? | Yes, ACL/OHS/Conformist/Partnership |
| Team ownership | Every BC has owning team? | Yes |
| Conformist plan | All Conformist flagged? | Yes, with ACL migration path |
| Integration type | All relationships typed? | Yes, sync/async/batch |
| Direction | All upstream/downstream explicit? | Yes, U/D notation |

## Coupling Severity Matrix

| Pattern | Release Coupling | Model Coupling | Recommended Action |
|---------|-----------------|---------------|-------------------|
| ACL | None | None | Maintain translator |
| OHS | None | Loose | Maintain API contract |
| Conformist | Loose | HIGH | Plan ACL migration |
| Customer/Supplier | Medium | Medium | Maintain backlog priority |
| Partnership | HIGH | HIGH | Coordinate release trains |
| Shared Kernel | VERY HIGH | VERY HIGH | Minimize scope aggressively |
| Shared Kernel | VERY HIGH | VERY HIGH | Minimize scope, consider alternatives |
| bc_language | Ubiquitous language documented? | Yes, key domain terms listed |
| relationships_count | matches body table rows? | Yes |
| patterns valid | Only ACL/OHS/Conformist/Partnership/Shared_Kernel? | Yes |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_sandbox_spec]] | upstream | 0.19 |
| [[bld_schema_integration_guide]] | upstream | 0.18 |
| [[bld_schema_safety_policy]] | upstream | 0.18 |
| [[bld_schema_ai_rmf_profile]] | upstream | 0.17 |
| [[bld_schema_reranker_config]] | upstream | 0.17 |
| [[bld_schema_pitch_deck]] | upstream | 0.17 |
| [[bld_collaboration_white_label_config]] | downstream | 0.17 |
| [[bld_schema_sandbox_config]] | upstream | 0.17 |
| [[bld_collaboration_contributor_guide]] | downstream | 0.17 |
| [[bld_schema_search_strategy]] | upstream | 0.17 |
