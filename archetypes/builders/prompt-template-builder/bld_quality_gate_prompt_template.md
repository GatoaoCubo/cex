---
id: p11_qg_prompt_template
kind: quality_gate
pillar: P11
title: "Gate: Prompt Template"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: prompt_template
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - prompt-template
  - p11
  - variables
  - reusable
tldr: "Quality gate for reusable prompt molds with typed {{variables}}, injection points, and composable structure."
llm_function: GOVERN
---
## Definition
A prompt template is a reusable text mold containing one or more `{{variable}}` placeholders filled at invocation time. It declares where in the conversation it is injected (system or user turn), documents each variable's type and constraints, and provides at least one complete invocation example with all slots filled.
Scope: files with `kind: prompt_template`. Does not apply to system prompts (fixed text, no slots) or instruction files (behavioral rules, no variable slots).
## HARD Gates
Failure on any single gate means REJECT regardless of soft score.
| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p03_pt_*` | `id.startswith("p03_pt_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `prompt_template` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr all present |
| H07 | Body contains at least one `{{variable}}` placeholder | `re.search(r'\{\{[a-z_]+\}\}', body)` matches |
| H08 | Every `{{variable}}` in body is declared in the Variables section | set(body_vars) == set(declared_vars) |
| H09 | Injection point declared as `system` or `user` | `injection_point` field equals `system` or `user` |
## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.
| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Every variable has at least one constraint (enum, regex, max_len, or range) | 1.0 |
| 3  | Syntax is uniform throughout (all `{{}}` Mustache or all `[]` bracket, never mixed) | 1.0 |
| 4  | Complete invocation example present with every variable slot filled | 1.0 |
| 5  | Default values documented for all optional variables | 0.5 |
| 6  | Tags list includes `prompt-template` | 0.5 |
| 7  | Scope note confirms this is not a system_prompt and not an instruction | 1.0 |
| 8  | Output format specified (what the rendered template is expected to produce) | 1.0 |
| 9  | Template is composable — no hard-coded surrounding structure that prevents embedding | 0.5 |
| 10 | No hardcoded content placed inside variable slots (slots are empty placeholders only) | 1.0 |
| 11 | `tldr` is <= 160 characters | 0.5 |
**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 9.0. Each dimension contributes proportionally. Score range: 0.0 to 10.0.
## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as golden; add to curated prompt library |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |
## Bypass
| Field | Value |
|-------|-------|
| condition | Template is a one-off migration aid with a documented lifespan under 30 days |
| approver | Domain lead must approve in writing before bypass takes effect |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver, and reason |
| expiry | 30 days from bypass grant; template must be retired or brought to full compliance |
