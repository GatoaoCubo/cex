---
kind: output_template
id: bld_output_template_reasoning_trace
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a reasoning_trace
pattern: every field here exists in the schema; template derives, never invents
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
- The first six body fields (agent, intent, steps, conclusion, confidence, timestamp) are required
- `alternatives_rejected` is strongly recommended but technically optional
- `duration_ms`, `context`, and `trigger` are optional extensions
- Omit absent optional fields instead of filling with placeholder strings
- Each step MUST have thought + evidence + confidence — never skip evidence
- Overall confidence is geometric mean: `(c1 * c2 * ... * cn) ^ (1/n)`
- Keep the trace focused: no instructions, no tool calls, no workflow steps
