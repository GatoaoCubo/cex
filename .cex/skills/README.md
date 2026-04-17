---
id: cex_skills_readme
kind: context_doc
pillar: P03
version: 1.0.0
created: 2026-04-15
updated: 2026-04-15
author: n03_builder
mission: BORIS_MERGE
runtime_agnostic: true
density_score: 0.97
---

# .cex/skills/ — runtime-agnostic skill mirror

Claude Code loads `.claude/skills/*.md` natively (harness feature). Codex, Gemini, and Ollama do not. This directory mirrors the 5 native skills so every runtime can load them through its boot wrapper.

## Frontmatter contract (shared across runtimes)

```yaml
---
name: <slug>
description: <1 line trigger description>
runtime_agnostic: true
invoked_by: [claude, codex, gemini, ollama]   # who can trigger
activation:
  triggers: ["/<name>", "<natural phrase 1>", "<phrase 2>"]
  nuclei: [N00-N07]                            # all nuclei see it
  depth: full                                   # loads full body into context
mirror_of: .claude/skills/<name>.md            # canonical copy (Claude)
---
```

## How non-Claude runtimes load these

Each runtime's boot wrapper (`boot/n0x.ps1`, `boot/n0x_codex.ps1`, `boot/n0x_gemini.ps1`, `boot/n0x_ollama.ps1`) concatenates `.cex/skills/*.md` (body only, frontmatter stripped) into the system prompt at section `## Skills Available`.

Activation is string-match on triggers. When a user message contains a trigger, the runtime treats the matched skill's body as the operating protocol for that turn.

## Maintenance rule

When `.claude/skills/<name>.md` changes, update `.cex/skills/<name>.md` in the same commit. A pre-commit hook enforces this (see `_tools/cex_hooks.py::check_skill_parity`).

## Files

| Skill | Purpose |
|-------|---------|
| commit.md | CEX-aware git commit, conventional message, hook-safe |
| simplify.md | Three-lens (reuse/quality/efficiency) audit on diff |
| btw.md | Inline memory capture routing |
| verify.md | Sanitize + test + typecheck + lint chain |
| dream.md | Divergent ideation (3-5 approaches) before committing |
