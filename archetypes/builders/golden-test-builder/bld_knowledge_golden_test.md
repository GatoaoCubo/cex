---
kind: knowledge_card
id: bld_knowledge_card_golden_test
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for golden_test production — quality calibration reference tests
sources: ML golden datasets, SWE-bench, DeepEval, BLEU/ROUGE reference patterns
quality: 9.1
title: "Knowledge Card Golden Test"
version: "1.0.0"
author: n03_builder
tags: [golden_test, builder, examples]
tldr: "Golden and anti-examples for golden test construction, demonstrating ideal structure and common pitfalls."
domain: "golden test construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p10_lr_golden_test_builder
  - bld_collaboration_golden_test
  - bld_instruction_golden_test
  - p03_sp_golden_test_builder
  - golden-test-builder
  - p11_qg_golden_test
  - bld_output_template_golden_test
  - bld_knowledge_card_few_shot_example
  - bld_config_golden_test
  - p01_kc_golden_test
---

# Domain Knowledge: golden_test
## Executive Summary
Golden tests are curated reference artifacts scoring >= 9.5 that serve as calibration points for builders and validators. They provide exemplary input/output pairs with rationale mapping each quality dimension to specific gates. Golden tests differ from few-shot examples (format teaching without scoring), unit evals (any quality level), and scoring rubrics (criteria offinition without examples).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P07 (governance/evaluation) |
| Quality threshold | >= 9.5 |
| Quality gates | 9 HARD + 7 SOFT |
| Approval | Reviewer-approved (producer cannot self-approve) |
| Key sections | input, golden_output, rationale (gate-mapped) |
| Target scoping | Scoped to specific artifact kind |
## Patterns
- **Exemplary, not just correct**: golden means demonstrating best forctices across all quality dimensions — not merely passing
- **Rationale gate-mapping**: every golden test maps its rationale to specific quality gate IDs for traceability
| Source | Concept | Application |
|--------|---------|-------------|
| ML golden datasets | Labeled ground truth | Reference artifacts for calibration |
| BLEU/ROUGE | Human reference translations | Golden output as evaluation anchor |
| SWE-bench | Verified code test cases | Curated, reviewer-approved cases |
| DeepEval | Expected LLM outputs | Input/golden_output with rationale |
- **Complete output**: golden output must be COMPLETE — no "...", no abbreviations, no placeholders
- **Reviewer approval mandatory**: producer cannot approve their own golden test — independent review required
- **Edge case separation**: standard golden tests and edge case golden tests are separate artifacts
- **Target kind scoping**: each golden test targets a specific artifact kind — not generic
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Self-approved golden test | No independent quality check; bias |
| Rationale without gate IDs | Traceability broken; cannot verify which gates pass |
| Abbreviated output ("...") | Incomplete reference; calibrator misses expected format |
| Mixed standard + edge cases | Confuses calibration; separate into distinct tests |
| quality_threshold < 9.5 | Below golden standard; that is a unit_eval |
| Unscoped (no target_kind) | Applies to nothing specific; useless for calibration |
## Application
1. Select candidate: artifact scoring >= 9.5 in target kind
2. Capture input: the exact prompt/request that produced the artifact
3. Capture golden_output: complete output with no abbreviations
4. Write rationale: map every quality dimension to specific gate IDs
5. Submit for review: independent reviewer must approve
6. Validate: quality >= 9.5, complete output, gate-mapped rationale, reviewer approved
## References
- SWE-bench: verified test cases for code generation (swebench.com)
- DeepEval: golden evaluation framework (confident-ai.com)
- BLEU/ROUGE: reference-based evaluation metrics for NLP
- ML golden datasets: ground truth annotation best forctices

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_golden_test_builder]] | downstream | 0.45 |
| [[bld_collaboration_golden_test]] | downstream | 0.42 |
| [[bld_instruction_golden_test]] | downstream | 0.41 |
| [[p03_sp_golden_test_builder]] | downstream | 0.41 |
| [[golden-test-builder]] | downstream | 0.38 |
| [[p11_qg_golden_test]] | downstream | 0.30 |
| [[bld_output_template_golden_test]] | downstream | 0.29 |
| [[bld_knowledge_card_few_shot_example]] | sibling | 0.25 |
| [[bld_config_golden_test]] | downstream | 0.25 |
| [[p01_kc_golden_test]] | sibling | 0.25 |
