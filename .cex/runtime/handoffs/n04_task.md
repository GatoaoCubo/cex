# N04 Task
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## TAREFA
FASE3 N04 rebuild continuation. Your partial work (19 files) was committed. Check N04_knowledge/ for what exists. Complete any REMAINING artefatos from FASE3_n04 handoff. The handoff at .cex/runtime/handoffs/FASE3_n04.md lists 12 artefatos total. Validate, compile, signal complete.

## COMMIT
git add -A
git commit -m "[N04] task complete"

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('n04', 'complete', 9.0)"
