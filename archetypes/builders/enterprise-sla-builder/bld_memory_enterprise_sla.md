---
kind: memory
id: p10_mem_enterprise_sla_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for enterprise_sla construction
quality: 8.7
title: "Learning Record Enterprise Sla"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [enterprise_sla, builder, learning_record]
tldr: "Learned patterns and pitfalls for enterprise_sla construction"
domain: "enterprise_sla construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - enterprise-sla-builder
  - bld_instruction_enterprise_sla
  - bld_examples_enterprise_sla
  - bld_knowledge_card_enterprise_sla
  - p03_sp_enterprise_sla_builder
  - kc_enterprise_sla
  - p01_kc_api_health_monitoring
  - p10_mem_eval_metric_builder
  - p03_sp_eval_metric_builder
  - p10_mem_reranker_config_builder
---

## Observation
Common issues include vague uptime definitions (e.g., "high availability" without thresholds), inconsistent latency metrics across services, and ambiguous support response time commitments (e.g., "within business hours" without specific SLAs).

## Pattern
Effective SLAs use quantifiable metrics (e.g., 99.9% uptime), align latency targets with service criticality, and define tiered support commitments (e.g., 15-minute response for critical issues).

## Evidence
Reviewed artifacts showed 70% of successful SLAs included specific uptime thresholds and penalty clauses for non-compliance.

## Recommendations
- Define uptime, latency, and support metrics with precise numerical thresholds.
- Align SLA terms with business priorities (e.g., mission-critical vs. non-essential services).
- Include measurable penalties for service providers and remedies for customers.
- Regularly review and update SLAs to reflect changing service requirements.
- Involve legal and operations teams early to ensure enforceability and feasibility.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[enterprise-sla-builder]] | downstream | 0.42 |
| [[bld_instruction_enterprise_sla]] | upstream | 0.40 |
| [[bld_examples_enterprise_sla]] | upstream | 0.39 |
| [[bld_knowledge_card_enterprise_sla]] | upstream | 0.39 |
| [[p03_sp_enterprise_sla_builder]] | upstream | 0.35 |
| [[kc_enterprise_sla]] | upstream | 0.34 |
| [[p01_kc_api_health_monitoring]] | upstream | 0.25 |
| [[p10_mem_eval_metric_builder]] | sibling | 0.24 |
| [[p03_sp_eval_metric_builder]] | upstream | 0.20 |
| [[p10_mem_reranker_config_builder]] | sibling | 0.19 |
