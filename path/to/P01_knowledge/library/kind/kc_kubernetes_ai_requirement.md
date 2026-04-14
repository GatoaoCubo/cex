---
id: kc_kubernetes_ai_requirement
kind: knowledge_card
title: Kubernetes AI Requirement (KAR) Conformance
version: 1.0.0
quality: null
pillar: P01
---

# Kubernetes AI Requirement (KAR) Conformance

The CNCF Kubernetes AI Requirement (KAR) defines conformance criteria for AI workloads in Kubernetes environments. Key requirements include:

1. **GPU Topology Awareness**  
   Support for GPU device discovery, resource allocation, and topology-aware scheduling across multi-GPU nodes.

2. **InfiniBand Integration**  
   Native support for high-speed interconnects (InfiniBand) to enable low-latency communication in distributed AI training.

3. **Multi-Instance GPU (MIG)**  
   Compatibility with NVIDIA MIG technology for fine-grained GPU resource partitioning across multiple workloads.

4. **Dedicated Resource Allocation (DRA)**  
   Ability to reserve dedicated hardware resources (e.g., GPUs, InfiniBand ports) for AI workloads.

5. **Checkpoint PVCs**  
   Persistent Volume Claim (PVC) support for checkpoint storage, enabling fault tolerance and resumable training.

6. **Multi-Node Training**  
   Native support for distributed training across heterogeneous nodes with synchronized resource management.

This conformance ensures Kubernetes platforms can reliably host complex AI workloads with optimized hardware utilization.
