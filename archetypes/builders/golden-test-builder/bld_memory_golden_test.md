---
id: p10_lr_golden_test_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Golden tests built from artifacts scoring 9.4 or below fail the quality_threshold >= 9.5 gate. Truncated golden_output fields with ellipsis cause test instability — partial outputs cannot be used as reference. Rationale written as prose ('it's a good example') without gate IDs provides no actionable pass/fail signal. Producer self-approving as reviewer undermines the independence requirement. Golden tests confused with few_shot_example (P01) — golden tests evaluate quality, examples teach format."
pattern: "Source artifact must score >= 9.5 before being nominated as a golden test candidate. golden_output must be the complete artifact with no truncation. Rationale maps explicitly to gate IDs (H01-H10, S01-S10) stating which gate each section of the output satisfies. Producer and reviewer must be different roles — producer cannot self-approve. quality field is always null (self-scoring rejected). quality_threshold is always >= 9.5."
evidence: "9 golden test artifacts validated. 100% of golden_output truncated with '...' ca..."
confidence: 0.75
outcome: SUCCESS
domain: golden_test
tags: [golden_test, quality_gate, gate_mapping, reviewer_independence, complete_output, 9_5_threshold]
tldr: "Source must score >= 9.5; output must be complete; rationale maps to gate IDs; producer cannot self-approve."
impact_score: 7.5
decay_rate: 0.04
agent_group: edison
keywords: [golden_test, quality_threshold, gate_ids, rationale, reviewer_independence, complete_artifact, pool_admission, regression]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Golden Test"
density_score: 0.90
llm_function: INJECT
related:
  - bld_manifest_memory_type
  - bld_knowledge_card_golden_test
  - bld_collaboration_golden_test
  - p03_sp_golden_test_builder
  - bld_instruction_golden_test
  - p10_lr_few_shot_example_builder
  - golden-test-builder
  - bld_config_memory_type
  - bld_tools_memory_type
  - skill
---
## Summary
A golden test is a high-quality artifact paired with gate-mapped rationale that serves as a regression anchor. Its purpose is to evaluate whether new outputs meet the same standard — not to teach format (that is few_shot_example). The source artifact must already score >= 9.5. The output must be complete. The rationale must reference specific gate IDs, not prose opinions.
## Pattern
1. Source artifact must have a documented quality score >= 9.5 before nomination as a golden test.
2. `golden_output` contains the complete artifact — no truncation, no ellipsis, no summarization.
3. `rationale` maps to explicit gate IDs: "H01: id format valid. H02: pillar prefix correct. S04: input is specific and realistic."
4. `quality_threshold` is always >= 9.5. Values below this are rejected by schema validator H07.
5. `quality` field is always null — self-scoring is rejected by H06.
6. Producer and reviewer are different roles. The engineer who built the artifact cannot be its golden test reviewer.
7. Candidates come from three sources: pool artifacts with quality >= 9.5 in metadata, builder EXAMPLES.md golden sections, or manually curated domain expert artifacts.
## Anti-Pattern
1. Source artifact with quality 9.4 or below — below-threshold sources produce below-threshold golden tests.
2. Truncated `golden_output` with "..." — partial output cannot serve as a regression reference, test results become unstable.
3. Rationale as prose opinion ("this is well-structured and thorough") — no gate IDs means no actionable pass/fail signal for reviewers.
4. Producer self-approving as reviewer — independence is required; the builder cannot be the judge of their own output.
5. Confusing golden_test (P07, evaluates quality) with few_shot_example (P01, teaches format) — different artifacts, different pillars, different purposes.
6. `quality_threshold: 9.0` — below the minimum of 9.5 for golden test classification.
## Context
Applies when: an artifact has achieved >= 9.5 quality and should serve as a stable regression reference for future outputs of the same type.

## Builder Context

This ISO operates within the `golden-test-builder` stack, one of 125
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
id: p10_lr_golden_test_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_golden_test_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | golden_test |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_manifest_memory_type]] | upstream | 0.39 |
| [[bld_knowledge_card_golden_test]] | upstream | 0.39 |
| [[bld_collaboration_golden_test]] | downstream | 0.38 |
| [[p03_sp_golden_test_builder]] | upstream | 0.38 |
| [[bld_instruction_golden_test]] | upstream | 0.37 |
| [[p10_lr_few_shot_example_builder]] | sibling | 0.34 |
| [[golden-test-builder]] | upstream | 0.33 |
| [[bld_config_memory_type]] | upstream | 0.32 |
| [[bld_tools_memory_type]] | upstream | 0.32 |
| [[skill]] | upstream | 0.31 |
