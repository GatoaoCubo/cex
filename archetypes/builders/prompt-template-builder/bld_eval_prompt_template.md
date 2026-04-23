---
id: p11_qg_prompt_template
kind: quality_gate
pillar: P11
llm_function: GOVERN
domain: prompt_template
version: 1.0.0
created: '2026-03-27'
updated: '2026-03-27'
author: builder
tags:
- eval
- P11
- quality_gate
- examples
quality: 9.0
title: 'Gate: Prompt Template'
tldr: Quality gate for reusable prompt molds with typed {{variables}}, injection points,
  and composable structure.
density_score: 0.85
related:
  - bld_knowledge_card_prompt_template
  - p11_qg_response_format
  - p11_qg_quality_gate
  - p03_ins_prompt_template
  - p03_sp_prompt_template_builder
  - bld_collaboration_prompt_template
  - p11_qg_collaboration_pattern
  - p11_qg_action_paradigm
  - p11_qg_creation_artifacts
  - p11_qg_runtime_state
---

## Quality Gate

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

## Examples

# Examples — prompt-template-builder
## Golden Example
A complete, valid `prompt_template` artifact with 19+ fields.
```yaml
id: p03_pt_knowledge_card_production
kind: prompt_template
pillar: P03
title: "Knowledge Card Production Template"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: knowledge-engine
variables:
  - name: topic
    type: string
    required: true
    default: null
    description: The subject or concept the knowledge card will cover
  - name: domain
    type: string
    required: true
    default: null
    description: The knowledge domain (e.g., machine_learning, finance, biology)
  - name: audience
    type: string
    required: false
    default: "intermediate"
    description: Target reader level (beginner, intermediate, expert)
  - name: max_sections
    type: integer
    required: false
    default: 5
    description: Maximum number of body sections to generate
  - name: include_examples
    type: boolean
    required: false
    default: true
    description: Whether to include concrete examples in each section
  - name: source_refs
    type: list
    required: false
    default: []
    description: List of source URLs or citation keys to incorporate
variable_syntax: "mustache"
composable: false
domain: knowledge
quality: 9.0
tags: [knowledge-card, pytha, production, parameterized]
tldr: "Generates a structured knowledge card for any topic and domain with configurable depth."
keywords: [knowledge, card, synthesis, structured, reusable, topic]
density_score: 0.87
# Knowledge Card Production Template
## Purpose
Produces a structured knowledge card for any topic within a specified domain. Reuse scope: any subject requiring a dense, well-organized reference document. Invoke once per topic; vary `topic`, `domain`, and `audience` to produce distinct cards from the same mold.
## Variables Table
| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| topic | string | true | null | The subject or concept the knowledge card will cover |
| domain | string | true | null | The knowledge domain (e.g., machine_learning, finance) |
| audience | string | false | "intermediate" | Target reader level (beginner, intermediate, expert) |
| max_sections | integer | false | 5 | Maximum number of body sections to generate |
| include_examples | boolean | false | true | Whether to include concrete examples in each section |
| source_refs | list | false | [] | List of source URLs or citation keys to incorporate |
## Template Body
```
You are a knowledge synthesis expert. Produce a knowledge card for the following topic.
Topic: `{{topic}}`
Domain: `{{domain}}`
Audience level: `{{audience}}`
Maximum sections: `{{max_sections}}`
Include examples: `{{include_examples}}`
Source references: `{{source_refs}}`
Structure your output as follows:
1. TLDR (1 sentence)
2. Core Definition (2-3 sentences, precise, domain-apownte)
3. Key Concepts (up to `{{max_sections}}` bullet points)
4. Relationships (how `{{topic}}` connects to adjacent concepts in `{{domain}}`)
5. Common Misconceptions (2-3 items, audience-calibrated for `{{audience}}`)
{{#include_examples}}
6. Concrete Examples (2-3 examples grounded in `{{domain}}`)
{{/include_examples}}
7. References: `{{source_refs}}`
Calibrate terminology and depth for a `{{audience}}`-level reader in `{{domain}}`.
```
## Quality Gates
| Gate | Status | Notes |
|---|---|---|
| H01 id pattern | PASS | `p03_pt_knowledge_card_production` matches `^p03_pt_[a-z][a-z0-9_]+$` |
| H02 required fields | PASS | id, kind, title, variables, quality all present |
| H03 no undeclared vars | PASS | All `{{vars}}` in body declared in variables list |
| H04 no unused vars | PASS | All 6 declared variables appear in template body |
| H05 size <= 8192 bytes | PASS | ~1.8KB |
| H06 valid syntax tier | PASS | variable_syntax: mustache |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
