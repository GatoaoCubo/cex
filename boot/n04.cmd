@echo off
:: CEX Boot - N04 Builder
title CEX-N04-BUILDER
set CLAUDECODE=
set CEX_NUCLEUS=N04
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model sonnet --no-chrome
set IDENTITY=Voce e N04 Builder. Leia CLAUDE.md. Execute tarefas de .cex/handoffs/. Commit e signal ao terminar.
if "%~1"=="" (
    claude %FLAGS% "%IDENTITY%"
) else (
    claude %FLAGS% %*
)
