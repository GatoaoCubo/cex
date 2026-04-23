---
kind: collaboration
id: bld_collaboration_enterprise_sla
pillar: P12
llm_function: COLLABORATE
purpose: How enterprise_sla-builder works in crews with other builders
quality: 8.9
title: "Collaboration Enterprise Sla"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [enterprise_sla, builder, collaboration]
tldr: "How enterprise_sla-builder works in crews with other builders"
domain: "enterprise_sla construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - enterprise-sla-builder
  - p03_sp_enterprise_sla_builder
  - bld_collaboration_compliance_framework
  - bld_tools_enterprise_sla
  - bld_collaboration_compliance_checklist
  - bld_collaboration_healthcare_vertical
  - bld_knowledge_card_enterprise_sla
  - bld_collaboration_action_paradigm
  - bld_instruction_enterprise_sla
  - bld_collaboration_legal_vertical
---

## Crew Role  
Coordinates SLA contract creation, aligns service expectations, and ensures legal/operational alignment.  

## Receives From  
| Builder         | What                  | Format   |  
|-----------------|-----------------------|----------|  
| service_catalog | Service definitions   | JSON     |  
| legal_team      | Legal terms           | YAML     |  
| operations_team | Performance benchmarks| CSV      |  

## Produces For  
| Builder         | What                  | Format   |  
|-----------------|-----------------------|----------|  
| contract_signing| SLA document          | PDF      |  
| compliance_team | SLA compliance matrix | YAML     |  
| analytics_team  | SLA metrics report    | JSON     |  

## Boundary  
Does NOT enforce runtime quality gates (handled by `runtime_quality_builder`) or audit compliance checklists (handled by `audit_compliance_builder`).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[enterprise-sla-builder]] | upstream | 0.42 |
| [[p03_sp_enterprise_sla_builder]] | upstream | 0.38 |
| [[bld_collaboration_compliance_framework]] | sibling | 0.35 |
| [[bld_tools_enterprise_sla]] | upstream | 0.32 |
| [[bld_collaboration_compliance_checklist]] | sibling | 0.30 |
| [[bld_collaboration_healthcare_vertical]] | sibling | 0.27 |
| [[bld_knowledge_card_enterprise_sla]] | upstream | 0.26 |
| [[bld_collaboration_action_paradigm]] | sibling | 0.24 |
| [[bld_instruction_enterprise_sla]] | upstream | 0.24 |
| [[bld_collaboration_legal_vertical]] | sibling | 0.23 |
