---
id: p01_kc_meta_factory
kind: knowledge_card
type: domain
pillar: P01
title: "Meta-Factory — Builders that Build Builders"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: llm_patterns
quality: 9.0
tags: [meta, factory, builder, bootstrap, self-referential]
tldr: "A builder that produces other builders. Template + kind definition → specialized agent. CEX _builder-builder, AutoGPT agent-creator."
when_to_use: "System has >10 specialist agents with shared structure but different domains"
keywords: [meta-factory, builder-builder, template, bootstrap, self-referential]
density_score: 0.91
updated: "2026-04-07"
related:
  - p01_kc_meta_bootstrap
  - bld_collaboration_builder
  - kind-builder
  - bld_architecture_kind
  - _builder-builder
  - bld_config_capability_registry
  - bld_knowledge_card_builder
  - p01_kc_anti_isolated_sessions
  - capability-registry-builder
  - p01_kc_pattern_extraction
---

# Meta-Factory Pattern

## The Pattern
```
KIND DEFINITION → META-FACTORY → SPECIALIZED BUILDER → ARTIFACTS
```

## Industry Examples

| System | Meta-Factory | Produces |
|--------|-------------|----------|
| CEX | _builder-builder (13 meta-templates) | 105 builders |
| AutoGPT | Agent creator | Task-specific agents |
| CrewAI | Crew builder | Role-defined agents |
| LangChain | Chain factory | Task-specific chains |

## When to Use
1. >10 specialist agents needed
2. Agents share structural patterns
3. New agents added frequently
4. Consistency across agents matters

## Anti-Pattern
<5 agents → hand-craft. Meta-factory overhead exceeds benefit.

## Quality Criteria

| Dimension | Requirement | Weight |
|-----------|------------|--------|
| Factual accuracy | Verifiable claims only | 0.25 |
| Atomicity | One concept per card | 0.20 |
| Actionability | Reader knows next steps | 0.20 |
| Density | No filler sentences | 0.20 |
| Searchability | Tags enable retrieval | 0.15 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_meta_bootstrap]] | sibling | 0.44 |
| [[bld_collaboration_builder]] | downstream | 0.29 |
| [[kind-builder]] | downstream | 0.27 |
| [[bld_architecture_kind]] | downstream | 0.26 |
| [[_builder-builder]] | downstream | 0.26 |
| [[bld_config_capability_registry]] | downstream | 0.26 |
| [[bld_knowledge_card_builder]] | sibling | 0.24 |
| [[p01_kc_anti_isolated_sessions]] | sibling | 0.23 |
| [[capability-registry-builder]] | downstream | 0.23 |
| [[p01_kc_pattern_extraction]] | sibling | 0.22 |
