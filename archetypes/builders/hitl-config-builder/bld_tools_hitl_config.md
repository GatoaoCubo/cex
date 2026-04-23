---
kind: tools
id: bld_tools_hitl_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for hitl_config production
quality: 9.1
title: "Tools Hitl Config"
version: "1.0.0"
author: n03_builder
tags: [hitl_config, builder, tools, P11]
tldr: "Tools for hitl_config production: search existing gates, validate YAML, compile artifact, check size."
domain: "hitl_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_path_config
  - bld_tools_prompt_version
  - bld_tools_chunk_strategy
  - bld_tools_quality_gate
  - bld_tools_handoff_protocol
  - bld_tools_output_validator
  - bld_tools_runtime_rule
---

# Tools: hitl-config-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing hitl_config artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| cex_compile.py | Compile .md to .yaml frontmatter | Phase 3 (F8) | AVAILABLE |
| cex_score.py --apply | Run quality gate scoring | Phase 3 (F7) | AVAILABLE |
| cex_retriever.py | Find similar hitl_config artifacts for reference | Phase 1 | AVAILABLE |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
## Data Sources
| Source | Path | Data |
|--------|------|------|
| CEX Schema | P11_feedback/_schema.yaml | Field definitions, hitl_config kind |
| CEX Examples | P11_feedback/examples/ | Real hitl_config artifacts |
| Kind KC | P01_knowledge/library/kind/kc_hitl_config.md | Domain knowledge, patterns, anti-patterns |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, governance layer |
| kinds_meta | .cex/kinds_meta.json | max_bytes, naming, llm_function |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Validation Checklist (manual until automated validator exists)
Run in order at Phase 3:
1. YAML frontmatter parses: `python3 -c "import yaml; yaml.safe_load(open('FILE').read().split('---')[1])"`
2. id pattern: `^p11_hitl_[a-z][a-z0-9_]+$`
3. escalation_chain >= 2 roles
4. approval_flow in [binary, edit, score]
5. timeout_seconds > 0
6. fallback_action in [reject, accept_with_flag, retry]
7. quality == null
8. Body <= 3072 bytes: `python3 -c "print(len(open('FILE').read().encode()))"`

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_hitl_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-hitl-config.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_retriever_config]] | sibling | 0.59 |
| [[bld_tools_memory_scope]] | sibling | 0.57 |
| [[bld_tools_cli_tool]] | sibling | 0.56 |
| [[bld_tools_path_config]] | sibling | 0.56 |
| [[bld_tools_prompt_version]] | sibling | 0.55 |
| [[bld_tools_chunk_strategy]] | sibling | 0.55 |
| [[bld_tools_quality_gate]] | sibling | 0.55 |
| [[bld_tools_handoff_protocol]] | sibling | 0.54 |
| [[bld_tools_output_validator]] | sibling | 0.54 |
| [[bld_tools_runtime_rule]] | sibling | 0.54 |
