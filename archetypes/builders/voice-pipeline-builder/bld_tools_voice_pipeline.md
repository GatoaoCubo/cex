---
kind: tools
id: bld_tools_voice_pipeline
pillar: P04
llm_function: CALL
purpose: Tools available during voice_pipeline artifact production
quality: 9.1
title: "Tools: voice-pipeline-builder"
version: "1.0.0"
author: n02_reviewer
tags: [voice_pipeline, builder, tools, P04]
tldr: "Tool registry for voice_pipeline builder: CEX pipeline tools and file system operations for pipeline production."
domain: "voice_pipeline construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - tools_prompt_template_builder
  - bld_tools_thinking_config
  - bld_tools_collaboration_pattern
  - bld_tools_action_paradigm
  - bld_tools_naming_rule
  - bld_tools_realtime_session
  - bld_tools_quality_gate
  - bld_tools_citation
  - bld_tools_cli_tool
  - bld_tools_golden_test
---

# Tools -- voice-pipeline-builder
## Tool Registry
| Tool | Status | Tag | Purpose |
|------|--------|-----|---------|
| brain_query | CONDITIONAL | [MCP] | Discover existing voice pipelines and STT/TTS integration patterns |
| Read | ACTIVE | [FS] | Read SCHEMA.md, OUTPUT_TEMPLATE.md, sibling examples |
| Glob | ACTIVE | [FS] | Find existing p04_vp_* files in the pool |
| Grep | ACTIVE | [FS] | Search for component patterns or provider abstraction approaches |
| Write | ACTIVE | [FS] | Produce the final voice_pipeline artifact |
| Edit | ACTIVE | [FS] | Patch frontmatter or body sections during VALIDATE phase |

## Tool Descriptions
### brain_query [MCP] -- CONDITIONAL
Available only when the Brain MCP server is running. Use to:
- Find existing `voice_pipeline` artifacts that overlap with the requested use case
- Retrieve component naming conventions used in the pool
- Identify fallback chain patterns already documented

```
brain_query("voice pipeline STT NLU TTS architecture")
brain_query("P04 kind:voice_pipeline domain:{{domain}}")
brain_query("speech recognition dialogue management provider abstraction")
```

Mark results as advisory -- validate component names against SCHEMA.md before adopting.

### Read [FS] -- ACTIVE
Read before composing:
- `SCHEMA.md` -- source of truth for all field definitions
- `OUTPUT_TEMPLATE.md` -- exact frontmatter and body structure to follow
- `QUALITY_GATES.md` -- gate list to validate against
- Sibling p04_vp_* files for naming and style reference

### Glob [FS] -- ACTIVE
```
records/pool/**/p04_vp_*.md
archetypes/builders/voice-pipeline-builder/
```

Use to check for ID collisions before assigning a new `id`.

### Grep [FS] -- ACTIVE
```
grep pattern: "components"          -- verify component list presence
grep pattern: "fallback"            -- check fallback chain documentation
grep pattern: "kind: voice_pipeline"  -- inventory existing pipelines
```

### Write [FS] -- ACTIVE
Final delivery tool. Write the completed artifact to its target path under `records/pool/` or
the caller-specified output path.

### Edit [FS] -- ACTIVE
Use during VALIDATE phase to patch specific fields (quality score, updated date, component list)
without rewriting the full file.

## Data Sources
| Source | Content | When to use |
|--------|---------|-------------|
| SCHEMA.md | Field definitions, ID pattern, constraints | Every production run |
| OUTPUT_TEMPLATE.md | Exact frontmatter + body structure | Every production run |
| QUALITY_GATES.md | H01-H08 HARD gates | Every validation run |
| KNOWLEDGE.md | STT/NLU/TTS concepts, latency targets, compliance requirements | When designing pipeline stages |
| MEMORY.md | Common mistakes, anti-patterns | When stuck or producing a variant |
| pool p04_vp_* files | Reference examples | When uncertain about style |

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
| Domain | voice_pipeline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[tools_prompt_template_builder]] | sibling | 0.65 |
| [[bld_tools_thinking_config]] | sibling | 0.63 |
| [[bld_tools_collaboration_pattern]] | sibling | 0.62 |
| [[bld_tools_action_paradigm]] | sibling | 0.62 |
| [[bld_tools_naming_rule]] | sibling | 0.52 |
| [[bld_tools_realtime_session]] | sibling | 0.52 |
| [[bld_tools_quality_gate]] | sibling | 0.39 |
| [[bld_tools_citation]] | sibling | 0.38 |
| [[bld_tools_cli_tool]] | sibling | 0.38 |
| [[bld_tools_golden_test]] | sibling | 0.37 |
