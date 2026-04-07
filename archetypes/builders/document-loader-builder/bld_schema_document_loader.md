---
kind: schema
id: bld_schema_document_loader
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for document_loader
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Document Loader"
version: "1.0.0"
author: n03_builder
tags: [document_loader, builder, examples]
tldr: "Golden and anti-examples for document loader construction, demonstrating ideal structure and common pitfalls."
domain: "document loader construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Schema: document_loader
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_loader_{format_slug}) | YES | - | Namespace compliance |
| kind | literal "document_loader" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable loader name |
| formats_supported | list[string MIME], len >= 1 | YES | - | MIME types handled |
| chunk_strategy | enum: fixed, recursive, semantic, sentence, paragraph | YES | recursive | Chunking algorithm |
| output_format | enum: langchain_doc, llamaindex_node, haystack_doc, raw_dict | YES | langchain_doc | Output document type |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "document_loader" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What formats and use case |
| metadata_fields | list[string] | REC | - | Extracted metadata keys |
| chunk_size | int | REC | 512 | Tokens or chars per chunk |
| overlap | int | REC | 64 | Overlap between chunks |
| encoding | string | REC | "utf-8" | Default text encoding |

## ID Pattern
Regex: `^p04_loader_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Overview` — what formats, use case, pipeline stage
2. `## Formats` — each format: MIME type, parser library, known limitations
3. `## Chunking` — strategy, chunk_size, overlap, boundary handling
4. `## Metadata` — extracted metadata fields, source tracking per format

## Constraints
- max_bytes: 2048 (body only)
- naming: p04_loader_{format_slug}.md (single file per loader)
- machine_format: yaml (compiled artifact)
- id == filename stem
- formats_supported MUST list valid MIME types
- chunk_strategy MUST be one of the enum values
- quality: null always
- NO implementation code in body — spec only
