---
mission: FRACTAL_FILL_W3
nucleus: n02
wave: W3_AGENT_LAYER
created: 2026-04-16
model: gpt-5-codex
pillars: [P02, P03]
artifact_count: 13
---

# N02 -- Wave 3 AGENT_LAYER (13 artifacts: agents + prompts)

## Mission

You are N02_marketing (Creative Lust). Fill P02 (agents) and P03 (prompts) pillars:
13 artifacts via 8F. This is the thinking layer -- identity + reasoning.

## Context (READ)

1. `N02_marketing/P08_architecture/nucleus_def_n02.md`
2. `N02_marketing/P06_schema/`, `N02_marketing/P09_config/`, `N02_marketing/P01_knowledge/`, `N02_marketing/P10_memory/` -- prior waves
3. `archetypes/builders/{kind}-builder/` per kind
4. `P02_model/_schema.yaml`, `P03_prompt/_schema.yaml`
5. `P01_knowledge/library/kind/kc_{kind}.md`

## Deliverables

### P02 (agents) -- 7 artifacts

1. `N02_marketing/P02_model/age_agent_package_n02.md` -- kind=`agent_package` -- Portable AI agent package (ISO format) -- self-contained, LLM-agnostic
2. `N02_marketing/P02_model/age_axiom_n02.md` -- kind=`axiom` -- Principio fundamental imutavel â€” parte da identidade profunda da entidade
3. `N02_marketing/P02_model/age_handoff_protocol_n02.md` -- kind=`handoff_protocol` -- Agent-to-agent transfer protocol
4. `N02_marketing/P02_model/age_mental_model_n02.md` -- kind=`mental_model` -- Agent mental model (routing, decisions)
5. `N02_marketing/P02_model/age_model_provider_n02.md` -- kind=`model_provider` -- LLM provider adapter (Claude, GPT, Gemini, Ollama, OpenRouter, LiteLLM)
6. `N02_marketing/P02_model/age_nucleus_def_n02.md` -- kind=`nucleus_def` -- Formal definition of a CEX nucleus (N00-N07). Fields: nucleus_id, role, pillars_owned, sin_lens, cli
7. `N02_marketing/P02_model/age_router_n02.md` -- kind=`router` -- Routing rule (task > agent_group)

### P03 (prompts) -- 6 artifacts

8. `N02_marketing/P03_prompt/pro_constraint_spec_n02.md` -- kind=`constraint_spec` -- Constrained generation rules
9. `N02_marketing/P03_prompt/pro_context_window_config_n02.md` -- kind=`context_window_config` -- Token budget allocation, priority tiers, and overflow rules for prompt assembly
10. `N02_marketing/P03_prompt/pro_multimodal_prompt_n02.md` -- kind=`multimodal_prompt` -- Cross-modal prompt pattern for vision/audio/text
11. `N02_marketing/P03_prompt/pro_prompt_compiler_n02.md` -- kind=`prompt_compiler` -- Intent-to-artifact transmutation rules. Compiles vague user input into structured {kind, pillar, nuc
12. `N02_marketing/P03_prompt/pro_reasoning_trace_n02.md` -- kind=`reasoning_trace` -- Structured chain-of-thought reasoning with confidence scores
13. `N02_marketing/P03_prompt/pro_tagline_n02.md` -- kind=`tagline` -- Short memorable phrase capturing brand essence — taglines, slogans, headlines

## Format

Standard frontmatter + structured body (min 80 lines, density >= 0.85).
Agents: role, capabilities, tools, boundaries via **Creative Lust** lens.
Prompts: template vars, input/output schema, examples, constraints.

## 8F trace (HTML comment IMMEDIATELY BELOW the closing `---` of frontmatter, NEVER above it)

## ASCII rule: unaccented PT identifiers; no emoji in code fields.

## On completion
1. Save.  2. Print `=== COMPLETE === nucleus=n02 wave=W3 count=13 ===`.
3. DO NOT commit.  4. Exit.
