---
kind: tools
id: bld_tools_diff_strategy
pillar: P04
llm_function: CALL
purpose: Tools available for diff_strategy production
quality: 9.1
title: "Tools Diff Strategy"
version: "1.1.0"
author: n06_audit_hybrid_review2
tags: [diff_strategy, builder, tools]
tldr: "Real diff tools: difflib, git apply, patch, Aider formats, libxdiff, tree-sitter"
domain: "diff_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

## Core Diff Libraries
| Tool                  | Purpose                                      | When to use                         |
|:----------------------|:---------------------------------------------|:------------------------------------|
| difflib (Python stdlib)| SequenceMatcher, unified_diff, ndiff, HtmlDiff| Line/char diff in Python agents     |
| libxdiff              | Myers + histogram diff (used inside git)     | C-level performance; git internals  |
| diff-match-patch (Google)| Bitap algorithm for fuzzy patch application| Web/JS environments; fuzzy matching |
| bsdiff/bspatch        | Binary file delta compression                | Binary assets, executables          |
| xdelta3               | Delta encoding for large binary streams      | Incremental updates, ROM patching   |

## Patch Application Tools
| Tool                  | Purpose                                      | Command / API                       |
|:----------------------|:---------------------------------------------|:------------------------------------|
| patch (POSIX)         | Apply unified diff to file tree              | `patch -p1 < file.diff`             |
| git apply             | Apply patch with git context                 | `git apply --3way --whitespace=fix` |
| git apply --3way      | Three-way merge fallback on conflict         | `git apply --3way file.diff`        |
| git merge-file        | Three-way merge of 3 versions                | `git merge-file local base remote`  |

## LLM Code-Agent Edit Formats (Aider)
| Format       | Description                                          | Best for                        |
|:-------------|:-----------------------------------------------------|:--------------------------------|
| whole         | Full file replacement                               | Small files; guaranteed apply   |
| diff          | Unified diff blocks                                 | Line-level changes; standard    |
| udiff-simple  | Simplified unified diff; no line numbers            | Reduced token count; GPT-3.5    |
| diff-fenced   | Diff wrapped in fenced code blocks                  | Models that output markdown      |

## CEX Infrastructure Tools
| Tool            | Purpose              | When                      |
|:----------------|:---------------------|:--------------------------|
| cex_compile.py  | YAML compilation     | Post-production           |
| cex_score.py    | Quality scoring      | After artifact generation |
| cex_doctor.py   | System health check  | Pre-dispatch              |
| cex_retriever.py| Similarity search    | Find similar strategies   |

## Structural (AST-level) Diff
| Tool       | Purpose                                | Notes                              |
|:-----------|:---------------------------------------|:-----------------------------------|
| tree-sitter| Parse source to AST for structural diff| Language-agnostic; 40+ languages   |
| GumTree    | AST diff (move/update/insert/delete)   | Java-origin; cross-language        |
| difftastic | Structural diff using tree-sitter      | Terminal tool; human-readable AST  |
