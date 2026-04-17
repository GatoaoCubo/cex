---
kind: instruction
id: bld_instruction_enterprise_sla
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for enterprise_sla
quality: 8.9
title: "Instruction Enterprise Sla"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [enterprise_sla, builder, instruction]
tldr: "Step-by-step production process for enterprise_sla"
domain: "enterprise_sla construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify stakeholder uptime requirements (e.g., 99.99% annual availability).  
2. Analyze industry benchmarks for latency thresholds (e.g., <50ms for critical services).  
3. Review existing support SLAs (response/resolve times, escalation paths).  
4. Assess infrastructure capacity to meet proposed SLA metrics.  
5. Evaluate legal and compliance constraints (data residency, audit requirements).  
6. Document business impact of SLA non-compliance (financial, operational).  

## Phase 2: COMPOSE  
1. Align SLA structure with bld_schema_enterprise_sla.md (sections: scope, metrics, penalties).  
2. Define uptime targets (e.g., 99.95% monthly, with credit tiers).  
3. Specify latency metrics (e.g., P99 <200ms for API endpoints).  
4. Draft support commitments (response time: 15 mins; resolution: 4 hrs).  
5. Outline escalation procedures (Tier 1–3 support roles, contact channels).  
6. Include penalty clauses (service credits, termination thresholds).  
7. Reference bld_output_template_enterprise_sla.md for formatting (tables, definitions).  
8. Add compliance clauses (GDPR, SOC2, etc.) per research phase.  
9. Finalize with stakeholder sign-off and version control.  

## Phase 3: VALIDATE  
[ ] ✅ Verify schema alignment (bld_schema_enterprise_sla.md)  
[ ] ✅ Confirm metric feasibility (infrastructure capacity checks)  
[ ] ✅ Stakeholder alignment (sign-off on targets/penalties)  
[ ] ✅ Legal review (compliance, liability clauses)  
[ ] ✅ Test with sample data (template rendering, edge cases)
