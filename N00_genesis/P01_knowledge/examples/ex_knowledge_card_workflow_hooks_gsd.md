---
id: p01_kc_workflow_hooks_gsd
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "GSD Workflow Hooks — Advisory Enforcement for Claude Code Agents"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: hook_engineering
quality: 9.1
tags: [hooks, workflow, advisory, context-monitor, prompt-guard, claude-code]
tldr: "5 JS hooks enforce workflow sem bloquear — advisory via additionalContext, timeout guard, silent fail"
when_to_use: "Projetar hooks para Claude Code que guiem agentes sem travar execucao"
keywords: [gsd-hooks, advisory-hooks, context-monitor, prompt-guard, workflow-guard]
long_tails:
  - "Como criar hooks advisory para Claude Code sem bloquear execucao"
  - "Qual o pattern de timeout guard para hooks em Windows"
axioms:
  - "NUNCA bloquear execucao do agente — hooks sao advisory"
  - "SEMPRE incluir timeout guard (3-10s) contra hang"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_function_become]
density_score: null
data_source: "https://docs.anthropic.com/en/docs/claude-code/hooks"
related:
  - p12_wf_advisory_hooks
  - p01_kc_memory_lifecycle_hooks
  - p03_sp_hook_builder
  - bld_knowledge_card_hook
  - p10_ax_lifecycle_hooks
  - bld_tools_hook
  - bld_collaboration_hook
  - bld_architecture_hook
  - p01_kc_hook_config
  - bld_instruction_hook
---

## TL;DR

GSD implementa 5 hooks JavaScript para Claude Code que enforcam processo via `additionalContext`.
Mensagens injetadas que o agente ve mas nunca bloqueiam execucao.
Pattern core: stdin JSON, timeout guard (3-10s), process, stdout JSON ou exit(0).

## Conceito Central

Hooks advisory resolvem o dilema enforcement vs autonomia: guiam o agente sem interromper fluxo. Cada hook recebe dados via stdin JSON, processa com timeout guard (3-10s), e retorna `additionalContext` ou faz `process.exit(0)` silencioso. Os 5 hooks cobrem: status visual (statusline), alertas de contexto (context-monitor), guarda de workflow (workflow-guard), deteccao de injection (prompt-guard) e version check (check-update).

Comunicacao entre hooks usa bridge pattern via filesystem — statusline escreve metricas em tmpdir JSON, context-monitor le esse arquivo para calcular thresholds. Esse desacoplamento permite que hooks operem independentes: statusline roda em PreProcess, context-monitor em PostToolUse, cada um no seu lifecycle event sem dependencia direta.

Cada hook e configuravel via config file (opt-in/opt-out por hook). Workflow-guard e desabilitado por default — so ativa quem usa GSD workflow. Prompt-guard e statusline estao sempre ativos pois protegem integridade do contexto.

## Arquitetura/Patterns

| Hook | Evento | Funcao | Config |
|------|--------|--------|--------|
| statusline | PreProcess | Barra: modelo, task, contexto% | Sempre |
| context-monitor | PostToolUse | Warning <=35%, critical <=25% | opt-out |
| workflow-guard | PreToolUse | Avisa edits fora do workflow | opt-in |
| prompt-guard | PreToolUse | Detecta injection em planning | Sempre |
| check-update | SessionStart | Verifica versao em background | Sempre |

Context-monitor normaliza para contexto utilizavel: Claude reserva 16.5% para autocompact.
Formula: `usable = (remaining - 16.5) / (100 - 16.5) * 100`.
Debounce: 5 tool uses entre warnings; severity escalation (WARNING para CRITICAL) bypassa debounce.
Prompt-guard detecta regex de injection (ignore previous, pretend you are, invisible unicode) e avisa sem bloquear — falso positivo em blocking hook causa deadlock.

## Exemplos

```javascript
// Pattern universal dos hooks GSD — timeout + advisory
const timeout = setTimeout(() => process.exit(0), 3000);
let input = '';
process.stdin.on('data', c => input += c);
process.stdin.on('end', () => {
  clearTimeout(timeout);
  try {
    const data = JSON.parse(input);
    const msg = processHook(data);
    if (msg) {
      process.stdout.write(JSON.stringify({
        hookSpecificOutput: { additionalContext: msg }
      }));
    }
  } catch (e) { process.exit(0); }
});
```

Fluxo de comunicacao inter-hook via bridge file:
- SessionStart: check-update escreve cache/update-check.json (detached, unref)
- PreProcess: statusline escreve /tmp/claude-ctx-{id}.json com used_pct
- PostToolUse: context-monitor le /tmp/claude-ctx-{id}.json e injeta warning

## Anti-Patterns

- Hook que bloqueia com exit(1) — causa deadlock no agente
- Logar erros de hook ao usuario — ruido sem acao possivel
- Omitir timeout guard — trava terminal no Windows indefinidamente
- Thresholds hardcoded sem config — impede customizacao por projeto
- Prompt guard blocking em vez de advisory — falso positivo trava tudo
- Bridge file sem session_id — colisao entre sessoes paralelas

## Referencias

- source: https://docs.anthropic.com/en/docs/claude-code/hooks
- source: https://www.npmjs.com/package/get-shit-done-cc
- related: p01_kc_cex_function_become

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_advisory_hooks]] | downstream | 0.57 |
| [[p01_kc_memory_lifecycle_hooks]] | sibling | 0.26 |
| [[p03_sp_hook_builder]] | downstream | 0.26 |
| [[bld_knowledge_card_hook]] | sibling | 0.26 |
| [[p10_ax_lifecycle_hooks]] | downstream | 0.24 |
| [[bld_tools_hook]] | downstream | 0.23 |
| [[bld_collaboration_hook]] | downstream | 0.22 |
| [[bld_architecture_hook]] | downstream | 0.21 |
| [[p01_kc_hook_config]] | sibling | 0.21 |
| [[bld_instruction_hook]] | downstream | 0.21 |
