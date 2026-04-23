---
id: p01_kc_daemon
kind: knowledge_card
type: kind
pillar: P04
title: "Daemon — Deep Knowledge for daemon"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: daemon
quality: 9.1
tags: [daemon, P04, GOVERN, kind-kc]
tldr: "Persistent background process that runs continuously, monitoring events or serving requests without direct agent invocation"
when_to_use: "Building, reviewing, or reasoning about daemon artifacts"
keywords: [background-process, service, persistent-runner]
feeds_kinds: [daemon]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - daemon-builder
  - bld_collaboration_daemon
  - bld_architecture_daemon
  - p03_sp_daemon_builder
  - p04_daemon_{{NAME_SLUG}}
  - p04_daemon_autonomous
  - bld_instruction_daemon
  - bld_knowledge_card_daemon
  - bld_output_template_daemon
  - p11_qg_daemon
---

# Daemon

## Spec
```yaml
kind: daemon
pillar: P04
llm_function: GOVERN
max_bytes: 1024
naming: p04_daemon_{{name}}.md + .yaml
core: false
```

## What It Is
A daemon is a persistent background process that runs continuously — monitoring file changes, polling APIs, serving HTTP requests, or watching for events. It operates independently of any single agent invocation. It is NOT a hook (which fires once on a specific event and terminates) nor a cli_tool (which executes once and exits). A daemon persists in the background and governs ongoing system behavior.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `LangServe` / custom FastAPI server | Persistent server serving LangChain chains via API |
| LlamaIndex | `LlamaDeploy` workflow service | Persistent service running LlamaIndex workflows |
| CrewAI | `CrewAI+` enterprise deployment | Managed persistent crew execution environment |
| DSPy | Custom server wrapping DSPy modules | FastAPI/Flask serving optimized DSPy programs |
| Haystack | Hayhooks / custom pipeline server | Persistent server hosting Haystack pipelines |
| OpenAI | Assistants API (server-managed runs) | OpenAI manages persistent state server-side |
| Anthropic | No native daemon — MCP servers persist | MCP servers are the daemon pattern for Anthropic ecosystem |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| restart_policy | enum | "on-failure" | Always = resilient but masks bugs; never = manual recovery |
| health_check_interval_s | int | 60 | Lower = faster detection but more resource overhead |
| log_level | enum | "info" | Debug = detailed but noisy and expensive storage |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| File watcher | React to filesystem changes | Watch `.claude/signals/` for agent_group completion signals |
| API server | Serve LLM capabilities over HTTP | FastAPI daemon serving RAG pipeline on Railway |
| Poll-and-act | Monitor external state changes | Poll marketplace API every 5min for price changes |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No health check | Silent failure, no one knows daemon is down | Add health_check endpoint and monitoring |
| No graceful shutdown | Data corruption, orphaned resources | Handle SIGTERM, flush buffers, close connections |

## Integration Graph
```
[boot_config] --> [daemon] --> [hook]
                     |
              [api_client, cli_tool]
```

## Decision Tree
- IF process must run continuously THEN daemon
- IF process fires once per event THEN hook instead
- IF process runs once and exits THEN cli_tool instead
- IF serving HTTP API THEN daemon with health check endpoint
- DEFAULT: Daemon with on-failure restart and 60s health check

## Quality Criteria
- GOOD: Restart policy defined, health check configured, log level set
- GREAT: Graceful shutdown, resource cleanup, monitoring integration
- FAIL: No health check; no restart policy; no shutdown handler; >1024 bytes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[daemon-builder]] | related | 0.52 |
| [[bld_collaboration_daemon]] | downstream | 0.47 |
| [[bld_architecture_daemon]] | downstream | 0.45 |
| [[p03_sp_daemon_builder]] | upstream | 0.39 |
| [[p04_daemon_{{NAME_SLUG}}]] | related | 0.38 |
| [[p04_daemon_autonomous]] | related | 0.36 |
| [[bld_instruction_daemon]] | upstream | 0.35 |
| [[bld_knowledge_card_daemon]] | sibling | 0.33 |
| [[bld_output_template_daemon]] | downstream | 0.32 |
| [[p11_qg_daemon]] | downstream | 0.31 |
