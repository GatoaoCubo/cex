---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for action_prompt
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: action_prompt

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p03_ap_{task_slug}) | YES | - | Namespace compliance |
| kind | literal "action_prompt" | YES | - | Type integrity |
| pillar | literal "P03" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| title | string | YES | - | Human-readable prompt name |
| action | string (verb phrase) | YES | - | What this prompt does |
| input_required | list[string] | YES | - | What data the prompt needs |
| output_expected | string | YES | - | What the prompt produces |
| purpose | string | YES | - | Why this prompt exists |
| steps_count | integer | REC | - | Execution steps in body |
| timeout | string or null | REC | null | Max execution time |
| edge_cases | list[string], len >= 2 | YES | - | Known edge cases |
| constraints | list[string] | REC | [] | What the prompt must NOT do |
| domain | string | YES | - | Domain this prompt belongs to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "action_prompt" |
| tldr | string <= 160ch | YES | - | Dense summary |
| density_score | float 0.80-1.00 | REC | - | Content density |

## ID Pattern
Regex: `^p03_ap_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Context` — background and purpose of this action
2. `## Input` — what is received, data types, format
3. `## Execution` — what to do with the input (concise steps)
4. `## Output` — expected output format and structure
5. `## Validation` — how to verify output quality

## Constraints
- max_bytes: 3072 (body only)
- naming: p03_ap_{task_slug}.md
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- action MUST be a verb phrase ("Extract X from Y", not "X extraction")
- input_required MUST list specific data items (not "some data")
- output_expected MUST describe verifiable structure
- edge_cases MUST have >= 2 entries
- quality: null always
- action_prompt defines TASK — no identity (system_prompt) or detailed recipe (instruction)
