---
id: p08_dm_n03_leverage_v2_verification
kind: decision_record
8f: F4_reason
title: "N03 LEVERAGE_MAP_V2: Builder Linter Verification + Next Builds"
version: 1.1.0
quality: 9.1
pillar: P08
mission: LEVERAGE_MAP_V2
nucleus: n03
iteration: 4
date: 2026-04-15
author: n03
tags: [n03, leverage_map_v2, builder_linter, verification, audit]
tldr: "Verified cex_builder_linter.py is present and catches structural builder defects, but it does not enforce full 8F compliance. Current repo state: 259 builder directories linted, 259 pass."
density_score: 0.94
related:
  - leverage_map_v2_verify_2026_04_15
  - bld_architecture_kind
  - kind-builder
  - bld_collaboration_kind
  - bld_collaboration_builder
  - bld_knowledge_card_kind
  - bld_collaboration_validation_schema
  - bld_config_kind
  - bld_schema_kind
  - bld_knowledge_card_builder
---

# N03 LEVERAGE_MAP_V2 Verification

## 8F Trace

```text
F1 CONSTRAIN: mission=LEVERAGE_MAP_V2, deliverable=verification decision record, target=n03 report artifact
F2 BECOME: loaded N03 builder rules, 8F protocol, N03 agent docs, and active handoff
F3 INJECT: inspected live linter/tooling files, counted builder dirs, and compared existing report against repo state
F4 REASON: verify actual linter coverage first, then separate structural guarantees from semantic gaps
F5 CALL: ran builder linter in normal and strict modes, enumerated builder dirs, checked related tools, prepared report update
F6 PRODUCE: refreshed verification report with current facts, gaps, and prioritized next builds
F7 GOVERN: report frontmatter complete, facts grounded in live command output, no unsupported self-scoring
F8 COLLABORATE: save report, compile report, emit runtime completion signal
```

## Verification

`_tools/cex_builder_linter.py` is present and executable.

Live verification from this repo state:

| Check | Result |
|-------|--------|
| `_tools/cex_builder_linter.py` present | YES |
| `python _tools/cex_builder_linter.py` | `259 PASS, 0 FAIL` |
| `python _tools/cex_builder_linter.py --strict` | `259 PASS, 0 FAIL` |
| Directories under `archetypes/builders/` | 261 |
| Directories matching `*-builder` | 259 |
| Non-builder dirs skipped by linter | `compiled`, `_shared` |

Conclusion: the tool is added, wired, and does catch real structural builder issues of the type it is designed to check.

It is sufficient for:

- missing required ISO families (`bld_manifest_`, `bld_instruction_`, `bld_system_prompt_`)
- builder folders with fewer than 13 `bld_*.md` files
- missing frontmatter
- missing frontmatter keys: `id`, `kind`, `title`, `version`
- body length under strict mode

It is not sufficient for full "8F compliance" despite the docstring claim. The implementation does not validate:

- all 13 ISO names exactly
- cross-ISO consistency
- section-level 8F expectations inside ISO bodies
- kind or pillar alignment
- quality gate semantics
- examples matching schema/template
- invalid builders with extra duplicate ISO files

The strongest proof of that gap is `_builder-builder`, which passes with `26` ISO files because the linter only rejects counts below `13`, not counts different from `13`.

## New Wired Tools Since V1

These tools are already in the repo and should be treated as wired, not missing:

| Tool | Status | Evidence |
|------|--------|----------|
| `cex_builder_linter.py` | NEW and working | full-suite pass on 259 builders |
| `cex_schema_hydrate.py` | already wired | hydrates universal schema/frontmatter fields across builders |
| `cex_materialize.py` | already wired | generates builder sub-agent scaffolds from `.cex/kinds_meta.json` |
| `cex_system_test.py` | already wired | system-level validation harness including builder checks |

Correction to the prior framing:

- schema auto-gen is not missing; the current gap is stronger schema-contract enforcement
- scaffold CLI is not missing; the current gap is builder archetype scaffold coverage and exactness
- test harness is not missing; the current gap is builder-specific semantic validation, not existence of tests

## Still Missing

The leverage gap is no longer "do these tools exist?" The gap is "do they prove builders are valid beyond surface structure?"

### 1. Exact ISO Contract Validator

Need a validator that enforces:

- exactly 13 canonical ISO files per builder
- no duplicates or alternate names
- required file names by kind
- expected section headers per ISO type

Why it matters: current linter allows `_builder-builder` to pass with 26 ISO files, which means over-generation and contract drift are invisible.

### 2. Builder Semantics Validator

Need cross-file checks such as:

- manifest role/capabilities align with instruction flow
- schema fields match output template placeholders
- examples satisfy schema
- quality gates reference actual required fields
- tools/memory/config specs do not contradict each other

Why it matters: current validation proves shape, not correctness.

### 3. 8F Compliance Scorer

Need an audit layer that scores whether a builder actually supports F1-F8, for example:

- F1: schema/constraints explicit
- F2: role/identity explicit
- F3: examples/memory/knowledge injection explicit
- F4: reasoning/planning guidance explicit
- F5: tool usage explicit
- F6: production template explicit
- F7: quality gates explicit
- F8: compile/signal/save flow explicit

Why it matters: the current linter references 8F in prose but does not inspect it in code.

## Next Iteration

Top 3 builds, prioritized:

1. Build `cex_builder_contract_validator.py`
   Purpose: enforce exact 13-file canonical ISO contract and reject duplicate/extra ISO drift.

2. Build `cex_builder_semantics_validator.py`
   Purpose: verify cross-ISO alignment between schema, template, examples, manifest, and quality gates.

3. Build `builder_8f_compliance_card.md` plus scorer support
   Purpose: formalize what 8F-complete builders must contain and score every builder against that rubric.

## Decision

The builder linter should remain in the stack. It is fast, useful, and already preventing the most common structural regressions.

But it should be positioned honestly:

- It is a structural lint pass.
- It is not a full builder validator.
- It is not an 8F compliance checker.

That distinction is the main result of this verification cycle.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[leverage_map_v2_verify_2026_04_15]] | related | 0.53 |
| [[bld_architecture_kind]] | related | 0.43 |
| [[kind-builder]] | related | 0.37 |
| [[bld_collaboration_kind]] | downstream | 0.35 |
| [[bld_collaboration_builder]] | downstream | 0.32 |
| [[bld_knowledge_card_kind]] | upstream | 0.31 |
| [[bld_collaboration_validation_schema]] | upstream | 0.29 |
| [[bld_config_kind]] | downstream | 0.28 |
| [[bld_schema_kind]] | upstream | 0.28 |
| [[bld_knowledge_card_builder]] | upstream | 0.27 |
