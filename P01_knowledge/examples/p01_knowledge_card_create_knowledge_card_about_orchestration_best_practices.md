---
id: p01_kc_orchestration_best_practices
kind: knowledge_card
pillar: P01
title: "Container Orchestration Best Practices"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "builder"
domain: orchestration
quality: 8.9
tags: [orchestration, kubernetes, containers, devops, scalability, knowledge]
tldr: "Container orchestration requires resource limits, health checks, rolling updates, and pod disruption budgets for production reliability"
when_to_use: "When deploying containerized applications at scale requiring automated management"
keywords: [orchestration, kubernetes, containers, scaling, deployment]
long_tails:
  - How to configure resource limits for Kubernetes pods
  - Best practices for rolling deployments in container orchestration
  - Container health check patterns for production workloads
axioms:
  - ALWAYS set resource requests and limits on every container
  - NEVER deploy without readiness and liveness probes
  - IF scaling > 10 replicas THEN use horizontal pod autoscaler
linked_artifacts:
  primary: null
  related: []
density_score: 0.87
data_source: "https://kubernetes.io/docs/concepts/configuration/overview/"
---
# Container Orchestration Best Practices

## Quick Reference
```yaml
topic: container_orchestration
scope: Production deployment patterns (Kubernetes, Docker Swarm, ECS)
owner: devops_team
criticality: high
```

## Key Concepts
- **Resource Management**: CPU/memory requests define scheduling; limits prevent overconsumption
- **Health Monitoring**: Liveness probes restart unhealthy pods; readiness probes control traffic routing
- **Update Strategy**: Rolling deployments maintain availability; blue-green eliminates downtime
- **Pod Disruption**: PodDisruptionBudgets ensure minimum replicas during node maintenance
- **Affinity Rules**: Node affinity controls placement; pod anti-affinity spreads replicas

## Strategy Phases
1. **Design**: Define resource requirements, dependencies, and scaling triggers
2. **Deploy**: Apply manifests with probes, limits, and disruption budgets
3. **Monitor**: Track metrics via Prometheus; log aggregation via Fluentd/ELK
4. **Scale**: Horizontal Pod Autoscaler based on CPU/memory/custom metrics
5. **Update**: Rolling deployments with max surge/unavailable parameters

## Golden Rules
- SET requests=limits for guaranteed QoS class on critical workloads
- CONFIGURE readiness probe delay > application startup time
- LIMIT blast radius with namespaces and network policies
- BACKUP persistent volumes before major updates
- MONITOR resource utilization at 70% triggers scaling events

## Flow
```text
[Manifest] -> [Scheduler] -> [Node Selection] -> [Pod Creation]
                |                                     |
           [Resource Check]                    [Health Probes]
                |                                     |
           [Placement Decision]                [Traffic Routing]
```

## Comparativo
| Platform | Orchestrator | Health Checks | Auto-scaling | Networking |
|----------|-------------|---------------|-------------|------------|
| Kubernetes | kube-scheduler | Liveness/Readiness | HPA/VPA | CNI plugins |
| Docker Swarm | Swarm manager | HEALTHCHECK | Global/replicated | Overlay networks |
| ECS | EC2/Fargate | Target group health | Auto Scaling | VPC/ALB |
| Nomad | Nomad scheduler | Health checks | Horizontal scaling | Consul Connect |

## References
- Source: https://kubernetes.io/docs/concepts/configuration/overview/
- Related: https://12factor.net/processes (stateless process patterns)