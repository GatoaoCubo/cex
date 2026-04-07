---
kind: quality_gate
id: bld_quality_gate_memory_type
pillar: P11
llm_function: GOVERN
quality: 9.0
title: "Quality Gate Memory Type"
version: "1.0.0"
author: n03_builder
tags: [memory_type, builder, examples]
tldr: "Golden and anti-examples for memory type construction, demonstrating ideal structure and common pitfalls."
domain: "memory type construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Quality Gate: memory_type

## Hard Gates (must ALL pass)
| Gate | Check | Fail Action |
|------|-------|-------------|
| H01 | YAML frontmatter parses | REJECT |
| H02 | id matches p10_mt_ pattern | REJECT |
| H03 | kind == "memory_type" | REJECT |
| H04 | quality == null | REJECT |
| H05 | type_name in [correction, preference, convention, context] | REJECT |
| H06 | decay_rate is float 0.0-1.0 | REJECT |
| H07 | body <= 2048 bytes | REJECT |

## Soft Gates (score deductions)
| Gate | Check | Deduction |
|------|-------|-----------|
| S01 | Has >= 3 examples | -1.0 |
| S02 | Has >= 2 anti-examples | -0.5 |
| S03 | Decay Policy section present | -1.0 |
| S04 | Storage Rules section present | -0.5 |
| S05 | tldr <= 160 chars | -0.5 |

## Gate Execution Steps

1. Parse frontmatter and validate required fields
2. Run all hard gates as binary pass/fail checks
3. Score soft dimensions with weighted 0-10 scale
4. Compute weighted average across all dimensions
5. Apply threshold: 7.0 publish, 8.0 pool, 9.5 golden

## Scoring Command

```bash
python _tools/cex_score.py --apply --verbose target.md
```

```bash
python _tools/cex_score.py --apply N0*/*.md
```
