---
id: bld_knowledge_card_constitutional_rule
kind: knowledge_card
pillar: P11
title: "Constitutional Rule Builder -- Knowledge Card"
version: 1.0.0
quality: null
tags: [builder, constitutional_rule, knowledge]
llm_function: INJECT
---
# Knowledge: constitutional_rule
## Core Concept
Constitutional Rule is an absolute behavioral constraint for an agent.
Differs from guardrail: no bypass, no approver, no audit trail that unlocks it.
Origin: Anthropic Constitutional AI (2022) -- principles that cannot be trained away.
## When to Use
- Agent must NEVER do X under any circumstances (harm, deception, illegal action)
- The prohibition is derived from a fundamental value (not operational policy)
- No legitimate business or operational scenario could justify an exception
- The rule must hold even if the operator instructs otherwise
## When NOT to Use
- There is any legitimate bypass scenario: use guardrail instead
- The constraint is about output quality: use quality_gate
- The constraint is about access control: use permission
- It is a policy document for humans: use safety_policy
## The Bypass Test
Before creating a constitutional_rule, ask:
"Is there ANY scenario -- security hotfix, regulatory requirement, executive override --
where this should be bypassed?"
- YES to any: it is a guardrail, not a constitutional_rule
- NO to all: proceed with constitutional_rule
## CEX Integration
- Pillar: P11 (Feedback)
- Builder: constitutional-rule-builder (13 ISOs)
- core: true (applied to all nuclei, cannot be scoped away)
- Related: guardrail (P11), quality_gate (P11)
- Produced by: N07 (Orchestrator) -- core rules come from orchestrator
- max_bytes: 2048
