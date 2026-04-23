---
id: p01_kc_action_prompt
kind: knowledge_card
type: kind
pillar: P03
title: "Action Prompt — Deep Knowledge for action_prompt"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: action_prompt
quality: 9.1
tags: [action_prompt, P03, INJECT, kind-kc]
tldr: "Task-specific prompt that a human or orchestrator sends to an agent for immediate execution"
when_to_use: "Building, reviewing, or reasoning about action_prompt artifacts"
keywords: [user-prompt, task-injection, execution-trigger]
feeds_kinds: [action_prompt]
density_score: 0.99
linked_artifacts:
  primary: null
  related: []
related:
  - action-prompt-builder
  - bld_collaboration_action_prompt
  - bld_knowledge_card_action_prompt
  - p01_kc_instruction
  - bld_architecture_action_prompt
  - p01_kc_handoff
  - p01_kc_prompt_template
  - bld_instruction_action_prompt
  - p01_kc_constraint_spec
  - p03_sp_action_prompt_builder
---

# Action Prompt

## Spec
```yaml
kind: action_prompt
pillar: P03
llm_function: INJECT
max_bytes: 2048
naming: p03_up_{{task}}.md
core: true
```

## What It Is
An action prompt is a task-specific instruction that a human or orchestrator injects into an agent's context for immediate execution. The LLM reads it and acts. It is distinct from system_prompt (which defines identity/rules, read at boot) and prompt_template (which has variables to fill). An action prompt is concrete, complete, and executable as-is.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `HumanMessage` content / `PromptTemplate.format()` output | The final rendered prompt sent to the model |
| LlamaIndex | Query string to `QueryEngine.query()` | User's question or instruction to the engine |
| CrewAI | `Task(description=..., expected_output=...)` | Task description is the action prompt for the assigned agent |
| DSPy | Input fields of a `Signature` call | `module(question="...")` — the concrete input |
| Haystack | Input to `PromptBuilder` component | Template-rendered text passed to generator |
| OpenAI | User message in `messages` array | `{"role": "user", "content": "..."}` |
| Anthropic | User message content block | `{"role": "user", "content": "..."}` in Messages API |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| task | string | required | Specific = precise output vs vague = creative latitude |
| context | string | "" | More context = better grounding but longer input tokens |
| output_format | string | "free" | Structured = parseable but constrained vs free = flexible |
| seeds | list[str] | [] | More seeds = richer exploration but potential scope creep |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Direct instruction | Clear, unambiguous task | "Research top 5 competitors for category X" |
| Seeded exploration | Open-ended research with guardrails | "Explore [topic]. Seeds: keyword1, keyword2, keyword3" |
| Structured output request | Need parseable result | "Return a JSON object with fields: name, price, url" |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Mixing identity with task | Agent re-defines itself mid-execution | Keep identity in system_prompt, tasks in action_prompt |
| Unbounded scope | No clear deliverable, agent spirals | Add expected output format and word/byte limit |

## Integration Graph
```
[system_prompt] --> [action_prompt] --> [chain]
                         |
                    [constraint_spec]
```

## Decision Tree
- IF task is atomic and one-shot THEN single action_prompt
- IF task requires multi-step reasoning THEN use chain with multiple action_prompts
- IF task needs variable substitution THEN use prompt_template, not action_prompt
- DEFAULT: Write a direct, concrete action_prompt with explicit expected output

## Quality Criteria
- GOOD: Clear task, expected output defined, under 2048 bytes
- GREAT: Includes context seeds, output format spec, and scope boundaries
- FAIL: Vague instructions; mixes identity with task; no expected output; >2048 bytes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[action-prompt-builder]] | related | 0.44 |
| [[bld_collaboration_action_prompt]] | downstream | 0.40 |
| [[bld_knowledge_card_action_prompt]] | sibling | 0.40 |
| [[p01_kc_instruction]] | sibling | 0.39 |
| [[bld_architecture_action_prompt]] | downstream | 0.36 |
| [[p01_kc_handoff]] | sibling | 0.31 |
| [[p01_kc_prompt_template]] | sibling | 0.31 |
| [[bld_instruction_action_prompt]] | related | 0.28 |
| [[p01_kc_constraint_spec]] | sibling | 0.27 |
| [[p03_sp_action_prompt_builder]] | related | 0.27 |
