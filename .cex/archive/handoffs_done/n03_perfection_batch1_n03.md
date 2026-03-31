# N03 Continuous Batch — Wave 1 (Templates P01-P02)
**Autonomia Total** | **Quality 9.0+ target** | **Batch: 1/5**

## REGRAS
1. Leia `.claude/rules/n03-8f-enforcement.md` PRIMEIRO
2. Para cada artefato: leia → analise por que score é baixo → enriqueça → salve
3. NÃO altere id/kind/pillar — apenas enriqueça body + adicione tags/tldr se faltam
4. Mantenha frontmatter válido. quality: null (NUNCA auto-score)
5. Cada template deve ter: seções ##, tabelas |, exemplos concretos, tldr no frontmatter

## ARTEFATOS (10 files — enriquecer body para densidade ≥0.80, ≤4096B)

1. `P01_knowledge/templates/tpl_chunk_strategy.md` — score 8.3
2. `P01_knowledge/templates/tpl_glossary_entry.md` — score 8.3
3. `P01_knowledge/templates/tpl_rag_source.md` — score 8.3
4. `P01_knowledge/templates/tpl_retriever_config.md` — score 8.3
5. `P02_model/templates/tpl_axiom.md` — score 8.3
6. `P02_model/templates/tpl_fallback_chain.md` — score 8.3
7. `P02_model/templates/tpl_handoff_protocol.md` — score 8.3
8. `P02_model/templates/tpl_memory_scope.md` — score 8.3
9. `P02_model/templates/tpl_router.md` — score 8.3
10. `P01_knowledge/examples/ex_glossary_entry_director.md` — score 8.2

## PADRÃO DE ENRIQUECIMENTO
Para cada template/exemplo:
- Adicionar `tldr:` e `tags:` no frontmatter se ausentes
- Expandir seções ## com conteúdo real (não placeholders)
- Adicionar pelo menos 1 tabela | ou 1 code block
- Garantir ≥5 seções ## no body
- Manter ≤4096B (templates) ou ≤5120B (examples)

## COMMIT
```bash
git add -A
git commit -m "[N03] batch1: enrich 10 templates P01-P02 (target 8.8+)"
```

## SIGNAL
```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'batch1_complete', 9.0)"
```
