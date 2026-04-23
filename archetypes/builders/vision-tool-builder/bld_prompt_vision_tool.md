---
kind: instruction
id: bld_instruction_vision_tool
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for vision_tool
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Vision Tool"
version: "1.0.0"
author: n03_builder
tags: [vision_tool, builder, examples]
tldr: "Golden and anti-examples for vision tool construction, demonstrating ideal structure and common pitfalls."
domain: "vision tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_memory_scope
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_chunk_strategy
  - bld_instruction_prompt_version
  - bld_instruction_handoff_protocol
  - bld_instruction_function_def
  - bld_instruction_constraint_spec
  - bld_instruction_cli_tool
  - bld_instruction_search_tool
---

# Instructions: How to Produce a vision_tool
## Phase 1: RESEARCH
1. Identify the visual analysis task (OCR, object detection, classification, scene description, face detection, document parsing)
2. Define accepted input types: base64 (inline payload), url (remote image), file_path (local disk), buffer (memory), screenshot (captured frame)
3. List all capabilities the tool exposes as named operations
4. Determine output format: json (structured fields), text (narrative description), table (extracted rows/columns)
5. Select providers: OpenAI Vision API, Anthropic Claude Vision, Google Cloud Vision, Tesseract OCR, DocTR, Azure Computer Vision
6. Identify supported image formats: png, jpg, jpeg, webp, gif, bmp, tiff, pdf
7. Set confidence_threshold (default 0.8) and max_resolution constraints
8. Check for existing vision_tool artifacts to avoid duplicates
9. Confirm capability slug for id: snake_case, lowercase, no hyphens
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write Overview section: what the tool does, primary use case, who calls it
5. Write Input Types section: each type with format details, size limits, and encoding requirements
6. Write Capabilities section: each capability with description, confidence range, and concrete output example
7. Write Output Format section: JSON schema or text structure with field names and types
8. Verify body <= 2048 bytes
9. Verify id matches `^p04_vision_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p04_vision_` prefix
4. Confirm kind == vision_tool
5. Confirm input_types list contains only valid enum values
6. Confirm capabilities list matches section names in ## Capabilities body
7. Confirm output_format is json, text, or table
8. Confirm providers list is non-empty
9. Cross-check boundary: processes visual input only (not DOM, not screen control)?
10. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify vision
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | vision tool construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_memory_scope]] | sibling | 0.50 |
| [[bld_instruction_output_validator]] | sibling | 0.50 |
| [[bld_instruction_retriever_config]] | sibling | 0.49 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.47 |
| [[bld_instruction_prompt_version]] | sibling | 0.46 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.46 |
| [[bld_instruction_function_def]] | sibling | 0.46 |
| [[bld_instruction_constraint_spec]] | sibling | 0.45 |
| [[bld_instruction_cli_tool]] | sibling | 0.45 |
| [[bld_instruction_search_tool]] | sibling | 0.44 |
