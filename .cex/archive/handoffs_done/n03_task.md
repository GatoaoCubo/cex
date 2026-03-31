# N03 Task — Post-Trilogy Consolidation: KCs + Query Tool + Autodiscovery Wiring
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## TAREFA (3 phases sequenciais)

### Phase 1: Create 7 Missing Knowledge Cards (45min)
Usar 8F pipeline para criar KCs para kinds que existem mas não têm KC:

1. `P01_knowledge/library/kind/kc_content_monetization.md`
2. `P01_knowledge/library/kind/kc_effort_profile.md`
3. `P01_knowledge/library/kind/kc_hook_config.md`
4. `P01_knowledge/library/kind/kc_research_pipeline.md`
5. `P01_knowledge/library/kind/kc_social_publisher.md`
6. `P01_knowledge/library/kind/kc_software_project.md`
7. `P01_knowledge/library/kind/kc_supabase_data_layer.md`

Padrão: copiar estrutura de kc_agent.md (frontmatter + boundary + purpose + schema + examples).
Cada KC: ~2-3KB, quality >= 8.0.

Commit: `[N03] kc: create 7 missing knowledge cards`

### Phase 2: Create cex_query.py — Discovery Query Tool (45min)
**Novo**: `_tools/cex_query.py`

O sistema tem 105 manifests com keywords_json no index.db mas NENHUM query tool.
Criar cex_query.py que:

1. Recebe query natural language (e.g. "monetizar curso hotmart")
2. Busca no index.db: keywords_json match + domain match + kind match
3. Usa TF-IDF simples ou fuzzy match (sem dependências externas pesadas)
4. Retorna top-5 builders com score de relevância
5. Para cada resultado: builder_id, kind, pillar, score, keywords matched
6. Flag --intent: integra com OBJECT_TO_KINDS do Motor 8F para fallback

Interface:
```
python _tools/cex_query.py "criar agente de vendas"
python _tools/cex_query.py "monetizar curso" --top 3
python _tools/cex_query.py "webhook hotmart" --json
python _tools/cex_query.py --rebuild-cache  # rebuild keyword index from manifests
```

Algoritmo:
1. Tokenizar query -> stems
2. Buscar keywords_json com match parcial
3. Buscar domain com match parcial
4. Score = keyword_matches * 0.6 + domain_match * 0.3 + kind_match * 0.1
5. Sort DESC, return top-k

BÔNUS: --suggest-crew flag que retorna crew recomendada do bld_collaboration

Commit: `[N03] tool: create cex_query.py (builder discovery by keyword/intent)`

### Phase 3: Wire Autodiscovery into Motor 8F (30min)
Tracks restantes do mission_builder_autodiscovery.md:

**A2 — Enhance Indexer**: Atualizar `_tools/cex_index.py` para:
- Extrair keywords do frontmatter dos bld_manifest (se não está fazendo)
- Popular keywords_json para os 6 manifests que faltam (105/111)
- Rebuild automático ao compilar

**A4 — Integration Motor 8F**: Atualizar `_tools/cex_8f_motor.py`:
- Na função classify_intent: se OBJECT_TO_KINDS não acha match, chamar cex_query.py como fallback
- Importar query function: `from cex_query import query_builders`
- Resultado do query enriquece o execution plan

**C1 — Smoke Tests**: Criar `_tools/tests/test_autodiscovery.py` (5 tests):
1. cex_query retorna resultados para "criar agente"
2. cex_query retorna content-monetization-builder para "monetizar hotmart"
3. Motor 8F com intent desconhecido usa fallback query
4. Index tem keywords para >= 100 manifests
5. Rebuild-cache funciona sem erros

Commit: `[N03] wire: autodiscovery A2+A4+C1 — indexer + motor fallback + tests`

## COMMITS
```
git add -A && git commit -m "[N03] kc: create 7 missing knowledge cards"
git add -A && git commit -m "[N03] tool: create cex_query.py (builder discovery by keyword/intent)"
git add -A && git commit -m "[N03] wire: autodiscovery A2+A4+C1 — indexer + motor fallback + tests"
```

## SIGNAL
```python
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'post_trilogy_consolidation_complete', 9.0)"
```
