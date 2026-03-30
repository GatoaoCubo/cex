---
id: p12_sc_builder_nucleus
kind: spawn_config
pillar: P12
title: Spawn Config -- Builder Nucleus
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [spawn-config, builder, N03]
tldr: How to spawn the builder -- model, timeout, environment.
density_score: 0.88
---

# Spawn Config: Builder Nucleus

## Default Configuration

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| model | opus | Meta-construction needs highest capability |
| thinking | extended | Complex multi-step reasoning |
| timeout | 120s per artifact | Includes LLM + compile + index |
| max_artifacts | 10 per session | Context limits |
| working_dir | CEX repo root | Access to all builders and tools |

## Model Override by Complexity

| Score | Model | When |
|-------|-------|------|
| 0-25 | haiku | Scaffold, format |
| 26-50 | sonnet | Content, single artifact |
| 51-75 | opus | Multi-kind, architecture |
| 76-100 | opus + xthinking | Nucleus bootstrap |

## Environment

| Requirement | Check |
|-------------|-------|
| Python 3.10+ | python --version |
| CEX repo | .cex/kinds_meta.json exists |
| Builders | archetypes/builders/ has 99+ dirs |
| API key | ANTHROPIC_API_KEY or equivalent |

## MCP Servers

Builder operates with zero MCPs (all tools are local Python).
Optional: brain MCP for enhanced knowledge search.
