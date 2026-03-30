---
id: n01_sr_intelligence
kind: scoring_rubric
pillar: P07
title: "Scoring Rubric for N01 Intelligence Briefs"
version: "2.0.0"
created: "2026-03-30"
updated: "2026-03-30"
author: "N01_rebuild_8F"
framework: "N01 Intelligence Brief Quality"
target_kinds: [Intelligence Brief]
dimensions_count: 4
total_weight: 100
threshold_publish: 8.0
threshold_review: 7.0
domain: "intelligence, research, analysis"
quality: null
tags: [scoring, rubric, n01, intelligence, quality, eval]
tldr: "Defines the 4-dimension scoring rubric for N01's soft quality gates: Clarity, Synthesis, Source Quality, and Actionability."
linked_artifacts:
  primary: "n01_qg_intelligence"
---

## Purpose
This scoring rubric provides a detailed, quantitative guide for evaluating the four **Soft Gates** defined in `n01_qg_intelligence`. It is used by human reviewers and LLM-as-a-judge models to ensure a consistent and objective measure of quality for all `Intelligence Brief` artifacts produced by the N01 nucleus.

## Dimensions
The final score is a weighted average of the following four dimensions, each rated on a scale of 0-10.

| Dimension                 | Weight | Score 9-10 (Excellent)                                                                       | Score 5-6 (Average)                                                                     | Score 1-2 (Poor)                                                                       |
|---------------------------|--------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **Clarity & Conciseness** | 30%    | Key judgements are sharp and instantly understandable. Language is precise. No wasted words.   | Main points are understandable but require some effort. Contains mild jargon or verbosity. | The text is confusing, ambiguous, or overly verbose. Key insights are buried.         |
| **Depth of Synthesis**    | 30%    | Connects multiple, disparate data points to reveal a novel insight not obvious from any single source. | Summarizes and groups related information from sources, but draws limited new conclusions.  | Primarily paraphrases or lists facts from sources with no new synthesis.               |
| **Source Quality**        | 20%    | Analysis is overwhelmingly based on primary, peer-reviewed, or high-authority sources.       | A mix of high- and low-quality sources is used. Over-reliance on secondary commentary.  | Analysis relies on blogs, opinion pieces, or unverified sources. Citations are weak.   |
| **Actionability**         | 20%    | Key judgements directly inform a strategic decision, highlight a clear risk, or reveal a tangible opportunity. | Insights are interesting but lack a clear "so what?" for decision-making.               | The analysis is purely descriptive and provides no basis for taking action.           |

## Scoring Calculation
The final quality score is calculated as a weighted sum:
`Score = (Clarity * 0.3) + (Synthesis * 0.3) + (Source Quality * 0.2) + (Actionability * 0.2)`

### Example
- Clarity: 9/10
- Synthesis: 8/10
- Source Quality: 7/10
- Actionability: 8/10
- **Final Score**: `(9 * 0.3) + (8 * 0.3) + (7 * 0.2) + (8 * 0.2) = 2.7 + 2.4 + 1.4 + 1.6 = 8.1`

## Tier Thresholds & Actions
This rubric maps directly to the actions defined in `n01_qg_intelligence`.
| Tier    | Score | Action                 |
|---------|-------|------------------------|
| PUBLISH | >= 8.0| `ACCEPT`               |
| REVIEW  | >= 7.0| `ACCEPT_WITH_WARNING`  |
| REJECT  | < 7.0 | `REJECT`               |
