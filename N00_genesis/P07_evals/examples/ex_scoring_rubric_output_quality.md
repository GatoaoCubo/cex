---
id: p07_sr_output_quality_density
kind: scoring_rubric
pillar: P07
title: Output Quality & Density Scoring Rubric
version: 1.0.0
created: 2026-03-23
updated: 2026-03-23
author: builder_agent
domain: evaluation
quality: 9.0
tags: [quality, density, scoring, evaluation, rubric]
tldr: Rubrica 5-dimensao para avaliar qualidade e densidade de artefatos CEX com thresholds actionaveis por tier
when_to_use: Avaliar qualquer artefato CEX antes de pool promotion ou golden designation
related:
  - p01_kc_lp01_knowledge
  - p07_sr_5d_scoring
---

# Output Quality & Density Scoring Rubric

## Framework Overview
Rubrica de 5 dimensoes para avaliacao sistematica de artefatos CEX. Cada dimensao tem peso, escala 1-10, e criterios observaveis. Score final = media ponderada.

## Dimensions

### D1: Density (peso: 0.25)
Informacao unica por unidade de texto. Zero filler, zero repeticao.

| Score | Criterio |
|-------|----------|
| 9-10 | Cada frase contem fato unico, verificavel. Nenhuma frase removivel sem perda. |
| 7-8 | 1-2 frases redundantes ou genéricas. Bulk e denso. |
| 5-6 | ~20% do texto e filler ("e importante notar", "como sabemos"). |
| 3-4 | Mais da metade e repeticao ou obviedade. |
| 1-2 | Texto vazio de conteudo. Parece gerado sem instrucao. |

### D2: Correctness (peso: 0.25)
Fatos verificaveis, codigo funcional, claims com evidencia.

| Score | Criterio |
|-------|----------|
| 9-10 | Todos os fatos verificaveis. Codigo compila. Numeros com fonte. |
| 7-8 | 1 imprecisao menor (versao desatualizada, numero arredondado). |
| 5-6 | Claim central sem evidencia ou codigo com bug sintatico. |
| 3-4 | Multiplos erros factuais ou logicos. |
| 1-2 | Hallucination dominante. Dados inventados. |

### D3: Structure (peso: 0.20)
Organizacao, frontmatter, naming, sections obrigatorias.

| Score | Criterio |
|-------|----------|
| 9-10 | Frontmatter 100% completo. Todas as secoes do schema. Naming correto. |
| 7-8 | 1 campo CEX-extended ausente. Estrutura solida. |
| 5-6 | Frontmatter incompleto ou secao obrigatoria ausente. |
| 3-4 | Estrutura ad-hoc, ignora schema. |
| 1-2 | Texto corrido sem frontmatter. |

### D4: Actionability (peso: 0.20)
O leitor sabe O QUE fazer apos ler. Instrucoes executaveis, nao abstratas.

| Score | Criterio |
|-------|----------|
| 9-10 | Cada secao tem acao clara. Comandos copy-paste. Decision trees. |
| 7-8 | Maioria actionavel, 1-2 secoes descritivas sem next step. |
| 5-6 | Metade e descricao passiva ("RAG e um paradigma..."). |
| 3-4 | Texto academico. Leitor nao sabe por onde comecar. |
| 1-2 | Puramente teorico. Zero aplicabilidade pratica. |

### D5: Specificity (peso: 0.10)
Concreto vs generico. Numeros > adjetivos. Exemplos > descricoes.

| Score | Criterio |
|-------|----------|
| 9-10 | Numeros concretos, exemplos reais, thresholds definidos. |
| 7-8 | Maioria especifico, 1-2 claims vagos ("melhora performance"). |
| 5-6 | Mix de concreto e generico. |
| 3-4 | Maioria generico ("use boas praticas"). |
| 1-2 | Completamente abstrato. Aplicavel a qualquer dominio. |

## Scoring Protocol

```text
1. Ler artefato completo
2. Pontuar cada dimensao (1-10) com justificativa de 1 frase
3. Calcular: final = D1*0.25 + D2*0.25 + D3*0.20 + D4*0.20 + D5*0.10
4. Classificar tier:
   >= 9.5: Golden (pool promotion automatica)
   >= 8.0: Skilled (pool eligible, remember())
   >= 7.0: Learning (experimental, iteracao necessaria)
   < 7.0: Rejected (redo obrigatorio)
```

## Calibration Examples

| Artefato | D1 | D2 | D3 | D4 | D5 | Final | Tier |
|----------|----|----|----|----|----| ------|------|
| KC com 5 fatos unicos, frontmatter completo, flow ASCII | 9 | 9 | 10 | 8 | 9 | 9.0 | Skilled |
| Agent com "TODO" no frontmatter, overview generico | 5 | 7 | 4 | 6 | 5 | 5.6 | Rejected |
| Skill com metricas reais, anti-patterns, 3 fases | 8 | 8 | 9 | 9 | 8 | 8.4 | Skilled |

## Anti-Patterns in Scoring
- Inflar score por "parece completo" sem verificar fatos (D2 trap)
- Penalizar brevidade — documentos curtos podem ter density 10
- Ignorar naming/frontmatter porque "o conteudo e bom" (D3 still matters)
- Score 7.0 como "default seguro" — se nao sabe, releia e pontue honestamente

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_lp01_knowledge]] | upstream | 0.18 |
| [[p07_sr_5d_scoring]] | sibling | 0.16 |
