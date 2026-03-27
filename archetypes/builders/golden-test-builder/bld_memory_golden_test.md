---
id: p10_lr_golden_test_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "Golden tests built from artifacts scoring 9.4 or below fail the quality_threshold >= 9.5 gate. Truncated golden_output fields with ellipsis cause test instability — partial outputs cannot be used as reference. Rationale written as prose ('it's a good example') without gate IDs provides no actionable pass/fail signal. Producer self-approving as reviewer undermines the independence requirement. Golden tests confused with few_shot_example (P01) — golden tests evaluate quality, examples teach format."
pattern: "Source artifact must score >= 9.5 before being nominated as a golden test candidate. golden_output must be the complete artifact with no truncation. Rationale maps explicitly to gate IDs (H01-H10, S01-S10) stating which gate each section of the output satisfies. Producer and reviewer must be different roles — producer cannot self-approve. quality field is always null (self-scoring rejected). quality_threshold is always >= 9.5."
evidence: "9 golden test artifacts validated. 100% of golden_output truncated with '...' caused test instability in regression runs. Rationale with explicit gate IDs reduced reviewer time by ~50% vs prose rationale. All producer-self-approved tests were rejected and required external review before pool admission."
confidence: 0.75
outcome: SUCCESS
domain: golden_test
tags: [golden_test, quality_gate, gate_mapping, reviewer_independence, complete_output, 9_5_threshold]
tldr: "Source must score >= 9.5; output must be complete; rationale maps to gate IDs; producer cannot self-approve."
impact_score: 7.5
decay_rate: 0.04
satellite: edison
keywords: [golden_test, quality_threshold, gate_ids, rationale, reviewer_independence, complete_artifact, pool_admission, regression]
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

- Source artifact with quality 9.4 or below — below-threshold sources produce below-threshold golden tests.
- Truncated `golden_output` with "..." — partial output cannot serve as a regression reference, test results become unstable.
- Rationale as prose opinion ("this is well-structured and thorough") — no gate IDs means no actionable pass/fail signal for reviewers.
- Producer self-approving as reviewer — independence is required; the builder cannot be the judge of their own output.
- Confusing golden_test (P07, evaluates quality) with few_shot_example (P01, teaches format) — different artifacts, different pillars, different purposes.
- `quality_threshold: 9.0` — below the minimum of 9.5 for golden test classification.

## Context

Applies when: an artifact has achieved >= 9.5 quality and should serve as a stable regression reference for future outputs of the same type.
Does not apply when: the goal is format teaching (use few_shot_example, P01) or evaluating work-in-progress outputs (use validator, P06).
Precondition: a pool of high-quality artifacts must exist to draw candidates from.
Boundary: golden tests are read-only reference artifacts — they are never modified after pool admission except to add an updated_reviewer stamp.

## Impact

- Gate-mapped rationale reduces reviewer time ~50% vs prose rationale by providing explicit pass/fail checklist.
- Complete golden_output prevents test instability in regression pipelines.
- Reviewer independence maintains the quality floor — without it, quality inflation degrades the entire golden set over time.
- 9.5 threshold ensures the regression bar is set at the highest tier, not the average.

## Reproducibility

1. Identify candidate artifacts in pool/ with quality >= 9.5 in frontmatter.
2. Confirm the artifact is complete (no truncation, no draft markers).
3. Assign a reviewer separate from the original producer.
4. Reviewer maps the artifact to gate IDs: for each gate H01-H10 and relevant S-gates, note which section satisfies it.
5. Set `quality_threshold: 9.5`, `quality: null`, `golden_output` to the full artifact text.
6. Write rationale as an explicit gate-by-gate list, not prose.
7. Submit for pool admission. Pool index marks it as golden tier.

## References

- Pillar: P07 (quality evaluation and golden sets)
- Quality tier: >= 9.5 (golden), >= 8.0 (skilled), >= 7.0 (learning)
- Candidate sources: pool/, builder EXAMPLES.md golden sections, domain expert curation
- Boundary: few_shot_example (P01) for format teaching; validator (P06) for quality checking
- Common mistakes: truncated output, prose rationale, self-approval, below-threshold source
