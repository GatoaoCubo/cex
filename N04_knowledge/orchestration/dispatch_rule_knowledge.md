---
id: n04_dr_knowledge
kind: dispatch_rule
pillar: P12_orchestration
version: "2.0.0"
created: "2024-03-30"
updated: "2024-03-30"
author: "N04 Knowledge Nucleus"
domain: "RAG, Knowledge Graphs, Semantic Search, Taxonomy"
quality: null
tags: [dispatch, n04, knowledge, orchestration, p12]
tldr: "Routes all tasks related to knowledge architecture, RAG, and semantic search to the N04 Knowledge Nucleus."
scope: "CEX-wide knowledge retrieval and management tasks."
keywords": [knowledge, rag, index, search, distill, taxonomy, embed, chunk, find, what is, how does, explain, document]
agent_node: "n04_knowledge_nucleus"
model: "gemini-2.5-pro"
priority: 10
confidence_threshold: 0.85
fallback: "n01_intelligence"
conditions:
  - "intent in ['query', 'build', 'architect', 'manage']"
  - "domain in ['knowledge', 'data', 'information']"
load_balance: false
routing_strategy: "semantic_keyword_match"
---

# N04 Knowledge Nucleus Dispatch Rule

## 1. Purpose
This rule directs all incoming tasks related to the CEX knowledge base, information architecture, and Retrieval-Augmented Generation (RAG) to the **N04 Knowledge Nucleus**. As the specialized agent for this domain, N04 has the necessary tools and capabilities to handle these requests with the highest fidelity.

## 2. Routing Strategy: `semantic_keyword_match`
The dispatch system employs a hybrid strategy. It first performs a fast check for the presence of high-signal keywords. If matched, it then uses a lightweight semantic model to confirm the user's *intent* aligns with N04's core functions before routing.

### 2.1. Keywords
The keyword set is designed to be comprehensive, capturing verbs and nouns associated with knowledge management.

- **Core Domain**: `knowledge`, `rag`, `taxonomy`, `search`, `index`
- **Actions**: `find`, `explain`, `distill`, `embed`, `chunk`
- **Entities**: `document`, `source`, `information`, `data`
- **Interrogatives**: `what is`, `how does` (often signal a knowledge query)

### 2.2. Conditions
To prevent false positives, the following conditions must also be met:
- The user's intent should be classifiable as `query` (seeking info), `build` (designing a knowledge structure), `architect` (same as build), or `manage` (organizing info).
- The domain of the query should relate to `knowledge`, `data`, or `information`.

## 3. Priority & Confidence
- **Priority**: `10` (Maximum)
  - **Rationale**: Correctly routing knowledge queries is fundamental to the operation of all other agents. A high-quality information backbone is non-negotiable.
- **Confidence Threshold**: `0.85`
  - **Rationale**: A high threshold ensures that only tasks with a strong semantic match are routed to N04. Ambiguous queries are better handled by a generalist.

## 4. Fallback Logic
If the confidence score is below `0.85`, or if N04 is offline or at maximum capacity, the task is routed to **N01_intelligence**.

- **Rationale**: N01, as the general intelligence nucleus, has the broad reasoning capability to understand the user's ambiguous request, clarify it, or route it to the appropriate specialist (which may still be N04 after clarification). This prevents routing failures and ensures the user's request is always handled.
