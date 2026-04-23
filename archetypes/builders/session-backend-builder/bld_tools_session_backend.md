---
kind: tools
id: bld_tools_session_backend
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for session_backend production
quality: 9.0
title: "Tools Session Backend"
version: "1.0.0"
author: n03_builder
tags: [session_backend, builder, examples]
tldr: "Golden and anti-examples for session backend construction, demonstrating ideal structure and common pitfalls."
domain: "session backend construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_memory_scope
  - bld_tools_retriever_config
  - bld_tools_interface
  - bld_tools_cli_tool
  - bld_tools_path_config
  - bld_tools_runtime_rule
  - bld_tools_prompt_version
  - bld_tools_chunk_strategy
  - bld_tools_output_validator
  - bld_tools_handoff_protocol
---

# Tools: session-backend-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing session_backend artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| cex_memory_update.py | Read/write session state — validates backend compatibility | Phase 1 (understand interface) | AVAILABLE |
| cex_coordinator.py | Cross-nucleus session handoffs — validates scoping strategy | Phase 1 (understand coordination) | AVAILABLE |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P10_memory/_schema.yaml | Field definitions, session_backend kind |
| CEX Examples | P10_memory/examples/ | Real session_backend artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P10_session_backend |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, memory layer |
| Runtime dir | .cex/runtime/ | Default file backend location |
| SDK stores | cex_sdk/memory/stores.py | Storage interface implementation |
| Memory update | _tools/cex_memory_update.py | Session state read/write interface |
| Coordinator | _tools/cex_coordinator.py | Cross-nucleus coordination patterns |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, backend enum valid,
path/connection_string present for correct backend type, ttl_hours positive,
no embedded credentials, body <= 4096 bytes, quality == null.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_memory_scope]] | sibling | 0.58 |
| [[bld_tools_retriever_config]] | sibling | 0.56 |
| [[bld_tools_interface]] | sibling | 0.55 |
| [[bld_tools_cli_tool]] | sibling | 0.55 |
| [[bld_tools_path_config]] | sibling | 0.54 |
| [[bld_tools_runtime_rule]] | sibling | 0.54 |
| [[bld_tools_prompt_version]] | sibling | 0.54 |
| [[bld_tools_chunk_strategy]] | sibling | 0.54 |
| [[bld_tools_output_validator]] | sibling | 0.53 |
| [[bld_tools_handoff_protocol]] | sibling | 0.53 |
