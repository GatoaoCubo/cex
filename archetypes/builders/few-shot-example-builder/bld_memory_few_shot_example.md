---
id: p10_lr_few_shot_example_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Few-shot examples that demonstrate format teach more reliably than examples that demonstrate content. Output fields that contain prose descriptions ('a good response would include...') rather than actual format demonstrations fail to transfer format patterns. Body exceeding 1024 bytes — the tightest limit in P01 — forces cuts to explanation rather than examples. Input prompts that are vague ('write something about X') produce outputs that cannot be reused as format templates. Difficulty calibration absent from a set means all examples are easy, leaving edge cases untaught."
pattern: "The output field must show the actual format, not describe it. Input must be specific and realistic. Sequence examples easy -> medium -> hard across a set. Each pair includes an Explanation section stating exactly which format rule the output demonstrates. Body cap is 1024 bytes — trim Variations and Edge Cases before trimming the output demonstration. Never include scoring rubric or quality assessment; that belongs in golden_test (P07)."
evidence: "12 few-shot example artifacts reviewed. Output fields containing descriptions in..."
confidence: 0.70
outcome: SUCCESS
domain: few_shot_example
tags: [few_shot_example, format_teaching, difficulty_calibration, input_output_pairs, format_demonstration]
tldr: "Show format in output, not describe it. Calibrate easy->medium->hard. Stay under 1024 bytes body."
impact_score: 7.5
decay_rate: 0.04
agent_group: edison
keywords: [few_shot, format_teaching, difficulty_calibration, output_demonstration, input_specificity, edge_case, explanation]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Few Shot Example"
density_score: 0.90
llm_function: INJECT
related:
  - p03_sp_few_shot_example_builder
  - bld_instruction_few_shot_example
  - bld_manifest_memory_type
  - bld_collaboration_few_shot_example
  - few-shot-example-builder
  - p10_lr_golden_test_builder
  - bld_output_template_few_shot_example
  - p01_kc_few_shot_example
  - bld_examples_few_shot_example
  - bld_config_memory_type
---
## Summary
Few-shot examples teach a model what format to produce, not what content to generate. The output field must be an actual demonstration of the target format. Difficulty must be calibrated across a set — easy examples establish the baseline, medium ones show variation, hard ones handle edge cases. The body limit is 1024 bytes, the tightest in the P01 pillar.
## Pattern
1. The `output` field must contain the actual formatted artifact, not a description of what it should contain.
2. The `input` field must be specific and realistic — a real task someone would submit, not a placeholder.
3. Sequence examples across a set: easy (canonical request) -> medium (realistic variation) -> hard (edge case or boundary condition).
4. Every example includes an `## Explanation` section stating which specific format rule the output demonstrates and why.
5. Body cap is 1024 bytes. Trim `## Variations` and `## Edge Cases` prose sections before trimming the output itself.
6. `quality` must be null — self-scoring is rejected. Scoring belongs in golden_test (P07).
7. The `id` field value must match the filename stem exactly.
8. Tags must be a YAML list, not a string.
## Anti-Pattern
1. Output field containing prose: "a good response would have a tldr, then three bullet points..." — this teaches nothing about format.
2. Input so vague it cannot produce a consistent format demonstration: "write something about quality gates."
3. Including a scoring rubric or quality threshold — that is golden_test (P07), not few_shot_example.
4. All examples set to easy difficulty — edge cases go untaught and the model fails on boundary inputs.
5. Body over 1024 bytes — the fix is trimming prose sections, never truncating the output demonstration with "...".
6. Recursive drift: producing a few_shot_example about few_shot_examples that evaluates quality (crosses into P07).
## Context
Applies when: teaching format for any artifact type by showing concrete input/output pairs.

## Builder Context

This ISO operates within the `few-shot-example-builder` stack, one of 125
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

## Reference

```yaml
id: p10_lr_few_shot_example_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_few_shot_example_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | few_shot_example |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_few_shot_example_builder]] | upstream | 0.42 |
| [[bld_instruction_few_shot_example]] | upstream | 0.40 |
| [[bld_manifest_memory_type]] | upstream | 0.39 |
| [[bld_collaboration_few_shot_example]] | downstream | 0.38 |
| [[few-shot-example-builder]] | upstream | 0.38 |
| [[p10_lr_golden_test_builder]] | sibling | 0.37 |
| [[bld_output_template_few_shot_example]] | upstream | 0.35 |
| [[p01_kc_few_shot_example]] | upstream | 0.33 |
| [[bld_examples_few_shot_example]] | upstream | 0.33 |
| [[bld_config_memory_type]] | upstream | 0.33 |
