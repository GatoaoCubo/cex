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
related:
  - bld_examples_memory_type
  - bld_output_template_memory_type
  - bld_knowledge_card_memory_type
  - p01_kc_memory_type
  - bld_schema_memory_type
  - p01_kc_artifact_quality_evaluation_methods
  - p11_qg_quality_gate
  - bld_system_prompt_memory_type
  - bld_knowledge_card_quality_gate
  - bld_architecture_memory_type
---

## Quality Gate

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

## Examples

# Examples: memory_type

## Golden: Correction

| Field | Value |
|-------|-------|
| id | p10_mt_correction |
| type_name | correction |
| decay_rate | 0.00 |
| preserve_on_compact | true |
| tldr | User-corrected facts -- permanent, zero decay |

Definition: Explicit user overrides. "No, YAML not JSON." Zero decay = ground truth.
Decay: 0.00 -- never loses confidence. Verified by authoritative source.
Storage: Append to bld_memory. Never overwrite. Always preserve. Confidence 1.0.
Examples: (1) "pt-BR not en-US" (2) "API /v2 not /v1" (3) "voice warm, not clinical"
Anti-ex: (1) "prefer bullets" = PREFERENCE (2) "we use tabs" = CONVENTION

## Golden: Context

| Field | Value |
|-------|-------|
| type_name | context |
| decay_rate | 0.05 |
| preserve_on_compact | false |
| tldr | Session-bound situational facts -- fast decay |

Definition: Time-bound facts. "Debugging auth module now." Fast decay after session.
Storage: Session memory. First to drop on compaction (Wire 6).
Examples: (1) "working on auth today" (2) "file open: router.py" (3) "sprint 14"
Anti-ex: (1) "always use auth middleware" = CONVENTION (repeatable pattern)

## Anti-Example: Misclassified

| Field | Wrong Value | Correct Value | Why |
|-------|------------|---------------|-----|
| type_name | correction | context | "Today working on X" is temporal, no override |
| decay_rate | 0.00 | 0.05 | Session-bound, not permanent |
| preserve | true | false | No long-term value after session |

Rule: If observation contains "today/now/currently" WITHOUT contradicting agent, it is CONTEXT not CORRECTION.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
