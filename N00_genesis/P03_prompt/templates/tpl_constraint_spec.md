---
id: p03_constraint_spec
kind: constraint_spec
8f: F1_constrain
pillar: P03
version: 1.0.0
title: "Template — Constraint Spec"
tags: [template, constraint, boundary, validation, rules]
tldr: "Defines hard boundaries for artifact production. Lists required fields, size limits, naming patterns, and content rules that the 8F pipeline enforces."
quality: 9.0
domain: "prompt engineering"
density_score: 0.82
author: "n03_builder"
created: "2026-04-07"
updated: "2026-04-07"
related:
  - bld_collaboration_constraint_spec
  - constraint-spec-builder
  - bld_examples_constraint_spec
  - p10_lr_constraint_spec_builder
  - p01_kc_constraint_spec
  - p03_sp_constraint_spec_builder
  - p11_qg_context_doc
  - bld_config_constraint_spec
  - p11_qg_boot_config
  - p08_ac_verification
---

# Constraint Spec: [CONSTRAINT_NAME]

## Purpose
[WHAT this constraint protects — data integrity, consistency, or domain boundary]

## Hard Constraints (must pass or reject)

| Constraint | Rule | Example |
|------------|------|---------|
| id_pattern | `^[a-z][a-z0-9_]{2,60}$` | `kc_python_patterns` |
| max_bytes | [4096 \| 5120 \| 6144] | Body content only |
| required_fields | [id, kind, pillar] | YAML frontmatter |
| quality_field | Must be `null` (never self-score) | `quality: null` |
| naming | [PREFIX_KIND_SLUG.md] | `kc_docker_patterns.md` |

## Soft Constraints (warn but allow)

| Constraint | Rule | Rationale |
|------------|------|-----------|
| density_score | ≥ 0.78 | Non-empty lines / total lines |
| section_count | ≥ 3 sections (`##`) | Ensures structured content |
| tldr_present | Frontmatter has `tldr:` | Enables quick scanning |
| tags_present | Frontmatter has `tags: []` | Enables search/filter |

## Scope
- **Applies to**: [specific kind \| pillar \| all artifacts]
- **Enforced by**: [cex_hooks.py \| cex_8f_runner.py F7 \| cex_doctor.py]
- **Override**: [never \| with explicit exemption in _schema.yaml]

## Validation Logic
```python
def validate(artifact: str) -> list[str]:
    issues = []
    fm = parse_frontmatter(artifact)
    if not fm: issues.append("H01: No frontmatter")
    if not re.match(ID_PATTERN, fm.get("id", "")): issues.append("H02: Bad id")
    if len(body.encode("utf-8")) > MAX_BYTES: issues.append("H06: Oversized")
    return issues
```

## Quality Gate
- [ ] At least 3 hard constraints defined
- [ ] Each constraint has an example
- [ ] Enforcement tool identified
- [ ] No conflicting constraints

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_constraint_spec]] | downstream | 0.30 |
| [[constraint-spec-builder]] | related | 0.28 |
| [[bld_examples_constraint_spec]] | downstream | 0.27 |
| [[p10_lr_constraint_spec_builder]] | downstream | 0.25 |
| [[p01_kc_constraint_spec]] | related | 0.25 |
| [[p03_sp_constraint_spec_builder]] | related | 0.24 |
| [[p11_qg_context_doc]] | downstream | 0.24 |
| [[bld_config_constraint_spec]] | downstream | 0.22 |
| [[p11_qg_boot_config]] | downstream | 0.22 |
| [[p08_ac_verification]] | downstream | 0.21 |
