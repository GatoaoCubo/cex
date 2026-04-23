---
id: p01_kc_constraint_spec
kind: knowledge_card
type: kind
pillar: P03
title: "Constraint Spec — Deep Knowledge for constraint_spec"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: constraint_spec
quality: 9.1
tags: [constraint_spec, P03, CONSTRAIN, kind-kc]
tldr: "Declarative rules governing LLM decoder behavior — output format, length, vocabulary, and safety boundaries"
when_to_use: "Building, reviewing, or reasoning about constraint_spec artifacts"
keywords: [constraints, guardrails, generation-rules]
feeds_kinds: [constraint_spec]
density_score: null
related:
  - constraint-spec-builder
  - bld_examples_constraint_spec
  - bld_collaboration_constraint_spec
  - p10_lr_constraint_spec_builder
  - bld_knowledge_card_constraint_spec
  - p03_sp_constraint_spec_builder
  - p01_kc_response_format
  - bld_architecture_constraint_spec
  - p01_kc_action_prompt
  - p03_constraint_spec
---

# Constraint Spec

## Spec
```yaml
kind: constraint_spec
pillar: P03
llm_function: CONSTRAIN
max_bytes: 2048
naming: p03_constraint.md
core: true
```

## What It Is
A constraint spec is a declarative set of rules that govern LLM generation behavior — output format, max length, allowed vocabulary, forbidden topics, and safety boundaries. It shapes the decoder without changing the task (action_prompt) or identity (system_prompt). It is NOT a validation_schema (P06, which validates after generation) — a constraint spec operates during generation to steer the output.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `BaseOutputParser` constraints / `StructuredOutputParser` | Output format constraints enforced via parser instructions |
| LlamaIndex | `ResponseSynthesizer` params / output format config | Controls how responses are synthesized and formatted |
| CrewAI | `Task(expected_output=..., guardrail=...)` | Guardrail function validates output; expected_output constrains format |
| DSPy | `Signature` output field types + `Assert`/`Suggest` | Type constraints on OutputField; runtime assertions on quality |
| Haystack | `ConditionalRouter` + component output types | Type-safe component outputs enforce structural constraints |
| OpenAI | `response_format` + `strict` mode | `json_schema` with strict=true guarantees schema compliance |
| Anthropic | `tool_choice` + `strict` param on tool defs | Strict tool use ensures schema-conformant structured output |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| max_bytes | int | 5120 | Lower = concise but may truncate complex responses |
| output_format | enum | "text" | Structured = parseable but less natural; free = creative but unparseable |
| forbidden_topics | list | [] | More = safer but may over-restrict legitimate content |
| temperature_override | float | null | Lower = deterministic but less creative |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Format constraint | Need parseable output | `output_format: json, schema: {name: str, price: float}` |
| Length constraint | Token budget management | `max_tokens: 500, density_min: 0.85` |
| Safety constraint | User-facing or compliance contexts | `forbidden: [medical_advice, financial_advice, pii]` |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Over-constraining creative tasks | Model produces stilted, formulaic output | Relax constraints for exploration; tighten only for final output |
| Constraints in system_prompt text | Hard to version, test, or compose independently | Extract constraints to standalone constraint_spec artifact |

## Integration Graph
```
[action_prompt] --> [constraint_spec] --> [output_template]
                         |
                  [prompt_template]
```

## Decision Tree
- IF output must be machine-parseable THEN use format constraint with schema
- IF task is safety-sensitive THEN add forbidden_topics constraint
- IF token budget is tight THEN add max_bytes + density_min constraints
- DEFAULT: Minimal constraints (output_format + max_bytes only)

## Quality Criteria
- GOOD: Has output format and max_bytes defined; constraints are testable
- GREAT: Each constraint has rationale; constraints compose without conflict
- FAIL: Contradictory constraints; constraints embedded in prose; untestable rules

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[constraint-spec-builder]] | related | 0.34 |
| [[bld_examples_constraint_spec]] | downstream | 0.34 |
| [[bld_collaboration_constraint_spec]] | downstream | 0.33 |
| [[p10_lr_constraint_spec_builder]] | downstream | 0.31 |
| [[bld_knowledge_card_constraint_spec]] | sibling | 0.30 |
| [[p03_sp_constraint_spec_builder]] | related | 0.30 |
| [[p01_kc_response_format]] | sibling | 0.30 |
| [[bld_architecture_constraint_spec]] | downstream | 0.28 |
| [[p01_kc_action_prompt]] | sibling | 0.28 |
| [[p03_constraint_spec]] | related | 0.25 |
