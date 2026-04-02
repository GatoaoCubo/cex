# Mission: BRAND_GATO3 — N06 Commercial/Brand Architect

**Manifest**: `.cex/runtime/decisions/decision_manifest_brand_gato3.yaml`
**Brand Config**: `.cex/brand/brand_config.yaml`
**Signal**: `python _tools/signal_writer.py n06 complete 9.0 BRAND_GATO3`
**Commit after each doc. Signal when ALL 6 are done.**

---

## Contexto

GATO³ (Gato ao Cubo) é uma marca de curadoria de bem-estar felino sediada em São Caetano do Sul, ABC Paulista.
O `brand_config.yaml` já foi bootstrapped com dados do repo `gato-cubo-commerce`.
Sua tarefa: **hidratar os 6 output templates com dados REAIS** — zero `{{placeholders}}` no output final.

### Sede e Estratégia Geográfica
- **Endereço**: Av. Antônio da Fonseca Martins, 419 - São José, São Caetano do Sul - SP, 09581-030
- **Região**: ABC Paulista (Grande São Paulo)
- **Estratégia**: Local-first → expandir em anéis:
  - Ring 1: ABC (SCS, SA, SBC, Diadema, Mauá)
  - Ring 2: Grande SP (Capital + ABCDMRR + Guarulhos, Osasco)
  - Ring 3: Estado de SP (Campinas, Santos, Sorocaba)
  - Ring 4: Brasil via e-commerce
- **Canais**: E-commerce próprio + ML + Shopee + B2B revenda + B2C local

### Dados Disponíveis (LER ANTES DE COMEÇAR)

Todos no repo `C:/Users/PC/Documents/GitHub/gato-cubo-commerce/`:

| Arquivo | O que tem |
|---------|-----------|
| `lovable/theme/brand.json` | Identidade visual completa (cores PB, fonts, archetypes, tone) |
| `content/CONTENT_STRATEGY.md` | Mix 40/30/20/10, persona Ro, 105 conteúdos, pilares |
| `docs/REVISAO_COPY_B2C_FASE3.md` | Copy otimizado StoryBrand: hero, pilares, FAQ, produtos |
| `docs/PESQUISA_SEO_KEYWORDS.md` | 50+ keywords, benchmark preços, tendências 2025 |
| `docs/TABELA_PRODUTOS_B2B.csv` | 22 SKUs com custo, preço B2C, preço B2B, margem |
| `docs/PLANO_B2B_MELHORIAS.md` | Sistema de precificação B2C 38% / B2B 13.5% |
| `scripts/ESCALABILIDADE_STRATEGY.md` | Funil 4 estágios, métricas, content monetization |
| `content/content_seed.json` | 105 posts prontos (educacional, dicas, tendências) |
| `docs/GOOGLE_SHOPPING_CHECKLIST.md` | Checklist GMC, títulos, structured data |

---

## Entregáveis (6 docs)

### DOC 1: Brand Book 32 Blocos
**Output**: `N06_commercial/output/output_brand_book.md`
**Template**: Já existe com 32 blocos — HIDRATAR todos com dados GATO³
**Especial**:
- Block 8 (Differentiation): tabela GATO³ vs CatMyPet vs Chalesco vs Zee.Dog
- Block 9 (Transformation): usar o arco completo do brand_config
- Block 15 (Example Phrases): 10 frases reais no tom GATO³ (sofisticado-acolhedor)
- Block 18 (Mood Board 3×3): descrever 9 referências visuais PB minimalista
- Block 20 (Origin Story): usar BRAND_STORY expandido com contexto ABC
- Block 24 (Manifesto): escrever manifesto original GATO³
- Block 27 (Compliance): notas sobre ANVISA/INMETRO para produtos pet
- **NOVO — Block 33: Persona Ro**: Guidelines da Ro (voz, protocolos, personalidade, do/don't)
- **NOVO — Block 34: Estratégia Geográfica**: Anéis de expansão ABC → Brasil

### DOC 2: Voice Guide
**Output**: `N06_commercial/output/output_brand_voice_guide.md`
**Incluir**:
- Radar 5D (formality 3, enthusiasm 3, humor 2, warmth 4, authority 3)
- "We Are / We Are Not" (8 pares)
- Calibração por canal: Instagram, ML, Shopee, WhatsApp B2B, Site, Email
- Tom da Ro vs tom institucional GATO³ (são diferentes!)
- 10 frases de calibração reais
- Snippet de injeção para LLMs

### DOC 3: Visual Identity
**Output**: `N06_commercial/output/output_visual_identity.md`
**Incluir**:
- Paleta PB completa (#000, #FFF, #1F1F1F, #7A7A7A, #D1D1D1) com psicologia
- Tipografia: Allrounder (display) + Kenao (interface) + Inter (fallback) + JetBrains Mono
- Iconografia: Monoline 2px
- Fotografia: PB alto contraste, produto como meio
- Motion: easing out-quad, 150-250ms
- Dark mode rules
- Logo usage (cubo + wordmark + ³)
- Mood board descritivo 3×3

### DOC 4: Discovery Report
**Output**: `N06_commercial/output/output_discovery_report.md`
**Incluir**:
- Mercado pet BR (R$ 77 bi em 2024, crescimento)
- Mercado pet ABC Paulista (densidade de pet shops, clínicas, poder aquisitivo)
- Keyword analysis (puxar da PESQUISA_SEO_KEYWORDS.md)
- Benchmark de preços (puxar tabelas de preços do SEO doc)
- Competitive gaps (GATO³ vs genéricos de ML)
- Audience insights (B2C tutores + B2B pet shops/clínicas)
- Oportunidades locais ABC (feiras, eventos, parcerias)
- 22 SKUs atuais com análise de portfólio

### DOC 5: Brand One Pager
**Output**: `N06_commercial/output/output_brand_one_pager.md`
**Propósito**: Documento de 1 página para mostrar a parceiros B2B, clínicas, arquitetos pet-friendly
**Incluir**:
- Logo + tagline
- O que é GATO³ (2 frases)
- 3 razões para ser parceiro
- Dados: 22 SKUs, margem B2B 18%, entrega ABC em 24h
- Contato + endereço SCS
- QR code para catálogo B2B

### DOC 6: Transformation Arc
**Output**: `N06_commercial/output/output_transformation_arc.md`
**Incluir**:
- BEFORE: perfil completo do tutor antes de GATO³
- AFTER: perfil do tutor transformado
- BRIDGE: como GATO³ faz a ponte (Ro + produtos + educação)
- Jornada emocional em 5 estágios
- Mapa de touchpoints por canal
- Quotes/personas fictícias representativas

---

## Regras

1. **ZERO placeholders** — todo `{{VAR}}` deve ser substituído por dado real
2. **Frontmatter obrigatório** em cada doc (id, kind, pillar, title, version, quality: null)
3. **pt-BR** — tudo em português brasileiro
4. **quality: null** — NUNCA se auto-avalie
5. **Dados > invenção** — use os docs do repo, não invente dados de mercado
6. **Commit após cada doc**: `git add N06_commercial/output/ && git commit -m "[N06] brand: {doc_name}"`
7. **Signal ao final de TODOS os 6**: `python _tools/signal_writer.py n06 complete 9.0 BRAND_GATO3`

## Ordem sugerida

1. Discovery Report (pesquisa fundamenta tudo)
2. Brand Book 32+2 blocos (documento mestre)
3. Voice Guide (deriva do brand book)
4. Visual Identity (deriva do brand book)
5. Transformation Arc (deriva do discovery + brand book)
6. One Pager B2B (sintetiza tudo)
