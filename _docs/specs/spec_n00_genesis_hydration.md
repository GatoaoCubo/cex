---
id: spec_n00_genesis_hydration
kind: constraint_spec
pillar: P06
title: "Spec -- N00 Genesis Targeted Hydration"
version: 1.0.0
created: 2026-04-25
author: n07_orchestrator
domain: knowledge_quality
quality_target: 9.0
status: SPEC
scope: N00_genesis
depends_on: null
tags: [spec, hydration, n00, genesis, kind-kcs, isos, frontmatter]
tldr: "Hydrate N00_genesis: add tldr/when_to_use to 160 kind KCs + 181 ISOs, densify 5 thin ISOs, enrich 28 kind-specific deep-dive folders."
density_score: 0.95
---

## Problem

N00_genesis holds the archetype layer -- the source of truth that every nucleus
clones from. Quality gaps here propagate to all 7 operational nuclei. Current gaps:

| Issue | Count | Impact |
|-------|-------|--------|
| Kind KCs missing `tldr:` | 153 / 309 (49%) | Retriever can't show one-line summaries |
| Kind KCs missing `when_to_use:` | 160 / 309 (52%) | Builders lack selection heuristic |
| ISOs missing `tldr:` | 181 / 3,647 (5%) | Prompt assembly has no preview |
| ISOs missing `when_to_use:` | 3,623 / 3,647 (99%) | Nearly universal gap in builder ISOs |
| Thin ISOs (<200B body) | 5 / 3,647 | Hollow instructions, builders skip them |
| kind_* deep-dive folders | 28 folders x 1 file each | Manifest only, no real content |

**Not a problem (already healthy):**
- Kind KC body size: 306/309 are >1KB (GOOD tier) -- body hydration NOT needed
- N00 P02-P12 pillars: 0 thin artifacts across 656 files
- Examples: 0 thin across 197 files

## Vision

After hydration, every kind KC has `tldr` + `when_to_use` in frontmatter.
Every ISO has `tldr`. The 5 thin ISOs get real instruction content.
This makes the archetype layer complete for downstream cloning.

## Scope Decision: What NOT to Do

The ISO `when_to_use` gap (3,623/3,647) is too large for this mission.
Adding `when_to_use` to 3,600+ ISOs would be ~3,600 LLM writes across
301 builder folders. That is a separate tooling mission (script-based injection).
This spec focuses on high-leverage targets only.

## Artifacts

### Wave 1: Kind KC Frontmatter Enrichment (160 files)

**Task:** Add `tldr:` and `when_to_use:` fields to ~160 kind KCs that lack them.
Each KC already has a rich body (>1KB). The LLM reads the body, extracts a 1-line
tldr and a when_to_use heuristic, and inserts them into frontmatter.

| Action | Scope | Kind | Est. Files | Notes |
|--------|-------|------|-----------|-------|
| ENRICH | `N00_genesis/P01_knowledge/library/kind/kc_*.md` | knowledge_card | ~160 | Add tldr + when_to_use from existing body |

**Nucleus assignment:** N04 (Knowledge Gluttony) -- frontmatter enrichment is its domain.

**Technique:** Read each KC body, generate:
- `tldr:` -- 1 sentence, <120 chars, what this kind IS
- `when_to_use:` -- 1 sentence, <150 chars, when a builder should pick this kind

**Constraint:** Never modify body content. Frontmatter-only changes.

### Wave 2: ISO tldr Enrichment (181 files)

**Task:** Add `tldr:` to the 181 ISOs that lack it. Each ISO is a builder instruction
file with a body that explains what the ISO does. Extract a 1-liner.

| Action | Scope | Kind | Est. Files | Notes |
|--------|-------|------|-----------|-------|
| ENRICH | `archetypes/builders/**/bld_*.md` (missing tldr) | builder_iso | ~181 | Add tldr from existing body |

**Nucleus assignment:** N03 (Inventive Pride) -- builder ISOs are N03's domain.

**Technique:** For each ISO missing `tldr:`, read body, generate 1-line summary.

**Constraint:** Frontmatter-only. Never touch ISO body instructions.

### Wave 3: Thin ISO Body Densification (5 files)

**Task:** The 5 ISOs with <200B body have hollow instructions. Rewrite their body
to match the density of sibling ISOs in the same builder folder.

| Action | Scope | Kind | Est. Files | Notes |
|--------|-------|------|-----------|-------|
| REWRITE | 5 thin ISOs in `archetypes/builders/` | builder_iso | 5 | Densify body using sibling ISOs as reference |

**Nucleus assignment:** N03 (Inventive Pride).

**Can be merged with Wave 2** -- same nucleus, same folder scope.

### Wave 4: kind_* Deep-Dive Manifests (28 folders) -- DEFERRED

The 28 `kind_*` folders under P01_knowledge each have a single manifest file.
These are stubs from the initial scaffolding. Real content would be per-kind
research briefs, usage guides, and pattern collections.

**Decision: DEFER.** These are low-leverage compared to Waves 1-3. Each folder
needs domain research to fill meaningfully. Better as an N01 research mission later.

## Wave Plan

```
Wave 1: N04 -- 160 kind KCs (frontmatter enrichment)
    |
    | (parallel)
    |
Wave 2+3: N03 -- 186 ISOs (181 tldr + 5 body densify)
    |
    v
Consolidate: N07 verifies, commits, runs doctor
```

**Waves 1 and 2+3 run in parallel.** No dependency between kind KCs and ISOs.
Two nuclei, ~20 minutes estimated per wave.

## Decisions (from user)

- EN-only: all content must be English
- quality: null stays null (Rule 4)
- Approach: parallel dispatch (N03 + N04 simultaneously)
- ISO when_to_use: DEFERRED (3,600 files = separate tooling mission)
- kind_* deep dives: DEFERRED (low leverage, needs research)

## Acceptance Criteria

- [ ] 0 kind KCs missing `tldr:` (currently 153)
- [ ] 0 kind KCs missing `when_to_use:` (currently 160)
- [ ] 0 ISOs with <200B body (currently 5)
- [ ] ISO tldr gap reduced from 181 to 0
- [ ] `python _tools/cex_doctor.py` passes
- [ ] `python _tools/cex_stats_inject.py --check` passes (no stale counts)
- [ ] All files compile: `python _tools/cex_compile.py --all`
- [ ] Signal sent: n03 + n04 complete

## Estimated Cost

| Wave | Nucleus | Files | Est. Time | Model |
|------|---------|-------|-----------|-------|
| 1 | N04 | ~160 | 15-20 min | Opus |
| 2+3 | N03 | ~186 | 15-20 min | Opus |
| Consolidate | N07 | -- | 5 min | -- |
| **Total** | -- | **~346** | **~25 min** | -- |

## Anti-Patterns

- DO NOT rewrite kind KC bodies (they are already >1KB GOOD tier)
- DO NOT add `when_to_use` to 3,647 ISOs (separate mission)
- DO NOT populate kind_* deep-dive folders with generic content
- DO NOT self-score quality (Rule 4)
- DO NOT touch compiled/ directories
