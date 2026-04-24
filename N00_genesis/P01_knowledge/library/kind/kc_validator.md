---
id: p01_kc_validator
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P06
title: "Validator — Deep Knowledge for validator"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: knowledge_agent
domain: validator
quality: 9.1
tags: [validator, P06, GOVERN, kind-kc]
tldr: "Discrete pass/fail validation rule applied at pipeline boundaries or pre-commit quality gates."
when_to_use: "Building, reviewing, or reasoning about validator artifacts"
keywords: [validator, rule, pass-fail, quality-gate, pre-commit]
feeds_kinds: [validator]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - validator-builder
  - bld_architecture_validator
  - bld_knowledge_card_validator
  - output-validator-builder
  - p03_sp_validator-builder
  - p11_qg_validator
  - bld_architecture_quality_gate
  - bld_memory_validator
  - bld_examples_validator
  - bld_collaboration_output_validator
---

# Validator

## Spec
```yaml
kind: validator
pillar: P06
llm_function: GOVERN
max_bytes: 3072
naming: p06_val_{{rule}}.yaml
core: true
```

## What It Is
A single, named, executable validation rule that returns PASS or FAIL for a specific condition. Applied at pipeline pre-commit stages, quality gates, or artifact submission checks. NOT a quality_gate (P11)—quality_gate aggregates numeric scores; validator is binary. NOT scoring_rubric (P07)—rubric defines multi-dimensional criteria; validator runs one deterministic check.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | validate() method | Custom validator in runnable chain |
| LlamaIndex | EvalResult / correctness | Binary pass/fail eval module |
| CrewAI | guardrail func | task.guardrail callback returning bool |
| DSPy | assert/suggest | Runtime assertion with message |
| Haystack | ValidationError component | Raises error on constraint violation |
| OpenAI | moderation endpoint | Binary safe/unsafe classifier |
| Anthropic | content policy check | Pre-flight content safety validation |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| rule_type | enum | structural | structural/semantic/safety/performance |
| on_fail | enum | block | block/warn/auto_fix |
| severity | enum | error | error/warning/info |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Pre-commit gate | Block bad artifact from being saved | p06_val_density_min.yaml |
| Pipeline guard | Validate stage output before proceeding | p06_val_required_fields.yaml |
| Safety check | Detect policy violations | p06_val_no_pii.yaml |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Validator with score output | Blurs binary with scored eval | Use scoring_rubric (P07) for scores |
| Chained validators as one file | Hard to disable individually | One rule = one validator file |
| Using quality_gate syntax | Wrong pillar, wrong contract | quality_gate aggregates; validator tests one |

## Integration Graph
```
[validation_schema] --> [validator] --> [pipeline gate]
[scoring_rubric] -----> [validator]         |
                             |-----------> [quality_gate (P11)]
                             |-----------> [pre-commit hook]
```

## Decision Tree
- IF binary pass/fail on one condition THEN validator
- IF numeric scoring across multiple dimensions THEN scoring_rubric (P07)
- IF aggregating multiple scores into a threshold decision THEN quality_gate (P11)
- DEFAULT: validator for any atomic pre-commit or pipeline guard check

## Quality Criteria
- GOOD: Single condition, binary result, named for the rule it enforces
- GREAT: on_fail action defined, severity set, linked to validation_schema it enforces
- FAIL: Multiple conditions in one file, returns score instead of bool, no on_fail

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[validator-builder]] | related | 0.45 |
| [[bld_architecture_validator]] | downstream | 0.42 |
| [[bld_knowledge_card_validator]] | sibling | 0.38 |
| [[output-validator-builder]] | upstream | 0.37 |
| [[p03_sp_validator-builder]] | upstream | 0.37 |
| [[p11_qg_validator]] | related | 0.37 |
| [[bld_architecture_quality_gate]] | downstream | 0.36 |
| [[bld_memory_validator]] | downstream | 0.34 |
| [[bld_examples_validator]] | downstream | 0.34 |
| [[bld_collaboration_output_validator]] | downstream | 0.33 |
