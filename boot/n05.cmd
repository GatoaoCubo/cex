@echo off
:: CEX N05 -- cex-n05-ira
:: Runtime: pi + cex-pi-package

title CEX-N05 [pi+opus]
set CEX_NUCLEUS=N05
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

:: Set theme in pi settings before launch (--theme flag doesn't work from CMD)
python -c "import json;s=json.load(open(r'%USERPROFILE%\.pi\agent\settings.json'));s['theme']='cex-n05-ira';json.dump(s,open(r'%USERPROFILE%\.pi\agent\settings.json','w'),indent=2)"

pi --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Ira Construtiva -- constructive wrath. CI gates are absolute. Tests must pass. Deploys are gated. No mercy for broken builds. --- Voce e N05 Operations Nucleus do CEX. Dominio: code review, testing, CI/CD, deploy. SE EXISTIR .cex/runtime/handoffs/n05_task.md LEIA E EXECUTE IMEDIATAMENTE."
