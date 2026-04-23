---
kind: tools
id: bld_tools_realtime_session
pillar: P04
llm_function: CALL
purpose: Tools available during realtime_session artifact production
quality: 9.1
title: "Tools: realtime-session-builder"
version: "1.1.0"
author: n01_audit
tags: [realtime_session, builder, tools, P04]
tldr: "Tool registry for realtime-session-builder: CEX pipeline tools and FS operations for session config production."
domain: "realtime_session construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_tools_voice_pipeline
  - tools_prompt_template_builder
  - bld_tools_thinking_config
  - bld_tools_collaboration_pattern
  - bld_tools_action_paradigm
  - bld_tools_naming_rule
  - bld_tools_notifier
  - bld_tools_prompt_compiler
  - bld_tools_retriever_config
  - bld_tools_pattern
---

# Tools -- realtime-session-builder
## Tool Registry
| Tool | Status | Tag | Purpose |
|------|--------|-----|---------|
| Read | ACTIVE | [FS] | Read schema, output_template, sibling examples |
| Glob | ACTIVE | [FS] | Find existing p04_rs_* files in pool |
| Grep | ACTIVE | [FS] | Search for provider/model patterns in existing artifacts |
| Write | ACTIVE | [FS] | Produce final realtime_session artifact |
| Edit | ACTIVE | [FS] | Patch frontmatter or session config during VALIDATE phase |
| brain_query | CONDITIONAL | [MCP] | Discover existing realtime_session artifacts and patterns |

## Tool Descriptions
### Read [FS] -- ACTIVE
Read before composing:
- `bld_schema_realtime_session.md` -- ID pattern, required fields, body structure
- `bld_output_template_realtime_session.md` -- session config JSON + latency table structure
- `bld_quality_gate_realtime_session.md` -- H01-H10 gates to validate against
- `bld_knowledge_card_realtime_session.md` -- provider/model pairs, event types

### Glob [FS] -- ACTIVE
```
P04_tools/realtime_session/p04_rs_*.md
archetypes/builders/realtime-session-builder/
```

Check for ID collisions before assigning new `id`.

### Grep [FS] -- ACTIVE
```
grep pattern: "provider: openai"        -- find openai realtime examples
grep pattern: "server_vad"              -- check VAD config patterns
grep pattern: "kind: realtime_session"  -- inventory existing artifacts
grep pattern: "ephemeral"               -- verify auth patterns
```

### Write [FS] -- ACTIVE
Final delivery. Write completed artifact to `P04_tools/realtime_session/` or
caller-specified path.

### Edit [FS] -- ACTIVE
Use during VALIDATE phase to patch specific fields (model version, VAD threshold,
latency targets) without rewriting full file.

### brain_query [MCP] -- CONDITIONAL
Available when Brain MCP server is running. Use to:
- Find existing `realtime_session` artifacts for the target provider
- Retrieve VAD threshold patterns used across deployments
- Identify barge-in handler implementations already documented

```
brain_query("realtime_session provider:openai transport:websocket")
brain_query("VAD threshold server_vad barge-in handler")
brain_query("p04_rs LLM streaming ephemeral token")
```

## CEX Pipeline Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile .md artifact to .yaml | After Write (F8) |
| cex_score.py | Peer-review quality scoring | After production (F7) |
| cex_retriever.py | Discover similar artifacts by TF-IDF | During F3 INJECT |
| cex_doctor.py | Health check builder ISOs | Before dispatch |

## Data Sources
| Source | Content | When to use |
|--------|---------|-------------|
| bld_schema_realtime_session.md | ID pattern, required fields | Every production run |
| bld_output_template_realtime_session.md | Session config JSON structure | Every production run |
| bld_quality_gate_realtime_session.md | H01-H10 HARD gates | Every validation run |
| bld_knowledge_card_realtime_session.md | Provider/model pairs, events, latency targets | During F3 INJECT |
| bld_memory_realtime_session.md | VAD tuning, barge-in patterns, anti-patterns | When stuck or producing variant |

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
| Domain | realtime_session construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_voice_pipeline]] | sibling | 0.58 |
| [[tools_prompt_template_builder]] | sibling | 0.55 |
| [[bld_tools_thinking_config]] | sibling | 0.54 |
| [[bld_tools_collaboration_pattern]] | sibling | 0.54 |
| [[bld_tools_action_paradigm]] | sibling | 0.53 |
| [[bld_tools_naming_rule]] | sibling | 0.44 |
| [[bld_tools_notifier]] | sibling | 0.35 |
| [[bld_tools_prompt_compiler]] | sibling | 0.35 |
| [[bld_tools_retriever_config]] | sibling | 0.35 |
| [[bld_tools_pattern]] | sibling | 0.35 |
