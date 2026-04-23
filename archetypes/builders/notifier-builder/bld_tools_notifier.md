---
kind: tools
id: bld_tools_notifier
pillar: P04
llm_function: CALL
purpose: Tool registry for notifier-builder
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
tags: [tools, notifier, P04, brain, validate, forge]
quality: 9.0
tldr: "Tools used by notifier-builder: brain_query for discovery, validate for gates, forge for artifact creation."
density_score: 1.0
title: Tools ISO - notifier
related:
  - bld_tools_webhook
  - tools_prompt_template_builder
  - bld_tools_naming_rule
  - bld_tools_voice_pipeline
  - bld_tools_collaboration_pattern
  - bld_tools_action_paradigm
  - bld_tools_thinking_config
  - bld_tools_realtime_session
  - bld_tools_type_def
  - bld_tools_golden_test
---
# Tools: notifier-builder

## Primary Tools

### brain_query
**Purpose**: Discover existing notifier artifacts, find related builders, retrieve patterns
**When**: Before composing — check for duplicate channels, find provider patterns
```
brain_query("notifier {channel} {use_case}")
brain_query("p04_notify_{channel_slug}")
brain_query("notifier rate limit {provider}")
```

### validate (quality_gate)
**Purpose**: Run HARD + SOFT gates against composed artifact
**When**: After Phase 2 COMPOSE, before declaring complete
**Input**: artifact frontmatter + body as string
**Checks**: H01-H10 HARD, S01-S12 SOFT, score >= 7.0

### forge (artifact write)
**Purpose**: Write final artifact to correct path with correct filename
**When**: After validate passes all HARD gates
**Path pattern**: `archetypes/notifiers/p04_notify_{channel_slug}.md`
**Naming**: id == filename stem, .md extension

## Supporting Tools

### Read
**When**: Load SCHEMA, OUTPUT_TEMPLATE, existing artifacts for dedup check
**Files**: bld_schema_notifier.md, bld_output_template_notifier.md

### Glob
**When**: Check for existing notifiers before creating new one
**Pattern**: `archetypes/notifiers/p04_notify_*.md`

### Grep
**When**: Find channel slug usage, verify id uniqueness across pool
**Pattern**: `^id: p04_notify_{channel_slug}$`

## Tool Call Order
```
1. brain_query     -> discover existing + patterns
2. Read SCHEMA     -> internalize constraints
3. Read TEMPLATE   -> fill vars
4. forge/Write     -> create artifact
5. validate        -> run gates
6. brain_query     -> confirm indexed
```

## Anti-Patterns
- Skipping brain_query -> duplicate artifacts with conflicting ids
- Skipping validate -> broken artifacts reach pool
- Writing to wrong path -> artifact not discoverable

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_webhook]] | sibling | 0.52 |
| [[tools_prompt_template_builder]] | sibling | 0.43 |
| [[bld_tools_naming_rule]] | sibling | 0.43 |
| [[bld_tools_voice_pipeline]] | sibling | 0.43 |
| [[bld_tools_collaboration_pattern]] | sibling | 0.41 |
| [[bld_tools_action_paradigm]] | sibling | 0.40 |
| [[bld_tools_thinking_config]] | sibling | 0.39 |
| [[bld_tools_realtime_session]] | sibling | 0.38 |
| [[bld_tools_type_def]] | sibling | 0.38 |
| [[bld_tools_golden_test]] | sibling | 0.38 |
