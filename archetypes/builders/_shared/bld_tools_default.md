---
quality: 7.9
id: bld_tools_default
kind: builder_default
pillar: P04
source: shared
title: "Tools Default: Universal Builder Toolkit"
llm_function: CALL
version: 1.1.0
quality: 7.6
tags: [tools, P04, shared, default]
related:
  - bld_tools_kind
  - p08_ac_explore
  - bld_tools_voice_pipeline
  - bld_tools_skill
  - bld_tools_golden_test
  - bld_tools_collaboration_pattern
  - bld_tools_quality_gate
  - bld_tools_action_paradigm
  - bld_tools_thinking_config
  - bld_tools_action_prompt
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-22"
---

# P04 Tools — Universal Builder Toolkit

## Standard Tools

Every builder has access to these tools by default:

| Tool | Purpose |
|------|---------|
| `Read` | Read any file from the filesystem |
| `Write` | Create new files |
| `Edit` | Modify existing files (preferred over Write for patches) |
| `Bash` | Run shell commands (git, python, compile steps) |
| `Glob` | Find files by pattern |
| `Grep` | Search file contents by regex |

## CEX System Tools (available in all nuclei)

| Command | Purpose |
|---------|---------|
| `python _tools/cex_compile.py {path}` | Compile .md artifact to .yaml |
| `python _tools/cex_doctor.py` | Validate builder health |
| `python _tools/cex_index.py` | Refresh search index |
| `python _tools/cex_sanitize.py --check` | Verify ASCII-only in code files |

## Tool Selection Rules

1. Prefer `Edit` over `Write` when modifying existing files
2. Use `Glob` before `Bash ls` for file discovery
3. Use `Grep` before `Bash grep` for content search
4. Chain `Bash` calls with `&&` for sequential steps
5. Never use tools requiring user interaction in autonomous mode

## When to Override This Default

Override `bld_tools_{kind}.md` when the builder needs:
- External APIs (browser_tool, search_tool)
- Database access (db_connector)
- MCP servers (mcp_server)
- Specialized compute (code_executor)

## Hard Gates (H01-H07) -- ALL must pass

| Gate | Check | Fail Action |
|------|-------|-------------|
| H01 | Frontmatter present and valid YAML | Return to F6, add frontmatter |
| H02 | `quality: null` in frontmatter (never self-score) | Remove score, set null |
| H03 | Required fields: id, kind, 8f, pillar, title | Add missing fields |
| H04 | Body density >= 0.85 (content lines / total lines) | Add structured data, remove filler |
| H05 | No hallucinated sources (cited paths must exist) | Remove or verify citations |
| H06 | ASCII-only in any generated code blocks | Replace non-ASCII per cex_sanitize rules |
| H07 | Output matches pillar schema constraints | Restructure to match schema |

## Scoring Dimensions (5D)

| Dimension | Weight | Criteria |
|-----------|--------|---------|
| D1 Structural | 30% | Frontmatter complete, naming correct, file in right pillar dir |
| D2 Content | 25% | Density >= 0.85, no filler, tables preferred over prose |
| D3 Accuracy | 20% | No hallucination, sources verified, constraints respected |
| D4 Usefulness | 15% | Actionable, implementable, unambiguous |
| D5 CEX fit | 10% | Kind/pillar/nucleus alignment, 8F stage correctness |

## Tool Integration Checklist

- Verify tool name follows snake_case convention
- Validate input/output schema matches interface contract
- Cross-reference with capability_registry for discoverability
- Test tool invocation in sandbox before production use

## Invocation Pattern

```yaml
# Tool invocation contract
name: tool_name
input_schema: validated
output_schema: validated
error_handling: defined
timeout: configured
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_kind]] | related | 0.32 |
| [[p08_ac_explore]] | downstream | 0.31 |
| [[bld_tools_voice_pipeline]] | related | 0.31 |
| [[bld_tools_skill]] | related | 0.29 |
| [[bld_tools_golden_test]] | related | 0.29 |
| [[bld_tools_collaboration_pattern]] | related | 0.28 |
| [[bld_tools_quality_gate]] | related | 0.28 |
| [[bld_tools_action_paradigm]] | related | 0.28 |
| [[bld_tools_thinking_config]] | related | 0.28 |
| [[bld_tools_action_prompt]] | related | 0.28 |
