---
mission: FRACTAL_FILL_W3
nucleus: n01
wave: W3_AGENT_LAYER
created: 2026-04-16
model: gpt-5-codex
pillars: [P02, P03]
artifact_count: 12
---

# N01 -- Wave 3 AGENT_LAYER (12 artifacts: agents + prompts)

## Mission

You are N01_intelligence (Analytical Envy). Fill P02 (agents) and P03 (prompts) pillars:
12 artifacts via 8F. This is the thinking layer -- identity + reasoning.

## Context (READ)

1. `N01_intelligence/architecture/nucleus_def_n01.md`
2. `N01_intelligence/schemas/`, `N01_intelligence/config/`, `N01_intelligence/knowledge/`, `N01_intelligence/memory/` -- prior waves
3. `archetypes/builders/{kind}-builder/` per kind
4. `P02_model/_schema.yaml`, `P03_prompt/_schema.yaml`
5. `P01_knowledge/library/kind/kc_{kind}.md`

## Deliverables

### P02 (agents) -- 7 artifacts

1. `N01_intelligence/agents/age_agent_package_n01.md` -- kind=`agent_package` -- Portable AI agent package (ISO format) -- self-contained, LLM-agnostic
2. `N01_intelligence/agents/age_axiom_n01.md` -- kind=`axiom` -- Principio fundamental imutavel â€” parte da identidade profunda da entidade
3. `N01_intelligence/agents/age_handoff_protocol_n01.md` -- kind=`handoff_protocol` -- Agent-to-agent transfer protocol
4. `N01_intelligence/agents/age_mental_model_n01.md` -- kind=`mental_model` -- Agent mental model (routing, decisions)
5. `N01_intelligence/agents/age_model_provider_n01.md` -- kind=`model_provider` -- LLM provider adapter (Claude, GPT, Gemini, Ollama, OpenRouter, LiteLLM)
6. `N01_intelligence/agents/age_nucleus_def_n01.md` -- kind=`nucleus_def` -- Formal definition of a CEX nucleus (N00-N07). Fields: nucleus_id, role, pillars_owned, sin_lens, cli
7. `N01_intelligence/agents/age_router_n01.md` -- kind=`router` -- Routing rule (task > agent_group)

### P03 (prompts) -- 5 artifacts

8. `N01_intelligence/prompts/pro_action_prompt_n01.md` -- kind=`action_prompt` -- Task prompt sent by human/orchestrator to the agent
9. `N01_intelligence/prompts/pro_constraint_spec_n01.md` -- kind=`constraint_spec` -- Constrained generation rules
10. `N01_intelligence/prompts/pro_context_window_config_n01.md` -- kind=`context_window_config` -- Token budget allocation, priority tiers, and overflow rules for prompt assembly
11. `N01_intelligence/prompts/pro_prompt_compiler_n01.md` -- kind=`prompt_compiler` -- Intent-to-artifact transmutation rules. Compiles vague user input into structured {kind, pillar, nuc
12. `N01_intelligence/prompts/pro_reasoning_trace_n01.md` -- kind=`reasoning_trace` -- Structured chain-of-thought reasoning with confidence scores

## Format

Standard frontmatter + structured body (min 80 lines, density >= 0.85).
Agents: role, capabilities, tools, boundaries via **Analytical Envy** lens.
Prompts: template vars, input/output schema, examples, constraints.

## 8F trace HTML comment at top of each file.

## ASCII rule: unaccented PT identifiers; no emoji in code fields.

## On completion
1. Save.  2. Print `=== COMPLETE === nucleus=n01 wave=W3 count=12 ===`.
3. DO NOT commit.  4. Exit.
