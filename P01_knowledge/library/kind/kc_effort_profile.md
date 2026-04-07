---
id: p01_kc_effort_profile
kind: knowledge_card
type: kind
pillar: P09
title: "Effort Profile — Deep Knowledge for effort_profile"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: builder_agent
domain: effort_profile
quality: 9.1
tags: [effort_profile, P09, CONSTRAIN, kind-kc, thinking, model-selection]
tldr: "Declarative config mapping task complexity to model selection, thinking budget, and token limits — decides WHICH model and HOW MUCH thinking, not WHEN to run (that is runtime_rule)"
when_to_use: "Building, reviewing, or reasoning about effort_profile artifacts"
keywords: [effort_profile, thinking, model, budget, token_limit, effort]
feeds_kinds: [effort_profile]
density_score: null
---

# Effort Profile

## Spec
```yaml
kind: effort_profile
pillar: P09
llm_function: CONSTRAIN
max_bytes: 4096
naming: p09_effort_profile_{{topic}}.md + .yaml
core: false
```

## What It Is
An effort_profile is a declarative configuration that maps task complexity tiers to model selection, thinking budget, and token constraints. It answers "WHICH model and HOW MUCH thinking?" for a given task class. It is NOT a runtime_rule (which defines WHEN/HOW to execute) nor a model_card (which describes a model's capabilities). The effort_profile kind governs resource allocation per complexity tier — runtime_rule governs execution triggers and conditions.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| Anthropic | extended thinking budget + model selection | thinking: {budget_tokens: N} |
| OpenAI | reasoning_effort parameter (low/medium/high) | o1/o3 models only |
| LangChain | model routing via RouterChain | Route to different models by task type |
| DSPy | dspy.configure(lm=...) per module | Per-module model assignment |
| CrewAI | Agent(llm=..., max_tokens=...) | Per-agent model config |
| Vertex AI | Model Garden + routing | Traffic split across model variants |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| tiers | list[obj] | required | More tiers = finer control but more config complexity |
| default_model | str | required | Fallback model when no tier matches |
| thinking_budget | int | 1024 | Higher = better reasoning but more cost + latency |
| max_output_tokens | int | 4096 | Higher = longer responses but slower + costlier |
| cost_ceiling_usd | float | null | Hard cost cap per invocation; prevents runaway |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| 3-tier (low/medium/high) | Standard builder system | low=haiku, medium=sonnet, high=opus |
| Task-class routing | Heterogeneous workload | research=gemini-pro, build=opus, review=sonnet |
| Budget-capped thinking | Cost-sensitive production | thinking_budget: 2048, cost_ceiling: $0.50 |
| Escalation chain | Start cheap, escalate on failure | Try haiku -> sonnet -> opus with retry |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Always-opus | 10x cost for trivial tasks | Use tiers; route simple tasks to haiku/sonnet |
| No thinking budget | Complex tasks fail silently | Set thinking_budget >= 1024 for reasoning tasks |
| Mixing effort + runtime | Config becomes tangled | Keep effort_profile (what model) separate from runtime_rule (when to run) |

## Integration Graph
```
[dispatch_rule] --> [effort_profile] --> [model_selection]
                         |                    |
                  [runtime_rule]        [token_budget]
                         |                    |
                  [builder_execution] <-------+
```

## Decision Tree
- IF need to define execution triggers/conditions THEN use runtime_rule
- IF need to describe model capabilities THEN use model_card
- IF need per-agent model assignment THEN set in agent definition
- IF need task-complexity-to-model mapping THEN effort_profile
- DEFAULT: effort_profile when optimizing cost/quality tradeoff across task types

## Quality Criteria
- GOOD: At least 2 tiers defined; default_model set; thinking_budget specified
- GREAT: 3+ tiers with clear complexity criteria; cost_ceiling set; escalation chain defined; validated against real task distribution
- FAIL: Single tier (no routing value); no default_model; missing thinking_budget for reasoning tasks
