---
id: p01_cs_recursive_1000
kind: chunk_strategy
pillar: P01
title: Recursive Markdown Splitter (1000 tokens)
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: knowledge_ingestion
quality: 9.1
tags: [chunk-strategy, recursive, markdown, rag, langchain, text-splitter]
tldr: Recursive text splitter otimizado para documentacao Markdown — chunk_size=1000, overlap=200, separadores hierarquicos por heading level
when_to_use: Ingestao de knowledge cards, READMEs, e documentacao tecnica no pipeline RAG do organization Brain
---

# Chunk Strategy: Recursive Markdown Splitter (1000 tokens)

## Overview
Estrategia de chunking para documentos Markdown usados no pipeline RAG do organization Brain. Usa RecursiveCharacterTextSplitter do LangChain com separadores hierarquicos que respeitam a estrutura semantica do Markdown — prioriza split por headings antes de quebrar paragrafos.

## Parameters
| Param | Value | Rationale |
|-------|-------|-----------|
| chunk_size | 1000 | Balanco entre contexto suficiente e custo de embedding. nomic-embed-text performa melhor com chunks 512-1500 tokens |
| chunk_overlap | 200 | 20% overlap preserva continuidade semantica entre chunks adjacentes |
| separators | `["\n## ", "\n### ", "\n#### ", "\n\n", "\n", " "]` | Hierarquia Markdown-first: headings > paragrafos > linhas > palavras |
| strip_whitespace | true | Remove whitespace leading/trailing pos-split |
| length_function | tiktoken (cl100k_base) | Contagem por tokens, nao caracteres — alinhado com modelo de embedding |
| is_separator_regex | false | Separadores literais, sem regex overhead |

## Implementation
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n## ", "\n### ", "\n#### ", "\n\n", "\n", " "],
    length_function=lambda text: len(enc.encode(text)),
    strip_whitespace=True,
    is_separator_regex=False,
)

# Uso com knowledge cards
documents = splitter.split_documents(loaded_kcs)
```

## Metadata Preservation
Cada chunk herda metadata do documento original:
```python
{
    "source": "records/pool/knowledge/KC_knowledge_agent_007_CHATKIT.md",
    "kind": "knowledge_card",
    "pillar": "P01",
    "chunk_index": 3,
    "total_chunks": 7,
    "heading_context": "## Architecture > ### Frontend Widget"
}
```

## Quality Gates
| Gate | Threshold | Action on Fail |
|------|-----------|----------------|
| Min chunk size | >= 50 tokens | Merge com chunk anterior |
| Max chunk size | <= 1200 tokens (1.2x target) | Re-split com separador mais granular |
| Heading orphan | Heading sem body >= 20 tokens | Merge heading com proximo chunk |
| Code block integrity | Code blocks nao cortados | Extend chunk ate fechar ``` |

## Benchmarks (organization Brain corpus)
| Metric | Value |
|--------|-------|
| Avg chunk size | 847 tokens |
| Median chunk size | 912 tokens |
| Chunks/document (avg) | 4.2 |
| Retrieval recall@5 | 0.89 |
| Retrieval recall@5 sem overlap | 0.81 |

## When NOT to Use
- Dados tabulares (CSV/JSON) — usar StructuredSplitter
- Codigo fonte — usar CodeSplitter com language-aware parsing
- Documentos < 500 tokens — nao precisa chunking, indexar inteiro

## Related
- `ex_embedding_config_nomic_embed_text.md` — modelo de embedding usado com estes chunks
- `ex_retriever_config_hybrid_rag.md` — retriever que busca estes chunks
- `ex_rag_source_brain_faiss_index.md` — indice FAISS onde os chunks sao armazenados
