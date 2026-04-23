---
kind: output_template
id: bld_output_template_knowledge_card
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for knowledge_card production
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Knowledge Card"
version: "1.0.0"
author: n03_builder
tags: [knowledge_card, builder, examples]
tldr: "Golden and anti-examples for knowledge card construction, demonstrating ideal structure and common pitfalls."
domain: "knowledge card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_response_format
  - bld_instruction_knowledge_card
  - bld_schema_knowledge_card
  - p03_sp_knowledge_card_builder
  - p10_out_knowledge_card
  - bld_examples_quality_gate
  - bld_config_knowledge_card
  - p01_kc_knowledge_best_practices
  - bld_knowledge_card_knowledge_card
  - bld_output_template_competitive_matrix
---

# Output Template: knowledge_card (domain_kc)
```yaml
id: p01_kc_{{topic_slug}}
kind: knowledge_card
pillar: P01
title: "{{Title 5-100 chars}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{agent_group_name}}"
domain: {{domain_name}}
quality: null
tags: [{{tag1}}, {{tag2}}, {{tag3}}, knowledge]
tldr: "{{Dense <=160ch, no self-refs}}"
when_to_use: "{{Retrieval condition}}"
keywords: [{{kw1}}, {{kw2}}, {{kw3}}]
long_tails:
  - {{long tail query 1}}
  - {{long tail query 2}}
axioms:
  - {{ALWAYS/NEVER actionable rule}}
linked_artifacts:
  primary: {{artifact_id_or_null}}
  related: [{{related_id_or_empty}}]
density_score: {{0.80_to_1.00}}
data_source: "{{source_url_or_artifact_ref}}"
# {{Title}}
## Quick Reference
` ``yaml
topic: {{topic_name}}
scope: {{scope_description}}
owner: {{owner_agent_group}}
criticality: {{low|medium|high}}
` ``
## Key Concepts
- **{{Concept 1}}**: {{concrete detail with example}}
- **{{Concept 2}}**: {{concrete detail with example}}
- **{{Concept 3}}**: {{concrete detail with example}}
## Strategy Phases
1. **{{Phase 1}}**: {{action with measurable outcome}}
2. **{{Phase 2}}**: {{action with measurable outcome}}
3. **{{Phase 3}}**: {{action with measurable outcome}}
## Golden Rules
- {{RULE 1 — actionable, concrete}}
- {{RULE 2 — actionable, concrete}}
- {{RULE 3 — actionable, concrete}}
## Flow
` ``text
[{{Input}}] -> [{{Process}}] -> [{{Decide}}] -> [{{Output}}]
` ``
## Comparativo
| {{Dimension}} | {{Option A}} | {{Option B}} |
|---------------|-------------|-------------|
| {{Row 1}} | {{val}} | {{val}} |
| {{Row 2}} | {{val}} | {{val}} |
## References
- Related artifact: {{artifact_ref}}
- Source: {{external_url}}
```
NOTE: For meta_kc, replace body with:
Executive Summary, Spec Table, Patterns, Anti-Patterns, Application, References.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_response_format]] | downstream | 0.26 |
| [[bld_instruction_knowledge_card]] | upstream | 0.25 |
| [[bld_schema_knowledge_card]] | downstream | 0.24 |
| [[p03_sp_knowledge_card_builder]] | upstream | 0.22 |
| [[p10_out_knowledge_card]] | downstream | 0.22 |
| [[bld_examples_quality_gate]] | downstream | 0.19 |
| [[bld_config_knowledge_card]] | downstream | 0.19 |
| [[p01_kc_knowledge_best_practices]] | upstream | 0.18 |
| [[bld_knowledge_card_knowledge_card]] | upstream | 0.18 |
| [[bld_output_template_competitive_matrix]] | sibling | 0.18 |
