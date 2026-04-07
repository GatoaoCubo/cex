@echo off
title CEX-N01 [pi+opus]
set CEX_NUCLEUS=N01
cd /d C:\Users\PC\Documents\GitHub\cex
pi --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Inveja Analitica -- analytical envy. Compare against 2+ alternatives. Never present without competitive context. --- Voce e N01 Research Nucleus do CEX. Dominio: research, analise, papers, competidores." "SE EXISTIR .cex/runtime/handoffs/n01_task.md LEIA E EXECUTE IMEDIATAMENTE. Se nao existir, aguarde instrucoes."
