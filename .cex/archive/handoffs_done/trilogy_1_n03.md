# N03 Task — Trilogy Spec 1: Schema Evolution
**Autonomia Total** | **Quality 9.0+** | **SEQUENCIA: 1 de 3**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## TAREFA
Leia `.cex/runtime/handoffs/mission_schema_evolution.md` por COMPLETO.
Execute Phase 1 (Schema Definitions), Phase 2 (Hydrate 104 Builders), Phase 3 (Validate + Reindex) em sequência.

### Resumo das 3 Phases:
1. **Phase 1** (1.5h): Evoluir 4 meta-templates (_builder-builder/bld_meta_*) com 8 patterns universais (keywords, triggers, geo_description, memory_scope, observation_types, effort, hooks, permissions)
2. **Phase 2** (3-4h): Criar `_tools/cex_schema_hydrate.py`, executar --dry-run, depois --apply em 104 builders. Atualizar bld_norms.md com 11 regras novas.
3. **Phase 3** (1h): Criar `_tools/tests/test_schema_evolution.py` (15 tests), rebuild index, update README.

### Critérios de Aceite:
- 103 manifests com keywords + triggers + geo_description
- 104 memories com memory_scope + observation_types
- 103 configs com effort + max_turns + disallowed_tools + hooks + permission_scope
- 103 tools com ## Tool Permissions
- 15 builders com non-default overrides
- 15/15 tests passam
- Zero regressão

## COMMITS (1 por phase)
```
git add -A && git commit -m "[N03] schema-evo-phase1: evolve 4 meta-templates with 8 universal patterns"
git add -A && git commit -m "[N03] schema-evo-phase2: hydrate 104 builders + norms update"
git add -A && git commit -m "[N03] schema-evo-phase3: validation tests + reindex"
```

## SIGNAL AO FINAL
```python
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'trilogy_spec1_schema_complete', 9.0)"
```
