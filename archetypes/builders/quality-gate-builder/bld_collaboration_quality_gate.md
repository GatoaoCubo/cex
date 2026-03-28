---
kind: collaboration
id: bld_collaboration_quality_gate
pillar: P11
llm_function: COLLABORATE
purpose: How quality-gate-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: quality-gate-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what must pass before this artifact ships?"
I define HARD gates (block on fail) and SOFT gates (score contribution) with numeric thresholds. I do not write validator code, scoring rubric criteria, or run bugloop cycles.

## Crew Compositions

### Crew: "Artifact Quality Assurance"
```
  1. scoring-rubric-builder   -> "criteria dimensions and weights for evaluation"
  2. quality-gate-builder     -> "HARD/SOFT gates with numeric thresholds and bypass policy"
  3. validator-builder        -> "executable code that enforces the gates post-generation"
```

### Crew: "Agent Governance Layer"
```
  1. law-builder              -> "inviolable rules that override all other decisions"
  2. guardrail-builder        -> "safety boundaries on agent behavior"
  3. quality-gate-builder     -> "quality thresholds artifacts must clear before acceptance"
  4. lifecycle-rule-builder   -> "rules governing artifact lifecycle transitions"
```

### Crew: "Builder Certification Pack"
```
  1. prompt-template-builder  -> "template artifact under review"
  2. response-format-builder  -> "output format artifact under review"
  3. quality-gate-builder     -> "gates both artifacts must pass (score >= 8.0)"
  4. iso-package-builder      -> "packages certified artifacts into deployable unit"
```

## Handoff Protocol

### I Receive
- seeds: artifact kind, domain, required quality dimensions, minimum passing score
- optional: scoring rubric reference, existing gate definitions to extend, bypass policy conditions

### I Produce
- quality_gate artifact (YAML frontmatter + HARD gates list + SOFT gates list + scoring formula, max 4096 bytes)
- committed to: `cex/P11/examples/p11_qg_{name}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- scoring-rubric-builder: provides evaluation dimensions that map to SOFT gate contributions
- law-builder: inviolable laws become mandatory HARD gates with no bypass

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| validator-builder | Implements executable checks that enforce the gates I define |
| iso-package-builder | Uses my gates as acceptance criteria before packaging artifacts |
| bugloop-builder | Triggers fix cycles when gate scores fall below threshold |
| benchmark-builder | References my thresholds to define pass/fail on benchmark runs |
| every kind-builder | Each builder's QUALITY_GATES.md is produced by me |
