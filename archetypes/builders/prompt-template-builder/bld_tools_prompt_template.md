---
id: tools_prompt_template_builder
kind: tools
pillar: P04
llm_function: CALL
domain: prompt_template
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [tools, prompt-template, P03, data-sources]
quality: 9.1
title: "Tools Prompt Template"
tldr: "Golden and anti-examples for prompt template construction, demonstrating ideal structure and common pitfalls."
density_score: 0.90
related:
  - bld_tools_voice_pipeline
  - bld_tools_collaboration_pattern
  - bld_tools_action_paradigm
  - bld_tools_thinking_config
  - bld_tools_naming_rule
  - bld_tools_realtime_session
  - bld_tools_golden_test
  - bld_tools_quality_gate
  - bld_tools_prompt_compiler
  - bld_tools_type_def
---

# Tools — prompt-template-builder
## Tool Registry
| Tool | Status | Tag | Purpose |
|---|---|---|---|
| brain_query | CONDITIONAL | [MCP] | Discover existing templates and variable patterns |
| Read | ACTIVE | [FS] | Read SCHEMA.md, OUTPUT_TEMPLATE.md, sibling examples |
| Glob | ACTIVE | [FS] | Find existing p03_pt_* files in the pool |
| Grep | ACTIVE | [FS] | Search for variable name collisions or pattern reuse |
| Write | ACTIVE | [FS] | Produce the final prompt_template artifact |
| Edit | ACTIVE | [FS] | Patch frontmatter or template body during VALIDATE phase |
## Tool Descriptions
### brain_query [MCP] — CONDITIONAL
Available only when the Brain MCP server is running. Use to:
- Find existing `prompt_template` artifacts that overlap with the requested topic
- Retrieve variable naming conventions used in the pool
- Identify composable partials that could be referenced
```
brain_query("prompt template {{topic}} variables")
brain_query("P03 kind:prompt_template domain:{{domain}}")
brain_query("reusable mold {{keyword}} CEX")
```
Mark results as advisory — do not copy-paste variable names without validating types.
### Read [FS] — ACTIVE
Read before composing:
- `SCHEMA.md` — source of truth for all field definitions
- `OUTPUT_TEMPLATE.md` — exact frontmatter and body structure to follow
- `QUALITY_GATES.md` — gate list to validate against
- Sibling p03_pt_* files for naming and style reference
### Glob [FS] — ACTIVE
```
records/pool/**/p03_pt_*.md
archetypes/builders/prompt-template-builder/
```
Use to check for ID collisions before assigning a new `id`.
### Grep [FS] — ACTIVE
```
grep pattern: "{{variable_name}}"  -- check if a variable name is already standardized
grep pattern: "kind: prompt_template" -- inventory existing templates
```
### Write [FS] — ACTIVE
Final delivery tool. Write the completed artifact to its target path under `records/pool/` or the caller-specified output path.
### Edit [FS] — ACTIVE
Use during VALIDATE phase to patch specific fields (quality score, updated date, variable defaults) without rewriting the full file.
## Data Sources
| Source | Content | When to use |
|---|---|---|
| SCHEMA.md | Field definitions, ID pattern, constraints | Every production run |
| OUTPUT_TEMPLATE.md | Exact frontmatter + body structure | Every production run |
| QUALITY_GATES.md | H01-H08 HARD, S01-S10 SOFT | Every validation run |
| KNOWLEDGE.md | Industry implementations, syntax tiers | When choosing variable_syntax |
| MEMORY.md | Common mistakes, anti-patterns | When stuck or producing a variant |
| pool p03_pt_* files | Reference examples | When uncertain about style |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_voice_pipeline]] | sibling | 0.66 |
| [[bld_tools_collaboration_pattern]] | sibling | 0.62 |
| [[bld_tools_action_paradigm]] | sibling | 0.61 |
| [[bld_tools_thinking_config]] | sibling | 0.60 |
| [[bld_tools_naming_rule]] | sibling | 0.57 |
| [[bld_tools_realtime_session]] | sibling | 0.49 |
| [[bld_tools_golden_test]] | sibling | 0.37 |
| [[bld_tools_quality_gate]] | sibling | 0.37 |
| [[bld_tools_prompt_compiler]] | sibling | 0.37 |
| [[bld_tools_type_def]] | sibling | 0.36 |
