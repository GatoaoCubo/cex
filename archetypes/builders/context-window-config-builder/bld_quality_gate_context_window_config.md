---
id: p11_qg_context_window_config
kind: quality_gate
pillar: P11
title: "Gate: Context Window Config"
version: "1.0.0"
created: "2026-04-07"
updated: "2026-04-07"
author: "n04_knowledge"
domain: "context_window_config — token budget allocation for prompt assembly"
quality: 9.0
tags: [quality-gate, context-window-config, token-budget, overflow]
tldr: "Gates ensuring context_window_config artifacts have valid budgets, priority tiers, and overflow strategy."
density_score: 0.90
llm_function: GOVERN
---
# Gate: Context Window Config
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: context_window_config` |
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | ID matches `^p03_cwc_[a-z][a-z0-9_]+$` | Wrong prefix |
| H03 | Kind equals literal `context_window_config` | Wrong kind |
| H04 | Quality field is `null` | Non-null value |
| H05 | total_tokens is positive integer | Zero, negative, or non-integer |
| H06 | output_reserve >= 2000 | Too small — model will truncate |
| H07 | sum(budgets) + output_reserve <= total_tokens | Budget overflow |
| H08 | priority_tiers is non-empty ordered list | Missing or empty |
| H09 | overflow_strategy is valid enum | Not in truncate_lowest/compress/drop_section |
| H10 | Total file <= 2048 bytes | Exceeds limit |
## SOFT Scoring
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Budget proportionality | 1.0 | Proportional to workload | Reasonable | Equal or arbitrary |
| S02 | Model specificity | 1.0 | target_model with exact name/version | Generic model class | No model specified |
| S03 | Overflow detail | 1.0 | Strategy + trigger + fallback documented | Strategy only | No overflow handling |
| S04 | Priority rationale | 0.5 | Each tier justified | Order present | No tiers |
| S05 | Dynamic scaling | 0.5 | Buffer for variable content | Fixed allocation | Budgets sum to exactly total |

## Cross-References

- **Pillar**: P11 (Feedback)
- **Kind**: `quality gate`
- **Artifact ID**: `p11_qg_context_window_config`
- **Tags**: [quality-gate, context-window-config, token-budget, overflow]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P11 | Feedback domain |
| Kind `quality gate` | Artifact type |
| Pipeline | 8F (F1→F8) |
