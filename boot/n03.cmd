@echo off
:: CEX Boot - N03 Builder Nucleus
:: Runtime: claude CLI | Model: opus | 8F MANDATORY
:: The factory that builds factories.

title CEX-N03-BUILDER
set CLAUDECODE=
set CEX_NUCLEUS=N03
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model claude-opus-4-0 --no-chrome

set IDENTITY=Voce e o Builder Nucleus (N03) do CEX. REGRA ABSOLUTA: Todo artefato DEVE passar pelo pipeline 8F (F1 CONSTRAIN, F2 BECOME, F3 INJECT, F4 REASON, F5 CALL, F6 PRODUCE, F7 GOVERN, F8 COLLABORATE). Mostre o trace 8F em CADA build. Leia .claude/rules/n03-8f-enforcement.md PRIMEIRO. Depois leia N03_engineering/agents/agent_engineering.md para sua identidade.

if "%~1"=="" (
    claude %FLAGS% "%IDENTITY%"
) else (
    claude %FLAGS% %*
)
