# KC Library Architecture -- Execution Plan

**Version**: 1.0.0 | **Date**: 2026-03-29
**Status**: PLAN (nao executado)
**Prereq**: 98 kinds completos (DONE)

---

## O QUE EH

KC Library eh a biblioteca viva de conhecimento destilado do CEX.
Nao eh um pillar novo. Eh o MECANISMO que conecta os pilares num ciclo.

O ciclo:
- PESQUISAR: copiar o que ja existe (fontes, repos, docs, concorrentes)
- DESTILAR: processar pesquisa bruta em KCs estruturados
- CONSTRUIR: usar KCs como ingredientes pra preencher kinds
- VALIDAR: test, review, fix

Cada volta do ciclo CRESCE a library. Cada KC futuro eh consultavel via:
- RAG (busca semantica durante geracao)
- FT (fine-tuning com KCs acumulados)
- 8F Inject (funcao F3 consulta library durante pipeline)

---

## O QUE JA EXISTE (prototipo que rodou sem formalizar)

| Artefato | Onde | O que eh |
|----------|------|----------|
| 73 KCs examples | P01_knowledge/examples/ex_knowledge_card_*.md | KCs reais com frontmatter rico |
| KC template | P01_knowledge/templates/tpl_knowledge_card.md | Schema com 20+ campos |
| KC schema | P01_knowledge/_schema.yaml kinds.knowledge_card | density>=0.8, quality>=7.0 |
| distill.py | _tools/distill.py | Raw input para KC template-compliant |
| 3 source docs | _docs/sources/*.md | Pesquisa bruta (73KB) |
| 11 ecosystem maps | _docs/ecosystem/P*_ECOSYSTEM_MAP.md | Pesquisa por pilar |
| 8F Motor F3 INJECT | _tools/cex_8f_motor.py | Funcao que injeta conhecimento |
| bld_knowledge_card | 98x builders/*/bld_knowledge_card_*.md | KC do KIND (definicao) |

---

## 3 TIPOS DE KC

| Tipo | Descricao | Origem | Exemplo |
|------|-----------|--------|---------|
| KC-Source | Pesquisa bruta estruturada | Scraping, docs, papers | FRAMEWORK_TAXONOMY.md |
| KC-Domain | Conhecimento destilado | distill.py sobre KC-Source | kc_rag_fundamentals.md |
| KC-Kind | Definicao + boundary de um kind | Builder generation | bld_knowledge_card_chunk_strategy.md |

---

## ONDE VIVEM

    P01_knowledge/
      library/                      NOVO: KC Library raiz
        sources/                    KC-Source (pesquisa bruta)
          src_framework_taxonomy.md
          src_provider_taxonomy.md
          src_standards_global.md
        domain/                     KC-Domain (destilado)
          kc_rag_fundamentals.md
          kc_chunking_strategies.md
          ... (cresce com uso)
        index.yaml                  Indice consultavel
      examples/                     Examples (como hoje)
      templates/
      _schema.yaml

---

## KC-Domain Frontmatter (campos NOVO marcados)

    id: kc_chunking_strategies
    kind: knowledge_card
    type: domain                    NOVO: source | domain | kind
    pillar: P01
    title: Chunking Strategies for RAG Systems
    origin: src_framework_taxonomy  NOVO: de qual KC-Source veio
    feeds_kinds: [chunk_strategy, retriever_config]  NOVO: chave do wiring
    density_score: 0.88

Campo feeds_kinds eh a CHAVE: diz quais kinds esse KC alimenta.
8F Motor usa isso pra injetar KC certo no kind certo.

Fluxo:
  Intent -> Motor classifica kind=chunk_strategy
  -> Busca KCs onde feeds_kinds contem chunk_strategy
  -> F3 INJECT: injeta KCs no contexto
  -> F6 PRODUCE: gera com conhecimento real

---

## FERRAMENTAS

### 1. cex_research.py (NOVO ~200 loc) -- Fase PESQUISAR
Input: tema + fontes. Output: KC-Source em library/sources/. Dry-run default.

### 2. distill.py (EVOLUIR ~150 loc) -- Fase DESTILAR
Ja existe. Adicionar: --source, --feeds, auto-tag type+origin, auto-update index.yaml

### 3. cex_8f_motor.py (EVOLUIR ~50 loc) -- Fase CONSTRUIR
fan_out() consulta library/index.yaml, filtra feeds_kinds, injeta no INJECT.
Fallback: bld_knowledge_card se library vazia.

### 4. cex_doctor.py (EVOLUIR ~30 loc) -- Fase VALIDAR
Check feeds_kinds, origin, report KC coverage %.

### 5. library/index.yaml (auto-gerado)
Sources + domains + coverage map per kind.

---

## PLANO DE EXECUCAO (5 waves, ~2h total)

### Wave 1: Estrutura + Migrate (orchestrator direto, ~15 min)
- 1.1 Criar P01_knowledge/library/ com dirs sources/ e domain/
- 1.2 Mover _docs/sources/*.md para library/sources/ (prefixo src_)
- 1.3 Criar library/index.yaml seed com 3 sources
- 1.4 Adicionar campo type (source/domain/kind) ao KC schema
- 1.5 Commit: feat KC Library structure

### Wave 2: Distill Sources para Domain KCs (3 builder_agent, ~30 min)
- 2.1 Destilar FRAMEWORK_TAXONOMY para 5-8 KC-Domains
- 2.2 Destilar PROVIDER_TAXONOMY para 5-6 KC-Domains
- 2.3 Destilar STANDARDS_GLOBAL para 4-5 KC-Domains
- 2.4 Cada KC-Domain inclui feeds_kinds
- 2.5 Auto-update library/index.yaml

### Wave 3: Wire 8F Motor (1 builder_agent, ~20 min)
- 3.1 fan_out() consulta library/index.yaml
- 3.2 KC lookup: dado kind, buscar KCs com feeds_kinds match
- 3.3 Injetar KCs no plano INJECT como contexto
- 3.4 Fallback pra bld_knowledge_card se library vazia
- 3.5 Test: gerar chunk_strategy COM vs SEM library

### Wave 4: Evolve Tools + Doctor (1 builder_agent, ~15 min)
- 4.1 Criar cex_research.py
- 4.2 Evoluir distill.py (--source, --feeds, auto-index)
- 4.3 Evoluir cex_doctor.py (KC coverage check)
- 4.4 Test: ciclo completo dry-run

### Wave 5: Proof -- Full Cycle (1 builder_agent, ~20 min)
- 5.1 Escolher 1 kind sem KC coverage (ex: reward_signal)
- 5.2 cex_research.py: pesquisar RLHF/DPO/reward modeling
- 5.3 distill.py: destilar em KC-Domain com feeds_kinds
- 5.4 cex_8f_motor.py: gerar reward_signal COM KC injection
- 5.5 Comparar output COM vs SEM KC: medir delta qualidade
- 5.6 cex_doctor.py: validar tudo

---

## METRICAS DE SUCESSO

| Metrica | Antes | Depois |
|---------|-------|--------|
| KC-Sources | 0 formais | 3+ (73KB+) |
| KC-Domains | 73 (examples soltos) | ~90+ (library indexada) |
| Kinds com KC coverage | 0 mapeados | 50+ via feeds_kinds |
| 8F Motor KC injection | nenhum | automatico via index |
| Doctor KC coverage | nenhum | % reportado |

---

## NOTAS

1. bld_knowledge_card nos builders NAO muda. KC-Domain na library eh complementar.
2. Os 73 KC examples existentes SAO KC-Domains. Falta feeds_kinds + organizar.
3. KC-Source = input rastreavel. KC-Domain = asset permanente.
4. Ciclo mapeia pros nuclei organization: 01(pesquisa) > KC > 03(constroi) > 04(indexa).
5. FT futuro: KCs > 500 = treinar modelo especialista CEX (JSONL from frontmatter+body).

## DEPENDENCIAS: PyYAML (ja instalado). Zero deps novas.
## ETA TOTAL: ~2h com grid (5 waves)