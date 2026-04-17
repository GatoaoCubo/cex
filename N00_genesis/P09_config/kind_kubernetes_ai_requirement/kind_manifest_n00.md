---
id: n00_kubernetes_ai_requirement_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Kubernetes AI Requirement -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, kubernetes_ai_requirement, p09, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A kubernetes_ai_requirement is a CNCF Kubernetes AI Requirement conformance artifact that declares the compute, memory, and GPU resource requirements for deploying AI agents and model inference workloads on Kubernetes. It enables infrastructure teams to provision correct node pools, set resource limits, and configure GPU scheduling for CEX nucleus deployments.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `kubernetes_ai_requirement` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable requirement name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| workload | string | yes | Name of the AI workload being configured |
| cpu_request | string | yes | CPU request (e.g. "2") |
| cpu_limit | string | yes | CPU limit |
| memory_request | string | yes | Memory request (e.g. "8Gi") |
| memory_limit | string | yes | Memory limit |
| gpu_count | integer | no | Number of GPUs required (0 = CPU only) |
| gpu_type | string | no | GPU model requirement (e.g. nvidia-a100) |
| node_selector | object | no | K8s node label selectors |
| tolerations | list | no | K8s tolerations for GPU node taints |

## When to use
- Deploying CEX nuclei on a Kubernetes cluster for production scale
- Configuring local Ollama model inference pods on GPU nodes
- Specifying resource requirements for CNCF AI Working Group compliance

## Builder
`archetypes/builders/kubernetes_ai_requirement-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind kubernetes_ai_requirement --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: k8s_req_n03_builder
kind: kubernetes_ai_requirement
pillar: P09
nucleus: n05
title: "N03 Builder K8s Resource Requirements"
version: 1.0
quality: null
---
workload: n03-builder
cpu_request: "4"
cpu_limit: "8"
memory_request: "16Gi"
memory_limit: "32Gi"
gpu_count: 1
gpu_type: nvidia-rtx-4090
node_selector:
  workload: ai-gpu
```

## Related kinds
- `quantization_config` (P09) -- model quantization reduces GPU memory requirements
- `sandbox_spec` (P09) -- K8s sandbox specifications for pilot enterprise deployments
- `env_config` (P09) -- environment variables injected into K8s pods
