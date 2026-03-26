---
id: memory_prompt_template_builder
kind: memory
pillar: P10
llm_function: INJECT
domain: prompt_template
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [memory, prompt-template, P03, anti-patterns, lessons]
---

# Memory — prompt-template-builder

## Common Mistakes (7)

1. **Static prompt submitted as template**: Producer writes a complete, fixed prompt with no `{{variables}}` and labels it `kind: prompt_template`. Gate H08 catches this — the template body must contain at least one `{{variable}}`.

2. **Undeclared variable in body**: Template body uses `{{context}}` but the variables list only declares `{{topic}}` and `{{domain}}`. Gate H03 catches this. Fix: add `context` to the variables list with type, required, default, description.

3. **Declared variable missing from body**: Variables list declares `include_examples: boolean` but the template body never references `{{include_examples}}`. Gate H04 catches this. Fix: either add `{{include_examples}}` to the body or remove it from the variables list.

4. **ID pattern violation**: Producer uses `knowledge_card` instead of `p03_pt_knowledge_card`. Gate H01 catches this. The full prefix `p03_pt_` is mandatory — it encodes both pillar and kind.

5. **Mixed syntax tiers**: Template uses `{{topic}}` (Mustache tier-1) and `[DOMAIN]` (bracket tier-2) in the same body. Fix: choose one tier, set `variable_syntax` accordingly, and rewrite all slots to match.

6. **Conflating prompt_template with meta_prompt**: A template that instructs the LLM to "generate a better prompt for X" is a `meta_prompt`, not a `prompt_template`. Decision test: does invoking this artifact produce a rendered prompt (template) or another prompt artifact (meta_prompt)?

7. **Quality field left as null after validation**: Producer validates against all gates, gets a score, but forgets to write the numeric score back into the `quality` field. Artifacts with `quality: null` are blocked from pool submission.

## Template Patterns

| Pattern | When to use | Example id |
|---|---|---|
| Single-topic synthesis | One topic, multiple depth controls | `p03_pt_research_synthesis` |
| Role + task matrix | Parameterize both role and task | `p03_pt_role_task_executor` |
| Conditional sections | boolean vars control included blocks | `p03_pt_knowledge_card_production` |
| List iteration | list var drives repeated structure | `p03_pt_batch_review` |
| Domain-scoped generation | domain var constrains terminology | `p03_pt_domain_explainer` |
| Audience-adaptive | audience var controls depth/vocabulary | `p03_pt_adaptive_explanation` |

## Production Counter

| Metric | Value |
|---|---|
| Templates produced | 0 (builder initialized 2026-03-26) |
| Average quality score | — |
| Most common failure gate | — |
| Most reused variable name | — |

*(Update this table after each production run.)*
