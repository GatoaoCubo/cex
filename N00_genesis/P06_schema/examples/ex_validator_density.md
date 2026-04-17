---
id: ex_validation_rule_density
kind: validation_rule
pillar: P06
title: "Example — Density Validation Rule"
tags: [schema, validation, density, constraint, quality]
tldr: "Validates artifact content density: ratio of non-empty lines to total lines must be >= 0.78. Prevents empty stubs from passing quality gates."
references:
  - tpl_validation_rule
  - bld_schema_validator
quality: 9.0
---

# Density Validation Rule

## Rule Definition
```yaml
id: vr_density
kind: validation_rule
field: body
metric: density_score
operator: gte
threshold: 0.78
severity: warn    # WARN, not ERROR — allows override
```

## Calculation
```python
def calculate_density(content: str) -> float:
    lines = content.split("\n")
    if not lines: return 0.0
    non_empty = [l for l in lines if l.strip()]
    return len(non_empty) / len(lines)
```

## Why 0.78?
| Density | Meaning | Example |
|---------|---------|---------|
| < 0.50 | Mostly empty — stub | Placeholder template |
| 0.50-0.78 | Sparse — needs enrichment | Has structure but thin |
| **0.78-0.90** | **Good — production quality** | **Dense content, tables, code** |
| > 0.90 | Very dense — may lack readability | Wall of text |

## Where Applied
- `cex_doctor.py` — checks all builder ISOs (WARN at < 0.78)
- `cex_hooks.py` — pre-commit validation (advisory)
- `cex_score.py` — factors into quality score (~10% weight)

## Dense Content Patterns
- Tables `| col | col |` — 100% dense lines
- Code blocks — nearly 100% dense
- Lists `- item` — 100% dense
- Headers `## Section` — 100% dense
- Blank separators between sections — reduce density

## How to Improve Density
1. Replace blank lines between list items with no separator
2. Combine short sections into tables
3. Remove redundant whitespace
4. Add content to empty sections (don't leave `## Purpose` bare)

## Quality Gate
- [ ] Threshold is documented (0.78)
- [ ] Calculation method is deterministic
- [ ] Severity is WARN (not ERROR) for flexibility
- [ ] Improvement guidance provided
