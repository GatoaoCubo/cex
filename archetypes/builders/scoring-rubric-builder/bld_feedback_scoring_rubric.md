---
quality: 8.8
id: p11_fb_scoring_rubric
kind: builder_default
pillar: P11
title: "Feedback: Scoring Rubric"
domain: scoring_rubric
version: 1.1.0
tags: [feedback, anti-patterns, P11, scoring_rubric]
related:
  - p08_ac_verification
  - p10_lr_golden_test_builder
  - p03_sp_n03_creation_nucleus
  - p03_sp_system-prompt-builder
  - bld_instruction_knowledge_card
  - bld_examples_axiom
  - p03_sp__builder_builder
  - p03_sp_golden_test_builder
  - p03_sp_output_validator_builder
  - p01_kc_artifact_quality_evaluation_methods
tldr: "Anti-patterns and correction protocol for scoring rubric builders. 6 NEVER rules + 4 failure modes + 3-step correction."
author: builder
llm_function: GOVERN
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-22"
---

# Feedback: Scoring Rubric

## Anti-Patterns (NEVER do)

| Rule | Violation | Gate |
|------|-----------|------|
| No self-score | Never assign quality score to own output | H01 |
| No hallucination | Cite sources; no invented facts, metrics, refs | H03 |
| ASCII-only code | No emoji, no accented chars in .py/.ps1/.sh | H04 |
| No partial output | Complete artifact; no truncation, no "..." | H05 |
| No frontmatter omission | Every artifact starts with valid YAML frontmatter | H01 |
| No quality below 8.0 | Re-draft before publishing if self-assessment < 8.0 | H07 |

## Common Failure Modes

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| Vague identity section | No concrete capabilities, tools, or constraints | Add specifics from builder ISOs |
| Missing frontmatter fields | id, kind, pillar absent or quality not null | Add all required fields per schema |
| Body prose only | density < 0.85, no tables | Convert lists to tables |
| Output schema mismatch | Output does not match output template | Re-read bld_output ISO |

## Correction Protocol

| Step | Action | Gate |
|------|--------|------|
| 1 | Identify which H01-H07 gate failed | F7 |
| 2 | Return to F6 PRODUCE with explicit fix instruction | F6 |
| 3 | Re-run F7 GOVERN | F7 |
| 4 | Max 2 retries before escalating to N07 | F8 |

## Key Behaviors

- Builder MUST load all 12 ISOs (1:1 with pillars) before producing any artifact
- Builder MUST run F7 GOVERN quality gate before saving output
- Builder MUST compile output via cex_compile.py after saving (F8 COLLABORATE)
- Builder MUST signal completion with quality score to N07 orchestrator
- Builder MUST NOT self-score: quality field is always null in own output
## Quality Thresholds

| Dimension | Weight | Target | Gate |
|-----------|--------|--------|------|
| Structural completeness | 30% | >= 8.0 | L1 |
| Rubric compliance | 30% | >= 8.0 | L2 |
| Semantic coherence | 40% | >= 8.5 | L3 |
| Density score | -- | >= 0.85 | S09 |
| Tables present | -- | >= 1 | S05 |

## Gate Check

```bash
python _tools/cex_score.py {FILE} --layer structural
python _tools/cex_score.py {FILE} --layer rubric
```

```yaml
# Expected output structure
structural: 8.5+
rubric: 7.5+
average: 8.0+
gates_passed: 7/7
density: 0.85+
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p08_ac_verification]] | upstream | 0.23 |
| [[p10_lr_golden_test_builder]] | upstream | 0.22 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.22 |
| [[p03_sp_system-prompt-builder]] | upstream | 0.21 |
| [[bld_instruction_knowledge_card]] | upstream | 0.21 |
| [[bld_examples_axiom]] | upstream | 0.21 |
| [[p03_sp__builder_builder]] | upstream | 0.21 |
| [[p03_sp_golden_test_builder]] | upstream | 0.21 |
| [[p03_sp_output_validator_builder]] | upstream | 0.20 |
| [[p01_kc_artifact_quality_evaluation_methods]] | upstream | 0.20 |
