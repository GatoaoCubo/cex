---
id: p01_ctx_codexa_boot_chain
type: context_doc
domain: architecture
scope: boot_initialization
---

# CODEXA Boot Chain

Sequencia deterministica de 8 camadas que inicializa qualquer sessao CODEXA, de variavel de ambiente ate execucao de tarefa.

## Boot Layers

```
LAYER 0: ENVIRONMENT
  .env (API keys) + CODEXA_SATELLITE env var
       |
LAYER 1: BOOT SCRIPT (boot/{satellite}.cmd)
  set CLAUDECODE= | set CODEXA_SATELLITE= | claude launch
       |
LAYER 2: CLAUDE.MD (auto-loaded)
  "Check CODEXA_SATELLITE -> read PRIME_{SAT}.md"
       |
LAYER 3: RULES (.claude/rules/, 10 files auto-loaded)
  navigation, encoding, multi_repo, boot-autonomy-flags,
  STELLA_RULES, satellite-execution, agents-context,
  satellites-context, codexa-learning
       |
LAYER 4: PRIME_{SAT}.md (satellite identity + capabilities)
       |
LAYER 5: MENTAL_MODEL.yaml (deep identity + execution history)
       |
LAYER 6: HANDOFF (dispatch queue)
  .claude/handoffs/{satellite}_*.md
       |
LAYER 7: EXECUTION
  Agent loaded -> Skill applied -> Sub-agents spawned -> Output validated
```

## Key Properties

- **Deterministic**: same env = same boot state
- **Fractal**: each layer references the next
- **Identity-first**: satellite knows WHO it is before WHAT to do
- **Fail-safe**: missing layer = graceful fallback (general session)

## Critical Details

| Layer | Token Cost | Mandatory |
|-------|-----------|-----------|
| L0 env | 0 | yes |
| L1 boot script | 0 | yes (satellites) |
| L2 CLAUDE.md | ~2K | yes |
| L3 rules | ~8K | yes (auto-loaded) |
| L4 PRIME | ~3K | yes (satellites) |
| L5 mental_model | ~2K | recommended |
| L6 handoff | ~1K | if dispatched |
| L7 execution | variable | yes |

Source: `records/framework/docs/META_BOOTSTRAP.md`
