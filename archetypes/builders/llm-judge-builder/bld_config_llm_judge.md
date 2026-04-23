---
kind: config
id: bld_config_llm_judge
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Llm Judge"
version: "1.0.0"
author: n03_builder
tags: [llm_judge, builder, examples]
tldr: "Golden and anti-examples for llm judge construction, demonstrating ideal structure and common pitfalls."
domain: "llm judge construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_llm_judge
  - p03_sp_llm_judge_builder
  - bld_config_memory_scope
  - bld_schema_llm_judge
  - bld_config_prompt_version
  - bld_config_retriever_config
  - bld_config_output_validator
  - bld_config_reward_signal
  - bld_config_handoff_protocol
  - bld_config_constraint_spec
---
# Config: llm_judge Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p07_judge_{slug}.md` | `p07_judge_rag_quality.md` |
| Builder directory | kebab-case | `llm-judge-builder/` |
| Frontmatter fields | snake_case | `judge_model`, `few_shot`, `chain_of_thought` |
| Judge slug | snake_case, lowercase, no hyphens | `rag_quality`, `code_correctness`, `dialogue_safety` |
| Criterion names | snake_case, noun or noun_noun | `faithfulness`, `answer_relevance`, `code_correctness` |
| Scale anchor keys | integer or float matching scale min/max | `1`, `3`, `5` or `0.0`, `0.5`, `1.0` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths
- Output: `cex/P07_evals/examples/p07_judge_{slug}.md`
- Compiled: `cex/P07_evals/compiled/p07_judge_{slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~4096 bytes
- Density: >= 0.80 (no filler)

## Scale Type Reference
| Type | Range | When to use |
|------|-------|-------------|
| binary | 0/1 or pass/fail | Hard pass/fail gates; safety checks |
| likert | 1-5 | General quality evaluation (most common) |
| extended | 1-10 | Fine-grained differentiation needed |
| continuous | 0.0-1.0 | Framework normalization (Braintrust, RAGAS) |

## Anchor Requirements
| Scale type | Minimum anchors required |
|------------|--------------------------|
| binary | 2 (0 and 1) |
| likert 1-5 | 3 (1, 3, 5) |
| extended 1-10 | 3 (1, 5, 10) |
| continuous | 3 (0.0, 0.5, 1.0) |

Rule: anchors must be concrete behavioral descriptions, not adjectives.
Good: "All claims supported by retrieved context; no fabricated facts."
Bad: "Very good response."

## Temperature Conventions
| Value | When |
|-------|------|
| 0.0 | Default — reproducible scoring (recommended) |
| 0.1 | Acceptable when very slight variation tolerated |
| 0.2 | Maximum — document reason explicitly |
| > 0.2 | NEVER for judges — score variance unacceptable |

## Criteria Count Limits
| Count | Status |
|-------|--------|
| 1 | Ideal — single-dimension focused judge |
| 2-3 | Acceptable — declare aggregation method |
| 4-5 | Maximum — verify non-overlap before publishing |
| > 5 | REJECT — split into multiple focused judges |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_llm_judge]] | upstream | 0.39 |
| [[p03_sp_llm_judge_builder]] | upstream | 0.37 |
| [[bld_config_memory_scope]] | sibling | 0.35 |
| [[bld_schema_llm_judge]] | upstream | 0.34 |
| [[bld_config_prompt_version]] | sibling | 0.34 |
| [[bld_config_retriever_config]] | sibling | 0.34 |
| [[bld_config_output_validator]] | sibling | 0.33 |
| [[bld_config_reward_signal]] | sibling | 0.32 |
| [[bld_config_handoff_protocol]] | sibling | 0.32 |
| [[bld_config_constraint_spec]] | sibling | 0.32 |
