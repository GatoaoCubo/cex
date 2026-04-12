---
id: p04_tool_mcp_config
kind: tool_config
pillar: P04
title: "MCP Server Orchestration Config -- N01 Intelligence"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n01_intelligence
agent_group: n01-research-analyst
domain: research-intelligence
quality: 8.9
tags: [tool-config, mcp, server, orchestration, n01, pipeline]
tldr: "Orchestration config for N01's 5 MCP servers -- startup sequence, health checks, fallback chains, and pipeline coordination for the discover-extract-convert-structure-publish research flow."
density_score: 0.92
---

## Purpose

N01 operates 5 MCP servers that form a research pipeline: discover (brave-search) -> extract (firecrawl/fetch) -> convert (markitdown) -> structure (8F) -> publish (notebooklm). This config defines startup order, health verification, fallback behavior, and pipeline coordination. Without it, servers are started ad-hoc, failures cascade silently, and pipeline ordering breaks.

## Server Registry

| # | Server | Command | Port/Protocol | Startup Order | Required? |
|---|--------|---------|---------------|---------------|-----------|
| 1 | brave-search | `npx @anthropic/mcp-server-brave-search` | MCP stdio | 1st | YES -- discovery phase |
| 2 | firecrawl | `npx firecrawl-mcp` | MCP stdio | 2nd | YES -- primary extraction |
| 3 | fetch | `uvx mcp-server-fetch` | MCP stdio | 2nd (parallel with firecrawl) | NO -- fallback extraction |
| 4 | markitdown | `npx markitdown-mcp` | MCP stdio | 3rd | CONDITIONAL -- only for PDF/DOCX |
| 5 | notebooklm | `npx notebooklm-mcp@latest` | MCP stdio | 4th (last) | NO -- publish phase optional |

## Startup Sequence

```
Phase 1: Discovery     → Start brave-search
Phase 2: Extraction    → Start firecrawl + fetch (parallel)
Phase 3: Conversion    → Start markitdown (if PDF/DOCX detected)
Phase 4: Publication   → Start notebooklm (if publish requested)
```

### Lazy Loading

Not all servers are needed for every research task. Start servers on-demand:

| Research Type | Servers Needed |
|---------------|---------------|
| Quick market check | brave-search only |
| Competitive grid | brave-search + firecrawl |
| Paper review | brave-search + fetch + markitdown |
| Full pipeline | All 5 |
| Internal-only research | None (use cex_retriever.py) |

## Health Checks

| Server | Health Command | Expected Response | Timeout |
|--------|---------------|-------------------|---------|
| brave-search | `mcp({ server: "brave-search" })` | Tool list returned | 10s |
| firecrawl | `mcp({ server: "firecrawl" })` | Tool list returned | 10s |
| fetch | `mcp({ server: "fetch" })` | Tool list returned | 5s |
| markitdown | `mcp({ server: "markitdown" })` | Tool list returned | 5s |
| notebooklm | `mcp({ server: "notebooklm" })` | Tool list returned | 15s |

### Health Check Frequency

- **On startup**: Verify each server before first use
- **On error**: Re-check after any 5xx/timeout response
- **Periodic**: Not needed (MCP servers are stateless per-request)

## Fallback Chains

| Primary | Fallback | When to Switch |
|---------|----------|---------------|
| firecrawl | fetch | firecrawl returns error, timeout, or empty result |
| brave-search | (none) | No fallback -- discovery is essential. If brave fails, use internal knowledge only |
| markitdown | (manual copy-paste) | If markitdown fails on a PDF, extract key sections manually |
| notebooklm | (skip publish) | Publishing is optional -- research quality unaffected |

## Pipeline Coordination

### Data Flow Between Servers

```
brave-search → URLs list
    ↓
firecrawl/fetch → Raw content (HTML/PDF/markdown)
    ↓
markitdown → Clean markdown (if PDF/DOCX input)
    ↓
[8F Pipeline] → Structured artifact
    ↓
notebooklm → Published audio/content (optional)
```

### Handoff Format

Each server passes data to the next via:
- **URLs**: Plain text list, one per line
- **Content**: Markdown format (firecrawl outputs markdown natively)
- **Metadata**: YAML frontmatter appended by each stage

### Error Handling

| Error Type | Action | Log Level |
|------------|--------|-----------|
| Server not started | Start on demand (lazy) | INFO |
| Server timeout | Retry once, then fallback | WARN |
| Server crash | Log error, skip server, continue pipeline | ERROR |
| Rate limit (429) | Wait per scraping_config backoff schedule | WARN |
| Empty result | Log, try next source/URL, continue | INFO |

## Environment Variables

| Variable | Purpose | Default |
|----------|---------|---------|
| `BRAVE_API_KEY` | Brave Search API authentication | (required if using brave-search) |
| `FIRECRAWL_API_KEY` | Firecrawl API authentication | (required if using firecrawl) |
| `MCP_TIMEOUT_MS` | Global MCP request timeout | 30000 |
| `GOOGLE_ACCOUNT` | NotebookLM authentication | financeiro@gatoaocubo3.com |

## Comparison to Alternative Architectures

| Architecture | Pros | Cons | N01 Verdict |
|-------------|------|------|-------------|
| **Sequential pipeline (current)** | Simple, predictable, debuggable | Slower (serial execution) | CHOSEN -- reliability > speed for research |
| **Parallel fan-out** | Fast (all servers simultaneously) | Complex error handling, wasted requests | Rejected -- most tasks don't need all servers |
| **Event-driven (pub/sub)** | Scalable, decoupled | Overkill for 5 servers, debugging nightmare | Rejected -- over-engineering |
| **Single mega-server** | Simple deployment | Vendor lock-in, single point of failure | Rejected -- loses MCP composability |
