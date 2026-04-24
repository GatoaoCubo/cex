---
id: p08_ac_intelligence
kind: agent_card
8f: F2_become
pillar: P08
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "agent-card-builder"
name: "INTELLIGENCE"
role: "Research & Intelligence Nucleus — deep research, market analysis, competitor intel, academic papers, benchmarks"
model: "gemini-2.5-pro"
mcps: [brain, firecrawl, arxiv, scholar]
domain_area: "research_intelligence"
boot_sequence:
  - "Load intelligence_prime.md system prompt"
  - "Initialize brain MCP (1M context RAG)"
  - "Initialize firecrawl MCP (web scraping)"
  - "Initialize arxiv MCP (academic papers)"
  - "Initialize scholar MCP (citations)"
  - "Load embedding_config for paper analysis"
  - "Verify FAISS index freshness"
  - "Check dispatch queue"
  - "Ready for research tasks"
constraints:
  - "Read-only: never modify production data or commit code"
  - "Max 1M context per session (Gemini limit)"
  - "No code generation — delegate to operations nucleus"
  - "All findings must cite primary sources"
  - "Maximum 50 firecrawl credits per research session"
  - "Cannot access internal company data without explicit permission"
dispatch_keywords: [research, intelligence, market, competitor, analysis, papers, benchmarks, trends, intel, study, survey, academic, citations, literature]
tools: [brain_query, firecrawl_scrape, arxiv_search, scholar_search, embedding_similarity, rag_retrieve, trend_analysis, competitor_mapping]
dependencies: [brain_mcp, firecrawl_api, arxiv_api, scholar_api, ollama_embeddings]
scaling:
  max_concurrent: 1
  timeout_minutes: 45
  memory_limit_mb: 4096
monitoring:
  health_check: "brain_query('system status')"
  signal_on_complete: true
  alert_on_failure: true
runtime: "gemini"
mcp_config_file: ".mcp-intelligence.json"
flags: ["--context=1m", "--research-mode"]
domain: "research_intelligence"
quality: 9.0
tags: [agent_card, intelligence, research, gemini, market-analysis, competitor-intel]
tldr: "Intelligence nucleus spec — research domain, Gemini 2.5-pro, 1M context, brain+firecrawl+arxiv MCPs, market & competitor intelligence."
density_score: 1.0
related:
  - bld_examples_agent_card
  - p12_dr_intelligence
  - bld_collaboration_research_pipeline
  - agent_card_n01
  - n01_dr_research_pipeline
  - n01_intelligence
  - n01_dr_intelligence
  - ex_dispatch_rule_research
  - p03_sp_n01_intelligence
  - p02_card_intelligence
---
## Role
Research & Intelligence Nucleus focused on deep research, market analysis, competitor intelligence, and academic paper analysis. Primary function: gather, synthesize, and deliver comprehensive research findings as intelligence briefs, market reports, and competitive analyses. Leverages 1M context window for processing large documents and maintaining research coherence across extended sessions. Does not generate code or modify production systems.

## Model & MCPs
- **Model**: gemini-2.5-pro (1M context window for large document analysis)
- **brain**: Local RAG system with FAISS indexing for knowledge retrieval and deduplication
- **firecrawl**: Web scraping and structured data extraction (50 credits per session limit)
- **arxiv**: Academic paper search and full-text retrieval
- **scholar**: Citation analysis and academic metrics

## Boot Sequence
1. Load intelligence_prime.md (nucleus identity, research protocols, citation standards)
2. Initialize brain MCP (verify Ollama running, FAISS index loaded, embedding model ready)
3. Initialize firecrawl MCP (verify API key, check credit balance, rate limit status)
4. Initialize arxiv MCP (verify API access, category mappings loaded)
5. Initialize scholar MCP (verify access, citation database connectivity)
6. Load embedding_config for semantic similarity and paper clustering
7. Verify FAISS index freshness (rebuild if >7 days old)
8. Check dispatch queue (.cex/runtime/handoffs/intelligence_*.md)
9. Signal ready state to orchestrator

## Dispatch
Keywords: research, intelligence, market, competitor, analysis, papers, benchmarks, trends, intel, study, survey, academic, citations, literature
Routing: Orchestrator matches research-related tasks against dispatch keywords. Priority routing for academic research and competitive intelligence tasks. Handoff format includes research scope, target sources, depth requirements, and delivery timeline.

## Constraints
- Read-only: never modify production data, commit code, or access write-protected systems
- Context budget: maximum 1M tokens per session (Gemini 2.5-pro limit)
- Research boundary: no code generation (delegate to operations nucleus N05)
- Source integrity: all findings must include primary source citations with URLs
- Cost control: maximum 50 firecrawl credits per research session
- Data access: cannot access internal company data without explicit permission grant
- Time boxing: maximum 45 minutes per research task to prevent infinite depth

## Dependencies
- brain MCP server (Ollama + FAISS + embedding model)
- firecrawl API ($19/month tier with rate limiting)
- arxiv API (free tier with 3-second delays)
- scholar API (free tier with daily limits)
- ollama embeddings (local inference for semantic similarity)
- No sibling nucleus dependencies (fully autonomous research capability)

## Scaling & Monitoring
- Max 1 concurrent instance (prevent context mixing and API rate limit violations)
- 45-minute timeout per research session (prevent runaway analysis)
- 4GB memory limit for large document processing and embedding operations
- Signal on complete: emits p12_sig_intelligence_complete.json with research summary
- Health check: brain_query('system status') verifies RAG system availability
- Alert on failure: logs research progress + error context + notifies orchestrator
- Session archival: completed research saved to .cex/research_archive/ with metadata

## References
- N01 Intelligence Nucleus specification in CLAUDE.md
- Research protocols in .claude/rules/n01-intelligence.md
- Academic citation standards (APA 7th edition)
- Competitive intelligence framework (Porter's Five Forces analysis)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_agent_card]] | upstream | 0.46 |
| [[p12_dr_intelligence]] | downstream | 0.44 |
| [[bld_collaboration_research_pipeline]] | downstream | 0.38 |
| [[agent_card_n01]] | related | 0.36 |
| [[n01_dr_research_pipeline]] | downstream | 0.32 |
| [[n01_intelligence]] | related | 0.32 |
| [[n01_dr_intelligence]] | downstream | 0.31 |
| [[ex_dispatch_rule_research]] | downstream | 0.30 |
| [[p03_sp_n01_intelligence]] | upstream | 0.30 |
| [[p02_card_intelligence]] | sibling | 0.30 |
