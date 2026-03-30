---
kind: output_template
id: bld_output_template_law
pillar: P00
---
id: p08_law_{{number}}
kind: law
pillar: P08
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
domain: "{{domain}}"
quality: null
tags: [{{tag_1}}, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
number: {{integer}}
statement: "{{imperative_rule_one_sentence}}"
rationale: "{{why_this_law_exists}}"
enforcement: "{{how_violation_detected}}"
scope: "{{system|agent_node|domain}}"
exceptions: [{{exception_1_or_empty}}]
priority: {{integer_1_to_10}}
keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}]
---

## Statement
{{imperative_rule_expanded}}
## Rationale
{{why_this_law_exists_detailed}}
## Enforcement
- Mechanism: {{automated_check_or_review_or_runtime}}
- Detection: {{how_violation_is_detected}}
- Consequence: {{what_happens_on_violation}}
## Exceptions
{{exception_conditions_or_none}}
## Examples
1. **{{example_name_1}}**: {{correct_application_1}}
2. **{{example_name_2}}**: {{correct_application_2}}
## Violations
1. **{{violation_name_1}}**: {{what_happened_and_consequence_1}}
2. **{{violation_name_2}}**: {{what_happened_and_consequence_2}}
## History
- Established: {{date_and_reason}}
- {{revision_if_any_or_remove_line}}
## References
- {{reference_1}}
- {{reference_2}}
