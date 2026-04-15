---
id: plan_h2_completion_20260407
mission: H2_COMPLETION
created: 2026-04-07T13:00:00-03:00
author: n07_orchestrator
roadmap_ref: roadmap_cex.md
waves: 3
nuclei: [n01, n03, n04, n05]
quality: 9.1
title: "Plan H2 Completion 20260407"
version: "1.0.0"
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
updated: "2026-04-07"
density_score: 0.90
---

# Plan: H2 Completion -- Context Assembly + Doc Hygiene

## Gaps

| # | Gap | Files affected | Nucleus | Wave |
|---|-----|---------------|---------|------|
| G3 | 1302 prose-heavy artifacts | 1302 .md files | OVERNIGHT | - |
| G4 | F3 INJECT needs refactor | _tools/cex_8f_runner.py | N05 | 1 |
| G5 | {{mustache}} audit | archetypes/builders/*/bld_output_template_*.md | N04 | 1 |
| G6 | 6 stale docs | _docs/*.md | N01+N03 | 2 |

## Wave 1: Core fixes (N04 + N05 parallel)

| Nucleus | Task | Depth amplifiers | Deliverables |
|---------|------|-----------------|-------------|
| N05 | Refactor F3 INJECT to pure Python (no LLM subprocess) | Read cex_8f_runner.py (1385 lines) + cex_prompt_layers.py + cex_retriever.py + cex_skill_loader.py. Understand current F3 flow. Refactor so F3 assembles context from files only (no execute_prompt). Test with: python _tools/cex_8f_runner.py --dry-run --verbose "create landing page" | Updated cex_8f_runner.py with F3 as code |
| N04 | Audit {{mustache}} in all output templates | Read ALL bld_output_template_*.md (120 files). Check which have {{BRAND_*}} slots, which have contextual {{variables}}, which have neither. Create report + fix missing slots in top 20 most-used templates. | Audit report + 20 updated templates |

Gate: F3 --dry-run works without LLM. 20+ templates have {{mustache}} slots.

## Wave 2: Doc CRUD (N01 + N03 parallel)

| Nucleus | Task | Depth amplifiers | Deliverables |
|---------|------|-----------------|-------------|
| N01 | UPDATE: ARCHITECTURE.md, HIERARCHY.md, QUICKSTART.md | Read current state: CLAUDE.md + spec_context_assembly.md + nucleus_models.yaml + cex_doctor output. Rewrite each doc with current counts, Claude Code runtime, context assembly architecture. All structured data (tables > prose). ARCHIVE ROADMAP_CONSOLIDATED.md to _docs/_archive/ | 3 updated docs + 1 archived |
| N03 | UPDATE: NAMING_CONVENTION.md, ONBOARDING.md, PATTERN_NUCLEUS_BOOT.md | Read kinds_meta.json (naming patterns), boot/*.cmd (new pi runtime), spec_context_assembly.md (two-phase loading). Rewrite with current reality. Check PLAYBOOK.md and LLM_INSTRUCTIONS.md for staleness. | 3+ updated docs |

Gate: All docs reference correct counts (121 builders, 117 kinds, 58 tools, Claude Code runtime). All docs use "claude" as the CLI name.

## Wave 3: Overnight prose sweep

| What | How | Budget |
|------|-----|--------|
| 1302 prose-heavy artifacts | boot/overnight_h1.cmd with evolve phase targeting density | 200K tokens |
| Heuristic first (free) | cex_evolve.py sweep --target 9.0 | 0 tokens |
| Agent for stubborn ones | cex_evolve.py auto mode | remaining budget |

Gate: Prose-heavy ratio < 20% (was 37%).

## Handoff template (N07 uses this for every dispatch)

```markdown
---
from: N07
to: {NUCLEUS}
mission: H2_COMPLETION
wave: {N}
---

# Task: {title}

## Context (pre-loaded on boot)
Your deck: {nucleus_dir}/deck_{nuc}.md

## Relevant artifacts (READ before producing)
- {path_1} -- {why relevant}
- {path_2} -- {why relevant}
- {path_3} -- {why relevant}

## Task
{detailed task with depth amplifiers}

## Expected output
- File: {path}
- Kind: {kind}
- Format: structured data (tables > prose, per core purpose)

## On completion
1. Compile: python _tools/cex_compile.py {paths}
2. Verify: python _tools/cex_doctor.py
3. Commit: git add -A && git commit -m "[{NUC}] {description}"
4. Signal: python -c "from _tools.signal_writer import write_signal; write_signal('{nuc}', 'complete', 9.0)"
```
