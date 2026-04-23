---
kind: quality_gate
id: p11_qg_vision_tool
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of vision_tool artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: vision_tool"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, vision-tool, P04, image, ocr, confidence-threshold]
tldr: "Pass/fail gate for vision_tool artifacts: input type coverage, capability documentation, provider mapping, confidence thresholds, and output schema."
domain: "visual analysis tool definition — image processrs with declared input types, capabilities, providers, and structured output"
created: "2026-03-28"
updated: "2026-03-28"
density_score: 0.90
related:
  - p11_qg_function_def
  - p11_qg_document_loader
  - p11_qg_browser_tool
  - p11_qg_cli_tool
  - p11_qg_computer_use
  - bld_examples_vision_tool
  - p11_qg_chunk_strategy
  - p11_qg_search_tool
  - p11_qg_enum_def
  - p11_qg_constraint_spec
---

## Quality Gate

# Gate: vision_tool
## Definition
| Field | Value |
|---|---|
| metric | vision_tool artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: vision_tool` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p04_vision_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, missing prefix, or spaces |
| H03 | ID equals filename stem | `id: p04_vision_ocr` but file is `p04_vision_document.md` |
| H04 | Kind equals literal `vision_tool` | `kind: tool` or `kind: image_tool` or any other value |
| H05 | Quality field is null | `quality: 8.5` or any non-null value |
| H06 | All required fields present | Missing any of: input_types, capabilities, output_format, providers |
| H07 | Body has all 4 required sections | Missing ## Overview, ## Input Types, ## Capabilities, or ## Output Format |
| H08 | input_types contains only valid enum values | `input_types: [file]` — "file" is not valid (must be "file_path") |
| H09 | output_format is one of: json, text, table | `output_format: xml` or unrecognized value |
| H10 | capabilities list non-empty and matches body section names | `capabilities: []` or capability in list has no matching ## Capabilities section |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Input type coverage | 1.0 | All meaningful input formats documented with encoding details and size limits |
| Capability documentation | 1.5 | Each capability has description, confidence range, and output schema |
| Provider mapping | 1.0 | Each provider listed; capabilities mapped to providers that support them |
| Confidence threshold declared | 1.0 | confidence_threshold present and justified; not left as implicit default |
| Supported formats declared | 1.0 | supported_formats list present; provider-specific format limitations noted |
| Output schema completeness | 1.5 | Output format section shows JSON envelope with field names and types |
| Boundary clarity | 1.0 | Explicitly distinguishes from browser_tool, computer_use, document_loader |
| Domain specificity | 1.0 | Capabilities and output schemas are specific to the declared visual domain |
| Batch support declared | 0.5 | batch_support field present with behavioral description if true |
| Resolution constraints | 0.5 | max_resolution and max_bytes_per_image declared for payload planning |
| Testability | 1.0 | Each capability has a concrete output example a caller can validate against |
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
| conditions | Internal prototype used only during provider evaluation, never shipped to production |
| approver | Author self-certification with comment explaining prototype-only scope |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 14d — prototypes must be promoted to >= 7.0 or removed from repo |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics), H10 (unmatched capabilities break validation pipeline) |

## Examples

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
author: "builder_agent"
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
