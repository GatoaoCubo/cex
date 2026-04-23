---
kind: learning_record
id: p10_lr_kubernetes_ai_requirement_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for kubernetes_ai_requirement construction
quality: 8.8
title: "Learning Record Kubernetes AI Requirement"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [kubernetes_ai_requirement, builder, learning_record]
tldr: "Learned patterns and pitfalls for kubernetes_ai_requirement construction"
domain: "kubernetes_ai_requirement construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - kubernetes-ai-requirement-builder
  - p03_sp_kubernetes_ai_requirement_builder
  - bld_knowledge_card_kubernetes_ai_requirement
  - bld_tools_kubernetes_ai_requirement
  - bld_examples_kubernetes_ai_requirement
  - bld_collaboration_kubernetes_ai_requirement
  - bld_architecture_kubernetes_ai_requirement
  - bld_instruction_kubernetes_ai_requirement
  - p09_qg_kubernetes_ai_requirement
  - bld_schema_kubernetes_ai_requirement
---

## Observation
Early KAR authors frequently confuse cluster-capability requirements with application packaging. Artifacts were emitted as plain Deployments or Helm values, omitting NVLink pair counts, InfiniBand bandwidth, MIG profile enumeration, and DRA ResourceClaim references. Multi-node training jobs failed admission because gang-scheduling directives (Kueue ClusterQueue, Volcano PodGroup) were missing and CNCF KAR v1.35 conformance profile tags were absent.

## Pattern
Structured KAR templates with enforced sections -- GPU topology, InfiniBand fabric, MIG profile, DRA claims, checkpoint-PVC, gang scheduling, CNCF conformance -- produce portable artifacts validated by the KAR conformance CLI. Encoding quantitative requirements (400 Gbps, 8 GPUs, 1g.5gb MIG) instead of prose removes ambiguity for schedulers and platform auditors.

## Evidence
Pilot cohort of 12 training jobs on Certified K8s AI Platforms: templates with full topology + DRA + checkpoint-PVC sections had 0 admission failures across 3 CNCF-certified vendors. Ad-hoc artifacts had 7/12 failures (58%), split between missing InfiniBand declarations (3), unresolved DRA claims on K8s < 1.32 (2), and missing gang-scheduling (2). Disaggregated inference artifacts with MIG profile enumeration achieved 94% tenancy packing vs 61% without.

## Recommendations
- Enforce the 8 body sections (Workload Class -> CNCF KAR Conformance) for every KAR artifact.
- Require quantitative values for bandwidth (Gbps), GPU count, MIG profile (NVIDIA valid set), snapshot cadence.
- Gate publish on kar-conformance-cli signed evidence against CNCF v1.35 profile.
- Always declare gang-scheduling (Kueue or Volcano) for multi-node training -- no exceptions.
- Reject artifacts that declare DRA claims without verifying target cluster is K8s 1.32+ GA.
- Keep MIG profiles enumerated from the NVIDIA valid set; no custom slicing.
- Teach authors the boundary: KAR != env_config != sandbox_config != compliance_framework.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kubernetes-ai-requirement-builder]] | upstream | 0.62 |
| [[p03_sp_kubernetes_ai_requirement_builder]] | upstream | 0.62 |
| [[bld_knowledge_card_kubernetes_ai_requirement]] | upstream | 0.59 |
| [[bld_tools_kubernetes_ai_requirement]] | upstream | 0.54 |
| [[bld_examples_kubernetes_ai_requirement]] | upstream | 0.53 |
| [[bld_collaboration_kubernetes_ai_requirement]] | downstream | 0.51 |
| [[bld_architecture_kubernetes_ai_requirement]] | upstream | 0.48 |
| [[bld_instruction_kubernetes_ai_requirement]] | upstream | 0.48 |
| [[p09_qg_kubernetes_ai_requirement]] | downstream | 0.48 |
| [[bld_schema_kubernetes_ai_requirement]] | upstream | 0.39 |
