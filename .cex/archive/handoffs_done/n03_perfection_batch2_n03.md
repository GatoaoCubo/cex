# N03 Continuous Batch — Wave 2 (Templates P03-P04)
**Autonomia Total** | **Quality 9.0+ target** | **Batch: 2/5**

## REGRAS
1. Leia `.claude/rules/n03-8f-enforcement.md` PRIMEIRO
2. Para cada artefato: leia → analise por que score é baixo → enriqueça → salve
3. NÃO altere id/kind/pillar — apenas enriqueça body + adicione tags/tldr se faltam
4. Mantenha frontmatter válido. quality: null (NUNCA auto-score)
5. Cada template deve ter: seções ##, tabelas |, exemplos concretos, tldr no frontmatter

## ARTEFATOS (10 files — enriquecer body para densidade ≥0.80, ≤4096B)

1. `P03_prompt/templates/tpl_constraint_spec.md` — score 8.3
2. `P03_prompt/templates/tpl_instruction.md` — score 8.3
3. `P03_prompt/templates/tpl_prompt_version.md` — score 8.3
4. `P04_tools/templates/tpl_audio_tool.md` — score 8.3
5. `P04_tools/templates/tpl_browser_tool.md` — score 8.3
6. `P04_tools/templates/tpl_code_executor.md` — score 8.3
7. `P04_tools/templates/tpl_computer_use.md` — score 8.3
8. `P04_tools/templates/tpl_document_loader.md` — score 8.3
9. `P04_tools/templates/tpl_function_def.md` — score 8.3
10. `P04_tools/templates/tpl_hook.md` — score 8.3

## PADRÃO DE ENRIQUECIMENTO
- Adicionar `tldr:` e `tags:` no frontmatter se ausentes
- Expandir seções ## com conteúdo real (não placeholders)
- Adicionar pelo menos 1 tabela | ou 1 code block
- Garantir ≥5 seções ## no body
- Manter ≤4096B

## COMMIT
```bash
git add -A
git commit -m "[N03] batch2: enrich 10 templates P03-P04 (target 8.8+)"
```

## SIGNAL
```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'batch2_complete', 9.0)"
```
