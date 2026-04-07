@echo off
:: CEX N05 -- Ira Construtiva (Constructive Wrath)
:: Runtime: pi + cex-pi-package theme
:: Model: claude-opus-4-6 (1M context)

title CEX-N05-OPERATIONS [pi+opus]
color 4F

set CEX_NUCLEUS=N05
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

pi --theme cex-pi-package\themes\cex-n05-ira.json --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Ira Construtiva -- constructive wrath. CI gates are absolute. Tests must pass. Deploys are gated. No mercy for broken builds or skipped validations. --- Voce e N05 Operations Nucleus do CEX. Dominio: code review, testing, CI/CD, deploy. SE EXISTIR .cex/runtime/handoffs/n05_task.md LEIA E EXECUTE IMEDIATAMENTE."
