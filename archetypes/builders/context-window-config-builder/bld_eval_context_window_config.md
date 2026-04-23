---
kind: quality_gate
id: p11_qg_context_window_config
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of context_window_config artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: Context Window Config"
version: "1.0.0"
author: "n04_knowledge"
tags: [quality-gate, context-window-config, token-budget, overflow]
tldr: "Gates ensuring context_window_config artifacts have valid budgets, priority tiers, and overflow strategy."
domain: "context_window_config — token budget allocation for prompt assembly"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_context_window_config
  - bld_instruction_context_window_config
  - bld_config_context_window_config
  - p01_kc_context_window_config
  - bld_output_template_context_window_config
  - p03_sp_context_window_config_builder
  - context-window-config-builder
  - bld_knowledge_card_context_window_config
  - bld_collaboration_context_window_config
  - bld_architecture_context_window_config
---

## Quality Gate

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

## Examples

# Examples: context-window-config-builder
## Golden Example
INPUT: "Create context window config for Claude Opus 200K with RAG-heavy workload"
OUTPUT:
```yaml
---
id: p03_cwc_opus_rag_heavy
kind: context_window_config
pillar: P03
title: "Claude Opus 200K — RAG-Heavy Profile"
version: "1.0.0"
created: "2026-04-07"
updated: "2026-04-07"
author: "context-window-config-builder"
target_model: claude-opus-4-20250514
total_tokens: 200000
system_prompt_budget: 10000
few_shot_budget: 15000
retrieved_context_budget: 100000
user_query_budget: 5000
output_reserve: 32000
overflow_strategy: truncate_lowest
priority_tiers: [system, query, context, examples]
domain: llm_engineering
quality: null
tags: [context_window_config, opus, rag, token-budget]
tldr: "Opus 200K RAG-heavy: 50% context, 16% output, 5% system — priority truncation on overflow"
---
# Budget: system 5%, examples 7.5%, context 50%, query 2.5%, output 16%
# Remaining 19% unallocated (buffer for dynamic scaling)
```
WHY THIS IS GOLDEN:
1. quality: null
2. Budgets sum <= total_tokens (162K of 200K, with buffer)
3. output_reserve >= 2000 (32K)
4. priority_tiers present and ordered
5. overflow_strategy is valid enum

## Anti-Example
BAD OUTPUT:
```yaml
id: window_config
total_tokens: 999999
system_prompt_budget: 500000
output_reserve: 100
quality: 9.0
```
FAILURES:
1. id: no p03_cwc_ prefix
2. total_tokens: exceeds any real model
3. output_reserve: too small (< 2000)
4. quality: not null
5. No priority_tiers or overflow_strategy

## Properties

| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P07 |
| Domain | context window config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
