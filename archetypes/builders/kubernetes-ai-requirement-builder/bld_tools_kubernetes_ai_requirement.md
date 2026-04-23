---
kind: tools
id: bld_tools_kubernetes_ai_requirement
pillar: P04
llm_function: CALL
purpose: Tools available for kubernetes_ai_requirement production
quality: 9.0
title: "Tools Kubernetes AI Requirement"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [kubernetes_ai_requirement, builder, tools]
tldr: "Tools available for kubernetes_ai_requirement production"
domain: "kubernetes_ai_requirement construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_kubernetes_ai_requirement
  - p10_lr_kubernetes_ai_requirement_builder
  - bld_instruction_kubernetes_ai_requirement
  - kubernetes-ai-requirement-builder
  - p03_sp_kubernetes_ai_requirement_builder
  - bld_examples_kubernetes_ai_requirement
  - p09_qg_kubernetes_ai_requirement
  - bld_collaboration_kubernetes_ai_requirement
  - bld_architecture_kubernetes_ai_requirement
  - bld_output_template_kubernetes_ai_requirement
---

## Production Tools
| Tool                | Purpose                                           | When                        |
|---------------------|---------------------------------------------------|-----------------------------|
| kubectl             | Inspect ResourceSlices, device classes (DRA)      | Pre-authoring discovery     |
| cex_compile.py      | Compile KAR .md -> .yaml conformance artifact     | Post-authoring              |
| cex_score.py        | HARD/SOFT gate scoring                            | Validation phase            |
| cex_retriever.py    | Fetch prior KAR templates by workload class       | Research phase              |
| mig-parted          | Inspect/apply NVIDIA MIG profiles on target nodes | Pre-authoring topology scan |
| nvidia-smi topo     | Derive NVLink/NVSwitch pairs, NUMA binding        | Research phase              |
| ibstat / ibnetdiscover | Verify InfiniBand NDR/XDR bandwidth on fabric   | Research phase              |

## Validation Tools
| Tool                   | Purpose                                             | When                      |
|------------------------|-----------------------------------------------------|---------------------------|
| kar-conformance-cli    | CNCF KAR v1.35 conformance check, signed evidence   | Pre-publish gate          |
| dra-check              | Verify ResourceClaims resolve on K8s 1.32+ cluster  | Validation phase          |
| csi-snap-inspect       | Test checkpoint-PVC snapshot class + cadence        | Durability check          |
| kueue-admission-check  | Dry-run gang scheduling admission                   | Multi-node plan verify    |

## External References
- CNCF KAR v1.35 specification (GA Nov 2025)
- Kubernetes AI Conformance Program profile catalog
- NVIDIA MIG valid-profile matrix (H100, B200)
- KEP-4381 (DRA GA in K8s 1.32)
- IBTA InfiniBand Architecture Spec (NDR 400, XDR 800)
- CSI Spec v1.9 (snapshot + cloning APIs)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_kubernetes_ai_requirement]] | upstream | 0.54 |
| [[p10_lr_kubernetes_ai_requirement_builder]] | downstream | 0.51 |
| [[bld_instruction_kubernetes_ai_requirement]] | upstream | 0.47 |
| [[kubernetes-ai-requirement-builder]] | downstream | 0.46 |
| [[p03_sp_kubernetes_ai_requirement_builder]] | upstream | 0.44 |
| [[bld_examples_kubernetes_ai_requirement]] | downstream | 0.43 |
| [[p09_qg_kubernetes_ai_requirement]] | downstream | 0.43 |
| [[bld_collaboration_kubernetes_ai_requirement]] | downstream | 0.40 |
| [[bld_architecture_kubernetes_ai_requirement]] | downstream | 0.39 |
| [[bld_output_template_kubernetes_ai_requirement]] | downstream | 0.32 |
