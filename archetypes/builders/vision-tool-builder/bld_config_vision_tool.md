---
kind: config
id: bld_config_vision_tool
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: vision_tool Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_vision_{capability_slug}.md` | `p04_vision_document_ocr.md` |
| Builder directory | kebab-case | `vision-tool-builder/` |
| Frontmatter fields | snake_case | `input_types`, `output_format`, `confidence_threshold` |
| Capability slug | snake_case, lowercase, no hyphens | `document_ocr`, `scene_classifier`, `face_detector` |
| Capability names | snake_case, noun or noun_verb | `text_extraction`, `object_detection`, `layout_detection` |
| Provider names | snake_case, lowercase | `openai_vision`, `google_vision`, `tesseract`, `doctr` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P04_tools/examples/p04_vision_{capability_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_vision_{capability_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~4000 bytes
- Density: >= 0.80 (no filler)
## Output Format Enum
| Value | When to use |
|-------|-------------|
| json | Structured extraction (OCR blocks, detected objects, classification labels) |
| text | Narrative scene description, caption generation |
| table | Tabular data extraction (spreadsheets, forms, structured documents) |
## Input Type Enum
| Value | Encoding | Max Size | Notes |
|-------|----------|----------|-------|
| base64 | UTF-8 base64 string | 10MB decoded | Optional data URI prefix |
| url | HTTP/HTTPS URL string | Provider limit | Must be publicly accessible |
| file_path | Absolute or relative path | Disk limit | Local filesystem only |
| buffer | In-memory bytes object | 20MB | For pipeline integrations |
| screenshot | Captured frame buffer | 5MB | From screen capture tools |
## Capability Name Conventions
| Category | Canonical Names |
|----------|----------------|
| Text | text_extraction, layout_detection, table_extraction, handwriting_recognition |
| Objects | object_detection, logo_detection, product_recognition |
| Scene | scene_description, landmark_detection, safe_search |
| Classification | image_classification, sentiment_analysis, topic_classification |
| People | face_detection, emotion_recognition, age_estimation |
| Documents | document_parsing, form_extraction, barcode_detection |
## Provider Name Registry
`openai_vision` | `anthropic_claude` | `google_vision` | `azure_computer_vision` | `tesseract` | `doctr`
Rule: use canonical provider names from registry — custom names must document full endpoint.
