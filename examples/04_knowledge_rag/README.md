# 04 -- Knowledge RAG Pipeline

**Difficulty:** Intermediate

## What it does

Demonstrates the full knowledge pipeline:

1. **Read** -- load a markdown file into Documents using `MarkdownReader`
2. **Chunk** -- split into sized chunks with `RecursiveChunking`
3. **Retrieve** -- find relevant chunks by keyword similarity
4. **Answer** -- pass retrieved context to `cex_sdk.chat()` for generation

This is the CEX approach to RAG (Retrieval-Augmented Generation), using
the SDK's knowledge pipeline modules.

## How to run

```bash
# Uses Ollama by default (no API key needed):
python examples/04_knowledge_rag/main.py

# Or with Claude:
export ANTHROPIC_API_KEY=sk-...
python examples/04_knowledge_rag/main.py
```

## Architecture

```
Markdown file -> MarkdownReader -> [Document] -> RecursiveChunker -> [chunks]
                                                        |
                                                 keyword search
                                                        |
                                                 top-K chunks -> chat() -> answer
```

## Notes

This example uses simple keyword matching for retrieval. For production,
use `cex_sdk.knowledge.embedder` + `cex_sdk.vectordb` for semantic search.
The `cex_retriever.py` tool provides TF-IDF retrieval across the full repo
(2184 docs, 12K vocab).
