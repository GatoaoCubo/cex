---
id: p01_kc_instruction
kind: knowledge_card
type: kind
pillar: P03
title: "Instruction — Deep Knowledge for instruction"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: instruction
quality: 9.1
tags: [instruction, P03, INJECT, kind-kc]
tldr: "Step-by-step execution recipe for agents or pipelines, bridging intent and action"
when_to_use: "Building, reviewing, or reasoning about instruction artifacts"
keywords: [steps, execution-recipe, how-to]
feeds_kinds: [instruction]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
---

# Instruction

## Spec
```yaml
kind: instruction
pillar: P03
llm_function: INJECT
max_bytes: 2048
naming: ex_instruction_{topic}.md
core: false
```

## What It Is
An instruction is a step-by-step execution recipe that tells an agent or pipeline exactly how to perform a task. It bridges the gap between intent (what to do) and action (how to do it). Unlike an action_prompt (a single task command), an instruction is a multi-step procedure. Unlike a system_prompt (identity and rules), an instruction is task-specific and disposable after execution.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | Few-shot examples in `ChatPromptTemplate` | Step-by-step examples guide the model's execution pattern |
| LlamaIndex | `QueryEngine` custom prompts / `Workflow` step definitions | Custom prompts define execution steps for the engine |
| CrewAI | `Task(description=...)` with numbered steps | Detailed task description serves as instruction set |
| DSPy | `Signature` docstring + `ChainOfThought` rationale | Signature docstring provides high-level instruction |
| Haystack | `PromptBuilder` template with step instructions | Jinja template embedding procedural instructions |
| OpenAI | `Assistant` instructions field | Persistent instructions defining how assistant should operate |
| Anthropic | System message with procedural content | Detailed system prompt with numbered execution steps |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| steps | list[str] | required | More steps = more precise but longer context, higher cost |
| prerequisites | list[str] | [] | Listed prereqs = safer execution but adds validation overhead |
| error_handling | string | "stop" | Explicit error paths = resilient but more complex instructions |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Sequential checklist | Linear task with clear order | "1. Read file. 2. Extract data. 3. Format output." |
| Conditional branching | Task with decision points | "IF file exists THEN parse ELSE create default" |
| Looped instruction | Iterative refinement | "REPEAT: generate → validate → fix UNTIL score >= 8.0" |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Instructions embedded in system_prompt | Bloats identity with disposable procedures | Separate identity (system_prompt) from procedure (instruction) |
| Ambiguous step boundaries | Agent skips or merges steps | Number each step; define explicit input/output per step |

## Integration Graph
```
[system_prompt] --> [instruction] --> [action_prompt]
                        |
                 [constraint_spec]
```

## Decision Tree
- IF task is procedural with >3 steps THEN create instruction
- IF task is a single action THEN use action_prompt instead
- IF procedure is reusable across agents THEN promote to skill (P12)
- DEFAULT: Write numbered steps with explicit input/output per step

## Quality Criteria
- GOOD: Numbered steps, clear prerequisites, under 2048 bytes
- GREAT: Each step has input/output contract; error handling defined; tested end-to-end
- FAIL: Vague prose without clear steps; mixed with identity; no completion criteria
