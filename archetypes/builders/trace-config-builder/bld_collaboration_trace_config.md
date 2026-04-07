---
kind: collaboration
id: bld_collaboration_trace_config
pillar: P12
llm_function: COLLABORATE
purpose: How trace-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Trace Config"
version: "1.0.0"
author: n03_builder
tags: [trace_config, builder, examples]
tldr: "Golden and anti-examples for trace config construction, demonstrating ideal structure and common pitfalls."
domain: "trace config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Collaboration: trace-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should this agent's execution be traced for debugging and observability?"
I do not score artifact quality. I do not format log messages.
I specify execution tracing so operators can debug failures and measure performance.
## Crew Compositions
### Crew: "Observability Stack"
```
  1. trace-config-builder -> "execution tracing (spans, latency, tokens)"
  2. log-config-builder -> "log formatting and routing"
  3. metric-config-builder -> "counters, gauges, histograms"
  4. alert-config-builder -> "threshold-based alerting"
```
### Crew: "Full Agent Infrastructure"
```
  1. agent-builder -> "agent definition"
  2. boot-config-builder -> "provider startup configuration"
  3. env-config-builder -> "environment variables"
  4. session-backend-builder -> "state persistence backend"
  5. trace-config-builder -> "execution tracing and observability"
  6. quality-gate-builder -> "artifact quality scoring"
```
## Handoff Protocol
### I Receive
- seeds: target scope, environment (dev/staging/prod), exporter preference, privacy requirements
- optional: sample_rate override, retention_days override, specific span attributes needed
### I Produce
- trace_config artifact (.md + .yaml frontmatter)
- committed to: `cex/P07/examples/p07_tc_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- env-config-builder: provides OTLP endpoint and LangSmith API key via environment variables
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| quality-gate-builder | Quality monitor reads trace data for regression detection |
| agent-builder | Agent config references trace_config for observability setup |
| daemon-builder | Background processes need tracing for long-running operation debugging |
