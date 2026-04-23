---
id: p01_kc_unit_eval
kind: knowledge_card
type: kind
pillar: P07
title: "Unit Eval — Deep Knowledge for unit_eval"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: knowledge_agent
domain: unit_eval
quality: 9.1
tags: [unit_eval, P07, GOVERN, kind-kc]
tldr: "Isolated correctness test of a single agent or prompt against expected output with scoring."
when_to_use: "Building, reviewing, or reasoning about unit_eval artifacts"
keywords: [unit-eval, isolated, correctness, agent-test, prompt-test]
feeds_kinds: [unit_eval]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
aliases: ["unit test", "agent test", "prompt test", "isolated eval", "component test"]
user_says: ["test this agent", "testar esse agente", "write a unit test", "check if the prompt works", "evaluate this component"]
long_tails: ["I need to test if this agent produces correct output for known inputs", "write an isolated test for a single prompt with scoring", "evaluate whether my agent handles edge cases correctly", "create a regression test for this prompt after I change it"]
cross_provider:
  langchain: "Unit test + LLM mock"
  llamaindex: "QueryEngine unit test"
  crewai: "Single agent test with mocked tools"
  dspy: "Evaluate(program, devset)"
  openai: "Single call + assertion"
  anthropic: "Single message + rubric scoring"
  haystack: "Component unit test"
related:
  - bld_architecture_unit_eval
  - p01_kc_e2e_eval
  - unit-eval-builder
  - p01_kc_smoke_eval
  - bld_knowledge_card_unit_eval
  - p03_sp_unit-eval-builder
  - p03_sp_e2e_eval_builder
  - p01_kc_golden_test
  - bld_memory_unit_eval
  - p01_kc_llm_judge
---

# Unit Eval

## Spec
```yaml
kind: unit_eval
pillar: P07
llm_function: GOVERN
max_bytes: 4096
naming: p07_ue_{{target}}.md + .yaml
core: true
```

## What It Is
A test that evaluates a single agent, prompt, or pipeline component in isolation—mocking dependencies—against a defined set of inputs and expected outputs. Scores each output against a scoring_rubric or exact match. NOT smoke_eval (only checks structural validity, no scoring, <30s). NOT e2e_eval (tests all stages together; unit_eval mocks all but the target component).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | Unit test + LLM mock | Chain test with mocked or real LLM |
| LlamaIndex | QueryEngine unit test | Single query engine test with assertions |
| CrewAI | Single agent test | One agent task with mocked tools |
| DSPy | Evaluate(program, devset) | Evaluate single module against devset |
| Haystack | Component unit test | Single component test with mock inputs |
| OpenAI | Single call + assertion | One model call with expected output check |
| Anthropic | Single message + rubric | One messages.create + scoring |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| target | str | required | Agent name, prompt ID, or tool name |
| n_cases | int | >= 10 | More = robust, higher cost |
| scorer | enum | llm_judge | llm_judge/exact/regex/semantic_sim |
| threshold | float | 7.0 | Pass score; below = fail |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Prompt regression | Test prompt after any edit | p07_ue_anuncio_prompt.yaml |
| Agent behavior | Verify agent decides correctly | p07_ue_router_agent.yaml |
| Tool output | Check tool returns expected shape | p07_ue_search_tool.yaml |
| Rubric-scored | LLM judge scores each output | scorer: llm_judge + rubric ref |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Testing without mocking deps | Flaky: fails due to external services | Mock all dependencies except target |
| n_cases < 5 | No statistical signal | Minimum 10 cases per unit eval |
| Exact match for LLM output | LLM is nondeterministic | Use semantic_sim or llm_judge scorer |
| Using for full pipeline | Scope creep, hard to debug | Extract to e2e_eval for pipeline tests |

## Integration Graph
```
[eval_dataset] --> [unit_eval] --> [pass/fail + scores]
[scoring_rubric] -> [unit_eval]         |
[llm_judge] ------> [unit_eval] --> [regression_check]
                        |--------> [quality_gate (P11)]
```

## Decision Tree
- IF fast structural check only THEN smoke_eval
- IF testing one component in isolation with scoring THEN unit_eval
- IF testing complete pipeline THEN e2e_eval
- IF comparing against baseline THEN regression_check (wraps unit_eval output)
- DEFAULT: unit_eval for any agent or prompt after initial implementation

## Quality Criteria
- GOOD: Target isolated, >= 10 cases, scorer + threshold defined
- GREAT: From eval_dataset, uses llm_judge calibrated on golden_tests, CI-integrated
- FAIL: Tests multiple components together, n_cases < 5, no threshold, exact match on LLM

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_unit_eval]] | downstream | 0.42 |
| [[p01_kc_e2e_eval]] | sibling | 0.41 |
| [[unit-eval-builder]] | related | 0.40 |
| [[p01_kc_smoke_eval]] | sibling | 0.36 |
| [[bld_knowledge_card_unit_eval]] | sibling | 0.36 |
| [[p03_sp_unit-eval-builder]] | upstream | 0.32 |
| [[p03_sp_e2e_eval_builder]] | upstream | 0.31 |
| [[p01_kc_golden_test]] | sibling | 0.30 |
| [[bld_memory_unit_eval]] | downstream | 0.29 |
| [[p01_kc_llm_judge]] | sibling | 0.28 |
