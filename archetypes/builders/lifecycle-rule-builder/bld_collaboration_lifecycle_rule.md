---
pillar: P11
llm_function: COLLABORATE
purpose: How lifecycle-rule-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: lifecycle-rule-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "when does this artifact change state, and who decides?"
I define declarative state machines for artifact creation, review, promotion, deprecation, and sunset. I do NOT implement transition logic (hook-builder), measure quality at a point in time (quality-gate-builder), or enforce safety boundaries (guardrail-builder).

## Crew Compositions

### Crew: "Full Governance for New Type"
```
  1. quality-gate-builder    -> "defines HARD/SOFT score thresholds that trigger state transitions"
  2. lifecycle-rule-builder  -> "encodes the full state machine: draft -> active -> deprecated -> sunset"
  3. guardrail-builder       -> "enforces safety restrictions during sensitive lifecycle transitions"
```

### Crew: "Content Maintenance Pipeline"
```
  1. lifecycle-rule-builder -> "declares review cadence, freshness triggers, and ownership"
  2. hook-builder           -> "implements automated cron jobs for staleness detection"
  3. signal-builder         -> "emits staleness and transition notifications to consumers"
```

### Crew: "Knowledge Freshness System"
```
  1. knowledge-card-builder  -> "produces the artifact that requires a lifecycle"
  2. lifecycle-rule-builder  -> "governs when the knowledge card is reviewed, promoted, or archived"
  3. learning-record-builder -> "captures patterns from freshness violations for future prevention"
```

## Handoff Protocol

### I Receive
- seeds: target artifact kind, expected lifespan, review cadence, ownership, freshness criteria
- optional: existing quality gate scores to use as transition thresholds, domain volatility data

### I Produce
- lifecycle_rule artifact (YAML, 17 required + 4 recommended frontmatter fields, state machine with transitions, max 4KB)
- committed to: `cex/P11_feedback/examples/p11_lc_{rule_slug}.yaml`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- quality-gate-builder: quality score thresholds define the promotion and demotion criteria for state transitions

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| hook-builder    | implements automated execution of the transition triggers defined here |
| signal-builder  | lifecycle state changes emit signals consumed by downstream builders |
| guardrail-builder | references lifecycle state to restrict operations on deprecated artifacts |
| optimizer-builder | uses freshness metrics from lifecycle rules as optimization targets |
