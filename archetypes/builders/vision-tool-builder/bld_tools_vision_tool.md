---
kind: tools
id: bld_tools_vision_tool
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for vision_tool production
quality: 9.0
title: "Tools Vision Tool"
version: "1.0.0"
author: n03_builder
tags: [vision_tool, builder, examples]
tldr: "Golden and anti-examples for vision tool construction, demonstrating ideal structure and common pitfalls."
domain: "vision tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_client
  - bld_tools_cli_tool
  - bld_tools_function_def
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_path_config
  - bld_tools_prompt_version
  - bld_tools_runtime_rule
  - bld_tools_output_validator
  - bld_tools_enum_def
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_client]] | sibling | 0.50 |
| [[bld_tools_cli_tool]] | sibling | 0.49 |
| [[bld_tools_function_def]] | sibling | 0.47 |
| [[bld_tools_retriever_config]] | sibling | 0.46 |
| [[bld_tools_memory_scope]] | sibling | 0.46 |
| [[bld_tools_path_config]] | sibling | 0.45 |
| [[bld_tools_prompt_version]] | sibling | 0.45 |
| [[bld_tools_runtime_rule]] | sibling | 0.45 |
| [[bld_tools_output_validator]] | sibling | 0.44 |
| [[bld_tools_enum_def]] | sibling | 0.44 |
