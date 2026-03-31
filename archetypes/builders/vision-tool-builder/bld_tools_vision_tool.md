---
kind: tools
id: bld_tools_vision_tool
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for vision_tool production
---

# Tools: vision-tool-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing vision_tool artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P04_tools/_schema.yaml | Field definitions, vision_tool kind |
| CEX Examples | P04_tools/examples/ | Real vision_tool artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_vision_tool |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
## Provider Reference
| Provider | Type | Input Types | Key Capabilities | Notes |
|----------|------|-------------|-----------------|-------|
| openai_vision | API (cloud) | base64, url | object_detection, scene_description, classification, ocr | GPT-4V, gpt-4o; max 20MB; rate limits apply |
| anthropic_claude | API (cloud) | base64, url | scene_description, document_parsing, classification, ocr | Claude 3+ vision; max 5MB; messages API |
| google_vision | API (cloud) | base64, url, file_path | ocr, face_detection, object_detection, safe_search, landmark | Cloud Vision API; 1800 req/min free tier |
| azure_computer_vision | API (cloud) | base64, url | ocr, object_detection, scene_description, face_detection | Azure CV v4; OCR optimized for documents |
| tesseract | Local (binary) | file_path, buffer | text_extraction, layout_detection | Open source; no API key; supports 100+ languages |
| doctr | Local (Python) | file_path, buffer, base64 | text_extraction, table_extraction, layout_detection | Deep learning OCR; GPU-accelerated; high accuracy |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern matches p04_vision_, capabilities
list matches body sections, body <= 2048 bytes, quality == null, providers non-empty,
input_types are valid enum values.
