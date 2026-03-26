---
pillar: P12
llm_function: COLLABORATE
purpose: How validator-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: validator-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what technical check must pass before this artifact is accepted?"
I do not score artifacts. I do not define scoring criteria.
I ENFORCE rules so quality-gate-builder and downstream consumers can trust artifact correctness.

## Crew Compositions

### Crew: "Artifact Quality Pipeline"
```
  1. knowledge-card-builder -> "produces the KC artifact"
  2. validator-builder -> "checks structural correctness (pass/fail)"
  3. quality-gate-builder -> "scores quality (0-10 weighted)"
```

### Crew: "New Kind Bootstrap"
```
  1. schema-builder [PLANNED] -> "defines the kind schema"
  2. validator-builder -> "creates validators for the schema"
  3. quality-gate-builder -> "creates scoring gates"
  4. output-template-builder [PLANNED] -> "creates the template"
```

### Crew: "Pre-Commit Enforcement"
```
  1. validator-builder -> "defines pass/fail rules"
  2. hook-builder [PLANNED] -> "wires validators into pre-commit"
  3. bugloop-builder [PLANNED] -> "auto-fixes failures when possible"
```

## Handoff Protocol

### I Receive
- seeds: target domain (artifact kind), rule description
- optional: existing schema (_schema.yaml), severity preference, auto_fix requirement

### I Produce
- validator artifact (YAML)
- committed to: `cex/P06_schema/examples/p06_val_{rule_slug}.yaml`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None. Validators are INDEPENDENT — they can be built from schema alone.
Optional enrichment from schema-builder [PLANNED] output.

## Builders That Depend On Me [PLANNED]

| Builder | Why |
|---------|-----|
| quality-gate-builder | Uses validators as HARD gate checklist source |
| hook-builder [PLANNED] | Wires validators into pre-commit automation |
| bugloop-builder [PLANNED] | References validators to detect + fix regressions |
