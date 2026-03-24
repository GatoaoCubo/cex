---
id: p05_parser_brain_query
type: parser
lp: P05
description: "Extracts ranked knowledge chunks from brain_query raw output"
input_format: json
output_format: structured_markdown
version: 1.0.0
created: 2026-03-24
author: edison
quality: 9.0
tags: [parser, brain, search-results, extraction]
---

# Parser: brain_query Results

## Purpose
Extracts ranked knowledge chunks from raw brain_query MCP tool output. Converts JSON response with scores and metadata into structured markdown sections for satellite consumption.

## Input
```json
{
  "results": [
    {"text": "chunk content...", "score": 0.87, "source": "KC_PYTHA_069.md", "section": "Strategy"},
    {"text": "another chunk...", "score": 0.72, "source": "KC_EDISON_029.md", "section": "Patterns"}
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

### KC_PYTHA_069.md (score: 0.87)
**Section**: Strategy
> chunk content...

### KC_EDISON_029.md (score: 0.72)
**Section**: Patterns
> another chunk...
```

## Edge Cases
- Empty results: return "No matches found for: {query}"
- All scores < 0.5: return warning + top 1 result anyway
- Single source multiple chunks: merge under one header
