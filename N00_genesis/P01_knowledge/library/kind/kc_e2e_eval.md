---
id: p01_kc_e2e_eval
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P07
title: "E2E Eval — Deep Knowledge for e2e_eval"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: knowledge_agent
domain: e2e_eval
quality: 9.1
tags: [e2e_eval, P07, GOVERN, kind-kc]
tldr: "End-to-end correctness test of a complete pipeline from raw input to final output across all stages."
when_to_use: "Building, reviewing, or reasoning about e2e_eval artifacts"
keywords: [e2e, pipeline, integration-test, end-to-end]
feeds_kinds: [e2e_eval]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
aliases: ["end-to-end test", "integration test", "pipeline test", "full-stack eval", "system test"]
user_says: ["test the whole pipeline", "testar o pipeline completo", "run an integration test", "check if everything works together", "evaluate end to end"]
long_tails: ["I need to test the entire pipeline from user input to final output", "verify that all agents and tools work correctly together", "run an end-to-end test across all stages of my workflow", "check if the full pipeline handles error recovery correctly"]
cross_provider:
  langchain: "End-to-end chain.invoke() test"
  llamaindex: "QueryPipeline eval run"
  crewai: "Crew.kickoff() test"
  dspy: "Evaluate on full compiled program"
  openai: "Assistants thread eval"
  anthropic: "Multi-turn eval with tool use"
  haystack: "Pipeline.run() test"
related:
  - e2e-eval-builder
  - p03_sp_e2e_eval_builder
  - bld_architecture_e2e_eval
  - p01_kc_unit_eval
  - bld_instruction_e2e_eval
  - p01_kc_smoke_eval
  - p10_lr_e2e_eval_builder
  - bld_collaboration_e2e_eval
  - bld_architecture_unit_eval
  - unit-eval-builder
---

# E2E Eval

## Spec
```yaml
kind: e2e_eval
pillar: P07
llm_function: GOVERN
max_bytes: 4096
naming: p07_e2e_{{pipeline}}.md + .yaml
core: false
```

## What It Is
A test that exercises a complete pipeline end-to-end—from raw user input through all agents, tools, and transforms to the final output—and asserts correctness of the result. Tests integration between all stages, not individual components. NOT unit_eval (isolated scope, one agent or prompt). NOT benchmark (measures performance magnitude, not correctness).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | End-to-end chain test | Full chain.invoke() + output assertion |
| LlamaIndex | QueryPipeline eval run | Runs full pipeline, checks final answer |
| CrewAI | Crew.kickoff() test | Full crew run with expected output check |
| DSPy | Evaluate on full program | Runs full compiled program, checks metric |
| Haystack | Pipeline.run() test | Full pipeline execution + output assertions |
| OpenAI | Assistants thread eval | Full thread from user -> final message check |
| Anthropic | Multi-turn eval | Full conversation eval with tool use |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| stages | list[str] | required | More stages = more coverage, slower |
| timeout_s | int | 120 | Low = fast fail, high = catches slow paths |
| flakiness_retries | int | 2 | Higher = masks real issues |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Happy path | Test nominal flow end-to-end | p07_e2e_research_pipeline.yaml |
| Error recovery | Test failure + fallback handling | p07_e2e_tool_failure_recovery.yaml |
| Multi-agent handoff | Test agent A -> B -> C chain | p07_e2e_research_to_anuncio.yaml |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Testing isolated component as e2e | Mislabeled unit_eval | If < full pipeline, use unit_eval |
| No stage list documented | Can't debug failure | List every pipeline stage explicitly |
| Retries > 3 | Masks flaky integration issues | Fix root cause, keep retries <= 2 |

## Integration Graph
```
[eval_dataset] --> [e2e_eval] --> [pass/fail report]
[golden_test] ---> [e2e_eval]         |
                       |----------> [quality_gate (P11)]
                       |----------> [regression_check]
```

## Decision Tree
- IF testing a single agent or prompt in isolation THEN unit_eval
- IF testing the complete pipeline from user input to final output THEN e2e_eval
- IF only running a fast sanity check THEN smoke_eval
- DEFAULT: e2e_eval for integration testing across multi-stage pipelines

## Quality Criteria
- GOOD: Covers happy path, all pipeline stages documented, timeout set
- GREAT: Error paths covered, golden_test cases used as inputs, flakiness tracked
- FAIL: Only tests one stage, no timeout, assertions too vague (e.g., "output exists")

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[e2e-eval-builder]] | related | 0.46 |
| [[p03_sp_e2e_eval_builder]] | upstream | 0.42 |
| [[bld_architecture_e2e_eval]] | downstream | 0.41 |
| [[p01_kc_unit_eval]] | sibling | 0.41 |
| [[bld_instruction_e2e_eval]] | upstream | 0.38 |
| [[p01_kc_smoke_eval]] | sibling | 0.37 |
| [[p10_lr_e2e_eval_builder]] | downstream | 0.37 |
| [[bld_collaboration_e2e_eval]] | downstream | 0.34 |
| [[bld_architecture_unit_eval]] | downstream | 0.33 |
| [[unit-eval-builder]] | related | 0.32 |
