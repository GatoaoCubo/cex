# Mission: BRAND_GATO3 — N06 Brand Architect: HIDRATAR 6 Docs de Branding

**Manifest**: `.cex/runtime/decisions/decision_manifest_brand_gato3.yaml`
**Brand Config**: `.cex/brand/brand_config.yaml`
**Signal**: `python _tools/signal_writer.py n06 complete 9.0 BRAND_GATO3`
**Commit após CADA doc. Signal quando TODOS 6 estiverem prontos.**

---

## ⚠️ INSTRUÇÃO CRÍTICA — LEIA PRIMEIRO

Sua tarefa é **HIDRATAR templates existentes**, NÃO criar docs novos.

Existem 6 templates em `N06_commercial/output/` com `{{PLACEHOLDERS}}`.
Você deve **substituir CADA `{{VAR}}`** por dados reais do GATO³.

**VERIFICAÇÃO**: ao terminar cada doc, rode mentalmente `grep "{{" arquivo.md`.
Se encontrar QUALQUER `{{`, o doc está incompleto. Corrija antes de commitar.

**NÃO crie arquivos em P04, P05 ou outros pilares. Edite APENAS os 6 arquivos listados abaixo.**

---

## Dados do GATO³

### Brand Config (leia primeiro)
```
Arquivo: .cex/brand/brand_config.yaml
```
Contém: nome, tagline, slogan, mission, vision, values, story, archetype, voice 5D, ICP, colors, fonts, positioning, UVP, competitors, monetization, localização ABC.

### Dados complementares (leia do repo gato-cubo-commerce)
| Arquivo | Path completo |
|---------|---------------|
| brand.json | C:/Users/PC/Documents/GitHub/gato-cubo-commerce/lovable/theme/brand.json |
| Content Strategy | C:/Users/PC/Documents/GitHub/gato-cubo-commerce/content/CONTENT_STRATEGY.md |
| Copy B2C | C:/Users/PC/Documents/GitHub/gato-cubo-commerce/docs/REVISAO_COPY_B2C_FASE3.md |
| SEO Keywords | C:/Users/PC/Documents/GitHub/gato-cubo-commerce/docs/PESQUISA_SEO_KEYWORDS.md |
| Tabela B2B | C:/Users/PC/Documents/GitHub/gato-cubo-commerce/docs/TABELA_PRODUTOS_B2B.csv |
| Plano B2B | C:/Users/PC/Documents/GitHub/gato-cubo-commerce/docs/PLANO_B2B_MELHORIAS.md |
| Escalabilidade | C:/Users/PC/Documents/GitHub/gato-cubo-commerce/scripts/ESCALABILIDADE_STRATEGY.md |
| Content Seed | C:/Users/PC/Documents/GitHub/gato-cubo-commerce/content/content_seed.json |

### Dados geográficos
- **Sede**: Av. Antônio da Fonseca Martins, 419 - São José, São Caetano do Sul - SP, 09581-030
- **Região**: ABC Paulista
- **Estratégia**: Local-first expandindo em anéis (ABC → Grande SP → SP → Brasil)
- **Canais**: E-commerce + ML + Shopee + B2B revenda + B2C local

---

## OS 6 DOCS PARA HIDRATAR

### DOC 1: `N06_commercial/output/output_brand_book.md`
- Template já tem 32 blocos com {{PLACEHOLDERS}}
- Substituir TODOS por dados GATO³
- ADICIONAR Block 33 (Persona Ro) e Block 34 (Estratégia Geográfica)
- Block 8: tabela comparativa GATO³ vs CatMyPet vs Chalesco vs Zee.Dog
- Block 15: 10 frases reais no tom GATO³
- Block 24: escrever manifesto original GATO³
- Block 27: compliance ANVISA/INMETRO para produtos pet

### DOC 2: `N06_commercial/output/output_brand_voice_guide.md`
- Hidratar radar 5D com scores (formality:3, enthusiasm:3, humor:2, warmth:4, authority:3)
- Preencher "We Are / We Are Not" (8 pares)
- Adicionar calibração por canal: Instagram, ML, Shopee, WhatsApp B2B, Site, Email
- Tom da Ro (acolhedor, prático) vs tom institucional GATO³ (sofisticado, minimalista)
- 10 frases de calibração

### DOC 3: `N06_commercial/output/output_visual_identity.md`
- Paleta: #000000, #FFFFFF, #1F1F1F, #7A7A7A, #D1D1D1 com psicologia das cores
- Tipografia: Allrounder (display) + Kenao (interface) + Inter (fallback)
- Iconografia: Monoline 2px
- Fotografia: PB alto contraste
- Motion: out-quad, 150-250ms
- Logo: cubo + wordmark + expoente ³

### DOC 4: `N06_commercial/output/output_discovery_report.md`
- Mercado pet BR (R$ 77 bi 2024)
- Mercado ABC Paulista
- Keywords do doc PESQUISA_SEO_KEYWORDS.md
- Benchmark preços do mesmo doc
- 22 SKUs da TABELA_PRODUTOS_B2B.csv
- Competitive gaps

### DOC 5: `N06_commercial/output/output_brand_one_pager.md`
- 1 página para parceiros B2B
- Logo + tagline + o que é + 3 razões para ser parceiro
- Dados: 22 SKUs, margem B2B 18%, sede SCS

### DOC 6: `N06_commercial/output/output_transformation_arc.md`
- BEFORE/AFTER/BRIDGE completo
- Jornada emocional em 5 estágios
- Personas fictícias representativas

---

## Workflow EXATO

```bash
# Para CADA doc (1 a 6):
# 1. Leia o template existente
# 2. Leia brand_config.yaml + dados complementares
# 3. Substitua TODOS os {{PLACEHOLDERS}} por dados reais
# 4. Verifique que ZERO {{}} restam
# 5. Salve o arquivo (SOBRESCREVER o template)
# 6. Commit:
git add N06_commercial/output/output_brand_book.md && git commit -m "[N06] brand book GATO³ — 34 blocos hidratados" --no-verify
git add N06_commercial/output/output_brand_voice_guide.md && git commit -m "[N06] voice guide GATO³ — radar 5D + Ro" --no-verify
git add N06_commercial/output/output_visual_identity.md && git commit -m "[N06] visual identity GATO³ — paleta PB" --no-verify
git add N06_commercial/output/output_discovery_report.md && git commit -m "[N06] discovery report GATO³ — mercado pet ABC" --no-verify
git add N06_commercial/output/output_brand_one_pager.md && git commit -m "[N06] one pager B2B GATO³" --no-verify
git add N06_commercial/output/output_transformation_arc.md && git commit -m "[N06] transformation arc GATO³" --no-verify

# Depois de TODOS os 6:
python _tools/signal_writer.py n06 complete 9.0 BRAND_GATO3
```

## Regras

1. **SOBRESCREVER os templates** — não crie arquivos novos em outros pilares
2. **ZERO `{{placeholders}}`** no output final — tudo dados reais GATO³
3. **Frontmatter**: kind: brand_book (não output_template), quality: null
4. **pt-BR** — tudo em português brasileiro
5. **quality: null** — NUNCA se auto-avalie
6. **Dados > invenção** — use os docs do repo, não invente
