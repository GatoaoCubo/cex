---
kind: quality_gate
id: p11_qg_response_format
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of response_format artifacts
pattern: "few-shot learning \u2014 LLM reads these before producing"
quality: 9.0
title: 'Gate: Response Format'
version: 1.0.0
author: builder
tags:
- eval
- P11
- quality_gate
- examples
tldr: 'Quality gate for LLM output structure specs: verifies format type, injection
  point, section definitions, and downstream parseability.'
domain: response_format
created: '2026-03-27'
updated: '2026-03-27'
density_score: 0.85
related:
  - p11_qg_quality_gate
  - p03_ins_response_format
  - p11_qg_prompt_template
  - response-format-builder
  - bld_collaboration_response_format
  - bld_examples_response_format
  - bld_architecture_response_format
  - p11_qg_marketing_artifacts
  - p11_qg_runtime_state
  - p11_qg_runtime_rule
---

## Quality Gate

## Definition
A response format artifact specifies the exact output structure an LLM must produce. It declares a format type (json, yaml, markdown, csv, or plaintext), an injection point where the spec is delivered to the model (system prompt or user message), and a section structure with field-level definitions. The artifact is consumed by the LLM at generation time — it is not a post-generation validator.
Scope: files with `kind: response_format`. Does not apply to validation schemas (P06), which check outputs after generation.
## HARD Gates
Failure on any single gate means REJECT regardless of soft score.
| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p05_rf_*` | `id.startswith("p05_rf_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `response_format` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr all present |
| H07 | `format_type` is one of: json, yaml, markdown, csv, plaintext | enum membership check |
| H08 | `injection_point` is one of: system_prompt, user_message | enum membership check |
| H09 | Section structure defined with at least one named section | sections table or list has >= 1 entry |
## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.
| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Each section has explicit field definitions (name, type, required/optional) | 1.0 |
| 3  | At least one complete example output present for the declared format | 1.0 |
| 4  | Injection point matches the use case (system for persistent structure, user for per-request) | 1.0 |
| 5  | Format is parseable by a downstream consumer without ambiguity | 1.0 |
| 6  | Tags list includes `response-format` | 0.5 |
| 7  | Scope note confirms this is for LLM generation time, not post-generation validation | 1.0 |
| 8  | Field constraints documented (max length, allowed values, nullable) | 1.0 |
| 9  | Fallback format described for partial or truncated LLM output | 0.5 |
| 10 | Format is compatible with the target model's context window and output style | 0.5 |
| 11 | `tldr` is <= 160 characters | 0.5 |
**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 9.0. Each dimension contributes proportionally. Score range: 0.0 to 10.0.
## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as golden; use as reference for format design |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |
## Bypass
| Field | Value |
|-------|-------|
| condition | Format is under active negotiation with a new model provider whose output style is not yet finalized |
| approver | Domain lead must approve in writing before bypass takes effect |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver, and reason |
| expiry | 14 days from bypass grant; format must reach full compliance once model behavior is confirmed |

## Examples

# Examples: response-format-builder
## Golden Example
INPUT: "Create response_format para knowledge_card output em YAML frontmatter + markdown"
OUTPUT:
```yaml
id: p05_rf_knowledge_card
kind: response_format
pillar: P05
title: "Response Format: Knowledge Card"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
target_kind: "knowledge_card"
format_type: "yaml"
injection_point: "system_prompt"
sections: [frontmatter, tldr, core_concepts, patterns, anti_patterns, quick_reference, references]
sections_count: 7
domain: "knowledge"
quality: null
tags: [response-format, knowledge-card, yaml-frontmatter, structured-output]
tldr: "KC output format: YAML frontmatter (id, kind, pillar, tags, tldr) + 6 markdown sections, injected in system_prompt"
example_output: "see body"
composable: false
density_score: 0.91
linked_artifacts:
  primary: "knowledge-card-builder"
  related: [p06_vs_knowledge_card, p01_kc_prompt_caching]
## Format Overview
Defines how the LLM should structure knowledge_card output: YAML frontmatter with required fields followed by 6 ordered markdown sections.
Injected in system_prompt so every KC production follows the same structure.
## Sections
| # | Section | Description | Required | Constraints |
|---|---------|-------------|----------|-------------|
| 1 | frontmatter | YAML block with id, kind, pillar, quality: null, tags, tldr | yes | all required fields per P01 schema |
| 2 | TL;DR | 1-2 sentence dense summary | yes | <= 160 chars, no filler |
| 3 | Core Concepts | Key facts as bullet list | yes | >= 3 bullets, <= 80 chars each |
| 4 | Patterns | Proven approaches | yes | >= 2 bullets with context |
| 5 | Anti-Patterns | What to avoid | yes | >= 1 bullet with why |
| 6 | Quick Reference | Commands, snippets, tables | yes | Actionable, copy-paste ready |
| 7 | References | Source URLs with dates | yes | >= 1 URL, verifiable |
## Example Output
```yaml
id: p01_kc_example_topic
kind: knowledge_card
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
domain: "example"
quality: null
tags: [example, knowledge-card, template]
tldr: "Example KC showing expected output structure with all 7 sections"
## TL;DR
Example knowledge card demonstrating the response format structure.
## Core Concepts
- First key concept with concrete data
- Second key concept with specific reference
- Third key concept with actionable detail
## Patterns
- Pattern 1: when X, do Y (proven in context Z)
- Pattern 2: use A instead of B (measured 30% improvement)
## Anti-Patterns
- Anti-pattern 1: avoid X because Y (causes Z failure)
## Quick Reference
| Command | Purpose |
|---------|---------|
| `example_cmd` | Does specific thing |
## References
- Source: https://example.com (2026-03-26)
```
## Injection Instructions
- **Point**: system_prompt
- **Position**: after identity rules, before task instructions
- **Template**: "When producing a knowledge_card, use the following output format:"
- **Composable**: false — KC format is self-contained
## References
- P01_knowledge/_schema.yaml: field definitions
- knowledge-card-builder SCHEMA.md: authoritative field reference
```
WHY THIS IS GOLDEN:
- quality: null (H06 pass)
- id matches p05_rf_ pattern (H02 pass)
- kind: response_format (H04 pass)
- 17 required fields present (H07 pass)
- sections_count 7 >= 1 (H08 pass)
- format_type "yaml" in valid enum (H09 pass)
- injection_point "system_prompt" in valid enum (H10 pass)
- target_kind non-empty (H11 pass)
- Sections table with all 7 sections, ordered (S03 pass)
- Example Output complete and matches sections (S04 pass)
- Injection Instructions with point, position, template (S05 pass)
- tldr <= 160 chars, dense (S01 pass)
## Anti-Example
INPUT: "Format para output"
BAD OUTPUT:
```yaml
id: output_format
kind: format
pillar: Output
format_type: text
sections_count: 0

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
