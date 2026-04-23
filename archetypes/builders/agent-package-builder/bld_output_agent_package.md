---
kind: output_template
id: bld_output_template_agent_package
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an agent_package manifest
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Agent Package"
version: "1.0.0"
author: n03_builder
tags: [agent_package, builder, examples]
tldr: "Golden and anti-examples for agent package construction, demonstrating ideal structure and common pitfalls."
domain: "agent package construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_agent_package
  - bld_schema_agent_package
  - bld_instruction_agent_package
  - bld_config_agent_package
  - p02_iso_organization_agent
  - p11_qg_agent_package
  - p03_sp_agent_package_builder
  - p10_qg_procedural_memory
  - p02_iso_[agent_name]
  - bld_knowledge_card_agent_package
---

# Output Template: agent_package
```yaml
id: p02_iso_{{agent_slug}}
kind: agent_package
pillar: P02
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
agent_name: "{{agent_name}}"
tier: "{{minimal|standard|complete|whitelabel}}"
files_count: {{integer_matching_directory}}
domain: "{{primary_domain}}"
llm_function: BECOME
portable: {{true|false}}
lp_mapping:
  manifest.yaml: P02
  system_instruction.md: P03
  instructions.md: P03
  architecture.md: P08
  output_template.md: P05
  examples.md: P07
  error_handling.md: P11
  quick_start.md: P01
  input_schema.yaml: P06
  upload_kit.md: P04
system_instruction_tokens: {{integer_token_count}}
quality: null
tags: [agent-package, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80-1.00}}
```
## Agent Identity
`{{agent_name}}` is a `{{domain}}` specialist.
`{{one_sentence_what_this_package_enables}}`
## File Inventory
| File | Pillar | Tier | Status |
|------|--------|------|--------|
| manifest.yaml | P02 | minimal | present |
| system_instruction.md | P03 | minimal | present |
| instructions.md | P03 | minimal | present |
| architecture.md | P08 | standard | {{present|absent}} |
| output_template.md | P05 | standard | {{present|absent}} |
| examples.md | P07 | standard | {{present|absent}} |
| error_handling.md | P11 | standard | {{present|absent}} |
| quick_start.md | P01 | complete | {{present|absent}} |
| input_schema.yaml | P06 | complete | {{present|absent}} |
| upload_kit.md | P04 | complete | {{present|absent}} |
| upload_kit_whitelabel.md | P04 | whitelabel | {{present|absent}} |
| branding_config.yaml | P09 | whitelabel | {{present|absent}} |
## Tier Compliance
Declared: `{{tier}}`. Files present: {{files_count}}/`{{tier_expected}}`.
`{{gap_description_if_any}}`
## Portability Notes
- Platform: {{platform_agnostic|platform_specific}}
- Hardcoded paths: {{none|list_of_violations}}
- External dependencies: `{{list_or_none}}`
## References
- Source agent: `{{agent_definition_path}}`
- Builder: agent-package-builder v1.0.0

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_agent_package]] | downstream | 0.55 |
| [[bld_schema_agent_package]] | downstream | 0.43 |
| [[bld_instruction_agent_package]] | upstream | 0.43 |
| [[bld_config_agent_package]] | downstream | 0.37 |
| [[p02_iso_organization_agent]] | upstream | 0.36 |
| [[p11_qg_agent_package]] | downstream | 0.32 |
| [[p03_sp_agent_package_builder]] | upstream | 0.32 |
| [[p10_qg_procedural_memory]] | downstream | 0.31 |
| [[p02_iso_[agent_name]]] | upstream | 0.30 |
| [[bld_knowledge_card_agent_package]] | upstream | 0.30 |
