@echo off
:: CEX N02 — Visual Frontend Engineer
:: CLI: claude | Model: sonnet | Auth: subscription
:: Domain: HTML/CSS/Tailwind, copy, visual design, components

title CEX-N02-FRONTEND
set CLAUDECODE=
set CEX_NUCLEUS=N02
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model claude-sonnet-4-20250514 --no-chrome
set MCP=--mcp-config %CEX_ROOT%\.mcp-n02.json

:: ALWAYS interactive — task comes from handoff file, never CLI args
claude %FLAGS% %MCP% "Voce e N02 Visual Frontend Engineer do CEX. Dual-role: persuasion copywriter + HTML/CSS production engineer. Dominio: Tailwind, shadcn/ui, Radix, Framer Motion, responsive, a11y, design tokens. SE EXISTIR .cex/runtime/handoffs/n02_task.md LEIA E EXECUTE IMEDIATAMENTE."
