# CEX Analysis: model_card (P02)

**Author**: EDISON | **Date**: 2026-03-26 | **Quality Target**: 9.0+

---

## Exemplo Atual

### Arquivo: `p02_mc_claude_opus_4.md`

**Frontmatter** (12 campos):
| Campo | Valor | Observacao |
|-------|-------|------------|
| id | p02_mc_claude_opus_4 | Correto: prefixo p02_mc_ |
| type | model_card | OK |
| lp | P02 | OK |
| model_name | claude-opus-4-0520 | Campo especifico de model_card |
| provider | anthropic | Campo especifico |
| context_window | 200000 | Campo especifico |
| pricing | nested (input/output/unit) | Estrutura rica |
| version | 1.0.0 | Semver OK |
| created | 2026-03-24 | OK |
| author | STELLA | Questionavel: STELLA orquestra, nao produz |
| domain | model_selection | OK |
| quality | 9.0 | ALERTA: auto-atribuido (BP KC proibe) |

**Body** (3 secoes):
1. Specifications — tabela tecnica (model, provider, context, pricing, features)
2. When to Use — tabela decisao (scenario vs use_opus?)
3. CODEXA Satellite Mapping — bullets mapeando sat -> modelo -> razao

**Formato**: Variante A (meta_kc/tecnico). Coerente com natureza spec.

**Score do Exemplo**: 7.5/10
- (+) Dados concretos, sem filler, tabelas uteis
- (+) Naming correto (p02_mc_)
- (-) quality auto-atribuido (deveria ser null)
- (-) author = STELLA (orquestradora, nao produtora)
- (-) Faltam campos extended: tldr, when_to_use, keywords, long_tails, axioms, linked_artifacts, density_score, data_source
- (-) Faltam secoes: Patterns, Anti-Patterns, References
- (-) Sem boundary explicito no body

### Gaps vs Blueprint KC (p06_bp_knowledge_card)

| Requisito BP | Presente? | Impacto |
|-------------|-----------|---------|
| 13 required fields | 8/13 (faltam: title, tldr, when_to_use, tags como lista, quality=null) | Recall prejudicado |
| 6 extended fields | 0/6 | ~30% menos recall no brain search |
| Body >= 4 secoes | 3/4 minimo | Incompleto |
| Boundary no body | Ausente | Confusao com boot_config |
| Patterns/Anti-Patterns | Ausentes | Sem guia de uso |
| References | Ausentes | Sem rastreabilidade |
| density_score >= 0.80 | Nao calculado | Sem validacao |

---

## Boundary: model_card

### O Que model_card EH

Especificacao tecnica de um LLM: provider, versao, pricing, context window, limites de output, features suportadas (tool use, extended thinking, vision). Funcao primaria: informar decisoes de roteamento e custo.

### O Que model_card NAO EH

| Confusao Comum | Por Que NAO EH | Tipo Correto |
|----------------|----------------|--------------|
| boot_config | boot_config INICIALIZA (temp, max_tokens, MCPs). model_card DESCREVE capacidades. | P02 boot_config |
| agent | agent eh identidade completa (memoria, tools, handoffs). model_card eh spec de infra. | P02 agent |
| persona | persona define tom/estilo de comunicacao. model_card eh tecnico, sem personalidade. | P02 persona |
| router | router mapeia task->satellite. model_card nao roteia, apenas informa. | P02 router |
| benchmark | benchmark avalia performance. model_card documenta specs declaradas pelo provider. | P07 benchmark |
| pricing (P01 KC) | KC de pricing seria conhecimento generico. model_card eh identity-bound (P02). | P01 knowledge_card |

### Regra de Disambiguacao

Se o artefato responde "o que este LLM PODE fazer e quanto CUSTA?" → model_card.
Se responde "como INICIALIZAR este LLM?" → boot_config.
Se responde "QUEM este LLM EH nesta sessao?" → agent/persona.

---

## Relacao com Outros Tipos P02

### Posicao no Boot Flow

```
[boot_config + model_card]   ← infra pre-requisito (camada 0)
          |
    [system_prompt]           ← papel persistente (camada 1)
          |
    [mental_model]            ← mapa cognitivo (camada 2)
          |
      [persona]               ← estilo comunicacao (camada 3)
          |
       [agent]                ← identidade completa (camada 4) ← BECOME completo
```

model_card esta na **camada 0** (infraestrutura). Eh carregado ANTES de qualquer identidade.

### Relacoes Diretas

| Tipo P02 | Relacao com model_card | Direcao |
|----------|----------------------|---------|
| boot_config | USA model_card para selecionar modelo | boot_config → model_card |
| agent | REFERENCIA model_card para limites | agent → model_card |
| router | CONSULTA model_card para custo/capacidade | router → model_card |
| fallback_chain | ORDENA model_cards por prioridade | fallback → model_card[] |
| mental_model | Indireta: limites do model_card constrangem decisoes | mental_model ←(implícito) model_card |
| persona | Nenhuma relacao direta | — |
| lens | Nenhuma relacao direta | — |
| iso_package | INCLUI model_card como dependencia de deploy | iso_package → model_card |
| axiom | Nenhuma relacao direta | — |

### Comparativo dos 9 Tipos P02

| Tipo | Core? | Max Bytes | Funcao Principal | Depende de model_card? |
|------|-------|-----------|------------------|----------------------|
| agent | sim | 5120 | Identidade completa | sim (referencia) |
| mental_model | sim | 2048 | Mapa cognitivo | nao |
| persona | nao | 2048 | Estilo comunicacao | nao |
| boot_config | nao | 2048 | Inicializacao | sim (selecao modelo) |
| **model_card** | **nao** | **2048** | **Spec LLM** | **—** |
| router | sim | 1024 | Roteamento task→sat | sim (custo/capacidade) |
| fallback_chain | nao | 512 | Fallback entre modelos | sim (lista priorizada) |
| iso_package | sim | 4096 | Bundle portable | sim (dependencia) |
| axiom | sim | 3072 | Principio imutavel | nao |

model_card eh **nao-core** mas **dependencia de 4 outros tipos**. Eh o unico tipo P02 puramente descritivo (sem aspecto prescritivo).

---

## Gaps vs Industria

### O Que Falta no Exemplo Atual

| Gap | Industria (Hugging Face, OpenAI, Google) | CEX Atual | Recomendacao |
|-----|------------------------------------------|-----------|--------------|
| Limites de rate | Docs de provider listam TPM, RPM, RPD | Ausente | Campo `rate_limits` no frontmatter |
| Modalidades | Vision, audio, code, embedding | Apenas "Extended Thinking" e "Tool Use" | Secao `## Capabilities` com lista completa |
| Deprecation/EOL | HF model cards tem lifecycle status | Ausente | Campo `status: active/deprecated/sunset` |
| Safety/alignment | Model cards de industria incluem safety evals | Ausente | Secao `## Safety` (opcional, se disponivel) |
| Benchmarks comparativos | HuggingFace Open LLM Leaderboard | Ausente | Secao `## Benchmarks` com scores publicos |
| Latency/throughput | Importante para decisao de roteamento | Ausente | Campos `latency_p50` e `throughput_tps` |
| Fine-tuning support | Relevante para customizacao | Ausente | Campo `fine_tunable: bool` |
| Data cutoff | Knowledge cutoff date | Ausente | Campo `knowledge_cutoff` |
| Versioning do provider | Pinned vs latest, snapshot dates | Parcial (model_name inclui date) | Campo `snapshot_date` explicito |

### Gaps Criticos (prioridade alta)

1. **rate_limits** — sem isto, router nao pode planejar throughput
2. **status/lifecycle** — modelos deprecam; sem campo, cards ficam stale
3. **knowledge_cutoff** — afeta decisao de uso para tarefas temporais
4. **capabilities list** — "tool use" e "extended thinking" nao cobrem vision/audio/code

### Gaps Opcionais (prioridade media)

5. **benchmarks** — util para comparacao, mas dados mudam rapido
6. **latency** — util para roteamento, mas varia por regiao/carga
7. **safety** — importante para compliance, mas dados nem sempre publicos

---

## Blueprint Structure Recomendada

### Frontmatter (19 campos)

```yaml
---
# IDENTITY (5) — obrigatorios
id: p02_mc_{{provider}}_{{model_slug}}  # ex: p02_mc_anthropic_opus_4
type: model_card
lp: P02
version: "{{semver}}"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{quem PRODUZIU}}"

# MODEL SPEC (8) — obrigatorios
model_name: "{{id oficial do provider}}"
provider: "{{anthropic|openai|google|meta|mistral}}"
context_window: {{int tokens}}
max_output: {{int tokens}}
pricing:
  input: {{float per 1M}}
  output: {{float per 1M}}
  cache_read: {{float or null}}
  cache_write: {{float or null}}
  unit: per_1M_tokens
status: "{{active|deprecated|sunset}}"
knowledge_cutoff: "{{YYYY-MM}}"
capabilities: [{{text, vision, audio, code, tool_use, extended_thinking, embedding, fine_tuning}}]

# SEARCH (6) — melhoram recall
domain: model_selection
quality: null  # NUNCA auto-atribuir
tags: [model-card, {{provider}}, {{model_family}}, pricing, capabilities]
tldr: "{{1 frase com dados: modelo, provider, preco, destaque}}"
when_to_use: "{{decisao de roteamento ou selecao de modelo}}"
linked_artifacts:
  primary: "{{boot_config que usa este card, ou null}}"
  related: ["{{outros model_cards do mesmo provider}}"]
---
```

### Body (6 secoes obrigatorias)

```markdown
## Boundary
model_card EH: spec tecnica de LLM (capacidades, custos, limites).
model_card NAO EH: boot_config (inicializacao), agent (identidade), benchmark (avaliacao).

## Specifications
| Spec | Value |
Tabela com: model, provider, context, max_output, pricing, features.

## Capabilities
| Capability | Support | Notes |
Tabela detalhada: text, vision, audio, code, tool_use, extended_thinking, embedding, fine_tuning.

## When to Use
| Scenario | Use This Model? | Alternative |
Tabela de decisao com alternativas explicitas e razao de custo.

## Rate Limits
| Tier | RPM | TPM | RPD |
Limites por tier (se disponivel publicamente).

## References
- source: {{provider docs URL}}
- related: {{outros model_cards}}
- boot_config: {{boot_config que referencia este card}}
```

### Secoes Opcionais

```markdown
## Benchmarks
| Benchmark | Score | Date |
Scores publicos (MMLU, HumanEval, etc). Marcar data — stale rapidamente.

## Safety
Alignment info do provider (se disponivel).

## CODEXA Mapping
Qual satellite usa este modelo e por que.
```

---

## Quality Gates Propostos

### Structural (automatizavel)

```yaml
structural:
  - id starts with "p02_mc_"
  - id == filename_stem
  - type == "model_card"
  - lp == "P02"
  - model_name is not empty
  - provider in [anthropic, openai, google, meta, mistral, cohere, deepseek]
  - context_window > 0 (integer)
  - max_output > 0 (integer)
  - pricing.input > 0 and pricing.output > 0
  - status in [active, deprecated, sunset]
  - capabilities is list, len >= 1
  - tags is list, not string
  - quality == null (never self-score)
  - body_bytes >= 300 and <= 2048
```

### Completeness (automatizavel)

```yaml
completeness:
  - 19 frontmatter fields present (null OK for optional)
  - body has >= 4 of 6 required sections
  - Specifications table has >= 5 rows
  - When to Use table has >= 3 scenarios
  - Boundary section present and non-empty
  - References has >= 1 source link
```

### Density (automatizavel)

```yaml
density:
  - sem filler: "This document", "In summary", "As mentioned"
  - sem frases duplicadas (jaccard > 0.8)
  - pricing tem numeros concretos (nao "varies" ou "contact sales")
  - context_window eh numero exato (nao "up to" ou "approximately")
  - density_score >= 0.85 (mais alto que KC generico por ser spec)
```

### Accuracy (manual/LLM-assisted)

```yaml
accuracy:
  - pricing matches provider's published pricing page
  - context_window matches provider docs
  - capabilities verified against API docs
  - knowledge_cutoff verified against provider announcement
  - status reflects current provider lifecycle
  - score = mean(structural, completeness, density, accuracy)
  - threshold: >= 8.0 for pool, >= 9.5 for golden
```

### Freshness Gate (novo para model_card)

```yaml
freshness:
  - updated date within 90 days (models change pricing/features)
  - if status == "deprecated": linked_artifacts must point to replacement
  - if provider announces new version: card should be updated within 7 days
  - stale cards (> 90 days without update) get flagged for review
```

---

## Sumario de Recomendacoes

| # | Recomendacao | Prioridade | Impacto |
|---|-------------|------------|---------|
| 1 | Adicionar boundary explicito no body de todo model_card | Alta | Elimina confusao com boot_config |
| 2 | Expandir frontmatter: status, knowledge_cutoff, capabilities, rate_limits | Alta | Decisoes de roteamento informadas |
| 3 | quality = null sempre (validacao externa) | Alta | Integridade do quality gate |
| 4 | author = quem PRODUZIU (nao quem roteou) | Alta | Rastreabilidade |
| 5 | Adicionar secoes Patterns + Anti-Patterns + References | Media | Completude |
| 6 | Freshness gate (90 dias) para detectar cards stale | Media | model_cards degradam mais rapido que KCs |
| 7 | Criar blueprint formal p06_bp_model_card.md seguindo estrutura acima | Alta | Padronizacao de producao |
| 8 | Refatorar exemplo existente para cumprir blueprint | Media | Exemplo de referencia |
