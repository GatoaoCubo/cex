---
id: bld_output_template_constitutional_rule
kind: output_template
pillar: P11
title: "Constitutional Rule Builder -- Output Template"
version: 1.0.0
quality: null
tags: [builder, constitutional_rule, template]
llm_function: PRODUCE
---
# Output Template: constitutional_rule
```yaml
---
id: p11_cr_{slug}
kind: constitutional_rule
pillar: P11
title: "Constitutional Rule: {Name}"
version: 0.1.0
constitutional_basis: "{harm_prevention|honesty|autonomy_preservation|legality}"
principle: "{One concrete prohibition statement -- begins with 'Never' or 'Always'}"
bypass_policy: none
core: true
severity: critical
applies_to: [all_agents]
detection_method: "{semantic_classifier|keyword_filter|regex|llm_judge}"
cai_reference: "{CAI principle number or name, if applicable}"
quality: null
tags: [constitutional_rule, {basis_slug}, P11, core]
tldr: "Absolute prohibition: {principle summary}. No bypass. Constitutional basis: {basis}."
---

## Principle
**{One concrete, testable prohibition}**

## Constitutional Basis
This rule protects **{basis value}** because {why this value is foundational and non-negotiable}.
{One paragraph: why this is absolute, not just preferred behavior}

## Rationale: Why No Exceptions
{2-3 bullet points: specific scenarios that might seem like exceptions and why they are not}
- "{Seemingly legitimate exception}" -- {why this still violates the principle}
- "{Edge case}" -- {why the rule holds even here}

## Violations
**Example 1**: {concrete input/action that breaks this rule}
**Example 2**: {another concrete input/action}

## Detection
Method: {how the system identifies a violation}
Confidence threshold: {what detection score triggers a block}
False positive risk: {expected rate + mitigation}

## Boundary
This is NOT a guardrail: guardrails have a bypass policy with an approver.
This constitutional rule has bypass_policy: none -- no approval process exists.
This is NOT a safety_policy: this artifact is enforced at runtime, not advisory.
```
