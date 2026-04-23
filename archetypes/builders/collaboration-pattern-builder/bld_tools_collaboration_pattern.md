---
kind: tools
id: bld_tools_collaboration_pattern
pillar: P04
llm_function: CALL
purpose: Tools available during collaboration_pattern artifact production
quality: 9.1
title: "Tools: collaboration-pattern-builder"
version: "1.0.0"
author: n02_reviewer
tags: [collaboration_pattern, builder, tools, P04]
tldr: "Tool registry for collaboration_pattern builder: CEX pipeline tools and file system operations for pattern production."
domain: "collaboration_pattern construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - bld_tools_voice_pipeline
  - tools_prompt_template_builder
  - bld_tools_action_paradigm
  - bld_tools_thinking_config
  - bld_tools_naming_rule
  - bld_tools_realtime_session
  - bld_tools_quality_gate
  - bld_tools_citation
  - bld_tools_pattern
  - bld_tools_cli_tool
---

# Tools -- collaboration-pattern-builder
## Tool Registry
| Tool | Status | Tag | Purpose |
|------|--------|-----|---------|
| brain_query | CONDITIONAL | [MCP] | Discover existing collaboration topologies and coordination patterns |
| Read | ACTIVE | [FS] | Read SCHEMA.md, OUTPUT_TEMPLATE.md, sibling examples |
| Glob | ACTIVE | [FS] | Find existing p12_collab_* files in the pool |
| Grep | ACTIVE | [FS] | Search for topology types or agent role patterns |
| Write | ACTIVE | [FS] | Produce the final collaboration_pattern artifact |
| Edit | ACTIVE | [FS] | Patch frontmatter or body sections during VALIDATE phase |

## Tool Descriptions
### brain_query [MCP] -- CONDITIONAL
Available only when the Brain MCP server is running. Use to:
- Find existing `collaboration_pattern` artifacts that overlap with the requested domain
- Retrieve topology type vocabulary used in the pool
- Identify conflict resolution strategies already documented

```
brain_query("collaboration pattern mesh hierarchical topology")
brain_query("P12 kind:collaboration_pattern domain:{{domain}}")
brain_query("multi-agent coordination channel protocol")
```

Mark results as advisory -- validate topology types against SCHEMA.md before adopting.

### Read [FS] -- ACTIVE
Read before composing:
- `SCHEMA.md` -- source of truth for all field definitions
- `OUTPUT_TEMPLATE.md` -- exact frontmatter and body structure to follow
- `QUALITY_GATES.md` -- gate list to validate against
- Sibling p12_collab_* files for naming and style reference

### Glob [FS] -- ACTIVE
```
records/pool/**/p12_collab_*.md
archetypes/builders/collaboration-pattern-builder/
```

Use to check for ID collisions before assigning a new `id`.

### Grep [FS] -- ACTIVE
```
grep pattern: "topology"            -- verify topology vocabulary
grep pattern: "communication channel"  -- check channel documentation patterns
grep pattern: "kind: collaboration_pattern"  -- inventory existing patterns
```

### Write [FS] -- ACTIVE
Final delivery tool. Write the completed artifact to its target path under `records/pool/` or
the caller-specified output path.

### Edit [FS] -- ACTIVE
Use during VALIDATE phase to patch specific fields (quality score, updated date, topology type)
without rewriting the full file.

## Data Sources
| Source | Content | When to use |
|--------|---------|-------------|
| SCHEMA.md | Field definitions, ID pattern, constraints | Every production run |
| OUTPUT_TEMPLATE.md | Exact frontmatter + body structure | Every production run |
| QUALITY_GATES.md | H01-H08 HARD gates | Every validation run |
| KNOWLEDGE.md | Topology types, consensus algorithms, coordination protocols | When designing agent topology |
| MEMORY.md | Common mistakes, anti-patterns | When stuck or producing a variant |
| pool p12_collab_* files | Reference examples | When uncertain about style |

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
| Domain | collaboration_pattern construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_voice_pipeline]] | sibling | 0.65 |
| [[tools_prompt_template_builder]] | sibling | 0.64 |
| [[bld_tools_action_paradigm]] | sibling | 0.62 |
| [[bld_tools_thinking_config]] | sibling | 0.60 |
| [[bld_tools_naming_rule]] | sibling | 0.50 |
| [[bld_tools_realtime_session]] | sibling | 0.50 |
| [[bld_tools_quality_gate]] | sibling | 0.37 |
| [[bld_tools_citation]] | sibling | 0.36 |
| [[bld_tools_pattern]] | sibling | 0.36 |
| [[bld_tools_cli_tool]] | sibling | 0.36 |
