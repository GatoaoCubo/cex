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
