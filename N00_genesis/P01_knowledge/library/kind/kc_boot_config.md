---
id: p01_kc_boot_config
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P02
title: "Boot Config — Deep Knowledge for boot_config"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: boot_config
quality: 9.1
tags: [boot_config, p02, GOVERN, kind-kc]
tldr: "Provider-specific bootstrap configuration — identity, constraints, tools, and MCPs loaded at agent initialization"
when_to_use: "Building, reviewing, or reasoning about boot_config artifacts"
keywords: [boot, bootstrap, provider, initialization, startup]
feeds_kinds: [boot_config]
density_score: null
related:
  - boot-config-builder
  - bld_collaboration_boot_config
  - p10_lr_boot-config-builder
  - p03_sp_boot_config_builder
  - bld_knowledge_card_boot_config
  - bld_architecture_boot_config
  - bld_instruction_boot_config
  - p11_qg_boot_config
  - agent-card-builder
  - bld_examples_boot_config
---

# Boot Config

## Spec
```yaml
kind: boot_config
pillar: P02
llm_function: GOVERN
max_bytes: 2048
naming: p02_boot_{{provider}}.md
core: false
```

## What It Is
A boot_config defines the initialization sequence for an agent on a specific provider (Claude Code, Cursor, Codex, etc.). It specifies which identity to load, which constraints apply, which tools are available, and which MCPs to connect. It is NOT an env_config (P09, which stores generic environment variables) nor a spawn_config (P12, which defines agent_group orchestration). Boot configs answer "how does this agent start on this provider?" — env configs answer "what variables exist?" and spawn configs answer "how do agent_groups launch?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | Agent initialization kwargs | Model, tools, prompt passed to `create_*_agent()` |
| LlamaIndex | `Settings` / `ServiceContext` | Global settings: LLM, embed_model, chunk_size |
| CrewAI | `Crew(agents, tasks, process)` | Crew initialization = boot sequence |
| DSPy | `dspy.configure(lm=...)` | Global LM configuration at startup |
| Haystack | `Pipeline.add_component()` sequence | Component wiring = boot graph |
| OpenAI | Assistant creation payload | model, tools, instructions, file_search config |
| Anthropic | Claude Code CLAUDE.md + .mcp.json | Boot chain: CLAUDE.md → rules/ → MCP servers |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| provider | string | required | Different providers need different boot sequences |
| identity | ref | required | Points to agent (P02) or PRIME file to load |
| constraints | list | [] | More constraints = safer but less flexible |
| tools | list | [] | More tools = more capable but higher token cost |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Minimal boot | Fast startup, simple tasks | Load identity + 2 core tools, no MCPs |
| Full boot | Production agent_group | Identity + mental_model + MCPs + all domain tools |
| Provider adapter | Same agent, different platforms | Claude Code boot vs Cursor boot for same research_agent agent |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Loading all tools regardless | Token waste; tool descriptions consume context | Load only domain-relevant tools |
| Hardcoded paths in boot | Breaks across machines/providers | Use relative paths or provider-specific resolution |
| No boot validation | Silent failures when MCP disconnects | Add health check step after boot |

## Integration Graph
```
[agent, mental_model] --> [boot_config] --> [spawn_config (P12)]
                               |
                        [env_config (P09), MCP servers]
```

## Decision Tree
- IF configuring how an agent starts on a specific platform THEN boot_config
- IF setting environment variables THEN env_config (P09)
- IF defining agent_group launch parameters THEN spawn_config (P12)
- IF defining the agent itself THEN agent (P02)
- DEFAULT: boot_config for any provider-specific initialization

## Quality Criteria
- GOOD: Provider specified; identity linked; tools listed; tested on target provider
- GREAT: Boot time measured; health check included; graceful fallback for missing MCPs
- FAIL: Hardcoded absolute paths; no provider specified; loads unnecessary tools; no identity reference

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[boot-config-builder]] | related | 0.56 |
| [[bld_collaboration_boot_config]] | downstream | 0.52 |
| [[p10_lr_boot-config-builder]] | downstream | 0.46 |
| [[p03_sp_boot_config_builder]] | downstream | 0.45 |
| [[bld_knowledge_card_boot_config]] | sibling | 0.44 |
| [[bld_architecture_boot_config]] | downstream | 0.42 |
| [[bld_instruction_boot_config]] | downstream | 0.42 |
| [[p11_qg_boot_config]] | downstream | 0.39 |
| [[agent-card-builder]] | downstream | 0.39 |
| [[bld_examples_boot_config]] | downstream | 0.38 |
