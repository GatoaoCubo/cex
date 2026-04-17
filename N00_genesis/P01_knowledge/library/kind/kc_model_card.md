---
id: p01_kc_model_card
kind: knowledge_card
type: kind
pillar: P02
title: "Model Card — Deep Knowledge for model_card"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: model_card
quality: 9.1
tags: [model_card, P02, GOVERN, kind-kc]
tldr: "Structured spec of an LLM's capabilities, pricing, context window, and operational constraints for routing decisions"
when_to_use: "Building, reviewing, or reasoning about model_card artifacts"
keywords: [llm-spec, pricing, context-window]
feeds_kinds: [model_card]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
---

# Model Card

## Spec
```yaml
kind: model_card
pillar: P02
llm_function: GOVERN
max_bytes: 2048
naming: p02_mc_{{model}}.md + .yaml
core: false
```

## What It Is
A model card is a structured specification of an LLM's capabilities, pricing tiers, context window size, supported modalities, and operational constraints. It governs which model gets assigned to which task based on cost/quality tradeoffs. It is NOT an agent definition (that's mental_model) nor a boot configuration (that's boot_config). A model card is a reference document about the model itself.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `BaseChatModel` init params | Model name, temperature, max_tokens configured at init |
| LlamaIndex | `LLM` class + `Settings.llm` | Global or per-query LLM configuration |
| CrewAI | `LLM` wrapper (LiteLLM-based) | Model string + params passed through LiteLLM |
| DSPy | `dspy.LM` configuration | `dspy.LM("provider/model", temperature=...)` |
| Haystack | `OpenAIGenerator` / `OpenAIChatGenerator` params | Model name and generation params at component init |
| OpenAI | Model object in API (`gpt-4o`, etc.) | Model ID, pricing, context window as platform specs |
| Anthropic | Model field (`claude-opus-4-6`, etc.) | Model ID + pricing + max_tokens in API docs |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| context_window | int | varies | Larger = more context but higher cost per request |
| cost_per_1k_input | float | varies | Cheaper = more budget-friendly but often lower quality |
| max_output_tokens | int | varies | Higher = longer responses but slower generation |
| modalities | list | [text] | Multimodal = more capable but higher latency and cost |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Tiered routing | Cost optimization across task types | Haiku for simple, Sonnet for balanced, Opus for complex |
| Capability gating | Task requires specific features | Vision tasks routed only to multimodal models |
| Budget-aware selection | Fixed budget constraints | Track cumulative cost, downgrade model when >80% spent |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Hardcoding model IDs in prompts | Breaks when models are deprecated or renamed | Reference model_card by capability, not by ID |
| Ignoring context window limits | Silent truncation or API errors | Check input size against model_card.context_window before calling |

## Integration Graph
```
[mental_model] --> [model_card] --> [router]
                        |
                   [boot_config]
```

## Decision Tree
- IF task requires vision THEN select model_card with `modalities: [text, vision]`
- IF budget is constrained THEN select model_card with lowest cost_per_1k_input meeting quality threshold
- IF task is complex reasoning THEN select model_card with highest benchmark scores
- DEFAULT: Use the model_card matching the agent_group's default model assignment

## Quality Criteria
- GOOD: Has model ID, context window, pricing, and modalities documented
- GREAT: Includes benchmark scores, deprecation date, rate limits, and failover model
- FAIL: Missing pricing or context window; outdated model ID; no capability list
