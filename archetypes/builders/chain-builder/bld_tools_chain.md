---
kind: tools
id: bld_tools_chain
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for chain production
quality: 9.1
title: "Tools Chain"
version: "1.0.0"
author: n03_builder
tags: [chain, builder, examples]
tldr: "Golden and anti-examples for chain construction, demonstrating ideal structure and common pitfalls."
domain: "chain construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_prompt_version
  - bld_tools_fallback_chain
  - bld_tools_retriever_config
  - bld_tools_action_prompt
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_constraint_spec
  - bld_tools_instruction
  - bld_tools_handoff_protocol
  - bld_tools_path_config
---

# Tools: chain-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing chains in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P03_prompt/_schema.yaml | Field definitions, chain kind |
| CEX Examples | P03_prompt/examples/ | Real chain artifacts |
| ADW files | records/pool/workflows/ADW_*.md | ~240 implicit chain patterns |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P03_chain |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, steps_count match,
body has all 4 required sections, no runtime orchestration leaked into prompt chain.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_chain
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-chain.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_prompt_version]] | sibling | 0.73 |
| [[bld_tools_fallback_chain]] | sibling | 0.72 |
| [[bld_tools_retriever_config]] | sibling | 0.72 |
| [[bld_tools_action_prompt]] | sibling | 0.72 |
| [[bld_tools_memory_scope]] | sibling | 0.71 |
| [[bld_tools_cli_tool]] | sibling | 0.70 |
| [[bld_tools_constraint_spec]] | sibling | 0.70 |
| [[bld_tools_instruction]] | sibling | 0.69 |
| [[bld_tools_handoff_protocol]] | sibling | 0.68 |
| [[bld_tools_path_config]] | sibling | 0.68 |
