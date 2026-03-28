---
kind: knowledge_card
id: bld_knowledge_card_validator_builder_codex
pillar: P01
llm_function: DISTILL
purpose: Core domain knowledge for producing validator artifacts
pattern: validator = objective technical rule, not numeric governance
---

# Knowledge: validator

## What A Validator Is
`validator` lives in layer `governance` and pillar `P06`.
It is a technical pass/fail rule applied to artifacts, fields, files, or
events. It should be machine-friendly, compact, and enforceable.

## Boundary Map
`validator` IS:
- rule with explicit condition
- check list with deterministic expressions
- error message catalog for failures
- triggerable at pre_commit, post_generate, pre_pool, or on_signal

`validator` IS NOT:
- `quality_gate` from P11: weighted score, publish threshold, bypass policy
- `scoring_rubric` from P07: evaluation criteria with dimensions and weights
- `input_schema` from P06: full input contract
- `grammar` from P06: decoder-time token constraint

## Canonical Seeds
From `SEED_BANK.yaml`: `rule`, `conditions`, `error_message`, `severity`,
`auto_fix`, `pre_commit`, `quality_gate`, `threshold`, `bypass`, `logging`.

## Typical Targets
- filename/id compliance
- field ranges or enum membership
- section presence
- forbidden patterns or paths
- max size / density / threshold checks

## Good Validator Traits
- one rule family per artifact
- conditions readable without prose interpretation
- `action_on_fail` is explicit: reject, warn, or log
- examples show realistic pass and fail cases
