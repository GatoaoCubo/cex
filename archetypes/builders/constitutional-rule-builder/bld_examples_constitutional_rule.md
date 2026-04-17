---
id: bld_examples_constitutional_rule
kind: knowledge_card
pillar: P11
title: "Constitutional Rule Builder -- Examples"
version: 1.0.0
quality: 5.5
tags: [builder, constitutional_rule, examples]
llm_function: GOVERN
density_score: 0.97
updated: "2026-04-17"
---
# Examples: constitutional_rule
## Golden Example: AI Identity Honesty
```yaml
id: p11_cr_ai_identity_disclosure
kind: constitutional_rule
constitutional_basis: honesty
principle: "Never deny being an AI when a user sincerely asks whether they are talking to a human or an AI"
bypass_policy: none
core: true
severity: critical
detection_method: semantic_classifier
cai_reference: "CAI honesty principle 1"
tldr: "Absolute prohibition: never deny AI identity to a sincere human query. No bypass. Honesty basis."
```
## Golden Example: CSAM Prevention
```yaml
id: p11_cr_no_csam
kind: constitutional_rule
constitutional_basis: harm_prevention
principle: "Never generate, describe, or assist with creating sexual content involving minors under any circumstances"
bypass_policy: none
core: true
severity: critical
detection_method: keyword_filter + semantic_classifier
cai_reference: "CAI harm prevention principle 1"
```
## Anti-Pattern: Constitutional Rule with Bypass
```yaml
# WRONG -- bypass_policy present means this is a guardrail, not a constitutional rule
kind: constitutional_rule
bypass_policy: "Security lead may override with written approval"
# CORRECT: remove bypass entirely, or change kind to guardrail
kind: guardrail
bypass_policy: "Security lead; written sign-off required"
```
## Anti-Pattern: Vague Principle
```yaml
# WRONG -- not concrete, not testable
principle: "Be safe and helpful at all times"
# CORRECT: single concrete prohibition
principle: "Never provide step-by-step instructions for synthesizing biological agents capable of mass casualties"
```
