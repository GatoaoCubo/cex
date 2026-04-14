---
kind: output_template
id: bld_output_template_decision_record
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a decision_record artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.1
title: "Output Template Decision Record"
version: "1.0.0"
author: n03_builder
tags: [decision_record, builder, examples]
tldr: "Golden and anti-examples for decision record construction, demonstrating ideal structure and common pitfalls."
domain: "decision record construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: decision_record
```yaml
id: p08_adr_{{decision_slug}}
kind: decision_record
pillar: P08

title: "{{human_readable_decision_title_max_80ch}}"
status: {{proposed|accepted|deprecated|superseded}}
context: "{{one_sentence_why_this_decision_arose}}"
decision: "{{one_sentence_what_was_decided}}"

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

quality: null
tags: [decision_record, {{domain_tag}}, {{pillar_or_area_tag}}]
tldr: "{{dense_summary_of_decision_and_primary_consequence_max_160ch}}"
consequences: "{{brief_summary_of_key_tradeoffs}}"

options:
  - "{{option_a_name}}"
  - "{{option_b_name}}"
supersedes: {{null|p08_adr_{{older_slug}}}}

superseded_by: {{null|p08_adr_{{newer_slug}}}}
related_to: [{{p08_adr_related_slug_1}}, {{p08_adr_related_slug_2}}]
deciders: ["{{name_or_role_1}}", "{{name_or_role_2}}"]
date_decided: "{{YYYY-MM-DD}}"
```
## Context
{{
  Describe the problem, forces, and circumstances that made this decision necessary.
  Answer: what was happening in the system/team/project that required a choice?

  Use 2-5 sentences. Write in present or past tense — not future.
  Do NOT state the decision here — only the situation.
}}
## Options Considered
### Option A: `{{option_a_name}}`
`{{brief description of option A}}`
Pros:
1. `{{pro_1}}`
2. `{{pro_2}}`
Cons:
1. `{{con_1}}`
2. `{{con_2}}`
### Option B: `{{option_b_name}}`
`{{brief description of option B}}`
Pros:
1. `{{pro_1}}`
2. `{{pro_2}}`
Cons:
1. `{{con_1}}`
2. `{{con_2}}`
### Option C: `{{option_c_name}}` (if applicable)
`{{brief description of option C}}`
Pros:
- `{{pro_1}}`

Cons:
- `{{con_1}}`
## Decision
{{
  State the chosen option clearly in the first sentence.
  Example: "We will use Option B: `{{option_b_name}}`."

  Follow with the primary rationale in 2-4 sentences.
  Explain why this option was preferred over the alternatives.
}}
## Consequences
**Positive:**
1. `{{what_becomes_easier_or_better}}`
2. `{{capability_or_property_gained}}`
**Negative:**
1. `{{what_becomes_harder_or_constrained}}`
2. `{{technical_debt_or_risk_introduced}}`
**Neutral:**
- `{{change_in_process_or_tooling_without_clear_valence}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | decision record construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
