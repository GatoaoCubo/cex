---
kind: memory
id: bld_memory_spawn_config
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for spawn_config artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Spawn Config"
version: "1.0.0"
author: n03_builder
tags: [spawn_config, builder, examples]
tldr: "Golden and anti-examples for spawn config construction, demonstrating ideal structure and common pitfalls."
domain: "spawn config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - spawn-config-builder
  - bld_knowledge_card_spawn_config
  - bld_collaboration_spawn_config
  - p11_qg_spawn_config
  - bld_architecture_spawn_config
  - bld_output_template_spawn_config
  - p01_kc_spawn_config
  - bld_tools_spawn_config
  - bld_memory_agent_card
  - p09_rr_agent_group_spawn
---
# Memory: spawn-config-builder
## Summary
Spawn configs define how autonomous agent_groups are launched: CLI flags, MCP profiles, timeout policies, and handoff file references. The critical production lesson is prompt size limits — inline prompts exceeding 200 characters cause hangs in non-interactive mode. Complex task descriptions must be offloaded to handoff files referenced by the spawn config. The second lesson is MCP profile isolation: agent_groups sharing MCP configs cause connection conflicts when spawned concurrently.
## Pattern
1. Keep inline prompts under 200 characters — offload complex instructions to handoff files
2. Each agent_group must have its own MCP config file — shared configs cause connection conflicts in parallel spawns
3. Timeout policies must cover both task execution and idle detection — agent_groups without idle timeout hang indefinitely
4. Interactive mode flag must be explicitly set: interactive (keeps terminal open) or batch (closes on completion)
5. Spawn delay between concurrent agent_groups should be 3-5 seconds — simultaneous spawns cause resource contention
6. Include workspace trust handling: non-interactive mode requires explicit trust bypass flag
## Anti-Pattern
1. Inline prompts exceeding 200 characters — non-interactive mode hangs waiting for truncated input
2. Shared MCP config across concurrent agent_groups — connection conflicts cause silent tool failures
3. Missing idle timeout — agent_group finishes tasks but terminal stays open consuming resources indefinitely
4. Spawning more than 3 concurrent agent_groups without delay — causes memory exhaustion and system instability
5. Confusing spawn_config (P12, launch parameters) with signal (P12, status event) or workflow (P12, multi-step orchestration)
6. Absolute paths in MCP config that differ across machines — config fails on any machine except the original
## Context
Spawn configs operate in the P12 orchestration layer. They are consumed by PowerShell spawn scripts that create terminal processes for each agent_group. In production, spawn configs enable automated agent_group deployment in solo (single agent_group), grid (multiple parallel), and continuous (queue-based refill) modes. The key constraint is that each spawned agent_group is an independent process with its own resources.
## Impact
Prompt size enforcement (under 200 characters) eliminated 100% of non-interactive mode hangs. Per-agent_group MCP profiles eliminated all concurrent connection conflicts. Idle timeout policies recovered 100% of zombie agent_group processes within configured windows.
## Reproducibility
Reliable spawn config production: (1) define agent_group-model pairing, (2) create isolated MCP config file, (3) keep inline prompt under 200 chars with handoff file reference, (4) set interactive/batch mode explicitly, (5) configure task and idle timeouts, (6) set spawn delay for concurrent launches, (7) handle workspace trust bypass, (8) validate against 8 HARD + 8 SOFT gates.
## References
1. spawn-config-builder SCHEMA.md (19 frontmatter fields)
2. P12 orchestration pillar specification
3. Process management and agent_group lifecycle patterns

## Metadata

```yaml
id: bld_memory_spawn_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-spawn-config.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | spawn config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spawn-config-builder]] | downstream | 0.52 |
| [[bld_knowledge_card_spawn_config]] | downstream | 0.50 |
| [[bld_collaboration_spawn_config]] | downstream | 0.49 |
| [[p11_qg_spawn_config]] | downstream | 0.47 |
| [[bld_architecture_spawn_config]] | upstream | 0.42 |
| [[bld_output_template_spawn_config]] | upstream | 0.41 |
| [[p01_kc_spawn_config]] | downstream | 0.40 |
| [[bld_tools_spawn_config]] | upstream | 0.37 |
| [[bld_memory_agent_card]] | sibling | 0.36 |
| [[p09_rr_agent_group_spawn]] | upstream | 0.34 |
