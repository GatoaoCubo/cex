# N03 Builder Task
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## TAREFA
Leia _ops/handoffs/_active/bootstrap_f1_n03.md PRIMEIRO. Execute todas as 10 tarefas listadas. 8F obrigatorio para cada artefato. Quality 9.0+. Compile cada um apos salvar. Commit incremental. Signal ao final.

## COMMIT
git add -A
git commit -m "[N03] task complete"

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 9.0)"
