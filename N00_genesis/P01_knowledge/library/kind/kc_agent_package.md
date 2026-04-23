---
id: p01_kc_agent_package
kind: knowledge_card
type: kind
pillar: P02
title: "ISO Package — Deep Knowledge for agent_package"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: agent_package
quality: 9.1
tags: [agent_package, p02, BECOME, kind-kc]
tldr: "Self-contained portable agent bundle — LLM-agnostic, distributable package with manifest, instructions, and examples"
when_to_use: "Building, reviewing, or reasoning about agent_package artifacts"
keywords: [iso, package, portable, bundle, agent-distribution]
feeds_kinds: [agent_package]
density_score: null
related:
  - agent-builder
  - p01_kc_agent
  - bld_collaboration_agent
  - agent-package-builder
  - bld_knowledge_card_agent_package
  - bld_architecture_agent
  - bld_knowledge_card_agent
  - bld_instruction_agent_package
  - p03_sp_agent_package_builder
  - bld_examples_agent_package
---

# ISO Package

## Spec
```yaml
kind: agent_package
pillar: P02
llm_function: BECOME
max_bytes: 4096
naming: agents/{{agent_name}}/manifest.yaml
core: true
```

## What It Is
An agent_package is a self-contained, LLM-agnostic bundle that makes an agent portable and distributable. It contains everything needed to instantiate an agent on any compatible platform: manifest (identity), system instruction (voice), instructions (how to execute), examples (demonstrations), and error handling. It is NOT the agent spec itself (which defines persona and capabilities at a conceptual level) — the agent_package is the deployable artifact built from the spec. Think: agent = blueprint, agent_package = shipping container.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | LangChain Hub prompts / serialized agents | `hub.pull("owner/agent")` — versioned agent packages |
| LlamaIndex | `download_loader` / Llama Hub | Packaged data loaders; similar distribution concept |
| CrewAI | Agent YAML config files | `agents.yaml` + `tasks.yaml` = crew package |
| DSPy | Serialized module state | `module.save()` / `module.load()` — trained weights + config |
| Haystack | Pipeline YAML / serialized pipelines | `pipeline.dumps()` / `Pipeline.loads()` |
| OpenAI | GPT builder export | Assistant config export (partial; no full portability) |
| Anthropic | No native packaging | organization ISO format fills this gap |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| tier | enum | standard | minimal(3 files) vs standard(7) vs complete(10) vs whitelabel(12) |
| density_min | float | 0.8 | Higher density = more valuable but harder to author |
| no_hardcoded_paths | bool | true | Portability requirement; violations break cross-platform |
| system_instruction_max_tokens | int | 4096 | Longer = more detailed persona but slower boot |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Minimal ISO | Prototype or internal-only agent | manifest + system_instruction + instructions (3 files) |
| Standard ISO | Production agent | 7 files including examples and error handling |
| Complete ISO | Public/distributable agent | 10 files with architecture, upload kit, quick start |
| Whitelabel ISO | Client-customizable agent | 12 files with whitelabel upload kit and branding slots |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Hardcoded paths in instructions | Breaks on different machines/platforms | Use relative refs or placeholder variables |
| Missing examples | Users can't understand expected I/O | Include min 2 input/output examples |
| System instruction > 4096 tokens | Consumes too much context window | Distill to essential persona; move details to instructions |

## Integration Graph
```
[agent] --> [agent_package] --> [boot_config, platform deployment]
                 |
          [skill (P04), system_prompt (P03), output_template (P05)]
```

## Decision Tree
- IF need to share agent across platforms THEN agent_package (standard+)
- IF internal prototype only THEN minimal ISO or just agent spec
- IF client-facing customizable agent THEN whitelabel ISO
- IF defining agent capabilities conceptually THEN agent (P02), not agent_package
- DEFAULT: standard ISO (7 files) for any production agent

## Quality Criteria
- GOOD: Manifest complete; system instruction under 4096 tokens; no hardcoded paths; min 2 examples
- GREAT: Complete tier (10+ files); density > 0.8 on all text files; tested on 2+ platforms; quality >= 8.0
- FAIL: Hardcoded paths; no examples; system instruction exceeds token limit; missing manifest

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent-builder]] | related | 0.50 |
| [[p01_kc_agent]] | sibling | 0.46 |
| [[bld_collaboration_agent]] | downstream | 0.44 |
| [[agent-package-builder]] | related | 0.44 |
| [[bld_knowledge_card_agent_package]] | sibling | 0.41 |
| [[bld_architecture_agent]] | downstream | 0.40 |
| [[bld_knowledge_card_agent]] | sibling | 0.40 |
| [[bld_instruction_agent_package]] | downstream | 0.39 |
| [[p03_sp_agent_package_builder]] | downstream | 0.38 |
| [[bld_examples_agent_package]] | downstream | 0.36 |
