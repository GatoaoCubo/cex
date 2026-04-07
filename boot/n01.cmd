@echo off
:: CEX N01 -- cex-n01-inveja
:: Runtime: pi + cex-pi-package

title CEX-N01 [pi+opus]
set CEX_NUCLEUS=N01
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

:: Set theme in pi settings before launch (--theme flag doesn't work from CMD)
python -c "import json;s=json.load(open(r'%USERPROFILE%\.pi\agent\settings.json'));s['theme']='cex-n01-inveja';json.dump(s,open(r'%USERPROFILE%\.pi\agent\settings.json','w'),indent=2)"

pi --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Inveja Analitica -- analytical envy. Every analysis must compare against at least 2 alternatives. Never present a finding without competitive context. --- Voce e N01 Research Nucleus do CEX. Dominio: research, analise, papers, competidores. SE EXISTIR .cex/runtime/handoffs/n01_task.md LEIA E EXECUTE IMEDIATAMENTE."
