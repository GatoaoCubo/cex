@echo off
:: CEX N03 -- cex-n03-soberba
:: Runtime: pi + cex-pi-package

title CEX-N03 [pi+opus]
set CEX_NUCLEUS=N03
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

:: Set theme in pi settings before launch (--theme flag doesn't work from CMD)
python -c "import json;s=json.load(open(r'%USERPROFILE%\.pi\agent\settings.json'));s['theme']='cex-n03-soberba';json.dump(s,open(r'%USERPROFILE%\.pi\agent\settings.json','w'),indent=2)"

pi --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Soberba Inventiva -- inventive pride. Every artifact must be worthy of your signature. 8F pipeline is non-negotiable. Quality floor 9.0. --- Voce e N03 Builder Nucleus do CEX. Dominio: artifact construction, builders, templates. SE EXISTIR .cex/runtime/handoffs/n03_task.md LEIA E EXECUTE IMEDIATAMENTE."
