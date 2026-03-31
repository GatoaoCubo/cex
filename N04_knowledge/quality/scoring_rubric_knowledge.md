---
id: n04_sr_knowledge
kind: scoring_rubric
pillar: P07_evals
version: 3.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge_nucleus
title: "Rubric: N04 Knowledge Artifact Integrity"
framework: "N04 Knowledge Artifact Quality Gate"
target_kinds: [knowledge_card, chunk_strategy, embedding_config, rag_source, retriever_config]
dimensions_count: 4
total_weight: 100
threshold_golden: 9.5
threshold_publish: 9.0
threshold_review: 7.5
automation_status: llm_assisted
quality: null
tags: [scoring_rubric, n04, knowledge, quality, evals, p07]
tldr: "The 4-dimension scoring rubric for the soft gates (S1-S4) of the N04 Knowledge Quality Gate, evaluating atomicity, connectivity, discoverability, and clarity."
calibration_set: [n04_kc_knowledge_management]
inter_rater_agreement: 0.92
appeals_process: "Submit re-evaluation request to N01_intelligence with justification."
linked_artifacts:
  primary:
    - n04_qg_knowledge
---

# N04 Scoring Rubric

## 1. Framework Overview
This rubric provides a structured evaluation framework for the four **Soft Gates (S1-S4)** defined in the `n04_qg_knowledge` artifact. It is designed to be used by an LLM-based evaluator (`n04_quality_scorer` tool) or a human expert to generate a consistent quality score. Each dimension is scored from 0 to 10, which is then multiplied by its weight to calculate the final score. An artifact must score `>= 9.0` to pass the gate.

## 2. Scoring Dimensions

### Dimension 1 (S1): Atomicity
- **Weight**: 40%
- **Description**: Evaluates if the artifact represents a single, cohesive, and self-contained concept. This is the most critical factor for high-quality retrieval.

| Score | Criteria | Example |
| :--- | :--- | :--- |
| **10 (Excellent)** | The artifact is perfectly atomic. It covers one concept thoroughly without including irrelevant or tangential information. | A Knowledge Card about "Cosine Similarity" that only explains that concept and its formula. |
| **5 (Fair)** | The artifact primarily focuses on one concept but includes 1-2 related but distinct ideas, slightly reducing its clarity. | The "Cosine Similarity" KC also attempts to briefly explain Euclidean distance. |
| **1 (Poor)** | The artifact is a "grab bag" of multiple, unrelated concepts, making it impossible to retrieve for a specific query. | A single artifact explaining similarity, chunking, and RAG pipelines all at once. |

### Dimension 2 (S2): Connectivity
- **Weight**: 30%
- **Description**: Evaluates how well the artifact is integrated into the CEX knowledge graph through explicit links.

| Score | Criteria | Example |
| :--- | :--- | :--- |
| **10 (Excellent)** | All relevant upstream and downstream concepts are linked in the `linked_artifacts` section. The graph linkage is logical and complete. | A "RAG" KC links to "Embeddings", "Chunking", "Retrievers", and the parent "AI Architectures" KC. |
| **5 (Fair)** | The artifact links to some, but not all, obvious concepts. The graph is partially connected. | The "RAG" KC only links to "Embeddings", missing the other critical components. |
| **1 (Poor)** | The artifact is an island. The `linked_artifacts` section is empty or contains irrelevant links. | The "RAG" KC has no links. |

### Dimension 3 (S3): Discoverability
- **Weight**: 20%
- **Description**: Evaluates the quality and comprehensiveness of the metadata used for search (`keywords`, `long_tails`, `tldr`).

| Score | Criteria | Example |
| :--- | :--- | :--- |
| **10 (Excellent)** | Keywords are specific and exhaustive. Long-tail queries capture common user questions. TLDR is a perfect, dense summary. | Keywords: `[rag, retrieval, augmented, generation]`. Long-tails: `["how does retrieval augmented generation work"]`. |
| **5 (Fair)** | Metadata is present but generic. Keywords are too broad, and long-tails are not representative of likely queries. | Keywords: `[ai, llm]`. Long-tails: `["rag info"]`. |
| **1 (Poor)** | Metadata is missing, irrelevant, or just a copy-paste of the title. The artifact is practically invisible to search. | Keywords are empty. |

### Dimension 4 (S4): Clarity
- **Weight**: 10%
- **Description**: Evaluates the linguistic and structural quality of the content. Is it easy for another agent (or human) to understand?

| Score | Criteria | Example |
| :--- | :--- | :--- |
| **10 (Excellent)** | The language is precise and unambiguous. The structure is logical and easy to parse. Markdown is used effectively. | Content is written in clear, declarative sentences with well-defined sections. |
| **5 (Fair)** | The content is generally understandable but contains some jargon, awkward phrasing, or inconsistent structure. | Sentences are long and convoluted; sections are poorly defined. |
| **1 (Poor)** | The content is confusing, contradictory, or contains significant grammatical errors, making it unreliable. | The artifact is a "wall of text" with no clear structure or formatting. |
