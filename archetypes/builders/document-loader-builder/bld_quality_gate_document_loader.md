---
id: p11_qg_document_loader
kind: quality_gate
pillar: P11
title: "Gate: document_loader"
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
domain: "file ingestion and chunking — transforms raw files into metadata-rich document chunks for RAG pipelines"
quality: 9.1
tags: [quality-gate, document-loader, P04, ingestion, chunking, RAG]
tldr: "Pass/fail gate for document_loader artifacts: format coverage, chunk strategy validity, metadata preservation, and body size limit."
density_score: 0.90
llm_function: GOVERN
---
# Gate: document_loader
## Definition
| Field | Value |
|---|---|
| metric | document_loader artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: document_loader` |

## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p04_loader_[a-z][a-z0-9_]+$` | Uppercase, missing prefix, invalid chars |
| H03 | ID equals filename stem | id field differs from file name (without .md) |
| H04 | Kind equals literal `document_loader` | kind: loader or kind: ingester or any other value |
| H05 | Quality field is null | quality: 8.0 or any non-null value |
| H06 | All required fields present | Missing formats_supported, chunk_strategy, or output_format |
| H07 | formats_supported is non-empty | Empty list or field absent |
| H08 | chunk_strategy is valid enum | Value not in: fixed, recursive, semantic, sentence, paragraph |
| H09 | output_format is valid enum | Value not in: langchain_doc, llamaindex_node, haystack_doc, raw_dict |
| H10 | Body <= 2048 bytes | Body section exceeds 2048 bytes |

## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Format coverage | 1.0 | All target formats listed with MIME types; no format described without MIME |
| Chunk strategy documentation | 1.0 | chunk_size, overlap, and boundary rule all specified |
| Metadata extraction | 1.0 | source provenance always present; format-specific fields documented |
| Overlap handling | 0.5 | Overlap value set; boundary split behavior described |
| Encoding support | 0.5 | Encoding field set; non-UTF-8 fallback strategy mentioned |
| Error handling | 1.0 | Corrupt file / parse failure behavior described per format |
| Boundary clarity | 1.0 | Explicitly not a retriever, search_tool, or db_connector |
| Domain specificity | 1.0 | Loader content specific to declared formats, not generic |
| Testability | 0.5 | Each format has verifiable output example or expected chunk count |
| Parser selection | 0.5 | Correct parser library selected for each format; tradeoffs noted |
| Output format contract | 1.0 | output_format maps correctly to downstream consumer (LangChain, LlamaIndex, etc.) |

## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |

## Bypass
| Field | Value |
|---|---|
| conditions | Experimental loader for internal format research, not production RAG |
| approver | Author self-certification with comment explaining experimental scope |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 14d — experimental loaders must reach >= 7.0 or be removed |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics) |
