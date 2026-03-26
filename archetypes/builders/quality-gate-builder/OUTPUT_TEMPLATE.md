---
lp: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for quality_gate production
pattern: derives from SCHEMA.md — no extra fields
---

# Output Template: quality_gate

```yaml
---
id: p11_qg_{{gate_slug}}
type: quality_gate
lp: P11
title: "Gate: {{gate_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
domain: "{{what_domain_this_protects}}"
quality: null
tags: [quality-gate, {{domain}}, {{scope}}]
tldr: "{{one_sentence_what_gate_enforces}}"
density_score: {{0.80_to_1.00}}
---

## Definition
| Property | Value |
|----------|-------|
| Metric | {{metric_name}} |
| Threshold | {{numeric_value}} |
| Operator | {{>= / <= / == / !=}} |
| Scope | {{where_gate_applies}} |

## Checklist (HARD gates — ALL must pass)
- [ ] {{check_1}}: {{description}}
- [ ] {{check_2}}: {{description}}
- [ ] {{check_3}}: {{description}}

## Scoring (SOFT gates — weighted dimensions)
| Dimension | Weight | Criteria |
|-----------|--------|----------|
| {{dim_1}} | {{pct}}% | {{what_to_check}} |
| {{dim_2}} | {{pct}}% | {{what_to_check}} |
| {{dim_3}} | {{pct}}% | {{wha
