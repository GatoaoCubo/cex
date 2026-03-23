# ADW: PESQUISA ORCHESTRATOR v3.0

## PURPOSE
Sequential 4-HOP pipeline: queries -> search -> competitors -> SEO -> 22-block output

## IDENTITY
```yaml
workflow: pesquisa_orchestrator
type: sequential
satellite: SHAKA
output: research_notes.md (22 blocks)
downstream: anuncio -> photo -> ads
```

---

## INPUT
```yaml
required:
  product_name: string
  category: string

optional:
  target_audience: string
  price_range: string
  known_attributes: array
  marketplaces: array  # default: all 9
```

---

## 4-STEP PIPELINE

```
INPUT
  |
  v
[STEP 1: QUERY GENERATION]
  HOP: prompts/query_generation.md
  IN: product_name, category, known_attributes
  OUT: head_terms[15], longtails[30-50], synonyms
  |
  v
[STEP 2: MARKETPLACE SEARCH]
  HOP: prompts/marketplace_search.md
  IN: head_terms, longtails, marketplaces
  OUT: search_results, queries_log[20+], patterns
  |
  v
[STEP 3: COMPETITOR ANALYSIS]
  HOP: 17_HOP_competitor_analysis.md
  IN: search_results
  OUT: profiles[3-5], benchmark, gaps, opportunities
  |
  v
[STEP 4: SEO TAXONOMY]
  HOP: prompts/seo_taxonomy.md
  IN: queries, search_results, competitor_data
  OUT: seo_inbound, seo_outbound, compliance, RA_data
  |
  v
OUTPUT: 22-block research_notes.md
```

---

## STEP SPECS

### Step 1: Query Generation
```yaml
hop: prompts/query_generation.md
priority: critical
validation:
  head_terms: [10, 15]
  longtails: [30, 50]
on_fail: retry(2)
feeds: Block 4-5
```

### Step 2: Marketplace Search
```yaml
hop: prompts/marketplace_search.md
priority: critical
validation:
  queries_logged: ">=15"
  marketplaces: ">=3"
  results: ">=30"
on_fail: retry_different_mp(3)
feeds: Block 6
```

### Step 3: Competitor Analysis
```yaml
hop: 17_HOP_competitor_analysis.md
priority: high
validation:
  competitors: [3, 5]
  benchmark: complete
  gaps: identified
on_fail: retry(2)
feeds: "Block 15-19, Appendice A"
```

### Step 4: SEO Taxonomy
```yaml
hop: prompts/seo_taxonomy.md
priority: high
validation:
  ra_checked: true
  compliance: [ANVISA, INMETRO, CONAR]
  category_paths: ">=3"
on_fail: retry(2)
feeds: "Block 7, 14, 21"
```

---

## OUTPUT MAPPING

| Step | HOP | Output Blocks |
|------|-----|---------------|
| 1 | query_generation.md | 4 (Head), 5 (Longtails) |
| 2 | marketplace_search.md | 6 (Inbound) |
| 3 | 17_HOP_competitor | 15-19 (Competitors), Appendice A |
| 4 | seo_taxonomy.md | 7 (Outbound), 14 (RA), 21 (Compliance) |
| Synthesis | All | 1-3, 8-13, 20, 22 |

---

## QUALITY GATES

| Gate | Threshold |
|------|-----------|
| Queries | >=15 logged + URLs |
| Competitors | >=3 analyzed |
| Marketplaces | >=3 searched |
| Confidence | >=0.75 |
| Blocks | 22/22 |

**PASS**: all gates met
**WARN**: 1 gate missed
**FAIL**: 2+ gates missed

---

## HANDOFF FORMAT

### -> anuncio_agent
```yaml
product_name | category | price_positioning
head_terms[] | longtails[] | synonyms{}
pain_points[] | desired_gains[]
competitor_avg_rating | compliance_notes
unique_selling_points[]
```

### -> photo_agent
```yaml
product_name | product_attributes[]
critical_details[] | competitor_visual_patterns[]
suggested_angles[]
```

---

## INVOCATION

```markdown
# Minimal
Produto: Garrafa Termica Premium
Categoria: Casa e Cozinha > Garrafas

# Full
Produto: Garrafa Termica Premium 500ml Inox
Categoria: Casa e Cozinha > Garrafas
Publico: Pessoas ativas 25-45
Preco: R$ 70 - R$ 120
Atributos: 500ml, inox 304, dupla parede
Marketplaces: ML, Shopee, Amazon
```

---

**v3.0** | Information-Dense | 4-HOP Sequential Pipeline
