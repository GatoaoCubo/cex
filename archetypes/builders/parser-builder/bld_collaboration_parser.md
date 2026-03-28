---
kind: collaboration
id: bld_collaboration_parser
pillar: P05
llm_function: COLLABORATE
purpose: How parser-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: parser-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should raw output be parsed into structured data?"
I produce extraction rules, regex patterns, JSON paths, and normalization pipelines. I do NOT format output for display (formatter-builder) or validate content correctness (validator-builder).

## Crew Compositions

### Crew: "LLM Output Processing Pipeline"
```
  1. response-format-builder -> "defines the expected output structure from the LLM"
  2. parser-builder          -> "builds extractor to pull fields from that structure"
  3. validator-builder       -> "validates extracted data meets schema constraints"
```

### Crew: "Scraper + Extractor"
```
  1. scraper-builder         -> "fetches raw HTML/JSON from external sources"
  2. parser-builder          -> "extracts structured fields from the raw content"
  3. formatter-builder       -> "formats extracted data for downstream consumption"
```

### Crew: "Agent Output Routing"
```
  1. instruction-builder     -> "defines agent steps that produce raw output"
  2. parser-builder          -> "extracts structured fields from agent output"
  3. dispatch-rule-builder   -> "routes downstream work based on parsed fields"
```

## Handoff Protocol

### I Receive
- seeds: raw output sample (text/JSON/HTML/log), target field names, desired output format
- optional: error handling requirements, fallback extraction strategy, normalization rules

### I Produce
- parser artifact (Markdown, max 4KB)
- committed to: `cex/P05/examples/p05_parser_{scope}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- response-format-builder: defines the structure I will extract from
- scraper-builder: produces the raw content I parse

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| validator-builder | validates the structured data I extracted |
| formatter-builder | receives my structured output to render for display |
| dispatch-rule-builder | routes on parsed fields I extracted |
| knowledge-card-builder | ingests parsed structured data as knowledge facts |
