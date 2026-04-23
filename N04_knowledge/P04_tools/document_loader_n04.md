---
id: p04_dl_n04_knowledge
kind: document_loader
pillar: P04
nucleus: n04
title: "Document Loader -- N04 Multi-Format Ingestion Pipeline"
version: "1.0.0"
quality: 9.1
tags: [document_loader, n04, ingestion, pdf, markdown, html, docx, repo, P04]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "Multi-format document loader for N04: handles PDF, Markdown, HTML, DOCX, code repos, and API sources. Each format has a dedicated extraction pipeline, chunking strategy, and metadata enrichment step before embedding and indexing."
density_score: null
related:
  - p04_document_loader_NAME
  - p01_kc_document_loader
  - p04_loader_pdf
  - p01_kc_rag_chunking_strategies
  - document_loader-builder
  - bld_architecture_document_loader
  - atom_07_llamaindex
  - SPEC_05_skills_runtime
  - p08_dir_rag_pipeline
  - bld_knowledge_card_document_loader
---

# Document Loader: N04 Multi-Format Ingestion Pipeline

## Overview

N04's Knowledge Gluttony demands that EVERY document format be ingestible.
This loader is the entry point for all external knowledge into the semantic corpus.
It normalizes diverse formats into the `Document` type defined in `type_def_document_types.md`.

---

## Supported Formats

| Format | Extractor | Chunking | Notes |
|--------|----------|---------|-------|
| Markdown (.md) | native | whole-doc for KC, heading-based for long | Primary CEX format |
| PDF | PyMuPDF or pdfplumber | 512-token sliding, 128-overlap | Check OCR quality >= 0.7 |
| HTML/Web | BeautifulSoup | paragraph-based | Strip nav/footer/ads |
| DOCX | python-docx | heading-based | Preserve heading hierarchy |
| Code repo | tree-sitter | function/class-level | Include docstrings |
| JSONL/CSV | pandas | row-based or fixed 512-token | Flatten to text per row |
| API (REST) | httpx | response-level | Rate-limit aware |
| YouTube transcript | yt-dlp | 512-token sliding | Auto-generated captions only if quality flag set |

---

## Per-Format Pipeline

### Markdown (Primary)

```python
def load_markdown(path: str) -> Document:
    content = open(path).read()
    frontmatter = parse_yaml_frontmatter(content)

    doc_type = (
        DocumentType.KNOWLEDGE_CARD if frontmatter.get("kind") == "knowledge_card"
        else DocumentType.ARTIFACT
    )

    return Document(
        id=uuid4(),
        type=doc_type,
        content=content,
        metadata={
            "kind": frontmatter.get("kind"),
            "pillar": frontmatter.get("pillar"),
            "nucleus": frontmatter.get("nucleus"),
            "path": path,
            "quality": frontmatter.get("quality"),
        }
    )
```

**Chunking**: whole document if < 8KB; heading-based split for larger docs.

### PDF

```python
def load_pdf(path: str, trust_level: int = 3) -> list[Document]:
    # Extract text via PyMuPDF
    doc = fitz.open(path)
    pages = [page.get_text() for page in doc]
    text = "\n\n".join(pages)

    # Quality check: OCR artifacts
    if count_ocr_artifacts(text) > 0.05:
        raise LowQualityExtractionError(f"OCR quality too low for {path}")

    # Chunk
    chunks = sliding_window(text, size=512, overlap=128)

    return [Document(
        id=uuid4(),
        type=DocumentType.CHUNK,
        content=chunk,
        metadata={"source_type": "pdf", "path": path, "trust_level": trust_level}
    ) for chunk in chunks]
```

### Code Repository

```python
def load_repo(repo_path: str, language: str) -> list[Document]:
    # Use tree-sitter for function/class-level parsing
    parser = get_parser(language)
    files = glob_files(repo_path, f"*.{language}")

    documents = []
    for file in files:
        tree = parser.parse(open(file).read().encode())
        for node in extract_function_nodes(tree):
            documents.append(Document(
                id=uuid4(),
                type=DocumentType.CHUNK,
                content=node.text,
                metadata={
                    "source_type": "code",
                    "language": language,
                    "file": file,
                    "function": node.name
                }
            ))
    return documents
```

---

## Metadata Enrichment

After extraction, N04 enriches every document with:

| Field | Source | Notes |
|-------|--------|-------|
| `ingestion_date` | now() | ISO 8601 UTC |
| `corpus` | caller-specified | default: `cex_artifacts` |
| `trust_level` | config or caller | 1-5, affects retrieval weight |
| `language` | langdetect | ISO 639-1 code |
| `token_count` | tiktoken | cl100k_base tokenizer |
| `embedding_model` | config | default: text-embedding-3-small |

---

## Batch Ingestion

For large-scale ingestion (> 100 documents):

```bash
python _tools/cex_retriever.py --ingest \
  --source /path/to/docs/ \
  --format markdown \
  --corpus cex_artifacts \
  --batch-size 50 \
  --workers 4
```

**Rate limits**: max 500 embeddings/min (OpenAI), max 100 upserts/min (pgvector free tier).
Batch processor respects limits via `con_rate_limit_config_n04.md` (P09).

---

## Error Handling

| Error | Cause | Recovery |
|-------|-------|---------|
| `LowQualityExtractionError` | OCR quality < 0.7 | Skip document, log to `P07_evals/` |
| `EmbeddingDimensionMismatch` | Wrong model | Fail fast, check `embedding_config_knowledge.md` |
| `RateLimitExceeded` | API throttle | Exponential backoff: 1s, 2s, 4s |
| `DocumentTooLarge` | > 200K tokens | Reject, request chunked version |
| `DuplicateDetected` | Similarity >= 0.97 | Skip upsert, log dedup event |

---

## Integration

| Artifact | Role |
|---------|------|
| `input_schema_knowledge_query.md` | `corpus` field maps to loader target namespaces |
| `type_def_document_types.md` | Document type classification |
| `chunk_strategy_knowledge.md` | Chunking parameters per document type |
| `api_reference_rag_apis.md` | Upsert endpoint specs |
| `workflow_rag_ingestion.md` | End-to-end orchestration of this loader |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_document_loader_NAME]] | sibling | 0.31 |
| [[p01_kc_document_loader]] | upstream | 0.31 |
| [[p04_loader_pdf]] | sibling | 0.29 |
| [[p01_kc_rag_chunking_strategies]] | upstream | 0.28 |
| [[document_loader-builder]] | related | 0.27 |
| [[bld_architecture_document_loader]] | related | 0.26 |
| [[atom_07_llamaindex]] | upstream | 0.24 |
| [[SPEC_05_skills_runtime]] | upstream | 0.24 |
| [[p08_dir_rag_pipeline]] | downstream | 0.24 |
| [[bld_knowledge_card_document_loader]] | related | 0.24 |
