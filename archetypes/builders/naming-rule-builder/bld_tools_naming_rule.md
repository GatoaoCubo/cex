---
id: bld_tools_naming_rule
pillar: P04
llm_function: CALL
kind: tools
domain: naming_rule
version: 1.0.0
quality: 9.1
title: "Tools Naming Rule"
author: n03_builder
tags: [naming_rule, builder, examples]
tldr: "Golden and anti-examples for naming rule construction, demonstrating ideal structure and common pitfalls."
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - tools_prompt_template_builder
  - bld_tools_voice_pipeline
  - bld_collaboration_naming_rule
  - bld_tools_collaboration_pattern
  - bld_tools_action_paradigm
  - bld_tools_thinking_config
  - bld_memory_naming_rule
  - bld_tools_realtime_session
  - bld_tools_workflow
  - naming-rule-builder
---

# Tools — Naming Rule Builder
## Tool Registry
| Tool | Status | Tag | Purpose |
|------|--------|-----|---------|
| brain_query | CONDITIONAL | [MCP] | Discover existing naming rules and related conventions |
| Read | ACTIVE | [FILE] | Read existing naming rule files for scope overlap check |
| Grep | ACTIVE | [FILE] | Search for naming patterns in existing artifacts |
| Glob | ACTIVE | [FILE] | List existing naming rule files in pool directories |
## brain_query [IF MCP]
**Activation**: Only when Brain MCP is available in the current session.
```
brain_query("naming rule {scope_slug}")
brain_query("p05 nr {keyword}")
brain_query("naming convention {domain}")
```
**Expected return**: Existing naming rule artifacts, related conventions, pillar assignments.
**Fallback (MCP unavailable)**: Use Grep to search `records/pool/` for `kind: naming_rule` entries.
## Read [ACTIVE]
Use to load existing naming rule artifacts for scope comparison:
```
Read: records/pool/{pillar}/{id}.md
Read: archetypes/builders/naming-rule-builder/SCHEMA.md
Read: archetypes/builders/naming-rule-builder/OUTPUT_TEMPLATE.md
```
## Grep [ACTIVE]
Search for naming rule patterns in the codebase:
```
Grep: pattern="kind: naming_rule" path=records/pool/
Grep: pattern="^id: p05_nr_" path=records/pool/
Grep: pattern="{scope_keyword}" path=records/pool/
```
## Glob [ACTIVE]
List existing naming rules for scope overlap detection:
```
Glob: pattern="records/pool/**/p05_nr_*.md"
Glob: pattern="archetypes/builders/naming-rule-builder/*.md"
```
## Data Sources
| Source | Content | When to Use |
|--------|---------|-------------|
| `records/pool/` | Existing naming rule artifacts | Always — check before creating |
| `SCHEMA.md` | Field definitions and constraints | Always — source of truth |
| `OUTPUT_TEMPLATE.md` | Output structure | Always — derive final artifact |
| `KNOWLEDGE.md` | Industry naming standards | When establishing case style or pattern base |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[tools_prompt_template_builder]] | sibling | 0.49 |
| [[bld_tools_voice_pipeline]] | sibling | 0.46 |
| [[bld_collaboration_naming_rule]] | downstream | 0.46 |
| [[bld_tools_collaboration_pattern]] | sibling | 0.42 |
| [[bld_tools_action_paradigm]] | sibling | 0.42 |
| [[bld_tools_thinking_config]] | sibling | 0.41 |
| [[bld_memory_naming_rule]] | downstream | 0.37 |
| [[bld_tools_realtime_session]] | sibling | 0.35 |
| [[bld_tools_workflow]] | sibling | 0.35 |
| [[naming-rule-builder]] | downstream | 0.34 |
