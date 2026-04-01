# N01 Task — Validate Intelligence Nucleus (continuation)
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO
N01 Intelligence Nucleus já tem 20 artefatos construídos. O spawn anterior (gemini) estourou tokens antes de validar e sinalizar.

## TAREFA
1. Revise todos os artefatos em N01_intelligence/ (exceto compiled/)
2. Verifique que TODOS têm frontmatter válido com quality score (não null)
3. Se algum tem quality:null, score com cex_score.py
4. Compile: `python _tools/cex_compile.py --all`
5. Verifique 0 erros de compilação
6. Se algum artefato está abaixo do padrão (genérico demais), melhore
7. Commit qualquer mudança

## SIGNAL
```python
python -c "from _tools.signal_writer import write_signal; write_signal('n01', 'fase3_n01_validated', 9.0)"
```
