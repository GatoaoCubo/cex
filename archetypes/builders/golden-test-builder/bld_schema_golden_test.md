---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for golden_test
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: golden_test

## Frontmatter Fields

### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_gt_{case_slug}) | YES | — | Namespace compliance |
| kind | literal "golden_test" | YES | — | Type integrity |
| pillar | literal "P07" | YES | — | Pillar assignment |
| title | string "Golden: {name}" | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| target_kind | string | YES | — | Artifact kind being tested |
| input | string | YES | — | Request/prompt that triggers production |
| golden_output_ref | string | YES | — | Path to golden artifact or "inline" |
| quality_threshold | float >= 9.5 | YES | 9.5 | Golden floor |
| rationale | string | YES | — | Why golden, with gate refs |
| domain | string | YES | — | Domain this test covers |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Searchability |
| tldr | string <= 160ch | YES | — | Dense summary |

### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| edge_case | boolean | REC | false | Edge case flag |
| reviewer | string | REC | — | Who approved as golden |
| approval_date | date YYYY-MM-DD | REC | — | Approval timestamp |
| linked_artifacts | object {primary, related} | REC | — | Cross-references |
| density_score | float 0.80-1.00 | REC | — | Content density |

## ID Pattern
Regex: `^p07_gt_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Input Scenario` — the complete request/prompt (verbatim)
2. `## Golden Output` — the full artifact (no abbreviation, no "...")
3. `## Rationale` — why golden, mapped to gate IDs (H01, S03, etc.)
4. `## Evaluation Criteria` — specific checks this golden validates

## Constraints
- max_bytes: 4096 (body only)
- naming: p07_gt_{case_slug}.md
- id == filename stem
- quality_threshold MUST be >= 9.5
- golden_output MUST be complete (no truncation)
- quality: null always
- rationale MUST reference gate IDs
