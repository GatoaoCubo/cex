---
kind: collaboration
id: bld_collaboration_bugloop
pillar: P12
llm_function: COLLABORATE
purpose: How bugloop-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: bugloop-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is the automatic detect-fix-verify loop for this system?"
I do not define quality gates. I do not score rubrics.
I design automated correction cycles so systems self-heal without manual intervention.

## Crew Compositions

### Crew: "Self-Healing System"
```
  1. benchmark-builder -> "performance thresholds for detection triggers"
  2. bugloop-builder -> "detect-fix-verify correction cycle"
  3. guardrail-builder -> "safety boundaries for auto-fix scope"
```

### Crew: "Governance Enforcement"
```
  1. axiom-builder -> "immutable rules to enforce"
  2. bugloop-builder -> "correction loop for axiom violations"
  3. e2e-eval-builder -> "end-to-end verification after fix"
```

## Handoff Protocol

### I Receive
- seeds: detection trigger pattern, target system/agent, fix strategy type
- optional: max_attempts, escalation target, rollback policy

### I Produce
- bugloop artifact (.md + .yaml frontmatter)
- committed to: `cex/P11/examples/p11_bugloop_{scope}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- benchmark-builder: provides thresholds that trigger detection
- axiom-builder: provides invariant rules that define "correct" state

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| e2e-eval-builder | Validates that bugloop fixes pass full pipeline |
| daemon-builder | Background processes may host bugloop execution |
