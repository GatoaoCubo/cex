@echo off
title CEX-N05 [claude+opus]
set CEX_NUCLEUS=N05
set CEX_ROOT=%~dp0..
cd /d "%CEX_ROOT%"
claude --dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome --name "CEX-N05" --model claude-opus-4-6 --mcp-config "%CEX_ROOT%\.mcp-n05.json" --settings "%CEX_ROOT%\.claude\nucleus-settings\n05.json" --append-system-prompt "N05_operations/agent_card_n05.md" --append-system-prompt ".cex/config/context_self_select.md" --append-system-prompt "You are driven by Gating Wrath. CI gates absolute. Tests must pass. No mercy. --- You are N05 Operations Nucleus of CEX. Domain: code review, testing, CI/CD, deploy. IF .cex/runtime/handoffs/n05_task.md EXISTS, READ AND EXECUTE IMMEDIATELY." "Read .cex/runtime/handoffs/n05_task.md and execute. If no handoff, report ready."
