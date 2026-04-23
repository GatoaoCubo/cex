---
id: p08_inv_n03
kind: invariant
pillar: P08
title: "Invariants -- N03 Engineering System"
version: 2.0.0
created: 2026-04-17
updated: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 9.1
tags: [invariant, N03, system-properties, constraints, 8F, quality, correctness, f2b-speak, ubiquitous-language, coc]
tldr: "24 system invariants for N03. Properties that ALWAYS hold regardless of context, model, or runtime. v2.0 adds F2b SPEAK and ubiquitous language invariants (INV-19 through INV-24). Violation of any invariant indicates a system bug, not a feature gap."
density_score: 0.93
related:
  - p03_sp_n03_creation_nucleus
  - bld_memory_webhook
  - bld_examples_invariant
  - p03_sp_engineering_nucleus
  - bld_collaboration_quality_gate
  - p03_sp_golden_test_builder
  - p03_sp_builder_nucleus
  - skill
  - bld_examples_axiom
  - p03_sp_kind_builder
---

# Invariants: N03 Engineering System

## Purpose

Invariants are properties that ALWAYS hold. Not guidelines. Not preferences.
They are the mathematical contract of the system.
If an invariant is violated, something is fundamentally wrong.

**Inventive Pride:** a builder that violates its own contracts is not a builder -- it is noise.

## Build Pipeline Invariants

| ID | Invariant | Scope | Violation Indicates |
|----|-----------|-------|-------------------|
| INV-01 | F1 always executes before F2 | Pipeline | Bypass of intent resolution |
| INV-02 | F7 always executes before F8 | Pipeline | Unvalidated artifact saved |
| INV-03 | quality field is always null in produced artifacts | All artifacts | Self-scoring violation |
| INV-04 | 8F trace always written to stdout | Pipeline | Invisible execution |
| INV-05 | F8 compile step always runs if compile=true | Pipeline | Uncompiled artifact saved |
| INV-06 | F8 signal always sent if signal=true | Pipeline | N07 never learns of completion |

## Artifact Invariants

| ID | Invariant | Scope | Violation Indicates |
|----|-----------|-------|-------------------|
| INV-07 | Every artifact has exactly one kind | Artifact | Malformed or hybrid artifact |
| INV-08 | Every artifact's pillar matches its kind's canonical pillar | Artifact | Misfiled artifact; breaks discovery |
| INV-09 | Every artifact id is globally unique in the repo | Artifact | Duplicate; breaks indexing |
| INV-10 | density_score in frontmatter reflects actual body density | Artifact | Inflated/deflated score |
| INV-11 | created date is <= updated date when both present | Artifact | Time paradox in frontmatter |
| INV-12 | All embedded .py/.ps1 code is ASCII-only (0x00-0x7F) | Artifact | Runtime UnicodeEncodeError |

## Schema Invariants

| ID | Invariant | Scope | Violation Indicates |
|----|-----------|-------|-------------------|
| INV-13 | type_def_cex_types.md is the single source of truth for all CEX types | P06 | Type divergence between nuclei |
| INV-14 | enum_def_build_actions.md PILLAR values are fixed at P01-P12 | P06 | Pillar namespace pollution |
| INV-15 | interface_builder_protocol.md bilateral contract applies to all 259 builders | All builders | Builder without contract |

## Quality Invariants

| ID | Invariant | Scope | Violation Indicates |
|----|-----------|-------|-------------------|
| INV-16 | quality_gate_n03.md hard gates (H01-H07) are all binary (pass/fail) | P11 | Partial gate creates ambiguity |
| INV-17 | Self-improvement loop NEVER raises the quality field -- only peer review can | P11 | Self-scoring through the back door |
| INV-18 | Regression check runs AFTER every F7 GOVERN for kinds with baselines | P07 | Undetected quality rot |

## Verification Protocol

Run invariant verification:
```bash
python _tools/cex_doctor.py --invariants --nucleus n03
```

Expected output: `[OK] 30/30 invariants hold`

| Group | Count | New in v2.0 |
|-------|-------|------------|
| Build Pipeline (INV-01 to INV-06) | 6 | 0 |
| Artifact (INV-07 to INV-12) | 6 | 0 |
| Schema (INV-13 to INV-15) | 3 | 0 |
| Quality (INV-16 to INV-18) | 3 | 0 |
| Language / F2b SPEAK (INV-19 to INV-24) | 6 | +6 |
| CoC Compliance (COC-01 to COC-06) | 6 | +6 |
| **Total** | **30** | **+12** |

## Invariant Proofs (Selected)

### INV-03 Proof: quality is always null in produced artifacts

*By construction:* Every builder instruction (bld_instruction_{kind}.md) includes:
"Set quality: null -- never self-score". The quality_gate_n03.md H04 gate blocks
any artifact where quality != null. cex_score.py sets quality only when called
with `--apply` by a DIFFERENT nucleus (peer review). Therefore, artifacts produced
by N03's own F6 PRODUCE will always have quality: null.

### INV-09 Proof: globally unique ids

*By convention:* ids follow pattern `p{pillar}_{prefix}_{slug}` where `pillar`
is the 2-digit pillar number, `prefix` is the kind abbreviation (2 chars),
and `slug` is derived from the artifact title. The combination is unique because
(a) pillar+kind combination is unique for a given domain, and (b) slug is derived
from the specific artifact purpose which is unique within a builder's output.
cex_doctor.py --ids detects duplicates on every scan.

### INV-12 Proof: ASCII-only in embedded code

*By enforcement:* cex_hooks.py pre-commit hook runs cex_sanitize.py on all
staged .py and .ps1 files. The ascii-code-rule.md specifies the complete
replacement table. Any non-ASCII in staged executable code blocks FAILS the
pre-commit hook, blocking the commit.

## Language Invariants (F2b SPEAK — added v2.0)

| ID | Invariant | Scope | Violation Indicates |
|----|-----------|-------|-------------------|
| INV-19 | F2b SPEAK always executes after F2 BECOME and before F3 INJECT | Pipeline | Vocabulary not loaded; artifacts may drift from canonical terms |
| INV-20 | kc_{domain}_vocabulary.md exists before first dispatch from any nucleus | Per nucleus | F2b SPEAK has no vocabulary to load |
| INV-21 | Artifact body uses only canonical terms from kinds_meta.json + kc_vocabulary.md | All artifacts | Vocabulary drift; LLM-to-LLM communication degrades |
| INV-22 | No nucleus redefines terms declared in N00_genesis P01 KCs | Cross-nucleus | Divergent definitions break cross-nucleus search + synthesis |
| INV-23 | Handoff files use {kind, pillar, nucleus, verb} tuples for all action references | Handoffs | Ambiguous handoffs; wrong nucleus executes wrong kind |
| INV-24 | Pattern artifacts loaded as F2 BECOME ISOs follow p08_pat_8f_full_trace.md format | Pattern artifacts | Inconsistent traces break cross-nucleus comparison |

## CoC Compliance Invariants

| ID | Invariant | Scope | Violation Indicates |
|----|-----------|-------|-------------------|
| COC-01 | Every N03 artifact resides in N03_engineering/P{01-12}_*/ (no root-level exceptions) | File placement | Discovery fails; cex_doctor.py FAIL |
| COC-02 | File names follow {kind}_{domain_slug}.md convention | File naming | Builder lookup by kind returns no match |
| COC-03 | All new kinds are first registered in kinds_meta.json before artifacts are created | Kind registry | Orphan artifacts; cex_doctor.py --kinds: unregistered kind |
| COC-04 | Cross-references use relative paths (not absolute) | Artifact body | Portability breaks across machines |
| COC-05 | Pattern artifacts in P08_architecture are self-contained: no external config required to load | Pattern artifacts | CoC defeats itself if configuration is required to load a convention |
| COC-06 | The 8F pipeline trace in every artifact run matches the template in pattern_8f_full_trace.md | Pipeline execution | Inconsistent traces block automated parsing |

## Invariant Violations Log

Invariant violations are written to:
`.cex/runtime/signals/invariant_violation_n03_{timestamp}.json`

Format:
```yaml
timestamp: 2026-04-17T14:30:00
nucleus: n03
invariant_id: INV-03
artifact: N03_engineering/P06_schema/input_schema_build_contract.md
description: "quality field was set to 9.0 instead of null"
severity: HIGH
action: reverted and rebuilt
```

## Cross-References

- `N03_engineering/P08_architecture/pattern_8f_full_trace.md` — INV-04, INV-24, COC-06 source convention
- `N03_engineering/P08_architecture/pattern_nucleus_instantiation.md` — COC-01, COC-02 structural contract
- `N03_engineering/P01_knowledge/kc_engineering_vocabulary.md` — INV-19 vocabulary source
- `.claude/rules/ubiquitous-language.md` — INV-19 through INV-23 authoritative protocol
- `.claude/rules/ascii-code-rule.md` — INV-12 enforcement mechanism
- `.cex/kinds_meta.json` — COC-03 kind registry (source of truth)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.28 |
| [[bld_memory_webhook]] | upstream | 0.24 |
| [[bld_examples_invariant]] | related | 0.21 |
| [[p03_sp_engineering_nucleus]] | upstream | 0.20 |
| [[bld_collaboration_quality_gate]] | downstream | 0.18 |
| [[p03_sp_golden_test_builder]] | upstream | 0.18 |
| [[p03_sp_builder_nucleus]] | upstream | 0.18 |
| [[skill]] | related | 0.18 |
| [[bld_examples_axiom]] | upstream | 0.18 |
| [[p03_sp_kind_builder]] | upstream | 0.18 |
