---
kind: tools
id: bld_tools_session_state
pillar: P04
llm_function: CALL
purpose: Tools and runtime surfaces relevant to session_state production
---

# Tools: session-state-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| `brain_query` | Search for existing session states | Phase 1 | CONDITIONAL [MCP] |
| `validate_artifact.py` | Generic artifact validator | Phase 3 | [PLANNED] |
## Runtime Interfaces
| Interface | Path | Use |
|-----------|------|-----|
| P10 schema | `P10_memory/_schema.yaml` | naming, machine format, limits |
| Session template | `P10_memory/templates/tpl_session_state.md` | human reference |
| Compiled output | `P10_memory/compiled/p10_ss_{session}.yaml` | production target |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Until a generic validator exists, validate manually:
- filename matches `p10_ss_{session}.yaml`
- YAML parses
- required fields present
- status in enum
- started_at is ISO 8601
- payload fits `session_state`, not `runtime_state` or `learning_record`
