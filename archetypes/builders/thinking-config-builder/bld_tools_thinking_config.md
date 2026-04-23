---
kind: tools
id: bld_tools_thinking_config
pillar: P04
llm_function: CALL
purpose: Tools available during thinking_config artifact production
quality: 9.1
title: "Tools: thinking-config-builder"
version: "1.0.0"
author: n02_reviewer
tags: [thinking_config, builder, tools, P04]
tldr: "Tool registry for thinking_config builder: CEX pipeline tools and file system operations for config production."
domain: "thinking_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - bld_tools_voice_pipeline
  - tools_prompt_template_builder
  - bld_tools_collaboration_pattern
  - bld_tools_action_paradigm
  - bld_tools_realtime_session
  - bld_tools_naming_rule
  - bld_instruction_thinking_config
  - bld_tools_context_window_config
  - bld_tools_cost_budget
  - p11_qg_thinking_config
---

# Tools -- thinking-config-builder
This ISO configures a thinking budget: how many tokens the model may spend on internal reasoning before emitting.

## Tool Registry
| Tool | Status | Tag | Purpose |
|------|--------|-----|---------|
| brain_query | CONDITIONAL | [MCP] | Discover existing thinking configs and budget patterns |
| Read | ACTIVE | [FS] | Read SCHEMA.md, OUTPUT_TEMPLATE.md, sibling examples |
| Glob | ACTIVE | [FS] | Find existing p09_thk_* files in the pool |
| Grep | ACTIVE | [FS] | Search for budget tier patterns or fallback strategies |
| Write | ACTIVE | [FS] | Produce the final thinking_config artifact |
| Edit | ACTIVE | [FS] | Patch frontmatter or body sections during VALIDATE phase |

## Tool Descriptions
### brain_query [MCP] -- CONDITIONAL
Available only when the Brain MCP server is running. Use to:
- Find existing `thinking_config` artifacts that overlap with the requested use case
- Retrieve budget tier vocabulary and threshold values used in the pool
- Identify fallback strategy patterns already documented

```
brain_query("thinking config budget token allocation tier")
brain_query("P09 kind:thinking_config domain:{{domain}}")
brain_query("extended reasoning budget fallback strategy")
```

Mark results as advisory -- validate budget values against SCHEMA.md before adopting.

### Read [FS] -- ACTIVE
Read before composing:
- `SCHEMA.md` -- source of truth for all field definitions
- `OUTPUT_TEMPLATE.md` -- exact frontmatter and body structure to follow
- `QUALITY_GATES.md` -- gate list to validate against
- Sibling p09_thk_* files for naming and style reference

### Glob [FS] -- ACTIVE
```
records/pool/**/p09_thk_*.md
archetypes/builders/thinking-config-builder/
```

Use to check for ID collisions before assigning a new `id`.

### Grep [FS] -- ACTIVE
```
grep pattern: "budget"              -- verify budget field presence
grep pattern: "fallback_strategy"   -- check fallback documentation patterns
grep pattern: "kind: thinking_config"  -- inventory existing configs
```

### Write [FS] -- ACTIVE
Final delivery tool. Write the completed artifact to its target path under `records/pool/` or
the caller-specified output path.

### Edit [FS] -- ACTIVE
Use during VALIDATE phase to patch specific fields (quality score, updated date, budget values)
without rewriting the full file.

## Data Sources
| Source | Content | When to use |
|--------|---------|-------------|
| SCHEMA.md | Field definitions, ID pattern, constraints | Every production run |
| OUTPUT_TEMPLATE.md | Exact frontmatter + body structure | Every production run |
| QUALITY_GATES.md | H01-H08 HARD gates | Every validation run |
| KNOWLEDGE.md | Token budget concepts, tiering strategies, fallback patterns | When designing budget structure |
| MEMORY.md | Common mistakes, anti-patterns | When stuck or producing a variant |
| pool p09_thk_* files | Reference examples | When uncertain about style |

## CEX Pipeline Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile .md artifact to .yaml | After Write (F8) |
| cex_score.py | Peer-review quality scoring | After production (F7) |
| cex_retriever.py | Discover similar artifacts by TF-IDF | During F3 INJECT |
| cex_doctor.py | Health check builder ISOs | Before dispatch |
| cex_token_budget.py | Count tokens and validate budget allocations | During F1 CONSTRAIN |

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
| Domain | thinking_config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_voice_pipeline]] | sibling | 0.63 |
| [[tools_prompt_template_builder]] | sibling | 0.60 |
| [[bld_tools_collaboration_pattern]] | sibling | 0.58 |
| [[bld_tools_action_paradigm]] | sibling | 0.58 |
| [[bld_tools_realtime_session]] | sibling | 0.48 |
| [[bld_tools_naming_rule]] | sibling | 0.47 |
| [[bld_instruction_thinking_config]] | upstream | 0.37 |
| [[bld_tools_context_window_config]] | sibling | 0.36 |
| [[bld_tools_cost_budget]] | sibling | 0.36 |
| [[p11_qg_thinking_config]] | downstream | 0.35 |
