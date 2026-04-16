---
kind: output_template
id: bld_output_template_agent_profile
pillar: P05
llm_function: PRODUCE
purpose: Fillable scaffold for agent_profile artifacts (persona + identity vectors + constraints)
quality: 9.0
title: "Output Template Agent Profile"
version: "1.1.0"
author: n03_builder
tags: [agent_profile, builder, output_template, P05]
keywords: [template, scaffold, persona_frame, identity_vector, placeholder]
triggers: ["render agent_profile", "fill p02_ap_ template", "scaffold persona artifact"]
tldr: "Fillable output scaffold producing p02_ap_{slug}.md with frontmatter (15 fields) + 6 body sections: Overview, Identity Vectors, Capabilities, Constraints, Collaborators, Compliance."
domain: "agent_profile construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
---

# Output Template: agent_profile

Every `{{var}}` below MUST be replaced. Remove this header block before saving.
Target filename: `p02_ap_{{slug}}.md` (slug: lowercase_snake_case, matches `^[a-z][a-z0-9_]+$`).

## Frontmatter (required — do not drop fields)
```yaml
---
id: p02_ap_{{slug}}
kind: agent_profile
pillar: P02
title: "{{display_name}}"
version: "1.0.0"
created: "{{iso_date}}"
updated: "{{iso_date}}"
author: "{{creator_nucleus}}"
domain: "{{operational_domain}}"
agent_type: "{{operator|analyst|automaton}}"
expertise: [{{skill_1}}, {{skill_2}}, {{skill_3}}]
status: "active"
quality: null
tags: [agent_profile, {{domain_tag}}, {{role_tag}}]
tldr: "{{one_line_persona_summary}}"
---
```

## Overview
`{{two_to_four_sentence_description_of_role_scope_and_primary_consumer}}`

## Identity Vectors
- **Domain of authority**: `{{vector_1_value}}` // `{{rationale}}`
- **Voice register**: `{{vector_2_value}}` // `{{rationale}}`
- **Decision latency**: `{{vector_3_value}}` // `{{rationale}}`

## Capabilities (3-7 verb phrases, present tense)
1. `{{verb_phrase_1}}`
2. `{{verb_phrase_2}}`
3. `{{verb_phrase_3}}`
4. `{{verb_phrase_4}}`

## Constraints (ALWAYS / NEVER / IF-THEN — minimum 3)
- ALWAYS `{{constraint_1}}`. Source: `{{policy_or_regulation}}`.
- NEVER `{{constraint_2}}`. Source: `{{policy_or_regulation}}`.
- IF `{{condition}}` THEN {{action}}. Source: `{{policy_or_regulation}}`.

## Collaborators (reference sibling agent_profile ids, not roles)
| Profile ID | Relationship | Hand-off artifact |
|---|---|---|
| p02_ap_`{{peer_1}}` | {{upstream|downstream|peer}} | `{{kind_of_handoff}}` |
| p02_ap_`{{peer_2}}` | {{upstream|downstream|peer}} | `{{kind_of_handoff}}` |

## Compliance
- Framework: {{ISO_IEC_23894|IEEE_7000|NIST_AI_RMF|other}}
- Review cadence: {{monthly|quarterly|annual}}
- Reviewer: `{{role_or_nucleus}}`

---
Validation: run `python _tools/cex_score.py --apply p02_ap_{{slug}}.md`
Schema reference: `bld_schema_agent_profile.md`
Quality gate: `bld_quality_gate_agent_profile.md`
