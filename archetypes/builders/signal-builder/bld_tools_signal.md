---
kind: tools
id: bld_tools_signal
pillar: P04
llm_function: CALL
purpose: Tools and runtime surfaces relevant to signal production
quality: 9.0
title: "Tools Signal"
version: "1.0.0"
author: n03_builder
tags: [signal, builder, examples]
tldr: "Golden and anti-examples for signal construction, demonstrating ideal structure and common pitfalls."
domain: "signal construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_handoff
  - bld_tools_dag
  - bld_tools_validation_schema
  - bld_tools_session_state
  - bld_tools_input_schema
  - bld_tools_retriever_config
  - bld_tools_validator
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_interface
---

# Tools: signal-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| `signal_writer.py` | Real emitter pattern for completion signals | Schema alignment | CONDITIONAL |
| `spawn_monitor.ps1` | Polls `.claude/signals/` for status changes | Consumer validation | CONDITIONAL |
| `validate_artifact.py` | Generic artifact validator | Phase 3 | [PLANNED] |
## Runtime Interfaces
| Interface | Path | Use |
|-----------|------|-----|
| Signal directory | `.claude/signals/` | write/read JSON event files |
| P12 schema | `P12_orchestration/_schema.yaml` | naming, machine format, limits |
| Signal template | `P12_orchestration/templates/tpl_signal.md` | human reference for event payload |
| Validation example | `P06_schema/examples/p06_vs_signal_completion.md` | downstream consumer expectation |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Until a generic validator exists, validate manually:
1. filename matches `p12_sig_{event}.json`
2. JSON parses
3. core fields present
4. status in enum
5. timestamp is ISO 8601
6. payload fits `signal`, not `handoff` or `dispatch_rule`

## Metadata

```yaml
id: bld_tools_signal
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-signal.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_handoff]] | sibling | 0.57 |
| [[bld_tools_dag]] | sibling | 0.51 |
| [[bld_tools_validation_schema]] | sibling | 0.49 |
| [[bld_tools_session_state]] | sibling | 0.48 |
| [[bld_tools_input_schema]] | sibling | 0.46 |
| [[bld_tools_retriever_config]] | sibling | 0.45 |
| [[bld_tools_validator]] | sibling | 0.45 |
| [[bld_tools_memory_scope]] | sibling | 0.45 |
| [[bld_tools_cli_tool]] | sibling | 0.45 |
| [[bld_tools_interface]] | sibling | 0.45 |
