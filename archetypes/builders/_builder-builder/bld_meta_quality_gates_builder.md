---
kind: meta_quality_gates
id: bld_meta_quality_gates_builder
meta: true
file_position: 12/13
pillar: P11
llm_function: GOVERN
purpose: Meta-template for generating QUALITY_GATES.md of any kind-builder
quality: 9.1
title: "Meta Quality Gates Builder"
version: "1.0.0"
author: n03_builder
tags: [_builder, builder, examples]
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
domain: "_builder construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_quality_gate
  - bld_memory_quality_gate
  - p03_ins_quality_gate
  - p11_qg_quality_gate
  - n04_qg_knowledge
  - bld_schema_quality_gate
  - bld_collaboration_quality_gate
  - p11_qg_kind_builder
  - p03_sp_quality_gate_builder
  - bld_quality_gate_memory_type
---

# Quality Gates: {{type_name}}
<!-- This meta-file generates the QUALITY_GATES.md of any builder -->
<!-- REQUIRED INPUT: SCHEMA.md ja gerado (gates validam o schema) -->
<!-- NOTE: HARD gates derivam dos fields required. SOFT gates derivam de quality. -->

```yaml
---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for {{type_name}} validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---
```

## HARD Gates (block publish if ANY fails)
<!-- NOTE: GERAR a partir de SCHEMA.md Required Fields + Constraints -->
<!-- HARD GATES UNIVERSAIS (presentes em TODOS os 4 builders): -->

| Gate | Check | Why |
|------|-------|-----|
| H01 | {{format_parses}} | Broken {{format}} = broken artifact |
| H02 | id matches `{{id_pattern}}` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "{{type_name}}" | Type integrity |
| H05 | {{quality_gate}} | Never self-score |
| H06 | {{required_fields_check}} | Completeness |
<!-- NOTE: H01-H06 are UNIVERSAIS (adaptar format): -->
<!-- H01: "YAML frontmatter parses" (md) or "JSON payload parses" (json) -->
<!-- H05: "quality == null" (md) or "quality_score is numeric" (json/signal) -->
<!-- H06: "N required fields present" or "core fields present" -->

<!-- HARD GATES ESPECIFICOS DO TIPO: -->
| H07 | {{hard_specific_1}} | {{why_1}} |
| H08 | {{hard_specific_2}} | {{why_2}} |
| H09 | {{hard_specific_3}} | {{why_3}} |
| H10 | {{hard_specific_4}} | {{why_4}} |
<!-- NOTE: Adicionar 2-5 specific gates based em: -->
<!-- - Campos with constraints fortes (enums, ranges, formats) -->
<!-- - Boundary violations (drift for outro type) -->
<!-- - Padroes de erros comuns do domain -->
<!-- Exemplos observados: -->
<!-- - model_card: provider in enum, context_window is integer, max_output is integer -->
<!-- - KC: tags is list, body 200-5120 bytes, no internal paths, author != orchestrator -->
<!-- - signal: status in enum, quality_score in range, no instruction fields, no routing fields -->
<!-- - quality_gate: scoring weights sum to 100%, Definition has numeric threshold -->

## SOFT Gates (contribute to score)
<!-- NOTE: GERAR a partir de SCHEMA.md Constraints + quality desejada -->
<!-- SOFT GATES UNIVERSAIS: -->

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3 | 0.5 | 10 |
<!-- NOTE: S01-S02 presentes na maioria dos types md -->

<!-- SOFT GATES ESPECIFICOS DO TIPO: -->
| S03 | {{soft_specific_1}} | {{weight}} | 10 |
| S04 | {{soft_specific_2}} | {{weight}} | 10 |
<!-- NOTE: Adicionar 5-18 gates based em: -->
<!-- - Secoes de body (each section obrigatoria = 1 gate) -->
<!-- - Formataction (tabelas, code blocks, URLs, bullets) -->
<!-- - Densidade (>= 0.80 or >= 0.85) -->
<!-- - Filler detection (no "this document", "in summary") -->
<!-- - Cross-references (linked_artifacts, data_source) -->
<!-- - Type-specific checks (pricing consistency, boolean fields, etc.) -->
<!-- Padroes de contagem observados: -->
<!-- - model_card: 15 SOFT gates (weights 0.5-1.0) -->
<!-- - KC: 20 SOFT gates (all weight 1.0) -->
<!-- - signal: 9 SOFT gates (weights 0.5-1.0) -->
<!-- - quality_gate: 7 SOFT gates (weights 0.5-1.0) -->

## Scoring Formula
<!-- NOTE: Formula UNIVERSAL (identica em all os 4 builders): -->
```text
hard_pass = all {{hard_count}} HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```
<!-- NOTE: Thresholds are UNIVERSAIS. Nao alterar. -->
<!-- Variaction possivel: KC adiciona ACCEPTABLE e NEEDS_WORK between REVIEW e REJECT -->

## Automation
<!-- NOTE: Indicar estado do validatar automatico -->
Primary: {{validation_command}}
<!-- Se validatar existe: "python _tools/validate_kc.py <file>" -->
<!-- Se planejado: "validate_artifact.py --kind {{type_name}} [PLANNED]" -->
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
<!-- NOTE: 3-5 verification items BEFORE starting to produce -->
- [ ] {{pre_check_1}}
- [ ] {{pre_check_2}}
- [ ] {{pre_check_3}}
<!-- Exemplos observados: -->
<!-- - model_card: "Official provider docs accessible", "No existing card for this model" -->
<!-- - KC: "Topic identified, not duplicate", "Sources gathered with URLs" -->
<!-- - signal: "filename uses p12_sig_ prefix", "no handoff drift" -->
<!-- - quality_gate: (nao tem; recomendata adicionar) -->

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_quality_gate]] | related | 0.48 |
| [[bld_memory_quality_gate]] | upstream | 0.39 |
| [[p03_ins_quality_gate]] | related | 0.37 |
| [[p11_qg_quality_gate]] | related | 0.36 |
| [[n04_qg_knowledge]] | related | 0.34 |
| [[bld_schema_quality_gate]] | upstream | 0.34 |
| [[bld_collaboration_quality_gate]] | related | 0.33 |
| [[p11_qg_kind_builder]] | related | 0.33 |
| [[p03_sp_quality_gate_builder]] | upstream | 0.31 |
| [[bld_quality_gate_memory_type]] | related | 0.30 |
