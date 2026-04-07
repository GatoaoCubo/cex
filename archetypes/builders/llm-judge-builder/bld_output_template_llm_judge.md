---
kind: output_template
id: bld_output_template_llm_judge
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a llm_judge artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: llm_judge
```yaml
id: p07_judge_{{judge_slug}}
kind: llm_judge
pillar: P07
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_judge_name}}"
judge_model: "{{concrete_model_id}}"
criteria:
  - {{criterion_name_1}}
  - {{criterion_name_2}}
scale:
  type: {{binary|likert|extended|continuous}}
  min: {{min_value}}
  max: {{max_value}}
  anchors:
    {{min_value}}: "{{anchor_label_low}}"
    {{mid_value}}: "{{anchor_label_mid}}"
    {{max_value}}: "{{anchor_label_high}}"
quality: null
tags: [llm_judge, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_judge_evaluates_max_200ch}}"
few_shot:
  - input: "{{example_input_1}}"
    output: "{{example_output_1}}"
    score: {{score_within_scale}}
    rationale: "{{why_this_score}}"
  - input: "{{example_input_2}}"
    output: "{{example_output_2}}"
    score: {{score_within_scale}}
    rationale: "{{why_this_score}}"
framework: {{braintrust|deepeval|ragas|promptfoo|openai_evals|costm}}
temperature: {{0.0}}
chain_of_thought: {{true|false}}
aggregation: {{mean|min|max|weighted_sum}}
pass_threshold: {{threshold_value}}
```
## Overview
{{what_the_judge_evaluates_1_to_2_sentences}}
{{use_case_and_whether_reference_based_or_free}}
## Criteria
### {{criterion_name_1}}
{{definition_of_this_quality_dimension}}
High score ({{max_value}}): {{concrete_example_of_excellent_output}}
Low score ({{min_value}}): {{concrete_example_of_poor_output}}
### {{criterion_name_2}}
{{definition_of_this_quality_dimension}}
High score ({{max_value}}): {{concrete_example_of_excellent_output}}
Low score ({{min_value}}): {{concrete_example_of_poor_output}}
## Scale
Type: {{scale_type}}
Range: {{min_value}} to {{max_value}}
| Score | Label | Meaning |
|-------|-------|---------|
| {{min_value}} | {{anchor_low}} | {{what_this_looks_like_concretely}} |
| {{mid_value}} | {{anchor_mid}} | {{what_this_looks_like_concretely}} |
| {{max_value}} | {{anchor_high}} | {{what_this_looks_like_concretely}} |
Assignment guidance: {{how_to_choose_between_adjacent_scores}}
## Few-Shot Examples
### Example 1 ({{high|low}} score)
Input: {{prompt_or_question}}
Output: {{model_response_being_judged}}
Score: {{score}} / {{max_value}}
Rationale: {{chain_of_thought_reasoning_then_score_justification}}
### Example 2 ({{high|low}} score)
Input: {{prompt_or_question}}
Output: {{model_response_being_judged}}
Score: {{score}} / {{max_value}}
Rationale: {{chain_of_thought_reasoning_then_score_justification}}
