---
id: p01_kc_few_shot_example
kind: knowledge_card
type: kind
pillar: P01
title: "Few-Shot Example — Deep Knowledge for few_shot_example"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: few_shot_example
quality: 9.1
tags: [few_shot_example, p01, INJECT, kind-kc]
tldr: "Input/output pair injected into prompts to teach format and reasoning by demonstration — the most reliable steering mechanism after instructions"
when_to_use: "Building, reviewing, or reasoning about few_shot_example artifacts"
keywords: [few-shot, in-context-learning, examples, demonstration]
feeds_kinds: [few_shot_example]
density_score: null
related:
  - bld_collaboration_few_shot_example
  - few-shot-example-builder
  - p01_fse_{{TOPIC_SLUG}}
  - p10_lr_few_shot_example_builder
  - p03_sp_few_shot_example_builder
  - bld_knowledge_card_few_shot_example
  - p01_fse_builder_golden
  - bld_examples_few_shot_example
  - p01_kc_prompt_engineering_best_practices
  - bld_schema_few_shot_example
---

# Few-Shot Example

## Spec
```yaml
kind: few_shot_example
pillar: P01
llm_function: INJECT
max_bytes: 1024
naming: p01_fse_{{topic}}.md + .yaml
core: true
```

## What It Is
A few_shot_example is a curated input/output pair injected into prompts to demonstrate expected format, reasoning pattern, or style. It teaches by showing, not telling. It is NOT a golden_test (P07, which evaluates output quality against ground truth) — few-shot examples steer generation, golden tests validate it. Few-shot examples are the single most effective technique for format compliance and consistent output structure.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `FewShotPromptTemplate` / `ExampleSelector` | Supports static lists or similarity-based selection |
| LlamaIndex | Few-shot via `PromptTemplate` string injection | No dedicated class; examples in template text |
| CrewAI | Task `expected_output` + agent examples | Informal; embedded in task descriptions |
| DSPy | `dspy.Example` + `dspy.BootstrapFewShot` | Auto-selects optimal examples via optimization |
| Haystack | `PromptBuilder` with example slots | Jinja2 templates with example iteration |
| OpenAI | Multi-turn user/assistant message pairs | Most effective pattern for chat models |
| Anthropic | Human/Assistant turn pairs in messages | Supports prefilled assistant turns for steering |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| input | string | required | Must be representative of real queries |
| output | string | required | Must be the exact format you want replicated |
| quality | float | required | Higher quality examples = better model adherence |
| count | int | 2-5 | More examples = better format lock but higher token cost |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Static few-shot | Consistent output format needed | 3 fixed examples showing JSON output structure |
| Dynamic selection | Large example pool, varied queries | Embed query, select 3 most similar examples |
| Chain-of-thought | Complex reasoning tasks | Input + reasoning steps + final answer |
| Negative examples | Common failure modes to avoid | "BAD: ..." paired with "GOOD: ..." |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Too many examples (>7) | Token waste; model starts pattern-matching noise | Use 2-5 high-quality examples |
| Examples don't match real inputs | Model learns wrong distribution | Source examples from production queries |
| Output format inconsistent across examples | Model averages formats, produces hybrid garbage | Standardize all example outputs to identical schema |

## Integration Graph
```
[knowledge_card, context_doc] --> [few_shot_example] --> [template (P03)]
                                        |
                                  [golden_test (P07)]
```

## Decision Tree
- IF output must follow exact JSON/YAML schema THEN 2-3 static examples with identical structure
- IF query types vary widely THEN dynamic selection from example pool
- IF complex multi-step reasoning THEN chain-of-thought examples
- IF model keeps making specific errors THEN add negative examples
- DEFAULT: 3 static examples covering common, edge, and boundary cases

## Quality Criteria
- GOOD: Input/output pair is representative; output matches desired format exactly
- GREAT: Covers common + edge cases; quality scored; tested for format compliance improvement
- FAIL: Output format differs from what's actually expected; examples are hypothetical not real

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_few_shot_example]] | downstream | 0.39 |
| [[few-shot-example-builder]] | related | 0.34 |
| [[p01_fse_{{TOPIC_SLUG}}]] | related | 0.31 |
| [[p10_lr_few_shot_example_builder]] | downstream | 0.30 |
| [[p03_sp_few_shot_example_builder]] | downstream | 0.30 |
| [[bld_knowledge_card_few_shot_example]] | sibling | 0.29 |
| [[p01_fse_builder_golden]] | related | 0.28 |
| [[bld_examples_few_shot_example]] | downstream | 0.27 |
| [[p01_kc_prompt_engineering_best_practices]] | sibling | 0.27 |
| [[bld_schema_few_shot_example]] | downstream | 0.26 |
