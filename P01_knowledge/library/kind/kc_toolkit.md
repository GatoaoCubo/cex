---
id: p01_kc_toolkit
kind: knowledge_card
type: kind
pillar: P04
title: "Toolkit -- Deep Knowledge for toolkit"
version: 1.0.0
created: 2026-04-05
updated: 2026-04-05
author: n07-orchestrator
domain: toolkit
quality: 9.1
tags: [toolkit, p04, CALL, kind-kc, tools]
tldr: "A bundled collection of related tools an agent can CALL -- groups tool definitions into coherent capability packages"
when_to_use: "Packaging multiple tools into a single capability unit for agent assignment"
keywords: [toolkit, tools, bundle, capability, function-calling, MCP]
feeds_kinds: [toolkit]
density_score: null
---

# Toolkit

## Spec
```yaml
kind: toolkit
pillar: P04
llm_function: CALL
max_bytes: 4096
naming: p04_tk_{{name}}.yaml
core: false
```

## Purpose

A toolkit groups related tools into a coherent capability package. Instead of assigning 15 individual tools to an agent, you assign 3 toolkits (e.g., `file_ops`, `git_ops`, `search`). This reduces prompt token overhead and makes capability management declarative.

## Anatomy

| Field | Purpose | Example |
|-------|---------|---------|
| name | Toolkit identifier | `file_operations` |
| tools | List of tool definitions | `[read_file, write_file, list_dir, search]` |
| category | Capability domain | `filesystem`, `git`, `web`, `data` |
| requires_confirmation | Tools that need user OK | `[write_file, delete_file]` |
| denied_for | Nuclei/builders that cannot use this | `[n01, n04]` |

## Key Patterns

1. **Least privilege**: Each nucleus gets only the toolkits it needs
2. **Confirmation tiers**: read-only tools auto-approve, write tools need confirmation, delete tools need double-confirm
3. **MCP mapping**: Each toolkit can expose as an MCP server for cross-process tool sharing
4. **Deny lists over allow lists**: Start with all tools available, deny dangerous ones per context

## CEX Integration

- `cex_sdk/tools/toolkit.py` provides the Toolkit class
- `bld_tools_*.md` ISOs define per-builder tool access
- `cex_skill_loader.py` resolves toolkit membership at runtime
