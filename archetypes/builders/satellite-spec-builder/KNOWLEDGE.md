---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for satellite_spec production
sources: [microservices architecture, multi-agent systems, CEX satellite model]
---

# Domain Knowledge: satellite_spec

## Foundational Concept
Satellite specs define autonomous processing units in multi-agent architectures.
Rooted in microservices architecture (bounded contexts, independent deployment),
multi-agent systems (specialized roles, message passing), and the CEX fractal model
where each satellite owns a domain, runs a specific LLM, and communicates via signals.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Microservices (Newman 2015) | Independent services with bounded contexts | satellite = bounded service |
| Multi-Agent Systems (Wooldridge 2009) | Autonomous agents with roles and coordination | satellite = autonomous agent cluster |
| Kubernetes Pod Spec | Container orchestration with resource limits | scaling + monitoring fields |
| AWS Lambda Function Config | Serverless function with timeout, memory, triggers | constraints + dispatch fields |
| Docker Compose Service | Service definition with deps, ports, env | dependencies + boot_sequence |

## Key Patterns
- Each satellite owns ONE domain (no cross-domain responsibilities)
- Model selection matches task complexity (opus for reasoning, sonnet for speed)
- MCP servers are the satellite's external tool interface
- Boot sequence is ORDERED and IDEMPOTENT
- Constraints define BOUNDARIES, not aspirations
- Dispatch keywords are the routing contract with the orchestrator
- Scaling limits prevent resource exhaustion (BSOD at >4 concurrent)
- Monitoring enables autonomous recovery (signal on complete/failure)
- Dependencies are EXPLICIT: no hidden couplings

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| mcps | CEX uses MCP protocol for tool access | K8s sidecar containers |
| dispatch_keywords | Orchestrator routes by keyword matching | API gateway routing rules |
| boot_sequence | Satellite-specific ordered init | Docker entrypoint + healthcheck |
| mcp_config_file | Per-satellite MCP config path | K8s ConfigMap mount |
| runtime | Engine choice (claude, codex) | K8s container runtime |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT satellite_spec |
|------|------------|---------------------------|
| agent (P02) | Individual agent identity with tools | agent is ONE entity INSIDE satellite; satellite_spec is the WHOLE unit |
| boot_config (P02) | Per-provider init config | boot_config is HOW to start; satellite_spec is WHAT to start |
| pattern (P08) | Reusable design pattern | pattern is ABSTRACT; satellite_spec is CONCRETE instance |
| law (P08) | Inviolable operational rule | law CONSTRAINS all satellites; satellite_spec defines ONE |
| spawn_config (P12) | Runtime spawn parameters | spawn_config is HOW to launch; satellite_spec is WHAT is launched |
| dispatch_rule (P12) | Single routing rule | dispatch_rule is ONE route; satellite_spec contains ALL routes for a satellite |

## References
- Newman, Sam. Building Microservices (2015) — Bounded contexts
- Wooldridge, Michael. Introduction to MultiAgent Systems (2009) — Agent architecture
- Kubernetes Pod Specification — Resource limits and health checks
