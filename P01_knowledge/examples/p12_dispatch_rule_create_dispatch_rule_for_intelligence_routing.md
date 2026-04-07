---
id: p12_dr_intelligence
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: dispatch-rule-builder
domain: intelligence
quality: 9.0
tags: [dispatch, intelligence, research, analysis, n01]
tldr: Route intelligence analysis and research tasks to N01 intelligence nucleus
scope: intelligence
keywords: [intelligence, inteligencia, research, pesquisa, analysis, analise, papers, artigos, benchmark, competitor, concorrente, market, mercado, intel, investigation, investigacao]
agent_group: n01_intelligence
model: gemini
priority: 8
confidence_threshold: 0.75
fallback: n04_knowledge
routing_strategy: hybrid
density_score: 0.83
---
# intelligence Dispatch Rule

## Purpose
Routes intelligence analysis, research, and competitive intelligence tasks to N01 intelligence nucleus. N01 specializes in deep research with large document analysis using Gemini 2.5-pro's 1M context window for processing papers, market reports, and comprehensive intelligence briefs.

## When to Use

| Trigger | Example |
|---------|---------|
| Market research | "Analyze competitors in the AI agent space" |
| Paper analysis | "Research latest LLM benchmarks from arXiv" |
| Intelligence briefs | "Compile industry trends in knowledge management" |
| Large document analysis | "Process 50-page market report on SaaS trends" |
| Competitive intelligence | "Map feature comparison across 10 competitors" |

**Route to N01 when:** Task involves deep analysis, multiple sources, market intelligence, or processing large documents.

**Do NOT route when:** Simple knowledge lookup (N04), creative copy (N02), or code-related tasks (N05).

## Keyword Rationale
Bilingual PT/EN coverage captures both Portuguese operator commands and English research terminology. Keywords include core intelligence terms (intelligence/inteligencia), research variants (research/pesquisa, analysis/analise), document types (papers/artigos), and business intelligence terms (benchmark, competitor/concorrente, market/mercado, intel). The hybrid strategy combines keyword matching with semantic understanding for nuanced intelligence requests.

## Fallback Logic
N04 knowledge nucleus handles knowledge management when N01 intelligence is unavailable. N04 can index, organize, and retrieve research outputs without the specialized intelligence analysis capabilities, providing a logical degradation path for research-adjacent tasks.