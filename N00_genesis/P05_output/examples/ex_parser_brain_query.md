---
id: p05_parser_brain_query
kind: parser
pillar: P05
description: "Extracts ranked knowledge chunks from brain_query raw output"
input_format: json
output_format: structured_markdown
version: 1.0.0
created: 2026-03-24
author: builder_agent
quality: 9.1
tags: [parser, brain, search-results, extraction]
updated: "2026-04-07"
domain: "output format"
title: "Parser Brain Query"
density_score: 0.92
tldr: "Defines parser for parser brain query, with validation gates and integration points."
---

# Parser: brain_query Results

## Purpose
Extracts ranked knowledge chunks from raw brain_query MCP tool output. Converts JSON response with scores and metadata into structured markdown sections for agent_group consumption.

## Input
```json
{
  "results": [
    {"text": "chunk content...", "score": 0.87, "source": "KC_knowledge_agent_069.md", "section": "Strategy"},
    {"text": "another chunk...", "score": 0.72, "source": "KC_builder_agent_029.md", "section": "Patterns"}
  ],
  "query": "agent orchestration patterns",
  "method": "hybrid"
}
```

## Extraction Rules
1. Filter results with score >= 0.5 (below = noise)
2. Group by source file (deduplicate same-file chunks)
3. Sort by score descending within groups
4. Extract: source path, section header, content snippet (max 200 chars)

## Output
```markdown
## brain_query: "agent orchestration patterns" (2 results)

### KC_knowledge_agent_069.md (score: 0.87)
**Section**: Strategy
> chunk content...

### KC_builder_agent_029.md (score: 0.72)
**Section**: Patterns
> another chunk...
```

## Edge Cases
1. Empty results: return "No matches found for: {query}"
2. All scores < 0.5: return warning + top 1 result anyway
3. Single source multiple chunks: merge under one header

## Properties

| Property | Value |
|----------|-------|
| Kind | `parser` |
| Pillar | P05 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
