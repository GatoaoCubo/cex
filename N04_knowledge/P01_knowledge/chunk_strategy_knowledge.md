---
id: n04_cs_knowledge
kind: chunk_strategy
pillar: P01_knowledge
version: 3.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge_nucleus
title: "N04 Content-Aware Chunking Strategy"
default_strategy: hierarchical_recursive
chunk_size: 1024
chunk_overlap: 200
quality: 9.1
tags: [chunk_strategy, n04, knowledge, rag, chunking, p01, recursive]
tldr: "Defines the content-aware, hierarchical chunking strategies for N04. Prioritizes semantic boundaries (headers, code blocks, paragraphs) to maximize context cohesion for RAG."
density_score: 0.89
---

# N04 Content-Aware Chunking Strategy

## 1. Overview
This document specifies the set of hierarchical, content-aware chunking strategies used by the N04 Knowledge Nucleus. The primary goal is to maximize **Contextual Cohesion**: ensuring that each chunk is as semantically complete and self-contained as possible. This is the most critical step for achieving high-quality RAG performance.

## 2. Primary Strategy: `hierarchical_recursive`
This method is a top-down, recursive splitting algorithm. It attempts to split a document along the most significant semantic boundaries first. If a resulting chunk is still larger than the target `chunk_size`, the algorithm is recursively applied to that chunk using the next separator in the prioritized hierarchy.

## 3. Separator Hierarchies by Content Type
The effectiveness of the `hierarchical_recursive` strategy depends entirely on a separator list that is tailored to the document's content type.

### 3.1. Content Type: `markdown`
Designed for `.md` files, prioritizing document structure.
1.  `

# ` (H1 Header)
2.  `

## ` (H2 Header)
3.  `

### ` (H3 Header)
4.  `

---

` (Horizontal Rule)
5.  `

` (Paragraph break)
6.  `
` (Line break)
7.  ` ` (Space)
8.  `` (Character)

### 3.2. Content Type: `python`
Designed for `.py` files, prioritizing code structure.
1.  `
def ` (Function definition)
2.  `
class ` (Class definition)
3.  `

` (Double newline, separates logical blocks)
4.  `
` (Single newline)
5.  `` (Character)

### 3.3. Content Type: `generic_text` (Fallback)
A general-purpose hierarchy for unstructured text.
1.  `

` (Paragraph break)
2.  `
` (Line break)
3.  `. ` (Sentence end)
4.  ` ` (Space)
5.  `` (Character)

## 4. Global Parameters

| Parameter | Value | Rationale |
| :--- | :--- | :--- |
| **`chunk_size`** | `1024` | A target size (in characters) that offers a robust balance between context density and noise for modern embedding models. This is a target, not a hard limit. |
| **`chunk_overlap`**| `200` | A significant overlap (in characters) to ensure context continuity between related chunks, especially when a semantic split (like a paragraph break) occurs. |

## 5. Advanced Strategies (Future State)

### 5.1. Propositional Chunking
- **Description**: A sophisticated technique where an LLM is used to extract every atomic statement (a "proposition") from a document. Each proposition is embedded individually. This allows for highly granular and factual retrieval.
- **Pros**: Extremely high precision for fact-based queries.
- **Cons**: High cost and complexity. Best for high-value, fact-heavy documents.

### 5.2. Agentic Chunking
- **Description**: An LLM analyzes a document and determines optimal chunk boundaries based on its holistic understanding of the content flow and semantic shifts.
- **Pros**: Potentially the highest quality for complex, narrative documents.
- **Cons**: High cost (token usage) and latency. Reserved for "golden" or highly critical source documents.
