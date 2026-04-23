---
kind: quality_gate
id: p11_qg_trace_config
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of trace_config artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: trace_config"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, trace-config, observability, tracing, P11]
tldr: "Gates for trace_config artifacts: validates exporter, sample rate, capture flags, span attributes, retention, and privacy controls."
domain: "trace_config — execution tracing specifications with exporters, sample rates, capture rules, and retention policies"
created: "2026-04-06"
updated: "2026-04-06"
density_score: 0.91
related:
  - bld_examples_trace_config
  - bld_output_template_trace_config
  - p03_sp_trace_config_builder
  - bld_architecture_trace_config
  - bld_schema_trace_config
  - bld_instruction_trace_config
  - p11_qg_quality_gate
  - p01_kc_trace_config
  - p11_qg_kind_builder
  - p11_qg_dispatch_rule
---

## Quality Gate

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

## Examples

# Examples: trace-config-builder
## Golden Example
INPUT: "Define a production trace config for CEX 8F pipeline with OTLP export"
OUTPUT:
```yaml
id: p07_tc_production_8f
kind: trace_config
pillar: P07
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "builder_agent"
enabled: true
sample_rate: 0.10
export_format: otlp
export_path: "${OTEL_EXPORTER_OTLP_ENDPOINT}"
capture_prompts: false
capture_responses: false
span_attributes:
  - cex.nucleus
  - cex.kind
  - cex.8f.function
  - cex.tokens.input
  - cex.tokens.output
  - cex.tokens.total
  - cex.model
  - cex.latency_ms
  - cex.error.type
  - cex.quality.score
retention_days: 30
quality: null
tags: [trace_config, production, otlp, P07, 8f-pipeline]
tldr: "Production OTLP tracing: 10% sample, no prompt capture, 8F spans, 30d retention"
description: "Production-grade execution tracing for CEX 8F pipeline with OTLP export to Tempo/Jaeger"
scope: "cex_pipeline"
environment: production
error_classification:
  transient: "rate_limit, timeout, connection_reset"
  permanent: "auth_failure, model_not_found, invalid_schema"
  degraded: "fallback_triggered, quality_below_threshold"
```
## Tracing Specification
Production tracing at 10% sample rate via OTLP/gRPC to the configured collector endpoint.
Captures span metadata (nucleus, kind, model, tokens, latency) but NOT prompt or response
content — privacy by default. 10% sample provides statistically meaningful data for
~100 req/day while keeping storage under 500MB/month.
## Capture Rules
| Category | Captured | Rationale |
|----------|----------|-----------|
| Span metadata | YES | Nucleus, kind, function name — lightweight, no PII |
| Token counts | YES | Input/output/total — essential for cost tracking |
| Latency | YES | Per-function and total — performance debugging |
| Error codes | YES | Classified by type — incident response |
| Prompt content | NO | May contain user PII, proprietary data |
| Response content | NO | Large, expensive to store, privacy risk |
| Tool call names | YES | Which tools invoked — debugging aid |
| Tool call results | NO | May contain sensitive data from external APIs |
## Span Attributes
| Span | Attributes | 8F Mapping |
|------|-----------|-----------|
| `cex.pipeline` | nucleus, kind, intent | Root span — one per build request |
| `cex.8f.f1_constrain` | kind_resolved, pillar, schema_loaded | F1 CONSTRAIN |
| `cex.8f.f2_become` | builder_id, iso_count | F2 BECOME |
| `cex.8f.f3_inject` | knowledge_sources, template_match_pct | F3 INJECT |
| `cex.8f.f4_reason` | section_count, approach | F4 REASON |
| `cex.8f.f5_call` | tools_ready, similar_count | F5 CALL |
| `cex.8f.f6_produce` | bytes, sections, density | F6 PRODUCE |
| `cex.8f.f7_govern` | score, gates_passed, gates_total | F7 GOVERN |
| `cex.8f.f8_collaborate` | path, compiled, committed | F8 COLLABORATE |
| `cex.llm.call` | model, tokens_in, tokens_out, latency_ms | LLM invocation |
## Retention Policy
| Tier | Days | Storage | Query speed | Cleanup |
|------|------|---------|-------------|---------|
| Hot | 7 | Primary store | Fast (indexed) | Auto-rollover |
| Warm | 30 | Compressed | Moderate | Weekly compaction |
| Cold | 90 | Archive | Slow (on-demand) | Quarterly purge |
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p07_tc_ pattern (H02 pass)
- kind: trace_config (H04 pass)
- All 8 core fields present: enabled, sample_rate, export_format, export_path, capture_prompts, capture_responses, span_attributes, retention_days (H06 pass)
- sample_rate 0.10 within 0.0-1.0 (H07 pass)
- export_format "otlp" is valid enum (H08 pass)
- capture_prompts/capture_responses explicitly false (H09 pass)
- retention_days 30 is positive integer (H10 pass)
- Span attributes map to all 8F functions
- Error classification with 3 categories
- Privacy-first: no prompt/response capture in production
## Anti-Example
INPUT: "Create trace config for debugging"
BAD OUTPUT:
```yaml
id: debug-traces
kind: tracing
pillar: observability
enabled: yes
sample_rate: 2.0
capture_prompts: always
quality: 9.0
tags: [tracing]
```
Trace everything and save forever.
FAILURES:
1. id: "debug-traces" uses hyphens and no `p07_tc_` prefix -> H02 FAIL
2. kind: "tracing" not "trace_config" -> H04 FAIL
3. pillar: "observability" not "P07" -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. sample_rate: 2.0 exceeds maximum 1.0 -> H07 FAIL
6. enabled: "yes" not a boolean (true/false) -> H06 FAIL
7. capture_prompts: "always" not boolean -> H09 FAIL
8. Missing fields: export_format, export_path, capture_responses, span_attributes, retention_days, version, created, author -> H06 FAIL
9. tags: only 1 item, missing "trace_config" -> S02 FAIL
10. Body missing Tracing Specification, Capture Rules, Span Attributes, Retention Policy -> structural FAIL
11. "Save forever" = no retention policy -> S05 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
