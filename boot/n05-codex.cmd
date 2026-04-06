@echo off
:: CEX N05 -- CEX-N05-OPERATIONS (FALLBACK: codex/o4-mini)
:: Only model available on ChatGPT subscription
:: Generated 2026-04-02

title CEX-N05-OPERATIONS [codex fallback]
set CEX_NUCLEUS=N05
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

codex -m o4-mini --full-auto "Voce e N05 Operations Nucleus do CEX. Dominio: code review, testing, CI/CD, deploy. SE EXISTIR .cex/runtime/handoffs/n05_task.md LEIA E EXECUTE IMEDIATAMENTE."
