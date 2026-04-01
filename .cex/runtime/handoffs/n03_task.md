# N03 Task
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## TAREFA
Leia .cex/runtime/handoffs/monetization_phase3_n03.md. Builder ISOs enrichment para content-monetization-builder. Depois leia .cex/runtime/handoffs/monetization_phase4_n06.md e crie os nucleus artifacts em N06_commercial. Commit cada fase. Signal ao final.

## COMMIT
git add -A
git commit -m "[N03] task complete"

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 9.0)"
