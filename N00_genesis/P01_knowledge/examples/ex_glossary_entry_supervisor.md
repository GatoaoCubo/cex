---
id: p01_gl_agent_group
kind: glossary_entry
8f: F3_inject
pillar: P01
version: 1.0.0
title: "Glossary — Agent Node"
term: agent_group
definition: "Processo Claude CLI especializado com identidade, modelo e MCPs proprios"
synonyms: [worker, executor, specialist]
tags: [glossary, agent, node, orchestration]
tldr: "An agent_group is an autonomous execution unit in the CEX system. Each has a fixed domain, dedicated LLM model, and exclusive MCP tools."
quality: 9.0
updated: "2026-04-07"
domain: "knowledge management"
author: n04_knowledge
created: "2026-04-07"
density_score: 0.98
related:
  - p01_gl_TERM_SLUG
  - bld_examples_glossary_entry
  - glossary-entry-builder
  - bld_collaboration_glossary_entry
  - bld_output_template_glossary_entry
  - p12_wf_create_orchestration_agent
  - p01_kc_spawn_patterns
  - p01_kc_workflow_orchestration
  - p01_kc_context_scoping
  - bld_tools_glossary_entry
---

# Glossary: agent_group

## Definition
Unidade autonoma de execucao no sistema CEX. Cada agent_group tem dominio fixo (Research, Build, Marketing), modelo LLM dedicado (opus ou sonnet), e MCPs exclusivos. O orchestrator (N07) coordena; agent_groups executam.

## Usage
1. **Context**: Aparece em N07 orchestration, dispatch rules, spawn configs
2. **Example**: "Spawnar agent_group builder_agent para executar 8F pipeline"
3. **Avoid confusion with**: `sub-agent` — um sub-agent é uma definição (.md); um agent_group é a execução viva

## Relationships

| Relation | Term | Notes |
|----------|------|-------|
| parent | nucleus | Agent nodes pertencem a um nucleus (N01-N07) |
| sibling | builder | Builders são agent_groups especializados em construção |
| child | task | Cada agent_group executa uma ou mais tasks |

## Domain Scope
1. **Pillars**: P02 (model), P03 (prompt), P12 (orchestration)
2. **Kinds**: agent, spawn_config, dispatch_rule
3. **Frequency**: high — termo usado em todo o sistema de orquestração

## Canonical Source
1. Reference: `.claude/rules/n07-orchestrator.md`
2. CEX adoption date: 2026-01-15

## Cross-References

1. **Pillar**: P01 (Knowledge)
2. **Kind**: `glossary entry`
3. **Artifact ID**: `p01_gl_agent_group`
4. **Tags**: [glossary, agent, node, orchestration]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `glossary entry` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Cross-References

1. **Pillar**: P01 (Knowledge)
2. **Kind**: `glossary entry`
3. **Artifact ID**: `p01_gl_agent_group`
4. **Tags**: [glossary, agent, node, orchestration]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `glossary entry` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Artifact Metadata

```yaml
kind: glossary_entry
pillar: P01
pipeline: 8F
scoring: hybrid_3_layer
compilation: cex_compile
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_gl_TERM_SLUG]] | sibling | 0.39 |
| [[bld_examples_glossary_entry]] | downstream | 0.34 |
| [[glossary-entry-builder]] | related | 0.33 |
| [[bld_collaboration_glossary_entry]] | downstream | 0.32 |
| [[bld_output_template_glossary_entry]] | downstream | 0.31 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.31 |
| [[p01_kc_spawn_patterns]] | related | 0.29 |
| [[p01_kc_workflow_orchestration]] | related | 0.29 |
| [[p01_kc_context_scoping]] | related | 0.28 |
| [[bld_tools_glossary_entry]] | downstream | 0.27 |
