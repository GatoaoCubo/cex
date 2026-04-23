---
kind: output_template
id: bld_output_template_few_shot_example
pillar: P05
llm_function: PRODUCE
purpose: Canonical output template for few_shot_example artifacts
quality: 9.0
title: "Output Template Few Shot Example"
version: "1.0.0"
author: n03_builder
tags: [few_shot_example, builder, examples]
tldr: "Golden and anti-examples for few shot example construction, demonstrating ideal structure and common pitfalls."
domain: "few shot example construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_few_shot_example
  - bld_instruction_few_shot_example
  - p10_lr_few_shot_example_builder
  - p03_sp_few_shot_example_builder
  - bld_config_few_shot_example
  - few-shot-example-builder
  - p11_qg_few_shot_example
  - bld_collaboration_few_shot_example
  - p01_fse_{{TOPIC_SLUG}}
  - bld_examples_response_format
---

# Output Template: few_shot_example
## Frontmatter Template
```yaml
id: p01_fse_{{topic_slug}}
kind: few_shot_example
pillar: P01
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
input: "{{task_request_or_prompt}}"
output: "{{ideal_response_showing_format}}"
domain: "{{artifact_kind_being_exemplified}}"
difficulty: "{{easy|medium|hard}}"
edge_case: {{true|false}}
format: "{{what_format_this_exemplifies}}"
quality: null
tags: [few-shot, {{domain_tag}}, {{format_tag}}]
tldr: "{{dense_summary_max_160ch}}"
keywords: [{{kw1}}, {{kw2}}, {{kw3}}]
```
## Body Template
```markdown
## Explanation
[WHY this input/output pair teaches the target format.
What pattern does the LLM learn from this example?
Which format rule is demonstrated?]
## Variations
- **Variation 1**: {{alternative_input_testing_different_aspect}}
- **Variation 2**: {{alternative_input_with_different_domain}}
- **Variation 3** (optional): {{harder_variation}}
## Edge Cases
- **Edge**: {{boundary_input_description}}
  **Expected**: {{how_output_handles_boundary}}
## References
- Schema: `_schemas/p01_schema.yaml`
- Related: `{{related_p01_fse_id}}` (if exists)
```
## Field Guidance
| Field | Rule | Example |
|-------|------|---------|
| id | p01_fse_{slug}, matches filename | p01_fse_kc_frontmatter |
| input | Realistic user request, not abstract | "Create a knowledge card about Docker networking" |
| output | Complete format demo, not description | Full YAML frontmatter block |
| quality | Always null — never self-score | null |
| difficulty | easy=canonical, medium=variation, hard=edge | medium |
| tldr | <= 160 chars, dense | "Input/output pair teaching KC YAML frontmatter format." |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_few_shot_example]] | downstream | 0.49 |
| [[bld_instruction_few_shot_example]] | upstream | 0.43 |
| [[p10_lr_few_shot_example_builder]] | downstream | 0.41 |
| [[p03_sp_few_shot_example_builder]] | upstream | 0.39 |
| [[bld_config_few_shot_example]] | downstream | 0.34 |
| [[few-shot-example-builder]] | upstream | 0.34 |
| [[p11_qg_few_shot_example]] | downstream | 0.31 |
| [[bld_collaboration_few_shot_example]] | downstream | 0.31 |
| [[p01_fse_{{TOPIC_SLUG}}]] | upstream | 0.31 |
| [[bld_examples_response_format]] | downstream | 0.30 |
