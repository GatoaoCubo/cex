---
kind: examples
id: bld_examples_vision_tool
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of vision_tool artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: vision-tool-builder
## Golden Example
INPUT: "Create an OCR tool for extracting text from scanned documents"
OUTPUT:
```yaml
id: p04_vision_document_ocr
kind: vision_tool
pillar: P04
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "EDISON"
name: "Document OCR Extractor"
input_types: [base64, file_path, url]
capabilities:
  - text_extraction
  - layout_detection
  - table_extraction
output_format: json
providers: [tesseract, doctr, google_vision, azure_computer_vision]
quality: null
tags: [vision_tool, ocr, document, text_extraction, P04]
tldr: "Document OCR: 3 capabilities, JSON output, extracts text+layout+tables from scanned docs"
description: "Vision tool extracting structured text, layout blocks, and tables from scanned documents via OCR"
max_resolution: "4096x4096"
supported_formats: [png, jpg, jpeg, tiff, pdf, bmp]
confidence_threshold: 0.85
batch_support: true
max_bytes_per_image: 10485760
```
## Overview
Extracts text content, layout structure, and tabular data from scanned documents and images.
Used by document processing pipelines, data entry automation, and archiving systems.
## Input Types
### base64
Inline image payload encoded as base64 string. Max 10MB decoded.
Encoding: UTF-8 base64 string, optionally prefixed with `data:{mime};base64,`.
### file_path
Absolute or relative path to image file on local filesystem.
Supported formats: png, jpg, jpeg, tiff, pdf, bmp. PDF extracts all pages.
### url
HTTP/HTTPS URL pointing to publicly accessible image or PDF.
Timeout: 30s. Max redirect depth: 3. Requires content-type image/* or application/pdf.
## Capabilities
### text_extraction
Extracts all readable text from the image in reading order.
Confidence range: 0.0–1.0. Results filtered at confidence_threshold (default 0.85).
Output: `{text: string, blocks: [{text, confidence, bbox: {x,y,w,h}, page}]}`
### layout_detection
Detects structural regions: header, footer, paragraph, title, list, figure, table.
Output: `{regions: [{type, bbox, text, confidence}]}`
### table_extraction
Detects and extracts tabular data with row/column structure preserved.
Output: `{tables: [{rows: [[cell_text]], headers: [string], bbox, confidence}]}`
## Output Format
All capabilities return JSON. Top-level envelope:
`{capability: string, pages: int, processing_ms: int, results: {…capability_schema}}`
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_vision_ pattern (H02 pass)
- kind: vision_tool (H04 pass)
- input_types, capabilities, output_format, providers all present (H06 pass)
- body has all 4 sections: Overview, Input Types, Capabilities, Output Format (H07 pass)
- capabilities list matches ## Capabilities section names exactly (S03 pass)
- confidence_threshold declared (S05 pass)
- tldr: 71 chars <= 160 (S01 pass)
- tags: 5 items, includes "vision_tool" (S02 pass)
- Each input type has format details and size limits (S06 pass)
## Anti-Example
INPUT: "Create image analyzer"
BAD OUTPUT:
```yaml
id: image-analyzer
kind: tool
pillar: tools
name: Image Analyzer
capabilities: [analyze]
quality: 9.0
tags: [image]
```
Analyzes images.
## Capabilities
analyze: looks at images and returns info
FAILURES:
1. id: "image-analyzer" has hyphens and no `p04_vision_` prefix -> H02 FAIL
2. kind: "tool" not "vision_tool" -> H04 FAIL
3. pillar: "tools" not "P04" -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. Missing fields: input_types, output_format, providers, version, created, updated, author, tldr -> H06 FAIL
6. tags: only 1 item, missing "vision_tool" -> S02 FAIL
7. Body missing ## Input Types and ## Output Format sections -> H07 FAIL
8. Capability entry has no confidence, output schema, or examples -> S06 FAIL
9. No providers declared — caller cannot know which API backs the tool -> H06 FAIL
10. No supported_formats — caller cannot know what image types to send -> S04 FAIL
