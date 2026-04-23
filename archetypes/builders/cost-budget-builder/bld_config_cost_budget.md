---
kind: config
id: bld_config_cost_budget
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 20
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Cost Budget"
version: "1.0.0"
author: n03_builder
tags: [cost_budget, builder, config, P09]
tldr: "Naming, path, and size constraints for cost_budget production: p09_cb_{name_slug}.yaml, 3072 bytes max."
domain: "cost budget construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_knowledge_card_cost_budget
  - bld_schema_cost_budget
  - bld_examples_cost_budget
  - bld_config_memory_scope
  - bld_config_batch_config
  - bld_config_prompt_version
  - bld_config_retriever_config
  - bld_config_output_validator
  - bld_instruction_cost_budget
  - bld_config_handoff_protocol
---
# Config: cost_budget Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_cb_{name_slug}.yaml` | `p09_cb_anthropic.yaml` |
| Builder directory | kebab-case | `cost-budget-builder/` |
| Frontmatter fields | snake_case | `reset_policy`, `overage_action` |
| Name slug | snake_case, lowercase, no hyphens | `anthropic`, `global`, `claude_opus` |
| Provider names | lowercase, official slug | `anthropic`, `openai`, `google`, `ollama` |
| Model slugs | lowercase with hyphens | `claude-opus-4-6`, `gpt-4o`, `gemini-2.5-pro` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL (use underscores in id).

## File Paths
1. Output: `P09_config/examples/p09_cb_{name_slug}.md`
2. Compiled: `P09_config/compiled/p09_cb_{name_slug}.yaml`

## Size Limits (aligned with SCHEMA)
1. Body: max 3072 bytes
2. Total (frontmatter + body): ~4200 bytes
3. Density: >= 0.85 (no filler; tables over prose)

## Reset Policy Enum
| Value | When to use |
|-------|-------------|
| daily | Interactive services billed or monitored daily |
| weekly | Batch jobs on weekly cadence |
| monthly | SaaS products on monthly billing cycle |
| rolling_7d | 7-day rolling window to avoid month-boundary spikes |
| rolling_30d | 30-day rolling window for smoother cap enforcement |
| none | One-time project budget that must not be reset |

## Overage Action Enum
| Value | Behavior |
|-------|----------|
| block | Hard stop: raise BudgetExceededError before API call |
| warn | Soft alert: allow call, notify ops channel, continue |
| log | Silent audit: allow call, write to cost audit log only |

## Currency Conventions
| Unit | Field value | Numeric type |
|------|-------------|--------------|
| US Dollars | USD | float, 2 decimal places |
| Raw tokens | token_units | integer |

Rule: do not mix USD and token_units in the same budget catalog without explicit rationale.

## Metadata

```yaml
id: bld_config_cost_budget
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld_config_cost_budget.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_cost_budget]] | upstream | 0.38 |
| [[bld_schema_cost_budget]] | upstream | 0.35 |
| [[bld_examples_cost_budget]] | upstream | 0.35 |
| [[bld_config_memory_scope]] | sibling | 0.33 |
| [[bld_config_batch_config]] | sibling | 0.33 |
| [[bld_config_prompt_version]] | sibling | 0.32 |
| [[bld_config_retriever_config]] | sibling | 0.32 |
| [[bld_config_output_validator]] | sibling | 0.31 |
| [[bld_instruction_cost_budget]] | upstream | 0.31 |
| [[bld_config_handoff_protocol]] | sibling | 0.30 |
