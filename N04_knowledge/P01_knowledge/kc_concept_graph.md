---
quality: 8.8
quality: 8.0
id: kc_concept_graph
kind: knowledge_card
kc_type: meta_kc
pillar: P01
nucleus: n04
version: 1.0.0
created: "2026-04-19"
updated: "2026-04-19"
author: n04_knowledge
title: "Concept Graph -- CEX Prerequisite Dependency Map"
domain: didactic_engine
subdomain: teaching_engine
tags: [concept_graph, prerequisites, learning_path, mentor, journey, dependency, teaching]
tldr: "Directed prerequisite graph for all major CEX concepts. Used by /mentor journey to generate ordered learning paths. Root nodes have no prerequisites; leaf nodes require the full chain."
density_score: null
related:
  - p03_sp_orchestration_nucleus
  - p12_wf_orchestration_pipeline
  - p08_ac_orchestrator
  - p01_kc_orchestration_best_practices
  - p01_ctx_cex_project
  - p02_agent_admin_orchestrator
  - p12_wf_admin_orchestration
  - ctx_cex_new_dev_guide
  - dispatch
  - p12_wf_create_orchestration_agent
---

# Concept Graph

> Directed prerequisite graph. Arrows mean "must understand A before B." Used by mentor_journey.md to order learning paths.

## Root Nodes (no prerequisites)

These concepts have no dependencies -- start here if new to CEX:

| Concept | Brief definition | First touch |
|---------|----------------|-------------|
| `CEX` | The enterprise brain system (not an agent) | "What is CEX?" story in any lens |
| `artifact` | A .md file with YAML frontmatter that encodes one piece of knowledge | "The finished product" in factory lens |
| `pillar` | P01-P12 domain groupings (12 departments) | "The 12 zones" in game lens |
| `kind` | Atomic artifact type (293 types exist) | "Product specification" in factory lens |

## Tier 1 (requires roots)

| Concept | Requires | Brief definition |
|---------|----------|----------------|
| `nucleus` | CEX, pillar | An LLM agent specialized for one domain (N01-N07) |
| `builder` | kind, artifact | The machine/archetype that produces one specific kind |
| `ISO` | builder | The 12 configuration files per builder (1:1 with pillars) |
| `8F pipeline` | kind, builder, artifact | The 8-step reasoning protocol every task passes through |
| `knowledge_card` | artifact, pillar (P01) | A dense, searchable atomic fact card |
| `prompt_template` | artifact, pillar (P03) | A reusable mold with variables that generates prompts |

## Tier 2 (requires Tier 1)

| Concept | Requires | Brief definition |
|---------|----------|----------------|
| `N07 orchestrator` | nucleus, 8F pipeline | The orchestrating nucleus that dispatches but never builds |
| `dispatch` | nucleus, 8F pipeline | Sending a task + handoff to a nucleus |
| `handoff` | dispatch, 8F pipeline | The written task spec passed to a nucleus |
| `quality gate (F7)` | 8F pipeline | The F7 step that scores and gates artifact quality |
| `GDP` | 8F pipeline, nucleus | Guided Decision Protocol: user decides WHAT, LLM decides HOW |
| `RAG` | knowledge_card, embedding | Retrieval-Augmented Generation: fetch relevant KCs before generating |
| `sin lens` | nucleus | Each nucleus's motivational archetype (one of 7 sins) |

## Tier 3 (requires Tier 2)

| Concept | Requires | Brief definition |
|---------|----------|----------------|
| `wave` | dispatch, N07 orchestrator | A sequenced group of parallel dispatches with a gate between |
| `grid` | dispatch, wave | Parallel dispatch of multiple nuclei on a mission |
| `signal` | 8F pipeline, dispatch | F8 completion notification sent by nucleus to N07 |
| `decision_manifest` | GDP | The YAML file that locks user decisions for autonomous execution |
| `crew` | nucleus, dispatch, handoff | A multi-role team with defined topology and handoffs |
| `quality score` | quality gate (F7) | Numeric score (0-10) assigned to an artifact by F7 GOVERN |

## Tier 4 (requires Tier 3)

| Concept | Requires | Brief definition |
|---------|----------|----------------|
| `mission` | grid, wave, GDP | A full end-to-end execution: plan -> guide -> spec -> grid -> consolidate |
| `8F pipeline mastery` | all Tier 1-3 | Ability to reason about any task using all 8F steps with correct depth |
| `CEX as enterprise brain` | mission, 8F pipeline mastery, all nuclei | Understanding CEX as infrastructure (not an agent) |

## Key Learning Paths

### Beginner to "first artifact"
```
CEX -> artifact -> kind -> builder -> 8F pipeline -> [produce knowledge_card]
```

### Beginner to "understand dispatch"
```
CEX -> kind -> nucleus -> 8F pipeline -> N07 orchestrator -> handoff -> dispatch
```

### Beginner to "run a mission"
```
CEX -> kind -> nucleus -> 8F pipeline -> GDP -> decision_manifest -> dispatch -> wave -> grid -> signal -> mission
```

### Beginner to "understand RAG"
```
CEX -> artifact -> kind -> knowledge_card -> RAG
```

### Beginner to "build a crew"
```
CEX -> nucleus -> 8F pipeline -> dispatch -> handoff -> crew
```

## Concept Distance Matrix (steps from root)

| Concept | Distance from "CEX" root | Path length |
|---------|--------------------------|-------------|
| artifact | 1 | CEX -> artifact |
| kind | 1 | CEX -> kind |
| pillar | 1 | CEX -> pillar |
| nucleus | 2 | CEX -> pillar -> nucleus |
| 8F pipeline | 3 | CEX -> kind -> builder -> 8F pipeline |
| knowledge_card | 3 | CEX -> artifact -> pillar(P01) -> knowledge_card |
| GDP | 4 | CEX -> kind -> 8F pipeline -> GDP |
| dispatch | 4 | CEX -> nucleus -> 8F pipeline -> dispatch |
| grid | 6 | CEX -> nucleus -> 8F pipeline -> dispatch -> wave -> grid |
| mission | 8 | (full path, see above) |

## Quick Reference

```yaml
topic: concept_graph
scope: Prerequisite dependencies for all major CEX concepts
owner: n04_knowledge
criticality: high
audience: mentor_journey_template, /mentor_journey_subcommand
root_concepts: [CEX, artifact, pillar, kind]
deepest_concept: mission (distance=8 from CEX root)
graph_type: directed_acyclic_graph (DAG)
```

## Sources

- CEX CLAUDE.md: all concept definitions, nucleus identities, 8F pipeline
- Dependency ordering: topological sort of CEX knowledge domain
- Learning path design: Bloom's taxonomy (knowledge -> comprehension -> application -> synthesis)
  (https://www.bloomstaxonomy.net/)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_orchestration_nucleus]] | downstream | 0.40 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.37 |
| [[p08_ac_orchestrator]] | downstream | 0.36 |
| [[p01_kc_orchestration_best_practices]] | sibling | 0.35 |
| [[p01_ctx_cex_project]] | related | 0.35 |
| [[p02_agent_admin_orchestrator]] | downstream | 0.34 |
| [[p12_wf_admin_orchestration]] | downstream | 0.34 |
| [[ctx_cex_new_dev_guide]] | related | 0.34 |
| [[dispatch]] | downstream | 0.33 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.31 |
