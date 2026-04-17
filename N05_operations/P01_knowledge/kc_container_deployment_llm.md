---
id: kc_container_deployment_llm
kind: knowledge_card
title: "Container Deployment for LLM Apps"
version: 1.0.0
quality: 9.0
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
| Practice | Description | Example | Benefit |
|---------|-------------|---------|---------|
| Multi-stage builds | Reduce image size by separating build and runtime stages | `FROM golang:1.20 AS builder` | Smaller production images |
| GPU device plugin | Enable GPU access in containers | `--gpus all` flag | Utilize GPU resources |
| Base image selection | Use optimized base images | `nvidia/cuda:12.1.0` | Pre-installed CUDA libraries |
| Resource limits | Define memory and CPU limits | `resources: { limits: { memory: "4Gi" } }` | Prevent resource starvation |
| Image scanning | Detect vulnerabilities in container images | Trivy or Clair tools | Improve security posture |

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
| Framework | Features | Use Case | Throughput (QPS) | Latency (ms) |
|----------|----------|----------|------------------|--------------|
| vLLM     | High-throughput inference | Production-scale deployments | 100,000+ | 1-5 |
| TGI      | Text generation inference | Chatbots and conversational AI | 50,000 | 5-10 |
| Ollama   | Local model serving | Development and testing | 10,000 | 10-20 |
| TorchServe | Model serving with PyTorch | Research and prototyping | 20,000 | 5-15 |
| HuggingFace Transformers | Easy model deployment | NLP tasks | 30,000 | 8-12 |

## Health Check Implementation
```bash
curl -I http://localhost:8000/health
```
Expected response:
```
HTTP/1.1 200 OK
Content-Type: application/json
{"status": "healthy", "timestamp": "2023-10-05T14:30:00Z"}
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
| Tool | Purpose | Integration | Example Query |
|-----|---------|-------------|---------------|
| Prometheus | Metrics collection | Kubernetes | `container_cpu_usage_seconds_total` |
| Grafana | Visualization | Prometheus | CPU usage dashboard |
| Alertmanager | Incident management | Prometheus | CPU threshold alerts |
| Loki | Log aggregation | Kubernetes | `container_log_line` |
| Tempo | Distributed tracing | OpenTelemetry | Request latency traces |

## Security Considerations
- **GPU-specific security contexts**: Restrict GPU access to authorized containers only
- **Network policies**: Implement Calico or Cilium policies to control container communication
- **Secret management**: Use Kubernetes Secrets or HashiCorp Vault for API key storage
- **Image scanning**: Regularly scan images with Clair or Trivy for vulnerabilities
- **Resource limits**: Set strict limits on CPU, memory, and GPU usage to prevent abuse

## Related Kinds
- **kc_model_serving**: Focuses on deploying models via frameworks like vLLM, TGI, and Ollama
- **kc_kubernetes_ops**: Covers Kubernetes orchestration, including deployments and autoscaling
- **kc_gpu_optimization**: Deals with GPU resource allocation, scheduling, and performance tuning
- **kc_ci_cd_pipeline**: Involves CI/CD processes for containerized applications
- **kc_security_best_practices**: Includes security measures for container environments

## Boundary

Static, versioned distilled knowledge. Not instruction, template, or configuration.