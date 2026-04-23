---
kind: architecture
id: bld_architecture_hitl_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of hitl_config -- inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Hitl Config"
version: "1.0.0"
author: n03_builder
tags: [hitl_config, builder, architecture, P11]
tldr: "Component map for hitl_config: review_trigger + escalation_chain + approval_flow + timeout/fallback + notification; governance layer P11."
domain: "hitl_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - hitl-config-builder
  - bld_collaboration_hitl_config
  - p03_sp_hitl_config_builder
  - p01_kc_hitl_config
  - p11_qg_hitl_config
  - bld_examples_hitl_config
  - bld_schema_hitl_config
  - bld_knowledge_card_hitl_config
  - bld_output_template_hitl_config
  - bld_instruction_hitl_config
---
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| review_trigger | Evaluable condition that routes output to human (confidence threshold, domain flag, classifier score) | hitl-config-builder | required |
| escalation_chain | Ordered list of reviewer roles: L1 (fast triage) -> L2 (expert) -> L3 (senior/legal) | hitl-config-builder | required |
| approval_flow | How reviewers respond: binary (accept/reject), edit (annotate), score (numeric rating) | hitl-config-builder | required |
| timeout_seconds | Maximum seconds before fallback fires at each escalation level | hitl-config-builder | required |
| fallback_action | Action when chain exhausted or timed out: reject, accept_with_flag, retry | hitl-config-builder | required |
| notification_channel | How reviewers are alerted: email, slack, webhook | hitl-config-builder | required |
| max_queue_depth | Maximum pending reviews before backlog alert fires | hitl-config-builder | recommended |
| priority_rules | Conditions that fast-track outputs to senior reviewers | hitl-config-builder | optional |
| feedback_loop | How review decisions feed back to model training pipeline | hitl-config-builder | optional |
| workflow | Name of the AI process this gate is attached to | hitl-config-builder | required |
## Dependency Graph
```
model_output --> [review_trigger evaluates] --> hitl_config gate
                                                    |
                           [confidence >= threshold]  [confidence < threshold OR domain flag]
                                    |                          |
                              auto-release              review_queue
                                                              |
                                                    [escalation_chain L1]
                                                              |
                                                  [timeout/SLA exceeded]
                                                              |
                                                    [escalation_chain L2]
                                                              |
                                                  [timeout_seconds exceeded]
                                                              |
                                                    [fallback_action fires]
                                                              |
                                          [reject | accept_with_flag | retry]
                                                              |
                                                    [feedback_loop -> learning_record]
```
| From | To | Type | Data |
|------|----|------|------|
| guardrail (P11) | hitl_config | upstream | Outputs that pass automated filter but need human review |
| quality_gate (P11) | hitl_config | upstream | Outputs that score below threshold triggering human escalation |
| hitl_config | learning_record (P11) | downstream | Review decisions as training/improvement signal |
| hitl_config | reward_signal (P11) | downstream | Accept/reject signals for RLHF or quality tracking |
| hitl_config | agent workflow (P12) | consumed_by | Workflow pauses at HITL node, resumes after decision |
| model_provider (P02) | hitl_config | feeds | Model output + confidence scores that trigger review |
## Boundary Table
| hitl_config IS | hitl_config IS NOT |
|---------------|-------------------|
| A configuration of when and how AI outputs are routed to human reviewers | A guardrail (P11) -- guardrail is automated blocking/filtering with no human required |
| Requires human judgment to resolve (automation insufficient or prohibited) | A quality_gate (P11) -- quality_gate is automated numeric scoring with no human |
| Defines escalation chain: ordered roles, SLAs, contact channels | A permission (P09) -- permission governs who can access what, not who reviews outputs |
| Specifies timeout behavior and fallback when reviewers are unavailable | A scoring_rubric (P07) -- scoring_rubric defines quality criteria, not review routing |
| Configures approval_flow: how reviewers interact with the output | A workflow (P12) -- workflow orchestrates steps; hitl_config is a gate within a step |
| Closes the loop: review decisions feed back to model improvement | A benchmark (P07) -- benchmark measures model performance, not human review routing |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Trigger | review_trigger, priority_rules | Determine which outputs enter the human review queue |
| Routing | escalation_chain, notification_channel | Route outputs to the correct human reviewer |
| Response | approval_flow | Define how reviewer judgment is captured |
| Resilience | timeout_seconds, fallback_action, max_queue_depth | Ensure pipeline continues even without reviewer response |
| Learning | feedback_loop | Close the improvement loop by capturing human decisions |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[hitl-config-builder]] | downstream | 0.66 |
| [[bld_collaboration_hitl_config]] | downstream | 0.58 |
| [[p03_sp_hitl_config_builder]] | upstream | 0.58 |
| [[p01_kc_hitl_config]] | downstream | 0.54 |
| [[p11_qg_hitl_config]] | downstream | 0.44 |
| [[bld_examples_hitl_config]] | upstream | 0.43 |
| [[bld_schema_hitl_config]] | upstream | 0.42 |
| [[bld_knowledge_card_hitl_config]] | upstream | 0.42 |
| [[bld_output_template_hitl_config]] | upstream | 0.41 |
| [[bld_instruction_hitl_config]] | upstream | 0.40 |
