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
quality: 9.1
tags: [spawn-config, builder, N03]
tldr: How to spawn the builder -- model, timeout, environment.
density_score: 0.88
related:
  - bld_collaboration_model_card
  - p02_bc_builder_nucleus
  - bld_collaboration_model_provider
  - spec_infinite_bootstrap_loop
  - p01_kc_spawn_config
  - p02_mp_anthropic
  - p08_ac_builder_nucleus
  - p08_ac_orchestrator
  - p08_pat_builder_construction
  - p02_agent_admin_orchestrator
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


## Spawn Configuration Details

Process spawning uses validated configurations to ensure reproducible execution:

- **Model pinning**: each nucleus specifies exact model version to prevent behavioral drift
- **Resource limits**: token budgets and timeout caps prevent runaway processes
- **Environment isolation**: spawned processes inherit only declared environment variables
- **Health probes**: spawned processes must respond to health check within startup grace period

### Configuration Validation

```yaml
# Spawn pre-flight checks
validation:
  required_fields: [nucleus, model, task]
  model_exists: true
  budget_within_limits: true
  cwd_accessible: true
  no_duplicate_spawn: true
  max_concurrent: 6
```

| Parameter | Range | Default | Override |
|-----------|-------|---------|---------|
| timeout | 30-600s | 120s | Per-task |
| token_budget | 1K-200K | 50K | Per-nucleus |
| retry_count | 0-3 | 1 | Per-task |
| startup_grace | 5-30s | 10s | Global |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_model_card]] | upstream | 0.26 |
| [[p02_bc_builder_nucleus]] | upstream | 0.25 |
| [[bld_collaboration_model_provider]] | upstream | 0.24 |
| [[spec_infinite_bootstrap_loop]] | related | 0.24 |
| [[p01_kc_spawn_config]] | related | 0.22 |
| [[p02_mp_anthropic]] | upstream | 0.21 |
| [[p08_ac_builder_nucleus]] | upstream | 0.21 |
| [[p08_ac_orchestrator]] | upstream | 0.21 |
| [[p08_pat_builder_construction]] | upstream | 0.21 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.21 |
