---
kind: knowledge_card
id: bld_knowledge_card_vision_tool
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for vision_tool production — visual analysis and OCR specification
sources: OpenAI Vision API docs, Google Cloud Vision API, Tesseract OCR, DocTR, Azure Computer Vision, Anthropic Claude Vision
---

# Domain Knowledge: vision_tool
## Executive Summary
Vision tools are visual input processors that accept images (base64, URL, file path, buffer, screenshot) and return structured data via cloud vision APIs or local OCR engines. They define input types, capabilities, output format, and provider mapping. Vision tools are purely input-processing contracts — they do not interact with DOM (browser_tool), control the screen (computer_use), or ingest documents without visual analysis (document_loader).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools) |
| llm_function | CALL (invocable) |
| Output formats | json, text, table |
| Input types | base64, url, file_path, buffer, screenshot |
| Default confidence | 0.8 |
| Max body bytes | 2048 |
## Provider Capabilities Matrix
| Capability | OpenAI Vision | Anthropic | Google Vision | Tesseract | DocTR | Azure CV |
|-----------|--------------|-----------|--------------|-----------|-------|---------|
| text_extraction (OCR) | YES | YES | YES | YES | YES | YES |
| object_detection | YES | YES | YES | NO | NO | YES |
| scene_description | YES | YES | NO | NO | NO | YES |
| classification | YES | YES | YES | NO | NO | YES |
| face_detection | NO | NO | YES | NO | NO | YES |
| document_parsing | YES | YES | YES | NO | YES | YES |
| table_extraction | YES | YES | NO | NO | YES | YES |
| layout_detection | NO | YES | YES | NO | YES | YES |
## Patterns
- **Input encoding**: base64 is fastest for small images (<1MB); url preferred for large files; file_path for local pipelines; buffer for in-memory processing
- **Confidence filtering**: always filter results below confidence_threshold before returning — raw model output includes low-confidence noise
- **Provider fallback**: declare primary provider + fallback in providers list (e.g., `[google_vision, tesseract]`)
- **Format declaration**: always declare supported_formats — providers differ (Tesseract: no PDF native; OpenAI: no TIFF)
- **Resolution limits**: OpenAI max 20MB / 2048px longest side (auto-downscaled); Google max 20MB; Tesseract: no hard limit but >600 DPI recommended for OCR
| Pattern | When to use |
|---------|-------------|
| Cloud API (OpenAI/Anthropic/Google/Azure) | Complex scenes, semantic understanding, multi-language OCR |
| Local OCR (Tesseract/DocTR) | Privacy-sensitive docs, high volume, air-gapped environments |
| Hybrid (cloud + local fallback) | Reliability-critical pipelines |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No input_types declared | Caller sends wrong format; runtime error not spec error |
| Missing confidence_threshold | Low-confidence results corrupt downstream data |
| Conflating with browser_tool | vision_tool reads static image; browser_tool interacts with live DOM |
| Conflating with computer_use | vision_tool receives image as input; computer_use controls the cursor |
| Provider list empty | Caller cannot select or configure the backing API |
| No supported_formats | Caller sends TIFF to Tesseract-only tool; silent failure |
| Implementation code in spec | Spec is a contract, not source; code belongs in implementing repo |
## Application
1. Identify visual task: what does the tool see, and what does it return?
2. Enumerate input types: how will callers provide images? (base64 for inline, url for remote, file_path for local)
3. Define capabilities: named operations the tool performs on the visual input
4. Select providers: cloud (OpenAI/Anthropic/Google/Azure) vs. local (Tesseract/DocTR) based on privacy, volume, complexity
5. Set output format: json for structured extraction, text for descriptions, table for tabular data
6. Declare constraints: max_resolution, supported_formats, confidence_threshold, batch_support
## References
- OpenAI Vision: platform.openai.com/docs/guides/vision
- Anthropic Vision: docs.anthropic.com/claude/docs/vision
- Google Cloud Vision: cloud.google.com/vision/docs
- Azure Computer Vision: learn.microsoft.com/en-us/azure/ai-services/computer-vision
- Tesseract OCR: github.com/tesseract-ocr/tesseract
- DocTR: github.com/mindee/doctr
