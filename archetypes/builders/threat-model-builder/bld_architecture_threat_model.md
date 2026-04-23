---
kind: architecture
id: bld_architecture_threat_model
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of threat_model -- inventory, dependencies
quality: 9.0
title: "Architecture Threat Model"
version: "1.1.0"
author: n05_ops
tags: [threat_model, builder, architecture]
tldr: "Component map of threat_model -- inventory, dependencies"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_collaboration_threat_model
  - bld_architecture_compliance_framework
  - threat-model-builder
  - p10_lr_threat_model_builder
  - p03_sp_threat_model_builder
  - p11_qg_threat_model
  - bld_tools_threat_model
  - bld_config_threat_model
  - bld_knowledge_card_threat_model
  - bld_examples_threat_model
---

## Component Inventory  

This ISO records a threat model: the assets worth protecting and the attacker profiles that target them.
| Name              | Role                      | Owner         | Status    |  
|-------------------|---------------------------|---------------|-----------|  
| Threat Database   | Stores threat data        | Security Team | Production|  
| Model Validator   | Validates threat models   | Dev Team      | Testing   |  
| User Interface    | Frontend for model input  | UX Team       | Development |  
| Rule Engine       | Applies validation rules  | Dev Team      | Production|  
| Compliance Checker| Ensures regulatory checks | Legal Team    | Testing   |  
| API Gateway       | Manages external requests | Infrastructure| Production|  
| Audit Logger      | Logs all model changes    | Security Team | Production|  

## Dependencies  
| From              | To                | Type   |  
|-------------------|-------------------|--------|  
| User Interface    | API Gateway       | API    |  
| API Gateway       | Threat Database   | Data   |  
| Model Validator   | Rule Engine       | API    |  
| Compliance Checker| Threat Database   | Data   |  
| Audit Logger      | Threat Database   | Data   |  
| User Interface    | Model Validator   | API    |  

## Architectural Position  
The threat_model-builder sits within the CEX P11 Feedback pillar as the pre-deployment risk analysis module. It feeds into downstream builders: compliance_framework (regulatory gap mapping), guardrail (runtime controls), and red_team_eval (adversarial validation). Outputs are structured STRIDE documents consumed by security architects and compliance officers. It does NOT perform runtime monitoring (trace_config) or auto-remediation (bugloop).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_threat_model]] | downstream | 0.45 |
| [[bld_architecture_compliance_framework]] | sibling | 0.37 |
| [[threat-model-builder]] | downstream | 0.33 |
| [[p10_lr_threat_model_builder]] | downstream | 0.32 |
| [[p03_sp_threat_model_builder]] | upstream | 0.30 |
| [[p11_qg_threat_model]] | downstream | 0.30 |
| [[bld_tools_threat_model]] | upstream | 0.30 |
| [[bld_config_threat_model]] | downstream | 0.29 |
| [[bld_knowledge_card_threat_model]] | upstream | 0.28 |
| [[bld_examples_threat_model]] | upstream | 0.27 |
