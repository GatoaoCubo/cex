---
kind: tools
id: bld_tools_quality_gate
pillar: P04
llm_function: CALL
purpose: Tools available for quality_gate production
quality: 9.0
title: "Tools Quality Gate"
version: "1.0.0"
author: n03_builder
tags: [quality_gate, builder, examples]
tldr: "Golden and anti-examples for quality gate construction, demonstrating ideal structure and common pitfalls."
domain: "quality gate construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_prompt_version
  - bld_tools_handoff_protocol
  - bld_tools_chunk_strategy
  - bld_tools_constraint_spec
  - bld_tools_path_config
  - bld_tools_runtime_rule
  - bld_tools_action_prompt
---

# Tools: quality-gate-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing quality_gates | Phase 1 (check duplicates) | CONDITIONAL |
| validate_kc.py | Reference pattern for HARD/SOFT gates | Design time | CONDITIONAL |
| validate_artifact.py | Validate any artifact kind | Phase 3 | [PLANNED] |
## Reference Gates (existing)
| Gate | File | Domain |
|------|------|--------|
| CEX Quality Gate | P11_feedback/examples/p11_qg_cex_quality.md | Pre-commit |
| Shokunin Pool Gate | P11_feedback/examples/p11_qg_shokunin_pool.md | Pool entry |
| TDD Compliance | P11_feedback/examples/p11_qg_tdd_compliance.md | Testing |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_quality_gate
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-quality-gate.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_retriever_config]] | sibling | 0.57 |
| [[bld_tools_memory_scope]] | sibling | 0.57 |
| [[bld_tools_cli_tool]] | sibling | 0.56 |
| [[bld_tools_prompt_version]] | sibling | 0.55 |
| [[bld_tools_handoff_protocol]] | sibling | 0.54 |
| [[bld_tools_chunk_strategy]] | sibling | 0.54 |
| [[bld_tools_constraint_spec]] | sibling | 0.54 |
| [[bld_tools_path_config]] | sibling | 0.54 |
| [[bld_tools_runtime_rule]] | sibling | 0.54 |
| [[bld_tools_action_prompt]] | sibling | 0.54 |
