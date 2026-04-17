---
id: bld_architecture_constitutional_rule
kind: knowledge_card
pillar: P11
title: "Constitutional Rule Builder -- Architecture"
version: 1.0.0
quality: 7.0
tags: [builder, constitutional_rule, architecture]
llm_function: CONSTRAIN
density_score: 0.92
updated: "2026-04-17"
---
# Architecture: constitutional_rule
## Pattern Origin
Anthropic Constitutional AI (Bai et al. 2022): a set of principles used to evaluate and revise
model outputs. Extended here: constitutional_rule = runtime-enforced absolute prohibition,
not just an RLHF training signal.
## The Absoluteness Property
A constitutional_rule has ONE property that distinguishes it from all other safety kinds:
bypass_policy: none. No role, no context, no instruction can override it.
This is the architectural guarantee: the rule is not a preference or a default -- it is a hard stop.
## Hierarchy (from softest to hardest)
```
safety_policy     -- document, advisory, no enforcement
    |
guardrail         -- soft constraint, has bypass with approver
    |
constitutional_rule -- hard constraint, bypass_policy: none, core: true
```
## Relationship to Other Kinds
| Kind | Relationship |
|------|-------------|
| guardrail | soft constraint with defined bypass policy (approver + audit trail) |
| quality_gate | governs output quality, not agent behavior |
| permission | controls what users can ACCESS, not what agents can DO |
| safety_policy | advisory document, no runtime enforcement |
## Constitutional Basis Categories
| Basis | Protects | Example Rule |
|-------|---------|-------------|
| harm_prevention | physical, psychological, societal safety | never generate content that facilitates mass violence |
| honesty | no deception, no manipulation | never deny being an AI when directly asked |
| autonomy_preservation | user's right to make own decisions | never use dark patterns to push a specific choice |
| legality | compliance with applicable law | never assist with actions that are illegal in user's jurisdiction |
## Enforcement Model
Constitutional rules are checked before output delivery.
If violation detected: hard block, no partial output, no bypass option.
Detection can be: keyword filter, semantic classifier, regex, LLM judge (depends on rule).
