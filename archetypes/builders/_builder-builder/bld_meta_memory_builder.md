---
kind: meta_memory
id: bld_meta_memory_builder
meta: true
file_position: 11/13
pillar: P10
llm_function: INJECT
purpose: Meta-template for generating MEMORY.md of any kind-builder
---

# Memory: {{builder_name}}
<!-- Este meta-file gera o MEMORY.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: SCHEMA.md + QUALITY_GATES.md ja gerados -->
<!-- NOTA: Memory comeca vazio e eh atualizado apos cada producao -->

```yaml
---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
memory_scope: project
observation_types: [user, feedback, project, reference]
---
```

<!-- NOTA: memory_scope = user (~/.claude/) | project (.claude/) | local (.claude/local/) -->
<!-- NOTA: observation_types = taxonomia fixa de 4 tipos. NUNCA alterar ordem ou remover -->
<!-- Decay rules: user=0.03/dia, feedback=0.00 (NUNCA), project=0.05/dia, reference=0.01/dia -->

## Observation Format (universal)
<!-- NOTA: Cada observacao DEVE seguir este formato. type: eh OBRIGATORIO -->
<!-- Tipos validos: user | feedback | project | reference -->

```
### Observation N (YYYY-MM-DD)
- type: user | feedback | project | reference
- observation: "o que foi aprendido"
- pattern: "regra generalizavel"
- evidence: "dados que suportam"
- confidence: 0.0-1.0
- outcome: SUCCESS | PARTIAL | FAILURE
- session: session_id
- tags: [tag1, tag2]
```

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
<!-- NOTA: Iniciar com 5-10 erros previsiveis baseados no SCHEMA e QUALITY_GATES -->
<!-- Padrao UNIVERSAL observado em todos os 4 builders: -->
1. Setting quality to a number instead of null ({{hard_gate_quality}} rejects any value)
2. {{mistake_id_format}} (must follow {{id_pattern}})
<!-- NOTA: Adicionar erros especificos baseados nos HARD gates -->
<!-- Exemplos observados: -->
<!-- - model_card: "Using string for context_window instead of integer" -->
<!-- - KC: "Using hyphens in id slug (must be underscores)" -->
<!-- - signal: "Using quality instead of quality_score" -->
<!-- - quality_gate: "Weights not summing to 100%" -->
3. {{mistake_type_specific_1}}
4. {{mistake_type_specific_2}}
5. {{mistake_type_specific_3}}
<!-- Incluir: erros de formato, erros de boundary, erros de campo -->

### {{Domain_Patterns_Section}}
<!-- NOTA: Secao especifica do dominio com dados acumulados -->
<!-- Exemplos observados: -->
<!-- - model_card: "Pricing Sources" (Provider | URL | Last verified) -->
<!-- - KC: "Density Boosters" (tecnicas para aumentar densidade) -->
<!-- - signal: "Recurrent Patterns" (quais campos opcionais sao mais uteis) -->
<!-- - quality_gate: "Proven Gate Patterns" (Domain | HARD count | SOFT dims | Threshold) -->
<!-- Criar tabela ou lista relevante para o dominio do tipo -->
{{domain_patterns_content}}

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | {{anticipated_friction}} |
<!-- NOTA: {{anticipated_friction}} = pontos de atrito previstos -->
<!-- Exemplos: "tiered pricing", "density threshold", "boundary drift" -->

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a {{type_name}}, update:
- New common mistake (if encountered)
- New {{domain_pattern_type}} (if discovered)
- Production counter increment
<!-- NOTA: Esta secao eh IDENTICA em todos os builders -->
