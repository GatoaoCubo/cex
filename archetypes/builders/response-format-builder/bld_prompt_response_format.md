---
id: p03_ins_response_format
kind: instruction
pillar: P05
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Response Format Builder Instructions
target: "response-format-builder agent"
phases_count: 4
prerequisites:
  - "Caller has identified the task the LLM will perform (e.g. entity extraction, summarization, classification)"
  - "The desired output structure is known at a high level (e.g. JSON object, markdown report, CSV rows)"
  - "Injection point is known or inferable: system_prompt (persistent) or user_message (per-request)"
validation_method: checklist
domain: response_format
quality: 9.1
tags: [instruction, response-format, P05, structured-output, output-design, injection]
idempotent: true
atomic: false
rollback: "Delete the produced format file. No LLM behavior changes until the format is injected into a prompt."
dependencies: []
logging: true
tldr: "Design how the LLM structures its output — sections, fields, examples — and produce a response_format artifact ready for prompt injection."
density_score: 0.92
llm_function: REASON
related:
  - bld_collaboration_response_format
  - bld_architecture_response_format
  - response-format-builder
  - bld_memory_response_format
  - p03_sp_response_format_builder
  - bld_knowledge_card_response_format
  - p11_qg_response_format
  - p01_kc_response_format
  - p01_kc_validation_schema
  - bld_examples_response_format
---
## Context
A **response_format** is a prompt-injected specification that tells the LLM how to structure its output. It is placed into the prompt (system or user turn) so the model sees the format during generation. It governs the shape of every response the agent produces for a given task. The LLM reads this artifact; the system does not execute it.
**Inputs**
| Field | Type | Description |
|---|---|---|
| `task` | string | What the LLM will do (e.g. `extract entities`, `summarize document`, `classify intent`) |
| `format_type` | enum | `json` \| `yaml` \| `markdown` \| `csv` \| `plaintext` |
| `injection_point` | enum | `system_prompt` \| `user_message` |
| `sections` | list | Named output sections or fields the format must contain (ordered) |
| `target_kind` | string | The artifact or task type this format serves (for discovery and routing) |
**Output**
A single `.md` file with YAML frontmatter (17 required fields) + 4 mandatory body sections: Format Overview, Sections, Example Output, Injection Instructions. The format specification must be written exactly as it will appear when injected into the prompt.
**Critical boundary**
- response_format = what the LLM sees during generation and uses to shape output (this builder)
- validation_schema = what the system checks *after* generation (different builder)
- parser = code that extracts structured data from LLM output (different builder)
- formatter = code that converts one format to another (different builder)
## Phases
### Phase 1: Research — Output Structure Design
Determine the exact structure the LLM must produce and how it will be consumed.
```
FOR each section in sections:
  classify:
    required:  LLM must always emit this section
    optional:  LLM emits only when relevant data is present
    repeated:  LLM emits one instance per item (array/list pattern)
  FOR json/yaml format:
    field_name (snake_case), value_type, nullable (bool)
  FOR markdown format:
    heading_level (##, ###), content_type (prose, list, table, code block)
  FOR csv format:
    column_name, data_type, column_order (integer)
  FOR plaintext format:
    structural constraints described as prose rules
injection_point selection:
  system_prompt:  format is a standing instruction (best for consistent output shape across sessions)
  user_message:   format is per-request (best for task-specific variation)
consumption context:
  WHO reads the output: human | parser | validation_schema | another LLM
  This affects how strict the format must be.
Check brain_query [IF MCP] for existing response_formats in same domain to avoid duplicates.
```
Deliverable: ordered section list with types, optionality, and injection strategy.
### Phase 2: Classify — Boundary Check
Confirm the artifact belongs to `response_format` and not a sibling kind.
```
IF caller wants code that parses the LLM's output into structured data:
  RETURN "Route to parser-builder — parsers extract data post-generation."
IF caller wants a schema to validate the LLM's output after generation:
  RETURN "Route to validation-schema-builder."
IF caller wants to transform the LLM's output from one format to another:
  RETURN "Route to formatter-builder."
IF caller wants to define a standing instruction the LLM follows:
  CHECK: is it about OUTPUT SHAPE (proceed here) or AGENT BEHAVIOR (route to system-prompt-builder)?
IF the format will be injected into the prompt so the LLM sees it during generation:
  PROCEED as response_format
```
Deliverable: confirmed `kind: response_format` with one-line justification.
### Phase 3: Compose — Build the Format Artifact
Assemble frontmatter and all 4 required body sections, following SCHEMA.md.
```
ID generation:
  id = "p05_rf_" + task_slug + "_" + format_type
  task_slug: snake_case, describes the task
  must conform to valid response_format id pattern
Frontmatter (all 17 required fields from SCHEMA.md):
  id, kind (= response_format), pillar (= P05), title, version,
  created, updated, author, task, format_type, injection_point,
  target_kind, sections (ordered list), sections_count (integer),
  quality (= null), tags, domain
Body sections (in this order):
  ## Format Overview
  One paragraph: what structure this format defines and for what task.
  State whether strict mode applies (LLM must follow exactly) or
  approximate mode (LLM uses format as a guide).
  ## Sections
  Ordered list of sections with per-section constraints:
    - Section name, heading level (for markdown), field names (for json/yaml)
    - Required vs optional for each section
    - Content type: prose | list | table | code block | key-value pairs
    - Cardinality for repeated sections (min/max items if known)
  ## Example Output
  At least one complete, realistic example.
  Must be valid for the declared format_type:
    json/yaml: parseable, no placeholder strings like "value1" or "string"
    markdown:  rendered section headers with realistic content
    csv:       header row + minimum 2 data rows
  Variables in example must match the sections list.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_response_format]] | related | 0.52 |
| [[bld_architecture_response_format]] | downstream | 0.50 |
| [[response-format-builder]] | related | 0.50 |
| [[bld_memory_response_format]] | downstream | 0.41 |
| [[p03_sp_response_format_builder]] | upstream | 0.41 |
| [[bld_knowledge_card_response_format]] | related | 0.40 |
| [[p11_qg_response_format]] | downstream | 0.39 |
| [[p01_kc_response_format]] | upstream | 0.37 |
| [[p01_kc_validation_schema]] | downstream | 0.34 |
| [[bld_examples_response_format]] | downstream | 0.34 |
