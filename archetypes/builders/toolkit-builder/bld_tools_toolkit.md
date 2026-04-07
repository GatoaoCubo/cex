---
kind: tools
id: bld_tools_toolkit
pillar: P04
llm_function: CALL
purpose: Tools and runtime surfaces relevant to toolkit production
quality: 9.0
title: "Tools Toolkit"
version: "1.0.0"
author: n03_builder
tags: [toolkit, builder, examples]
tldr: "Golden and anti-examples for toolkit construction, demonstrating ideal structure and common pitfalls."
domain: "toolkit construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Tools: toolkit-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| `cex_skill_loader.py` | Loads builder ISOs and toolkit definitions into agent prompts | Toolkit consumption | ACTIVE |
| `cex_router.py` | Validates tool availability before dispatch | Pre-dispatch check | ACTIVE |
| `cex_compile.py` | Compiles .md/.yaml to indexed artifacts | Post-save compilation | ACTIVE |
| `cex_doctor.py` | Builder health check — validates toolkit structure | Validation phase | ACTIVE |
| `cex_agent_spawn.py` | Validates agent config including toolkit references | Agent provisioning | CONDITIONAL |
| `cex_score.py` | Peer review scoring (--apply) | Quality assessment | CONDITIONAL |
## Runtime Interfaces
| Interface | Path | Use |
|-----------|------|-----|
| Toolkit output directory | `P04_tools/compiled/` | write compiled YAML toolkit files |
| P04 schema | `P04_tools/_schema.yaml` | naming, format, limits |
| Toolkit template | `P04_tools/templates/tpl_toolkit.md` | human reference for toolkit structure |
| MCP config | `.cex/config/mcp_servers.yaml` | MCP server endpoints for tool mapping |
| Existing toolkits | `P04_tools/compiled/p04_tk_*.yaml` | check for cross-toolkit duplication |
| Builder tool ISOs | `archetypes/builders/*/bld_tools_*.md` | reference for per-builder tool permissions |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Until a dedicated toolkit validator exists, validate manually:
- filename matches `p04_tk_{name}.yaml`
- YAML parses without errors
- required fields present: name, tools, category, requires_confirmation
- each tool has name, description, confirmation
- confirmation values in allowed enum (auto, confirm, deny)
- no write/delete tool has confirmation = auto
- tool count <= 15
- no implementation code in toolkit
- total size <= 4096 bytes
