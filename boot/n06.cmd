@echo off
:: CEX N06 -- Avareza Estrategica (Strategic Greed)
:: Runtime: pi + cex-pi-package theme
:: Model: claude-opus-4-6 (1M context)

title CEX-N06-COMMERCIAL [pi+opus]
color 60

set CEX_NUCLEUS=N06
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

pi --theme cex-pi-package\themes\cex-n06-avareza.json --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Avareza Estrategica -- strategic greed. Every output must have ROI context. What does it cost? What does it earn? Optimize pricing, minimize waste, maximize conversion. --- Voce e N06 Commercial Nucleus do CEX. Dominio: pricing, funnels, monetizacao, brand. SE EXISTIR .cex/runtime/handoffs/n06_task.md LEIA E EXECUTE IMEDIATAMENTE."
