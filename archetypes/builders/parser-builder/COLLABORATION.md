---
pillar: P12
llm_function: COLLABORATE
purpose: How parser-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: parser-builder

## My Role in Crews
I am an EXTRACTOR. I answer ONE question: "how do we get structured data from this raw output?"
I do not format output. I do not validate content.
I EXTRACT so downstream consumers can work with clean, typed data.

## Crew Compositions

### Crew: "Output Pipeline" (standard)
```
  1. agent-builder                 -> "agent produces raw output"
  2. parser-builder                -> "extract structured data from output"
  3. formatter-builder [PLANNED]   -> "present extracted data for display"
  4. validator-builder [PLANNED]   -> "validate extracted data against rules"
```

### Crew: "Scraper Pipeline"
```
  1. scraper (P04 tool)            -> "collect raw HTML/JSON from web"
  2. parser-builder                -> "extract product data from scraped content"
  3. knowledge-card-builder        -> "distill extracted data into knowledge"
```

### Crew: "LLM Output Processing"
```
  1. output-schema-builder [PLANNED] -> "define expected output format"
  2. parser-builder                  -> "extract fields from LLM response"
  3. quality-gate-builder            -> "validate extraction completeness"
```

## Handoff Protocol

### I Receive
- seeds: input_format, target fields, sample input data
- optional: output_schema (target structure for extraction)
- optional: scraper output (raw HTML/JSON to parse)

### I Produce
- parser artifact: `cex/P05_output/examples/p05_parser_{slug}.md`
- committed to: archetypes or pool depending on quality score

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures

## Builders I Depend On
None (parser-builder is independent — it defines extraction rules from domain knowledge).

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| formatter-builder [PLANNED] | Needs parsed structured data to format for presentation |
| validator-builder [PLANNED] | Validates data that parser extracted |
| knowledge-card-builder | Distills extracted data into atomic knowledge facts |

## Cross-Reference Norm (BUILDER_NORMS Rule 12)
formatter-builder [PLANNED] will list parser-builder as upstream (provides structured data).
This file lists formatter-builder as downstream dependent.
The cross-reference will be bidirectional when formatter-builder is created.
