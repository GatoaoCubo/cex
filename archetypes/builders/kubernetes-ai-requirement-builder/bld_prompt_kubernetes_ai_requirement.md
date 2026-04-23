---
kind: instruction
id: bld_instruction_kubernetes_ai_requirement
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for kubernetes_ai_requirement
quality: 8.9
title: "Instruction Kubernetes AI Requirement"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [kubernetes_ai_requirement, builder, instruction]
tldr: "Step-by-step production process for kubernetes_ai_requirement"
domain: "kubernetes_ai_requirement construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_kubernetes_ai_requirement_builder
  - kubernetes-ai-requirement-builder
  - bld_knowledge_card_kubernetes_ai_requirement
  - p09_qg_kubernetes_ai_requirement
  - bld_examples_kubernetes_ai_requirement
  - bld_schema_kubernetes_ai_requirement
  - bld_tools_kubernetes_ai_requirement
  - p10_lr_kubernetes_ai_requirement_builder
  - bld_output_template_kubernetes_ai_requirement
  - bld_collaboration_kubernetes_ai_requirement
---

## Phase 1: RESEARCH
1. Identify workload class: training (multi-node), inference (disaggregated prefill/decode), fine-tuning (LoRA/QLoRA), or batch.
2. Survey GPU topology requirement: NVLink/NVSwitch pairs, PCIe affinity, NUMA alignment, device count per node.
3. Determine InfiniBand fabric: NDR 400 Gbps, XDR 800 Gbps, GPUDirect RDMA, NCCL all-to-all patterns.
4. Assess MIG partitioning need: fractional GPU profiles (1g.5gb through 7g.40gb) for multi-tenant inference.
5. Evaluate DRA eligibility (K8s 1.32+ GA): ResourceClaim templates, ResourceSlices, device classes.
6. Audit checkpoint durability: CSI driver support, PVC access mode, snapshot cadence, restore RTO/RPO.
7. Cross-reference CNCF KAR v1.35 conformance matrix and Kubernetes AI Conformance Program (Nov 2025) profile.

## Phase 2: COMPOSE
1. Reference SCHEMA.md for required fields (workload_class, gpu_topology, rdma_fabric, mig_profile, dra_claims, checkpoint_pvc).
2. Populate OUTPUT_TEMPLATE.md with workload-specific values drawn from the research phase.
3. Encode GPU topology with NVLink/NVSwitch pair count and NUMA node binding (e.g., `numa: node0`).
4. Declare RDMA fabric with explicit Gbps (e.g., `rdma_bandwidth: 400Gbps`, `gpudirect_rdma: true`).
5. List MIG profiles as enumerated values: `[1g.5gb, 2g.10gb, 3g.20gb, 7g.40gb]`.
6. Author DRA ResourceClaims referencing named device classes (e.g., `deviceClassName: nvidia.com/h100`).
7. Specify checkpoint-PVC block: storage class, access mode (ReadWriteMany), CSI snapshot class, frequency.
8. Add gang-scheduling directives (`schedulingGates`, Kueue ClusterQueue, Volcano PodGroup) for multi-node jobs.
9. Tag with CNCF KAR v1.35 conformance marker for platform auditors.

## Phase 3: VALIDATE
- [x] All required fields present (workload_class, gpu_topology, rdma_fabric, mig_profile, dra_claims, checkpoint_pvc).
- [x] GPU-topology declares NVLink/NVSwitch pairs and NUMA binding consistent with node SKU.
- [x] InfiniBand bandwidth matches fabric installed on target nodes (no over-subscription).
- [x] MIG profile values drawn from NVIDIA valid set for the target GPU generation.
- [x] DRA ResourceClaims reference existing ResourceSlices and device classes on the cluster.
- [x] Checkpoint-PVC snapshot cadence meets RPO target for multi-node training checkpoint resume.
- [x] CNCF KAR v1.35 conformance keys present; Kubernetes AI Conformance Program profile declared.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_kubernetes_ai_requirement_builder]] | related | 0.62 |
| [[kubernetes-ai-requirement-builder]] | downstream | 0.58 |
| [[bld_knowledge_card_kubernetes_ai_requirement]] | upstream | 0.58 |
| [[p09_qg_kubernetes_ai_requirement]] | downstream | 0.50 |
| [[bld_examples_kubernetes_ai_requirement]] | downstream | 0.49 |
| [[bld_schema_kubernetes_ai_requirement]] | downstream | 0.49 |
| [[bld_tools_kubernetes_ai_requirement]] | downstream | 0.48 |
| [[p10_lr_kubernetes_ai_requirement_builder]] | downstream | 0.46 |
| [[bld_output_template_kubernetes_ai_requirement]] | downstream | 0.44 |
| [[bld_collaboration_kubernetes_ai_requirement]] | downstream | 0.44 |
