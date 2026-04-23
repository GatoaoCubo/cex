---
id: bld_rules_bounded_context
kind: guardrail
pillar: P11
llm_function: COLLABORATE
version: 1.0.0
quality: 7.7
tags: [bounded_context, rules, guardrail]
title: "Rules: bounded_context Builder"
author: builder
density_score: 0.99
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p03_sp_context_window_config_builder
  - p03_sp_system-prompt-builder
  - p03_sp_kind_builder
  - p03_sp_prompt_cache_builder
  - p03_sp_model_card_builder
  - p03_sp_few_shot_example_builder
  - p03_sp_multi_modal_config_builder
  - p03_sp_embedding_config_builder
  - p03_sp_collaboration_pattern_builder
  - p03_sp_type-def-builder
---
# Builder Rules: bounded_context
## ALWAYS
- ALWAYS write scope_statement in SEMANTIC terms (domain model, not technical)
- ALWAYS identify team_owner (one team per BC)
- ALWAYS list key aggregates within the BC
- ALWAYS document integration patterns with neighboring contexts
- ALWAYS reference the domain_vocabulary for this BC
- ALWAYS set quality: null

## NEVER
- NEVER define a bounded_context by its technical implementation (service, container, namespace)
- NEVER conflate with component_map (deployment topology)
- NEVER allow a BC to be ownerless (anti-pattern: no team = no governance)
- NEVER model a BC that spans multiple teams without Partnership pattern
- NEVER omit integration patterns with neighboring contexts

## EDGE CASES
| Case | Rule |
|------|------|
| BC too large (> 10 aggregates) | Consider splitting into sub-contexts |
| Two teams share a BC | Use Partnership pattern; plan to split |
| BC model conflicts with upstream | Add ACL; protect your model |
| BC needs to be discoverable by others | Use OHS; publish a stable API |

## Naming Conventions
| Pattern | Example |
|---------|---------|
| bc_{domain_noun} | bc_sales, bc_billing, bc_identity |
| context_name PascalCase | Sales, Billing, CexOrchestration |
| Integration patterns | ACL, OHS, CF, Partnership, PL (abbreviations) |

## Size Budget
max_bytes: 4096 (aggregates + integration + rules = ~3KB typical)
Table format for aggregates and integration patterns required.

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
| [[p03_sp_context_window_config_builder]] | upstream | 0.26 |
| [[p03_sp_system-prompt-builder]] | upstream | 0.23 |
| [[p03_sp_kind_builder]] | upstream | 0.23 |
| [[p03_sp_prompt_cache_builder]] | upstream | 0.21 |
| [[p03_sp_model_card_builder]] | upstream | 0.21 |
| [[p03_sp_few_shot_example_builder]] | upstream | 0.20 |
| [[p03_sp_multi_modal_config_builder]] | upstream | 0.20 |
| [[p03_sp_embedding_config_builder]] | upstream | 0.19 |
| [[p03_sp_collaboration_pattern_builder]] | upstream | 0.19 |
| [[p03_sp_type-def-builder]] | upstream | 0.19 |
