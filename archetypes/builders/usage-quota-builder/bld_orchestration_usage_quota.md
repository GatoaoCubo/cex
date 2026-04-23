---
kind: collaboration
id: bld_collaboration_usage_quota
pillar: P12
llm_function: COLLABORATE
purpose: How usage_quota-builder works in crews with other builders
quality: 8.9
title: "Collaboration Usage Quota"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_quota, builder, collaboration]
tldr: "How usage_quota-builder works in crews with other builders"
domain: "usage_quota construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_usage_quota_builder
  - usage-quota-builder
  - kc_usage_quota
  - bld_instruction_usage_quota
  - p10_mem_usage_quota_builder
  - bld_knowledge_card_usage_quota
  - bld_examples_usage_quota
  - bld_collaboration_rate_limit_config
  - rate-limit-config-builder
  - bld_collaboration_usage_report
---

## Crew Role  
Defines and enforces usage quotas across services, ensuring compliance with predefined limits and policies.  

## Receives From  
| Builder         | What                  | Format  |  
|-----------------|-----------------------|---------|  
| Quota Policy Validator | Validated quota policies | JSON    |  
| Usage Tracker   | Real-time usage metrics | CSV     |  
| Config Manager  | Configuration updates | YAML    |  

## Produces For  
| Builder         | What                  | Format  |  
|-----------------|-----------------------|---------|  
| Quota Enforcer  | Enforceable quota specs | JSON    |  
| Usage Dashboard | Aggregated quota data | CSV     |  
| Audit Log       | Enforcement records   | JSON    |  

## Boundary  
Does NOT handle rate_limit_config (RPM) or cost_budget (dollars). Rate limits are managed by `Rate Limit Builder`; cost budgets by `Cost Budget Manager`. Does NOT enforce quotas directly—only generates specs for enforcers.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_usage_quota_builder]] | upstream | 0.43 |
| [[usage-quota-builder]] | upstream | 0.42 |
| [[kc_usage_quota]] | upstream | 0.41 |
| [[bld_instruction_usage_quota]] | upstream | 0.40 |
| [[p10_mem_usage_quota_builder]] | upstream | 0.40 |
| [[bld_knowledge_card_usage_quota]] | upstream | 0.39 |
| [[bld_examples_usage_quota]] | upstream | 0.36 |
| [[bld_collaboration_rate_limit_config]] | sibling | 0.35 |
| [[rate-limit-config-builder]] | upstream | 0.28 |
| [[bld_collaboration_usage_report]] | sibling | 0.26 |
