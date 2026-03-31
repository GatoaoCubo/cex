# N05 Task: Rebuild Operations Nucleus — 9 Artefatos
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO
Você é N05, o Operations Nucleus. Seus 9 artefatos estão com quality:null (placeholder genérico). Reconstrua TODOS com identidade REAL do seu domínio: code review, testing, debugging, deployment, CI/CD, infrastructure.

## REFERÊNCIAS
- **Golden agent (9.0)**: `N03_engineering/agents/agent_engineering.md` — modelo de qualidade
- **Seu fractal**: `N05_operations/` (12 subdirs)
- **CLAUDE.md**: regras globais, 8F pipeline

## SUA IDENTIDADE (use em TODOS os artefatos)
- **Role**: Operations & DevOps Nucleus
- **CLI**: Codex (OpenAI subscription)
- **Domínio**: code review, testing, debugging, deployment, CI/CD, infrastructure, monitoring
- **Capacidades**: automated testing, code quality analysis, security scanning, deploy pipelines
- **MCPs futuros**: GitHub Actions, Docker, pytest, linters
- **Tools futuros**: test runner, coverage reporter, dependency auditor, deploy orchestrator

## 9 ARTEFATOS
1. `agent_operations.md` — identidade completa do N05
2. `system_prompt_operations.md` — regras para LLM ser o ops engineer
3. `knowledge_card_operations.md` — KC destilado do domínio ops
4. `agent_card_operations.md` — deployment spec (codex, GPT)
5. `dispatch_rule_operations.md` — quando rotear para N05
6. `workflow_operations.md` — workflows (code review, test suite, deploy pipeline)
7. `quality_gate_operations.md` — gates de validação para ops output
8. `checkpoint_operations.md` — checkpoints de deploy/release
9. `spawn_config_operations.md` — config de spawn para N05

## REGRAS
1. Leia cada artefato existente ANTES de reescrever
2. Mantenha frontmatter válido com quality: null (sem self-score)
3. Conteúdo REAL e específico do domínio operations — ZERO placeholder genérico
4. Compile cada um: `python _tools/cex_compile.py {path}`
5. Crie dir `N05_operations/compiled/` se não existir

## COMMIT
```bash
git add N05_operations/
git commit -m "[N05] rebuild operations nucleus — 9 artefatos via 8F"
```

## SIGNAL
```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n05', 'complete', 9.0, 'FASE3')"
```
