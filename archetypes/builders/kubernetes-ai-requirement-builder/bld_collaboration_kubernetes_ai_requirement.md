---
kind: collaboration
id: bld_collaboration_kubernetes_ai_requirement
pillar: P12
llm_function: COLLABORATE
purpose: How kubernetes_ai_requirement-builder works in crews with other builders
quality: 8.9
title: "Collaboration Kubernetes AI Requirement"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [kubernetes_ai_requirement, builder, collaboration]
tldr: "How kubernetes_ai_requirement-builder works in crews with other builders"
domain: "kubernetes_ai_requirement construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role
Authors CNCF KAR v1.35 conformance artifacts translating ML workload needs (multi-node training, disaggregated inference, LoRA finetune) into declarative cluster-capability requirements: GPU-topology, InfiniBand, MIG, DRA, checkpoint-PVC.

## Receives From
| Builder / Team        | What                              | Format |
|-----------------------|-----------------------------------|--------|
| ML Research           | Workload class + GPU count target | YAML   |
| Platform Engineering  | Node SKU, NVSwitch, NUMA map      | JSON   |
| Storage Team          | CSI driver capabilities, snapshot classes | YAML |
| Network Team          | InfiniBand fabric inventory (NDR/XDR) | YAML |

## Produces For
| Builder / Team              | What                                   | Format |
|-----------------------------|----------------------------------------|--------|
| KAR Conformance CLI         | p09_kar_*.md -> signed evidence bundle | JSON   |
| Kueue / Volcano scheduler   | Gang-scheduling directives             | YAML CRD |
| DRA scheduler (K8s 1.32+)   | ResourceClaim templates                | YAML CRD |
| Platform auditors           | CNCF Kubernetes AI Conformance evidence| Signed JSON |

## Boundary
Does NOT author env_config (runtime env vars -- handled by `env_config-builder`), sandbox_config (execution isolation -- handled by `sandbox_config-builder`), or broad compliance_framework artifacts (handled by `compliance_framework-builder`). Application packaging (Dockerfile, Helm chart) is owned by Platform Engineering. Security-context and RBAC policies are managed by the Security crew.
