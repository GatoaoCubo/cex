---
id: p01_kc_search_tool
kind: knowledge_card
type: kind
pillar: P01
title: "Search Tool — Deep Knowledge for search_tool"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: marketing_agent
domain: search_tool
quality: 9.1
tags: [search_tool, P04, CALL, kind-kc, web-search]
tldr: "Queries external search engines (Tavily, Serper, Perplexity, Brave) and returns ranked results with URLs and snippets — the web grounding layer for LLM agents"
when_to_use: "Building, reviewing, or reasoning about search_tool artifacts"
keywords: [search, web, tavily, serper, perplexity]
feeds_kinds: [search_tool]
density_score: null
---

# Search Tool

## Spec
```yaml
kind: search_tool
pillar: P04
llm_function: CALL
max_bytes: 2048
naming: p04_search_{{provider}}.md + .yaml
core: true
```

## What It Is
A search_tool queries external search engines (Tavily, Serper, Perplexity, Brave, SerpAPI) and returns ranked results with titles, URLs, and snippets. It provides web grounding for LLM responses with fresh, external information. It is NOT a retriever (which searches a local embedding store with pre-indexed data) nor a document_loader (which ingests files into chunks). The search_tool reaches out to the live web; retriever operates on already-indexed local data.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | TavilySearchResults, GoogleSerperAPIWrapper | Tool wrapping search API; returns snippets |
| LlamaIndex | TavilyToolSpec, DuckDuckGoSearchToolSpec | FunctionTool wrapper around search API |
| CrewAI | SerperDevTool, TavilySearchTool | Built-in tools via crewai-tools package |
| DSPy | dspy.ColBERTv2 (web variant) | Experimental; mostly local in practice |
| Haystack | SerperWebSearch, TavilyWebSearch | Native pipeline WebSearch component |
| OpenAI | web_search tool (Responses API) | Native; model-driven, no provider config |
| Anthropic | web_search tool (tool_use) | Native in Claude 3.5+ via tool_use block |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| provider | str | tavily | Cost vs accuracy; Tavily leads accuracy |
| max_results | int | 5 | More = richer context; higher API cost |
| search_depth | str | basic | advanced = deeper but 2x cost (Tavily) |
| include_raw_content | bool | false | True = full page text; high token count |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Tavily for accuracy | Fact-checking, deep research tasks | TavilySearchResults(k=5, depth="advanced") |
| Serper for speed | High-volume query pipelines | SerperDev max_results=3 per query |
| Perplexity for synthesis | Summarized web answer needed | search_online mode with citation |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| include_raw_content=True always | Context window overflow on long pages | Enable only for targeted deep reads |
| No result deduplication | Duplicate snippets confuse LLM reasoning | Dedup by URL before injecting into prompt |
| Missing API key validation | Silent empty results, no error surfaced | Validate key at startup; raise on missing |

## Integration Graph
```
[user_query / LLM tool_call] --> [search_tool] --> [ranked: title+url+snippet]
                                       |                      |
                              [provider, max_results]   [LLM prompt injection]
                                       |
                              [search_depth, filters]
```

## Decision Tree
- IF searching local embedding store THEN use retriever
- IF need to ingest found pages as documents THEN document_loader after search
- IF need structured DB data THEN use db_connector
- DEFAULT: search_tool for any live web query requiring fresh external grounding

## Quality Criteria
- GOOD: provider configured, max_results set, URL and snippet in each result
- GREAT: result dedup, depth routing (basic/advanced), fallback provider on failure
- FAIL: no API key validation, raw_content always on, no result count limit enforced
