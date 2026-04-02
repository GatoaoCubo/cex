# Mission: COMPETITIVE_INTEL — N03 Engineering

**Output**: `N03_engineering/output/output_competitive_architecture.md`
**Signal**: `python _tools/signal_writer.py n03 complete 9.0 COMPETITIVE_INTEL`
**MAX 150 LINES. Commit + signal when done.**

## Task: Comparação Arquitetural Profunda

Compare a arquitetura do CEX com os principais competidores. Foco em 3 dimensões:

### A. Typed Knowledge Systems
O CEX tem 114 kinds tipados com schemas YAML, 12 pilares, knowledge cards. Quem mais faz isso?
- DSPy signatures?
- BAML type system?
- Semantic Kernel plugins?
- LangChain structured output?
Compare: quão tipado é cada um? Schema enforcement? Validation pipeline?

### B. Multi-Agent Orchestration Architecture
O CEX tem 8 núcleos (N00-N07), cada um é um processo CLI separado (Claude, Gemini). Comunicação via filesystem (handoffs, signals, PIDs). Compare com:
- CrewAI crews/agents
- AutoGen conversation patterns
- MetaGPT roles
- LangGraph state machines
- ChatDev phases

### C. /mission-style Multi-Model Dispatch ← FOCO PRINCIPAL
O CEX /mission faz: `spawn 6 CMD windows → each runs different AI CLI → poll filesystem for signals → kill-tree → quality gate → consolidate`

**Quem mais faz algo parecido?** Especificamente:
- Lançar múltiplos MODELOS DIFERENTES em paralelo (não múltiplas chamadas ao mesmo modelo)
- Cada modelo como processo independente (não threads na mesma app)
- Comunicação via filesystem (não API calls)
- Orquestrador que espera, detecta crashes, mata processos
- Quality gate pós-execução

### Entregáveis:
1. **Tabela arquitetural** (CEX vs 5 mais relevantes): typed system, agent model, communication, orchestration, quality
2. **O que é genuinamente único no CEX** do ponto de vista de engenharia
3. **Onde a arquitetura do CEX é inferior** — limitações reais
4. **Veredicto**: estamos na frente, atrás ou lateral?

Frontmatter: id: n03_competitive_architecture, kind: competitive_analysis, quality: null

After writing: `git add N03_engineering/ && git commit -m "[N03] competitive architecture comparison" --no-verify`
Then: `python _tools/signal_writer.py n03 complete 9.0 COMPETITIVE_INTEL`
