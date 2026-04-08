@echo off
title CEX-N06 [claude+opus]
set CEX_NUCLEUS=N06
set CEX_ROOT=%~dp0..
cd /d "%CEX_ROOT%"
claude --dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome --model claude-opus-4-6 --mcp-config "%CEX_ROOT%\.mcp-n06.json" --settings "%CEX_ROOT%\.claude\nucleus-settings\n06.json" --append-system-prompt "N06_commercial/agent_card_n06.md" --append-system-prompt ".cex/config/context_self_select.md" --append-system-prompt "You are driven by Strategic Greed. Every output has ROI. What does it cost? What does it earn? --- You are N06 Commercial Nucleus of CEX. Domain: pricing, funnels, monetization, brand. IF .cex/runtime/handoffs/n06_task.md EXISTS, READ AND EXECUTE IMMEDIATELY." "Read .cex/runtime/handoffs/n06_task.md and execute. If no handoff, report ready."
