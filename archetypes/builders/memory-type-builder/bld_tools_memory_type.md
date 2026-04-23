---
kind: tools
id: bld_tools_memory_type
pillar: P04
llm_function: CALL
quality: 9.1
title: "Tools Memory Type"
version: "1.0.0"
author: n03_builder
tags: [memory_type, builder, examples]
tldr: "Golden and anti-examples for memory type construction, demonstrating ideal structure and common pitfalls."
domain: "memory type construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_manifest_memory_type
  - bld_config_memory_type
  - bld_config_tagline
  - skill
  - bld_tools_agent
  - bld_output_template_builder
  - research_then_build
  - bld_collaboration_memory_type
  - bld_tools_prompt_cache
  - bld_output_template_signal
---

# Tools: memory-type-builder

| Tool | Purpose | Status |
|------|---------|--------|
| cex_memory_types.py | MemoryType enum, should_save(), parse_memory_type() | ACTIVE |
| cex_memory_age.py | Age labels, freshness caveats, decay functions | ACTIVE |
| cex_memory_update.py | Append observations with type-aware decay | ACTIVE |
| cex_compile.py | Compile .md to .yaml in P10_memory/compiled/ | ACTIVE |
| cex_score.py | Score artifact quality (hybrid) | ACTIVE |

## Tool Permissions

| Tool | Read | Write | Execute | Scope |
|------|------|-------|---------|-------|
| cex_memory_types.py | ✅ | ❌ | ✅ | P10 |
| cex_memory_age.py | ✅ | ❌ | ✅ | P10 |
| cex_memory_update.py | ✅ | ✅ | ✅ | P10 |
| cex_compile.py | ✅ | ✅ | ✅ | pillar |
| cex_score.py | ✅ | ❌ | ✅ | pillar |

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_memory_type
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-memory-type.md
```

## Builder Context

This ISO operates within the `memory-type-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_manifest_memory_type]] | upstream | 0.68 |
| [[bld_config_memory_type]] | downstream | 0.50 |
| [[bld_config_tagline]] | downstream | 0.43 |
| [[skill]] | downstream | 0.42 |
| [[bld_tools_agent]] | sibling | 0.41 |
| [[bld_output_template_builder]] | upstream | 0.38 |
| [[research_then_build]] | downstream | 0.37 |
| [[bld_collaboration_memory_type]] | downstream | 0.36 |
| [[bld_tools_prompt_cache]] | sibling | 0.36 |
| [[bld_output_template_signal]] | downstream | 0.35 |
