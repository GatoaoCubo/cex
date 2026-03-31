---
kind: tools
id: bld_tools_dispatch_rule
pillar: P04
llm_function: CALL
purpose: Tools and runtime surfaces relevant to dispatch_rule production
---

# Tools: dispatch-rule-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| `brain_query` | Find existing dispatch rules for same scope | Phase 1 dedup check | CONDITIONAL [MCP] |
| `brain_query` | Retrieve agent_node routing table context | Phase 1 classification | CONDITIONAL [MCP] |
| `validate_artifact.py` | Generic artifact validator against SCHEMA | Phase 3 | [PLANNED] |
| `dispatch_loader.py` | Load and apply dispatch_rule at runtime | Runtime consumption | CONDITIONAL |
## Runtime Interfaces
| Interface | Path | Use |
|-----------|------|-----|
| P12 schema | `P12_orchestration/_schema.yaml` | naming, machine format, field contracts |
| Routing table | `records/framework/docs/SUBAGENT_CATALOG.md` | agent_node-domain mapping reference |
| orchestrator rules | `.claude/rules/orchestrator_RULES.md` | routing keyword table for validation |
| Dispatch output dir | `cex/P12_orchestration/compiled/` | where produced rules are stored |
| Template | `cex/P12_orchestration/templates/tpl_dispatch_rule.md` | human reference for rule shape |
## brain_query Usage (CONDITIONAL — only when MCP available)
```text
brain_query("dispatch_rule {scope}")        # check for existing rules in scope
brain_query("agent_node routing {domain}")   # get agent_node-domain affinity
brain_query("agent for {task_keywords}")    # confirm correct agent_node target
```
Do NOT call brain_query if MCP is not available in current runtime.
Fall back to KNOWLEDGE.md routing table for agent_node selection.
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
- `fallback` != `agent_node`
- `model` in allowed enum
- `priority` is integer 1-10
- `confidence_threshold` is float 0.0-1.0
- no status/timestamp/quality_score fields (signal boundary)
- no tasks/scope_fence/commit fields (handoff boundary)
- file <= 3072 bytes
