---
kind: instruction
id: bld_instruction_rbac_policy
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for rbac_policy
quality: 8.8
title: "Instruction Rbac Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [rbac_policy, builder, instruction]
tldr: "Step-by-step production process for rbac_policy"
domain: "rbac_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - kc_rbac_policy
  - p10_mem_rbac_policy_builder
  - rbac-policy-builder
  - bld_knowledge_card_rbac_policy
  - p03_sp_rbac_policy_builder
  - p09_qg_rbac_policy
  - bld_instruction_playground_config
  - p03_ins_permission
  - bld_instruction_safety_policy
  - bld_instruction_judge_config
---

## Phase 1: RESEARCH  
1. Identify tenant domains and their unique resource hierarchies.  
2. Map roles to tenant-specific operations (e.g., admin, viewer).  
3. Define access constraints per role (e.g., read-only, write-only).  
4. Audit existing policies for conflicts or overlaps.  
5. Consult compliance requirements (e.g., GDPR, SOC2).  
6. Document stakeholder approval workflows for policy changes.  

## Phase 2: COMPOSE  
1. Use bld_schema_rbac_policy.md to structure policy JSON with `role`, `resource`, `action`, `tenant`.  
2. Define base roles (e.g., `tenant_admin`, `service_user`).  
3. Assign permissions via `allow`/`deny` rules per resource type.  
4. Scope policies to tenant identifiers (e.g., `tenant_id: "abc123"`).  
5. Reference bld_output_template_rbac_policy.md for required fields: `policy_id`, `version`, `created_by`.  
6. Embed multi-tenant isolation rules using `tenant_scope` enum.  
7. Validate against bld_schema_rbac_policy.md using JSON schema validator.  
8. Write policy in YAML format with `---` separators.  
9. Add comments for audit trails and change logs.  

## Phase 3: VALIDATE  
- [ ] ✅ Check syntax using `yamllint` and JSON schema.  
- [ ] ✅ Test policy enforcement with mock tenant data.  
- [ ] ✅ Confirm isolation: no cross-tenant access leaks.  
- [ ] ✅ Verify compliance with Pillar P09 constraints.  
- [ ] ✅ Obtain stakeholder sign-off on final artifact.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_rbac_policy]] | upstream | 0.44 |
| [[p10_mem_rbac_policy_builder]] | downstream | 0.43 |
| [[rbac-policy-builder]] | downstream | 0.40 |
| [[bld_knowledge_card_rbac_policy]] | upstream | 0.38 |
| [[p03_sp_rbac_policy_builder]] | related | 0.37 |
| [[p09_qg_rbac_policy]] | downstream | 0.34 |
| [[bld_instruction_playground_config]] | sibling | 0.31 |
| [[p03_ins_permission]] | sibling | 0.29 |
| [[bld_instruction_safety_policy]] | sibling | 0.28 |
| [[bld_instruction_judge_config]] | sibling | 0.22 |
