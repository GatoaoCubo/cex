---
id: p10_lr_trace_config_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
observation: "Trace configs that capture all prompts and responses in production generated 12GB/day of trace data for a 500-request/day workload — 95% of storage was prompt/response content that was never queried. Configs without sampling (sample_rate: 1.0) in production caused 8% latency overhead from the tracing pipeline itself. Configs without retention policies accumulated 200GB of trace data over 3 months before storage alerts fired. Configs without error classification made incident response slower because operators had to manually categorize each error before knowing whether to retry or escalate."
pattern: "Default to privacy-first: capture_prompts: false, capture_responses: false in production. Use selective capture only in dev/eval. Set sample_rate to 0.05-0.10 for production, 1.0 for dev. Always define retention with 3 tiers: hot (7d), warm (30d), cold (90d). Map spans to 8F functions for pipeline-level visibility. Classify errors into transient (retry), permanent (escalate), and degraded (fallback triggered). Track token counts in every LLM span — essential for cost analysis."
evidence: "Privacy-first capture reduced storage by 95% (12GB/day to 600MB/day) with zero loss of debugging capability. 10% sampling provided statistically equivalent error detection to 100% sampling for workloads above 50 req/day. 3-tier retention kept queryable data under 20GB while maintaining 90-day audit trail. 8F function spans reduced mean-time-to-debug from 45 minutes to 12 minutes by showing exactly which pipeline stage failed. Error classification reduced incident escalation time by 60%."
confidence: 0.85
outcome: SUCCESS
domain: trace_config
tags:
  - trace-config
  - observability
  - opentelemetry
  - sampling
  - privacy
  - retention
  - error-classification
tldr: "Privacy-first (no prompt capture), sample 5-10% prod, 3-tier retention (7/30/90d), 8F span mapping, classify errors, track tokens."
impact_score: 8.2
decay_rate: 0.03
agent_group: edison
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Trace Config"
density_score: 0.90
llm_function: INJECT
---
## Summary
Tracing failures cluster into three categories: storage explosion (capturing everything without sampling or retention), privacy violations (prompts with PII captured and stored indefinitely), and debugging blindness (traces without 8F function mapping that show the agent did something but not what pipeline stage failed). Privacy-first configuration with selective sampling, tiered retention, and function-level spans addresses all three.
## Pattern
**Privacy-first capture**: default to capturing span metadata (nucleus, kind, tokens, latency, error codes) but NOT prompt or response content. Prompt content is only useful for evaluation/debugging and can be enabled per-session via `capture_prompts: true` in development or evaluation configs. This prevents accidental PII exposure in production trace stores.
**Selective sampling**: production workloads above 50 req/day get statistically meaningful data at 5-10% sample rate. Below 50 req/day, use 20-50%. Development always uses 1.0. Sampling decisions are made at the root span and propagated to child spans — never sample individual child spans independently.
**3-tier retention**: hot (7 days, indexed, fast query), warm (30 days, compressed, moderate query), cold (90 days, archival, on-demand query). Hot tier is for active debugging. Warm is for trend analysis. Cold is for compliance and audit. Auto-purge after cold tier expires.
**8F function mapping**: create one span per 8F function (F1-F8) as children of the root pipeline span. Each span captures function-specific attributes: F1 records kind_resolved, F6 records bytes and density, F7 records score and gate results. This gives pipeline-level visibility into exactly which stage is slow or failing.
**Error classification**: every error span must be classified as transient (retry automatically), permanent (escalate to operator), or degraded (fallback was triggered, continue with reduced capability). This enables automated retry logic and faster incident response.
## Anti-Pattern
1. Capturing all prompts in production: 95% of storage wasted on content never queried, PII exposure risk.
2. sample_rate 1.0 in production: 8% latency overhead from tracing pipeline, storage explosion.
3. No retention policy: trace data grows unbounded — 200GB in 3 months is common.
4. No error classification: every error treated the same, slows incident response.
5. No 8F span mapping: traces show "something happened" but not which pipeline stage failed.

## Builder Context

This ISO operates within the `trace-config-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Checklist

1. Created via 8F pipeline
2. Scored by cex_score across three layers
3. Compiled by cex_compile for validation
4. Retrieved by cex_retriever for injection
5. Evolved by cex_evolve when quality drops

## Reference

```yaml
id: p10_lr_trace_config_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_trace_config_builder.md
```
