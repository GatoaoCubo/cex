---
pillar: P12
llm_function: COLLABORATE
purpose: How formatter-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: formatter-builder

## My Role in Crews
I am a PRESENTER. I answer ONE question: "how should this structured data be displayed?"
I do not extract data. I do not validate content.
I PRESENT so consumers can read, display, or transmit formatted data.

## Crew Compositions

### Crew: "Output Pipeline" (standard)
```
  1. agent-builder                 -> "agent produces raw output"
  2. parser-builder                -> "extract structured data from output"
  3. formatter-builder             -> "present extracted data in target format"
  4. validator-builder [PLANNED]   -> "validate formatted output against rules"
```

### Crew: "Report Generation"
```
  1. knowledge-card-builder        -> "distill facts from research"
  2. formatter-builder             -> "render facts as Markdown table or HTML"
  3. quality-gate-builder          -> "validate report completeness"
```

### Crew: "API Response Pipeline"
```
  1. parser-builder                -> "extract data from LLM response"
  2. formatter-builder             -> "serialize as JSON with escaping"
  3. validator-builder [PLANNED]   -> "validate JSON against output_schema"
```

## Handoff Protocol

### I Receive
- seeds: target_format, input data structure, sample data
- optional: template (pre-defined formatting template)
- optional: locale (for number/date formatting)

### I Produce
- formatter artifact: `cex/P05_output/examples/p05_fmt_{slug}.md`
- committed to: archetypes or pool depending on quality score

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures

## Builders I Depend On
- parser-builder: provides structured data that formatter presents (upstream)

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| validator-builder [PLANNED] | Validates data that formatter presented |

## Cross-Reference Norm (BUILDER_NORMS Rule 12)
parser-builder lists formatter-builder as downstream dependent (provides structured data).
This file lists parser-builder as upstream dependency.
The cross-reference is bidirectional.
