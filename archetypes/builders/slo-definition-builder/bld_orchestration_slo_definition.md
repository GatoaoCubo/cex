---
quality: 8.0
quality: 7.8
id: bld_rules_slo_definition
kind: knowledge_card
pillar: P08
title: "Rules: slo_definition Builder Constraints"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: slo_definition
tags: [rules, slo_definition, P09]
llm_function: COLLABORATE
tldr: "Hard constraints and edge case handling for slo_definition builder."
density_score: null
related:
  - bld_tools_enterprise_sla
  - p11_qg_enterprise_sla
  - p03_sp_enterprise_sla_builder
  - bld_knowledge_card_enterprise_sla
  - bld_norms
  - enterprise-sla-builder
  - p10_lr_few_shot_example_builder
---

# Rules: slo_definition Builder

## Hard Constraints
1. target_percent MUST be < 100.0 and >= 50.0
2. error_budget_minutes MUST be computed: (1 - target/100) * window_days * 1440
3. error_budget_policy MUST be set: block_deploy | alert_only | auto_rollback
4. owner MUST be specified
5. quality MUST be null
6. id MUST match filename stem, pattern `^p09_slo_[a-z][a-z0-9_]+$`

## Edge Cases
| Situation | Resolution |
|-----------|-----------|
| User requests 100% SLO | Reject: explain error budget math; suggest 99.99% max |
| User has multiple SLIs | Create 1 slo_definition per SLI type; link via slo_group (future kind) |
| User conflates SLO with SLA | Teach: SLA >= SLO; write slo_definition; enterprise_sla is separate kind |
| No monitoring system yet | Use placeholder metric query; mark as draft until instrumented |
| Agent-based service (not HTTP) | Use custom SLI: task_success_rate / total_tasks_attempted |
| User asks for SLO on build quality | Redirect: that is quality_gate, not slo_definition |

## Integration Points

| Point | Direction | Protocol |
|-------|-----------|----------|
| F8 COLLABORATE | outbound | signal_writer.write_signal() |
| F3 INJECT | inbound | Receives upstream artifacts via handoff |
| enterprise_sla | upstream | Must exist before slo definition production |
| quality_gate | upstream | Must exist before slo definition production |
| benchmark | upstream | Must exist before slo definition production |

## Dependencies

| Dependency | Required | Purpose |
|-----------|----------|---------|
| enterprise_sla | yes | Upstream artifact for slo definition |
| quality_gate | yes | Upstream artifact for slo definition |
| benchmark | yes | Upstream artifact for slo definition |

## Properties

| Property | Value |
|----------|-------|
| Kind | `orchestration` |
| Pillar | P12 |
| Domain | slo definition construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_enterprise_sla]] | upstream | 0.21 |
| [[p11_qg_enterprise_sla]] | downstream | 0.21 |
| [[p03_sp_enterprise_sla_builder]] | upstream | 0.20 |
| [[bld_knowledge_card_enterprise_sla]] | sibling | 0.20 |
| [[bld_norms]] | related | 0.19 |
| [[enterprise-sla-builder]] | downstream | 0.18 |
| [[p10_lr_few_shot_example_builder]] | downstream | 0.15 |
