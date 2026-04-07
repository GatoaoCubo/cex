---
kind: tools
id: bld_tools_action_prompt
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for action_prompt production
quality: 9.1
title: "Tools Action Prompt"
version: "1.0.0"
author: n03_builder
tags: [action_prompt, builder, examples]
tldr: "Golden and anti-examples for action prompt construction, demonstrating ideal structure and common pitfalls."
domain: "action prompt construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Tools: action-prompt-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing action_prompts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P03_prompt/_schema.yaml | Field definitions, kinds |
| CEX Examples | P03_prompt/examples/ | Real action_prompt artifacts |
| HOP files | records/pool/*/task_prompt_*.md | 287 existing task prompts (action_prompt-like) |
| Handoff files | .claude/handoffs/*.md | 255 handoffs with task sections |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P03_action_prompt |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, action is verb phrase,
input_required is specific, edge_cases >= 2, no identity content, body has all 5 sections.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_action_prompt
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-action-prompt.md
```
