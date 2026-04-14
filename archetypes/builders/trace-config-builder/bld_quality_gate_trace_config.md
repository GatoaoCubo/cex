---
id: p11_qg_trace_config
kind: quality_gate
pillar: P11
title: "Gate: trace_config"
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "builder_agent"
domain: "trace_config — execution tracing specifications with exporters, sample rates, capture rules, and retention policies"
quality: 9.0
tags: [quality-gate, trace-config, observability, tracing, P11]
tldr: "Gates for trace_config artifacts: validates exporter, sample rate, capture flags, span attributes, retention, and privacy controls."
density_score: 0.91
llm_function: GOVERN
---
# Gate: trace_config
## Definition
| Field     | Value |
|-----------|-------|
| metric    | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator  | AND (all HARD) + weighted_sum (SOFT) |
| scope     | All artifacts where `kind: trace_config` |
## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.
| ID  | Check | Failure message |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p07_tc_[a-z][a-z0-9_]+$` | "ID fails trace_config namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"trace_config"` | "Kind is not 'trace_config'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, enabled, sample_rate, export_format, export_path, capture_prompts, capture_responses, span_attributes, retention_days, version, created, author, tags | "Missing required field(s)" |
| H07 | `sample_rate` is between 0.0 and 1.0 inclusive | "Sample rate out of valid range (0.0-1.0)" |
| H08 | `export_format` is one of: otlp, langsmith, console, json_file | "Invalid export format" |
| H09 | `capture_prompts` and `capture_responses` are explicit booleans | "Capture flags must be explicit true/false" |
| H10 | `retention_days` is a positive integer | "Retention days must be a positive integer" |
## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.
| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Exporter rationale | 1.0 | Why this exporter fits the target environment and infrastructure |
| Sample rate justification | 1.0 | Rate explained relative to request volume, storage budget, debugging needs |
| Capture rule clarity | 1.0 | Explicit rules for what is/isn't captured with privacy justification |
| Span attribute coverage | 1.0 | 8F function boundaries mapped to spans, token counts included |
| Retention tiering | 1.0 | Hot/warm/cold tiers with days per tier and cleanup strategy |
| Privacy controls | 1.0 | PII redaction, prompt capture policy, consent documentation |
| Error classification | 0.5 | Errors categorized (transient/permanent/rate_limit) with severity |
| Token accounting | 0.5 | Token usage tracked in span attributes (input, output, total) |
| Performance overhead | 0.5 | Tracing overhead estimated and within acceptable bounds |
| Boundary clarity | 0.5 | Explicitly not quality_gate, log_config, metric_config, or alert_config |
| Integration references | 1.0 | References to cex_8f_runner.py, cex_sdk/tracing/, cex_quality_monitor.py |
| Documentation | 0.5 | tldr names the exporter, sample rate, and environment |
Weight sum: 1.0+1.0+1.0+1.0+1.0+1.0+0.5+0.5+0.5+0.5+1.0+0.5 = 10.0 (100%)
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
| conditions | Development-only trace config where retention and privacy are not yet defined |
| approver | Security lead approval required (written) for any config with capture_prompts: true in production |
