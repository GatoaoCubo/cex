---
id: p06_vs_artifact_output
kind: validation_schema
8f: F1_constrain
pillar: P06
title: "Validation Schema -- Artifact Output"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 8.9
tags: [validation-schema, artifact, frontmatter, density, N03, 8F, quality-gate]
tldr: "Validation rules for every artifact produced by N03. Enforces frontmatter contract, density target, structural requirements, and kind-specific constraints at F7 GOVERN."
density_score: 0.93
updated: "2026-04-17"
related:
  - bld_instruction_input_schema
  - p11_qg_creation_artifacts
  - bld_examples_validation_schema
  - p11_qg_builder_nucleus
  - p03_sp_verification_agent
  - p06_vs_frontmatter
  - p11_qg_quality_gate
  - p01_kc_artifact_quality_evaluation_methods
  - p11_qg_input_schema
  - bld_examples_axiom
---

# Validation Schema: Artifact Output

## Purpose

Applied at **F7 GOVERN** for every artifact produced by N03.
This schema defines what makes an artifact VALID before it can be saved, compiled, and signaled.
It is the machine-readable companion to the 12LP quality checklist.

## Layer 1: Frontmatter Validation (HARD gates -- all must pass)

| Rule | Check | Error if Fail |
|------|-------|--------------|
| FM-01 | YAML frontmatter block present (--- delimiters) | MissingFrontmatterError |
| FM-02 | `id` field present and non-empty | MissingFieldError: id |
| FM-03 | `kind` field matches a value in kinds_meta.json | UnknownKindError |
| FM-04 | `pillar` field matches kind's canonical pillar | PillarMismatchError |
| FM-05 | `title` field present, length 5-120 chars | TitleLengthError |
| FM-06 | `version` matches semver pattern `\d+\.\d+\.\d+` | VersionFormatError |
| FM-07 | `quality: null` (never self-scored) | SelfScoringError |
| FM-08 | `tags` is a non-empty list | MissingTagsError |
| FM-09 | `tldr` present, length 20-300 chars | TldrLengthError |
| FM-10 | `created` matches ISO date `\d{4}-\d{2}-\d{2}` | DateFormatError |

## Layer 2: Body Validation (SOFT gates -- score against thresholds)

| Rule | Check | Weight |
|------|-------|--------|
| BD-01 | Body byte count in range [512, max_bytes for kind] | 20% |
| BD-02 | At least one H2 section heading present | 10% |
| BD-03 | density_score >= 0.85 (tables/code/structure ratio) | 15% |
| BD-04 | No placeholder text (TODO, FIXME, TBD, {{.*}}) in final output | 10% |
| BD-05 | At least one concrete example (code block, table row, or YAML block) | 15% |
| BD-06 | Cross-references use canonical path format (not colloquial names) | 10% |
| BD-07 | No duplicate sections (H2 headings unique) | 5% |
| BD-08 | No ASCII-rule violations in embedded code (.py, .ps1, .sh) | 15% |

## Layer 3: Kind-Specific Validation

Applied in addition to L1+L2 based on resolved `kind`:

### input_schema
- fields table required (columns: name, type, required, default, description)
- validation_rules section required
- examples section required

### knowledge_card
- definition section required
- application section required
- >= 3 body sections

### agent / agent_card
- capabilities list required
- tools list required
- nucleus field in frontmatter

### workflow
- steps table required
- trigger field in frontmatter

### scoring_rubric
- dimensions table required (columns: name, weight, description)
- weights must sum to 100

## Density Score Calculation

```
density_score = (structured_bytes / total_body_bytes)
structured_bytes = bytes in: tables + code_blocks + lists + yaml_blocks
threshold: >= 0.85
```

## Validation Modes

| Mode | When | Gates Applied |
|------|------|--------------|
| STRICT | Production builds (compile=true) | L1 + L2 + L3 |
| SOFT | Dry runs | L1 only |
| AUDIT | cex_doctor.py scan | L1 + L2 (no L3) |
| FAST | Signal writes | FM-01..FM-04 only |

## Pass/Fail Thresholds

| Outcome | Condition |
|---------|-----------|
| PASS | All L1 gates pass + L2 score >= 0.80 |
| WARN | All L1 gates pass + L2 score in [0.70, 0.80) |
| FAIL | Any L1 gate fails OR L2 score < 0.70 |
| RETRY | FAIL + retry_count < 2 (return to F6 PRODUCE) |
| REJECT | FAIL + retry_count >= 2 (escalate to N07) |

## Error Recovery Protocol

```
FAIL -> F6 PRODUCE retry (max 2 times)
WARN -> save artifact, log warning, continue to F8
REJECT -> write error to .cex/runtime/signals/signal_n03_fail_{timestamp}.json
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_input_schema]] | upstream | 0.34 |
| [[p11_qg_creation_artifacts]] | downstream | 0.30 |
| [[bld_examples_validation_schema]] | downstream | 0.30 |
| [[p11_qg_builder_nucleus]] | downstream | 0.30 |
| [[p03_sp_verification_agent]] | upstream | 0.29 |
| [[p06_vs_frontmatter]] | sibling | 0.29 |
| [[p11_qg_quality_gate]] | downstream | 0.28 |
| [[p01_kc_artifact_quality_evaluation_methods]] | upstream | 0.28 |
| [[p11_qg_input_schema]] | downstream | 0.28 |
| [[bld_examples_axiom]] | downstream | 0.27 |
