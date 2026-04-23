---
quality: 7.8
id: bld_rules_constitutional_rule
kind: knowledge_card
pillar: P11
title: "Constitutional Rule Builder -- Rules"
version: 1.0.0
quality: 7.5
tags: [builder, constitutional_rule, rules]
llm_function: COLLABORATE
author: builder
density_score: 0.81
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p03_sp_guardrail_builder
  - p10_lr_guardrail_builder
  - guardrail-builder
  - bld_collaboration_quality_gate
  - bld_collaboration_guardrail
  - bld_architecture_kind
  - bld_architecture_guardrail
  - bld_collaboration_permission
  - p11_qg_guardrail
  - p03_sp_kind_builder
---
# Rules: constitutional_rule
## Absolute Rules (HARD -- never violate)
1. bypass_policy MUST be "none" -- any other value means this is a guardrail, not a constitutional rule.
2. core MUST be true -- constitutional rules apply to all agents and cannot be scoped away.
3. severity MUST be critical -- constitutional rules are always the highest severity.
4. One rule, one prohibition -- never bundle multiple prohibitions in a single artifact.
5. Principle must be concrete and testable -- abstract values ("be helpful") are not rules.
6. quality: null always -- never self-score.
## Soft Rules (RECOMMEND)
1. detection_method should be specified to make enforcement practical.
2. Cite a cai_reference or external ethical framework (EU AI Act, NIST AI RMF) for grounding.
3. Violation examples: 2 minimum, prefer 3 covering different attack surfaces.
4. Rationale should address the most compelling "edge case" argument and rebut it.
## Boundary Rules
1. THIS BUILDER handles: constitutional_rule (P11) -- absolute, no bypass
2. NOT this builder: guardrail (soft, has bypass) -> guardrail-builder
3. NOT this builder: quality_gate (output quality) -> quality-gate-builder
4. NOT this builder: permission (access control) -> permission-builder
5. NOT a kind: safety_policy (document) -- there is no safety-policy-builder in CEX
## The Bypass Test (MANDATORY before building)
"Is there ANY legitimate scenario where this rule should be bypassed?"
- YES: use guardrail-builder instead
- NO: proceed with constitutional-rule-builder
## CEX-Specific Rules
1. id pattern: p11_cr_{slug} -- always prefix p11_cr_
2. Pillar: always P11 (Feedback)
3. Producing nucleus: N07 (Orchestrator) -- core rules come from the orchestrator level
4. max_bytes: 2048
5. Publish threshold: >= 8.0 (higher than standard 7.0 for safety-critical artifacts)

## Orchestration Checklist

- Verify workflow topology matches dependency graph
- Validate handoff protocol between upstream and downstream
- Cross-reference with dispatch rules for routing correctness
- Test wave sequencing with dry-run before live dispatch

## Orchestration Pattern

```yaml
# Workflow validation
topology: verified
handoffs: validated
routing: checked
sequencing: tested
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope orchestration
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_guardrail_builder]] | upstream | 0.34 |
| [[p10_lr_guardrail_builder]] | upstream | 0.32 |
| [[guardrail-builder]] | related | 0.30 |
| [[bld_collaboration_quality_gate]] | related | 0.30 |
| [[bld_collaboration_guardrail]] | downstream | 0.29 |
| [[bld_architecture_kind]] | upstream | 0.28 |
| [[bld_architecture_guardrail]] | upstream | 0.27 |
| [[bld_collaboration_permission]] | upstream | 0.26 |
| [[p11_qg_guardrail]] | related | 0.25 |
| [[p03_sp_kind_builder]] | upstream | 0.25 |
