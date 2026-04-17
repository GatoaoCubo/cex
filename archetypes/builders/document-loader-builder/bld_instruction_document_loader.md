---
id: bld_instruction_document_loader
kind: instruction
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
domain: document_loader
llm_function: REASON
quality: 9.0
tags: [instruction, document_loader, ingestion, chunking, P04]
tldr: "3-phase pipeline to produce a valid document_loader artifact: Research formats -> Compose spec -> Validate gates."
density_score: 0.92
title: Instruction ISO - document_loader
---
# Instructions: How to Produce a document_loader

## Phase 1: RESEARCH
1. Identify all file formats the loader must handle — collect MIME types, not extensions.
2. For each format, select parser library: PDF->PyPDF2/pdfplumber/Unstructured; HTML->BeautifulSoup/trafilatura; CSV->pandas; DOCX->python-docx; MD->markdown-it; JSON->stdlib; PPTX->python-pptx; XLSX->openpyxl.
3. Determine chunk_strategy based on content structure: narrative->sentence/paragraph; structured->recursive; uniform batches->fixed; topic-aware->semantic.
4. Set chunk_size and overlap: default 512 tokens / 64 overlap; adjust for context window of target LLM.
5. List all metadata to preserve: at minimum source (file path/url), format, page/line number, section heading, author where available.
6. Identify encoding risks: binary PDFs, Latin-1 legacy CSVs, UTF-16 Word docs — plan detection and fallback.
7. Confirm output_format required by downstream: LangChain Document, LlamaIndex Node, Haystack Document, or raw dict.
8. Check CEX pool for existing loaders that cover same formats — avoid duplicate artifacts.
9. Validate format list has no overlap with retriever or search_tool domains.
10. Note any format-specific limitations: scanned PDFs need OCR, HTML needs boilerplate stripping, CSV needs delimiter detection.

## Phase 2: COMPOSE
1. Read bld_schema_document_loader.md — internalize all required fields and constraints.
2. Generate id: `p04_loader_{format_slug}` where format_slug is the primary format (e.g., pdf, html, csv_tabular).
3. Write frontmatter: id, kind, pillar, version, created, updated, author, name, formats_supported (MIME list), chunk_strategy, output_format, quality: null, tags, tldr, metadata_fields, chunk_size, overlap, encoding.
4. Write `## Overview`: 2-3 sentences on what formats, primary use case, pipeline stage (stage 1 of RAG).
5. Write `## Formats`: table with columns Format | MIME Type | Parser | Limitations — one row per format.
6. Write `## Chunking`: chunk_strategy name, chunk_size, overlap, boundary handling rule, splitter class reference.
7. Write `## Metadata`: table of extracted fields — Field | Type | Source | Notes — include source provenance always.
8. Verify total body stays under 2048 bytes — trim descriptions before removing required fields.
9. Confirm tags include "document_loader" and at least 2 domain tags.
10. Set quality: null — never self-score.

## Phase 3: VALIDATE
1. Parse frontmatter block as YAML — must be error-free (H01).
2. Verify id matches regex `^p04_loader_[a-z][a-z0-9_]+$` (H02).
3. Confirm id equals filename stem (H03).
4. Confirm kind equals literal "document_loader" (H04).
5. Confirm quality is null (H05).
6. Check all required fields present: id, kind, pillar, version, created, updated, author, name, formats_supported, chunk_strategy, output_format (H06).
7. Verify formats_supported is non-empty list of MIME types (H07).
8. Verify chunk_strategy is one of: fixed, recursive, semantic, sentence, paragraph (H08).
9. Verify output_format is one of: langchain_doc, llamaindex_node, haystack_doc, raw_dict (H09).
10. Count body bytes — must be <= 2048 (H10).


## Validation
- Verify output matches expected schema before delivery
- Check all required fields are present and non-empty
- Confirm no template placeholders remain in output


## Edge Cases
- Empty input: return structured error with guidance
- Partial input: fill defaults, flag missing fields
- Oversized input: truncate with warning, preserve structure
