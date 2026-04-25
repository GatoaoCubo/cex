---
id: p01_kc_cex_function_become
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Function BECOME — Identity Configuration Before Processing"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, llm-function, become, identity, system-prompt, persona]
tldr: "BECOME configures LLM identity (persona, rules, limits) via 6 artifact types before any input"
when_to_use: "Understand how LLMs assume roles and why identity precedes context"
keywords: [become, identity, system-prompt, persona, agent-profile]
long_tails:
  - "How to configure LLM agent identity before processing"
  - "What is the difference between BECOME and INJECT in CEX"
axioms:
  - "ALWAYS execute BECOME before INJECT"
  - "NEVER mix identity (BECOME) with context (INJECT)"
linked_artifacts:
  primary: p01_kc_cex_function_inject
  related: [p01_kc_cex_function_reason]
density_score: null
data_source: "https://arxiv.org/abs/2308.00352"
related:
  - p01_kc_cex_lp02_model
  - p01_kc_mental_model
  - p01_kc_agent
  - bld_architecture_agent
  - agent-builder
  - p01_kc_cex_llm_function_concept
  - bld_collaboration_agent
  - p01_kc_cex_pipeline_execution
  - bld_architecture_boot_config
  - p01_kc_boot_config
---

## Summary

BECOME configures the identity, persona, and role of the LLM before any processing. Defines WHO the model is for the session via system prompt, mental model, and boot config. Maps to MetaGPT's "Role", CrewAI's "Agent Profile", and CAMEL's "InceptionPrompt". Represents 8% of CEX types (6 of 76).

## Spec

| Type | LP | Function | Detail |
|------|-----|----------|--------|
| agent | P02 | Complete identity | Memory, autonomy, tools, handoffs |
| mental_model | P02 | Cognitive map | Domains, productive biases, constraints |
| system_prompt | P03 | Persistent role | Baseline instruction pre-input |
| persona | P02 | Communication | Tone, style, affective preferences |
| boot_config | P02 | Initialization | Model, temperature, max_tokens, MCPs |
| model_card | P02 | LLM specification | Provider, version, costs, limits |

Execution order: system_prompt -> mental_model -> persona -> agent.
boot_config and model_card are infrastructure prerequisites.
BECOME executes BEFORE any INJECT — identity precedes context.

## Code

<!-- lang: python | purpose: agent identity via BECOME -->
```python
agent = Agent(
    name="shaka",
    instructions="Voce e um pesquisador de mercado brasileiro",
    model="sonnet",
    tools=[web_search, firecrawl],
    mental_model={"domain": "market_research", "bias": "quantitative"},
)
# system_prompt = instructions (BECOME)
# tools = CALL (configurado, nao executado)
# mental_model = restricoes cognitivas (BECOME)
```

## Patterns

| Trigger | Action |
|---------|--------|
| Agent needs persistent identity | Use agent type with memory |
| Direct interaction with humans | Add persona to agent |
| Model architectural decision | Create explicit model_card |
| Multiple agents in system | Mental model per specialist |
| Specific boot parameters | Boot config with flags and MCPs |

## Anti-Patterns

- Defining identity inside user prompt (volatile)
- Persona without system prompt (tone without role = incoherent)
- Confusing BECOME with INJECT (who I AM vs what I KNOW)
- Agent with 20+ tools without mental model (overload)
- Omitting boot_config (implicit defaults = bugs)

## References

- source: https://arxiv.org/abs/2308.00352
- source: https://arxiv.org/abs/2303.17760
- related: p01_kc_cex_function_inject
- related: p01_kc_cex_function_reason

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_lp02_model]] | sibling | 0.46 |
| [[p01_kc_mental_model]] | sibling | 0.36 |
| [[p01_kc_agent]] | sibling | 0.36 |
| [[bld_architecture_agent]] | downstream | 0.35 |
| [[agent-builder]] | downstream | 0.34 |
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.30 |
| [[bld_collaboration_agent]] | downstream | 0.30 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.29 |
| [[bld_architecture_boot_config]] | downstream | 0.28 |
| [[p01_kc_boot_config]] | sibling | 0.28 |
