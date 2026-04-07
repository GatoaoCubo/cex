---
kind: tools
id: bld_tools_hook
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for hook production
quality: 9.1
title: "Tools Hook"
version: "1.0.0"
author: n03_builder
tags: [hook, builder, examples]
tldr: "Golden and anti-examples for hook construction, demonstrating ideal structure and common pitfalls."
domain: "hook construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Tools: hook-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing hooks to avoid duplicates | Phase 1 (research) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 (validate) | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | SCHEMA.md (this builder) | Field definitions, condition object |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_hook |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Claude Code hooks | .claude/settings.json hooks section | Real hook configurations |
| Hook lifecycle docs | Claude Code documentation | Event types and payloads |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == hook, quality == null,
trigger_event valid enum, timeout in range, script_path present.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_hook
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-hook.md
```
