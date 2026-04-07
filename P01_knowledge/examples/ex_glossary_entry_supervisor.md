---
id: p01_gl_agent_group
kind: glossary_entry
pillar: P01
version: 1.0.0
title: "Glossary — Agent Node"
term: agent_group
definition: "Processo Claude CLI especializado com identidade, modelo e MCPs proprios"
synonyms: [worker, executor, specialist]
tags: [glossary, agent, node, orchestration]
tldr: "An agent_group is an autonomous execution unit in the CEX system. Each has a fixed domain, dedicated LLM model, and exclusive MCP tools."
quality: 8.5
---

# Glossary: agent_group

## Definition
Unidade autonoma de execucao no sistema CEX. Cada agent_group tem dominio fixo (Research, Build, Marketing), modelo LLM dedicado (opus ou sonnet), e MCPs exclusivos. O orchestrator (N07) coordena; agent_groups executam.

## Usage
- **Context**: Aparece em N07 orchestration, dispatch rules, spawn configs
- **Example**: "Spawnar agent_group builder_agent para executar 8F pipeline"
- **Avoid confusion with**: `sub-agent` — um sub-agent é uma definição (.md); um agent_group é a execução viva

## Relationships

| Relation | Term | Notes |
|----------|------|-------|
| parent | nucleus | Agent nodes pertencem a um nucleus (N01-N07) |
| sibling | builder | Builders são agent_groups especializados em construção |
| child | task | Cada agent_group executa uma ou mais tasks |

## Domain Scope
- **Pillars**: P02 (model), P03 (prompt), P12 (orchestration)
- **Kinds**: agent, spawn_config, dispatch_rule
- **Frequency**: high — termo usado em todo o sistema de orquestração

## Canonical Source
- Reference: `.claude/rules/n07-orchestrator.md`
- CEX adoption date: 2026-01-15
