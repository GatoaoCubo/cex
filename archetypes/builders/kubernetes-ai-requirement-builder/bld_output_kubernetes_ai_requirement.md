---
kind: output_template
id: bld_output_template_kubernetes_ai_requirement
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for kubernetes_ai_requirement production
quality: 9.0
title: "Output Template Kubernetes AI Requirement"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [kubernetes_ai_requirement, builder, output_template]
tldr: "Template with vars for kubernetes_ai_requirement production"
domain: "kubernetes_ai_requirement construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_kubernetes_ai_requirement
  - bld_schema_kubernetes_ai_requirement
  - bld_instruction_kubernetes_ai_requirement
  - bld_knowledge_card_kubernetes_ai_requirement
  - kubernetes-ai-requirement-builder
  - p03_sp_kubernetes_ai_requirement_builder
  - p10_lr_kubernetes_ai_requirement_builder
  - p09_qg_kubernetes_ai_requirement
  - bld_tools_kubernetes_ai_requirement
  - bld_collaboration_kubernetes_ai_requirement
---

```markdown
```yaml
---
id: p09_kar_{{name}}.md
kind: kubernetes_ai_requirement
pillar: P09
kar_version: "1.35"              # CNCF KAR spec version
workload_class: {{workload}}      # training | inference | finetune | batch
conformance_profile: {{profile}}  # Kubernetes AI Conformance Program profile id
quality: null
---
```

## GPU Topology
| Field              | Value                              |
|--------------------|------------------------------------|
| device_model       | {{gpu_model}}                      <!-- e.g., H100-SXM5, B200 -->
| devices_per_node   | {{gpu_count}}                      <!-- e.g., 8 -->
| nvlink_pairs       | {{nvlink_pairs}}                   <!-- NVLink/NVSwitch pair count -->
| pcie_affinity      | {{pcie_affinity}}                  <!-- e.g., same-root-complex -->
| numa_binding       | {{numa}}                           <!-- e.g., node0, node1 -->

## InfiniBand Fabric
```yaml
rdma_fabric:
  bandwidth_gbps: {{bandwidth}}     # 200 | 400 | 800
  gpudirect_rdma: {{gpudirect}}     # true | false
  nccl_all_to_all: {{nccl}}         # true for multi-node training
```

## MIG Partitioning (optional, inference tenancy)
- Profiles: {{mig_profiles}}        <!-- e.g., [1g.5gb, 2g.10gb, 3g.20gb, 7g.40gb] -->

## DRA ResourceClaims (K8s 1.32+ GA)
```yaml
dra_claims:
  - name: {{claim_name}}
    deviceClassName: {{device_class}}   # e.g., nvidia.com/h100
    count: {{device_count}}
```

## Checkpoint PVC
```yaml
checkpoint_pvc:
  csi_driver: {{csi_driver}}        # e.g., csi.vastdata.com
  access_mode: ReadWriteMany
  snapshot_class: {{snap_class}}
  cadence_minutes: {{cadence}}      # e.g., 15
```

## Multi-Node / Gang Scheduling
- [x] Kueue ClusterQueue: {{kueue_queue}}
- [x] OR Volcano PodGroup: {{volcano_pg}}
- [x] CNCF KAR v1.35 conformance declared
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_kubernetes_ai_requirement]] | downstream | 0.60 |
| [[bld_schema_kubernetes_ai_requirement]] | downstream | 0.54 |
| [[bld_instruction_kubernetes_ai_requirement]] | upstream | 0.51 |
| [[bld_knowledge_card_kubernetes_ai_requirement]] | upstream | 0.49 |
| [[kubernetes-ai-requirement-builder]] | related | 0.47 |
| [[p03_sp_kubernetes_ai_requirement_builder]] | upstream | 0.46 |
| [[p10_lr_kubernetes_ai_requirement_builder]] | downstream | 0.43 |
| [[p09_qg_kubernetes_ai_requirement]] | downstream | 0.40 |
| [[bld_tools_kubernetes_ai_requirement]] | upstream | 0.38 |
| [[bld_collaboration_kubernetes_ai_requirement]] | downstream | 0.36 |
