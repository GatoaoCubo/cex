---
id: p12_dr_builder_nucleus
kind: dispatch_rule
pillar: P12
title: Dispatch Rule -- Builder Nucleus
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.1
tags: [dispatch-rule, builder, N03]
tldr: Routes construction tasks to N03 via keyword matching and confidence scoring.
density_score: 0.88
scope: construction
keywords: [build, create, construct, design, scaffold, generate, forge, construir, criar, gerar]
priority: 8
confidence_threshold: 0.70
fallback: clarify
routing_strategy: keyword_match
related:
  - p12_dr_software_project
  - p12_sig_builder_nucleus
  - agent_card_engineering_nucleus
  - p08_ac_builder_nucleus
  - p03_pc_cex_universal
  - p02_agent_creation_nucleus
  - p06_if_builder_nucleus
  - agent_card_n03
  - p12_dr_creation
  - bld_sp_collaboration_software_project
---

# Dispatch Rule: Builder Nucleus

## Routing Keywords

| Keywords | Language | Confidence |
|----------|----------|------------|
| build, create, construct, make | EN | 0.90 |
| design, scaffold, generate, forge | EN | 0.85 |
| artifact, kind, template, component | EN | 0.80 |
| construir, criar, gerar, montar | PT | 0.85 |

## Decision Matrix

| Signal | Route | Conf |
|--------|-------|------|
| create a [kind] | N03 direct | 0.95 |
| build [thing] for [domain] | N03 via Motor | 0.85 |
| scaffold nucleus | N03 nucleus_builder | 0.90 |
| register new kind | N03 kind_register | 0.90 |
| deploy [thing] | NOT N03 -> N05 | 0.00 |
| research [topic] | NOT N03 -> N01 | 0.00 |
| write copy for | NOT N03 -> N02 | 0.00 |

## Fallback

If confidence < 0.70 and no other nucleus matches, route to N03
with clarification. Builder is safest default for ambiguous make intents.

## Quality Metrics

| Metric | Value | Threshold |
|--------|-------|-----------|
| Structural completeness | High | ≥ 8.5 |
| Domain specificity | engineering | Verified |
| Cross-reference density | Adequate | ≥ 3 refs |
| Actionability | Verified | Pass |

### Key Principles

- Route by intent classification, not by filename convention
- Fallback chains ensure graceful degradation on nucleus failure
- Session isolation prevents cross-orchestrator interference
- Signal completion within 30s of task finish or trigger timeout alert

### Usage Reference

```yaml
# dispatch_rule integration
artifact: dispatch_rule_engineering
nucleus: N03
domain: engineering
quality_threshold: 9.0
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_dr_software_project]] | sibling | 0.50 |
| [[p12_sig_builder_nucleus]] | related | 0.38 |
| [[agent_card_engineering_nucleus]] | upstream | 0.36 |
| [[p08_ac_builder_nucleus]] | upstream | 0.36 |
| [[p03_pc_cex_universal]] | upstream | 0.35 |
| [[p02_agent_creation_nucleus]] | upstream | 0.34 |
| [[p06_if_builder_nucleus]] | upstream | 0.33 |
| [[agent_card_n03]] | upstream | 0.31 |
| [[p12_dr_creation]] | sibling | 0.31 |
| [[bld_sp_collaboration_software_project]] | upstream | 0.31 |
