---
kind: instruction
id: bld_instruction_data_residency
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for data_residency
quality: 8.8
title: "Instruction Data Residency"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [data_residency, builder, instruction]
tldr: "Step-by-step production process for data_residency"
domain: "data_residency construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify applicable regulations (GDPR, CCPA, regional laws).  
2. Map data flows across systems and borders.  
3. Assess current infrastructure for data storage locations.  
4. Consult legal teams for compliance requirements.  
5. Evaluate cloud provider residency options.  
6. Document jurisdictional risks and mitigation strategies.  

## Phase 2: COMPOSE  
1. Define artifact scope using bld_schema_data_residency.md (data_residency).  
2. Specify data classification (sensitive, non-sensitive).  
3. Assign residency regions per bld_output_template_data_residency.md.  
4. Configure encryption standards (AES-256, TLS 1.3).  
5. Define access control policies (role-based, geo-fencing).  
6. Implement audit logging for data movement.  
7. Reference legal clauses (data processing agreements).  
8. Align with Pillar P09 CONSTRAIN constraints.  
9. Finalize artifact with versioning and metadata.  

## Phase 3: VALIDATE  
- [ ] [OK] Schema alignment (SCHEMA.md)  
- [ ] [OK] Regional residency rules enforced  
- [ ] [OK] Encryption and access controls verified  
- [ ] [OK] Legal compliance confirmed  
- [ ] [OK] Artifact approved by governance team
