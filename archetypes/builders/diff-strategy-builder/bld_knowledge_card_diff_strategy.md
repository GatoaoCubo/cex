---
kind: knowledge_card
id: bld_knowledge_card_diff_strategy
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for diff_strategy production
quality: 9.1
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
| Concept                  | Definition                                              | Source                      |
|:-------------------------|:--------------------------------------------------------|:----------------------------|
| LCS                      | Longest Common Subsequence -- backbone of most diff algorithms | Algorithm Theory       |
| Edit Distance            | Minimum cost sequence of insert/delete/replace ops      | Levenshtein (1966)          |
| Myers Algorithm          | Greedy O(ND) shortest-path diff on edit graph           | Myers (1986) IEEE TSE       |
| Patience Diff            | LCS over unique lines only; human-readable for code     | Bram Cohen (Bazaar/git)     |
| Histogram Diff           | Patience variant; buckets lines by occurrence count     | git default since 2012      |
| Ratcliff/Obershelp       | Gestalt pattern matching; recursive longest-match       | Ratcliff & Metzener (1988)  |
| Three-way Merge          | Merge two branches using common ancestor                | GNU diff3 / git merge       |
| Hunk                     | Contiguous block of changes in unified diff output      | POSIX unified diff spec     |
| Unified Diff             | @@ -L,S +L,S @@ format; standard patch interchange     | POSIX.1-2017                |
| Context Diff             | Older !!! format; 3-line context window default         | BSD diff (pre-POSIX)        |
| SES (Shortest Edit Script)| Optimal sequence of edits from source to target        | Myers (1986)                |
| Edit Graph               | 2D grid where diagonals = match, vertical/horizontal = edits | Algorithm Theory      |

## Algorithm Complexity
| Algorithm      | Time     | Space   | Quality      | Use case                         |
|:---------------|:---------|:--------|:-------------|:---------------------------------|
| Myers          | O(ND)    | O(D)    | Minimal SES  | Default; fast for small D        |
| Patience       | O(N log N)| O(N)   | Human-readable| Code refactors with brace noise  |
| Histogram      | O(N log N)| O(N)   | Human-readable| git default; better than patience|
| Ratcliff       | O(N^2)   | O(N)   | Gestalt score| Python difflib SequenceMatcher   |
| LCS (DP)       | O(NM)    | O(NM)  | Optimal      | Small files; reference baseline  |

## Real Tool Integrations
| Tool             | Algorithm        | Integration Point                  |
|:-----------------|:-----------------|:-----------------------------------|
| git diff         | histogram (default)| `git diff --diff-algorithm=...`  |
| difflib          | Ratcliff-Obershelp| `SequenceMatcher`, `unified_diff` |
| patch / git apply| Any unified diff | Applies SES to target file         |
| Aider whole      | N/A (full replace)| Replaces entire file content       |
| Aider diff       | Myers-based      | Context-line patch blocks          |
| Aider udiff-simple| Myers lite      | Stripped unified diff; fewer tokens|
| Aider diff-fenced| Myers-based      | Markdown fenced block wrapping     |
| difftastic       | tree-sitter AST  | Structural diff; language-aware    |
