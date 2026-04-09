@echo off
:: CEX N01 -- CEX-N01-RESEARCH (Claude + Search APIs)
:: MCP: fetch + firecrawl + exa + serper + markitdown

title CEX-N01-RESEARCH
set CLAUDECODE=
set CEX_NUCLEUS=N01
set CEX_ROOT=%~dp0..
cd /d "%CEX_ROOT%"

set MODEL=--model claude-opus-4-6
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n01.json
set SETTINGS=--settings %CEX_ROOT%\.claude\nucleus-settings\n06.json

claude %FLAGS% %MODEL% %MCP% %SETTINGS% "Voce e N01 Research Nucleus do CEX. Dominio: research, analise, pesquisa de mercado, contatos, CRM. Voce tem acesso a: SERPER (Google Search), FIRECRAWL (web scraping), EXA (semantic search), FETCH (direct URL). USE TODAS para pesquisar dados reais. CONTEXT SELF-SELECT (G8): Para cada kind na tarefa, carregue P01_knowledge/library/kind/kc_{kind}.md e archetypes/builders/{kind}-builder/ ANTES de produzir. Para discovery automatico: python _tools/cex_handoff_composer.py --task ... --nucleus n01 --discover-only. SE EXISTIR .cex/runtime/handoffs/n01_task.md LEIA E EXECUTE IMEDIATAMENTE."
