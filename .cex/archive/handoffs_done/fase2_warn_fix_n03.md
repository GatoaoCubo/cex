# N03 Task: Fix 13 Oversized Builder ISOs — Doctor 0 WARN
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO

`python _tools/cex_doctor.py` reporta 12 WARN (13 arquivos) — ISOs de builders que excedem 4096B por 1-74 bytes. Precisamos de 98 PASS, 0 WARN, 0 FAIL antes de avançar para Fase 3 (rebuild dos 51 artefatos N01-N06).

**Critério**: cada arquivo DEVE ficar <= 4096 bytes SEM perder informação semântica. Comprima prosa, remova redundâncias, encurte exemplos — mas NUNCA delete campos do frontmatter ou seções inteiras que transmitam conhecimento único.

## ARQUIVOS (13 files, 12 builders)

| # | Arquivo | Atual | Excesso |
|---|---------|-------|---------|
| 1 | `archetypes/builders/action-prompt-builder/bld_examples_action_prompt.md` | 4102B | +6B |
| 2 | `archetypes/builders/action-prompt-builder/bld_memory_action_prompt.md` | 4104B | +8B |
| 3 | `archetypes/builders/agent-package-builder/bld_system_prompt_agent_package.md` | 4101B | +5B |
| 4 | `archetypes/builders/benchmark-builder/bld_memory_benchmark.md` | 4099B | +3B |
| 5 | `archetypes/builders/brain-index-builder/bld_examples_brain_index.md` | 4098B | +2B |
| 6 | `archetypes/builders/dag-builder/bld_memory_dag.md` | 4104B | +8B |
| 7 | `archetypes/builders/diagram-builder/bld_examples_diagram.md` | 4108B | +12B |
| 8 | `archetypes/builders/fallback-chain-builder/bld_memory_fallback_chain.md` | 4097B | +1B |
| 9 | `archetypes/builders/feature-flag-builder/bld_memory_feature_flag.md` | 4100B | +4B |
| 10 | `archetypes/builders/hook-builder/bld_quality_gate_hook.md` | 4101B | +5B |
| 11 | `archetypes/builders/mental-model-builder/bld_examples_mental_model.md` | 4098B | +2B |
| 12 | `archetypes/builders/pattern-builder/bld_examples_pattern.md` | 4100B | +4B |
| 13 | `archetypes/builders/router-builder/bld_examples_router.md` | 4170B | +74B |

## TÉCNICAS DE COMPRESSÃO (use nesta ordem)

1. **Trailing whitespace** — remover espaços/tabs no final de linhas
2. **Blank lines duplicadas** — colapsar 2+ blank lines em 1
3. **Prosa redundante** — "This is important because" → cortar, manter só o fato
4. **Abreviar exemplos** — encurtar strings de exemplo sem perder o padrão demonstrado
5. **Último recurso** — encurtar 1 linha de comentário ou descrição genérica

## SCOPE FENCE
- **SOMENTE**: `archetypes/builders/` (os 13 arquivos listados)
- **NÃO TOQUE**: `N0*_*/`, `P0*_*/`, `_tools/`, `_spawn/`, `boot/`, `.claude/`, `CLAUDE.md`

## VALIDAÇÃO
Após cada arquivo, verificar: `wc -c < arquivo` deve ser <= 4096.
Ao final, rodar: `python _tools/cex_doctor.py` — resultado esperado: **98 PASS | 0 WARN | 0 FAIL**

## COMMIT
```bash
git add archetypes/builders/
git commit -m "[N03] fix 13 oversized builder ISOs — doctor 0 WARN"
```

## SIGNAL
```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 9.0, 'fase2_warn_fix')"
```
