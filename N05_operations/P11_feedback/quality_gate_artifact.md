---
id: p11_qg_artifact
kind: quality_gate
8f: F7_govern
pillar: P11
title: "Gate: Artifact Quality Validation"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n05_operations
domain: artifact-quality-operations
quality: 8.9
tags: [quality_gate, artifact, operations, N05, frontmatter, compilation]
tldr: "Artifact quality gate covering frontmatter validity, YAML compilation, density scoring, kind compliance, and cross-reference integrity."
density_score: 0.97
related:
  - p11_qg_knowledge
  - p11_qg_kind_builder
  - bld_instruction_kind
  - p11_qg_security
  - p11_qg_admin_orchestration
  - p11_qg_creation_artifacts
  - n04_qg_knowledge
  - p04_skill_verify
  - kind-builder
  - p11_qg_railway_superintendent
---

## Definition

| Property | Value |
|----------|-------|
| Metric | artifact_quality_score |
| Threshold | 0.90 |
| Operator | >= |
| Scope | All CEX artifacts (.md files with frontmatter) across all pillars and nuclei |

## Hard Gates

| gate_id | description | threshold | block |
|---------|-------------|-----------|-------|
| ART01 | Valid YAML frontmatter (parseable, no syntax errors) | 100% | true |
| ART02 | Required frontmatter fields present (id, kind, pillar, title, version) | 100% | true |
| ART03 | `kind` value exists in kinds_meta.json registry | 100% | true |
| ART04 | `quality` is null in source artifacts (peer-review assigns score) | 100% | true |
| ART05 | YAML compilation succeeds via `cex_compile.py` | 100% | true |
| ART06 | UTF-8 encoding (no cp1252, no BOM in body) | 100% | true |
| ART07 | `id` is unique across the entire CEX repository | 100% | true |
| ART08 | `pillar` matches the parent directory P{01-12}_* | 100% | true |

## Soft Gates

| gate_id | description | max_penalty | weight |
|---------|-------------|-------------|--------|
| SA01 | Content density score (meaningful content vs filler ratio) | 0.10 | 0.25 |
| SA02 | Cross-references to related artifacts are valid (linked files exist) | 0.10 | 0.20 |
| SA03 | tldr field is concise, accurate, and non-generic | 0.10 | 0.20 |
| SA04 | Tags are relevant and consistent with kind taxonomy | 0.10 | 0.15 |
| SA05 | Version follows semver and increments on edits | 0.10 | 0.10 |
| SA06 | Domain-specific content (not generic filler applicable to any nucleus) | 0.10 | 0.10 |

## Validation Commands

```bash
# ART01-02: Frontmatter validation
python _tools/cex_hooks.py --check <file>

# ART03: Kind registry check
python -c "import json; k=json.load(open('.cex/kinds_meta.json')); print('VALID' if '<kind>' in [x['kind'] for x in k] else 'INVALID')"

# ART05: Compilation
python _tools/cex_compile.py <file>

# ART06: Encoding check
python _tools/cex_sanitize.py --check <file>

# Full batch validation
python _tools/cex_doctor.py
```

## Scoring Formula

`artifact_score = (SA01 * 0.25) + (SA02 * 0.20) + (SA03 * 0.20) + (SA04 * 0.15) + (SA05 * 0.10) + (SA06 * 0.10)`

Pass condition: all hard gates pass AND `artifact_score >= 0.85`

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Exemplar artifact — reference for builders |
| >= 8.0 | PUBLISH | Ready for runtime use |
| >= 7.0 | REVIEW | Needs refinement before publish |
| < 7.0  | REJECT | Rework frontmatter, content, or structure |

## Boundary

Quality barrier with numeric score. NOT a validator (P06, technical pass/fail) nor a scoring_rubric (P07, defines criteria).


## 8F Pipeline Function

Primary function: **GOVERN**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_knowledge]] | sibling | 0.30 |
| [[p11_qg_kind_builder]] | sibling | 0.28 |
| [[bld_instruction_kind]] | upstream | 0.27 |
| [[p11_qg_security]] | sibling | 0.27 |
| [[p11_qg_admin_orchestration]] | sibling | 0.26 |
| [[p11_qg_creation_artifacts]] | sibling | 0.26 |
| [[n04_qg_knowledge]] | sibling | 0.26 |
| [[p04_skill_verify]] | upstream | 0.25 |
| [[kind-builder]] | upstream | 0.24 |
| [[p11_qg_railway_superintendent]] | sibling | 0.23 |
