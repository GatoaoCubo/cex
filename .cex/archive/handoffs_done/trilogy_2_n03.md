# N03 Task — Trilogy Spec 2: Runtime Evolution
**Autonomia Total** | **Quality 9.0+** | **SEQUENCIA: 2 de 3**
**REGRA: Commit e signal ANTES de qualquer pausa.**
**PRE-REQUISITO**: Spec 1 (Schema Evolution) COMPLETO. Campos universais JA existem nos 104 builders.

## TAREFA
Leia `.cex/runtime/handoffs/mission_runtime_evolution.md` por COMPLETO.
Execute Phase 1 (LLM Memory), Phase 2 (Hooks+Effort+Permissions), Phase 3 (Fork+Update+Tests) em sequência.

### Resumo das 3 Phases:
1. **Phase 1** (3h): Memory Scanner em cex_memory.py + NOVO cex_memory_select.py (LLM-powered) + integrar no Motor 8F e Crew Runner
2. **Phase 2** (3h): Effort→model mapping + tool deny-list enforcement + 4 hook lifecycle types + permission scope enforcement
3. **Phase 3** (2-3h): Fork execution context + cex_memory_update.py (dynamic) + max_turns enforcement + 10 smoke tests

### Critérios de Aceite:
- Memory scanner retorna headers corretos
- LLM selector retorna top-5 (fallback keyword)
- Effort maps: low→haiku, medium→sonnet, high→opus
- Tool deny-list bloqueia com erro explícito
- Hooks pre_build/post_build executam
- Permission scope enforced
- Fork execution produz output
- Memory update: append + decay + prune
- 10/10 tests passam

## COMMITS (1 por phase)
```
git add -A && git commit -m "[N03] runtime-evo-phase1: LLM-powered memory retrieval"
git add -A && git commit -m "[N03] runtime-evo-phase2: effort + deny-list + hooks + permissions"
git add -A && git commit -m "[N03] runtime-evo-phase3: fork + memory update + max turns + tests"
```

## SIGNAL AO FINAL
```python
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'trilogy_spec2_runtime_complete', 9.0)"
```
