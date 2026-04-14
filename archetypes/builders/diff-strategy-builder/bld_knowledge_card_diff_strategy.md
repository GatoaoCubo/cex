---
kind: knowledge_card
id: bld_knowledge_card_diff_strategy
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for diff_strategy production
quality: null
title: "Knowledge Card Diff Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [diff_strategy, builder, knowledge_card]
tldr: "Domain knowledge for diff_strategy production"
domain: "diff_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Domain Overview
The diff_strategy domain governs the logic used to identify, compute, and apply transformations between two states. It focuses on the algorithmic selection of the minimal edit script (Insert, Delete, Keep) and the reconciliation logic required to merge divergent histories.

Unlike parsing or formatting, this domain is concerned with the mathematical and structural integrity of the transformation. It encompasses the decision-making process for resolving overlaps, handling conflicts, and ensuring that a patch applied to a base version results in the intended target state, even in the presence of concurrent modifications.

## Key Concepts
| Concept | Definition | Source |
|----------|------------|--------|
| LCS | Longest Common Subsequence | Algorithm Theory |
| Edit Distance | Minimum cost of transformation | Levenshtein |
| Myers Algorithm | Greedy shortest-path diffing | Myers (1986) |
| Three-way Merge | Merge using a common ancestor | Version Control |
| Hunk | A contiguous block of changes | Unified Diff Spec
