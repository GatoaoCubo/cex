---
id: p11_qg_builder_nucleus
kind: quality_gate
pillar: P11
title: Quality Gate -- Builder Nucleus
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [quality-gate, builder, N03, validation]
tldr: 7 gates that validate every artifact before publication. HARD = instant reject. SOFT = retry allowed.
density_score: 0.92
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
