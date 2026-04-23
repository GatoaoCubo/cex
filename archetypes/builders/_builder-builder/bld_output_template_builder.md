---
kind: output_template
id: bld_output_template_builder
pillar: P03
llm_function: PRODUCE
purpose: Output format for generated builder artifacts
quality: 9.1
title: "Output Template Builder"
version: "1.0.0"
author: n03_builder
tags: [_builder, builder, examples]
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
domain: "_builder construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_architecture_kind
  - bld_manifest_memory_type
  - bld_instruction_kind
  - kind-builder
  - bld_schema_kind
  - bld_collaboration_kind
  - bld_config_memory_type
  - bld_output_template_signal
  - bld_knowledge_card_kind
  - bld_tools_agent
---
# Output Template: _builder-builder

## Generated Builder Structure
```
archetypes/builders/{kind}-builder/
├── bld_manifest_{kind}.md        # Identity + routing
├── bld_instruction_{kind}.md     # Step-by-step build guide
├── bld_config_{kind}.md          # Constraints + runtime fields
├── bld_memory_{kind}.md          # Learning records
├── bld_tools_{kind}.md           # Tool inventory + permissions
├── bld_collaboration_{kind}.md   # Crew compositions
├── bld_architecture_{kind}.md    # Structure + dependencies
├── bld_schema_{kind}.md          # Field definitions
├── bld_output_template_{kind}.md # Output format
├── bld_examples_{kind}.md        # Reference examples
├── bld_quality_gate_{kind}.md    # Validation gates
├── bld_knowledge_card_{kind}.md  # Domain knowledge
└── bld_system_prompt_{kind}.md   # LLM system prompt
```

## Post-Generation Checklist
1. All 13 files present
2. All frontmatter YAML-parseable
3. Universal fields hydrated
4. cex_doctor.py → PASS (0 WARN)
5. cex_compile.py --all → 0 errors
6. cex_materialize.py → sub-agent created

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P03 |
| Domain | _builder construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Builder Context

This ISO operates within the `_builder-builder` stack, one of 125
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
| [[bld_architecture_kind]] | downstream | 0.51 |
| [[bld_manifest_memory_type]] | upstream | 0.44 |
| [[bld_instruction_kind]] | related | 0.43 |
| [[kind-builder]] | downstream | 0.42 |
| [[bld_schema_kind]] | downstream | 0.40 |
| [[bld_collaboration_kind]] | downstream | 0.37 |
| [[bld_config_memory_type]] | downstream | 0.35 |
| [[bld_output_template_signal]] | sibling | 0.34 |
| [[bld_knowledge_card_kind]] | upstream | 0.33 |
| [[bld_tools_agent]] | downstream | 0.32 |
