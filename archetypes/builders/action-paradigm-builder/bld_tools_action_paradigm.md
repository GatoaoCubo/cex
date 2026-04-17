---
kind: tools
id: bld_tools_action_paradigm
pillar: P04
llm_function: CALL
purpose: Tools available during action_paradigm artifact production
quality: 9.1
title: "Tools: action-paradigm-builder"
version: "1.0.0"
author: n02_reviewer
tags: [action_paradigm, builder, tools, P04]
tldr: "Tool registry for action_paradigm builder: CEX pipeline tools and file system operations for paradigm production."
domain: "action_paradigm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
---

# Tools -- action-paradigm-builder

## Tool Registry

| Tool | Status | Tag | Purpose |
|------|--------|-----|---------|
| brain_query | CONDITIONAL | [MCP] | Discover existing action paradigms and behavioral patterns |
| Read | ACTIVE | [FS] | Read SCHEMA.md, OUTPUT_TEMPLATE.md, sibling examples |
| Glob | ACTIVE | [FS] | Find existing p04_act_* files in the pool |
| Grep | ACTIVE | [FS] | Search for precondition patterns or action type usage |
| Write | ACTIVE | [FS] | Produce the final action_paradigm artifact |
| Edit | ACTIVE | [FS] | Patch frontmatter or body sections during VALIDATE phase |

## Tool Descriptions

### brain_query [MCP] -- CONDITIONAL

Available only when the Brain MCP server is running. Use to:
- Find existing `action_paradigm` artifacts that overlap with the requested domain
- Retrieve action type classification patterns used in the pool
- Identify failure recovery strategies already documented

```
brain_query("action paradigm state machine reactive")
brain_query("P04 kind:action_paradigm domain:{{domain}}")
brain_query("precondition postcondition agent execution")
```

Mark results as advisory -- validate action types against SCHEMA.md before adopting.

### Read [FS] -- ACTIVE

Read before composing:
- `SCHEMA.md` -- source of truth for all field definitions
- `OUTPUT_TEMPLATE.md` -- exact frontmatter and body structure to follow
- `QUALITY_GATES.md` -- gate list to validate against
- Sibling p04_act_* files for naming and style reference

### Glob [FS] -- ACTIVE

```
records/pool/**/p04_act_*.md
archetypes/builders/action-paradigm-builder/
```

Use to check for ID collisions before assigning a new `id`.

### Grep [FS] -- ACTIVE

```
grep pattern: "action_type"     -- verify action type vocabulary
grep pattern: "precondition"    -- check precondition documentation patterns
grep pattern: "kind: action_paradigm"  -- inventory existing paradigms
```

### Write [FS] -- ACTIVE

Final delivery tool. Write the completed artifact to its target path under `records/pool/` or
the caller-specified output path.

### Edit [FS] -- ACTIVE

Use during VALIDATE phase to patch specific fields (quality score, updated date, action_type)
without rewriting the full file.

## Data Sources

| Source | Content | When to use |
|--------|---------|-------------|
| SCHEMA.md | Field definitions, ID pattern, constraints | Every production run |
| OUTPUT_TEMPLATE.md | Exact frontmatter + body structure | Every production run |
| QUALITY_GATES.md | H01-H08 HARD gates | Every validation run |
| KNOWLEDGE.md | Domain concepts, action types, failure patterns | When designing state-action model |
| MEMORY.md | Common mistakes, anti-patterns | When stuck or producing a variant |
| pool p04_act_* files | Reference examples | When uncertain about style |

## CEX Pipeline Tools

| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile .md artifact to .yaml | After Write (F8) |
| cex_score.py | Peer-review quality scoring | After production (F7) |
| cex_retriever.py | Discover similar artifacts by TF-IDF | During F3 INJECT |
| cex_doctor.py | Health check builder ISOs | Before dispatch |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Properties

| Property | Value |
|----------|-------|
| Kind | `tools` |
| Pillar | P04 |
| Domain | action_paradigm construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
