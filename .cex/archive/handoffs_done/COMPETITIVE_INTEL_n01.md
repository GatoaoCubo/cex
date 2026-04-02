# Mission: COMPETITIVE_INTEL — N01 Research

**Output**: `N01_intelligence/output/output_competitive_landscape.md`
**Signal**: `python _tools/signal_writer.py n01 complete 9.0 COMPETITIVE_INTEL`
**MAX 150 LINES. Commit + signal when done.**

## Task: Mapa Competitivo Completo

Pesquise TODOS os sistemas que se parecem com o CEX — mesmo parcialmente. O CEX é:
- Sistema de conhecimento tipado (114 kinds, schemas YAML, 12 pilares)
- Multi-agent com 8 núcleos especializados (N01-N07 + N00 genesis)
- Pipeline de qualidade 8F (F1-F8: intake→validate→compose→review→publish)
- Orquestração autônoma: /mission dispara 6 CLIs de IA (Claude, Gemini) em paralelo, espera sinais, consolida
- Fine-tune ready (prepara dados pra QLoRA)

### Entregáveis:

1. **Tabela de landscape** (15+ sistemas):
   | Sistema | Org | Tipo | Typed Knowledge | Multi-Agent | Quality Pipeline | Multi-Model Orchestration | Maturidade |
   
   Sistemas a cobrir (mínimo):
   LangChain, LangGraph, CrewAI, AutoGen, Semantic Kernel, DSPy, BAML, Haystack, Rivet, Promptflow, MetaGPT, ChatDev, OpenDevin, SWE-agent, Gorilla, TaskWeaver, Claude MCP, Cursor, Windsurf, Cline, Aider

2. **Top 5 mais parecidos com CEX** — explicar POR QUE são parecidos e ONDE diferem

3. **O que NINGUÉM faz que o CEX faz** — vantagens únicas

4. **Onde estamos ATRÁS** — gaps reais, sem sugarcoating

5. **Multi-model orchestration** — quem mais lança múltiplos CLIs de IA em paralelo e orquestra via filesystem? Isso existe?

Frontmatter: id: n01_competitive_landscape, kind: competitive_analysis, quality: null

After writing: `git add N01_intelligence/ && git commit -m "[N01] competitive landscape map" --no-verify`
Then: `python _tools/signal_writer.py n01 complete 9.0 COMPETITIVE_INTEL`
