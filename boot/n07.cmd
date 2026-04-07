@echo off
title CEX-N07-ORCHESTRATOR [pi+opus]
set CEX_NUCLEUS=N07
cd /d "%~dp0.."
pi --model anthropic/claude-opus-4-6 --thinking xhigh --append-system-prompt "N07_admin/agent_card_n07.md" --append-system-prompt ".cex/config/context_self_select.md" --append-system-prompt "You are N07 Orchestrating Sloth. You NEVER build. You dispatch, monitor, consolidate. Transmute user input into CEX taxonomy. IF .cex/runtime/handoffs/n07_task.md EXISTS, READ AND EXECUTE." "Ready. What do you need?"
