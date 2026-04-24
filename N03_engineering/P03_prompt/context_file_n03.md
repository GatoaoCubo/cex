---
id: context_file_n03
kind: context_file
8f: F2_become
nucleus: n03
pillar: P03
mirrors: N00_genesis/P03_prompt/tpl_context_file.md
overrides:
  tone: precise, principled, no-magic
  sin_lens: SOBERBA INVENTIVA
  quality_threshold: 9.3
  density_target: 0.90
  scope: repo-root
  injection_point: session_start
  applies_to_nuclei: [n03]
scope: repo-root
injection_point: session_start
max_bytes: 8192
priority: 0
applies_to_nuclei: [n03]
version: 1.0.0
quality: 8.5
tags: [mirror, n03, engineering, hermes_assimilation, context_file, agents_md]
tldr: "N03 repo-root context file (AGENTS.md/CLAUDE.md pattern): axiom-first rules for engineering sessions."
created: "2026-04-18"
related:
  - p03_sp_engineering_nucleus
  - p03_sp_n03_creation_nucleus
  - p03_sp_system-prompt-builder
  - agent_card_engineering_nucleus
  - p03_sp_kind_builder
  - p12_dr_software_project
  - p12_dr_builder_nucleus
  - bld_knowledge_card_system_prompt
  - p01_kc_creation_best_practices
  - p03_sp_workflow-builder
density_score: 1.0
updated: "2026-04-22"
---

## Axioms

1. Context files are the first thing an engineering agent reads -- every rule here must survive cold boot.
2. Rules are imperative ("ALWAYS X", "NEVER Y"), not suggestions.
3. Scope is repo-specific: override N00 universal rules, never contradict them.

## Build Rules (N03 Engineering)

1. ALWAYS run 8F pipeline before producing any artifact.
2. ALWAYS set `quality: null` -- peer review assigns the score.
3. ALWAYS compile after write: `python _tools/cex_compile.py {path}`.
4. NEVER skip F7 GOVERN -- quality gates are non-negotiable.
5. NEVER produce combined artifacts -- one kind per file.

## Anti-Patterns

| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| Undeclared side effects | Hidden state corrupts downstream | Declare in frontmatter or don't do it |
| Implicit imports in context | Circular dependency at session_start | Enumerate explicit dependency list |
| Rules as prose | Ambiguity → inconsistent execution | Table or numbered list only |
| Over-scoped context file | Pollutes unrelated sessions | Scope to `applies_to_nuclei: [n03]` |

## Usage (AGENTS.md pattern)

```markdown
<!-- AGENTS.md at repo root -- loaded by N03 at session_start -->
## Engineering Rules
See: N03_engineering/P03_prompt/context_file_n03.md
Injection: automatic via cex_hooks_native.py session-start
```

## Integration

- Upstream: `cex_hooks_native.py session-start` loads this file into N03 context
- Downstream: all N03 artifact builds inherit these rules
- Override: per-repo `AGENTS.md` or `CLAUDE.md` can extend but not contradict

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_engineering_nucleus]] | related | 0.31 |
| [[p03_sp_n03_creation_nucleus]] | related | 0.31 |
| [[p03_sp_system-prompt-builder]] | related | 0.25 |
| [[agent_card_engineering_nucleus]] | upstream | 0.23 |
| [[p03_sp_kind_builder]] | related | 0.23 |
| [[p12_dr_software_project]] | downstream | 0.23 |
| [[p12_dr_builder_nucleus]] | downstream | 0.22 |
| [[bld_knowledge_card_system_prompt]] | related | 0.21 |
| [[p01_kc_creation_best_practices]] | upstream | 0.20 |
| [[p03_sp_workflow-builder]] | related | 0.20 |
