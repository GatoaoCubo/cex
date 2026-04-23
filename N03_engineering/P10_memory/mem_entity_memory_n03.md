---
id: mem_entity_memory_n03
kind: entity_memory
pillar: P10
nucleus: N03
title: "N03 Entity Memory"
version: "1.0.0"
created: "2026-04-16"
updated: "2026-04-16"
author: n03_engineering
domain: engineering operational memory
quality: 9.1
tags: [entity_memory, p10, n03, memory, engineering, inventive_pride]
density_score: 0.99
related:
  - entity-memory-builder
  - p01_kc_entity_memory
  - bld_collaboration_entity_memory
  - bld_knowledge_card_entity_memory
  - p03_sp_entity_memory_builder
  - bld_schema_entity_memory
  - p10_lr_entity_memory_builder
  - bld_architecture_entity_memory
  - bld_collaboration_memory_type
  - bld_collaboration_knowledge_graph
---
<!-- 8F: F1=entity_memory/P10 F2=entity-memory-builder F3=nucleus_def_n03+kc_entity_memory+P10_schema F4=high-signal memory for build entities
     F5=Get-Content+rg+apply_patch+cex_compile.py F6=bytes:5444 F7=self-check:frontmatter+8f+properties+80l+ascii F8=N03_engineering/P10_memory/mem_entity_memory_n03.md -->

# N03 Entity Memory

## Properties

| Property | Value |
|----------|-------|
| Kind | `entity_memory` |
| Pillar | `P10` |
| Nucleus | `N03` |
| Lens | `Inventive Pride` |
| Entity focus | builders, nuclei, tools, artifact families |
| Retention style | current facts only |
| TTL default | 30 days for volatile entities |
| Confidence rule | explicit per fact |
| Update style | overwrite stale facts, do not append event logs |
| Primary risk | bloated memory masquerading as history |

## Core Principle

Entity memory exists so N03 can remember what something is right now.
It is not a diary.
It is not a changelog.
Inventive Pride demands crisp memory: few facts, well chosen, sourceable, and useful in the next build.

## Preferred Entity Types

| Entity type | Why it matters to N03 |
|------------|-----------------------|
| builder | construction capability and boundary |
| nucleus | ownership and routing |
| tool | execution capability and constraint |
| artifact family | patterns shared across kinds |
| runtime service | dependency state relevant to builds |

## Fact Model

Each remembered fact should carry:
- attribute name
- normalized value
- confidence level
- source path
- last verified date
- optional TTL

Facts without provenance are weak.
Facts without freshness are dangerous.

## Canonical N03 Entities

1. `N03` as a nucleus entity.
2. `cex_compile.py` as a build tool entity.
3. `chunk-strategy-builder` as a builder entity.
4. `knowledge-index-builder` as a builder entity.
5. `8F pipeline` as a concept entity when behavior is stable enough.

## Example Fact Priorities

| Priority | Fact shape | Example |
|---------|------------|---------|
| P1 | capability boundary | `N03 owns builder construction, not deployment` |
| P1 | active path | `agent_card_path = N03_engineering/agent_card_n03.md` |
| P2 | operational count | `builder archetypes available > 100` |
| P2 | runtime dependency | `compile step required in F8` |
| P3 | convenience detail | minor tool preference or alias |

## Update Policy

- overwrite facts when higher-confidence evidence appears
- expire volatile operational facts aggressively
- retain architectural facts longer
- collapse synonymous attributes into one canonical field
- reject facts that repeat entire prose passages

## Inventive Pride Lens

Pride in memory means refusing clutter.
An undisciplined memory store flatters itself by keeping everything.
N03 should keep only the facts that improve construction decisions.
If an entity record cannot justify its place in the next build cycle, it should shrink or disappear.

## Memory Boundaries

| Keep in entity_memory | Move elsewhere |
|----------------------|----------------|
| current role of a builder | lesson from a failed build |
| current path of a tool | full execution trace |
| stable nucleus ownership | session-only routing choice |
| current backend choice | temporary debug observation |

## Volatility Rules

- builder identity: low volatility
- file path: medium volatility
- tool counts: medium volatility
- runtime availability: high volatility
- user preference: only if materially impacts N03 outputs

## Failure Modes

| Failure | Why it hurts | Remedy |
|--------|--------------|--------|
| event log stuffing | retrieval noise replaces facts | move history to learning_record |
| stale facts | wrong build assumptions | enforce TTL and verification |
| duplicate aliases | fragmented truth | canonicalize names |
| prose dumps | weak retrieval precision | compress to attributes |

## Retrieval Usage

Entity memory should answer questions like:
- what does this builder own
- which tool compiles artifacts
- what pillar does this entity belong to
- what is the current preferred backend
It should not answer narrative questions requiring chronological detail.

## Quality Standard

- under a tight byte budget
- top facts visible immediately
- explicit confidence on every material claim
- source path attached to operational facts
- no more than ten high-value attributes per entity unless justified

## Synchronization Rules

When entity memory changes:
- update knowledge index metadata if names or paths changed
- review runtime state references for stale values
- refresh summaries if core architectural facts moved
- avoid silent divergence between P01 and P10 descriptions

## Recommended Shape for N03

N03 should maintain entity records for:
- itself
- core builder families
- critical tooling
- retrieval infrastructure
- any external service that can block F8

The records should be sparse, explicit, and audited.
That is the proud memory posture.

## Final Position

N03 entity memory should store only current, decision-relevant facts about builders, tools, and routing-critical entities.
Anything broader becomes vanity storage and weakens the next build.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[entity-memory-builder]] | related | 0.52 |
| [[p01_kc_entity_memory]] | related | 0.51 |
| [[bld_collaboration_entity_memory]] | downstream | 0.51 |
| [[bld_knowledge_card_entity_memory]] | upstream | 0.46 |
| [[p03_sp_entity_memory_builder]] | related | 0.39 |
| [[bld_schema_entity_memory]] | related | 0.39 |
| [[p10_lr_entity_memory_builder]] | related | 0.37 |
| [[bld_architecture_entity_memory]] | upstream | 0.34 |
| [[bld_collaboration_memory_type]] | downstream | 0.34 |
| [[bld_collaboration_knowledge_graph]] | downstream | 0.33 |
