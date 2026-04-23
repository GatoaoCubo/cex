#!/usr/bin/env python3
# 04_knowledge_rag -- Knowledge pipeline: read -> chunk -> retrieve -> answer
# Uses cex_sdk readers and chat() for a minimal RAG flow.
# ASCII-only (CEX convention).

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from cex_sdk.knowledge.reader.markdown import MarkdownReader
from cex_sdk.knowledge.chunking.recursive import RecursiveChunking
from cex_sdk.models.chat import chat

# -- Step 1: Read a markdown file into Documents --
reader = MarkdownReader()
repo_root = os.path.join(os.path.dirname(__file__), "..", "..")
sample_path = os.path.join(repo_root, "CLAUDE.md")
docs = reader.read(sample_path)
print(f"[Read] Loaded {len(docs)} document(s) from CLAUDE.md")

# -- Step 2: Chunk into smaller pieces --
chunker = RecursiveChunking(chunk_size=1500, chunk_overlap=200)
chunks = []
for doc in docs:
    chunks.extend(chunker.chunk(doc))
print(f"[Chunk] Split into {len(chunks)} chunks")

# -- Step 3: Retrieve relevant chunks by keyword match --
query = "How does the 8F pipeline work?"
query_words = set(query.lower().split())

def relevance(chunk):
    words = set(chunk.content.lower().split())
    return len(query_words & words)

ranked = sorted(chunks, key=relevance, reverse=True)
top_k = ranked[:3]
print(f"[Retrieve] Top {len(top_k)} chunks selected for query: '{query}'")

# -- Step 4: Answer using chat() with retrieved context --
context = "\n---\n".join(c.content[:500] for c in top_k)
prompt = f"Based on this context:\n\n{context}\n\nAnswer: {query}"

# Default model is claude-sonnet; switch to ollama model for free usage:
# answer = chat(prompt, model="qwen3:14b")
answer = chat(prompt, model="claude-sonnet-4-6", max_tokens=512)
print(f"\n=== Answer ===\n{answer[:500]}")
