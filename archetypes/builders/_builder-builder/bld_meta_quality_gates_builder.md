---
kind: meta_quality_gates
id: bld_meta_quality_gates_builder
meta: true
file_position: 12/13
pillar: P11
llm_function: GOVERN
purpose: Meta-template for generating QUALITY_GATES.md of any kind-builder
---

# Quality Gates: {{type_name}}
<!-- Este meta-file gera o QUALITY_GATES.md de qualquer builder -->
<!-- INPUT OBRIGATORIO: SCHEMA.md ja gerado (gates validam o schema) -->
<!-- NOTA: HARD gates derivam dos campos required. SOFT gates derivam de qualidade. -->

```yaml
---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for {{type_name}} validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---
```

## HARD Gates (block publish if ANY fails)
<!-- NOTA: GERAR a partir de SCHEMA.md Required Fields + Constraints -->
<!-- HARD GATES UNIVERSAIS (presentes em TODOS os 4 builders): -->

| Gate | Check | Why |
|------|-------|-----|
| H01 | {{format_parses}} | Broken {{format}} = broken artifact |
| H02 | id matches `{{id_pattern}}` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "{{type_name}}" | Type integrity |
| H05 | {{quality_gate}} | Never self-score |
| H06 | {{required_fields_check}} | Completeness |
<!-- NOTA: H01-H06 sao UNIVERSAIS (adaptar formato): -->
<!-- H01: "YAML frontmatter parses" (md) ou "JSON payload parses" (json) -->
<!-- H05: "quality == null" (md) ou "quality_score is numeric" (json/signal) -->
<!-- H06: "N required fields present" ou "core fields present" -->

<!-- HARD GATES ESPECIFICOS DO TIPO: -->
| H07 | {{hard_specific_1}} | {{why_1}} |
| H08 | {{hard_specific_2}} | {{why_2}} |
| H09 | {{hard_specific_3}} | {{why_3}} |
| H10 | {{hard_specific_4}} | {{why_4}} |
<!-- NOTA: Adicionar 2-5 gates especificos baseados em: -->
<!-- - Campos com constraints fortes (enums, ranges, formats) -->
<!-- - Boundary violations (drift para outro tipo) -->
<!-- - Padroes de erros comuns do dominio -->
<!-- Exemplos observados: -->
<!-- - model_card: provider in enum, context_window is integer, max_output is integer -->
<!-- - KC: tags is list, body 200-5120 bytes, no internal paths, author != orchestrator -->
<!-- - signal: status in enum, quality_score in range, no instruction fields, no routing fields -->
<!-- - quality_gate: scoring weights sum to 100%, Definition has numeric threshold -->

## SOFT Gates (contribute to score)
<!-- NOTA: GERAR a partir de SCHEMA.md Constraints + qualidade desejada -->
<!-- SOFT GATES UNIVERSAIS: -->

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3 | 0.5 | 10 |
<!-- NOTA: S01-S02 presentes na maioria dos tipos md -->

<!-- SOFT GATES ESPECIFICOS DO TIPO: -->
| S03 | {{soft_specific_1}} | {{weight}} | 10 |
| S04 | {{soft_specific_2}} | {{weight}} | 10 |
<!-- NOTA: Adicionar 5-18 gates baseados em: -->
<!-- - Secoes de body (cada secao obrigatoria = 1 gate) -->
<!-- - Formatacao (tabelas, code blocks, URLs, bullets) -->
<!-- - Densidade (>= 0.80 ou >= 0.85) -->
<!-- - Filler detection (no "this document", "in summary") -->
<!-- - Cross-references (linked_artifacts, data_source) -->
<!-- - Type-specific checks (pricing consistency, boolean fields, etc.) -->
<!-- Padroes de contagem observados: -->
<!-- - model_card: 15 SOFT gates (weights 0.5-1.0) -->
<!-- - KC: 20 SOFT gates (all weight 1.0) -->
<!-- - signal: 9 SOFT gates (weights 0.5-1.0) -->
<!-- - quality_gate: 7 SOFT gates (weights 0.5-1.0) -->

## Scoring Formula
<!-- NOTA: Formula UNIVERSAL (identica em todos os 4 builders): -->
```text
hard_pass = all {{hard_count}} HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```
<!-- NOTA: Thresholds sao UNIVERSAIS. Nao alterar. -->
<!-- Variacao possivel: KC adiciona ACCEPTABLE e NEEDS_WORK entre REVIEW e REJECT -->

## Automation
<!-- NOTA: Indicar estado do validador automatico -->
Primary: {{validation_command}}
<!-- Se validador existe: "python _tools/validate_kc.py <file>" -->
<!-- Se planejado: "validate_artifact.py --kind {{type_name}} [PLANNED]" -->
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
<!-- NOTA: 3-5 items de verificacao ANTES de comecar a produzir -->
- [ ] {{pre_check_1}}
- [ ] {{pre_check_2}}
- [ ] {{pre_check_3}}
<!-- Exemplos observados: -->
<!-- - model_card: "Official provider docs accessible", "No existing card for this model" -->
<!-- - KC: "Topic identified, not duplicate", "Sources gathered with URLs" -->
<!-- - signal: "filename uses p12_sig_ prefix", "no handoff drift" -->
<!-- - quality_gate: (nao tem; recomendado adicionar) -->
