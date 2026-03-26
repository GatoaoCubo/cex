---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for skill
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: skill

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_skill_{name}) | YES | - | Namespace compliance |
| kind | literal "skill" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable skill name |
| description | string <= 120ch | YES | - | One-line capability summary |
| user_invocable | boolean | YES | false | True = slash command available |
| trigger | string | YES | - | Exact invocation pattern |
| phases | list[string] | YES | - | Ordered phase names |
| when_to_use | list[string] | YES | - | Conditions favoring this skill |
| when_not_to_use | list[string] | YES | - | Conditions excluding this skill |
| examples | list[string] | YES | - | 2+ concrete invocation examples |
| quality | null | YES | null | Never self-score |
| references_dir | string | NO | - | Path to related artifacts |
| sub_skills | list[string] | NO | - | Skill IDs this skill delegates to |
| platforms | list[string] | NO | - | OS/runtime constraints |
| stack_default | string | NO | - | Default stack/runtime |

## ID Pattern
Regex: `^p04_skill_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Purpose` — what capability this skill provides and why it exists
2. `## Workflow Phases` — one subsection per phase with input/output/action
3. `## Anti-Patterns` — named failures and how to avoid them
4. `## Metrics` — measurable success criteria for this skill

## Constraints
- max_bytes: 5120 (body only)
- naming: p04_skill_{name}.md + .yaml
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- phases list MUST match ## Workflow Phases subsections in body
- user_invocable: true REQUIRES trigger to be a slash command pattern (/name)
- quality: null always
- skill has NO identity/persona — capability only, no "You are" statements
- when_to_use and when_not_to_use MUST be parallel (same abstraction level)
