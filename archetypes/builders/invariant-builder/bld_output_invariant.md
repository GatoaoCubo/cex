---
kind: output_template
id: bld_output_template_invariant
pillar: P00
quality: 9.0
title: "Output Template Invariant"
version: "1.0.0"
author: n03_builder
tags: [invariant, builder, examples]
tldr: "Golden and anti-examples for invariant construction, demonstrating ideal structure and common pitfalls."
domain: "invariant construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: PRODUCE
related:
  - bld_output_template_axiom
  - bld_knowledge_card_invariant
  - bld_schema_invariant
  - p11_qg_law
  - p03_ins_law
  - bld_output_template_pattern
  - p08_law_{{NUMBER}}
  - bld_examples_invariant
  - bld_output_template_learning_record
  - bld_output_template_golden_test
---
id: p08_law_`{{number}}`
kind: invariant
pillar: P08
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "`{{who_produced}}`"
domain: "`{{domain}}`"
quality: null
tags: [`{{tag_1}}`, {{tag_2}}, `{{tag_3}}`]
tldr: "`{{dense_summary_max_160ch}}`"
number: `{{integer}}`
statement: "`{{imperative_rule_one_sentence}}`"
rationale: "`{{why_this_law_exists}}`"
enforcement: "`{{how_violation_detected}}`"
scope: "{{system|agent_group|domain}}"
exceptions: [`{{exception_1_or_empty}}`]
priority: `{{integer_1_to_10}}`
keywords: [`{{keyword_1}}`, {{keyword_2}}, `{{keyword_3}}`]
---

## Statement
`{{imperative_rule_expanded}}`
## Rationale
`{{why_this_law_exists_detailed}}`
## Enforcement
1. Mechanism: `{{automated_check_or_review_or_runtime}}`
2. Detection: `{{how_violation_is_detected}}`
3. Consequence: `{{what_happens_on_violation}}`
## Exceptions
`{{exception_conditions_or_none}}`
## Examples
1. **`{{example_name_1}}`**: `{{correct_application_1}}`
2. **`{{example_name_2}}`**: `{{correct_application_2}}`
## Violations
1. **`{{violation_name_1}}`**: `{{what_happened_and_consequence_1}}`
2. **`{{violation_name_2}}`**: `{{what_happened_and_consequence_2}}`
## History
1. Established: `{{date_and_reason}}`
2. `{{revision_if_any_or_remove_line}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Metadata

```yaml
id: bld_output_template_invariant
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-output-template-invariant.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P00 |
| Domain | invariant construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_axiom]] | sibling | 0.39 |
| [[bld_knowledge_card_invariant]] | related | 0.35 |
| [[bld_schema_invariant]] | related | 0.34 |
| [[p11_qg_law]] | related | 0.33 |
| [[p03_ins_law]] | related | 0.31 |
| [[bld_output_template_pattern]] | sibling | 0.31 |
| [[p08_law_{{NUMBER}}]] | related | 0.30 |
| [[bld_examples_invariant]] | related | 0.30 |
| [[bld_output_template_learning_record]] | sibling | 0.30 |
| [[bld_output_template_golden_test]] | sibling | 0.29 |
