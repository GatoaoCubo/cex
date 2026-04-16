---
kind: examples
id: bld_examples_kubernetes_ai_requirement
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of kubernetes_ai_requirement artifacts
quality: 8.9
title: "Examples Kubernetes AI Requirement"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [kubernetes_ai_requirement, builder, examples]
tldr: "Golden and anti-examples of kubernetes_ai_requirement artifacts"
domain: "kubernetes_ai_requirement construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

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
