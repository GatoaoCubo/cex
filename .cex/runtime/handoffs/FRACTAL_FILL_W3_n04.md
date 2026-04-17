---
mission: FRACTAL_FILL_W3
nucleus: n04
wave: W3_AGENT_LAYER
created: 2026-04-16
model: gpt-5-codex
pillars: [P02, P03]
artifact_count: 13
---

# N04 -- Wave 3 AGENT_LAYER (13 artifacts: agents + prompts)

## Mission

You are N04_knowledge (Knowledge Gluttony). Fill P02 (agents) and P03 (prompts) pillars:
13 artifacts via 8F. This is the thinking layer -- identity + reasoning.

## Context (READ)

1. `N04_knowledge/P08_architecture/nucleus_def_n04.md`
2. `N04_knowledge/P06_schema/`, `N04_knowledge/P09_config/`, `N04_knowledge/P01_knowledge/`, `N04_knowledge/P10_memory/` -- prior waves
3. `archetypes/builders/{kind}-builder/` per kind
4. `P02_model/_schema.yaml`, `P03_prompt/_schema.yaml`
5. `P01_knowledge/library/kind/kc_{kind}.md`

## Deliverables

### P02 (agents) -- 7 artifacts

1. `N04_knowledge/P02_model/age_agent_package_n04.md` -- kind=`agent_package` -- Portable AI agent package (ISO format) -- self-contained, LLM-agnostic
2. `N04_knowledge/P02_model/age_axiom_n04.md` -- kind=`axiom` -- Principio fundamental imutavel â€” parte da identidade profunda da entidade
3. `N04_knowledge/P02_model/age_handoff_protocol_n04.md` -- kind=`handoff_protocol` -- Agent-to-agent transfer protocol
4. `N04_knowledge/P02_model/age_mental_model_n04.md` -- kind=`mental_model` -- Agent mental model (routing, decisions)
5. `N04_knowledge/P02_model/age_model_provider_n04.md` -- kind=`model_provider` -- LLM provider adapter (Claude, GPT, Gemini, Ollama, OpenRouter, LiteLLM)
6. `N04_knowledge/P02_model/age_nucleus_def_n04.md` -- kind=`nucleus_def` -- Formal definition of a CEX nucleus (N00-N07). Fields: nucleus_id, role, pillars_owned, sin_lens, cli
7. `N04_knowledge/P02_model/age_router_n04.md` -- kind=`router` -- Routing rule (task > agent_group)

### P03 (prompts) -- 6 artifacts

8. `N04_knowledge/P03_prompt/pro_action_prompt_n04.md` -- kind=`action_prompt` -- Task prompt sent by human/orchestrator to the agent
9. `N04_knowledge/P03_prompt/pro_constraint_spec_n04.md` -- kind=`constraint_spec` -- Constrained generation rules
10. `N04_knowledge/P03_prompt/pro_context_window_config_n04.md` -- kind=`context_window_config` -- Token budget allocation, priority tiers, and overflow rules for prompt assembly
11. `N04_knowledge/P03_prompt/pro_prompt_compiler_n04.md` -- kind=`prompt_compiler` -- Intent-to-artifact transmutation rules. Compiles vague user input into structured {kind, pillar, nuc
12. `N04_knowledge/P03_prompt/pro_prompt_template_n04.md` -- kind=`prompt_template` -- Reusable template with {{vars}} to generate prompts
13. `N04_knowledge/P03_prompt/pro_reasoning_trace_n04.md` -- kind=`reasoning_trace` -- Structured chain-of-thought reasoning with confidence scores

## Format

Standard frontmatter + structured body (min 80 lines, density >= 0.85).
Agents: role, capabilities, tools, boundaries via **Knowledge Gluttony** lens.
Prompts: template vars, input/output schema, examples, constraints.

## 8F trace (HTML comment IMMEDIATELY BELOW the closing `---` of frontmatter, NEVER above it)

## ASCII rule: unaccented PT identifiers; no emoji in code fields.

## On completion
1. Save.  2. Print `=== COMPLETE === nucleus=n04 wave=W3 count=13 ===`.
3. DO NOT commit.  4. Exit.
