---
id: p03_ins_prompt_template
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Prompt Template Builder Instructions
target: "prompt-template-builder agent"
phases_count: 4
prerequisites:
  - "Input describes a prompt with at least one dynamic slot (a value that changes per invocation)"
  - "Target rendering engine is known or inferable (mustache, bracket, jinja2, langchain, dspy)"
  - "Domain of the template is identifiable (e.g. research, code, marketing, knowledge)"
validation_method: checklist
domain: prompt_template
quality: 9.1
tags: [instruction, prompt-template, P03, parameterization, reusable]
idempotent: true
atomic: false
rollback: "Delete the produced .md file. No side effects — templates are inert until rendered."
dependencies: []
logging: true
tldr: "Extract variable slots, compose a reusable mustache template with full frontmatter, validate all 8 HARD gates, then deliver."
density_score: 0.93
llm_function: REASON
---
## Context
A **prompt_template** is a reusable mold: a prompt body where dynamic values are represented as named placeholders (`{{variable}}`). The same template produces many distinct prompts by substituting different values at invocation time. This builder operates at the prompt layer — above identity definitions (system_prompt) and below live execution.
**Inputs**
| Field | Type | Description |
|---|---|---|
| `raw_prompt` | string | The prompt or prompt sketch provided by the caller |
| `target_engine` | string | `mustache` (default) or `bracket` (only when `{{}}` conflicts with target system) |
| `domain` | string | Subject area the template serves (e.g. `code_review`, `summarization`, `research`) |
| `composable` | boolean | True if this template is designed to be embedded inside a larger template |
**Output**
A single `.md` file conforming to SCHEMA.md and OUTPUT_TEMPLATE.md. Contains YAML frontmatter (16 fields) + 5 mandatory body sections: Purpose, Variables Table, Template Body, Quality Gates, Examples.
**Boundary rules**
- If the input has zero variable slots → it is a fixed `user_prompt`, not a template. Reject and explain.
- If the input defines an agent's identity/persona → it is a `system_prompt`. Route there.
- If the input generates or improves other prompts → it is a `meta_prompt`. Route there.
## Phases
### Phase 1: Analyze — Extract Variables
Scan `raw_prompt` and identify every value that will differ between invocations.
```
FOR each token or phrase in raw_prompt:
  IF the value is domain-specific, caller-supplied, or context-dependent:
    mark as candidate variable
  ELSE (always the same regardless of invocation):
    mark as literal text
IF candidate_variables.count == 0:
  RETURN error: "No dynamic slots found. This is a fixed prompt, not a template."
FOR each candidate variable:
  name        <- snake_case descriptor (e.g. topic, audience, word_limit)
  type        <- string | list | integer | boolean | object
  required    <- true if omitting breaks the prompt; false otherwise
  default     <- concrete value for optional vars; null for required vars
  description <- one sentence stating the variable's purpose
variable_syntax:
  USE "mustache"  by default  ->  {{variable_name}}
  USE "bracket"   only when target system reserves {{ }} -> [VARIABLE_NAME]
composable:
  true  if this template will be embedded in a larger template
  false otherwise (default)
```
Deliverable: variable registry with name, type, required, default, description for every slot.
### Phase 2: Classify — Boundary Check
Confirm the artifact is `prompt_template` and not a sibling kind.
```
IF prompt defines agent role, values, or personality:
  RETURN "This is a system_prompt — route to system-prompt builder."
IF prompt is invoked once with no variable substitution:
  RETURN "This is a user_prompt — no template needed."
IF prompt's purpose is to generate or refine other prompts:
  RETURN "This is a meta_prompt — route to meta-prompt builder."
IF variables.count >= 1 AND body will be rendered repeatedly:
  PROCEED as prompt_template
```
Deliverable: confirmed `kind: prompt_template` with one-line justification.
### Phase 3: Compose — Build the Artifact
Assemble frontmatter and all 5 required body sections using OUTPUT_TEMPLATE.md as the structural guide.
```
ID generation:
  id = "p03_pt_" + topic_slug
  topic_slug: lowercase, underscores, describes template purpose
  pattern must match: ^p03_pt_[a-z][a-z0-9_]+$
Frontmatter (all 16 fields from SCHEMA.md):
  id, kind, pillar, title, version, created, updated, author,
  variables (list of objects), variable_syntax, composable,
  domain, quality (= null), tags, tldr, keywords, density_score
Body sections (in this order):
  ## Purpose
    One paragraph: what this template produces and its reuse scope.
  ## Variables Table
    Markdown table with columns: name | type | required | default | description
    One row per variable from Phase 1.
  ## Template Body
    Fenced code block containing the parameterized prompt text.
    Apply syntax: mustache -> {{variable_name}}, bracket -> [VARIABLE_NAME]
    Every variable from the table must appear at least once here.
    No hard-coded values where a variable slot was identified.
  ## Quality Gates
    Table: gate | status | notes
    Fill H01-H08 status as PASS or FAIL with one-line note each.
  ## Examples
    At least one filled example:
      - Variables block (yaml): concrete values for each variable
      - Rendered Output block: the actual prompt text after substitution
```
Deliverable: complete `.md` file with frontmatter + 5 body sections.
### Phase 4: Validate — Gate Check
Run all quality gates before delivering.
```
HARD gates (all must pass — fix before delivering):
  H01: id matches ^p03_pt_[a-z][a-z0-9_]+$
  H02: all frontmatter required fields present (id, kind, title, variables, quality)
  H03: no `{{var}}` in template body that is absent from variables list
  H04: no variable in variables list that is absent from template body
  H05: file size <= 8192 bytes
  H06: variable_syntax is "mustache" or "bracket" (not mixed)
