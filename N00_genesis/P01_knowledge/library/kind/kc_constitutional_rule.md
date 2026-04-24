---
quality: 8.2
quality: 7.7
id: kc_constitutional_rule
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n00
domain: kind-taxonomy
tags: [kind, taxonomy, constitutional_rule, cai, safety, P11]
density_score: 0.93
updated: "2026-04-17"
related:
  - bld_architecture_guardrail
  - guardrail-builder
  - p03_sp_guardrail_builder
  - p11_qg_guardrail
  - p10_lr_guardrail_builder
  - bld_instruction_guardrail
  - bld_collaboration_guardrail
  - bld_knowledge_card_guardrail
  - bld_schema_guardrail
  - bld_collaboration_constraint_spec
---
# Knowledge Card: constitutional_rule

## Definition
A `constitutional_rule` is an absolute behavioral constraint for an agent that cannot be
overridden by any instruction, context, or operator configuration. Distinguished from `guardrail`
by a single critical property: `bypass_policy: none`. There is no approver, no override path,
no escalation that unlocks the rule. It is the hardcoded floor of agent behavior.
Pattern origin: Anthropic Constitutional AI (Bai et al. 2022).

## When to Use
- The behavior must be prohibited regardless of who is asking (user, operator, system prompt)
- The prohibition is derived from a fundamental value: harm prevention, honesty, autonomy, or legality
- No legitimate business, security, or operational scenario would justify an exception
- The rule must hold even under adversarial prompt injection or operator override attempts

## When NOT to Use
- There is ANY legitimate bypass scenario (security hotfix, regulatory exemption, operator override): use `guardrail`
- The constraint governs output quality: use `quality_gate`
- The constraint governs what users can access: use `permission`
- It is an advisory document without runtime enforcement: use a policy document (not a CEX kind)
- The constraint has a valid bypass with approval (e.g., security lead sign-off): use `guardrail`

## The Absoluteness Test
Before creating a constitutional_rule, apply the bypass test:
"Is there ANY scenario -- emergency, security research, regulatory compliance, executive order --
where this rule should be bypassed?"
- YES to any: it is a guardrail, not a constitutional_rule
- NO to all: constitutional_rule is appropriate

## Structure
Every `constitutional_rule` defines:
1. **Principle**: one concrete, testable prohibition (never compound prohibitions)
2. **Constitutional basis**: harm_prevention | honesty | autonomy_preservation | legality
3. **Rationale**: why this rule has zero exceptions (address the most compelling edge case)
4. **Violations**: >= 2 concrete examples of what breaking this rule looks like
5. **Detection**: how a violation is identified (keyword filter, semantic classifier, regex, LLM judge)
6. **Boundary**: explicit statement that this is not a guardrail (no bypass) and not advisory

## Constitutional Basis Categories
| Basis | Core Value | Protects Against |
|-------|-----------|-----------------|
| harm_prevention | physical/psychological safety | violence, CSAM, CBRN weapons assistance |
| honesty | no deception | AI identity denial, deliberate misinformation |
| autonomy_preservation | user right to decide | manipulation, dark patterns, coercion |
| legality | compliance with law | direct assistance with illegal actions |

## Hierarchy of Safety Kinds
```
safety_policy (advisory document, no enforcement)
    |
guardrail (soft constraint, has bypass_policy with approver)
    |
constitutional_rule (hard constraint, bypass_policy: none, core: true)
```

## Use Cases
1. **AI identity disclosure**: "Never deny being an AI when a user sincerely asks if they are talking to a human" (honesty basis)
2. **CSAM prohibition**: "Never generate, describe, or assist with creating sexual content involving minors" (harm_prevention basis)
3. **Mass casualty assistance**: "Never provide step-by-step instructions for synthesizing biological, chemical, nuclear, or radiological weapons" (harm_prevention basis)

## Relationships to Other Kinds
| Kind | Relationship |
|------|-------------|
| `guardrail` | soft safety constraint with a defined bypass policy and approver |
| `quality_gate` | governs output quality thresholds, not agent behavioral prohibitions |
| `permission` | governs user access to capabilities, not agent hard-stop behavior |

## Anti-Patterns
- **Constitutional rule with any bypass**: if you write a bypass condition, you created a guardrail
- **Compound prohibition**: "never X and never Y" should be two separate constitutional rules
- **Abstract principle**: "be helpful and harmless" is not a constitutional rule -- it is a value
- **Missing detection**: a rule without a detection method is unenforceable at runtime

## CEX Metadata
| Property | Value |
|----------|-------|
| Pillar | P11 (Feedback) |
| ID pattern | `p11_cr_{slug}` |
| max_bytes | 2048 |
| llm_function | CONSTRAIN |
| core | true (applies to all agents, cannot be scoped) |
| Builder | constitutional-rule-builder (13 ISOs) |
| Nucleus | N07 (Orchestrator) -- core rules set at orchestrator level |
| Publish threshold | >= 8.0 (higher than standard due to safety criticality) |
| Pattern source | Bai et al. Constitutional AI (2022), Anthropic Usage Policy |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_guardrail]] | downstream | 0.33 |
| [[guardrail-builder]] | downstream | 0.33 |
| [[p03_sp_guardrail_builder]] | downstream | 0.33 |
| [[p11_qg_guardrail]] | downstream | 0.30 |
| [[p10_lr_guardrail_builder]] | downstream | 0.29 |
| [[bld_instruction_guardrail]] | downstream | 0.29 |
| [[bld_collaboration_guardrail]] | downstream | 0.26 |
| [[bld_knowledge_card_guardrail]] | sibling | 0.23 |
| [[bld_schema_guardrail]] | downstream | 0.21 |
| [[bld_collaboration_constraint_spec]] | downstream | 0.21 |
