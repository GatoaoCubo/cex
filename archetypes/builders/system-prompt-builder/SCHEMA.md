---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for system_prompt
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: system_prompt

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p03_sp_{agent_slug}) | YES | - | Namespace compliance |
| kind | literal "system_prompt" | YES | - | Type integrity |
| pillar | literal "P03" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| title | string | YES | - | Human-readable system prompt name |
| target_agent | string | YES | - | Agent this prompt is for |
| persona | string | YES | - | One-line persona description |
| rules_count | integer | YES | - | Number of rules in body |
| tone | enum: formal, technical, conversational, authoritative | YES | "technical" | Voice style |
| knowledge_boundary | string | YES | - | What agent knows and does NOT know |
| safety_level | enum: standard, strict, permissive | REC | "standard" | Constraint strictness |
| tools_listed | boolean | REC | false | Whether tools section is included |
| output_format_type | enum: markdown, json, yaml, text, structured | REC | "markdown" | Response format |
| domain | string | YES | - | Domain this agent operates in |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "system_prompt" |
| tldr | string <= 160ch | YES | - | Dense summary |
| density_score | float 0.80-1.00 | REC | - | Content density |

## ID Pattern
Regex: `^p03_sp_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Identity` — who the agent is, domain expertise, persona voice
2. `## Rules` — numbered ALWAYS/NEVER statements with justification
3. `## Output Format` — response structure, format constraints
4. `## Constraints` — knowledge boundary, safety, what NOT to do

## Constraints
- max_bytes: 4096 (body only)
- naming: p03_sp_{agent_slug}.md
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- rules_count MUST match actual count of numbered rules in body
- Rules MUST use ALWAYS/NEVER pattern
- Identity section MUST define domain expertise
- quality: null always
- system_prompt defines identity — no task instructions (that is action_prompt/instruction)
