---
kind: output_template
id: bld_output_template_reasoning_trace
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a reasoning_trace
pattern: every field here exists in the schema; template derives, never invents
quality: 9.1
title: "Output Template Reasoning Trace"
version: "1.0.0"
author: n03_builder
tags: [reasoning_trace, builder, examples]
tldr: "Golden and anti-examples for reasoning trace construction, demonstrating ideal structure and common pitfalls."
domain: "reasoning trace construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_reasoning_trace
  - p03_ins_reasoning_trace_builder
  - bld_schema_reasoning_trace
  - bld_examples_reasoning_trace
  - bld_config_reasoning_trace
  - p03_sp_reasoning_trace_builder
  - p03_rt_n03_builder_agent_20260406
  - p11_qg_reasoning_trace
  - p01_kc_reasoning_trace
  - bld_collaboration_reasoning_trace
---

# Output Template: reasoning_trace
Naming pattern: `p03_rt_{agent}_{timestamp}.yaml`
Filename: `p03_rt_{{agent}}_{{timestamp}}.yaml`
```yaml
---
id: p03_rt_{{agent}}_{{timestamp}}
kind: reasoning_trace
pillar: P03
agent: "{{agent_slug}}"
intent: "{{decision_question_or_goal}}"
timestamp: "{{ISO_8601_timestamp}}"
quality: null
tags: [reasoning_trace, {{domain_tag}}, P03]
---

agent: "{{agent_slug}}"
intent: "{{decision_question_or_goal}}"
steps:
  - step: 1
    thought: "{{what_the_agent_considered_first}}"
    evidence: "{{concrete_data_metric_or_file_reference}}"
    confidence: {{0.0_to_1.0}}
  - step: 2
    thought: "{{what_the_agent_considered_second}}"
    evidence: "{{concrete_data_metric_or_file_reference}}"
    confidence: {{0.0_to_1.0}}
  - step: 3
    thought: "{{what_the_agent_considered_third_or_omit}}"
    evidence: "{{concrete_data_metric_or_file_reference_or_omit}}"
    confidence: {{0.0_to_1.0_or_omit}}
conclusion: "{{final_decision_summary_referencing_strongest_evidence}}"
alternatives_rejected:
  - alternative: "{{rejected_option_description}}"
    reason: "{{evidence_based_rejection_reason}}"
confidence: {{geometric_mean_of_step_confidences}}
timestamp: "{{ISO_8601_timestamp}}"
duration_ms: {{integer_milliseconds_or_omit}}
context: "{{additional_context_or_omit}}"
trigger: "{{instruction_id_or_user_request_or_omit}}"
```
## Derivation Notes
1. The first six body fields (agent, intent, steps, conclusion, confidence, timestamp) are required
2. `alternatives_rejected` is strongly recommended but technically optional
3. `duration_ms`, `context`, and `trigger` are optional extensions
4. Omit absent optional fields instead of filling with placeholder strings
5. Each step MUST have thought + evidence + confidence — never skip evidence
6. Overall confidence is geometric mean: `(c1 * c2 * ... * cn) ^ (1/n)`
7. Keep the trace focused: no instructions, no tool calls, no workflow steps

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | reasoning trace construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_reasoning_trace]] | upstream | 0.56 |
| [[p03_ins_reasoning_trace_builder]] | upstream | 0.55 |
| [[bld_schema_reasoning_trace]] | downstream | 0.52 |
| [[bld_examples_reasoning_trace]] | downstream | 0.51 |
| [[bld_config_reasoning_trace]] | downstream | 0.49 |
| [[p03_sp_reasoning_trace_builder]] | upstream | 0.48 |
| [[p03_rt_n03_builder_agent_20260406]] | upstream | 0.41 |
| [[p11_qg_reasoning_trace]] | downstream | 0.41 |
| [[p01_kc_reasoning_trace]] | upstream | 0.40 |
| [[bld_collaboration_reasoning_trace]] | upstream | 0.40 |
