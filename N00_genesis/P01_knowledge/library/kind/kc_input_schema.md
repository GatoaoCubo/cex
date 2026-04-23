---
id: p01_kc_input_schema
kind: knowledge_card
type: kind
pillar: P06
title: "Input Schema — Deep Knowledge for input_schema"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: knowledge_agent
domain: input_schema
quality: 9.1
tags: [input_schema, P06, CONSTRAIN, kind-kc]
tldr: "Unilateral entry contract defining required fields, types, and constraints for agent or tool inputs."
when_to_use: "Building, reviewing, or reasoning about input_schema artifacts"
keywords: [input, schema, contract, required-fields]
feeds_kinds: [input_schema]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - p01_kc_interface
  - p01_kc_type_def
  - p01_kc_validation_schema
  - p03_sp_input_schema_builder
  - bld_architecture_input_schema
  - bld_knowledge_card_input_schema
  - p01_kc_function_def
  - bld_instruction_input_schema
  - p10_lr_input_schema_builder
  - bld_knowledge_card_validation_schema
---

# Input Schema

## Spec
```yaml
kind: input_schema
pillar: P06
llm_function: CONSTRAIN
max_bytes: 3072
naming: p06_is_{{scope}}.yaml
core: true
```

## What It Is
A formal YAML/JSON contract specifying what data a pipeline stage, agent, or tool requires as input. Defines field names, types, required/optional status, and inline constraints. Unilateral: describes what the CALLER must provide. NOT validation_schema (applied post-generation by system, LLM never sees it). NOT type_def (abstract type definition without call semantics). NOT interface (bilateral—also defines output).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | RunnableConfig / TypedDict input | Input type annotation on Chain.invoke() |
| LlamaIndex | QueryBundle / BaseModel input | Pydantic model for query pipeline inputs |
| CrewAI | Task inputs dict | input_variables in Task definition |
| DSPy | Signature inputs | dspy.InputField declarations |
| Haystack | ComponentInput | Input socket type annotation |
| OpenAI | function parameters | JSON Schema in function/tool definition |
| Anthropic | tool input_schema | JSON Schema in tool_use input_schema |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| required | list[str] | [] | More required = safer contract, less flexible |
| additionalProperties | bool | false | true = flexible but unpredictable |
| strict | bool | false | true = OpenAI strict mode, no extra fields |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Strict tool schema | OpenAI/Anthropic function calling | All fields in required[], no additionalProperties |
| Partial input | Allow optional context injection | Split required vs optional clearly |
| Versioned schema | Breaking changes between callers | Add schema_version field to frontmatter |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| No required fields | Callers omit critical data silently | Mark all non-optional fields as required |
| Giant monolithic schema | Hard to validate, reuse, or version | Split by concern into sub-schemas |
| Using for output validation | Wrong layer—output = validation_schema | Use p06_vs_{{scope}}.yaml for post-gen |

## Integration Graph
```
[enum_def] -----> [input_schema] --> [prompt_template (P03)]
[type_def] -----> [input_schema] --> [agent (P02)]
                       |----------> [tool_def (P04)]
                       |----------> [validation_schema]
```

## Decision Tree
- IF defining what a CALLER must provide THEN input_schema
- IF defining what system validates AFTER generation THEN validation_schema
- IF defining abstract reusable type shape THEN type_def
- IF defining bilateral agent-to-agent contract THEN interface
- DEFAULT: input_schema for any new agent or tool entry point

## Quality Criteria
- GOOD: All required fields declared, types explicit, naming consistent
- GREAT: Inline examples per field, enum_def refs for constrained fields, versioned
- FAIL: No required list, mixed YAML/JSON within file, ambiguous field names

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_interface]] | sibling | 0.41 |
| [[p01_kc_type_def]] | sibling | 0.38 |
| [[p01_kc_validation_schema]] | sibling | 0.38 |
| [[p03_sp_input_schema_builder]] | upstream | 0.37 |
| [[bld_architecture_input_schema]] | downstream | 0.36 |
| [[bld_knowledge_card_input_schema]] | sibling | 0.35 |
| [[p01_kc_function_def]] | sibling | 0.35 |
| [[bld_instruction_input_schema]] | upstream | 0.34 |
| [[p10_lr_input_schema_builder]] | downstream | 0.33 |
| [[bld_knowledge_card_validation_schema]] | sibling | 0.32 |
