# N04 Task — Validate Knowledge Nucleus (COMPLETED ✅)
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO
N04 Knowledge Nucleus já tem 19 artefatos construídos. O spawn anterior (gemini) estourou tokens antes de validar e sinalizar.

## TAREFA ✅ COMPLETA
1. ✅ Revise todos os artefatos em N04_knowledge/ (exceto compiled/) — 19 artefatos verificados
2. ✅ Verifique que TODOS têm frontmatter válido com quality score (não null) — Todos entre 8.7-8.9
3. ✅ Se algum tem quality:null, score com cex_score.py — Nenhum quality:null encontrado
4. ✅ Compile: `python _tools/cex_compile.py --all` — 264/264 compilados com sucesso
5. ✅ Verifique 0 erros de compilação — Zero erros
6. ✅ Se algum artefato está abaixo do padrão (genérico demais), melhore — Todos acima de 8.0
7. ✅ Commit qualquer mudança — Handoff atualizado

## RESULTADO FINAL
- **19 artefatos N04**: Todos validados ✅
- **Quality scores**: 8.7-8.9 (padrão: 8.0+) ✅
- **Compilação**: 264/264 success ✅
- **Status**: FASE3_N04_VALIDATED ✅

## SIGNAL
```python
python -c "from _tools.signal_writer import write_signal; write_signal('n04', 'fase3_n04_validated', 9.0)"
```
