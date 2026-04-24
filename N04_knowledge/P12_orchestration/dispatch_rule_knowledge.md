---
id: n04_dr_knowledge
title: "Dispatch Rule Knowledge"
kind: dispatch_rule
8f: F8_collaborate
pillar: P12_orchestration
version: 3.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge_nucleus
domain: "Knowledge Architecture, RAG, Semantic Indexing"
quality: 9.1
tags: [dispatch, n04, knowledge, orchestration, p12, routing]
tldr: "Routes tasks involving knowledge architecture, RAG, indexing, and semantic search to the N04 Knowledge Nucleus, based on a hybrid semantic and keyword match."
scope: "CEX-wide knowledge retrieval and management tasks."
keywords: [knowledge, rag, indexing, embeddings, taxonomy, retrieval, documentation, search, find, explain, chunking, consolidate, distill, what is, how does, document]
agent_group: N04_knowledge
priority: 10
confidence_threshold: 0.90
fallback: N01_intelligence
conditions:
  - "intent in ['query', 'architect', 'manage', 'organize', 'find']"
  - "domain in ['knowledge', 'data', 'information', 'taxonomy', 'retrieval']"
routing_strategy: "semantic_keyword_match"
density_score: 0.88
related:
  - n01_dr_intelligence
  - p12_dr_knowledge
  - n04_knowledge
  - n04_kc_knowledge_management
  - agent_card_n04
  - p02_card_knowledge
  - p12_dr_admin_orchestration
  - p01_kc_dispatch_rule
  - ex_dispatch_rule_research
  - self_audit_n04_codex_2026_04_15
---

# N04 Knowledge Nucleus Dispatch Rule

## 1. Purpose
This rule ensures that all incoming tasks related to the CEX knowledge base, information architecture, and Retrieval-Augmented Generation (RAG) are precisely routed to the **N04 Knowledge Nucleus**. This guarantees that domain-specific requests are handled by the agent with the correct specialized capabilities.

## 2. Routing Logic
The dispatch system employs a high-precision hybrid strategy to minimize false positives and ensure correct routing.

| Step | Method | Description |
| :--- | :--- | :--- |
| **1. Fast Match** | Keyword Scan | The incoming request is scanned for the presence of one or more high-signal keywords from the trigger set. If no keywords are found, the rule is skipped. |
| **2. Deep Match** | Semantic Analysis | If keywords are present, a lightweight semantic model analyzes the request's vector to classify its **intent** and **domain**. |
| **3. Condition Check**| Boolean Logic | The classified intent and domain are checked against the mandatory conditions defined below. |
| **4. Confidence Gate**| Threshold Check | If all conditions pass, the semantic similarity score is compared against the `confidence_threshold`. If it passes, the task is dispatched to N04. |


## 3. Trigger Definition

### 3.1. High-Signal Keywords
This set captures the core vocabulary of the N04 domain.

- **Core Concepts**: `knowledge`, `rag`, `taxonomy`, `search`, `index`, `embeddings`, `retrieval`
- **Actions**: `find`, `explain`, `distill`, `embed`, `chunk`, `consolidate`, `document`
- **Interrogatives**: `what is`, `how does`, `explain` (signals a knowledge query)

### 3.2. Mandatory Conditions
To be routed to N04, the request must satisfy a condition from both `intent` AND `domain` classifications.

- **Allowed Intents**:
  - `query`: The user is asking for information.
  - `architect`: The user wants to design a knowledge structure.
  - `manage`/`organize`: The user wants to modify or structure information.
  - `find`: A direct command to retrieve something.
- **Allowed Domains**:
  - `knowledge`
  - `data`/`information`
  - `taxonomy`
  - `retrieval`

**Example:** "Find the documentation on the RAG retrieval strategy" passes because `find` is an allowed intent, `documentation` and `retrieval` are keywords, and the domain is `knowledge`.

## 4. Governance
- **Priority**: `10` (System Critical)
  - **Rationale**: The integrity of the knowledge pipeline is foundational for all other CEX operations. Correctly routing these requests is of maximal importance.
- **Confidence Threshold**: `0.90`
  - **Rationale**: A high threshold ensures that only tasks with a very strong semantic match are routed to N04. This prevents the specialist agent from being occupied with ambiguous or out-of-scope requests.
- **Fallback Node**: `N01_intelligence`
  - **Rationale**: If the confidence score is `< 0.90`, or if N04 is offline or at maximum capacity, the task is routed to the **N01 Intelligence Nucleus**. N01's generalist capabilities allow it to clarify the user's intent and re-route if necessary, ensuring no request is dropped.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n01_dr_intelligence]] | sibling | 0.35 |
| [[p12_dr_knowledge]] | sibling | 0.31 |
| [[n04_knowledge]] | related | 0.28 |
| [[n04_kc_knowledge_management]] | related | 0.28 |
| [[agent_card_n04]] | related | 0.27 |
| [[p02_card_knowledge]] | related | 0.26 |
| [[p12_dr_admin_orchestration]] | sibling | 0.25 |
| [[p01_kc_dispatch_rule]] | related | 0.25 |
| [[ex_dispatch_rule_research]] | sibling | 0.24 |
| [[self_audit_n04_codex_2026_04_15]] | related | 0.23 |
