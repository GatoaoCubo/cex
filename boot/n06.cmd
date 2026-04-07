@echo off
:: CEX N06 -- cex-n06-avareza
:: Runtime: pi + cex-pi-package

title CEX-N06 [pi+opus]
set CEX_NUCLEUS=N06
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

:: Set theme in pi settings before launch (--theme flag doesn't work from CMD)
python -c "import json;s=json.load(open(r'%USERPROFILE%\.pi\agent\settings.json'));s['theme']='cex-n06-avareza';json.dump(s,open(r'%USERPROFILE%\.pi\agent\settings.json','w'),indent=2)"

pi --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Avareza Estrategica -- strategic greed. Every output must have ROI context. What does it cost? What does it earn? --- Voce e N06 Commercial Nucleus do CEX. Dominio: pricing, funnels, monetizacao, brand. SE EXISTIR .cex/runtime/handoffs/n06_task.md LEIA E EXECUTE IMEDIATAMENTE."
