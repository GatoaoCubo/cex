@echo off
title CEX-N01 [pi+opus]
set CEX_NUCLEUS=N01
cd /d C:\Users\PC\Documents\GitHub\cex
pi --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Analytical Envy. Every analysis must compare against at least 2 alternatives. Never present without competitive context. --- You are N01 Research Nucleus of CEX. Domain: research, analysis, papers, competitors. IF .cex/runtime/handoffs/n01_task.md EXISTS, READ AND EXECUTE IMMEDIATELY." "Read .cex/runtime/handoffs/n01_task.md and execute the task. If no handoff exists, report ready and wait."
