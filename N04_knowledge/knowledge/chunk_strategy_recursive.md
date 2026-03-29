---
id: p01_chunk_pytha_recursive
kind: chunk_strategy
pillar: P01
version: "1.0.0"
created: "2023-10-09"
updated: "2023-10-09"
author: "chunk-strategy-builder"
name: "Pytha Recursive Chunk Strategy"
method: "Recursive Character"
chunk_size: 600
chunk_overlap: 60
separators: ["\n\n", "\n", ".", " "]
quality: null
tags: [chunk_strategy, RAG, document_split]
tldr: "Recursive character-based chunking strategy tailored for Pytha knowledge documents."
---
## Overview
The Pytha Recursive Chunk Strategy is designed for splitting knowledge documents into coherent, retrievable segments suitable for Retrieval-Augmented Generation (RAG) applications. It is particularly effective for mixed-format documents with varying sectioning such as text paragraphs, lists, and bullet points.

## Method
This strategy uses a recursive character splitting method. It prioritizes breaking documents at significant separator positions in order: double new lines, single new lines, periods, and spaces. This approach ensures semantic coherence of chunks, making them useful for retrieval and question-answering tasks.

## Parameters
| Parameter     | Value               | Rationale                                                                   |
|---------------|---------------------|-----------------------------------------------------------------------------|
| chunk_size    | 600 tokens          | Balances retrieval efficiency with the embedding model's context limit.     |
| chunk_overlap | 60 tokens           | Ensures that contextual information is preserved across chunk boundaries.   |
| separators    | ["\n\n", "\n", ".", " "] | Ordered to prioritize logical breaks in documents before falling back to finer granularity splits. |

## Integration
- **Input**: Raw text documents from an appropriate document loader within a RAG pipeline.
- **Output**: A list of document chunks, each accompanied by metadata indicating original document source and chunk indices.
- **Compatible With**: This strategy pairs well with embedding configurations such as Word2Vec or BERT to maximize retrieval performance. Suitable for use in Pytha's knowledge aggregation frameworks, ensuring comprehensive document indexing and efficient retrieval.

--- 

This concise chunk strategy defines the method and parameters necessary for effective document segmentation within the Pytha knowledge management system, emphasizing the strategy's rationale and integration within a typical RAG pipeline.