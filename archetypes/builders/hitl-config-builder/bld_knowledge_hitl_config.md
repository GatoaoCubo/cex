---
kind: knowledge_card
id: bld_knowledge_card_hitl_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for hitl_config production -- human-in-the-loop gate specification
sources: LangGraph interrupt(), CrewAI human_input, AutoGen HumanProxyAgent, Anthropic Tool Use confirmation, Labelbox confidence routing
quality: 9.1
title: "Knowledge Card Hitl Config"
version: "1.0.0"
author: n03_builder
tags: [hitl_config, builder, knowledge_card, P11]
tldr: "HITL gate domain knowledge: trigger types, escalation patterns, approval flows, timeout sizing, fallback safety, feedback loop design."
domain: "hitl_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - p01_kc_hitl_config
  - hitl-config-builder
  - p03_sp_hitl_config_builder
  - p10_lr_hitl_config_builder
  - bld_instruction_hitl_config
  - p11_qg_hitl_config
  - bld_examples_hitl_config
  - bld_config_hitl_config
  - bld_architecture_hitl_config
  - bld_output_template_hitl_config
---

# Domain Knowledge: hitl_config
## Executive Summary
A hitl_config specifies when and how AI-generated outputs pause for human judgment before proceeding. It defines the review trigger (what condition routes to human), escalation chain (who reviews in what order), approval flow (how reviewers respond), timeout (how long before fallback fires), and fallback action (what happens with no response). It is NOT a guardrail (automated blocking), NOT a quality_gate (automated scoring). Human judgment is the distinguishing factor.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P11 (Feedback/Governance) |
| llm_function | GOVERN |
| Frontmatter fields | 15+ |
| Quality gates | 10 HARD + 12 SOFT |
| Approval flows | binary / edit / score |
| Fallback actions | reject / accept_with_flag / retry |
| Escalation minimum | 2 reviewer roles |
| Timeout | always > 0 |
## Cross-Framework Map
| Framework | HITL Primitive | Notes |
|-----------|---------------|-------|
| LangGraph | `interrupt()` / `human_node` | Graph pauses at node, resumes after human input |
| CrewAI | `human_input=True` on Task | Agent asks human before finalizing task |
| AutoGen | `HumanProxyAgent` | Dedicated proxy agent for human responses |
| Anthropic | Tool use confirmation step | Agent pauses, presents tool call for user approval |
| Labelbox | Confidence-based routing | Auto-accept high confidence, route low to humans |
| Scale AI | Spear human review API | Routes AI outputs to trained annotators |
## Trigger Types
| Type | Condition Pattern | Best For |
|------|------------------|----------|
| Confidence threshold | confidence < 0.8 | Models that output calibrated probabilities |
| Domain flag | output_domain IN [medical, legal] | High-stakes domain regardless of confidence |
| Classifier score | toxicity_score > 0.7 | Safety-sensitive content categories |
| Output category | output_type = draft_contract | Specific output types always requiring review |
| Composite | confidence < 0.8 OR domain = medical | Combines multiple conditions with OR/AND |
## Approval Flow Types
| Type | Pattern | Best For |
|------|---------|---------|
| binary | accept OR reject, no modification | High-throughput triage, clear pass/fail criteria |
| edit | reviewer modifies output before approving | Content generation where improvement > rejection |
| score | numeric rating (1-5); threshold determines release | Training data collection, gradual quality improvement |
## Escalation Design Principles
- Minimum 2 levels: L1 (fast, generalist) and L2 (expert, slower SLA)
- SLA per level must sum to < timeout_seconds
- L1 SLA: 15-60 min for async workflows; 1-5 min for real-time
- L2 SLA: 60-240 min for async; escalate critical items regardless of SLA
- Exhausted chain maps to fallback_action
## Timeout Sizing Guide
| Workflow Type | Recommended timeout_seconds | Notes |
|--------------|----------------------------|-------|
| Real-time agent | 300 (5 min) | User is waiting; fast fallback required |
| Async content | 3600 (1 hour) | Batch processing; business-hours SLA |
| Low-urgency review | 86400 (24 hours) | Overnight batch; no user waiting |
| Regulatory | 172800 (48 hours) | Compliance workflows; chain SLA matches |
## Fallback Safety Matrix
| Risk Level | Workflow Example | Recommended fallback |
|------------|-----------------|---------------------|
| High | Medical advice, legal contract | reject |
| Medium | Marketing copy, financial summary | accept_with_flag |
| Low | Informational FAQ, product description | accept_with_flag |
| Retriable | Any where model params can vary | retry |
## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Confidence gating | Model outputs calibrated scores | Review when P(correct) < 0.8 |
| Domain escalation | Different expertise per category | Legal -> legal team; medical -> clinical |
| Batch review | Low urgency, high volume | Queue 50 items, reviewer processes in session |
| Inline approval | High stakes, real-time execution | Agent pauses mid-execution, human approves |
## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Review everything | Human bottleneck, defeats automation | Set meaningful confidence threshold |
| No timeout | Pipeline blocks indefinitely | Always set timeout + fallback_action |
| Single reviewer | Vacation = blocked queue | Minimum 2 reviewers in escalation chain |
| Vague trigger | Cannot evaluate at runtime | Use numeric threshold or enum condition |
| fallback: accept | Silent acceptance bypasses audit | Use accept_with_flag or reject |
| No feedback loop | Reviews don't improve the model | Log decisions to learning_record |
## Application
1. Identify trigger: what output property determines review need?
2. Map reviewers: who has domain expertise? Build L1 -> L2 (-> L3 for high-stakes)
3. Choose approval_flow: binary for speed, edit for quality, score for training data
4. Size timeout: real-time (<5min), async (<1hr), compliance (<48hr)
5. Set fallback: reject for high-risk, accept_with_flag for medium-risk
6. Close the loop: log review decisions to reward_signal or learning_record
## References
- LangGraph: Human-in-the-loop (interrupt + resume pattern)
- CrewAI: human_input=True task configuration
- AutoGen: HumanProxyAgent documentation
- Anthropic: Tool use with confirmation step
- Labelbox: Model-assisted labeling + confidence routing

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_hitl_config]] | sibling | 0.60 |
| [[hitl-config-builder]] | downstream | 0.43 |
| [[p03_sp_hitl_config_builder]] | downstream | 0.43 |
| [[p10_lr_hitl_config_builder]] | downstream | 0.42 |
| [[bld_instruction_hitl_config]] | downstream | 0.41 |
| [[p11_qg_hitl_config]] | downstream | 0.38 |
| [[bld_examples_hitl_config]] | downstream | 0.36 |
| [[bld_config_hitl_config]] | downstream | 0.36 |
| [[bld_architecture_hitl_config]] | downstream | 0.33 |
| [[bld_output_template_hitl_config]] | downstream | 0.31 |
