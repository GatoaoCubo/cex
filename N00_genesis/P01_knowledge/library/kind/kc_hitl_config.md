---
id: p01_kc_hitl_config
kind: knowledge_card
type: kind
pillar: P11
title: "hitl_config: Human-in-the-Loop Review Configuration"
version: 1.0.0
created: 2026-04-12
updated: 2026-04-12
author: n03_builder
domain: hitl_config
quality: 9.1
tags: [hitl_config, p11, GOVERN, kind-kc]
tldr: "Configures human-in-the-loop review gates -- when to escalate, who reviews, approval flow, timeout behavior"
when_to_use: "Building, reviewing, or reasoning about hitl_config artifacts"
keywords: [hitl, human-review, escalation, approval, confidence-threshold]
feeds_kinds: [hitl_config]
density_score: null
related:
  - bld_knowledge_card_hitl_config
  - hitl-config-builder
  - p03_sp_hitl_config_builder
  - bld_architecture_hitl_config
  - bld_examples_hitl_config
  - bld_instruction_hitl_config
  - p11_qg_hitl_config
  - p10_lr_hitl_config_builder
  - bld_collaboration_hitl_config
  - bld_schema_hitl_config
---

# HITL Config

## Spec
```yaml
kind: hitl_config
pillar: P11
llm_function: GOVERN
max_bytes: 2048
naming: p11_hitl_{{workflow}}.yaml
core: false
```

## What It Is
A hitl_config defines when and how AI-generated outputs are routed to human reviewers for judgment. It specifies confidence thresholds that trigger review, escalation chains (who reviews, in what order), approval flows (accept/reject/edit), timeout behavior, and fallback actions when no human responds. It is NOT a guardrail (P11, which is automated blocking/filtering) nor a quality_gate (P07, which is automated scoring). The hitl_config requires HUMAN judgment -- the system cannot resolve the decision autonomously.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| Anthropic Tool Use | `tool_use` with confirmation step | Agent pauses, presents tool call for user approval |
| LangGraph | `interrupt()` / `human_node` | Graph execution pauses at node, resumes after human input |
| CrewAI | `human_input=True` on Task | Agent asks human before finalizing task output |
| AutoGen | `HumanProxyAgent` | Dedicated agent type that proxies human responses |
| Patronus AI | Guardrail + review queue | Flagged outputs routed to human dashboard |
| Scale AI | `Spear` human review | API for routing AI outputs to trained annotators |
| Labelbox | Model-assisted labeling | Confidence-based routing: auto-accept high, review low |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| review_trigger | condition | confidence < 0.8 | Lower threshold = more reviews but higher quality |
| escalation_chain | list[reviewer] | required | Order matters: L1 (fast) -> L2 (expert) -> L3 (admin) |
| approval_flow | enum(binary/edit/score) | binary | Binary = fast; edit = flexible; score = granular |
| timeout_seconds | int | 3600 | Too short = missed reviews; too long = blocked pipeline |
| fallback_action | enum(reject/accept_with_flag/retry) | reject | Safe default is reject; accept_with_flag for non-critical |
| max_queue_depth | int | 100 | Prevents unbounded review backlog |
| priority_rules | list[condition->priority] | [] | Route high-risk outputs to senior reviewers |
| notification_channel | string | email | Slack/email/webhook for review requests |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Confidence gating | Model outputs confidence scores | Review when P(correct) < 0.8 |
| Domain escalation | Different expertise needed per category | Legal questions -> legal team; medical -> clinical team |
| Batch review | Low urgency, high volume | Queue 50 items, reviewer processes in 1 session |
| Inline approval | High stakes, real-time | Agent pauses mid-execution, human approves tool call |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Review everything | Human becomes bottleneck, defeats automation | Set meaningful confidence threshold, review only edge cases |
| No timeout | Pipeline blocks indefinitely | Always set timeout + fallback_action |
| Single reviewer | Single point of failure, vacation = blocked | Minimum 2 reviewers in escalation chain |
| No feedback loop | Reviews don't improve the model | Log review decisions, use as fine-tuning signal |

## Integration Graph
```
[guardrail (auto-filter)] --> [hitl_config] --> [approved output]
         |                         |
  [confidence score]        [learning_record]
         |                         |
  [model output]            [finetune dataset]
```

## Decision Tree
- IF fully automatable with >99% accuracy THEN guardrail only (skip HITL)
- IF high-risk domain (medical, legal, financial) THEN mandatory HITL regardless of confidence
- IF moderate risk + confidence scoring available THEN confidence-gated HITL
- IF low-risk + high-volume THEN batch review with sampling (review 5%)
- DEFAULT: confidence < 0.8 triggers review, 1h timeout, reject fallback

## Quality Criteria
- GOOD: Trigger condition + escalation chain + timeout + fallback defined
- GREAT: Feedback loop to training data; priority routing; metrics on review latency
- FAIL: No timeout; single reviewer; reviews everything (no threshold)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_hitl_config]] | sibling | 0.63 |
| [[hitl-config-builder]] | related | 0.57 |
| [[p03_sp_hitl_config_builder]] | upstream | 0.48 |
| [[bld_architecture_hitl_config]] | upstream | 0.46 |
| [[bld_examples_hitl_config]] | upstream | 0.43 |
| [[bld_instruction_hitl_config]] | upstream | 0.40 |
| [[p11_qg_hitl_config]] | related | 0.38 |
| [[p10_lr_hitl_config_builder]] | upstream | 0.37 |
| [[bld_collaboration_hitl_config]] | downstream | 0.35 |
| [[bld_schema_hitl_config]] | upstream | 0.34 |
