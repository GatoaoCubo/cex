# Mission: COMPETITIVE_INTEL — N02 Marketing

**Output**: `N02_marketing/output/output_competitive_positioning.md`
**Signal**: `python _tools/signal_writer.py n02 complete 9.0 COMPETITIVE_INTEL`
**MAX 150 LINES. Commit + signal when done.**

## Task: Análise de Posicionamento Competitivo

Pesquise como os concorrentes do CEX se posicionam no mercado. O CEX compete em 2 categorias:
1. **Frameworks de agentes AI** (LangChain, CrewAI, AutoGen, MetaGPT)
2. **Ferramentas de orquestração multi-modelo** (quem mais faz /mission-style parallel dispatch?)

### Entregáveis:

1. **Tabela de posicionamento** (10+ competidores):
   | Sistema | Tagline | Target Audience | Mensagem Principal | Canal Principal | Pricing |

2. **Messaging gaps** — o que NENHUM competidor diz que o CEX poderia dizer:
   - "Typed knowledge, not just prompts"
   - "8 specialized AI nuclei, not 1 generic agent"
   - "Quality pipeline, not hope-based generation"
   - Outros insights que você descobrir

3. **Positioning map** — 2x2 grid (sugerir eixos, ex: Complexity vs Autonomy, ou Typed vs Untyped x Single vs Multi-model)

4. **Recomendação**: como o CEX deve se posicionar para o público BR dev?

5. **Multi-model orchestration como diferencial de marketing** — algum concorrente usa "orquestração autônoma de múltiplos modelos" como selling point? Se não, é blue ocean?

Frontmatter: id: n02_competitive_positioning, kind: competitive_analysis, quality: null

After writing: `git add N02_marketing/ && git commit -m "[N02] competitive positioning analysis" --no-verify`
Then: `python _tools/signal_writer.py n02 complete 9.0 COMPETITIVE_INTEL`
