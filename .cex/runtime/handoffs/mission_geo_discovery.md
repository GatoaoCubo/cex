# Mission: Geo Discovery Builder
**Superintendent**: N01 (Intelligence) | **Consumers**: N02 (Marketing), N06 (Commercial)
**Source**: codexa-core discovery & research stack (~3,745 lines production Python)
**Goal**: Distill entity resolution, marketplace search, grounded search, and context filtering into a reusable geo-discovery-builder

## Source Systems (codexa-core/api/core/)

| File | Lines | Domain |
|------|-------|--------|
| entity_resolver.py | 934 | 4-stage pipeline: NORMALIZE→BLOCK→MATCH→MERGE. Palantir-style cross-marketplace entity resolution |
| anuncio_synthesizer.py | 1586 | V5 sequential chain: titles, keywords, bullets, description, FAQs for BR marketplaces |
| compliance_checker.py | 410 | Policy validation, marketplace rules, content compliance |
| context_filter.py | 339 | Embedding-based chunking + MMR diversity selection + token budget enforcement |
| meli_client.py | 303 | MercadoLivre public API client: search, trends, category browsing (free, 1500 req/min) |
| gemini_search_client.py | 173 | Gemini with Search Grounding: outbound social intelligence (~$0.014/query) |
| **Total** | **3,745** | **End-to-end geo-aware market discovery** |

## Additional Sources
- `gato-cubo-commerce/` — E-commerce frontend with product discovery UX
- Existing research-pipeline-builder at `archetypes/builders/research-pipeline-builder/`
- N01 nucleus artifacts (20 existing, avg 8.80)
- Research pipeline examples in `P04_tools/examples/ex_research_pipeline_*.md` (4 verticals)

## Architecture: 5 Layers

### Layer 1: Knowledge Cards (N01 superintendent, N04 executes)
Platform KCs to create in `P01_knowledge/library/platform/`:
1. `kc_entity_resolution` — Blocking, matching, merging, Palantir ontology pattern
2. `kc_marketplace_apis` — MeLi, Shopee, Amazon BR: endpoints, rate limits, auth
3. `kc_gemini_grounding` — Search grounding, cost model, source attribution
4. `kc_mmr_diversity` — Maximal Marginal Relevance, embedding chunking, token budgets
5. `kc_br_ecommerce_taxonomy` — Brazilian marketplace categories, stop words, normalization
6. `kc_content_synthesis` — Sequential chain generation, zero-fabrication, marketplace copywriting

### Layer 2: Builder ISOs (N01 defines, N03 creates)
New builder: `archetypes/builders/geo-discovery-builder/` (14 ISOs)
Pipeline: INTENT→SOURCES→SEARCH→RESOLVE→FILTER→SYNTHESIZE→VALIDATE→DELIVER

### Layer 3: Nucleus Artifacts (N01)
- `N01_intelligence/knowledge/knowledge_card_geo_discovery.md`
- `N01_intelligence/tools/geo_discovery_tool.md`
- `N01_intelligence/orchestration/dispatch_rule_geo_discovery.md`
- `N01_intelligence/orchestration/workflow_geo_discovery.md`

### Layer 4: Templates + Examples (P04)
- `P04_tools/templates/tpl_geo_discovery.md`
- `P04_tools/examples/ex_geo_discovery_pet_shop.md` (local pet market)
- `P04_tools/examples/ex_geo_discovery_cosmetics.md` (skincare BR)
- `P04_tools/examples/ex_geo_discovery_food_delivery.md` (local food market)

### Layer 5: Instance Config
- `_instances/codexa/N01_intelligence/geo_discovery_config.md`

## Phases (DAG)

### Phase 1: Scrape (N07 does, 30min)
Read all 6 source files from codexa-core. Extract patterns, schemas, pipeline stages.
Output: Raw notes in session checkpoint.

### Phase 2: Knowledge Cards (N01 superintends → dispatch to N04, 2h)
Create 6 platform KCs. Each KC follows `kc_*` template.
Deps: Phase 1.

### Phase 3: Builder ISOs (N01 superintends → dispatch to N03, 2h)
Create 14 ISOs for geo-discovery-builder. Leverage existing research-pipeline-builder as reference.
Deps: Phase 2.

### Phase 4: Nucleus Artifacts + Templates (N01 executes, 1h)
Create N01 nucleus artifacts + P04 templates + examples.
Deps: Phase 3.

### Phase 5: Instance + Compile + Score (N07 consolidates, 30min)
Create instance config, compile all, score, commit.
Deps: Phase 4.

## Expected Output
- 6 platform KCs (avg 8.8+)
- 14 builder ISOs (all ≤4096B, density ≥0.78)
- 4 N01 nucleus artifacts
- 1 template + 3 examples
- 1 instance config
- 1 sub-agent `.claude/agents/geo-discovery-builder.md`
- **Total: ~29 artifacts**

## Key Patterns to Distill
1. **4-stage entity resolution**: NORMALIZE→BLOCK→MATCH→MERGE (from entity_resolver.py)
2. **Token budget enforcement**: MMR + embedding scoring (from context_filter.py)
3. **Zero-fabrication**: Generate content ONLY from provided data (from anuncio_synthesizer.py)
4. **Multi-source grounding**: MeLi API + Gemini Search + scrapers (from meli_client + gemini_search_client)
5. **BR-specific NLP**: Stop words, normalization, Portuguese-specific patterns (from entity_resolver.py)

## Differentiation from Research Pipeline
The existing research-pipeline-builder is GENERIC research. This builder is SPECIFIC to:
- Geo-aware market discovery (city/region/state level)
- Cross-marketplace entity resolution (same product across MeLi, Shopee, Amazon)
- Local business intelligence (nearby competitors, regional pricing)
- BR e-commerce patterns (CNPJ, CEP, frete, PIX discounts)

## Success Criteria
- [ ] All 29 artifacts pass compile
- [ ] Doctor: 0 FAIL
- [ ] Quality avg ≥ 8.7
- [ ] Builder covers all 6 source files (nothing lost)
- [ ] Entity resolution pipeline is fully abstracted (no codexa hardcodes)
- [ ] Works for any Brazilian city/vertical, not just pet/cosmetics

## Constraints
- All artifacts must be company-agnostic (use [PLACEHOLDERS])
- MeLi client is FREE — builder should prefer free APIs over paid
- Gemini grounding cost ($0.014/query) must be documented in rate_limit config
- Entity resolution must handle Portuguese text (accents, stop words, normalization)
