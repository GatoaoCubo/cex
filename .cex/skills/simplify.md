---
name: simplify
description: Review changed code for reuse, quality, and efficiency, then fix any issues found.
runtime_agnostic: true
invoked_by: [claude, codex, gemini, ollama]
activation:
  triggers: ["/simplify", "simplify this", "clean this up", "reduce complexity"]
  nuclei: [N03, N05]
  depth: full
mirror_of: .claude/skills/simplify.md
---

# simplify — reuse, quality, efficiency audit

Review code the user just changed (or a specified path), find simplifications, apply them.

## Scope

Default target: `git diff HEAD` (staged + unstaged). If user gives a path, target that.

## Three-lens audit

1. **Reuse**: Is there an existing helper/pattern being bypassed?
   - Grep for similar signatures in `_tools/`, `cex_sdk/`, nearest utility module.
   - Replace ad-hoc code with the canonical helper.
2. **Quality**: Delete unused variables, dead branches, speculative try/except. Flatten nested conditionals where early-return wins.
3. **Efficiency**: O(n^2) over lists that should be sets/dicts. Repeated I/O where batching is trivial. Unnecessary serialization round-trips.

## Boundaries

- Do NOT refactor beyond the diff's scope unless user asks.
- Do NOT add abstractions "for the future" — YAGNI.
- Do NOT add WHAT-comments — only WHY when non-obvious.
- Preserve public API unless user authorized a break.

## Verification

After each fix: type-check, run affected tests, report N fixes / M lines removed / 0 behavior changes.

## Output

Bulleted diff summary. Each bullet: `path:line -- what changed, why simpler`.
