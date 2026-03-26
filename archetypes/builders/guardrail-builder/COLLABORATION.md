---
pillar: P12
llm_function: COLLABORATE
purpose: How guardrail-builder works in crews
---

# Collaboration: guardrail-builder

## My Role
I define WHAT agents must NEVER do and what happens if they try.
I do not control ACCESS (permission-builder [PLANNED]).
I do not measure QUALITY (quality-gate-builder).

## Crew: "Safety Setup for New Agent"
```
  1. guardrail-builder         -> defines safety boundaries
  2. permission-builder [PLANNED] -> defines access controls
  3. quality-gate-builder      -> defines quality thresholds
```

## Crew: "Compliance Audit"
```
  1. guardrail-builder         -> reviews safety restrictions
  2. quality-gate-builder      -> reviews quality gates
  3. scoring-rubric-builder    -> reviews evaluation criteria
```

## Handoff Protocol
### I Receive
- seeds: scope (what to protect), domain, severity hint
- optional: threat model, existing laws, incident reports

### I Produce
- guardrail artifact in P11_feedback/examples/
- committed to: cex/P11_feedback/examples/p11_gr_{scope_slug}.md

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None directly. Independent at layer 0.
- quality-gate-builder: provides gate patterns as reference for enforcement

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| permission-builder [PLANNED] | Complements guardrails with access control |
| hook-builder [PLANNED] | Implements guardrail enforcement in code |
