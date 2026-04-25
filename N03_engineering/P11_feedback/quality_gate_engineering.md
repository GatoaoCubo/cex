---
id: p11_qg_builder_nucleus
kind: quality_gate
8f: F7_govern
pillar: P11
title: Quality Gate -- Builder Nucleus
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [quality-gate, builder, N03, validation]
tldr: "7 gates at F7 GOVERN: H01 frontmatter integrity [HARD], H02 kind match [HARD], H03 naming convention [WARN], H04 reference resolution [WARN], H05 density >= 0.80 [SOFT], H06 size <= max_bytes [SOFT], H07 schema compliance [HARD]. 4 tiers: GOLDEN >= 9.5, PUBLISH >= 8.0, REVIEW >= 7.0, REJECT < 7.0."
density_score: 0.92
related:
  - p11_qg_kind_builder
  - p07_qg_12_point_validation
  - p03_sp_verification_agent
  - bld_examples_cli_tool
  - p01_kc_artifact_quality_evaluation_methods
  - p11_qg_quality_gate
  - bld_instruction_kind
  - p11_qg_creation_artifacts
  - bld_examples_glossary_entry
  - p11_qg_artifact
---

# Quality Gate: Builder Nucleus

## Purpose
Every artifact produced by the 8F pipeline passes through these 7 gates
at Step 8 (F7 GOVERN). No artifact reaches publication without passing.

## Gates

### H01: Frontmatter Integrity [HARD FAIL]
- Valid YAML between --- delimiters
- Required fields present: id, kind, pillar, title, version, created, updated, author, quality, tags, tldr
- No duplicate keys
- id follows naming convention from kinds_meta.json

### H02: Kind Match [HARD FAIL]
- Frontmatter kind field matches the requested kind
- kind exists in .cex/kinds_meta.json
- pillar matches the pillar registered for that kind

### H03: Naming Convention [WARN]
- Filename follows {{pillar}}_{{kind}}_{{topic}}.md pattern
- id field follows same pattern
- Topic slug is lowercase, hyphenated or underscored

### H04: Reference Resolution [WARN]
- All [[wikilinks]] resolve to existing files
- All file paths mentioned exist in the repo
- Cross-references to other kinds use correct naming

### H05: Density Check [SOFT FAIL]
- content_lines / total_lines >= 0.80
- No lorem ipsum, no placeholder text, no Planned markers
- Every section has substantive content

### H06: Size Constraint [SOFT FAIL]
- Total bytes <= max_bytes from kinds_meta.json
- If exceeded: retry with instruction to compress (remove redundancy, tighten prose)
- Max 2 retries before escalating to HARD FAIL

### H07: Schema Compliance [HARD FAIL]
- All fields from _schema.yaml frontmatter_required are present
- Field types match expected (string, int, list, etc.)
- Constraints from schema (density_min, quality_min) are met

## Severity Matrix

| Severity | Action | Retry? | Gates |
|----------|--------|--------|-------|
| HARD FAIL | Reject immediately, log error | No | H01, H02, H07 |
| SOFT FAIL | Return to F6 with issues | Yes (max 2) | H05, H06 |
| WARN | Log warning, allow publication | N/A | H03, H04 |

## Thresholds

| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Publish as reference example |
| PUBLISH | >= 8.0 | Standard publication |
| REVIEW | >= 7.0 | Needs manual review |
| REJECT | < 7.0 | Redo from scratch |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_kind_builder]] | sibling | 0.31 |
| [[p07_qg_12_point_validation]] | sibling | 0.30 |
| [[p03_sp_verification_agent]] | upstream | 0.30 |
| [[bld_examples_cli_tool]] | upstream | 0.29 |
| [[p01_kc_artifact_quality_evaluation_methods]] | upstream | 0.29 |
| [[p11_qg_quality_gate]] | sibling | 0.28 |
| [[bld_instruction_kind]] | upstream | 0.28 |
| [[p11_qg_creation_artifacts]] | sibling | 0.27 |
| [[bld_examples_glossary_entry]] | upstream | 0.27 |
| [[p11_qg_artifact]] | sibling | 0.27 |
