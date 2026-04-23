---
kind: collaboration
id: bld_collaboration_capability_registry
pillar: P12
llm_function: COLLABORATE
purpose: How capability_registry-builder works in crews with other builders
quality: 9.0
title: "Collaboration Capability Registry"
version: "1.0.0"
author: n04_wave8
tags: [capability_registry, builder, collaboration, crew, orchestration]
tldr: "How capability_registry-builder works in crews with other builders"
domain: "capability_registry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - capability-registry-builder
  - bld_collaboration_agent
  - agent-builder
  - p01_kc_agent
  - bld_collaboration_agent_computer_interface
  - bld_collaboration_nucleus_def
  - p12_wf_create_orchestration_agent
  - bld_architecture_agent
  - p03_sp_capability_registry_builder
  - bld_knowledge_card_capability_registry
---

## Crew Role
Provides the discovery backbone for crew orchestration. Before any wave is dispatched, the orchestrator can query the capability registry to find ranked agent candidates for each task. This prevents hardcoded routing and enables dynamic crew composition.

## Receives From
| Source                    | What                                | Format      |
|---------------------------|-------------------------------------|-------------|
| .claude/agents/           | 252 builder sub-agent definitions   | Markdown    |
| N0x_*/agents/             | Nucleus domain agent definitions    | Markdown    |
| N0x_*/agent_card_n0x.md   | Nucleus-level capability cards      | Markdown    |
| cex_score.py output       | Quality baseline scores             | YAML/JSON   |
| .cex/kinds_meta.json      | Kind-to-pillar mapping              | JSON        |

## Produces For
| Consumer              | What                                    | Format      |
|-----------------------|------------------------------------------|-------------|
| N07 Orchestrator      | Ranked agent candidates for a query      | Markdown table |
| crew_runner.py        | Agent selection inputs                   | YAML        |
| dispatch.sh           | Agent routing decisions                  | CLI args    |
| gap analysis tools    | Coverage gaps per domain                 | Markdown table |

## Boundary
Does NOT execute agents or write handoffs (handled by N07 + dispatch.sh).
Does NOT manage agent lifecycles or update agent definitions (handled by N03 builders).
Does NOT perform semantic search at inference time (handled by cex_retriever.py + cex_query.py).
Legal and compliance review of agent capabilities is handled by N05.
Re-indexing on agent addition/removal is triggered by F8 COLLABORATE in the producing builder.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[capability-registry-builder]] | upstream | 0.45 |
| [[bld_collaboration_agent]] | sibling | 0.42 |
| [[agent-builder]] | upstream | 0.39 |
| [[p01_kc_agent]] | upstream | 0.36 |
| [[bld_collaboration_agent_computer_interface]] | sibling | 0.35 |
| [[bld_collaboration_nucleus_def]] | sibling | 0.34 |
| [[p12_wf_create_orchestration_agent]] | related | 0.34 |
| [[bld_architecture_agent]] | upstream | 0.32 |
| [[p03_sp_capability_registry_builder]] | upstream | 0.31 |
| [[bld_knowledge_card_capability_registry]] | upstream | 0.31 |
