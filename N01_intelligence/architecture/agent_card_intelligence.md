---
id: n01_ac_intelligence
kind: agent_card
pillar: P08
title: "Agent Card: N01 Research & Intelligence Nucleus"
version: "1.0.0"
created: "2026-03-31"
updated: "2026-03-31"
author: "N01_rebuild_8F"
quality: 8.8
tags: [agent_card, deployment, architecture, n01, research, gemini-2.5-pro]
tldr: "Deployment and configuration specification for the N01 Research & Intelligence Nucleus agent, defining its model, runtime parameters, linked artifacts, and boot sequence."
---

## 1. AGENT IDENTITY
- **Agent ID**: `n01_agent_intelligence`
- **Name**: N01 Research & Intelligence Nucleus
- **Domain**: `research, market analysis, competitor intelligence, papers, benchmarks`
- **Role**: `Expert Researcher and Intelligence Analyst`

## 2. MODEL CONFIGURATION
- **Model Provider**: `Google`
- **Model Name**: `gemini-2.5-pro`
- **Context Window**: `1,048,576 tokens`
- **Optimal Temperature**: `0.25` (tuned for high-fidelity, evidence-based reasoning and synthesis)
- **Subscription Tier**: `CEX Enterprise Account`

## 3. RUNTIME ARTIFACTS
This agent is a composition of the following artifacts which MUST be loaded at runtime:
- **Agent Definition**: `n01_agent_intelligence`
- **System Prompt**: `n01_sp_intelligence`
- **Domain Knowledge**: `n01_kc_intelligence_domain`
- **Dispatch Rule**: `n01_dispatch_rule_intelligence`
- **RAG Configuration**: `n01_rag_source_intelligence`

## 4. FUTURE TOOLCHAIN (MCPs & Functions)
The following tools are designed for N01 but are pending implementation:
- **MCP Servers**:
  - `google_scholar_mcp`: For searching and retrieving academic papers.
  - `arxiv_mcp`: For accessing pre-print scientific articles.
  - `sec_edgar_mcp`: For fetching corporate financial filings.
  - `high_quality_web_search_mcp`: For targeted searches on reputable news and industry sites.
- **Local Functions**:
  - `semantic_search`: To run vector search against the RAG knowledge base.
  - `citation_graph`: To analyze citation networks between papers.
  - `advanced_summarizer`: To create summaries of various lengths and complexities.

## 5. BOOT SEQUENCE
1.  **Instantiate Agent**: Create an instance of `n01_agent_intelligence`.
2.  **Load Persona**: Inject the `n01_sp_intelligence` system prompt to establish identity and operational rules.
3.  **Load Knowledge**: Inject the `n01_kc_intelligence_domain` knowledge card to provide domain context and methodologies.
4.  **Mount Vectorstore**: Connect to the RAG vector database specified in `n01_rag_source_intelligence`.
5.  **Arm Dispatch**: Activate the agent to listen for incoming requests that match the criteria in `n01_dispatch_rule_intelligence`.

## 6. OPERATIONAL CONSTRAINTS & GUARANTEES
- **Hard Constraints**:
  - The agent MUST NOT respond to requests outside the defined `knowledge_boundary`.
  - All analytical claims MUST have a verifiable source citation.
  - The output MUST conform to the structured `Intelligence Brief` format.
- **Guarantees**:
  - High-fidelity analysis based on provided sources.
  - Explicitly states confidence levels for judgments.
  - Identifies and lists information gaps.
