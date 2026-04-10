---
id: ux_conversion_audit_gato3_20260410
kind: scoring_rubric
pillar: P07
title: "UX & Conversion Audit -- gato3.com.br"
version: 1.0.0
date: 2026-04-10
nucleus: N02
quality: null
tags: [audit, ux, conversion, brand, gato3, marketing]
---

# UX & Conversion Audit — gato3.com.br

**Auditor**: N02 Marketing Nucleus (Luxuria Criativa)
**Date**: 2026-04-10
**Method**: Source code deep-read (SPA — WebFetch cannot render client-side React)
**Scope**: 8 pages, 2 repos (`gato-cubo-commerce` + `fresh-start`), 12 blog posts, 1 AI chat component
**Brand baseline**: `.cex/brand/brand_config.yaml` (Caregiver archetype, sofisticado-acolhedor voice)

---

## Executive Summary

GATO3 has a **surprisingly mature e-commerce foundation** for a young brand. The product detail pages are genuinely best-in-class for Brazilian pet e-commerce — benefit tabs, usage guides, vet-validated copy, and an AI chat assistant that recommends products contextually. The B2B program is well-structured with clear onboarding and margin transparency.

**But the site is leaving money on the table.** The biggest conversion killers are:

1. **The homepage hero sells features, not desire** — "Produtos inteligentes que harmonizam" is informative but doesn't make anyone's pulse quicken
2. **Zero social proof anywhere** — no reviews, no testimonials, no user photos, no "X tutores confiam"
3. **Blog is visually orphaned** — completely different design system (amber/orange), breaking brand trust
4. **No urgency or scarcity signals** — the only scarcity is "Ultimas unidades" on low-stock items
5. **Newsletter capture is buried** — only in footer, with the weakest possible hook ("dicas e ofertas")

**Overall site score: 7.2/10** — Solid architecture, weak persuasion layer.

---

## Page-by-Page Scoring

| Page | Copy Quality | CTA Effectiveness | Brand Consistency | Conversion Potential | Overall |
|------|:-----------:|:-----------------:|:-----------------:|:-------------------:|:-------:|
| Homepage (B2C) | 7 | 7 | 8 | 6 | **7.0** |
| Catalog | 6 | 7 | 9 | 7 | **7.3** |
| Product Detail | 9 | 8 | 9 | 8 | **8.5** |
| SAC / Ronronalda | 8 | 7 | 7 | 8 | **7.5** |
| B2B | 8 | 8 | 8 | 8 | **8.0** |
| About | 5 | 5 | 7 | 4 | **5.3** |
| Blog | 7 | 5 | 3 | 5 | **5.0** |
| Footer / Cross-cutting | 7 | 6 | 8 | 6 | **6.8** |

---

## 1. Homepage (`/b2c`) — Score: 7.0/10

### What Works
- **Hero headline is clear**: "Seu gato mais feliz. Sua casa mais bonita." — Directly addresses both ICP desires (cat wellbeing + home aesthetics). The dual-benefit structure is on-brand.
- **6 pillars section is strong**: "Curadoria Veterinaria", "Design Minimalista", "Preco Justo" — these are real differentiators, not fluff.
- **FAQ is excellent**: 6 questions that match real purchase objections (materials safety, sizing, returns, shipping, payment). This is conversion-aware copywriting.
- **Final CTA routes to Ronronalda**: Smart — turns exit intent into engagement.
- **Accessibility**: Skip links, ARIA labels, min-height touch targets (48px). Above average for Brazilian e-commerce.

### What Bleeds Revenue
- **Hero subtitle is feature-speak**: "Produtos inteligentes que harmonizam bem-estar felino e design de interiores" — this reads like a product brief, not a desire trigger. The ICP doesn't search for "harmonizar design de interiores". They search for "meu gato ta estressado" or "arranhador bonito".
- **Hero description undersells**: "Camas, brinquedos e acessorios validados por veterinarios comportamentalistas, enviados para todo o Brasil" — listing product categories in the hero is wasted real estate. The vet validation is the HOOK — it should lead, not follow.
- **No social proof above the fold**: Zero reviews, zero testimonials, zero "X tutores confiam na GATO3". For an unknown brand, this is the #1 conversion killer.
- **Product carousel has no headline**: The products section renders without a visible title or editorial curation signal. It feels like a Shopify default, not a curated experience.
- **No urgency**: No seasonal messaging, no limited editions, no countdown. The page is timeless — which means forgettable.

### Recommended Rewrites

**Hero subtitle** (current):
> "Produtos inteligentes que harmonizam bem-estar felino e design de interiores."

**Proposed**:
> "Cada produto validado por veterinarios comportamentalistas. Cada detalhe pensado para desaparecer na sua decoracao."

**Hero description** (current):
> "Camas, brinquedos e acessorios validados por veterinarios comportamentalistas, enviados para todo o Brasil."

**Proposed**:
> "Seu gato merece mais que o generico da pet shop. E voce merece mais que moveis feios na sala. Frete gratis acima de R$ 299."

---

## 2. Catalog (`/catalogo`) — Score: 7.3/10

### What Works
- **Filters are well-designed**: Price ranges (Ate R$50, R$50-100, R$100-200, R$200+), stock toggle, sort options. Mobile-responsive with collapsible panel.
- **Active filter badges**: Removable pills showing current filters — excellent UX pattern.
- **Empty state is handled**: "Nenhum produto encontrado com esses filtros" + clear filter button. No dead ends.
- **Results count**: "{N} produtos encontrados" — sets expectations.
- **Loading skeletons**: Proper skeleton cards instead of spinners. Professional.

### What Bleeds Revenue
- **Page headline is dead**: "Catalogo GATO3" — tells you nothing. Why should I browse? What makes this catalog different from Petlove or Petz?
- **Subheadline is generic**: "Design minimalista e funcionalidade para o bem-estar do seu gato" — this could be any pet brand.
- **No categories**: Everything is a flat grid. No "Camas", "Arranhadores", "Brinquedos" navigation. For a growing catalog, this becomes unusable fast.
- **No "bestseller" or "novo" badges**: The only badge is "ESGOTADO" (out of stock). No positive urgency signals.
- **Product card CTA says "Comprar" but links to cart**: The `ProductCard` has "Comprar" (add to cart) + "Detalhes" side by side. "Comprar" without seeing the full product page is aggressive for this price range. The ICP needs education before purchase.
- **No price anchoring**: No crossed-out original prices, no "Economize X%", no comparison to pet shop prices.

### Recommended Rewrites

**Headline** (current):
> "Catalogo GATO3"

**Proposed**:
> "Curadoria completa — cada produto aprovado por veterinarios"

**Subheadline** (current):
> "Design minimalista e funcionalidade para o bem-estar do seu gato"

**Proposed**:
> "Sem generico, sem exagero. So o que funciona de verdade."

---

## 3. Product Detail (`/produtos/{slug}`) — Score: 8.5/10

### What Works — This is the site's crown jewel
- **Benefit tabs (Functional + Emotional)**: Splitting benefits into "Funcionais" and "Emocionais" is brilliant. The ICP buys emotionally and justifies rationally. This structure serves both modes.
- **"Por que funciona" section**: Explaining the science behind the product (vet validation) is exactly what the Caregiver archetype demands.
- **Usage guide with numbered steps**: Reduces post-purchase anxiety. Shows the brand cares about adoption, not just sale.
- **Box contents**: "O que vem na caixa" — eliminates a common purchase objection.
- **Care instructions**: Extends product lifetime = higher satisfaction = more repeat purchases.
- **Warranty section**: Highlighted in a special card with brand accent. Trust signal.
- **Product FAQ**: Per-product FAQ with accordion. Addresses product-specific objections.
- **Related products carousel**: Cross-sell is present and functional.
- **Dual CTA**: "Adicionar ao Carrinho" + "Chat com a Ronronalda" — buy OR get help. No dead end.
- **GA4 tracking**: `view_item` and `add_to_cart` events. Data-driven.
- **SEO**: Product schema JSON-LD, custom SEO fields per product, breadcrumbs.
- **Media Kit for B2B**: Product pages double as B2B showcase with downloadable assets. Efficient.

### What Bleeds Revenue
- **No reviews or ratings**: This is the ONLY major gap. A product page this well-structured without social proof is like a five-star restaurant with no diners — the empty tables make you suspicious.
- **No "X people are viewing this" or "Y sold this week"**: Social proof and urgency are both absent.
- **Specifications section could show more context**: "Dimensoes: 50x40cm" means nothing without "Ideal para gatos ate 6kg" next to it.
- **No comparison table**: For a curated catalog, showing "Why this vs. that" would increase confidence and reduce SAC load.
- **"Indisponivel" CTA is a dead end**: When out of stock, there's no "Avise-me quando voltar" email capture. Lost lead.

### Recommended Addition
Add a review/social proof section above the fold. Even curated testimonials from WhatsApp conversations (with permission) would work. Structure:
```
"Comprei o Donut e meu gato dormiu 3 horas direto no primeiro dia." — Ana P., Sao Paulo
```

---

## 4. SAC / Ronronalda (`/sac`) — Score: 7.5/10

### What Works
- **Personality is present**: Cat emoji avatar, "Online" status, WhatsApp-style UI. The chat feels alive, not corporate.
- **Suggestion chips are excellent**: "Arranha o sofa", "Xixi fora da caixa", "Vomita apos comer" — these are EXACTLY the questions the ICP has. Whoever wrote these knows the audience.
- **Product recommendations in chat**: Ronronalda recommends products contextually with pricing, images, and "Ver detalhes" links. This is conversational commerce done right.
- **Structured steps**: Responses include numbered action steps in a card format. Actionable, not vague.
- **Text-to-speech**: Users can listen to responses. Accessibility win + novelty factor.
- **Voice input**: Speech recognition for hands-free chat. Premium feature.
- **WhatsApp fallback**: When API is down, a green button routes to WhatsApp. No dead end.

### What Bleeds Revenue
- **Medical disclaimer is visually loud**: The amber alert at the top ("Em casos de dor, sangue ou apatia, procure um veterinario") is necessary but it's the FIRST thing the user sees. It sets a clinical tone before the warm chat begins.
- **No Ronronalda personality intro**: The chat opens with a system message but there's no warm welcome like "Oi! Eu sou a Ronronalda, sua mentora felina. Me conta — o que ta acontecendo com o seu gatinho?"
- **Chat-to-cart friction**: Product recommendations link to product pages, not directly to cart. For high-intent moments ("Qual cama devo comprar?"), one extra click = drop-off.
- **No conversation history persistence**: `clearMessages` wipes everything. If the user navigates away and comes back, they lose context. This kills multi-session purchase journeys.
- **Blog header mismatch**: The SAC page uses `HeaderSimple` while the rest of the site uses `Header`. The navigation break is subtle but disorienting.

### Recommended Copy
**Welcome message** (add as initial assistant message):
> "Oi! Sou a Ronronalda, especialista em comportamento felino. Pode me contar o que esta acontecendo — eu te ajudo a entender e a encontrar a solucao certa."

---

## 5. B2B (`/b2b`) — Score: 8.0/10

### What Works
- **Hero headline is magnetic**: "Margem, narrativa e vitrine — para negocios que amam gatos" — this speaks DIRECTLY to what a pet shop owner wants. Three concrete benefits in one line.
- **"Programa Exclusivo para Parceiros" badge**: Creates exclusivity perception before the pitch.
- **24% discount transparency**: "Cadastre-se com seu CNPJ e tenha acesso imediato ao catalogo B2B com 24% de desconto" — concrete, specific, compelling.
- **Affiliate program for non-CNPJ**: "Nao tem CNPJ? Seja Afiliado!" — catches the spillover audience. Smart.
- **6-step onboarding timeline**: Visual with connecting line and step numbers. Reduces "how does this work?" anxiety.
- **Governance language**: "Cadencia mensal de governanca", "rituais de performance" — signals professionalism to business buyers.
- **Margin transparency**: "Margem sugerida de 40% a 60%" — this is the information B2B buyers need first.

### What Bleeds Revenue
- **No partner testimonials**: "Join our program" without "Here's what existing partners say" is weak proof.
- **No partner count**: "Junte-se a X parceiros em Y cidades" would add social proof.
- **B2B footer is separate and minimal**: Different footer from the main site. Feels disconnected.
- **Copyright says 2025**: `&copy; 2025 GATO3` — should be dynamic. Small but signals neglect.
- **No sample margin calculator**: Showing "Buy at R$X, sell at R$Y, pocket R$Z per unit" would make the value proposition tangible.

---

## 6. About (`/sobre`) — Score: 5.3/10

### What Works
- **Values are concise**: Educacao, Design, Bem-estar — three words that capture the brand.
- **Ro section**: Introducing the AI assistant on the About page is a smart brand-building move.
- **"Onde Encontrar" section**: Lists all channels (Mercado Livre, Shopee, site). Practical.

### What Bleeds Revenue
- **Brand story is anemic**: "A GATO3 nasceu da observacao de que o mercado pet brasileiro tinha muitos produtos genericos..." — this reads like a business plan executive summary, not a brand story. Where's the founder? Where's the emotion? Where's the cat that started it all?
- **No founder presence**: The brand config has a detailed brand story about "tres dimensoes" and vet validation, but this page strips all the richness away into a dry paragraph.
- **No photos**: An About page without a single image of a real cat, a real product, or a real person. This is the page where trust is built — and it's all text.
- **Accent-stripped copy**: "Educacao" instead of "Educacao" (likely sanitized for ASCII safety but visible to users). Multiple instances: "Historia", "duvidas", etc.
- **No team, no CNPJ, no address on this page**: Trust signals that should be HERE are only in the footer.

### Recommended Rewrite

**Brand story** (current):
> "A GATO3 nasceu da observacao de que o mercado pet brasileiro tinha muitos produtos genericos e poucos que equilibravam design, funcionalidade e o real bem-estar do gato."

**Proposed**:
> "Tudo comecou com uma pergunta simples: por que produtos para gatos precisam ser feios? A GATO3 nasceu da recusa em aceitar o generico. Cada produto no nosso catalogo passa por veterinarios comportamentalistas antes de chegar ate voce. Porque o seu gato merece mais que 'serve'. E a sua casa tambem."

---

## 7. Blog (`/blog`) — Score: 5.0/10

### What Works
- **Content quality is high**: 12 posts covering behavior, science, products, trends. Sources cited (Journal of Feline Medicine, Scientific American, Cornell). This is real educational content, not SEO filler.
- **Category system**: 5 categories with icons. Filterable. Searchable.
- **Reading time and dates**: Sets expectations. Professional.
- **Featured posts**: 3 highlighted articles. Editorial curation.

### What Bleeds Revenue — THE BIGGEST BRAND CONSISTENCY FAILURE
- **Completely different visual identity**: The blog uses `bg-gradient-to-b from-amber-50 to-white`, amber/orange color scheme, and a different header. The main site is PB minimalista (black/white). The blog looks like it belongs to a DIFFERENT BRAND.
- **Different header**: Uses its own inline header with `<Cat className="h-8 w-8 text-amber-600" />` and amber-900 text instead of the site's `<Header />` component. A user navigating from the catalog to the blog will feel lost.
- **Different footer**: `<footer className="bg-gray-900 text-white py-8">` — one line of text. The main footer has 4 columns with newsletter, social, trust signals. The blog footer has none of this.
- **No product integration in posts**: Blog posts about "tapete gelado" or "fonte de agua" don't link to actual products in the catalog. This is the #1 missed conversion opportunity — educational content that creates desire but doesn't offer the solution.
- **Instagram CTA uses gradient button**: `bg-gradient-to-r from-pink-500 to-purple-500` — Instagram-colored, not brand-colored. This is the only place on the site with pink/purple.
- **No newsletter capture on blog**: The main site footer has newsletter. The blog doesn't. Blog readers are the HIGHEST intent audience for email capture.

### Critical Fix
The blog MUST use `<Header variant="b2c" />` and `<Footer variant="b2c" />` from the main site. The amber color scheme must be replaced with the brand's PB palette. This is non-negotiable for brand coherence.

---

## 8. Cross-Cutting Conversion Analysis — Score: 6.8/10

### Navigation & Friction Map

```
Landing (B2C) → Catalogo → Produto → Carrinho → Checkout (Shopify)
     2 clicks to product page
     3 clicks to cart
     4 clicks to checkout (redirects to Shopify)
```

**Verdict**: Acceptable funnel length. The Shopify redirect at checkout is standard but creates a moment of doubt ("am I still on GATO3?").

### Newsletter Capture
- **Location**: Footer only (all pages except Blog)
- **Hook**: "Receba dicas de bem-estar felino e ofertas exclusivas"
- **Grade**: D — Generic hook, buried placement. No lead magnet, no discount incentive, no popup.
- **Fix**: Add a "Guia gratuito: 7 sinais de estresse felino" lead magnet with exit-intent popup.

### Social Proof
- **Reviews**: ZERO anywhere on the site
- **Testimonials**: ZERO
- **User photos**: ZERO
- **Trust badges**: Only "Compra Segura | Pagamento via Shopify" in footer
- **Grade**: F — This is the site's most critical gap

### Urgency/Scarcity
- **Stock signals**: "Ultimas unidades" badge when quantity <= 5
- **Limited editions**: None
- **Seasonal**: None
- **Countdown**: None
- **Grade**: D — Only reactive scarcity (low stock), no proactive urgency

### Mobile Experience
- **Touch targets**: min-h-[48px] on all interactive elements. WCAG compliant.
- **Mobile menu**: Hamburger with focus trap and Escape key handling. Excellent.
- **Carousel navigation**: Dot indicators on mobile, arrows on desktop. Good.
- **Product cards**: Full-width on mobile, 2-col on tablet, 3-col on desktop. Responsive.
- **Grade**: A — Mobile UX is well-executed

### Footer Trust Signals
- **CNPJ**: Present (51.765.687/0001-97)
- **Security badge**: "Compra Segura" with ShieldCheck icon
- **Payment**: "Pagamento via Shopify"
- **Social links**: Instagram, YouTube, Facebook, WhatsApp
- **Contact**: WhatsApp number displayed
- **Marketplace links**: Mercado Livre, Shopee
- **Legal**: Privacy Policy, Terms of Use
- **Grade**: B+ — All essentials present. Missing: SSL badge, payment method icons (Visa, Mastercard, Pix).

---

## TOP 5 QUICK WINS (highest impact, lowest effort)

| # | Fix | Impact | Effort | Page |
|---|-----|--------|--------|------|
| 1 | **Add 5-10 curated reviews** (from WhatsApp conversations or Mercado Livre) to product pages | Critical | Low — create a `reviews` array in product data | Product Detail |
| 2 | **Replace blog header/footer** with site-wide `<Header>` and `<Footer>` components | High — brand trust | Low — 2 import changes | Blog |
| 3 | **Add "Avise-me" email capture** on out-of-stock products | High — captures leads | Low — form + Supabase insert | Product Detail |
| 4 | **Add welcome message to Ronronalda** chat | Medium — sets tone | Trivial — 1 line in initial messages | SAC |
| 5 | **Update B2B copyright to dynamic year** | Low but signals care | Trivial — `{new Date().getFullYear()}` | B2B |

## TOP 5 STRATEGIC IMPROVEMENTS (high impact, more effort)

| # | Improvement | Impact | Effort | Scope |
|---|-------------|--------|--------|-------|
| 1 | **Social proof system**: Reviews, ratings, "X vendidos", user photo gallery | Critical — the #1 conversion blocker | Medium — DB schema + UI components + collection workflow | Sitewide |
| 2 | **Blog visual alignment**: Replace amber palette with PB minimalista. Add product cross-links in educational posts | High — brand coherence + content commerce | Medium — CSS overhaul + product linking logic | Blog |
| 3 | **Newsletter lead magnet**: Exit-intent popup with free guide ("7 sinais de estresse felino" PDF) + 10% first purchase discount | High — email list = owned audience | Medium — popup component + PDF + Supabase flow | Sitewide |
| 4 | **Product categories in catalog**: Add category tabs or sidebar (Camas, Arranhadores, Brinquedos, Acessorios) | Medium — improves discovery as catalog grows | Medium — category taxonomy + filter UI | Catalog |
| 5 | **Rewrite About page**: Founder story with photos, mission statement from brand_config.yaml, team section, timeline | Medium — builds trust for unknown brand | Medium — content creation + photo sourcing | About |

---

## Brand Voice Consistency Audit

| Criterion | Target (brand_config) | Actual (site) | Verdict |
|-----------|----------------------|---------------|---------|
| Tone: sofisticado-acolhedor | Warm + sophisticated | Mostly achieved except About (dry) and Blog (casual/amber) | 7/10 |
| Formality: 3/5 | Balanced | Consistent across B2C pages | 8/10 |
| Warmth: 4/5 | High warmth | Strong in Ronronalda, FAQ, product pages. Weak in About, Catalog headline | 7/10 |
| "Explicar o porque" | Science-backed education | Excellent in blog and product pages ("Por que funciona") | 9/10 |
| "Tratar tutor como parceiro" | No condescension | Consistent — language is respectful throughout | 9/10 |
| "Nunca prometer milagres" | No overclaiming | Clean — no false promises anywhere | 10/10 |
| "Sem CAPS LOCK ou emoji excessivo" | Restrained | Almost perfect — blog CTA has Instagram gradient that breaks this | 8/10 |
| Visual: PB minimalista | Black/white, Allrounder + Kenao | Perfect on B2C, Catalog, Product, B2B. Blog breaks this completely | 6/10 |

**Overall brand consistency: 8.0/10** (dragged down by Blog's visual divorce)

---

## Conversion Funnel Heatmap

```
STAGE          SCORE   NOTES
Awareness      7/10    SEO is solid. Blog content is quality. Social channels linked.
Interest       6/10    Hero creates interest but doesn't CREATE DESIRE. No social proof.
Desire         8/10    Product pages are exceptional. Benefits, science, usage guides.
Action         7/10    Cart works. Dual CTA (buy + chat). But no urgency, no reviews.
Retention      5/10    Newsletter is weak. No post-purchase sequence visible. No loyalty program.
Referral       3/10    No referral program. No "share with a friend". No UGC.
```

---

## Final Verdict

GATO3 has built a **technically excellent e-commerce site** with a **genuinely differentiated product page experience**. The combination of vet-validated products, benefit-driven copy, AI chat assistant, and B2B transparency is rare in Brazilian pet e-commerce.

**The site's architecture is a 9. Its persuasion layer is a 6.**

The gap between "informing" and "converting" is where the money lives. Adding social proof, fixing the blog's visual identity, and strengthening the newsletter capture would move the overall score from 7.2 to 8.5+ within 30 days.

The brand voice is consistent where it matters most (product pages, FAQ, Ronronalda). The About page and Blog are the weak links — and they're the cheapest to fix.

---

*Report generated by N02 Marketing Nucleus | 8F Pipeline | 2026-04-10*
*Source: gato-cubo-commerce repo (React/TypeScript/Lovable) + brand_config.yaml*
*Method: Source code analysis (SPA cannot be crawled via WebFetch)*
