# Mission: COMPETITIVE_INTEL — N04 Knowledge

**Output**: `N04_knowledge/output/output_competitive_knowledge.md`
**Signal**: `python _tools/signal_writer.py n04 complete 9.0 COMPETITIVE_INTEL`
**MAX 150 LINES. Commit + signal when done.**

## Task: Gestão de Conhecimento em Competidores

O CEX tem um sistema de conhecimento tipado único:
- 114 kinds (tipos de artefato: strategy, persona, brand_voice, output_template, etc.)
- 12 pillars (P01-P12: knowledge, brand, funnel, content, formatter, etc.)
- Knowledge Cards (KCs) por kind com definição, regras, exemplos
- Schemas YAML por pilar com validação
- Builder ISOs (13 arquivos por builder: system_prompt, instruction, quality_gate, etc.)
- Memory system com decay + relevance scoring

### Pesquisar:

1. **Quem tem typed knowledge?**
   - DSPy: signatures + modules — como se compara aos kinds do CEX?
   - BAML: type-safe LLM functions — overlap com schemas?
   - Semantic Kernel: plugin system — similar a builders?
   - LangChain: structured output — vs CEX schemas?
   - Haystack: pipeline components — typed?

2. **Quem tem knowledge cards / knowledge base integrada?**
   - RAG systems (LlamaIndex, Pinecone, etc.) — mas são typed?
   - Notion AI / Obsidian AI — knowledge but not typed
   - O CEX é unique em ter KCs por kind?

3. **Quem tem builder/agent templates com ISOs?**
   - CrewAI agent configs
   - AutoGen agent specs  
   - MetaGPT role definitions
   - Compare: quantos arquivos de config por agent? CEX tem 13 ISOs.

4. **Quem tem quality pipeline para knowledge?**
   - 8F pipeline (F1-F8) — existe equivalente?
   - Peer review scoring — quem faz?

### Entregáveis:
1. **Tabela**: CEX knowledge system vs 5 competidores
2. **Unique**: o que só o CEX tem
3. **Gaps**: onde estamos atrás
4. **Insight**: a profundidade do knowledge system (114 kinds × 13 ISOs = 1482 configs) é vantagem ou over-engineering?

Frontmatter: id: n04_competitive_knowledge, kind: competitive_analysis, quality: null

After writing: `git add N04_knowledge/ && git commit -m "[N04] competitive knowledge systems" --no-verify`
Then: `python _tools/signal_writer.py n04 complete 9.0 COMPETITIVE_INTEL`
