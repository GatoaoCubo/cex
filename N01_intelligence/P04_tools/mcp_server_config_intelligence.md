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
quality: 9.1
tags: [tool-config, mcp, server, orchestration, n01, pipeline]
tldr: "Orchestration config for N01's 5 MCP servers -- startup sequence, health checks, fallback chains, and pipeline coordination for the discover-extract-convert-structure-publish research flow."
density_score: 0.92
related:
  - p04_tool_scraping_config
  - bld_memory_mcp_server
  - p01_kc_mcp_server
  - mcp-server-builder
  - bld_collaboration_mcp_server
  - p01_kc_mcp_server_patterns
  - n04_self_audit_20260408
  - agent_card_n01
  - p10_lr_research_sessions
  - p11_qg_mcp_server
---

## Purpose

N01 operates 5 MCP servers that form a research pipeline: discover (brave-search) -> extract (firecrawl/fetch) -> convert (markitdown) -> structure (8F) -> publish (notebooklm). This config defines startup order, health verification, fallback behavior, and pipeline coordination. Without it, servers are started ad-hoc, failures cascade silently, and pipeline ordering breaks.

## Boundary

This artifact defines the orchestration rules for N01's 5 MCP servers in the research pipeline. It is NOT a general-purpose server configuration, but specifically addresses startup sequences, health checks, fallback chains, and pipeline coordination for the discover-extract-convert-structure-publish workflow.

## Related Kinds

- **pipeline_config**: Defines the sequence and dependencies between research stages
- **server_automation**: Handles on-demand server activation and deactivation
- **research_workflow**: Specifies the overall research process that this config supports
- **error_handling**: Manages failure scenarios across the MCP ecosystem
- **api_authentication**: Provides credentials required for external services like Brave and Firecrawl

## Server Registry

| # | Server | Command | Port/Protocol | Startup Order | Required? |
|---|---|---|---|---|---|
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
|------|-------------|
| Quick market check | brave-search only |
| Competitive grid | brave-search + firecrawl |
| Paper review | brave-search + fetch + markitdown |
| Full pipeline | All 5 |
| Internal-only research | None (use cex_retriever.py) |

## Health Checks

| Server | Health Command | Expected Response | Timeout |
|--------|------|-----|-----|
| brave-search | `mcp({ server: "brave-search" })` | Tool list returned | 10s |
| firecrawl | `mcp({ server: "firecrawl" })` | Tool list returned | 10s |
| fetch | `mcp({ server: "fetch" })` | Tool list returned | 10s |
| markitdown | `mcp({ server: "markitdown" })` | Tool list returned | 10s |
| notebooklm | `mcp({ server: "notebooklm" })` | Tool list returned | 10s |

## Health Check Frequency

| Trigger | Action | Frequency | Notes |
|--------|------|---------|-----|
| On startup | Verify each server before first use | Once per server | Ensures readiness before processing |
| On error | Re-check after any 5xx/timeout response | Immediately | Prevents cascading failures |
| Periodic | Not needed | N/A | Servers are stateless per-request |

## Fallback Chains

| Scenario | Fallback Action | Recovery Time |
|--------|------|-----|
| brave-search failure | Use cached search results | <5s |
| firecrawl failure | Switch to fetch | <2s |
| markitdown failure | Skip conversion, proceed to structure | <1s |
| notebooklm failure | Save output to disk, notify user | <3s |

## Error Handling

| Error Type | Description | Resolution |
|--------|------|-----|
| 503 Service Unavailable | Server overload | Retry after 10s |
| 401 Unauthorized | Authentication failure | Re-authenticate with stored credentials |
| 404 Not Found | Resource missing | Log error, skip processing |
| 500 Internal Server Error | Unexpected failure | Restart server, notify admin |
| Timeout | No response from server | Fallback to cached data |

## Data Flow Between Servers

```
brave-search → firecrawl → fetch → markitdown → 8F → notebooklm
```

## Handoff Format

- **brave-search → firecrawl**: JSON with search terms and metadata
- **firecrawl → fetch**: JSON with URLs and priority flags
- **fetch → markitdown**: PDF/DOCX files with source URLs
- **markitdown → 8F**: Structured text with metadata
- **8F → notebooklm**: Final structured data with analysis

## Comparison to Alternative Architectures

| Architecture | Pros | Cons | N01 Decision |
|--------|------|-----|-----|
| Monolithic | Simpler deployment | Single point of failure | Rejected for reliability |
| Decentralized | High availability | Complex coordination | Chosen for scalability |
| Stateless | Easier scaling | No session persistence | Chosen for performance |
| Centralized | Easier monitoring | Bottleneck risk | Rejected for latency |

## Environment Variables

| Variable | Value | Description |
|--------|------|-----|
| BRAVE_API_KEY | `xxx-xxx-xxx` | Authentication for Brave Search |
| FIRECRAWL_API_KEY | `yyy-yyy-yyy` | Authentication for Firecrawl |
| FETCH_API_KEY | `zzz-zzz-zzz` | Authentication for Fetch |
| MARKITDOWN_API_KEY | `aaa-aaa-aaa` | Authentication for Markitdown |
| NOTEBOOKLM_API_KEY | `bbb-bbb-bbb` | Authentication for NotebookLM |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_tool_scraping_config]] | sibling | 0.41 |
| [[bld_memory_mcp_server]] | downstream | 0.37 |
| [[p01_kc_mcp_server]] | upstream | 0.37 |
| [[mcp-server-builder]] | related | 0.36 |
| [[bld_collaboration_mcp_server]] | related | 0.36 |
| [[p01_kc_mcp_server_patterns]] | upstream | 0.35 |
| [[n04_self_audit_20260408]] | upstream | 0.34 |
| [[agent_card_n01]] | related | 0.33 |
| [[p10_lr_research_sessions]] | downstream | 0.31 |
| [[p11_qg_mcp_server]] | downstream | 0.31 |
