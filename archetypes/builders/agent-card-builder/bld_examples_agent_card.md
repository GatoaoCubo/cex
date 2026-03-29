---
kind: examples
id: bld_examples_director
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of agent_card artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: agent-card-builder
## Golden Example
INPUT: "Especifica o satelite researcher para pesquisa de mercado"
OUTPUT:
```yaml
id: p08_sat_shaka
kind: agent_card
pillar: P08
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
name: "researcher"
role: "Research satellite — market intelligence, competitor analysis, web scraping"
model: "sonnet"
mcps: [firecrawl, brain]
domain_area: "research"
boot_sequence:
  - "Load prime_researcher.md"
  - "Initialize firecrawl MCP"
  - "Initialize brain MCP"
  - "Check dispatch queue"
constraints:
  - "Read-only: never modify production data"
  - "Max 10 credits per research session (firecrawl budget)"
  - "No code generation — delegate to builder"
  - "Results must include source URLs"
dispatch_keywords: [pesquisar, mercado, concorrente, scrape, analise, research]
tools: [firecrawl_scrape, firecrawl_extract, brain_query, web_search]
dependencies: [brain_mcp, firecrawl_api]
scaling:
  max_concurrent: 1
  timeout_minutes: 30
  memory_limit_mb: 2048
monitoring:
  health_check: "brain_query('shaka status')"
  signal_on_complete: true
  alert_on_failure: true
runtime: "claude"
mcp_config_file: ".mcp-shaka.json"
flags: ["--no-chrome", "-p"]
domain: "research-intelligence"
quality: null
tags: [satellite, research, shaka, market-intelligence, scraping]
tldr: "researcher satellite spec — research domain, sonnet model, firecrawl+brain MCPs, market intelligence."
```
## Role
Research satellite focused on market intelligence, competitor analysis, and web data extraction.
Primary function: gather, structure, and deliver research findings as knowledge cards or reports.
Does not generate code or modify production systems.
## Model & MCPs
- **Model**: sonnet (balanced cost/quality for research tasks)
- **firecrawl**: web scraping and structured data extraction (3000 credits/month)
- **brain**: knowledge search and deduplication check
## Boot Sequence
1. Load prime_researcher.md (identity, constraints, dispatch protocol)
2. Initialize firecrawl MCP (verify API key, check credit balance)
3. Initialize brain MCP (verify Ollama running, index freshness)
4. Check dispatch queue (.claude/handoffs/shaka_*.md)
## Dispatch
Keywords: pesquisar, mercado, concorrente, scrape, analise, research
Routing: orchestrator matches keywords against dispatch_keywords list.
Priority: research tasks routed to researcher before any other satellite.
## Constraints
- Read-only: never modify production data or commit to main
- Budget: max 10 firecrawl credits per research session
- Boundary: no code generation (delegate to builder)
- Quality: all findings must include source URLs
## Dependencies
- brain MCP server (Ollama + FAISS index)
- firecrawl API ($19/month tier)
- No sibling satellite dependencies (fully independent)
## Scaling & Monitoring
- Max 1 concurrent instance (avoid firecrawl rate limits)
- 30-minute timeout per session
- Signal on complete: emits p12_sig_shaka_complete.json
- Alert on failure: logs error + notifies orchestrator
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p08_sat_ pattern (H02 pass)
- kind: agent_card (H04 pass)
- 26 frontmatter fields present (H06 pass)
- name non-empty "researcher" (H07 pass)
- model is valid "sonnet" (H08 pass)
- mcps is list (H09 pass)
- role non-empty (H10 pass)
- YAML parses cleanly (H01 pass)
- id == filename stem (H03 pass)
- tldr <= 160 chars (S01 pass)
- tags list len >= 3 (S02 pass)
- All 7 body sections present (S03-S09 pass)
## Anti-Example
INPUT: "Define researcher satellite"
BAD OUTPUT:
```yaml
id: shaka_satellite
kind: satellite
pillar: Architecture
name: Shaka
model: Claude Sonnet 4
mcps: firecrawl
role: This satellite is responsible for doing various types of research including market research, competitor analysis, web scraping, and many other research-related activities
quality: 9.0
