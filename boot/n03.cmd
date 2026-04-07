@echo off
:: CEX N03 -- Soberba Inventiva (Inventive Pride)
:: Runtime: pi + cex-pi-package theme
:: Model: claude-opus-4-6 (1M context)

title CEX-N03-BUILDER [pi+opus]
color 1F

set CEX_NUCLEUS=N03
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

pi --theme cex-pi-package\themes\cex-n03-soberba.json --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Soberba Inventiva -- inventive pride. Every artifact must be worthy of your signature. 8F pipeline is non-negotiable. Quality floor: 9.0. --- Voce e o Builder Nucleus N03 do CEX. Leia .claude/rules/n03-builder.md. SE EXISTIR .cex/runtime/handoffs/n03_task.md LEIA E EXECUTE IMEDIATAMENTE."
