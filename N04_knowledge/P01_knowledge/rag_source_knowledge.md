---
id: n04_rs_cex_codebase
title: "Rag Source Knowledge"
kind: rag_source
pillar: P01_knowledge
version: "2.0.0"
created: "2024-03-30"
updated: "2026-04-15"
author: "N04 Knowledge Nucleus"
url: "file://./"
domain: "CEX Internals"
last_checked: "2026-04-15"
quality: 9.0
tags: [rag-source, n04, knowledge, codebase, markdown, p01]
tldr: "The CEX project's own codebase, specifically all Markdown files, serving as the primary source of internal knowledge."
keywords: [cex, codebase, markdown, documentation, artifacts]
reliability: "high"
format: "markdown"
extraction_method: "file_glob"
density_score: 0.91
---

# RAG Source: CEX Codebase (Markdown)

## 1. Source Description
This RAG source encompasses the entire local CEX project directory, with a specific focus on Markdown (`.md`) files. These files constitute the primary, most up-to-date source of truth for all CEX architecture, processes, artifacts, and documentation. They are the living memory of the system.

## 2. Extraction Method: `file_glob`
- **Description**: The `document_loaders` MCP will use a file globbing mechanism to find all relevant files within the project directory specified by the `url`.
- **Configuration**:
  - **Glob Pattern**: `**/*.md`
  - **Exclude Patterns**:
    - `**/node_modules/**`
    - `**/_archive/**`
    - `**/.git/**`

## 3. Freshness & Update Policy

| Aspect | Details |
|--------|---------|
| **Re-check Interval** | Real-time |
| **Trigger Method** | Git pre-commit hook on `.md` file modifications |
| **Update Process** | Document Ingestion & Indexing workflow for specific modified file |
| **Sync Guarantee** | Perfect alignment between committed codebase state and searchable knowledge base |
| **Staleness Risk** | Eliminated for internal documentation |

## 4. Reliability & Authority
- **Reliability**: `High`. As the direct output of the CEX nuclei, these documents are considered canonical, authoritative sources of information.
- **Verification**: The content is implicitly verified by the peer review process of pull requests and the operational success of the described systems.

## 5. Integration
This is the default source for most queries related to CEX's internal workings. The `retriever_config` will prioritize results from this source when the user's query contains keywords like "CEX", "N0#", or refers to specific artifacts.