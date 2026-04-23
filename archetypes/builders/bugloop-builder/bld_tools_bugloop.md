---
kind: tools
id: bld_tools_bugloop
pillar: P04
llm_function: CALL
purpose: Tools available for bugloop production
quality: 9.1
title: "Tools Bugloop"
version: "1.0.0"
author: n03_builder
tags: [bugloop, builder, examples]
tldr: "Golden and anti-examples for bugloop construction, demonstrating ideal structure and common pitfalls."
domain: "bugloop construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_quality_gate
  - bld_tools_agent
  - bld_tools_memory_scope
  - bld_tools_mcp_server
  - bld_tools_optimizer
  - bld_tools_retriever_config
  - bld_tools_cli_tool
  - bld_tools_prompt_version
  - bld_tools_instruction
  - bld_tools_boot_config
---

# Tools: bugloop-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing bugloops in P11_feedback/examples/ | Phase 1 (check duplicates, find patterns) | CONDITIONAL |
| brain_query [MCP] | Find validators (P06) that implement detect.pattern | Phase 1 (cross-ref detection logic) | CONDITIONAL |
| validate_artifact.py | Validate bugloop YAML against SCHEMA.md | Phase 3 | [PLANNED] |
| signal_writer.py | Reference pattern for fix confirmation signals | Design time | CONDITIONAL |
## Reference Artifacts (existing)
| Artifact | File | Domain |
|----------|------|--------|
| KC Pipeline Bugloop | P11_feedback/examples/p11_bl_kc_pipeline.md | KC validation failures |
| API Schema Bugloop | P11_feedback/examples/p11_bl_api_schema.md | API drift detection |
| Embedding Refresh Bugloop | P11_feedback/examples/p11_bl_embedding_refresh.md | Stale vector index |
## Tool Usage Notes
1. brain_query is CONDITIONAL: only available when MCP server is running
2. Without MCP: manually inspect P11_feedback/examples/ for existing bugloops
3. validate_artifact.py is PLANNED: until available, use QUALITY_GATES.md checklist manually
4. signal_writer.py: reference its interface when defining escalation.target="signal_bus"

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Builder Context

This ISO operates within the `bugloop-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Checklist

1. Created via 8F pipeline
2. Scored by cex_score across three layers
3. Compiled by cex_compile for validation
4. Retrieved by cex_retriever for injection
5. Evolved by cex_evolve when quality drops

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_quality_gate]] | sibling | 0.56 |
| [[bld_tools_agent]] | sibling | 0.53 |
| [[bld_tools_memory_scope]] | sibling | 0.43 |
| [[bld_tools_mcp_server]] | sibling | 0.43 |
| [[bld_tools_optimizer]] | sibling | 0.42 |
| [[bld_tools_retriever_config]] | sibling | 0.42 |
| [[bld_tools_cli_tool]] | sibling | 0.42 |
| [[bld_tools_prompt_version]] | sibling | 0.42 |
| [[bld_tools_instruction]] | sibling | 0.41 |
| [[bld_tools_boot_config]] | sibling | 0.40 |
