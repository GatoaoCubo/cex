# N03 Continuous Batch — Wave 3 (Remaining Templates + Examples)
**Autonomia Total** | **Quality 9.0+ target** | **Batch: 3/5**

## REGRAS
1. Leia `.claude/rules/n03-8f-enforcement.md` PRIMEIRO
2. Para cada artefato: leia → analise por que score é baixo → enriqueça → salve
3. NÃO altere id/kind/pillar — apenas enriqueça body + adicione tags/tldr se faltam
4. Mantenha frontmatter válido. quality: null (NUNCA auto-score)

## ARTEFATOS (10 files)

1. `P04_tools/templates/tpl_notifier.md` — score 8.3
2. `P04_tools/templates/tpl_retriever.md` — score 8.3
3. `P05_output/templates/tpl_response_format.md` — score 8.2
4. `P10_memory/templates/tpl_runtime_state.md` — score 8.2
5. `P01_knowledge/examples/ex_context_session_memory.md` — score 8.3
6. `P01_knowledge/examples/ex_embedding_config_nomic_embed_text.md` — score 8.3
7. `P01_knowledge/examples/ex_knowledge_card_prompt_caching.md` — score 8.3
8. `P02_model/examples/ex_mental_model_pipeline.md` — score 8.3
9. `P03_prompt/examples/ex_chain_research_pipeline.md` — score 8.3
10. `P03_prompt/examples/ex_prompt_template_aida.md` — score 8.3

## PADRÃO DE ENRIQUECIMENTO
- Adicionar `tldr:` e `tags:` no frontmatter se ausentes
- Expandir seções ## com conteúdo denso (não stubs)
- Adicionar tabelas |, code blocks, listas concretas
- Templates: ≤4096B | Examples: ≤5120B
- Densidade ≥0.80

## COMMIT
```bash
git add -A
git commit -m "[N03] batch3: enrich 10 templates+examples (target 8.8+)"
```

## SIGNAL
```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'batch3_complete', 9.0)"
```
