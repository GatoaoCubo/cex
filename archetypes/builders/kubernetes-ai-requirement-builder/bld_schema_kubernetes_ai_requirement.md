---
kind: schema
id: bld_schema_kubernetes_ai_requirement
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for kubernetes_ai_requirement
quality: 9.2
title: "Schema Kubernetes AI Requirement"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [kubernetes_ai_requirement, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for kubernetes_ai_requirement"
domain: "kubernetes_ai_requirement construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field              | Type    | Required | Default | Notes |
|--------------------|---------|----------|---------|-------|
| id                 | string  | yes      |         | Matches ID pattern below |
| kind               | string  | yes      |         | Must be `kubernetes_ai_requirement` |
| pillar             | string  | yes      |         | Must be `P09` |
| title              | string  | yes      |         |       |
| version            | string  | yes      |         |       |
| created            | date    | yes      |         |       |
| updated            | date    | yes      |         |       |
| author             | string  | yes      |         |       |
| domain             | string  | yes      |         |       |
| quality            | null    | yes      | null    | Never self-score; peer review assigns |
| tags               | array   | yes      |         |       |
| tldr               | string  | yes      |         |       |
| workload_class     | string  | yes      |         | training, inference, finetune, batch |
| gpu_topology       | object  | yes      |         | nvlink_pairs, pcie_affinity, numa |
| rdma_fabric        | object  | yes      |         | bandwidth_gbps, gpudirect_rdma |
| kar_version        | string  | yes      | "1.35"  | CNCF KAR spec version |

### Recommended
| Field              | Type    | Notes |
|--------------------|---------|-------|
| mig_profile        | array   | e.g. [1g.5gb, 2g.10gb, 3g.20gb, 7g.40gb] |
| dra_claims         | array   | DRA ResourceClaim references (K8s 1.32+) |
| checkpoint_pvc     | object  | csi_driver, access_mode, snapshot_class, cadence |
| gang_scheduling    | object  | kueue_queue or volcano_podgroup |
| conformance_profile| string  | Kubernetes AI Conformance Program profile id |

## ID Pattern
^p09_kar_[a-z][a-z0-9_]+\.md$

## Body Structure
1. **Workload Class** -- training (multi-node), inference (disaggregated), finetune, batch.
2. **GPU Topology** -- NVLink/NVSwitch pairs, PCIe affinity, NUMA alignment.
3. **InfiniBand Fabric** -- RDMA bandwidth (200/400/800 Gbps), GPUDirect RDMA.
4. **MIG Partitioning** -- enumerated NVIDIA MIG profiles for inference tenancy.
5. **DRA Scheduling** -- ResourceClaims and ResourceSlices (K8s 1.32+ GA).
6. **Checkpoint PVC** -- CSI driver, access mode, snapshot class, cadence.
7. **Multi-Node / Gang Scheduling** -- Kueue ClusterQueue or Volcano PodGroup.
8. **CNCF KAR Conformance** -- v1.35 keys, Kubernetes AI Conformance Program profile.

## Constraints
- All required fields must be present and valid.
- `id` must match the regex pattern exactly (p09_kar_*.md).
- `workload_class` must be one of: training, inference, finetune, batch.
- `rdma_fabric.bandwidth_gbps` must be one of: 200, 400, 800.
- `mig_profile` entries must be drawn from NVIDIA valid set (1g.5gb, 2g.10gb, 3g.20gb, 7g.40gb).
- `dra_claims` must reference existing ResourceClaim templates; requires K8s 1.32+.
- `kar_version` must equal "1.35" or a newer approved CNCF release.
