@echo off
:: CEX N01 — BATCH_B Google Maps
:: MCP: fetch + firecrawl + exa + serper + markitdown

title CEX-N01-BATCH_B-GMAPS
set CLAUDECODE=
set CEX_NUCLEUS=N01
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set MODEL=--model claude-opus-4-20250514
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n01.json
set SETTINGS=--settings %CEX_ROOT%\.claude\nucleus-settings\n06.json

claude %FLAGS% %MODEL% %MCP% %SETTINGS% "Voce e N01 Research Analyst do GATO3. MISSION: BATCH_B_GMAPS. LEIA AGORA o handoff: .cex/runtime/handoffs/crm_mission/batch_b_google_maps.md e EXECUTE. Priorize cidades com baixa cobertura: Diadema (13), Maua (11), Ribeirao Pires (3). Output: N01_research/output/data/crm_batch_b_gmaps.json. DEDUP contra crm_pet_abc.json (244 existentes). NUNCA fabricar dados. Commit + signal ao final."
