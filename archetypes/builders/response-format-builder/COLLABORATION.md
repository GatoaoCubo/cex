---
pillar: P12
llm_function: COLLABORATE
purpose: How response-format-builder works in crews
---

# Collaboration: response-format-builder

## My Role
I define HOW the LLM should structure its output during generation.
I do not enforce output structure after generation (validation-schema-builder).
I do not extract data from output (parser-builder).

## Crew: "Output Quality Pipeline"
```
  1. response-format-builder    -> tells LLM how to structure output
  2. validation-schema-builder  -> system validates generated output
  3. quality-gate-builder       -> enforces quality score threshold
```

## Crew: "Agent Output Design"
```
  1. response-format-builder    -> defines output structure for agent
  2. parser-builder [PLANNED]   -> defines how to extract data from output
  3. formatter-builder [PLANNED] -> defines how to transform format
```

## Handoff Protocol
### I Receive
- seeds: target_kind, format_type, sections needed, consumption pattern
- optional: existing output examples, validation_schema reference

### I Produce
- response_format artifact in P05_output/examples/
- committed to: cex/P05_output/examples/p05_rf_{format_slug}.yaml

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None directly. Independent at layer 0.
- artifact-blueprint-builder [PLANNED]: provides shape definition (optional)

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| validation-schema-builder | Designs system-side checks aligned to the format |
| parser-builder [PLANNED] | Extracts data from output formatted by this spec |
| system-prompt-builder [PLANNED] | Includes response_format in agent prompts |
