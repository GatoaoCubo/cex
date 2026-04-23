---
id: simplify
kind: instruction
pillar: P08
description: "Review and fix changed code for reuse, quality, efficiency. Usage: /simplify [path]"
quality: 8.9
title: "Simplify"
version: "1.0.0"
author: n03_builder
tags: [instruction, command, audit, boris_merge]
tldr: "Review changed code, apply reuse/P07_evals/efficiency fixes via simplify skill."
domain: "CEX system"
created: "2026-04-15"
updated: "2026-04-15"
density_score: 0.90
related:
  - bld_collaboration_skill
  - bld_examples_skill
  - p01_kc_skill
  - bld_memory_skill
  - bld_architecture_skill
  - procedural-memory-builder
  - bld_knowledge_card_procedural_memory
  - bld_system_prompt_skill
  - spec_multi_runtime_features
  - skill-builder
---

# /simplify — Audit & Fix Changed Code

Delegates to the `simplify` skill (see `.claude/skills/simplify.md` and the
runtime-agnostic mirror `.cex/skills/simplify.md`).

## Usage

1. `/simplify` — audit `git diff HEAD` (staged + unstaged)
2. `/simplify _tools/cex_foo.py` — audit a specific file or directory
3. `/simplify --since "1 hour ago"` — audit recent commits

## Three-lens audit (from skill)

1. **Reuse**: existing helper being bypassed? Replace ad-hoc with canonical.
2. **Quality**: dead code, duplicate blocks, unnecessary nesting.
3. **Efficiency**: O(n^2) over lists, redundant I/O, serialization churn.

## Invocation

When the user types `/simplify`, invoke the skill:

```
Skill(skill="simplify", args="$ARGUMENTS")
```

## Boundaries

- Scope stays inside the diff/path given.
- No speculative abstractions (YAGNI).
- No new comments unless the WHY is non-obvious.
- Preserve public API without explicit user authorization.

## Verification

After each fix:
1. Type-check if supported (`mypy`, `tsc`, `pyright`).
2. Run affected tests.
3. Report: `N fixes, M lines removed, 0 behavior changes`.

## Cross-runtime

- **Claude Code**: native skill + this command
- **Codex/Gemini/Ollama**: boot wrapper loads `.cex/skills/simplify.md` as context

## Output Format

Bulleted diff summary, one bullet per fix:
`path:line -- what changed, why simpler`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_skill]] | downstream | 0.32 |
| [[bld_examples_skill]] | upstream | 0.31 |
| [[p01_kc_skill]] | upstream | 0.30 |
| [[bld_memory_skill]] | downstream | 0.29 |
| [[bld_architecture_skill]] | related | 0.28 |
| [[procedural-memory-builder]] | downstream | 0.27 |
| [[bld_knowledge_card_procedural_memory]] | upstream | 0.27 |
| [[bld_system_prompt_skill]] | upstream | 0.25 |
| [[spec_multi_runtime_features]] | related | 0.24 |
| [[skill-builder]] | upstream | 0.24 |
