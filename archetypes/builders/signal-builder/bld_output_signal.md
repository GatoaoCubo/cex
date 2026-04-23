---
kind: output_template
id: bld_output_template_signal
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a signal
pattern: every field here exists in SCHEMA.md; template derives, never invents
quality: 9.1
title: "Output Template Signal"
version: "1.0.0"
author: n03_builder
tags: [signal, builder, examples]
tldr: "Golden and anti-examples for signal construction, demonstrating ideal structure and common pitfalls."
domain: "signal construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_manifest_memory_type
  - bld_output_template_builder
  - bld_config_memory_type
  - bld_tools_memory_type
  - bld_examples_signal
  - bld_config_tagline
  - bld_config_signal
  - bld_tools_agent
  - p10_lr_input_schema_builder
  - bld_knowledge_card_signal
---

# Output Template: signal
Naming pattern: `p12_sig_{event}.json`
Filename: `p12_sig_{{event}}.json`
```json
{
  "agent_group": "{{agent_group_slug}}",
  "status": "{{complete|error|progress}}",

  "quality_score": {{0.0_to_10.0}},
  "timestamp": "{{ISO_8601_timestamp}}",
  "task": "{{short_task_label_or_omit}}",
  "artifacts": ["{{artifact_path_1}}"],

  "artifacts_count": {{integer_or_omit}},
  "commit_hash": "{{git_hash_or_omit}}",
  "error_code": "{{short_error_code_or_omit}}",
  "message": "{{short_message_or_omit}}",

  "progress_pct": {{0_to_100_or_omit}}
}
```
## Derivation Notes
1. The first four fields are the required minimum contract from SCHEMA.md
2. All remaining fields are optional extensions from SCHEMA.md
3. Omit absent optional fields instead of filling with placeholder strings
4. Keep the payload atomic: no instructions, no routing logic, no nested plans

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | signal construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Builder Context

This ISO operates within the `signal-builder` stack, one of 125
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
| [[bld_manifest_memory_type]] | upstream | 0.53 |
| [[bld_output_template_builder]] | sibling | 0.45 |
| [[bld_config_memory_type]] | downstream | 0.43 |
| [[bld_tools_memory_type]] | upstream | 0.39 |
| [[bld_examples_signal]] | downstream | 0.37 |
| [[bld_config_tagline]] | downstream | 0.37 |
| [[bld_config_signal]] | downstream | 0.36 |
| [[bld_tools_agent]] | upstream | 0.35 |
| [[p10_lr_input_schema_builder]] | downstream | 0.34 |
| [[bld_knowledge_card_signal]] | downstream | 0.33 |
