---
kind: architecture
id: bld_architecture_bias_audit
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of bias_audit -- inventory, dependencies
quality: 8.9
title: "Architecture Bias Audit"
version: "1.0.0"
author: wave1_builder_gen
tags: [bias_audit, builder, architecture]
tldr: "Component map of bias_audit -- inventory, dependencies"
domain: "bias_audit construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_tools_bias_audit
  - bld_architecture_compliance_framework
  - bld_collaboration_bias_audit
  - bias-audit-builder
  - kc_bias_audit
  - bld_architecture_planning_strategy
  - p03_sp_bias_audit_builder
  - bld_instruction_bias_audit
  - bld_architecture_sandbox_config
  - bld_architecture_collaboration_pattern
---

## Component Inventory

This ISO drives a bias audit: measuring fairness across demographic slices.
| Name | Role | Owner | Status |
|------|------|-------|--------|
| Bias Detector | Identifies biased patterns | Risk Team | In Progress |
| Audit Logger | Records audit trails | Compliance Team | Deployed |
| Data Validator | Ensures input quality | Data Team | Review |
| Rule Engine | Applies fairness rules | Policy Team | In Progress |
| UI Dashboard | Visualizes audit results | UX Team | Blocked |
| Config Manager | Manages audit parameters | DevOps | Deployed |
| Report Generator | Creates bias reports | Analytics Team | In Progress |

## Dependencies
| From | To | Type |
|------|----|------|
| Bias Detector | Data Validator | Data |
| Audit Logger | Report Generator | Control |
| Rule Engine | Bias Detector | Logic |
| Config Manager | Rule Engine | Configuration |
| UI Dashboard | Audit Logger | Visualization |

## Architectural Position
bias_audit sits within CEX’s compliance layer, ensuring algorithmic fairness by auditing trading systems for bias. It integrates with core exchange modules, leveraging data pipelines and policy engines to enforce ethical trading standards across market operations.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_bias_audit]] | upstream | 0.50 |
| [[bld_architecture_compliance_framework]] | sibling | 0.40 |
| [[bld_collaboration_bias_audit]] | downstream | 0.37 |
| [[bias-audit-builder]] | upstream | 0.34 |
| [[kc_bias_audit]] | upstream | 0.32 |
| [[bld_architecture_planning_strategy]] | sibling | 0.31 |
| [[p03_sp_bias_audit_builder]] | upstream | 0.30 |
| [[bld_instruction_bias_audit]] | upstream | 0.28 |
| [[bld_architecture_sandbox_config]] | sibling | 0.28 |
| [[bld_architecture_collaboration_pattern]] | sibling | 0.27 |
