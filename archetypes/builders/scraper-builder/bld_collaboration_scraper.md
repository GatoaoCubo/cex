---
pillar: P04
llm_function: COLLABORATE
purpose: How scraper-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: scraper-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what data does this scraper extract, from where, and in what format?"
I define web data extraction artifacts — target site, CSS/XPath selectors, pagination strategy, rate limiting, and output format. I do NOT handle structured API consumption (client-builder), bidirectional sync (connector-builder), LLM output parsing (parser-builder), or MCP protocol exposure (mcp-server-builder).

## Crew Compositions

### Crew: "Market Data Pipeline"
```
  1. scraper-builder        -> "extracts raw product/price data from HTML pages with selectors and pagination"
  2. parser-builder         -> "cleans and normalizes the scraped raw output into structured records"
  3. knowledge-card-builder -> "packages the structured data as a knowledge card for downstream use"
```

### Crew: "Competitive Intelligence Automation"
```
  1. scraper-builder     -> "defines extraction rules for competitor sites (selectors, rate limits, anti-bot)"
  2. formatter-builder   -> "transforms scraped JSON/CSV into a consistent comparison format"
  3. dag-builder         -> "assembles scraper + formatter + storage into a scheduled extraction pipeline"
```

### Crew: "Data Source Integration"
```
  1. scraper-builder     -> "handles sites with no API: defines HTML extraction with CSS selectors"
  2. client-builder      -> "handles sites with a structured API: defines typed request/response clients"
  3. connector-builder   -> "wraps both into a bidirectional sync layer for the target system"
```

## Handoff Protocol

### I Receive
- seeds: target site URL, data fields needed, pagination type, output format preference
- optional: rate limit tolerance, known anti-bot measures, proxy requirements, example HTML snippet

### I Produce
- scraper artifact (YAML frontmatter + selectors + pagination config, max 200 lines)
- committed to: `cex/P04/examples/scraper-{site-name}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- None required. Scraper specs are self-contained from a target URL and field list.

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| parser-builder      | receives raw scraper output format to define normalization rules |
| connector-builder   | uses scraper as the read-side of a bidirectional data sync |
| dag-builder         | places scraper as a source node in data extraction pipelines |
| smoke-eval-builder  | needs the scraper's selectors and target URL to write health checks |
