---
id: p08_cmap_organization_core
kind: component_map
pillar: P08
description: "Component map of organization-core repository"
scope: full_system
version: 1.0.0
created: 2026-03-24
author: edison
quality: 9.0
tags: [component-map, architecture, dependencies]
---

# Component Map: organization-core

## Components
| Component | Path | Depends On | Used By |
|-----------|------|-----------|---------|
| orchestrator orchestrator | boot/stella.cmd | pi runtime, rules | USER |
| Satellite boots | boot/*.cmd | claude CLI, MCP configs | orchestrator |
| Brain MCP | records/core/brain/ | Ollama, FAISS | All agent_nodes |
| Quality Gate | records/core/python/quality_gate.py | git hooks | Pre-commit |
| Spawn Scripts | records/core/powershell/ | PowerShell | orchestrator |
| Signal Writer | records/core/python/signal_writer.py | filesystem | Satellites |
| Agent Store | records/agents/ | Brain index | Satellites |
| Skill Store | records/skills/ | Brain index | Satellites |
| Pool | records/pool/ | Brain index | Knowledge queries |
| WhatsApp Bridge | records/framework/whatsapp/ | Node.js, Groq | orchestrator |
| Handoffs | .claude/handoffs/ | filesystem | orchestrator -> Satellites |
| Signals | .claude/signals/ | filesystem | Satellites -> orchestrator |

## Data Flow
```
USER -> orchestrator -> handoffs/ -> spawn -> SATELLITE -> signals/ -> orchestrator
                                           |
                                    brain_query (MCP)
                                           |
                                    Pool + Agents + Skills
```
