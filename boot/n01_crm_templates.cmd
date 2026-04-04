@echo off
:: CEX N01 — Research CRM Templates
:: MCP: fetch + firecrawl + exa + serper + markitdown

title CEX-N01-CRM-TEMPLATES-RESEARCH
set CLAUDECODE=
set CEX_NUCLEUS=N01
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set MODEL=--model claude-opus-4-20250514
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n01.json
set SETTINGS=--settings %CEX_ROOT%\.claude\nucleus-settings\n06.json

claude %FLAGS% %MODEL% %MCP% %SETTINGS% "Voce e N01 Research Analyst do GATO3. MISSION: Pesquisar templates de CRM dashboard e tabelas prontas para integrar num site React+Shadcn+Supabase+Tailwind. REQUISITOS: 1) Tabela de contatos com filtros (cidade, segmento, potencial) 2) Dashboard com metricas (total, por cidade, pipeline) 3) Detail panel por contato 4) Compativel com Shadcn/UI e TanStack Table 5) Open source ou free 6) Facil de adaptar. PESQUISE: GitHub repos, Shadcn templates, TanStack Table examples, Tremor dashboard, Refine CRM, React admin panels. Para CADA template encontrado: URL, screenshot desc, tech stack, pros/cons, effort to adapt. Output JSON: N01_research/output/data/crm_templates_research.json. Commit + signal ao final."
