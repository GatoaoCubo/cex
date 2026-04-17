---
kind: examples
id: bld_examples_agentic_rag
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of agentic_rag artifacts
quality: 8.9
title: "Examples Agentic Rag"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [agentic_rag, builder, examples]
tldr: "Golden and anti-examples of agentic_rag artifacts"
domain: "agentic_rag construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```markdown
---
cex_kind: agentic_rag
name: LegalDocAssistant
description: Agent-driven RAG for contract review using real tools
tools:
  - langchain
  - weaviate
  - openai/gpt-4
---
**Workflow**:
1. User submits contract text to LangChain agent
2. Agent queries Weaviate vector store for relevant legal precedents
3. Agent synthesizes findings with GPT-4 to generate risk assessment
4. Agent proposes amendments with cited precedents
```

## Anti-Example 1: Missing Agent Logic
```markdown
---
cex_kind: agentic_rag
name: SimpleRetriever
description: Basic document search without generation
tools:
  - elasticsearch
  - openai/text-embedding-ada-002
---
**Workflow**:
1. User submits query
2. Elasticsearch returns matching documents
3. Results displayed verbatim to user
```
## Why it fails
Lacks agent orchestration and generation layer - just simple retrieval without synthesis or decision-making

## Anti-Example 2: Missing Retrieval Component
```markdown
---
cex_kind: agentic_rag
name: PureAgent
description: Chatbot with no external data access
tools:
  - langchain
  - openai/gpt-4
---
**Workflow**:
1. User asks question
2. GPT-4 generates response from training data
3. Response delivered without external validation
```
## Why it fails
No retrieval component - agent operates solely on pre-trained knowledge without augmenting with external data sources
