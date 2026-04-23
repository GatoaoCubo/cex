---
kind: quality_gate
id: p11_qg_thinking_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for thinking_config artifacts
quality: 9.1
title: "Quality Gate: Thinking Config"
version: "1.0.0"
author: n02_reviewer
tags: [thinking_config, builder, quality_gate, P11]
tldr: "Quality gate for thinking budget configuration artifacts defining token allocation, depth limits, and fallback strategy."
domain: "thinking_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - p03_sp_thinking_config_builder
  - p11_qg_quality_gate
  - bld_instruction_thinking_config
  - bld_memory_thinking_config
  - p11_qg_collaboration_pattern
  - p11_qg_response_format
  - thinking-config-builder
  - bld_examples_thinking_config
  - bld_tools_thinking_config
  - p11_qg_voice_pipeline
---

## Quality Gate
## Definition
This ISO configures a thinking budget: how many tokens the model may spend on internal reasoning before emitting.

A `thinking_config` artifact defines the resource allocation parameters for extended AI
reasoning processes: token budgets, depth limits, timeout thresholds, and fallback strategies.
It does NOT define reasoning techniques (reasoning_strategy) or context window sizing
(context_window_config).

Scope: files with `kind: thinking_config`. Does NOT apply to reasoning_strategy
(chain-of-thought, heuristic methods) or context_window_config (max_tokens limits).

## HARD Gates
Failure on any single gate means REJECT regardless of soft score.

| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p09_thk_*` | `id.startswith("p09_thk_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `thinking_config` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr all present |
| H07 | Budget token limit declared | body or frontmatter contains `budget`, `max_tokens`, or `token_limit` |
| H08 | Fallback strategy or timeout defined | body references fallback behavior or timeout threshold |

## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.

| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Budget tier structure declared (e.g., low/medium/high or numeric values) | 1.0 |
| 3  | Fallback strategy documented for budget exhaustion | 1.0 |
| 4  | Reasoning depth limit or max iteration count specified | 1.0 |
| 5  | Priority tiers or task-complexity mapping documented | 0.5 |
| 6  | Dynamic adjustment rules present (e.g., scale by task complexity) | 0.5 |
| 7  | Tags include `thinking_config` | 0.5 |
| 8  | Boundary note: distinguishes from reasoning_strategy and context_window_config | 1.0 |
| 9  | At least one concrete use case with budget values | 1.0 |
| 10 | Default values provided for all optional parameters | 0.5 |
| 11 | `tldr` is <= 160 characters | 0.5 |

**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 9.0. Score range: 0.0 to 10.0.

## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool; add to curated config library |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle |
| REJECT | < 7.0 | Block from pool; full rewrite required |

## Bypass
| Field | Value |
|-------|-------|
| condition | Config is a temporary experiment with documented lifespan under 30 days |
| approver | Domain lead must approve in writing |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver, reason |
| expiry | 30 days from bypass grant; config must be retired or brought to full compliance |

## Properties
| Property | Value |
|----------|-------|
| Kind | `quality_gate` |
| Pillar | P11 |
| Domain | thinking_config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Examples
## Golden Example
This ISO configures a thinking budget: how many tokens the model may spend on internal reasoning before emitting.
```markdown
---
title: "Thinking Budget Configuration"
description: "Configures extended thinking with token budget limits"
version: "1.0"
author: "System Admin"
---

**thinking_budget**: 1000
**token_limits**: 
  - max_context: 500
  - max_response: 300
**dynamic_adjustment**: true
**fallback_strategy**: "truncate"
```

## Anti-Example 1: Missing Essential Fields
```markdown
---
title: "Incomplete Config"
description: "Missing thinking_budget parameter"
version: "0.5"
author: "Newbie"
---

**token_limits**: 
  - max_context: 500
  - max_response: 300
```
## Why it fails
Lacks required `thinking_budget` field, making resource allocation impossible.

## Anti-Example 2: Invalid Budget Values
```markdown
---
title: "Invalid Config"
description: "Uses non-numeric budget values"
version: "1.0"
author: "Mistake"
---

**thinking_budget**: "high"
**token_limits**: 
  - max_context: "unlimited"
  - max_response: 300
```
## Why it fails
Uses strings instead of numeric values for budget parameters, causing parsing errors.

## Properties
| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P07 |
| Domain | thinking_config construction |
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
