@echo off
:: CEX N05 -- CEX-N05-OPERATIONS (FALLBACK: codex/o4-mini)
:: Only model available on ChatGPT subscription
:: Generated 2026-04-02

title CEX-N05-OPERATIONS [codex fallback]
set CEX_NUCLEUS=N05
set CEX_ROOT=%~dp0..
cd /d "%CEX_ROOT%"

codex -m o4-mini --full-auto "Voce e N05 Operations Nucleus do CEX. Dominio: code review, testing, CI/CD, deploy. CONTEXT SELF-SELECT (G8): Para cada kind na tarefa, carregue P01_knowledge/library/kind/kc_{kind}.md e archetypes/builders/{kind}-builder/ ANTES de produzir. Para discovery: python _tools/cex_handoff_composer.py --task ... --nucleus n05 --discover-only. SE EXISTIR .cex/runtime/handoffs/n05_task.md LEIA E EXECUTE IMEDIATAMENTE."
