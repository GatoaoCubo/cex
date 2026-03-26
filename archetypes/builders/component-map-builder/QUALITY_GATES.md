---
id: component-map-builder-quality-gates
kind: quality_gates
parent: component-map-builder
version: 1.0.0
---

# Quality Gates — component-map-builder

## HARD Gates (9) — any failure = REJECT

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses without error | Broken YAML = broken artifact |
| H02 | id matches `^p08_cmap_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem (without .yaml) | Brain search relies on exact match |
| H04 | kind == "component_map" (exact literal) | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All 15 required fields present and non-null | Completeness minimum |
| H07 | tags is list, len >= 3 | Searchability minimum |
| H08 | scope field is non-empty string | Must know what is mapped |
| H09 | component_count >= 2 (integer) | Minimum meaningful inventory |

## SOFT Gates (10) — weighted score

| Gate | Check | Weight | Points |
|------|-------|--------|--------|
| S01 | tldr <= 160 chars and non-empty | 1.0 | 10 |
| S02 | connection_count >= 1 | 1.0 | 10 |
| S03 | Connections table has direction column for each row | 1.0 | 10 |
| S04 | Components table has name, role, owner, status per row | 1.0 | 10 |
| S05 | No orphan components (every component has >= 1 connection) | 1.0 | 10 |
| S06 | Interfaces section present and non-empty | 1.0 | 10 |
| S07 | Body has all 7 required sections (Scope/Components/Connections/Interfaces/Dependencies/Boundaries/References) | 1.0 | 10 |
| S08 | density >= 0.80 (no filler prose) | 1.0 | 10 |
| S09 | Dependencies section with failure_impact per row | 0.5 | 10 |
| S10 | keywords present, len >= 2 | 0.5 | 10 |

Total possible: 100 points. Minimum delivery: 80 points (score >= 8.0).

## Scoring Formula

```
hard_pass = all(H01..H09)
soft_score = sum(weight_i * 10 for gate_i if pass) / sum(all_weights * 10) * 10
final_score = soft_score if hard_pass else 0
```

## Common Failure Patterns

| Failure | Gate | Fix |
|---------|------|-----|
| `quality: 8.5` | H05 | Set `quality: null` |
| `id: brain_map` | H02 | Rename to `p08_cmap_brain_map` |
| Missing `scope` field | H08 | Add scope to frontmatter |
| `component_count: 1` | H09 | Map must cover >= 2 components |
| Prose instead of tables | S04, S03 | Replace with structured tables |
| "A and B connect" | S03 | Specify direction: unidirectional/bidirectional |
| Component with no connections | S05 | Add connection or remove component |
| Missing Interfaces section | S06 | Add `## Interfaces` with table |
| component_count: 5, table has 4 rows | H06 | Sync count with actual rows |
