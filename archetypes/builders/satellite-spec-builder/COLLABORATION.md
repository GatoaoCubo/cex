---
pillar: P12
llm_function: COLLABORATE
purpose: How satellite-spec-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: satellite-spec-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is this satellite's role, model, tools, and constraints?"
I do not implement agents. I do not configure boot providers.
I SPECIFY satellites so spawn systems and orchestrators can launch them correctly.

## Crew Compositions

### Crew: "Satellite Design"
```
  1. satellite-spec-builder -> "defines satellite architecture"
  2. agent-builder -> "creates agents that run inside the satellite"
  3. boot-config-builder -> "configures per-provider initialization"
```

### Crew: "System Architecture"
```
  1. satellite-spec-builder -> "specs each satellite"
  2. pattern-builder [PLANNED] -> "documents reusable patterns across satellites"
  3. law-builder [PLANNED] -> "defines constraints that apply to all satellites"
```

### Crew: "Deployment Pipeline"
```
  1. satellite-spec-builder -> "defines what to deploy"
  2. spawn-config-builder [PLANNED] -> "configures how to launch"
  3. signal-builder -> "monitors execution status"
```

## Handoff Protocol

### I Receive
- seeds: satellite name, domain, model preference
- optional: MCP list, constraints, dispatch keywords, scaling requirements

### I Produce
- satellite_spec artifact (YAML)
- committed to: `cex/P08_architecture/examples/p08_sat_{name_lower}.yaml`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None. Satellite specs can be built from a name and domain alone.
Optional: pattern-builder output for design pattern references.

## Builders That Depend On Me [PLANNED]

| Builder | Why |
|---------|-----|
| agent-builder | Agents reference satellite spec for context |
| boot-config-builder | Boot config implements satellite's init sequence |
| spawn-config-builder [PLANNED] | Spawn config reads satellite spec to launch |
| signal-builder | Signals reference satellite as emitter |
