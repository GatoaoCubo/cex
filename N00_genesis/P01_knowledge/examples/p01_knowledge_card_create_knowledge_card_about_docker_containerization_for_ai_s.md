---
id: p01_kc_docker_ai_containerization
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Docker Containerization Patterns for AI Services"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder"
domain: ai_infrastructure
quality: 9.1
tags: [docker, containerization, ai-services, gpu, model-serving, inference, knowledge]
tldr: "Docker AI containers require GPU runtime, multi-stage builds for 10-100GB models, shared volumes for weights, and memory limits 2-4x model size"
when_to_use: "When deploying ML models as scalable services with GPU acceleration and resource isolation"
keywords: [docker-ai, nvidia-docker, model-serving, gpu-passthrough, container-inference]
long_tails:
  - How to configure NVIDIA Docker runtime for GPU model inference
  - Multi-stage Docker builds for large language model deployment
  - Memory optimization patterns for containerized AI workloads
axioms:
  - ALWAYS mount model weights as read-only volumes, NEVER embed in image layers
  - ALWAYS set memory limits 2-4x model parameter size to prevent OOM kills
  - IF using GPU, THEN install nvidia-container-runtime on host
linked_artifacts:
  primary: null
  related: [p01_kc_k8s_ai_workloads]
density_score: 0.89
data_source: "https://docs.docker.com/config/containers/resource_constraints/"
related:
  - kc_container_deployment_llm
  - p01_kc_docker_patterns
  - kc_ollama_deployment_guide
  - bld_knowledge_card_model_registry
  - bld_tools_model_provider
  - kc_model_registry
  - bld_sp_architecture_software_project
  - bld_tools_sandbox_config
  - bld_memory_model_provider
  - bld_knowledge_card_code_executor
---
# Docker Containerization Patterns for AI Services

## Quick Reference
```yaml
topic: docker_ai_containerization
scope: AI model deployment with Docker (inference + training)
owner: infrastructure
criticality: high
```

## Key Concepts
- **NVIDIA Runtime**: `--runtime=nvidia` or `--gpus=all` for GPU access in containers
- **Multi-stage Builds**: separate stages for dependencies (8GB) + models (50-100GB)
- **Volume Strategy**: model weights in named volumes, not image layers (faster startup)
- **Memory Allocation**: container limit = model_params * 4 bytes * 2-4x safety margin
- **Base Images**: `nvidia/cuda:11.8-runtime-ubuntu20.04` for inference, `-devel` for training

## Strategy Phases
1. **Base Setup**: install NVIDIA Container Toolkit on host (`nvidia-container-runtime`)
2. **Image Design**: multi-stage Dockerfile with dependency layer + runtime layer
3. **Storage Config**: persistent volumes for models, temp volumes for inference cache
4. **Resource Limits**: memory=model_size*4, CPU cores=inference_workers, GPU count
5. **Orchestration**: health checks, rolling updates, horizontal pod autoscaling

## Golden Rules
- MONTE modelos em volumes read-only (`/models:/models:ro`)
- LIMITE memoria container = tamanho_modelo * 4 * margem_seguranca (2-4x)
- EXPONHA metricas Prometheus na porta 8080 (padrão observabilidade)
- EXECUTE como non-root user (security + compliance)

## Flow
```text
[Model Files] -> [Named Volume] -> [Container Mount] -> [Inference API]
                       |                    |               |
                  [Persistent]     [Read-Only Access]   [HTTP/gRPC]
```

## Comparativo
| Pattern | Image Size | Startup Time | Storage | Use Case |
|---------|-----------|--------------|---------|----------|
| Embedded Model | 50-100GB | 5-10min | Immutable | Single model, slow deploys |
| Volume Mount | 2-5GB | 30-60s | Shared | Multi-model, fast updates |
| Init Container | 5-10GB | 1-2min | Hybrid | K8s, versioned models |
| S3 Download | 2-5GB | 2-5min | Remote | Cloud-native, auto-scaling |

## Docker Compose Example
```yaml
services:
  ai-inference:
    image: myorg/llama-api:v1.2
    runtime: nvidia
    environment:
      NVIDIA_VISIBLE_DEVICES: all
    deploy:
      resources:
        limits:
          memory: 32G
        reservations:
          devices:
            - driver: nvidia
              count: 1
    volumes:
      - models:/app/models:ro
      - cache:/tmp/inference_cache
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

## Multi-stage Dockerfile
```dockerfile
# Stage 1: Dependencies (cached layer)
FROM nvidia/cuda:11.8-runtime-ubuntu20.04 AS deps
RUN apt-get update && apt-get install -y python3-pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Stage 2: Runtime (model weights external)
FROM deps AS runtime
COPY app/ /app/
WORKDIR /app
EXPOSE 8000
USER 1000:1000
CMD ["python3", "serve.py", "--model-path", "/models"]
```

## References
- NVIDIA Container Toolkit: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/
- Docker GPU Support: https://docs.docker.com/config/containers/resource_constraints/#gpu
- Related: p01_kc_k8s_ai_workloads (orchestration patterns)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_container_deployment_llm]] | sibling | 0.35 |
| [[p01_kc_docker_patterns]] | sibling | 0.30 |
| [[kc_ollama_deployment_guide]] | sibling | 0.25 |
| [[bld_knowledge_card_model_registry]] | sibling | 0.23 |
| [[bld_tools_model_provider]] | downstream | 0.18 |
| [[kc_model_registry]] | sibling | 0.18 |
| [[bld_sp_architecture_software_project]] | downstream | 0.18 |
| [[bld_tools_sandbox_config]] | downstream | 0.17 |
| [[bld_memory_model_provider]] | downstream | 0.16 |
| [[bld_knowledge_card_code_executor]] | sibling | 0.16 |
