---
id: p11_qg_compression_config
kind: quality_gate
pillar: P11
title: "Gate: compression_config"
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "builder_agent"
domain: "compression_config — context compression strategies with trigger ratios, preserve types, decay weights, and tiered pipelines"
quality: 9.0
tags: [quality-gate, compression-config, context-window, token-reduction, P11]
tldr: "Gates for compression_config artifacts: validates strategy completeness, trigger ratio range, preserve types, decay weights, and pipeline ordering."
density_score: 0.90
llm_function: GOVERN
---
# Gate: compression_config
## Definition
| Field     | Value |
|-----------|-------|
| metric    | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator  | AND (all HARD) + weighted_sum (SOFT) |
| scope     | All artifacts where `kind: compression_config` |
## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.
| ID  | Check | Failure message |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p10_cc_[a-z][a-z0-9_]+$` | "ID fails compression_config namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"compression_config"` | "Kind is not 'compression_config'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, strategy, trigger_ratio, preserve_types, max_summary_tokens, min_context_tokens, decay_weights, version, created, author, tags | "Missing required field(s)" |
| H07 | `preserve_types` includes `system_prompt` | "system_prompt must be in preserve_types — structural context must never be compressed" |
| H08 | `trigger_ratio` is between 0.50 and 0.99 inclusive | "Trigger ratio out of valid range (0.50-0.99)" |
| H09 | `strategy` is one of: summarize, truncate_oldest, rolling_window, priority_keep, tiered | "Invalid compression strategy" |
| H10 | `max_summary_tokens` > 0 and `min_context_tokens` > 0 | "Token limits must be positive integers" |
## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.
| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Strategy rationale | 1.0 | Why this strategy fits the target agent's workload |
| Preserve types completeness | 1.0 | All structural message types (system_prompt, tool_def, pinned) included |
| Decay weight coverage | 1.0 | Decay weights defined for all message types in the agent's vocabulary |
| Pipeline ordering | 1.0 | Stages ordered from least lossy to most lossy (summarize before drop) |
| Trigger ratio justification | 0.5 | Ratio explained relative to model context window and task length |
| Target ratio clarity | 0.5 | Post-compression target specified and achievable |
| Token accounting | 1.0 | max_summary_tokens and min_context_tokens justified with math |
| Graceful degradation | 1.0 | Config handles edge cases: what if summarization fails? fallback? |
| Boundary clarity | 0.5 | Explicitly not token_budget, session_backend, or memory config |
| Age decay curve | 1.0 | Decay weights include time-based component, not just type-based |
| Integration references | 0.5 | References to cex_token_budget.py, p04_skill_compact, or Wire 6 |
| Documentation | 0.5 | tldr names the strategy and trigger ratio |
Weight sum: 1.0+1.0+1.0+1.0+0.5+0.5+1.0+1.0+0.5+1.0+0.5+0.5 = 10.0 (100%)
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0  | REJECT | Return to author with failure report |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Experimental compression strategy being A/B tested where full decay weights are not yet calibrated |
| approver | Nucleus lead approval required (written); preserve_types never bypassed |
