---
kind: instruction
id: bld_instruction_usage_quota
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for usage_quota
quality: 8.9
title: "Instruction Usage Quota"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_quota, builder, instruction]
tldr: "Step-by-step production process for usage_quota"
domain: "usage_quota construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Analyze system usage patterns to identify peak load periods.  
2. Define rate limits for API endpoints based on service-level agreements.  
3. Determine quota metrics (e.g., requests per user, data transfer limits).  
4. Study fair-use policies to align enforcement with legal and business rules.  
5. Audit historical usage data for anomalies or abuse trends.  
6. Consult stakeholders to prioritize quota enforcement for critical services.  

## Phase 2: COMPOSE  
1. Reference bld_schema_usage_quota.md to define `usage_quota` fields (e.g., `quota_limit`, `reset_interval`).  
2. Set initial quota thresholds using P09 guidelines for resource allocation.  
3. Map metrics to monitored resources (e.g., CPU, memory, API calls).  
4. Write enforcement logic for exceeding thresholds (e.g., rate limiting, blocking).  
5. Implement fair-use exceptions for legitimate high-usage scenarios.  
6. Use bld_output_template_usage_quota.md to structure quota configuration files (YAML/JSON).  
7. Integrate with monitoring tools for real-time quota tracking.  
8. Document enforcement rules in a policy repository.  
9. Test artifact against sample workloads to ensure constraint accuracy.  

## Phase 3: VALIDATE  
- [ ] ✅ Validate schema compliance with SCHEMA.md  
- [ ] ✅ Test quota thresholds against edge cases (e.g., zero, max limits)  
- [ ] ✅ Verify fair-use exceptions trigger correctly  
- [ ] ✅ Confirm integration with monitoring tools logs quota events  
- [ ] ✅ Ensure artifact enforces constraints without service disruption
