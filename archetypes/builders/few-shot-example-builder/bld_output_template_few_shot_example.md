---
kind: output_template
id: bld_output_template_few_shot_example
pillar: P05
llm_function: PRODUCE
purpose: Canonical output template for few_shot_example artifacts
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
