---
kind: examples
id: bld_examples_diff_strategy
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of diff_strategy artifacts
quality: 9.1
title: "Examples Diff Strategy"
version: "1.1.0"
author: n06_audit_hybrid_review2
tags: [diff_strategy, builder, examples]
tldr: "Golden and anti-examples of code-level diff strategy artifacts (Myers, patience, AST)"
domain: "diff_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

## Golden Example -- Myers Line Diff (Aider udiff-simple format)
```yaml
---
kind: diff_strategy
id: p04_ds_myers_line_diff
algorithm_type: Myers
granularity: line
comparison_basis: edit_distance
performance_budget: O(ND) where N = sum of lengths, D = edit distance
---
```
```
## Overview
Myers greedy diff (1986): finds the shortest edit script (SES) by treating
diff as shortest-path search on an edit graph. Each diagonal k = x - y
represents balanced insertions/deletions. Runs in O(ND) time, O(D) space.

## Patch Format
Unified diff (POSIX): 3-line context window, @@ -L,S +L,S @@ hunk headers.
Applied via: `patch -p1 < file.diff` or `git apply --3way file.diff`

## Edge Cases
| Case            | Handling                                           |
|-----------------|----------------------------------------------------|
| Empty diff      | Return identity (no hunks); exit code 0            |
| Binary file     | Detect with NUL bytes; fall back to bsdiff         |
| CRLF/LF mismatch| Normalize before diff; preserve original in output |
| Identical files | Short-circuit LCS computation; emit empty script   |
| Partial match   | Apply cleanly-patching hunks; flag conflicts       |
```

## Golden Example -- Patience Diff (structural)
```yaml
---
kind: diff_strategy
id: p04_ds_patience_structural
algorithm_type: patience
granularity: line
comparison_basis: unique_lines_LCS
---
```
```
## Overview
Patience diff (Bram Cohen, used in Bazaar/git): LCS only over unique lines.
Produces human-readable diffs for code refactors -- avoids matching braces/
blank lines that Myers would greedily consume. Git uses histogram diff as
refinement; libxdiff implements both.

## When to use
Prefer patience/histogram over Myers when:
- Code has many identical-looking lines ({, }, pass, return)
- LLM code agent must understand structural intent of a patch
- Aider "diff" format is in use (context-line matching matters)
```

## Anti-Example 1: edit_format (boundary violation)
```yaml
---
kind: edit_format   # WRONG -- this is format, not strategy
description: Aider SEARCH/REPLACE block syntax
---
```
**Why it fails**: edit_format specifies HOW changes are *serialized* (block
delimiters, line markers). diff_strategy specifies HOW changes are *computed*
(which algorithm finds the minimal edit script). These are downstream stages;
conflating them means the builder will mix syntax rules with algorithm selection.

## Anti-Example 2: parser (upstream confusion)
```yaml
---
kind: parser        # WRONG -- this is ingestion, not diff
description: Tokenize Python source into AST before diffing
---
```
**Why it fails**: Tokenization/parsing is *upstream* of diff strategy. A
diff_strategy artifact receives already-parsed tokens or lines. The parser
decides representation; diff_strategy decides comparison algorithm over that
representation. Mixing them breaks the pipeline separation enforced by the
collaboration ISO.
