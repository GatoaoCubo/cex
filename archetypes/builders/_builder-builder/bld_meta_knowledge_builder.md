---
kind: meta_knowledge
id: bld_meta_knowledge_builder
meta: true
file_position: 3/13
pillar: P01
llm_function: INJECT
purpose: Meta-template for generating KNOWLEDGE.md of any kind-builder
---

# Domain Knowledge: {{type_name}}
<!-- Este meta-file gera o KNOWLEDGE.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: _schema.yaml do tipo-alvo, TAXONOMY_LAYERS.yaml, pesquisa de dominio -->
<!-- NOTA: Este eh o file mais variavel entre builders — requer pesquisa real -->

```yaml
---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for {{type_name}} production
sources: {{sources_used}}
---
```

## Foundational Standard/Concept
<!-- NOTA: Origem academica ou industrial do tipo -->
<!-- Padrao observado: -->
<!-- - model_card: Mitchell et al. 2019 "Model Cards for Model Reporting" -->
<!-- - knowledge_card: "Atomic searchable facts" (CEX-internal concept) -->
<!-- - signal: "Smallest coordination artifact in P12" (operational concept) -->
<!-- - quality_gate: Cooper 1990 stage-gate process -->
<!-- Se o tipo tem origem academica, cite paper + URL -->
<!-- Se o tipo eh CEX-interno, descreva o conceito fundamental -->
{{foundational_description}}

## Industry Implementations
<!-- NOTA: Tabela comparando implementacoes do conceito em ferramentas reais -->
<!-- Padrao: Source | What it defines | CEX uses -->
<!-- Se nao ha equivalente industrial direto: omitir ou adaptar como "Related Patterns" -->

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| {{source_1}} | {{what_1}} | {{cex_use_1}} |
| {{source_2}} | {{what_2}} | {{cex_use_2}} |
| {{source_3}} | {{what_3}} | {{cex_use_3}} |

## Key Patterns
<!-- NOTA: 5-8 patterns/principles que governam a producao deste tipo -->
<!-- Extrair de _schema.yaml constraints + experiencia do dominio -->
<!-- Padrao: bullet list com padroes concretos e actionable -->
- {{pattern_1}}
- {{pattern_2}}
- {{pattern_3}}

## CEX-Specific Extensions
<!-- NOTA: Campos ou regras que o CEX adiciona alem do padrao industrial -->
<!-- Padrao: tabela Field | Justification | Closest industry equivalent -->
<!-- Se todos os campos sao padrao industrial: omitir esta secao -->

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| {{field_1}} | {{why_1}} | {{equivalent_1}} |

## Boundary vs Nearby Types
<!-- NOTA: Tabela distinguindo este tipo dos vizinhos confusos -->
<!-- Padrao identico em TODOS os 4 builders existentes -->
<!-- Buscar overlaps em TAXONOMY_LAYERS.yaml -->

| Type | What it is | Why it is NOT {{type_name}} |
|------|------------|---------------------------|
| {{confused_type_1}} | {{what_it_is}} | {{why_different}} |
| {{confused_type_2}} | {{what_it_is}} | {{why_different}} |

## References
<!-- NOTA: URLs de fontes oficiais, papers, documentacao -->
- {{reference_1}}
- {{reference_2}}
