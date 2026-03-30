---
id: n04_cs_knowledge
kind: chunk_strategy
pillar: P01_knowledge
version: "2.0.0"
created: "2024-03-30"
updated: "2024-03-30"
author: "N04 Knowledge Nucleus"
name: "N04 Semantic Markdown Chunking"
method: "semantic_markdown_recursive"
chunk_size: 1000
chunk_overlap: 150
separators: ["

# ", "

## ", "

### ", "

", "
", " ", ""]
quality: null
tags: [chunk_strategy, n04, knowledge, rag, chunking, p01]
tldr: "Defines the primary chunking strategy for N04, using a semantic, Markdown-aware recursive splitter to preserve context."
density_score: 0.96
---

# N04 Semantic Markdown Chunking Strategy

## 1. Overview
This document defines the primary strategy used by the N04 Knowledge Nucleus for chunking text documents, particularly Markdown files. The goal of any chunking strategy is to maximize retrieval relevance by creating chunks that are **atomic**, **self-contained**, and **semantically complete**. This strategy is designed to be a significant improvement over simple fixed-size or character-based splitting.

## 2. Method: `semantic_markdown_recursive`
This method is a hierarchical, recursive splitting algorithm that is explicitly aware of Markdown syntax. It attempts to split the text along the most significant semantic boundaries first, only moving to less significant boundaries if the resulting chunk is still larger than the target `chunk_size`.

### 2.1. Separator Hierarchy
The core of the strategy is the prioritized list of separators. The splitter will attempt to divide the text using the first separator in the list. If any resulting chunk is too large, that chunk is then processed using the *next* separator in the list, and so on.

**Separator Priority List:**
1.  `

# ` (H1 Header) - Highest semantic boundary.
2.  `

## ` (H2 Header)
3.  `

### ` (H3 Header)
4.  `

` (Paragraph break) - The most common separator for prose.
5.  `
` (Line break)
6.  ` ` (Space)
7.  `` (Empty string / character-level split) - Fallback for dense text.

### 2.2. Parameters
| Parameter | Value | Rationale |
| :--- | :--- | :--- |
| **`chunk_size`** | `1000` | This is a target, not a hard limit. It represents a good balance for modern embedding models, providing enough context without introducing excessive noise. Measured in characters. |
| **`chunk_overlap`**| `150` | Provides essential context continuity between related chunks, especially when a split occurs in the middle of a logical section. Measured in characters. |
| **`separators`** | (See list above) | Prioritized to respect the semantic structure of well-formatted Markdown, ensuring that headers and paragraphs are treated as logical units. |

## 3. Alternative & Fallback Strategies

### 3.1. Agentic Chunking (Future State)
- **Description**: An advanced method where an LLM is used to analyze a document and determine the optimal chunk boundaries based on its understanding of the content.
- **Pros**: Highest possible quality, truly semantic.
- **Cons**: High cost (token usage) and latency. Reserved for "golden" or highly critical source documents.

### 3.2. Fixed-Size Chunking
- **Description**: The most basic method. The text is split into chunks of exactly `chunk_size` with a given overlap.
- **When to Use**: Only as a last resort for documents with no discernible structure (e.g., a plain text dump with no line breaks).
- **Pros**: Simple, fast, predictable.
- **Cons**: Extremely low semantic integrity. Often splits sentences or ideas, leading to poor retrieval performance.

## 4. Integration
This chunking strategy is a foundational component of the **Document Ingestion & Indexing** workflow. The output of this strategy (a list of text chunks) is the direct input to the **Generate Embeddings** step. The quality of the chunks produced here has the single largest impact on the success of the entire RAG pipeline.
