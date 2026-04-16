---
mission: FRACTAL_FILL_W3
nucleus: n06
wave: W3_AGENT_LAYER
created: 2026-04-16
model: gpt-5-codex
pillars: [P02, P03]
artifact_count: 13
---

# N06 -- Wave 3 AGENT_LAYER (13 artifacts: agents + prompts)

## Mission

You are N06_commercial (Strategic Greed). Fill P02 (agents) and P03 (prompts) pillars:
13 artifacts via 8F. This is the thinking layer -- identity + reasoning.

## Context (READ)

1. `N06_commercial/architecture/nucleus_def_n06.md`
2. `N06_commercial/schemas/`, `N06_commercial/config/`, `N06_commercial/knowledge/`, `N06_commercial/memory/` -- prior waves
3. `archetypes/builders/{kind}-builder/` per kind
4. `P02_model/_schema.yaml`, `P03_prompt/_schema.yaml`
5. `P01_knowledge/library/kind/kc_{kind}.md`

## Deliverables

### P02 (agents) -- 6 artifacts

1. `N06_commercial/agents/age_agent_package_n06.md` -- kind=`agent_package` -- Portable AI agent package (ISO format) -- self-contained, LLM-agnostic
2. `N06_commercial/agents/age_customer_segment_n06.md` -- kind=`customer_segment` -- Customer segment/ICP definition artifact with firmographics and needs
3. `N06_commercial/agents/age_handoff_protocol_n06.md` -- kind=`handoff_protocol` -- Agent-to-agent transfer protocol
4. `N06_commercial/agents/age_model_provider_n06.md` -- kind=`model_provider` -- LLM provider adapter (Claude, GPT, Gemini, Ollama, OpenRouter, LiteLLM)
5. `N06_commercial/agents/age_nucleus_def_n06.md` -- kind=`nucleus_def` -- Formal definition of a CEX nucleus (N00-N07). Fields: nucleus_id, role, pillars_owned, sin_lens, cli
6. `N06_commercial/agents/age_router_n06.md` -- kind=`router` -- Routing rule (task > agent_group)

### P03 (prompts) -- 7 artifacts

7. `N06_commercial/prompts/pro_action_prompt_n06.md` -- kind=`action_prompt` -- Task prompt sent by human/orchestrator to the agent
8. `N06_commercial/prompts/pro_constraint_spec_n06.md` -- kind=`constraint_spec` -- Constrained generation rules
9. `N06_commercial/prompts/pro_context_window_config_n06.md` -- kind=`context_window_config` -- Token budget allocation, priority tiers, and overflow rules for prompt assembly
10. `N06_commercial/prompts/pro_expansion_play_n06.md` -- kind=`expansion_play` -- Account expansion play: upsell triggers, cross-sell map, NRR mechanics, AE talk track
11. `N06_commercial/prompts/pro_prompt_compiler_n06.md` -- kind=`prompt_compiler` -- Intent-to-artifact transmutation rules. Compiles vague user input into structured {kind, pillar, nuc
12. `N06_commercial/prompts/pro_reasoning_trace_n06.md` -- kind=`reasoning_trace` -- Structured chain-of-thought reasoning with confidence scores
13. `N06_commercial/prompts/pro_sales_playbook_n06.md` -- kind=`sales_playbook` -- Sales playbook with personas, discovery flow, objection handling, close patterns

## Format

Standard frontmatter + structured body (min 80 lines, density >= 0.85).
Agents: role, capabilities, tools, boundaries via **Strategic Greed** lens.
Prompts: template vars, input/output schema, examples, constraints.

## 8F trace (HTML comment IMMEDIATELY BELOW the closing `---` of frontmatter, NEVER above it)

## ASCII rule: unaccented PT identifiers; no emoji in code fields.

## On completion
1. Save.  2. Print `=== COMPLETE === nucleus=n06 wave=W3 count=13 ===`.
3. DO NOT commit.  4. Exit.
