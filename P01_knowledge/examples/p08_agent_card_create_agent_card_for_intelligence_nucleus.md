---
id: p08_ac_intelligence
kind: agent_card
pillar: P08
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "agent-card-builder"
name: "intelligence"
role: "Research and intelligence nucleus — deep analysis of papers, market research, competitor intelligence, and trend analysis using large context processing"
model: "gemini-2.5-pro"
mcps: [web_search, document_processor, rag_source]
domain_area: "research_intelligence"
boot_sequence:
  - "Load n01_intelligence system prompt"
  - "Initialize web search MCP"
  - "Initialize document processor MCP"
  - "Initialize RAG source connections"
  - "Verify 1M context availability"
  - "Load research domain context"
  - "Ready for intelligence tasks"
constraints:
  - "Read-only: never build or modify artifacts"
  - "No marketing copy generation — delegate to N02"
  - "No code generation — delegate to N05"
  - "Must cite all sources in research outputs"
  - "Cannot exceed 1M token context limit"
dispatch_keywords: [research, intelligence, analysis, papers, market, competitor, trends, benchmarks, study, investigation]
tools: [web_search, document_extract, paper_analysis, market_research, competitor_scan, trend_analysis]
dependencies: [web_search_mcp, document_processor_mcp, rag_source_config]
scaling:
  max_concurrent: 1
  timeout_minutes: 60
  memory_limit_mb: 4096
monitoring:
  health_check: "web_search('test query')"
  signal_on_complete: true
  alert_on_failure: true
runtime: "gemini"
mcp_config_file: ".mcp-intelligence.json"
flags: ["--context-1m", "--research-mode"]
domain: "research-intelligence"
quality: 8.8
tags: [agent_node, intelligence, research, n01, analysis, papers]
tldr: "Intelligence nucleus spec — research domain, gemini-2.5-pro model, 1M context, deep analysis capabilities for papers and market research."
density_score: 1.0
---
## Role
Intelligence nucleus focused on research, market analysis, competitor intelligence, and academic paper review. Primary function: gather, analyze, and synthesize information from large documents and multiple sources into actionable intelligence briefs. Does not build artifacts, generate marketing copy, or write code.

## Model & MCPs
- **Model**: gemini-2.5-pro (1M context window for large document processing)
- **web_search**: Real-time web search and information gathering
- **document_processor**: PDF, academic paper, and document analysis
- **rag_source**: Knowledge base search and retrieval

## Boot Sequence
1. Load n01_intelligence system prompt (research methodology, analysis frameworks)
2. Initialize web search MCP (verify API access, rate limits)
3. Initialize document processor MCP (PDF parsing, text extraction)
4. Initialize RAG source connections (knowledge base, paper database)
5. Verify 1M context availability (model capacity check)
6. Load research domain context (research templates, citation formats)
7. Ready for intelligence tasks

## Dispatch
Keywords: research, intelligence, analysis, papers, market, competitor, trends, benchmarks, study, investigation
Routing: Orchestrator routes research-heavy tasks requiring deep analysis and large context processing.
Priority: Intelligence tasks take precedence for comprehensive analysis requirements.

## Constraints
- Read-only: never build artifacts or modify system files
- Domain boundary: no marketing copy generation (delegate to N02)
- Domain boundary: no code generation or deployment (delegate to N05)
- Quality requirement: all findings must include source citations
- Technical limit: cannot exceed 1M token context per session

## Dependencies
- web_search MCP server (real-time information access)
- document_processor MCP (academic paper and PDF analysis)
- rag_source configuration (knowledge base connections)
- No sibling nucleus dependencies (operates independently)

## Scaling & Monitoring
- Max 1 concurrent instance (large context model limitation)
- 60-minute timeout per research session
- Signal on complete: emits p12_sig_intelligence_complete.json
- Alert on failure: logs research errors and notifies orchestrator
- Heartbeat every 10 minutes for long-running analysis tasks

## References
- N01 Intelligence Rules (.claude/rules/n01-intelligence.md)
- Research methodology frameworks (academic standards)
- Citation format standards (APA, MLA, Chicago)