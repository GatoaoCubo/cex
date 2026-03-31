# N03 Task — Trilogy Spec 3: Validation Registry
**Autonomia Total** | **Quality 9.0+** | **SEQUENCIA: 3 de 3**
**REGRA: Commit e signal ANTES de qualquer pausa.**
**PRE-REQUISITO**: Spec 1 (Schema) + Spec 2 (Runtime) COMPLETOS.

## TAREFA
Leia `.cex/runtime/handoffs/mission_validation_registry.md` por COMPLETO.
Execute Phase 1 (Kind Registration + Builders), Phase 2 (E2E Tests + Recompile + Integrity) em sequência.

### Resumo das 2 Phases:
1. **Phase 1** (2.5h): Registrar 3 novos kinds (memory_scope, effort_profile, hook_config) em TAXONOMY_LAYERS.yaml + criar 3 skeleton builders (13 ISOs cada) + atualizar cex_kind_register.py
2. **Phase 2** (2h): 10 E2E smoke tests (test_e2e_evolution.py) + recompile --all + rebuild index + integrity report

### Critérios de Aceite:
- 3 kinds em TAXONOMY_LAYERS.yaml
- 3 skeleton builders com 13 files cada (<30KB)
- kind_register.py atualizado
- 10/10 E2E tests passam
- Compile sem erros
- Index rebuilt
- Integrity report green
- Zero regressão
- Total: 107 builders, 102 kinds, 8 universal patterns

## COMMITS (1 por phase)
```
git add -A && git commit -m "[N03] validation-phase1: 3 new kinds + 3 skeleton builders"
git add -A && git commit -m "[N03] validation-phase2: E2E tests + recompile + integrity report"
```

## SIGNAL AO FINAL
```python
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'trilogy_spec3_validation_complete', 9.0)"
```
