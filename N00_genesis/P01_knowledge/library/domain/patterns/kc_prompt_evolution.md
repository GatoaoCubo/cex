---
id: p01_kc_prompt_evolution
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Prompt Evolution"
version: 2.0.0
created: 2026-03-31
updated: 2026-04-07
author: n07_orchestrator
domain: patterns
quality: 9.1
tags: [prompt-evolution, versioning, iteration, optimization, llm, prompt-engineering]
tldr: "Version prompts like code. Measure per-version metrics, apply targeted fixes per pass, promote only on metric gain."
when_to_use: "When prompt output quality degrades, a new model drops, or A/B tests show regression"
keywords: [prompt-evolution, versioning, iteration, optimization, semantic-diff]
density_score: 0.93
related:
  - p01_kc_iterative_refinement_skill
  - p03_prompt_version
  - p01_kc_prompt_version
  - bld_collaboration_prompt_version
  - p07_regression_check
  - bld_collaboration_few_shot_example
  - bld_examples_prompt_version
  - p10_lr_action-prompt-builder
  - bld_knowledge_card_prompt_version
  - p01_kc_prompt_engineering_best_practices
---

# Prompt Evolution

## Core Principle

Treat prompts as versioned artifacts. Each version maps to a measurable outcome. Promote only when metrics improve.

## Evolution Lifecycle

```
v1.0 (initial) -> deploy -> measure -> v1.1 (fix) -> deploy -> measure -> v2.0 (structural)
```

## Version Types

| Type | When | Scope | Example |
|------|------|-------|---------|
| Patch (1.0.x) | Output drift, minor regressions | Wording, few-shot swap | Fix hallucinated dates by adding "cite source" |
| Minor (1.x.0) | New edge case, model update | Section add/remove, constraint | Add guard rail for empty input |
| Major (x.0.0) | Strategy shift, audience change | Full rewrite | Switch from chain-of-thought to tool-use |

## Measurement Framework

| Metric | How to capture | Threshold |
|--------|---------------|-----------|
| Task accuracy | Golden test pass rate | >= 90% |
| Hallucination rate | Source-vs-output diff | < 5% |
| Token efficiency | Output tokens / useful tokens | >= 0.80 |
| Format compliance | Schema validation pass | 100% |
| Latency | Time-to-first-token | < baseline * 1.2 |

## Evolution Passes (per version bump)

| Pass | Target | Action |
|------|--------|--------|
| 1 | Failure modes | Collect failures, classify root cause |
| 2 | Constraint tightening | Add explicit "do NOT" or format rules |
| 3 | Example refresh | Replace weak few-shots with edge-case examples |
| 4 | Structure change | Reorder sections, split/merge instructions |
| 5 | Model-specific tuning | Adjust for new model capabilities or quirks |

## Anti-Patterns

- **No baseline**: evolving without metrics = random drift
- **Big-bang rewrite**: changing everything at once hides what helped
- **Copy-paste inheritance**: forking prompts instead of versioning = divergence
- **Metric gaming**: optimizing token count at the cost of accuracy

## CEX Integration

| Concept | CEX artifact |
|---------|-------------|
| Prompt source | `P03_prompts/` .md files |
| Version tracking | Frontmatter `version` + git history |
| Metric capture | `cex_score.py` + `.cex/experiments/results.tsv` |
| Regression gate | `quality_gate` artifact (P07) |
| Automated evolution | `cex_evolve.py` (keep/discard loop) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_iterative_refinement_skill]] | sibling | 0.27 |
| [[p03_prompt_version]] | downstream | 0.22 |
| [[p01_kc_prompt_version]] | sibling | 0.22 |
| [[bld_collaboration_prompt_version]] | downstream | 0.21 |
| [[p07_regression_check]] | downstream | 0.21 |
| [[bld_collaboration_few_shot_example]] | downstream | 0.21 |
| [[bld_examples_prompt_version]] | downstream | 0.20 |
| [[p10_lr_action-prompt-builder]] | downstream | 0.20 |
| [[bld_knowledge_card_prompt_version]] | sibling | 0.20 |
| [[p01_kc_prompt_engineering_best_practices]] | sibling | 0.20 |
