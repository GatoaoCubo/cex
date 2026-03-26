---
id: arch_prompt_template_builder
kind: architecture
pillar: P08
llm_function: CONSTRAIN
domain: prompt_template
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [architecture, prompt-template, P03, boundary, dependency-graph]
---

# Architecture — prompt-template-builder

## Boundary: What IS and IS NOT a prompt_template

**Decision question**: "Is this a reusable mold with `{{variables}}` that will be invoked multiple times with different values to produce distinct prompts?"

- YES → `prompt_template`
- NO → see NAO EH table below

## NAO EH Table — All P03 Siblings

| Kind | Why it is NOT a prompt_template |
|---|---|
| `system_prompt` | Defines agent identity and behavioral rules. Fixed text, rarely parameterized. Purpose: BECOME, not PRODUCE. |
| `user_prompt` | One-time task message from human or orchestrator. No reuse contract. Purpose: single invocation. |
| `few_shot` | Collection of fixed input/output examples for in-context learning. Examples are static, not variable slots. |
| `chain_of_thought` | Instructs the LLM to reason step-by-step. Reasoning style directive, not a parameterized mold. |
| `react` | Interleaves Thought/Action/Observation in a loop pattern. Loop structure, not a template with variable slots. |
| `chain` | Sequence of prompts where output A feeds input B. Orchestration pattern, not a reusable single-mold. |
| `meta_prompt` | Generates, improves, or evolves other prompts. Creates templates; it is not itself a template instance. |
| `router_prompt` | Classifies input and routes to a handler. Decision logic, not a parameterized content mold. |
| `planner` | Decomposes a task into an executable plan. Planning logic, not a reusable prompt structure. |

## Position in Prompt Flow

```
[type_def P06] --> [prompt_template P03] --> [rendered_prompt] --> [LLM call]
                                                    |
                          [user_prompt P03] --------+
                          [system_prompt P03] ------+
```

A `prompt_template` sits between the schema definition (P06) and the actual LLM invocation. It is never sent to the LLM directly — it is rendered first by substituting variable values.

## Dependency Graph

```
P06 type_def
    --> prompt-template-builder (consumes type definitions for variable schemas)
        --> p03_pt_* artifacts (produced)
            --> LangChain PromptTemplate (consumer)
            --> DSPy Signature (consumer)
            --> Mustache renderer (consumer)
            --> Jinja2 pipeline (consumer)

P03 prompt-template-builder
    --> SCHEMA.md (source of truth)
        --> OUTPUT_TEMPLATE.md (derives from SCHEMA.md, zero drift)
            --> p03_pt_* artifacts (derives from OUTPUT_TEMPLATE.md)

P03 prompt-template-builder
    --> QUALITY_GATES.md (validation)
        --> H01-H08 HARD gates (blocking)
        --> S01-S10 SOFT gates (scoring)

P03 prompt-template-builder
    --> KNOWLEDGE.md (syntax tiers, industry implementations)
    --> MEMORY.md (anti-patterns, common mistakes)
    --> EXAMPLES.md (golden reference)
```

## Fractal Position

```
CEX taxonomy
  └── P03 prompt layer
        └── prompt_template (THIS)
              ├── variable_syntax: mustache (tier-1)
              ├── variable_syntax: bracket (tier-2)
              └── composable: true/false
                    └── partial templates (composable=true, embedded in larger molds)
```

## Key Architectural Invariants

| Invariant | Rule |
|---|---|
| Structure/content separation | Template body is structure; variables are content. Never hardcode content values in the template body. |
| Render-time substitution | Templates are rendered before LLM invocation. The LLM never sees `{{variable}}` syntax. |
| Idempotency | Same template + same variable values = same rendered output, always. |
| Schema primacy | SCHEMA.md is the single source of truth. OUTPUT_TEMPLATE.md and all p03_pt_* artifacts derive from it. |
| Zero undeclared slots | Every `{{var}}` in the body must be declared in the variables list. No implicit slots. |
