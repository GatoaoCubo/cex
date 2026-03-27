---
pillar: P11
llm_function: COLLABORATE
purpose: How optimizer-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: optimizer-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what metric drives what action at what threshold?"
I define continuous improvement cycles: metric targets, tripartite thresholds (trigger/target/critical), and automated actions. I do NOT handle one-time fixes (bugloop-builder), passive measurement (benchmark-builder), or pass/fail barriers (quality-gate-builder).

## Crew Compositions

### Crew: "Performance Improvement Loop"
```
  1. benchmark-builder    -> "establishes baseline measurements passively"
  2. optimizer-builder    -> "defines metric>action cycle to improve on baseline"
  3. bugloop-builder      -> "handles point-in-time corrections when critical threshold hit"
```

### Crew: "Process Quality System"
```
  1. quality-gate-builder -> "sets pass/fail barriers for artifact acceptance"
  2. optimizer-builder    -> "defines continuous tuning cycle beyond the gate"
  3. signal-builder       -> "emits metric events that trigger optimizer actions"
```

### Crew: "Pipeline Optimization"
```
  1. dag-builder          -> "maps the pipeline structure being optimized"
  2. optimizer-builder    -> "defines optimization targets per pipeline stage"
  3. runtime-rule-builder -> "encodes timeout/retry rules informed by optimizer thresholds"
```

## Handoff Protocol

### I Receive
- seeds: process name, metric name, current baseline values, direction (minimize/maximize)
- optional: existing threshold data, automation constraints, risk tolerance

### I Produce
- optimizer artifact (Markdown, max 4KB)
- committed to: `cex/P11/examples/p11_opt_{scope}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- benchmark-builder: provides baseline measurements that anchor optimizer targets
- scoring-rubric-builder: provides quality dimensions that become secondary metrics

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| bugloop-builder | triggered when optimizer detects critical threshold breach |
| signal-builder | emits the metric events the optimizer monitors |
| runtime-rule-builder | encodes thresholds from optimizer into operational timeouts/retries |
| validator-builder | implements the metric collection this optimizer monitors |
