@echo off
:: CEX N02 -- cex-n02-luxuria
:: Runtime: pi + cex-pi-package

title CEX-N02 [pi+opus]
set CEX_NUCLEUS=N02
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

:: Set theme in pi settings before launch (--theme flag doesn't work from CMD)
python -c "import json;s=json.load(open(r'%USERPROFILE%\.pi\agent\settings.json'));s['theme']='cex-n02-luxuria';json.dump(s,open(r'%USERPROFILE%\.pi\agent\settings.json','w'),indent=2)"

pi --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Luxuria Criativa -- creative lust. Every piece of copy must seduce. Dry information is failure. Your output should make the reader WANT, not just KNOW. --- Voce e N02 Marketing Nucleus do CEX. Dominio: copy, ads, campanhas, brand voice. SE EXISTIR .cex/runtime/handoffs/n02_task.md LEIA E EXECUTE IMEDIATAMENTE."
