---
kind: output_template
id: bld_output_template_context_window_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for context_window_config production
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: context_window_config
```yaml
---
id: p03_cwc_{{model_slug}}
kind: context_window_config
pillar: P03
title: "{{Model Name}} Context Window Config"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{builder_name}}"
target_model: {{model_name}}
total_tokens: {{total_context_window}}
system_prompt_budget: {{tokens_for_system}}
few_shot_budget: {{tokens_for_examples}}
retrieved_context_budget: {{tokens_for_rag}}
user_query_budget: {{tokens_for_query}}
output_reserve: {{tokens_for_response}}
overflow_strategy: {{truncate_lowest|compress|drop_section}}
priority_tiers: [system, query, context, examples]
domain: {{domain_name}}
quality: null
tags: [context_window_config, {{tag1}}, {{tag2}}]
tldr: "{{Dense <=160ch budget description}}"
---

# {{Model Name}} Context Window Config

## Budget Allocation
| Section | Tokens | Percentage | Priority |
|---------|--------|------------|----------|
| System prompt | {{system_tokens}} | {{pct}}% | 1 (highest) |
| User query | {{query_tokens}} | {{pct}}% | 2 |
| Retrieved context | {{context_tokens}} | {{pct}}% | 3 |
| Few-shot examples | {{example_tokens}} | {{pct}}% | 4 |
| Output reserve | {{output_tokens}} | {{pct}}% | — |
| **Total** | {{total}} | 100% | — |

## Priority Tiers
1. **System prompt** — always protected (agent identity)
2. **User query** — never truncated (task definition)
3. **Retrieved context** — truncated first if over budget
4. **Few-shot examples** — dropped before context if needed

## Overflow Rules
- **Strategy**: {{overflow_strategy}}
- **Trigger**: when assembled prompt exceeds total_tokens
- **Action**: {{specific overflow handling steps}}
- **Fallback**: {{compression or summarization approach}}

## Model Profile
| Property | Value |
|----------|-------|
| Model | {{model_name}} |
| Max context | {{total_tokens}} tokens |
| Max output | {{max_output_tokens}} tokens |

## Integration
- Consumed by: prompt_template, agent_card, cex_token_budget.py
- Validated by: cex_compile.py
```
