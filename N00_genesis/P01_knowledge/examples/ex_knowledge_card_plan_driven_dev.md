---
id: p01_kc_plan_driven_dev
kind: knowledge_card
pillar: P01
title: "Plan-Driven Development — Plans as Executable Prompts for Sub-Agents"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: engineering_process
quality: 9.1
tags: [plan-driven, subagent, task-granularity, tdd, execution-plan]
tldr: "Plans are prompts: 2-5 min tasks with exact paths, verification steps, and TDD — directly executable by sub-agents without human interpretation"
when_to_use: "Decomposing features into sub-agent-executable tasks or reviewing plan quality before dispatch"
keywords: [plan-driven-development, subagent-execution, task-decomposition, implementation-plan]
long_tails:
  - "How to write implementation plans that sub-agents can execute autonomously"
  - "What granularity should tasks have for LLM sub-agent execution"
axioms:
  - "SEMPRE escrever verificacao explicita para cada task"
  - "NUNCA criar tasks maiores que 5 minutos de execucao"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_function_become, p01_kc_cex_function_reason]
density_score: null
data_source: "https://martinfowler.com/bliki/TestDrivenDevelopment.html"
---

## Summary

Plan-driven development trata planos como prompts executaveis, nao documentos de design.
Cada task de 2-5 minutos contem caminhos exatos, codigo completo, steps de verificacao e dependencias explicitas.
Ciclo completo: brainstorm → write-plan → execute-plan → verify.
Audiencia-alvo: "junior engineer sem contexto e sem julgamento" — se o plano nao for claro para este perfil, nao esta pronto.
Dois modos de execucao: subagent-driven (paralelo, sem intervencao humana) e sequential (fallback com checkpoints humanos).

## Spec

| Aspecto | Valor | Motivo |
|---------|-------|--------|
| Granularidade | 2-5 min por task | Tasks maiores causam desvio |
| Campos por task | paths, codigo, verificacao, deps | Sub-agente nao infere contexto |
| Audiencia | Junior sem contexto | Forca clareza maxima |
| TDD | Obrigatorio | Testes primeiro, sempre |
| Status contract | DONE, CONCERNS, BLOCKED, NEEDS_CTX | Protocolo pos-task padrao |
| Modo paralelo | 1 sub-agente por task | Rapido para tasks independentes |
| Modo sequential | Fallback sem sub-agentes | Checkpoints humanos por batch |
| Plano output | plans/YYYY-MM-DD-topic.md | Rastreavel por data e topico |
| Review pre-exec | Obrigatorio | Granularidade + deps + verificacoes |

Principios de design: TDD obrigatorio, YAGNI ruthlessly, DRY no design, isolation para paralelismo. Plano deve ser revisado criticamente antes de executar — tasks com granularidade correta, dependencias claras, verificacoes testaveis, e caminhos de arquivo existentes ou com task de criacao.

## Patterns

| Trigger | Action |
|---------|--------|
| Feature aprovada | Brainstorm → design doc → plano executavel |
| Task envolve codigo | Escrever teste RED antes de implementar |
| Tasks sem dependencia mutua | Despachar em paralelo via sub-agentes |
| Plano pronto | Revisar: granularidade, deps, verificacoes |
| Sub-agente reporta BLOCKED | Parar cadeia, resolver dependencia externa |
| Contexto insuficiente | Sub-agente retorna NEEDS_CONTEXT (nao inventa) |

## Code

<!-- lang: python | purpose: plan-to-prompt conversion for subagent dispatch -->
```python
# Controller converte task do plano em prompt executavel
def task_to_prompt(task, plan):
    dep = plan.get_task(task.depends_on)
    return f"""You are implementing Task {task.id}: {task.name}.

    **Task Description**
    {task.full_text}

    **Context**
    Follows Task {dep.id} ({dep.summary}).
    Files: {', '.join(task.file_paths)}

    **Your Job**
    1. Write failing tests first (TDD)
    2. Implement exactly what the task specifies
    3. Run verification: {task.verification}
    4. Commit with message: "{task.commit_msg}"
    5. Report: DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT"""

# Dispatch: paralelo para independentes, sequencial para dependentes
for batch in plan.dependency_batches():
    results = parallel_execute(
        [task_to_prompt(t, plan) for t in batch],
        tools=["read", "write", "edit", "bash"]
    )
    if any(r.status == "BLOCKED" for r in results):
        escalate(blocked=[r for r in results if r.status == "BLOCKED"])
    for r in results:
        if r.status == "DONE_WITH_CONCERNS":
            log_concerns(r.task_id, r.concerns)
```

Fluxo tipico: plan loader le arquivo `.md`, parser extrai tasks com metadata (files, deps, verification), dispatcher agrupa por dependencia em batches, executor despacha batch inteiro em paralelo. Resultado de cada task alimenta o contexto da proxima wave.

## Anti-Patterns

- Plano como design doc sem steps executaveis (sub-agente nao sabe o que fazer)
- Tasks de 30+ minutos (perda de foco, desvio do objetivo)
- Verificacao ausente ("implemente X" sem "confirme via Y")
- Pular brainstorming e ir direto ao plano (design nao validado)
- Referenciar arquivos inexistentes sem task de criacao previa

## References

- source: https://martinfowler.com/bliki/TestDrivenDevelopment.html
- source: https://docs.anthropic.com/en/docs/agents-and-tools
- related: p01_kc_cex_function_become
- related: p01_kc_cex_function_reason
