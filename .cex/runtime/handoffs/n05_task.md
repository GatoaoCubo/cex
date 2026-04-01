# N05 Task — PSPEC Railway Backend Superintendent: Rewrite Identity + Quality
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO
N05 evolui de DevOps genérico para **Railway Backend Superintendent**.
Leia a spec completa: `_docs/pspecs/PSPEC_N05_RAILWAY_SUPERINTENDENT.md`

## 10 KCs JÁ CRIADOS EM
`P01_knowledge/library/infrastructure/` — railway-platform, railway-cli, postgresql-railway, nixpacks, zero-downtime, health-monitoring, uvicorn, networking, middleware-stack, credit-system

## TAREFA — Rewrite 9 existentes + Create 5 novos = 14 artefatos

### Identidade (rewrite com Railway superintendent):
1. `agents/agent_operations.md` — Railway Superintendent, 12 capabilities do F2, opus model
2. `prompts/system_prompt_operations.md` — Persona Railway-native, deploy-first
3. `architecture/agent_card_operations.md` — Deploy spec com postgres MCP, opus model

### Quality (rewrite com 6 gates de deploy):
4. `feedback/quality_gate_operations.md` — deploy smoke 30s, rollback 4svcs, migration safe, env 63vars, health full, middleware intact
5. `orchestration/dispatch_rule_operations.md` — Triggers: deploy/railway/api/health/rollback/migrate/env/infrastructure
6. `orchestration/workflow_operations.md` — Deploy workflow: verify-toml→verify-env→migrations→railway-up→health-30s→verify→monitor
7. `orchestration/spawn_config_operations.md` — Spawn config para opus + postgres MCP

### Knowledge (rewrite):
8. `knowledge/knowledge_card_operations.md` — Rewrite com refs aos 10 infra KCs
9. `memory/checkpoint_operations.md` — Deploy checkpoint state

### CREATE novos:
10. `schemas/railway_toml_schema.md` — Schema para railway.toml validation
11. `schemas/health_check_schema.md` — Schema para HealthResponse
12. `schemas/env_contract_schema.md` — Schema para env var contract (63 vars)
13. `output/deploy_checklist_template.md` — Deploy checklist output
14. `output/rollback_plan_template.md` — Rollback plan output

## REFERÊNCIAS
- PSPEC: `_docs/pspecs/PSPEC_N05_RAILWAY_SUPERINTENDENT.md`
- Golden agent: `N03_engineering/agents/agent_engineering.md`
- KCs: `P01_knowledge/library/infrastructure/kc_*.md`

## COMMIT
```bash
git add -A && git commit -m "[N05] pspec: Railway Backend Superintendent — 14 artifacts"
```

## SIGNAL
```python
python -c "from _tools.signal_writer import write_signal; write_signal('n05', 'pspec_n05_complete', 9.0)"
```
