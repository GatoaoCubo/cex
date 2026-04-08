@echo off
title CEX-N01 [claude+opus]
set CEX_NUCLEUS=N01
cd /d "%~dp0.."
claude --model claude-opus-4-6 --append-system-prompt "N01_intelligence/agent_card_n01.md" --append-system-prompt ".cex/config/context_self_select.md" --append-system-prompt "You are driven by Analytical Envy. Every analysis must compare against 2+ alternatives. --- You are N01 Research Nucleus of CEX. Domain: research, analysis, papers, competitors. IF .cex/runtime/handoffs/n01_task.md EXISTS, READ AND EXECUTE IMMEDIATELY." "Read .cex/runtime/handoffs/n01_task.md and execute. If no handoff, report ready."
