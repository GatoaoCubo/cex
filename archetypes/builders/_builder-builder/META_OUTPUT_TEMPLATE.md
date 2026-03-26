---
meta: true
file_position: 6/13
lp: P05
llm_function: PRODUCE
purpose: Meta-template for generating OUTPUT_TEMPLATE.md of any type-builder
---

# Output Template: {{type_name}}
<!-- Este meta-file gera o OUTPUT_TEMPLATE.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: SCHEMA.md ja gerado (este file DERIVA do schema) -->
<!-- REGRA: todo campo aqui DEVE existir em SCHEMA.md. Template NUNCA inventa. -->

```yaml
---
lp: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a {{type_name}}
pattern: every field here exists in SCHEMA.md — template derives, never invents
---
```

<!-- NOTA: O formato do template depende do machine_format do tipo -->
<!-- - md (maioria): YAML frontmatter + markdown body -->
<!-- - json (signal): JSON payload puro -->
<!-- - yaml: YAML documento -->

<!-- ====== FORMATO MD (model_card, knowledge_card, quality_gate, e maioria) ====== -->

<!-- FRONTMATTER: Gerar a partir de SCHEMA.md Frontmatter Fields -->
```yaml
---
id: {{id_prefix}}_{{slug_var}}
type: {{type_name}}
lp: {{lp}}
<!-- NOTA: {{id_prefix}} = derivar de _schema.yaml naming. Ex: p02_mc, p01_kc, p11_qg -->
<!-- NOTA: {{slug_var}} = parte variavel do id. Ex: {{provider}}_{{model_slug}}, {{topic_slug}} -->
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
<!-- CAMPOS ESPECIFICOS DO TIPO: -->
<!-- Copiar cada campo de SCHEMA.md Required/Extended fields -->
<!-- Usar {{variable}} para valores dinamicos -->
<!-- Usar literais para valores fixos (type, lp, quality: null) -->
{{schema_specific_fields}}
domain: {{domain_value}}
quality: null
tags: [{{tag_1}}, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
<!-- CAMPOS OPCIONAIS/RECOMENDADOS: -->
{{optional_fields}}
---
```

<!-- BODY: Gerar secoes a partir de SCHEMA.md Body Structure -->
<!-- Para cada secao obrigatoria, crie a estrutura com {{vars}} -->

## {{body_section_1_name}}
<!-- NOTA: Copiar estrutura da secao de SCHEMA.md -->
<!-- Incluir tabelas, bullets, code blocks conforme o tipo exige -->
{{body_section_1_content_with_vars}}

## {{body_section_2_name}}
{{body_section_2_content_with_vars}}

## {{body_section_3_name}}
{{body_section_3_content_with_vars}}

<!-- NOTA: Numero de secoes varia por tipo: -->
<!-- - model_card: 4 secoes (Boundary, Specifications, Capabilities, When to Use, References) -->
<!-- - knowledge_card: 7 secoes domain_kc OU 6 secoes meta_kc -->
<!-- - signal: 0 secoes body (JSON puro, apenas Derivation Notes) -->
<!-- - quality_gate: 5 secoes (Definition, Checklist, Scoring, Actions, Bypass) -->

<!-- ====== FORMATO JSON (signal e tipos machine-only) ====== -->
<!-- Se machine_format == json, usar template JSON ao inves de YAML+MD: -->
<!--
```json
{
  "{{required_field_1}}": "{{value_placeholder}}",
  "{{required_field_2}}": {{numeric_placeholder}},
  "{{optional_field_1}}": "{{value_or_omit}}"
}
```
Derivation Notes:
- First N fields are required minimum from SCHEMA.md
- Remaining fields are optional extensions
- Omit absent optional fields instead of using placeholders
-->

<!-- SECAO UNIVERSAL (todos os tipos md): -->
## References
- {{reference_1}}
- {{reference_2}}
<!-- NOTA: Formato varia: source URL, artifact ref, pricing page, etc. -->
