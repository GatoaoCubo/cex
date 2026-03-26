---
meta: true
file_position: 10/13
pillar: P09
llm_function: CONSTRAIN
purpose: Meta-template for generating CONFIG.md of any type-builder
---

# Config: {{type_name}} Production Rules
<!-- Este meta-file gera o CONFIG.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: SCHEMA.md ja gerado (CONFIG restringe SCHEMA) -->

```yaml
---
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---
```

## Naming Convention
<!-- NOTA: Tabela UNIVERSAL presente em todos os 4 builders -->

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `{{naming_pattern}}` | `{{naming_example}}` |
| Builder directory | kebab-case | `{{builder_name}}/` |
| Frontmatter fields | snake_case | `{{example_field_1}}`, `{{example_field_2}}` |
| {{scope_extra}} | {{convention_extra}} | {{example_extra}} |

<!-- NOTA: {{naming_pattern}} = id pattern com extensao -->
<!-- Padroes observados: -->
<!-- - model_card: p02_mc_{provider}_{slug}.md -->
<!-- - KC: p01_kc_{topic_slug}.md -->
<!-- - signal: p12_sig_{event}.json -->
<!-- - quality_gate: p11_qg_{slug}.md -->
<!-- Padrao universal: {lp_lower}_{type_abbrev}_{slug}.{ext} -->

Rule: id MUST equal filename stem.

## File Paths
- Output: `cex/{{lp_dir}}/examples/{{naming_pattern}}`
- Compiled: `cex/{{lp_dir}}/compiled/{{naming_compiled}}`
<!-- NOTA: {{lp_dir}} = P02_model, P01_knowledge, P12_orchestration, P11_feedback, etc. -->
<!-- {{naming_compiled}} = mesmo padrao mas com extensao .yaml ou .json -->

## Size Limits (aligned with SCHEMA)
<!-- NOTA: Copiar limites de SCHEMA.md Constraints -->
- Body: {{body_size_limits}}
- Total: {{total_size_limit}}
- Density: >= {{density_min}}
<!-- Padroes observados: -->
<!-- - model_card: body max 4096 bytes, total ~5300, density >= 0.85 -->
<!-- - KC: body 200-5120 bytes, total ~6500, density >= 0.80 -->
<!-- - signal: payload <= 4096 bytes (preferred <= 1024) -->
<!-- - quality_gate: body max 4096, density >= 0.80 -->

## {{Type_Specific_Constraints}}
<!-- NOTA: Restricoes que nao cabem nas categorias acima -->
<!-- Exemplos observados: -->
<!-- - model_card: Provider Enum, Pricing Policy, Freshness (90 days) -->
<!-- - KC: Body Requirements (>= 4 sections, >= 3 lines each), KC Type Selection -->
<!-- - signal: Payload Restrictions, Boundary Restrictions (no instructions) -->
<!-- - quality_gate: (simples, sem extras) -->
<!-- Incluir se o tipo tem: -->
<!-- - Enums especificos (provider, status, etc.) -->
<!-- - Politicas de preenchimento (BASE TIER, null vs 0, etc.) -->
<!-- - Regras de freshness (90 days, etc.) -->
<!-- - Restricoes de body (min sections, min lines, etc.) -->
<!-- - Variantes de body structure (domain_kc vs meta_kc) -->
{{type_specific_constraint_sections}}
