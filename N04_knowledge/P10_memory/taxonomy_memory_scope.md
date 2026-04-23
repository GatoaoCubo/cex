---
id: p10_memscope_taxonomy
kind: memory_scope
pillar: P02
title: "Taxonomy Memory Scope — Classification Decision History"
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
domain: taxonomy-management
quality: 8.9
tags: [memory-scope, taxonomy, classification, decisions, n04]
tldr: "Persistent memory tracking taxonomy decisions: kind reclassifications, tag normalizations, orphan resolutions, domain boundary rulings."
density_score: 0.91
related:
  - p03_sp_taxonomy_engineer
  - n04_agent_taxonomy_engineer
  - p04_tool_taxonomy_builder
  - p01_gl_taxonomy
  - agent_card_n04
  - bld_collaboration_memory_scope
  - bld_manifest_memory_type
  - bld_collaboration_memory_type
  - bld_knowledge_card_kind
  - bld_system_prompt_memory_type
---

# Taxonomy Memory Scope

## Purpose

Tracks all classification decisions made during taxonomy maintenance. Prevents re-debating settled classifications. Provides audit trail for why an artifact lives where it does.

## Memory Categories

| Category | Type | Retention | Example |
|----------|------|-----------|---------|
| **Reclassification** | correction | 365 days | `spawn_config` moved from P03 to P12 (deploy, not agent) |
| **Tag canonical form** | convention | Permanent | `llm` is canonical, not `large-language-model` |
| **Domain boundary** | preference | 365 days | `system_prompt` → N04 owns when for knowledge agents |
| **Orphan resolution** | context | 180 days | `output_grid_test.md` assigned `kind: context_doc` |

## Decision Record Format

```yaml
- date: 2026-04-07
  type: reclassification
  artifact: path/to/artifact.md
  from: { kind: X, pillar: PY }
  to: { kind: Z, pillar: PW }
  reason: "Content is 80% deploy config, not agent definition"
  decided_by: n04_taxonomy_engineer
```

## Active Conventions

| Convention | Rule | Established |
|------------|------|-------------|
| Tag format | `lowercase-kebab-case`, max 3 words | 2026-04-07 |
| Kind echo | Tags must not repeat `kind` value | 2026-04-07 |
| Pillar echo | Tags must not repeat `pillar` code | 2026-04-07 |
| Cross-pillar | Tag `cross-pillar` + source + target pillars | 2026-04-07 |
| Synonym resolution | Prefer shorter canonical form | 2026-04-07 |

## Memory Lifecycle

| Phase | Tool | Action |
|-------|------|--------|
| **Create** | `cex_memory_update.py --append` | New classification decision |
| **Age** | `cex_memory_age.py` | Apply linear decay (365d half-life) |
| **Retrieve** | `cex_memory_select.py --scope taxonomy` | Inject relevant decisions into taxonomy tasks |
| **Prune** | `cex_memory_update.py --prune` | Archive decisions older than retention period |

## Queries

| Question | Memory Lookup |
|----------|--------------|
| "Why is X in pillar Y?" | Search reclassification records for artifact path |
| "What's the canonical tag for Z?" | Search convention records for synonym |
| "Has this orphan been resolved before?" | Search orphan-resolution records |
| "What boundaries has N04 set?" | Filter domain-boundary decisions by `decided_by: n04_*` |

## Boundary

Qual memoria usar. NAO eh session_state.


## 8F Pipeline Function

Primary function: **INJECT**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_taxonomy_engineer]] | downstream | 0.34 |
| [[n04_agent_taxonomy_engineer]] | downstream | 0.34 |
| [[p04_tool_taxonomy_builder]] | downstream | 0.32 |
| [[p01_gl_taxonomy]] | upstream | 0.29 |
| [[agent_card_n04]] | upstream | 0.23 |
| [[bld_collaboration_memory_scope]] | downstream | 0.22 |
| [[bld_manifest_memory_type]] | related | 0.21 |
| [[bld_collaboration_memory_type]] | downstream | 0.19 |
| [[bld_knowledge_card_kind]] | upstream | 0.19 |
| [[bld_system_prompt_memory_type]] | related | 0.19 |
