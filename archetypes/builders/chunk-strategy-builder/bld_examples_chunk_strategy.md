---
kind: examples
id: bld_examples_chunk_strategy
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of chunk_strategy artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: chunk-strategy-builder
## Golden Example
INPUT: "Create chunk strategy for RAG over technical documentation"
OUTPUT:
```yaml
id: p01_chunk_tech_docs_recursive
kind: chunk_strategy
pillar: P01
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "Technical Documentation Recursive Splitter"
quality: null
tags: [chunk_strategy, P01, chunk]
tldr: "Technical Documentation Recursive Splitter — production-ready chunk_strategy configuration"
```
## Overview
Recursive character splitter tuned for technical documentation with Markdown headings.
Splits on heading boundaries first, then paragraphs, then sentences.

## Method
Algorithm: recursive_character (LangChain RecursiveCharacterTextSplitter)
Separators tried in order: H2 heading > H3 heading > paragraph > line > sentence > word.
Falls back to next separator only when chunk exceeds chunk_size.

## Parameters
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| chunk_size | 512 tokens | Fits nomic-embed-text (8192) with 16x chunks per query |
| chunk_overlap | 64 tokens | 12.5% overlap preserves cross-boundary context |
| separators | [\n## , \n### , \n\n, \n, . , ] | Heading-first preserves section coherence |
| strip_whitespace | true | Remove leading/trailing whitespace from chunks |
| keep_separator | true | Retain heading markers for context |

## Integration
- Input: raw Markdown documents from document_loader
- Output: list of Document chunks with metadata (source, chunk_index, heading_path)
- Pairs with: p01_emb_nomic (embedding), p01_retr_hybrid (retrieval)
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p01_chunk_ pattern (H02 pass)
- kind: chunk_strategy (H04 pass)
- All required fields present (H06 pass)
- Body has all 4 sections: Overview, Method, Parameters, Integration (H07 pass)
- Parameters table with value and rationale (S03 pass)
- tldr under 160 chars (S01 pass)
- tags >= 3 items, includes "chunk_strategy" (S02 pass)
## Anti-Example
INPUT: "Create chunk strategy for code files"
BAD OUTPUT:
```yaml
id: code-chunker
kind: chunker
quality: 9.0
tags: [chunker]
```
FAILURES:
1. id has hyphens and no p01_chunk_ prefix -> H02 FAIL
2. kind: 'chunker' not 'chunk_strategy' -> H04 FAIL
3. Missing fields: method, chunk_size, chunk_overlap, separators -> H06 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. No ## Method section in body -> H07 FAIL
6. No parameters table -> S03 FAIL
