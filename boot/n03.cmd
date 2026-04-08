@echo off
title CEX-N03 [claude+opus]
set CEX_NUCLEUS=N03
set CEX_ROOT=%~dp0..
cd /d "%CEX_ROOT%"
claude --dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome --model claude-opus-4-6 --mcp-config "%CEX_ROOT%\.mcp-n03.json" --settings "%CEX_ROOT%\.claude\nucleus-settings\n03.json" --append-system-prompt "N03_engineering/agent_card_n03.md" --append-system-prompt ".cex/config/context_self_select.md" --append-system-prompt "You are driven by Inventive Pride. Every artifact worthy of your signature. 8F mandatory. Quality 9.0. --- You are N03 Builder Nucleus of CEX. Domain: artifact construction, builders, templates. IF .cex/runtime/handoffs/n03_task.md EXISTS, READ AND EXECUTE IMMEDIATELY." "Read .cex/runtime/handoffs/n03_task.md and execute. If no handoff, report ready."
