---
pillar: P12
llm_function: COLLABORATE
purpose: How scraper-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: scraper-builder

## My Role in Crews
I am a WEB EXTRACTION SPECIALIST. I answer ONE question: "what data does this scraper
extract from the target site, and in what format?"
I do not define agent identity. I do not write skill phases. I do not implement code.
I DEFINE EXTRACTION CONTRACTS so agents know exactly what data they can collect.

## Crew Compositions

### Crew: "Market Intelligence Pipeline"
```
  1. scraper-builder         -> "scraper spec: selectors, pagination, output"
  2. client-builder          -> "API client for enrichment data"
  3. knowledge-card-builder  -> "knowledge card from scraped data"
  4. agent-builder [PLANNED] -> "research agent wired to scraper + client"
```

### Crew: "Competitive Monitoring"
```
  1. scraper-builder         -> "price/product scraper for competitors"
  2. cli-tool-builder        -> "CLI tool for diff/comparison of snapshots"
  3. quality-gate-builder    -> "data quality validation for scraped results"
```

### Crew: "Scraper Audit"
```
  1. scraper-builder         -> "current scraper spec"
  2. validator-builder       -> "validate selector freshness"
  3. knowledge-card-builder  -> "capture learnings from audit"
```

## Handoff Protocol

### I Receive
- seeds: target site URL, data fields to extract
- optional: pagination strategy, rate limit requirements
- optional: anti-bot assessment, proxy needs

### I Produce
- scraper artifact: `p04_scraper_{target_slug}.md` + `.yaml`
- committed to: `cex/P04_tools/examples/p04_scraper_{target_slug}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures

## Builders I Depend On
- knowledge-card-builder: provides domain knowledge about the target site
- client-builder: if scraper has API fallback, need client spec

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| knowledge-card-builder | Scraped data becomes knowledge cards |
| cli-tool-builder | CLI tools may post-process scraped data |
| agent-builder [PLANNED] | Research agents use scrapers for data collection |
| connector-builder | Connectors may sync scraped data to external systems |
