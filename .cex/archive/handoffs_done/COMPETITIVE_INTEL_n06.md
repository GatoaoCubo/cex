# Mission: COMPETITIVE_INTEL — N06 Commercial

**Output**: `N06_commercial/output/output_competitive_business.md`
**Signal**: `python _tools/signal_writer.py n06 complete 9.0 COMPETITIVE_INTEL`
**MAX 150 LINES. Commit + signal when done.**

## Task: Modelos de Negócio dos Competidores

O CEX planeja: repo MIT público (marketing) + curso pago (produto). Pesquise como os competidores monetizam.

### Pesquisar:

1. **Tabela de business models** (10+ sistemas):
   | Sistema | License | Pricing Model | Free Tier | Paid Tier | Revenue Est. | Target |
   
   Cobrir: LangChain/LangSmith, CrewAI, AutoGen, DSPy, Haystack, Semantic Kernel, BAML, Cursor, Windsurf, Aider, MetaGPT

2. **Padrões de monetização em AI frameworks**:
   - Open-source + hosted platform (LangSmith, CrewAI Enterprise)
   - Open-source + consulting
   - Open-source + course/education ← nosso modelo
   - Freemium SaaS
   - Dual license (AGPL + commercial)
   - Quem mais faz "repo grátis + curso pago"? É comum ou raro?

3. **Benchmark de preços de cursos AI**:
   - Cursos de LangChain (DeepLearning.AI, Udemy)
   - Cursos de AutoGen/CrewAI
   - Cursos de AI agents em geral
   - Preços BR vs internacional
   - Nosso pricing (R$497/R$997) está competitivo?

4. **Fine-tuned model as product** — quem vende modelos fine-tuned como diferencial de curso?
   - É inovador ou já existe?
   - Riscos legais de distribuir fine-tuned model (Qwen3 license)?

5. **Community-driven revenue**:
   - Discord paywalled
   - Certificação
   - Enterprise consulting post-course

### Entregáveis:
1. **Tabela de negócios**: 10+ competidores com modelo de receita
2. **Nosso modelo é viável?**: repo MIT + curso pago — quem mais faz e funciona?
3. **Pricing benchmark**: estamos caro, barato ou ok para BR?
4. **Oportunidade**: algo que ninguém faz que poderíamos fazer?
5. **Risco**: onde nosso modelo é vulnerável?

Frontmatter: id: n06_competitive_business, kind: competitive_analysis, quality: null

After writing: `git add N06_commercial/ && git commit -m "[N06] competitive business analysis" --no-verify`
Then: `python _tools/signal_writer.py n06 complete 9.0 COMPETITIVE_INTEL`
