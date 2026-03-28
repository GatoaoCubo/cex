---
kind: output_template
id: bld_output_template_pattern
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a pattern
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: pattern
```yaml
id: p08_pat_{{slug}}
kind: pattern
pillar: P08
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
domain: "{{domain}}"
quality: null
tags: [{{tag_1}}, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
name: "{{pattern_name_2_5_words}}"
problem: "{{recurring_problem_one_sentence}}"
solution: "{{core_solution_approach}}"
context: "{{when_where_pattern_applies}}"
forces: [{{force_1}}, {{force_2}}]
consequences: [{{consequence_1}}, {{consequence_2}}]
related_patterns: [{{related_1}}]
anti_patterns: [{{anti_1}}]
applicability: "{{when_to_use_and_when_not}}"
keywords: [{{kw_1}}, {{kw_2}}, {{kw_3}}]
```
## Problem
{{recurring_problem_in_concrete_terms}}
## Context
- Environment: {{where_problem_occurs}}
- Frequency: {{how_often_encountered}}
- Severity: {{impact_if_unsolved}}
## Forces
- {{tension_1}}: {{why_hard_1}}
- {{tension_2}}: {{why_hard_2}}
- {{tension_3}}: {{why_hard_3}}
## Solution
{{reusable_approach_concrete_steps}}
```text
{{optional_ascii_diagram_of_solution}}
```
## Consequences
Benefits:
- {{benefit_1}}
- {{benefit_2}}
Costs:
- {{cost_1}}
- {{cost_2}}
## Examples
1. **{{example_name_1}}**: {{concrete_application_1}}
2. **{{example_name_2}}**: {{concrete_application_2}}
## Anti-Patterns
- **{{anti_name_1}}**: {{why_wrong_1}}
- **{{anti_name_2}}**: {{why_wrong_2}}
## Related Patterns
- {{related_pattern_1}}: {{relationship_description_1}}
- {{related_pattern_2}}: {{relationship_description_2}}
## References
- {{reference_1}}
- {{reference_2}}
