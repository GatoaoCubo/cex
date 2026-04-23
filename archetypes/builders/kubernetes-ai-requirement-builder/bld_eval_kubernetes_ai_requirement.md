---
kind: quality_gate
id: p09_qg_kubernetes_ai_requirement
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for kubernetes_ai_requirement
quality: 9.1
title: "Quality Gate Kubernetes AI Requirement"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [kubernetes_ai_requirement, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for kubernetes_ai_requirement"
domain: "kubernetes_ai_requirement construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_kubernetes_ai_requirement
  - bld_instruction_kubernetes_ai_requirement
  - bld_output_template_kubernetes_ai_requirement
  - kubernetes-ai-requirement-builder
  - bld_knowledge_card_kubernetes_ai_requirement
  - p03_sp_kubernetes_ai_requirement_builder
  - bld_schema_kubernetes_ai_requirement
  - p10_lr_kubernetes_ai_requirement_builder
  - bld_tools_kubernetes_ai_requirement
  - bld_collaboration_kubernetes_ai_requirement
---

## Quality Gate

## Definition
| Metric                              | Threshold | Operator | Scope |
|-------------------------------------|-----------|----------|-------|
| CNCF KAR v1.35 conformance coverage | 100%      | equals   | All declared workload classes |

## HARD Gates
| ID  | Check                                        | Fail Condition |
|-----|----------------------------------------------|----------------|
| H01 | YAML frontmatter valid                       | Invalid YAML syntax or missing fields |
| H02 | ID matches pattern ^p09_kar_[a-z][a-z0-9_]+\.md$ | ID format mismatch |
| H03 | kind field equals 'kubernetes_ai_requirement'| Kind field incorrect or missing |
| H04 | workload_class in {training, inference, finetune, batch} | Invalid or missing workload class |
| H05 | gpu_topology declares NVLink pairs + NUMA    | Missing NVLink/NVSwitch or NUMA binding |
| H06 | rdma_fabric.bandwidth_gbps in {200, 400, 800}| Invalid InfiniBand bandwidth |
| H07 | kar_version >= "1.35" (CNCF)                 | Missing or outdated KAR version |
| H08 | DRA claims reference valid device class (K8s 1.32+) | Unresolved DRA ResourceClaim reference |

## SOFT Scoring
| Dim | Dimension                                                          | Weight | Scoring Guide |
|-----|--------------------------------------------------------------------|--------|---------------|
| D01 | GPU-topology completeness (NVLink pairs, PCIe affinity, NUMA)      | 0.25   | All three declared = 1.0, two = 0.5, one or fewer = 0 |
| D02 | InfiniBand realism (bandwidth matches fabric, GPUDirect RDMA flag) | 0.20   | Both fields correct = 1.0, partial = 0.5, missing = 0 |
| D03 | MIG profile validity (NVIDIA valid set 1g.5gb .. 7g.40gb)          | 0.15   | All entries valid = 1.0, some invalid = 0.5, all invalid = 0 |
| D04 | DRA ResourceClaim resolution (K8s 1.32+ ResourceSlices exist)      | 0.20   | All claims resolvable = 1.0, partial = 0.5, none = 0 |
| D05 | Checkpoint-PVC durability (CSI driver, snapshot class, cadence)    | 0.20   | All three present = 1.0, partial = 0.5, missing = 0 |

## Actions
| Score  | Action                                          |
|--------|-------------------------------------------------|
| GOLDEN | >=9.5 -- Auto-publish to platform registry      |
| PUBLISH| >=8.0 -- Auto-publish after KAR conformance CLI check |
| REVIEW | >=7.0 -- Require platform-engineer review       |
| REJECT | <7.0  -- Reject and flag for topology rewrite   |

## Bypass
| Conditions                               | Approver                     | Audit Trail |
|------------------------------------------|------------------------------|-------------|
| Urgent multi-node training onboarding    | Head of Platform Engineering | CNCF KAR escalation log |

## Examples

## Golden Example -- 64-GPU H100 Training Cluster with InfiniBand NDR + DRA
```markdown
---
id: p09_kar_llama3_70b_pretrain.md
kind: kubernetes_ai_requirement
pillar: P09
kar_version: "1.35"
workload_class: training
conformance_profile: cncf.k8s-ai.v1.35.multi-node-training
quality: null
---

## GPU Topology
- device_model: H100-SXM5
- devices_per_node: 8
- nodes: 8   (total = 64 GPUs)
- nvlink_pairs: 4 per node (NVSwitch fabric)
- pcie_affinity: same-root-complex per GPU pair
- numa_binding: node0..node7 (one NUMA per GPU quad)

## InfiniBand Fabric
rdma_fabric:
  bandwidth_gbps: 400        # NDR
  gpudirect_rdma: true
  nccl_all_to_all: true

## DRA ResourceClaims (K8s 1.32+ GA)
dra_claims:
  - name: h100-claim
    deviceClassName: nvidia.com/h100
    count: 64

## Checkpoint PVC
checkpoint_pvc:
  csi_driver: csi.vastdata.com
  access_mode: ReadWriteMany
  snapshot_class: vast-snap
  cadence_minutes: 15

## Gang Scheduling
kueue_queue: llm-training-q
CNCF KAR v1.35 conformance declared.
```

## Anti-Example 1 -- Plain Kubernetes Deployment (NOT a KAR artifact)
```markdown
---
kind: kubernetes_ai_requirement
title: My Training Deployment
---
apiVersion: apps/v1
kind: Deployment
spec:
  replicas: 8
  template:
    spec:
      containers:
        - name: trainer
          image: pytorch:2.5
          resources:
            limits:
              nvidia.com/gpu: 1
```
## Why it fails:
This is a standard K8s Deployment. It lacks every KAR v1.35 requirement: no GPU-topology (NVLink, NUMA), no InfiniBand bandwidth, no MIG profile, no DRA ResourceClaims, no checkpoint-PVC, no CNCF conformance profile. A KAR artifact declares cluster-capability requirements, not workload pods.

## Anti-Example 2 -- Helm Chart Values (packaging, not conformance)
```markdown
---
kind: kubernetes_ai_requirement
title: vllm-helm-values
---
image:
  repository: vllm/vllm-openai
  tag: v0.6.0
replicaCount: 4
resources:
  limits:
    nvidia.com/gpu: 1
service:
  type: ClusterIP
```
## Why it fails:
This is a Helm chart values file -- application packaging config. It does not declare InfiniBand RDMA bandwidth, MIG profile tenancy, DRA ResourceClaims, checkpoint-PVC durability, or CNCF KAR v1.35 conformance profile. KAR artifacts answer "what must the cluster provide?" -- not "how do I package my app?"

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
