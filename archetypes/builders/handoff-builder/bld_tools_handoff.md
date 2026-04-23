---
kind: tools
id: bld_tools_handoff
pillar: P04
llm_function: CALL
purpose: Tools and runtime surfaces relevant to handoff production
quality: 9.1
title: "Tools Handoff"
version: "1.0.0"
author: n03_builder
tags: [handoff, builder, examples]
tldr: "Golden and anti-examples for handoff construction, demonstrating ideal structure and common pitfalls."
domain: "handoff construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_signal
  - bld_tools_dag
  - bld_tools_handoff_protocol
  - bld_tools_action_prompt
  - bld_tools_session_state
  - bld_tools_memory_scope
  - bld_tools_output_validator
  - bld_tools_retriever_config
  - bld_tools_instruction
  - bld_tools_cli_tool
---

# Tools: handoff-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| `brain_query` | Search for existing handoffs and related artifacts | Phase 1 | CONDITIONAL [MCP] |
| `validate_artifact.py` | Generic artifact validator | Phase 3 | [PLANNED] |
| `signal_writer.py` | Signal completion mechanism referenced in handoffs | Signal section | CONDITIONAL |
## Runtime Interfaces
| Interface | Path | Use |
|-----------|------|-----|
| P12 schema | `P12_orchestration/_schema.yaml` | naming, machine format, limits |
| Handoff template | `P12_orchestration/templates/tpl_handoff.md` | human reference |
| Handoff directory | `.claude/handoffs/` | primary output location |
| Compiled output | `P12_orchestration/compiled/p12_ho_{task}.md` | secondary output |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Until a generic validator exists, validate manually:
1. filename matches `p12_ho_{task}.md`
2. YAML frontmatter parses
3. required fields present
4. autonomy in enum (`full`, `supervised`, `assisted`)
5. all 5 body sections exist
6. scope fence has SOMENTE + NAO TOQUE
7. payload fits `handoff`, not `action_prompt` or `signal`
8. size <= 4096 bytes

## Metadata

```yaml
id: bld_tools_handoff
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-handoff.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_signal]] | sibling | 0.63 |
| [[bld_tools_dag]] | sibling | 0.55 |
| [[bld_tools_handoff_protocol]] | sibling | 0.52 |
| [[bld_tools_action_prompt]] | sibling | 0.50 |
| [[bld_tools_session_state]] | sibling | 0.50 |
| [[bld_tools_memory_scope]] | sibling | 0.47 |
| [[bld_tools_output_validator]] | sibling | 0.47 |
| [[bld_tools_retriever_config]] | sibling | 0.46 |
| [[bld_tools_instruction]] | sibling | 0.46 |
| [[bld_tools_cli_tool]] | sibling | 0.46 |
