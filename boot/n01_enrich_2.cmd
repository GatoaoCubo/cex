@echo off
:: CEX N01 — ENRICH_2 SBC + Ribeirao Pires
:: MCP: fetch + firecrawl + exa + serper + markitdown

title CEX-N01-ENRICH_2-SBC-RP
set CLAUDECODE=
set CEX_NUCLEUS=N01
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set MODEL=--model claude-opus-4-20250514
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n01.json
set SETTINGS=--settings %CEX_ROOT%\.claude\nucleus-settings\n06.json

claude %FLAGS% %MODEL% %MCP% %SETTINGS% "Voce e N01 Research Analyst do GATO3. MISSION: ENRICH_2. LEIA AGORA: .cex/runtime/handoffs/crm_mission/enrich_2_sbc_rp.md — Enriquecer 117 contatos de SBC+Ribeirao Pires. A lista de nomes esta em N01_research/output/data/enrich_targets_2.json. Para CADA nome, pesquise telefone, whatsapp, email, instagram, website via SERPER e FETCH. Output: N01_research/output/data/crm_enrich_2.json. NUNCA inventar. Commit + signal ao final."
