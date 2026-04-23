---
id: bld_output_template_document_loader
kind: output_template
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
domain: document_loader
llm_function: PRODUCE
quality: 9.0
tags: [output_template, document_loader, ingestion, chunking, P04]
tldr: "Fillable template for document_loader artifacts. Replace all {{vars}} with concrete values."
density_score: 1.0
title: Output Template ISO - document_loader
related:
  - bld_schema_document_loader
  - p03_sp_document_loader_builder
  - bld_instruction_document_loader
  - bld_examples_document_loader
  - p04_loader_pdf
  - p11_qg_document_loader
  - document_loader-builder
  - bld_knowledge_card_document_loader
  - bld_memory_document_loader
  - bld_config_document_loader
---
# Output Template: document_loader

## Frontmatter Template
```yaml
---
id: p04_loader_{{format_slug}}
kind: document_loader
pillar: P04
version: 1.0.0
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
author: {{author}}
name: "{{Human Readable Loader Name}}"
formats_supported:
  - {{mime_type_1}}
  - {{mime_type_2}}
chunk_strategy: {{fixed|recursive|semantic|sentence|paragraph}}
output_format: {{langchain_doc|llamaindex_node|haystack_doc|raw_dict}}
chunk_size: {{int_tokens}}
overlap: {{int_tokens}}
encoding: {{utf-8|auto-detect}}
quality: null
tags: [document_loader, {{format_tag}}, {{domain_tag}}, P04]
tldr: "{{<=160 char summary of what formats, chunk strategy, and output}}"
description: "{{<=200 char description of use case and pipeline role}}"
metadata_fields:
  - source
  - {{format_specific_field_1}}
  - {{format_specific_field_2}}
---
```

## Body Template

```markdown
## Overview
{{2-3 sentences: what file formats this loader handles, primary use case (e.g., PDF ingestion
for legal document RAG), and pipeline position (stage 1: raw file -> chunked Documents).}}

## Formats
| Format | MIME Type | Parser | Limitations |
|--------|-----------|--------|-------------|
| {{format_name}} | {{mime_type}} | {{parser_library}} | {{known_limits}} |
| {{format_name}} | {{mime_type}} | {{parser_library}} | {{known_limits}} |

## Chunking
- Strategy: {{chunk_strategy}}
- Chunk size: {{chunk_size}} tokens
- Overlap: {{overlap}} tokens
- Boundary rule: {{how boundaries are respected, e.g., "never split mid-sentence"}}
- Splitter: {{LangChain class or equivalent, e.g., RecursiveCharacterTextSplitter}}

## Metadata
| Field | Type | Source | Notes |
|-------|------|--------|-------|
| source | string | file path or URL | Required — provenance for every chunk |
| {{field}} | {{type}} | {{how extracted}} | {{notes}} |
| {{field}} | {{type}} | {{how extracted}} | {{notes}} |
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_document_loader]] | downstream | 0.44 |
| [[p03_sp_document_loader_builder]] | related | 0.44 |
| [[bld_instruction_document_loader]] | related | 0.44 |
| [[bld_examples_document_loader]] | related | 0.38 |
| [[p04_loader_pdf]] | related | 0.38 |
| [[p11_qg_document_loader]] | downstream | 0.38 |
| [[document_loader-builder]] | related | 0.34 |
| [[bld_knowledge_card_document_loader]] | related | 0.33 |
| [[bld_memory_document_loader]] | related | 0.33 |
| [[bld_config_document_loader]] | related | 0.31 |
