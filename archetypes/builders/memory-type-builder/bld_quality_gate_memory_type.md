---
kind: quality_gate
id: bld_quality_gate_memory_type
pillar: P11
llm_function: GOVERN
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
