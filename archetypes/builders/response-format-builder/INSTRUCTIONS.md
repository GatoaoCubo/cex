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
quality: null
tags: [instruction, response-format, P05, structured-output, output-design, injection]
idempotent: true
atomic: false
rollback: "Delete the produced format file. No LLM behavior changes until the format is injected into a prompt."
dependencies: []
logging: true
tldr: "Design how the LLM structures its output — sections, fields, examples — and produce a response_format artifact ready for prompt injection."
density_score: 0.92
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

---

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

  ## Injection Instructions
  Exactly how to place this format specification in the prompt:
    - Which turn: system_prompt or user_message
    - Suggested phrasing to introduce the format (e.g. "Respond using this structure:")
    - Whether to include the Example Output in the same injection or separately
```

Deliverable: complete `.md` file with frontmatter + 4 body sections.

### Phase 4: Validate — Gate Check

Run all quality gates before delivering.

```
HARD gates (all must pass — fix before delivering):
  H01: YAML frontmatter parses without errors
  H02: id follows valid response_format id pattern
  H03: kind == "response_format"
  H04: pillar == "P05"
  H05: quality == null
  H06: sections_count == len(sections) (must match actual list)
  H07: format_type is one of: json, yaml, markdown, csv, plaintext
  H08: injection_point is one of: system_prompt, user_message
  H09: target_kind is non-empty
  H10: at least one complete Example Output is present in body

SOFT gates (target >= 5/9):
  S01: example output is realistic (not "string", "value1", generic placeholders)
  S02: example output is internally valid for the declared format_type
  S03: sections are ordered (not a flat unordered list)
  S04: injection_point selection is justified with one-line rationale
  S05: optional sections are explicitly labeled as optional
  S06: Format Overview states strict vs approximate mode
  S07: tags include format_type and domain
  S08: Injection Instructions include suggested phrasing
  S09: body does not contain parser code, validation code, or transformation code

IF any HARD gate fails: fix the violation and re-run that gate.
IF soft_score < 5: add "Known gaps" note.
Verify: still a PROMPT INSTRUCTION? Not drifting into system-side validation?
Set quality: null — never self-score.
```

---

## Output Contract

```
---
id: p05_rf_{{task_slug}}_{{format_type}}
kind: response_format
pillar: P05
title: "{{title}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{author}}"
task: "{{task}}"
format_type: {{json|yaml|markdown|csv|plaintext}}
injection_point: {{system_prompt|user_message}}
target_kind: {{target_kind}}
sections: [{{section_1}}, {{section_2}}, {{section_3}}]
sections_count: {{integer}}
quality: null
tags: [response-format, {{format_type}}, {{domain}}]
domain: {{domain}}
---

## Format Overview

{{one_paragraph_describing_structure_and_task}}

## Sections

{{ordered_list_of_sections_with_field_names_types_and_constraints}}

## Example Output

{{complete_realistic_example_valid_for_format_type}}

## Injection Instructions

Injection point: {{system_prompt|user_message}}
Phrasing: "{{suggested_introduction_text}}"
{{additional_injection_guidance}}
```

---

## Validation

- [ ] All 10 HARD gates pass (H01-H10)
- [ ] Soft score >= 5/9 or "Known gaps" block present
- [ ] Example output is valid for the declared `format_type` (parseable JSON, renderable markdown, etc.)
- [ ] Format spec body is written as the LLM will see it — not as a meta-description
- [ ] `sections_count` matches the actual count of items in `sections` list
- [ ] `quality: null` — never self-scored
- [ ] No parser code, validation code, or format-transformation code is embedded
- [ ] Injection point choice is justified

---

## Metacognition

**Does**
- Design the output structure the LLM sees and follows during generation
- Produce a format specification written exactly as it will be injected into a prompt
- Include a complete, realistic example so the LLM has a concrete target to match
- Distinguish required, optional, and repeated sections with explicit markup

**Does NOT**
- Validate the LLM's output after generation (validation-schema-builder)
- Extract structured data from the LLM's output (parser-builder)
- Transform the LLM's output from one format to another (formatter-builder)
- Execute LLM calls or process actual responses

**Chaining**
- Upstream: task specification and desired output shape from the caller
- Downstream: format spec is injected into a prompt template or system prompt
- Common pair: response-format-builder (output shape) + validation-schema-builder (post-check) = complete output contract
