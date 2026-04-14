---
id: kc_kubernetes_ai_requirement
kind: knowledge_card
title: Kubernetes AI Requirement (KAR) Conformance Artifact
version: 1.0.0
quality: null
pillar: P01
---

# Kubernetes AI Requirement (KAR) Conformance Artifact

The CNCF Kubernetes AI Requirement (KAR) defines conformance criteria for AI workloads in Kubernetes environments. Key requirements include:

1. **GPU Topology Awareness**  
   - Support for GPU device discovery and resource allocation  
   - GPU affinity and NUMA node awareness  

2. **InfiniBand Integration**  
   - RDMA support for high-speed inter-node communication  
   - RoCEv2 protocol compatibility  

3. **Multi-GPU Support**  
   - MIG (Multi-Instance GPU) capability  
   - DRA (Dedicated Resource Allocation) enforcement  

4. **Persistent Storage**  
   - Checkpoint PVCs for model state persistence  
   - Volume lifecycle management for training jobs  

5. **Multi-Node Training**  
   - Distributed training framework compatibility  
   - Network partition tolerance and recovery  

6. **Resource Monitoring**  
   - Real-time GPU utilization tracking  
   - InfiniBand latency monitoring  

This artifact provides a standardized framework for validating Kubernetes distributions' ability to support AI workloads with specific hardware and network requirements.
