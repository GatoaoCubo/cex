---
id: p01_kc_spawn_config
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P12
title: "Spawn Config — Deep Knowledge for spawn_config"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: spawn_config
quality: 9.1
tags: [spawn_config, P12, GOVERN, kind-kc]
tldr: "Agent_group launch configuration specifying model, mode (solo/grid/continuous), MCP profile, and prompt constraints"
when_to_use: "Building, reviewing, or reasoning about spawn_config artifacts"
keywords: [spawn, agent_group, launch]
feeds_kinds: [spawn_config]
density_score: null
related:
  - p11_qg_spawn_config
  - bld_knowledge_card_spawn_config
  - p03_sp_spawn-config-builder
  - spawn-config-builder
  - bld_architecture_spawn_config
  - bld_output_template_spawn_config
  - bld_memory_spawn_config
  - bld_collaboration_spawn_config
  - bld_examples_spawn_config
  - bld_config_spawn_config
---

# Spawn Config

## Spec
```yaml
kind: spawn_config
pillar: P12
llm_function: GOVERN
max_bytes: 3072
naming: p12_spawn_{{mode}}.yaml
core: true
```

## What It Is
A spawn configuration defines how a agent node is launched — which model, CLI flags, MCP tool profile, prompt size limit, and handoff file to load. It is the declarative specification that spawn scripts (solo/grid/continuous) read to start agent_group sessions. It is NOT boot_config (P02 — per-provider model configuration, model parameters; spawn_config is about CLI launch mechanics) nor env_config (P09 — environment variables for runtime; spawn_config is launch-time orchestration config).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableConfig` (configurable fields) | Per-run config with model, callbacks, metadata |
| LlamaIndex | `Settings` global configuration | Model, embedder, chunk_size set at launch time |
| CrewAI | `Crew(llm=..., process=..., memory=...)` | Crew init parameters define execution config |
| DSPy | `dspy.configure(lm=..., rm=...)` | Global configure sets model and retriever for entire program |
| Haystack | Pipeline YAML serialization | Full pipeline config in YAML; load with `Pipeline.from_dict()` |
| OpenAI | `client.beta.assistants.create(model=..., tools=...)` | Assistant creation config = spawn config equivalent |
| Anthropic | `client.messages.create(model=..., system=..., tools=...)` | Per-call model and tool config |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| mode | enum | solo | solo/grid/continuous — solo: 1 sat; grid: parallel batch; continuous: queue-refill |
| model | string | required | opus-4-6/sonnet/haiku — opus=quality; haiku=speed/cost |
| mcp_profile | string | null | .mcp-{sat}.json — null = default; explicit = strict tool isolation |
| prompt_max_chars | int | 200 | Keep short for `-p` flag; offload detail to handoff file |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Solo interactive | 1 task, user oversight needed | `mode: solo, -interactive, model: opus` |
| Grid static | 2-6 independent tasks, all parallel | `mode: grid, sats: [research_agent, marketing_agent, builder_agent], model: sonnet` |
| Continuous batching | >6 tasks, queue auto-refills | `mode: continuous, batch_size: 3, queue_dir: .claude/handoffs/` |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| >4 simultaneous agent_groups | BSOD risk on Windows (RAM + terminal limit) | Max 3 sats + orchestrator; stagger spawns 5s apart |
| Inline prompt >200 chars with -p flag | TSP hangs waiting for user input | Write handoff file; prompt = "Read [file] and execute" |
| --mcp-config absolute path in PS chain | Path resolution fails in PowerShell→cmd chain | Use relative path or .mcp-{sat}.json in cwd |

## Integration Graph
```
[handoff] --> [spawn_config] --> [agent_group session]
[dag] ---------^           |
                      [signal: spawned]
```

## Decision Tree
- IF 1 task THEN mode: solo
- IF 2-6 independent tasks THEN mode: grid (static)
- IF >6 tasks THEN mode: continuous (auto-refill from handoff queue)
- IF task needs browser THEN add `--add browser` modifier; use chrome.cmd boot
- DEFAULT: model: opus for build/execute; sonnet for research/marketing; haiku for simple utility tasks

## Quality Criteria
- GOOD: Has mode, model, mcp_profile (or null), prompt_max_chars, handoff_file; YAML parseable
- GREAT: Agent_group count within limits (<=3+orchestrator); spawn delay documented; continuous batch_size set
- FAIL: >4 simultaneous sats; prompt >200 chars inline; missing model; --mcp-config absolute path

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_spawn_config]] | related | 0.45 |
| [[bld_knowledge_card_spawn_config]] | sibling | 0.44 |
| [[p03_sp_spawn-config-builder]] | upstream | 0.39 |
| [[spawn-config-builder]] | related | 0.39 |
| [[bld_architecture_spawn_config]] | upstream | 0.38 |
| [[bld_output_template_spawn_config]] | upstream | 0.37 |
| [[bld_memory_spawn_config]] | upstream | 0.36 |
| [[bld_collaboration_spawn_config]] | related | 0.35 |
| [[bld_examples_spawn_config]] | upstream | 0.33 |
| [[bld_config_spawn_config]] | upstream | 0.33 |
