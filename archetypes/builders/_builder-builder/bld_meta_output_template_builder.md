---
id: bld_meta_output_template_builder
kind: builder_meta
meta: true
file_position: 6/13
pillar: P05
llm_function: PRODUCE
purpose: Meta-template for generating OUTPUT_TEMPLATE.md of any kind-builder
quality: 9.2
title: "Meta Output Template Builder"
version: "1.0.0"
author: n03_builder
tags: [_builder, builder, examples]
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
domain: "_builder construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_meta_schema_builder
  - bld_meta_instructions_builder
  - bld_output_template_kind
  - bld_meta_manifest_builder
  - bld_output_template_input_schema
  - bld_meta_config_builder
  - bld_meta_quality_gates_builder
  - bld_meta_examples_builder
  - bld_meta_system_prompt_builder
  - bld_output_template_signal
---

# Output Template: {{type_name}}
<!-- This meta-file generates the OUTPUT_TEMPLATE.md of any builder -->
<!-- REQUIRED INPUT: SCHEMA.md already generated (this file DERIVES from the schema) -->
<!-- RULE: every field here MUST exist in SCHEMA.md. Template NEVER invents. -->

```yaml
---
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a {{type_name}}
pattern: every field here exists in SCHEMA.md — template derives, never invents
---
```

<!-- NOTE: The template format depends on the type's machine_format -->
<!-- - md (majority): YAML frontmatter + markdown body -->
<!-- - json (signal): JSON payload puro -->
<!-- - yaml: YAML documento -->

<!-- ====== MD FORMAT (model_card, knowledge_card, quality_gate, and majority) ====== -->

<!-- FRONTMATTER: Generate from SCHEMA.md Frontmatter Fields -->
```yaml
---
id: {{id_prefix}}_{{slug_var}}
kind: {{type_name}}
8f: {{8f}}
pillar: {{lp}}
<!-- NOTE: {{id_prefix}} = derivar de _schema.yaml naming. Ex: p02_mc, p01_kc, p11_qg -->
<!-- NOTE: {{slug_var}} = parte variable do id. Ex: {{provider}}_{{model_slug}}, {{topic_slug}} -->
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
<!-- TYPE-SPECIFIC FIELDS: -->
<!-- Copy each field from SCHEMA.md Required/Extended fields -->
<!-- Use {{variable}} for dynamic values -->
<!-- Use literals for fixed values (kind, lp, quality: null) -->
{{schema_specific_fields}}
domain: {{domain_value}}
quality: null
tags: [{{tag_1}}, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
<!-- OPTIONAL/RECOMMENDED FIELDS: -->
{{optional_fields}}
---
```

<!-- BODY: Generate sections from SCHEMA.md Body Structure -->
<!-- For each mandatory section, create the structure with {{vars}} -->

## {{body_section_1_name}}
<!-- NOTE: Copy section structure from SCHEMA.md -->
<!-- Include tables, bullets, code blocks as the type requires -->
{{body_section_1_content_with_vars}}

## {{body_section_2_name}}
{{body_section_2_content_with_vars}}

## {{body_section_3_name}}
{{body_section_3_content_with_vars}}

<!-- NOTE: Number of sections varies per type: -->
<!-- - model_card: 4 sections (Boundary, Specifications, Capabilities, When to Use, References) -->
<!-- - knowledge_card: 7 sections domain_kc OU 6 sections meta_kc -->
<!-- - signal: 0 sections body (JSON puro, only Derivation Notes) -->
<!-- - quality_gate: 5 sections (Definition, Checklist, Scoring, Actions, Bypass) -->

<!-- ====== JSON FORMAT (signal and machine-only types) ====== -->
<!-- If machine_format == json, use JSON template instead of YAML+MD: -->
<!--
```json
{
  "{{required_field_1}}": "{{value_placeholder}}",
  "{{required_field_2}}": {{numeric_placeholder}},
  "{{optional_field_1}}": "{{value_or_omit}}"
}
```
Derivation Notes:
1. First N fields are required minimum from SCHEMA.md
2. Remaining fields are optional extensions
3. Omit absent optional fields instead of using placeholders
-->

<!-- UNIVERSAL SECTION (all md types): -->
## References
1. {{reference_1}}
2. {{reference_2}}
<!-- NOTE: Format varies: source URL, artifact ref, pricing page, etc. -->

## Properties

| Property | Value |
|----------|-------|
| Kind | `` |
| Pillar | P05 |
| Domain | _builder construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_meta_schema_builder]] | downstream | 0.35 |
| [[bld_meta_instructions_builder]] | upstream | 0.31 |
| [[bld_output_template_kind]] | related | 0.29 |
| [[bld_meta_manifest_builder]] | sibling | 0.29 |
| [[bld_output_template_input_schema]] | related | 0.27 |
| [[bld_meta_config_builder]] | downstream | 0.27 |
| [[bld_meta_quality_gates_builder]] | downstream | 0.26 |
| [[bld_meta_examples_builder]] | downstream | 0.26 |
| [[bld_meta_system_prompt_builder]] | upstream | 0.26 |
| [[bld_output_template_signal]] | related | 0.25 |
