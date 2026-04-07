---
id: p01_kc_langchain_patterns
kind: knowledge_card
type: domain
pillar: P01
title: "LangChain Patterns — LCEL, Runnables, Tools, Retrievers, Output Parsers"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: langchain
origin: src_framework_taxonomy
quality: 9.1
tags: [langchain, lcel, runnable, retriever, output-parser, agent, chain]
tldr: "LangChain composes LLM pipelines via LCEL Runnables, unifying agents, retrievers, tools, and output parsers into streamable chains"
when_to_use: "Building or mapping LangChain constructs to CEX kinds"
keywords: [langchain, lcel, runnable, chain, retriever, tool, output-parser]
long_tails:
  - "How does LangChain LCEL map to CEX workflow and chain kinds"
  - "Which LangChain classes map to CEX retriever and agent kinds"
axioms:
  - "LCEL pipe operator composes Runnables into RunnableSequence — the universal chain primitive"
  - "Legacy Chain/LLMChain are deprecated; prefer LCEL Runnable composition"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_taxonomy, p01_kc_llamaindex_patterns, p01_kc_haystack_patterns]
feeds_kinds:
  - agent           # create_agent, AgentExecutor
  - chain           # RunnableSequence (LCEL pipe), LLMChain (legacy)
  - retriever       # BaseRetriever, VectorStoreRetriever
  - retriever_config # VectorStore backend selection + top_k
  - prompt_template # ChatPromptTemplate, PromptTemplate
  - function_def    # BaseTool, StructuredTool, @tool decorator
  - document_loader # BaseDocumentLoader
  - chunk_strategy  # TextSplitter, RecursiveCharacterTextSplitter
  - embedding_config # BaseEmbeddings
  - parser          # BaseOutputParser, StrOutputParser, JsonOutputParser, PydanticOutputParser
  - memory_scope    # BaseChatMessageHistory
  - workflow        # RunnableParallel (fan-out), RunnableSequence (pipeline)
density_score: 0.91
---

# LangChain Patterns

## Quick Reference
```yaml
topic: LangChain Core (langchain_core + langchain)
scope: LCEL composition, agents, retrieval, tools, output parsing
source: python.langchain.com
criticality: high
```

## Key Concepts

| Concept | Module | CEX Kind | Role |
|---------|--------|----------|------|
| `Runnable` | `langchain_core.runnables` | workflow | Base interface for all composable units |
| `RunnableSequence` | `langchain_core.runnables` | chain | Chain via `\|` operator (LCEL) |
| `RunnableParallel` | `langchain_core.runnables` | workflow | Fan-out parallel execution |
| `RunnableLambda` | `langchain_core.runnables` | chain | Wrap any function as Runnable |
| `create_agent` | `langchain.agents` | agent | Factory for prebuilt agents |
| `AgentExecutor` | `langchain.agents` | agent | Legacy agent loop with tools |
| `BaseTool` / `@tool` | `langchain_core.tools` | function_def | Tool definition for LLM invocation |
| `StructuredTool` | `langchain_core.tools` | function_def | Tool with Pydantic input schema |
| `BaseRetriever` | `langchain_core.retrievers` | retriever | Abstract retriever interface |
| `VectorStoreRetriever` | `langchain_core.vectorstores` | retriever | Retriever backed by VectorStore |
| `VectorStore` | `langchain_core.vectorstores` | retriever_config | Vector store backend interface |
| `ChatPromptTemplate` | `langchain_core.prompts` | prompt_template | Chat prompt with message slots |
| `BaseOutputParser` | `langchain_core.output_parsers` | parser | Abstract output parser |
| `PydanticOutputParser` | `langchain_core.output_parsers` | parser | Parse into Pydantic model |
| `TextSplitter` | `langchain_text_splitters` | chunk_strategy | Hierarchical text chunking |
| `BaseDocumentLoader` | `langchain_core.document_loaders` | document_loader | Abstract document loader |
| `BaseEmbeddings` | `langchain_core.embeddings` | embedding_config | Embedding model interface |
| `BaseChatMessageHistory` | `langchain_core.chat_history` | memory_scope | Conversation memory store |
| `Document` | `langchain_core.documents` | knowledge_card | Core data container (page_content + metadata) |

## Patterns

| Trigger | Action |
|---------|--------|
| Build RAG pipeline | `loader \| splitter \| embedder \| vectorstore` then `retriever \| prompt \| llm \| parser` |
| Create tool-using agent | `create_agent(llm, tools)` — returns Runnable, not AgentExecutor |
| Compose multi-step chain | LCEL: `prompt \| llm \| parser` — each step is Runnable |
| Parse structured output | `PydanticOutputParser(pydantic_object=MyModel)` in chain |
| Fan-out parallel work | `RunnableParallel(branch_a=chain_a, branch_b=chain_b)` |
| Stream intermediate steps | `chain.stream(input)` — LCEL supports streaming natively |

## Anti-Patterns

- Using legacy `LLMChain` / `Chain` instead of LCEL Runnables
- Creating `AgentExecutor` directly instead of `create_agent` factory
- Calling `VectorStore.similarity_search()` directly instead of wrapping as `Retriever`
- Hardcoding prompt strings instead of using `ChatPromptTemplate`
- Ignoring `Document.metadata` — critical for filtering and attribution

## CEX Mapping

```text
[Document -> document_loader -> chunk_strategy] -> [embedding_config -> retriever_config]
    -> [retriever -> prompt_template -> agent/chain -> parser] -> [memory_scope]
```

## References

- source: python.langchain.com/docs/concepts/
- related: p01_kc_cex_taxonomy
