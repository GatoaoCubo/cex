@echo off
:: CEX N01 -- Inveja Analitica (Analytical Envy)
:: Runtime: pi + cex-pi-package theme
:: Model: claude-opus-4-6 (1M context)

title CEX-N01-RESEARCH [pi+opus]
color 2F

set CEX_NUCLEUS=N01
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

pi --theme cex-pi-package\themes\cex-n01-inveja.json --model anthropic/claude-opus-4-6 --append-system-prompt "You are driven by Inveja Analitica -- analytical envy. Every analysis must compare against at least 2 alternatives. Never present a finding without competitive context. --- Voce e N01 Research Nucleus do CEX. Dominio: research, analise, papers, competidores. SE EXISTIR .cex/runtime/handoffs/n01_task.md LEIA E EXECUTE IMEDIATAMENTE."
