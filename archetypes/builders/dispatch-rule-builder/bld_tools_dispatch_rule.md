---
kind: tools
id: bld_tools_dispatch_rule
pillar: P04
llm_function: CALL
purpose: Tools and runtime surfaces relevant to dispatch_rule production
quality: 9.1
title: "Tools Dispatch Rule"
version: "1.0.0"
author: n03_builder
tags: [dispatch_rule, builder, examples]
tldr: "Golden and anti-examples for dispatch rule construction, demonstrating ideal structure and common pitfalls."
domain: "dispatch rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_handoff
  - bld_tools_spawn_config
  - bld_tools_signal
  - bld_tools_dag
  - bld_tools_optimizer
  - bld_tools_agent_card
  - bld_tools_memory_scope
  - bld_tools_workflow
  - bld_tools_runtime_rule
  - bld_tools_mcp_server
---

# Tools: dispatch-rule-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| `brain_query` | Find existing dispatch rules for same scope | Phase 1 dedup check | CONDITIONAL [MCP] |
| `brain_query` | Retrieve agent_group routing table context | Phase 1 classification | CONDITIONAL [MCP] |
| `validate_artifact.py` | Generic artifact validator against SCHEMA | Phase 3 | [PLANNED] |
| `dispatch_loader.py` | Load and apply dispatch_rule at runtime | Runtime consumption | CONDITIONAL |
## Runtime Interfaces
| Interface | Path | Use |
|-----------|------|-----|
| P12 schema | `P12_orchestration/_schema.yaml` | naming, machine format, field contracts |
| Routing table | `records/framework/docs/SUBAGENT_CATALOG.md` | agent_group-domain mapping reference |
| orchestrator rules | `.claude/rules/orchestrator_RULES.md` | routing keyword table for validation |
| Dispatch output dir | `cex/P12_orchestration/compiled/` | where produced rules are stored |
| Template | `cex/P12_orchestration/templates/tpl_dispatch_rule.md` | human reference for rule shape |
## brain_query Usage (CONDITIONAL — only when MCP available)
```text
brain_query("dispatch_rule {scope}")        # check for existing rules in scope
brain_query("agent_group routing {domain}")   # get agent_group-domain affinity
brain_query("agent for {task_keywords}")    # confirm correct agent_group target
```
Do NOT call brain_query if MCP is not available in current runtime.
Fall back to KNOWLEDGE.md routing table for agent_group selection.
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation (without validator tool)
Validate manually before output:
- filename matches `p12_dr_{scope}.yaml`
- YAML frontmatter parses without error
- `id` matches `^p12_dr_[a-z][a-z0-9_]+$`
- all 17 required fields present
- `quality: null` (literal)
- `fallback` != `agent_group`
- `model` in allowed enum
- `priority` is integer 1-10
- `confidence_threshold` is float 0.0-1.0
- no status/timestamp/quality_score fields (signal boundary)
- no tasks/scope_fence/commit fields (handoff boundary)
- file <= 3072 bytes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_handoff]] | sibling | 0.42 |
| [[bld_tools_spawn_config]] | sibling | 0.41 |
| [[bld_tools_signal]] | sibling | 0.40 |
| [[bld_tools_dag]] | sibling | 0.40 |
| [[bld_tools_optimizer]] | sibling | 0.39 |
| [[bld_tools_agent_card]] | sibling | 0.39 |
| [[bld_tools_memory_scope]] | sibling | 0.39 |
| [[bld_tools_workflow]] | sibling | 0.39 |
| [[bld_tools_runtime_rule]] | sibling | 0.39 |
| [[bld_tools_mcp_server]] | sibling | 0.38 |
