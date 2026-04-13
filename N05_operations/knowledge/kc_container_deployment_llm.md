---
id: kc_container_deployment_llm
kind: knowledge_card
title: "Container Deployment for LLM Apps"
version: 1.0.0
quality: 8.8
pillar: P01
language: en
---

# Container Deployment for LLM Applications

## Key Concepts
- **Docker**: Package models and dependencies into portable containers
- **Kubernetes**: Orchestrate containerized workloads at scale
- **GPU Scheduling**: Optimize resource allocation for compute-intensive tasks
- **Model Serving**: Deploy inference pipelines with vLLM, TGI, or Ollama
- **Health Checks**: Monitor service availability and auto-restart failed containers
- **Autoscaling**: Dynamically adjust resources based on workload demand

## Docker Best Practices
- Use multi-stage builds for production containers
- Implement GPU device plugin for CUDA-enabled containers
- Set `--gpus all` in Docker run commands for GPU access
- Use `nvidia/cuda` base images for GPU-accelerated workloads

## Kubernetes Configuration
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: llm-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: llm
  template:
    metadata:
      labels:
        app: llm
    spec:
      containers:
      - name: llm-container
        image: your-llm-image:latest
        resources:
          limits:
            nvidia.com/gpu: 1
```

## Model Serving Options
| Framework | Features | Use Case |
|----------|---------|---------|
| vLLM     | High-throughput inference | Production-scale deployments |
| TGI      | Text generation inference | Chatbots and conversational AI |
| Ollama   | Local model serving | Development and testing |

## Health Check Implementation
```bash
curl -I http://localhost:8000/health
```
Expected response:
```
HTTP/1.1 200 OK
Content-Type: application/json
```

## Autoscaling Setup
```hcl
resource "kubernetes_horizontal_pod_autoscaler" "llm_scaler" {
  metadata {
    name = "llm-autoscaler"
  }
  spec {
    scale_target_ref {
      api_version = "apps/v1"
      kind       = "Deployment"
      name       = "llm-service"
    }
    min_replicas = 1
    max_replicas = 10
    target_cpu_utilization_percentage = 80
  }
}
```

## Monitoring Stack
1. Prometheus for metrics collection
2. Grafana for visualization
3. Alertmanager for incident management
4. Loki for log aggregation
5. Tempo for distributed tracing

## Security Considerations
- Use GPU-specific security contexts
- Implement network policies for container communication
- Enable secret management for API keys
- Use image scanning for vulnerabilities
- Set appropriate resource limits
```

## Boundary

Conhecimento destilado, estatico, versionado. NAO eh instrucao, template, ou configuracao.


## 8F Pipeline Function

Primary function: **INJECT**
