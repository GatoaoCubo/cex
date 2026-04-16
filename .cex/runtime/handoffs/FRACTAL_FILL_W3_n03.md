---
mission: FRACTAL_FILL_W3
nucleus: n03
wave: W3_AGENT_LAYER
created: 2026-04-16
model: gpt-5-codex
pillars: [P02, P03]
artifact_count: 10
---

# N03 -- Wave 3 AGENT_LAYER (10 artifacts: agents + prompts)

## Mission

You are N03_engineering (Inventive Pride). Fill P02 (agents) and P03 (prompts) pillars:
10 artifacts via 8F. This is the thinking layer -- identity + reasoning.

## Context (READ)

1. `N03_engineering/architecture/nucleus_def_n03.md`
2. `N03_engineering/schemas/`, `N03_engineering/config/`, `N03_engineering/knowledge/`, `N03_engineering/memory/` -- prior waves
3. `archetypes/builders/{kind}-builder/` per kind
4. `P02_model/_schema.yaml`, `P03_prompt/_schema.yaml`
5. `P01_knowledge/library/kind/kc_{kind}.md`

## Deliverables

### P02 (agents) -- 5 artifacts

1. `N03_engineering/agents/age_agent_package_n03.md` -- kind=`agent_package` -- Portable AI agent package (ISO format) -- self-contained, LLM-agnostic
2. `N03_engineering/agents/age_handoff_protocol_n03.md` -- kind=`handoff_protocol` -- Agent-to-agent transfer protocol
3. `N03_engineering/agents/age_model_provider_n03.md` -- kind=`model_provider` -- LLM provider adapter (Claude, GPT, Gemini, Ollama, OpenRouter, LiteLLM)
4. `N03_engineering/agents/age_nucleus_def_n03.md` -- kind=`nucleus_def` -- Formal definition of a CEX nucleus (N00-N07). Fields: nucleus_id, role, pillars_owned, sin_lens, cli
5. `N03_engineering/agents/age_router_n03.md` -- kind=`router` -- Routing rule (task > agent_group)

### P03 (prompts) -- 5 artifacts

6. `N03_engineering/prompts/pro_action_prompt_n03.md` -- kind=`action_prompt` -- Task prompt sent by human/orchestrator to the agent
7. `N03_engineering/prompts/pro_constraint_spec_n03.md` -- kind=`constraint_spec` -- Constrained generation rules
8. `N03_engineering/prompts/pro_context_window_config_n03.md` -- kind=`context_window_config` -- Token budget allocation, priority tiers, and overflow rules for prompt assembly
9. `N03_engineering/prompts/pro_prompt_compiler_n03.md` -- kind=`prompt_compiler` -- Intent-to-artifact transmutation rules. Compiles vague user input into structured {kind, pillar, nuc
10. `N03_engineering/prompts/pro_reasoning_trace_n03.md` -- kind=`reasoning_trace` -- Structured chain-of-thought reasoning with confidence scores

## Format

Standard frontmatter + structured body (min 80 lines, density >= 0.85).
Agents: role, capabilities, tools, boundaries via **Inventive Pride** lens.
Prompts: template vars, input/output schema, examples, constraints.

## 8F trace (HTML comment IMMEDIATELY BELOW the closing `---` of frontmatter, NEVER above it)

## ASCII rule: unaccented PT identifiers; no emoji in code fields.

## On completion
1. Save.  2. Print `=== COMPLETE === nucleus=n03 wave=W3 count=10 ===`.
3. DO NOT commit.  4. Exit.
