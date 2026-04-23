---
kind: collaboration
id: bld_collaboration_collaboration_pattern
pillar: P12
llm_function: COLLABORATE
purpose: How collaboration_pattern-builder works in crews with other builders
quality: 8.9
title: "Collaboration Collaboration Pattern"
version: "1.0.0"
author: wave1_builder_gen
tags: [collaboration_pattern, builder, collaboration]
tldr: "How collaboration_pattern-builder works in crews with other builders"
domain: "collaboration_pattern construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_collaboration_action_paradigm
  - bld_collaboration_builder
  - kind-builder
  - bld_collaboration_kind
  - bld_architecture_kind
  - bld_collaboration_handoff_protocol
  - bld_collaboration_handoff
  - bld_examples_handoff
  - bld_tools_kind
  - bld_collaboration_retriever_config
---

## Crew Role
Facilitates alignment, resolves conflicts, and ensures consistent communication among builders to maintain coherence in collaborative outputs.

## Receives From
| Builder      | What               | Format     |
|--------------|--------------------|------------|
| Design Builder | Design updates     | JSON       |
| Content Builder| Content drafts     | Markdown   |
| Code Builder   | Implementation feedback | Plain text |

## Produces For
| Builder      | What                   | Format     |
|--------------|------------------------|------------|
| All Builders | Coordination plan      | JSON       |
| Stakeholder Manager | Conflict resolution summary | Plain text |
| QA Builder   | Sync validation checklist | Markdown |

## Boundary
Does NOT execute tasks, manage workflows, or define handoff rules. Execution sequence is handled
by workflow builders; handoff rules by handoff_protocol builders; task routing by dispatch_rule
builders.

## Properties

| Property | Value |
|----------|-------|
| Kind | `collaboration` |
| Pillar | P12 |
| Domain | collaboration_pattern construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_action_paradigm]] | sibling | 0.36 |
| [[bld_collaboration_builder]] | sibling | 0.36 |
| [[kind-builder]] | upstream | 0.35 |
| [[bld_collaboration_kind]] | sibling | 0.34 |
| [[bld_architecture_kind]] | upstream | 0.33 |
| [[bld_collaboration_handoff_protocol]] | sibling | 0.32 |
| [[bld_collaboration_handoff]] | sibling | 0.30 |
| [[bld_examples_handoff]] | upstream | 0.29 |
| [[bld_tools_kind]] | upstream | 0.29 |
| [[bld_collaboration_retriever_config]] | sibling | 0.28 |
