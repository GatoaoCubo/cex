---
pillar: P12
llm_function: COLLABORATE
purpose: How interface-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: interface-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is the formal contract between these two agents/systems?"
I do not implement communication. I do not validate data.
I SPECIFY contracts so connector-builder and downstream consumers can implement correctly.

## Crew Compositions

### Crew: "Agent Integration Pipeline"
```
  1. interface-builder -> "defines bilateral contract (methods, IO)"
  2. input-schema-builder -> "defines input contract for each method"
  3. connector-builder [PLANNED] -> "implements the interface"
  4. validator-builder -> "creates validators for contract compliance"
```

### Crew: "Satellite Wiring"
```
  1. interface-builder -> "defines inter-satellite contract"
  2. signal-builder [PLANNED] -> "defines completion/error events"
  3. dispatch-rule-builder [PLANNED] -> "routes requests to correct satellite"
```

## Handoff Protocol

### I Receive
- seeds: provider name, consumer name, integration purpose
- optional: existing method signatures, versioning requirements

### I Produce
- interface artifact (YAML)
- committed to: `cex/P06_schema/examples/p06_iface_{contract_slug}.yaml`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None. Interfaces are INDEPENDENT — they can be built from requirements alone.
Optional enrichment from input-schema-builder for method input shapes.

## Builders That Depend On Me [PLANNED]

| Builder | Why |
|---------|-----|
| connector-builder [PLANNED] | Implements interface methods at runtime |
| validator-builder | Creates compliance checks for the interface |
| signal-builder [PLANNED] | Models events that flow through the interface |
