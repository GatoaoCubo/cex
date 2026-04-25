---
id: spec_launch
kind: decision_record
pillar: P08
title: "MISSION LAUNCH: Open-Source Release Preparation"
version: "1.0.0"
created: "2026-04-22"
updated: "2026-04-22"
author: "n07_orchestrator"
domain: "release_engineering"
quality: null
tags: [spec, launch, open-source, release, n00-genesis, prompt-compiler]
tldr: "3-wave spec to ship CEXAI: fix N00 genesis (17 artifacts), expand prompt compiler (45%->90%), create GitHub release with changelog."
density_score: 0.92
related:
  - spec_plateau
  - p03_pc_cex_universal
  - kind_manifest_n00
  - p01_kc_orchestration_best_practices
  - bld_instruction_kind
  - spec_infinite_bootstrap_loop
  - project_opensource_launch
  - CHANGELOG
  - README
  - spec_context_assembly
---

## Mission

Ship CEXAI as a credible open-source project. Three tracks, three waves, zero GDP needed (all decisions are technical, not subjective).

## Current State

| Metric | Value | Target | Gap |
|--------|-------|--------|-----|
| N00_genesis below 8.0 | 17 | 0 | 17 artifacts |
| Prompt compiler coverage | 133/293 (45%) | 264/293 (90%) | 300 kinds |
| GitHub releases | 0 | 1 (v1.0.0) | 1 release |
| Doctor FAIL | 0 | 0 | -- |
| Release check | 28/28 | 28/28 | -- |
| Quality >= 8.0 | 96.9% | 98%+ | ~30 artifacts |

## Wave 1: N00 Genesis Hardening (N03 + N04)

**Why first:** N00 is the archetype — every nucleus, pillar, kind, and builder inherits from it. A broken template propagates to 300 kinds x 12 ISOs = 3,516 artifacts.

### W1.1: Fix 17 below-8.0 artifacts (N03)

| Artifact | Quality | Pillar | Fix Strategy |
|----------|---------|--------|-------------|
| kc_legal_vertical.md | 7.1 | P01 | Expand domain facts, add industry sources |
| kc_diff_strategy.md | 7.4 | P01 | Add tables, concrete diffing algorithms |
| tpl_context_file.md | 7.4 | P03 | Enrich template with field docs |
| tpl_personality.md | 7.5 | P03 | Add persona dimensions table |
| tpl_pipeline_template.md | 7.5 | P12 | Add stage/hook/config tables |
| kind_manifest_n00.md | 7.6 | P09 | Add missing field descriptions |
| tpl_messaging_gateway.md | 7.7 | P04 | Add platform matrix |
| tpl_e2e_eval.md | 7.7 | P07 | Add assertion pattern table |
| kc_canary_config.md | 7.9 | P01 | Add deployment strategy table |
| kc_lineage_record.md | 7.9 | P01 | Add provenance chain example |
| + 7 more | 7.9 | various | Standard enrichment |

### W1.2: Audit N00 schema completeness (N04)

- Verify all 12 `P{01-12}_*/_schema.yaml` files are parseable and complete
- Cross-check schema fields against builder ISOs for drift
- Report: which schemas have fields not covered by any builder ISO?

**Dispatch:** N03 (evolve 17 artifacts) + N04 (schema audit) in parallel.

## Wave 2: Prompt Compiler Expansion (N03)

**Why second:** the prompt compiler is the intent resolution engine. At 45% coverage, 300 kinds silently fail to resolve — the user says "build X" and N07 can't map it.

### W2.1: Generate missing kind entries

300 kinds need entries in `p03_pc_cex_universal.md`. Each entry is a row in the bilingual pattern table:

```
| User says (EN) | User says (PT) | kind | pillar | nucleus |
```

**Source:** `.cex/kinds_meta.json` has all 300 kinds with pillar assignments. The missing 160 can be batch-generated from metadata + builder ISOs.

### W2.2: Validate intent resolution end-to-end

For each of the 160 newly added kinds:
1. Feed a natural-language intent through `cex_intent_resolver.py`
2. Verify it resolves to the correct `{kind, pillar, nucleus, verb}` tuple
3. Report: which kinds still fail resolution?

**Dispatch:** N03 solo (this is structural, not creative). Single deep handoff.

## Wave 3: Ship (N07 + N05)

### W3.1: GitHub Release (N07)

```bash
# Tag
git tag -a v1.0.0 -m "CEXAI v1.0.0: 300 kinds, 301 builders, 12 pillars, 8 nuclei"

# Release
gh release create v1.0.0 \
  --title "CEXAI v1.0.0 — Typed Knowledge System for LLM Agents" \
  --notes-file _docs/release_notes_v1.md \
  --latest
```

### W3.2: Release notes (N07)

Generate `_docs/release_notes_v1.md` from:
- CHANGELOG.md (summarize)
- Quality metrics (from PLATEAU)
- Showoff comparison (from _showcase/)
- Getting started pointer (examples/)

### W3.3: Verify examples/ (N05)

The 5 numbered tutorials + 3 standalone guides in `examples/` must:
- Have valid frontmatter
- Reference current tool names (not stale)
- Include expected output or success criteria
- Be runnable by a new user after `git clone`

**Dispatch:** N05 validates examples, N07 writes release notes + creates release.

## Dependencies

```
W1 (N00 genesis) ──┐
                    ├──> W3 (ship)
W2 (prompt compiler)┘
```

W1 and W2 can run in parallel. W3 depends on both completing.

## Success Criteria

| Criterion | Measurement |
|-----------|-------------|
| N00_genesis 0 below 8.0 | `cex_evolve.py sweep --scope N00_genesis` reports 0 |
| Prompt compiler >= 90% | `grep -c` kind entries in p03_pc >= 264 |
| GitHub release exists | `gh release view v1.0.0` returns 200 |
| Examples valid | N05 reports all 8 guides pass |
| Doctor 0 FAIL | `cex_doctor.py` exit 0 |
| Release 28/28 | `cex_release_check.py` exit 0 |

## Timeline

| Wave | Duration | Parallel? |
|------|----------|-----------|
| W1 | ~30 min (N03 evolve + N04 audit) | yes with W2 |
| W2 | ~45 min (160 kind entries + validation) | yes with W1 |
| W3 | ~15 min (release notes + tag + verify) | sequential after W1+W2 |
| Total | ~60 min | -- |

## GDP

None needed. All decisions are technical (schema correctness, kind resolution, release mechanics). No subjective choices (tone, audience, style) involved.
