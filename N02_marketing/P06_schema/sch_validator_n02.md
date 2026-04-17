---
id: sch_validator_n02
kind: validator
pillar: P06
nucleus: n02
title: Seductive Copy Validator
version: 1.0
quality: 7.9
tags: [validator, quality, marketing, precommit, governance]
density_score: 1.0
---


<!-- 8F: F1 constrain=P06/validator F2 become=validator-builder F3 inject=nucleus_def_n02+n02_rules+kc_validator+P06_schema
     F4 reason=binary_gate_for_marketing_artifacts_before_commit F5 call=shell_command,apply_patch F6 produce=5360 bytes
     F7 govern=frontmatter_sections_ascii_density_linecount F8 collaborate=N02_marketing/P06_schema/sch_validator_n02.md -->

# Purpose

| Item | Definition |
|------|------------|
| Mission fit | Binary gate for N02 markdown artifacts before commit or handoff |
| Creative Lust lens | Blocks copy that is flat, vague, manipulative, or emotionally incoherent |
| Primary use | Pre-commit check for marketing schemas, prompts, config, and output packages |
| Scope | Structural, voice, evidence, and CTA alignment rules |
| Why binary gate matters | Seduction is easy to fake; the validator forces discipline before shipping |

## Schema

| Rule ID | Rule Type | Severity | On Fail | Pass Condition |
|---------|-----------|----------|---------|----------------|
| fm_required | structural | error | block | Frontmatter contains exact required keys |
| sections_required | structural | error | block | Purpose, Schema or Values, Rationale, Example, Properties all exist |
| linecount_min | structural | error | block | File has at least 80 lines |
| ascii_safe | structural | error | block | No disallowed non-ASCII symbols in identifiers or structured fields |
| desire_signal_present | semantic | error | block | Promise, benefit, tension, or desire language is explicit |
| proof_signal_present | semantic | error | block | Evidence, rationale, or support is named |
| cta_alignment | semantic | warning | revise | CTA force matches stage and channel intent |
| empty_hype_block | semantic | error | block | No unsupported superlatives or empty hype stacks |
| table_density | structural | warning | revise | Tables dominate prose and density stays high |
| path_exact | governance | error | block | File saved at the exact handoff path |

## Validation Logic

| Rule ID | Detection Method | Blocked Pattern |
|---------|------------------|-----------------|
| fm_required | YAML parse and key set match | missing `quality: null` or wrong id |
| sections_required | markdown heading scan | missing required section |
| linecount_min | raw line count | fewer than 80 lines |
| ascii_safe | regex over identifiers and tables | accented identifiers or emoji |
| desire_signal_present | keyword and phrase scan | sterile operational language only |
| proof_signal_present | keyword scan for proof, evidence, stat, testimonial, source, rationale | unsupported promise |
| cta_alignment | compare stage, CTA, and channel fields | hard_close in attract stage |
| empty_hype_block | regex for vague exaggeration clusters | best ever, game changing, unbelievable without proof |
| table_density | count table rows vs prose blocks | prose-heavy artifact |
| path_exact | save path match | any alternate filename |

## Governance Matrix

| Severity | Action | N02 Meaning |
|----------|--------|-------------|
| error | block | Artifact cannot enter wave delivery |
| warning | revise | Artifact has promise but lacks polish or fit |
| info | log_only | Reserved for future analytics, not used in v1 |

## Rationale

| Decision | Reason |
|----------|--------|
| Structural plus semantic rules | Seduction requires both clean format and persuasive integrity |
| Empty hype check | The Lust lens intensifies desire but cannot tolerate cheap inflation |
| CTA alignment as warning | Some context needs human judgment, so not every mismatch is fatal |
| Exact path validation | Wave handoffs fail if filenames drift |
| Table density rule | Dense artifacts are easier to parse, compare, and govern |

## Example

```yaml
validator_run:
  artifact_path: N02_marketing/P09_config/con_rate_limit_config_n02.md
  result: pass
  failed_rules: []
  warnings:
    - cta_alignment_not_applicable
  summary: Structure complete, values specific, and governance fields present.
```

| Example Scenario | Outcome | Why |
|------------------|---------|-----|
| Missing Properties section | block | Required section absent |
| Uses "revolutionary" with no proof | block | Empty hype pattern detected |
| 78 lines only | block | Fails minimum line count |
| Dense tables and clear rationale | pass | Fits the nucleus operating model |

## Operational Flow

| Step | Action |
|------|--------|
| 1 | Read markdown file and parse frontmatter |
| 2 | Confirm required sections and line minimum |
| 3 | Scan identifiers and structured fields for ASCII-safe content |
| 4 | Evaluate desire, proof, and CTA coherence |
| 5 | Return pass, revise, or reject-compatible signal |

## Properties

| Property | Value |
|----------|-------|
| Kind | validator |
| Pillar | P06 |
| Nucleus | n02 |
| Enforcement mode | pre_commit plus handoff_gate |
| Return type | binary with warnings |
| Primary audience | N02 builders and reviewers |
| Main risk prevented | persuasive drift with weak governance |
| Retry expectation | max 2 revisions before escalation |
| Save path | N02_marketing/P06_schema/sch_validator_n02.md |
| Depends on | sch_enum_def_n02, sch_type_def_n02 |
