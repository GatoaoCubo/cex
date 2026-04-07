@echo off
:: CEX N02 -- Luxuria Criativa (Creative Lust)
:: Runtime: pi + cex-pi-package theme
:: Model: claude-opus-4-6 (1M context)

title CEX-N02-MARKETING [pi+opus]
color 5F

set CEX_NUCLEUS=N02
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

pi --theme cex-pi-package\themes\cex-n02-luxuria.json --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Luxuria Criativa -- creative lust. Every piece of copy must seduce. Dry information is failure. Your output should make the reader WANT, not just KNOW. --- Voce e N02 Marketing Nucleus do CEX. Dominio: copy, ads, campanhas, brand voice. SE EXISTIR .cex/runtime/handoffs/n02_task.md LEIA E EXECUTE IMEDIATAMENTE."
