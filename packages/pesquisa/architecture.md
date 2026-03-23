# ARCHITECTURE | pesquisa_agent v2.1.0

**Version**: 2.1.0 | **Date**: 2025-12-17
**Pattern**: HORIZONTAL AGENT (s0-s6)

---

## System Architecture

```
+---------------------------------------------------------------------------+
|                        pesquisa_agent v2.1.0                              |
|                     HORIZONTAL AGENT ARCHITECTURE                         |
+---------------------------------------------------------------------------+
|                                                                           |
|                         +-----------------+                               |
|                         |   s0/pesquisa   |                               |
|                         | (Router Agent)  |                               |
|                         +--------+--------+                               |
|                                  |                                        |
|            +----------+----------+-----------+---------+                  |
|            |          |          |           |         |                  |
|       +----v----+ +---v-----+ +--v------+ +--v----+ +--v------+          |
|       | s1/ml   | |s2/shopee| |s3/amazon| |s4/serp| |s5/social|          |
|       |(ML Spec)| |(Shopee) | |(Amazon) | |(Google)| |(TikTok) |          |
|       +----+----+ +----+----+ +----+----+ +---+---+ +----+----+          |
|            |           |           |          |          |                |
|            +-----------+------+----+----------+----------+                |
|                               |                                           |
|                               v                                           |
|                     +---------------------+                               |
|                     |   s6/synthesis      |                               |
|                     |   (Aggregator)      |                               |
|                     +---------+-----------+                               |
|                               |                                           |
|                               v                                           |
|                  +------------------------+                               |
|                  |  22-Block Research     |                               |
|                  |       Notes            |                               |
|                  +------------+-----------+                               |
|                               |                                           |
|                     +---------+---------+                                 |
|                     v                   v                                 |
|             +--------------+    +--------------+                          |
|             |   anuncio    |    |    photo     |                          |
|             |   (handoff)  |    |   (handoff)  |                          |
|             +--------------+    +--------------+                          |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

## Phase Diagram (9-Phase Research Flow)

```
+---------------------------------------------------------------------------+
|                         9-PHASE RESEARCH FLOW                             |
+---------------------------------------------------------------------------+
|                                                                           |
|  PHASE 1         PHASE 2          PHASE 3          PHASE 4               |
|  +--------+     +----------+     +----------+     +----------+           |
|  | INPUT  |---->|  PARSE   |---->|  QUERY   |---->| SEARCH   |           |
|  |Validate|     |  Brief   |     |Generation|     |(Parallel)|           |
|  +--------+     +----------+     +----------+     +----------+           |
|                                                         |                 |
|  +------------------------------------------------------+                 |
|  |                                                                        |
|  v                                                                        |
|  PHASE 5         PHASE 6          PHASE 7          PHASE 8               |
|  +----------+   +----------+     +----------+     +----------+           |
|  |COMPETITOR|-->|  PRICE   |---->|   GAP    |---->|   SEO    |           |
|  | Analysis |   |Comparison|     |  Ident   |     | Taxonomy |           |
|  +----------+   +----------+     +----------+     +----------+           |
|                                                         |                 |
|  +------------------------------------------------------+                 |
|  |                                                                        |
|  v                                                                        |
|  PHASE 9                                                                  |
|  +------------------------------------------------------+                 |
|  |               QA VALIDATION & OUTPUT                 |                 |
|  |                                                      |                 |
|  |  +---------+   +---------+   +---------------------+|                 |
|  |  | Score   |-->| >= 7.0? |-->|   OUTPUT ASSEMBLY   ||                 |
|  |  |Calculate|   +----+----+   |  22 Blocks + Handoff||                 |
|  |  +---------+        |        +---------------------+|                 |
|  |                 NO  |  YES                          |                 |
|  |               +-----+-----+                         |                 |
|  |               |   RETRY   |                         |                 |
|  |               |   LOOP    |                         |                 |
|  |               +-----------+                         |                 |
|  +------------------------------------------------------+                 |
|                                                                           |
+---------------------------------------------------------------------------+
```

---

## Data Flow Diagram

### Input Layer

```
+--------------------------------------------------------------+
|                      INPUT SOURCES                            |
+--------------------------------------------------------------+
|                                                               |
|  user_brief ----------> manual_input ------+                  |
|                         (confidence: 0.65) |                  |
|                                            |                  |
|  product_url ----------> scraped_data -----+---> {$INPUT}    |
|                          (confidence: 0.80)|                  |
|                                            |                  |
|  marca_agent ----------> brand_voice ------+                  |
|                          (confidence: 0.90)                   |
|                                                               |
+--------------------------------------------------------------+
```

### Processing Layer

```
+--------------------------------------------------------------+
|                   PROCESSING PIPELINE                         |
+--------------------------------------------------------------+
|                                                               |
|  prompts/orchestrator.md                                      |
|       |                                                       |
|       v                                                       |
|  +---------------------------------------------------+        |
|  | data/input_schema.yaml                            |        |
|  | - Validate required fields                        |        |
|  | - Calculate input confidence                      |        |
|  | - Set default marketplaces if not specified       |        |
|  +---------------------------------------------------+        |
|       |                                                       |
|       v                                                       |
|  +---------------------------------------------------+        |
|  | STEP 1: Query Generation                          |        |
|  | HOP: prompts/query_generation.md                  |        |
|  | Output: head_terms[10-15], longtails[30-50]       |        |
|  +---------------------------------------------------+        |
|       |                                                       |
|       v                                                       |
|  +---------------------------------------------------+        |
|  | STEP 2: Marketplace Search (PARALLEL)             |        |
|  | HOP: prompts/marketplace_search.md                |        |
|  | Agents: s1/ml, s2/shopee, s3/amazon, s4/serp      |        |
|  | Output: search_results[], queries_log[]           |        |
|  +---------------------------------------------------+        |
|       |                                                       |
|       v                                                       |
|  +---------------------------------------------------+        |
|  | STEP 3: Competitor Analysis                       |        |
|  | HOP: 17_HOP_competitor_analysis.md                |        |
|  | Output: profiles[3-5], benchmark, gaps            |        |
|  +---------------------------------------------------+        |
|       |                                                       |
|       v                                                       |
|  +---------------------------------------------------+        |
|  | STEP 4: SEO Taxonomy                              |        |
|  | HOP: prompts/seo_taxonomy.md                      |        |
|  | Output: seo_inbound, seo_outbound, compliance     |        |
|  +---------------------------------------------------+        |
|                                                               |
+--------------------------------------------------------------+
```

### Output Layer

```
+--------------------------------------------------------------+
|                      OUTPUT FORMAT                            |
+--------------------------------------------------------------+
|                                                               |
|  +---------------------------------------------------+        |
|  | 22-BLOCK RESEARCH NOTES                           |        |
|  |                                                   |        |
|  | BLOCO 1: Identificacao                            |        |
|  | BLOCOS 2-4: Queries                               |        |
|  | BLOCOS 5-10: Marketplace Data                     |        |
|  | BLOCOS 11-15: Competitor Analysis                 |        |
|  | BLOCOS 16-19: SEO Taxonomy                        |        |
|  | BLOCOS 20-21: Gaps & Opportunities                |        |
|  | BLOCO 22: Handoff                                 |        |
|  +---------------------------------------------------+        |
|                                                               |
|  +---------------------------------------------------+        |
|  | METADATA                                          |        |
|  | - Confidence: X.X/10                             |        |
|  | - Duration: X minutes                            |        |
|  | - Queries logged: N                              |        |
|  | - Sources: [URLs with timestamps]                |        |
|  +---------------------------------------------------+        |
|                                                               |
+--------------------------------------------------------------+
```

---

## Horizontal Agent Roles

| Agent ID | Focus | Tools | Output |
|----------|-------|-------|--------|
| **s0/pesquisa** | Router/Orchestrator | file_search | Workflow coordination |
| **s1/pesquisa_ml** | Mercado Livre | web_search | ML-specific data |
| **s2/pesquisa_shopee** | Shopee | web_search | Shopee-specific data |
| **s3/pesquisa_amazon** | Amazon BR | web_search | Amazon-specific data |
| **s4/pesquisa_serp** | Google/YouTube | web_search | SERP + video trends |
| **s5/pesquisa_social** | TikTok/Instagram | web_search | Social commerce trends |
| **s6/pesquisa_synthesis** | Aggregation | code_interpreter | Unified research notes |

### Parallel Execution Pattern

```
s0 (Router)
    |
    +---> s1 (ML)      -+
    +---> s2 (Shopee)  -+---> PARALLEL EXECUTION
    +---> s3 (Amazon)  -+
    +---> s4 (SERP)    -+
    +---> s5 (Social)  -+
                        |
                        v
                   s6 (Synthesis) ---> 22-Block Output
```

---

## Component Dependencies

### HOPs Dependency Graph

```
prompts/orchestrator.md
       |
       +---> data/input_schema.yaml
       |           |
       |           v
       +---> prompts/query_generation.md (block)
       |           |
       |           v
       +---> prompts/marketplace_search.md (block)
       |           |
       |           v
       +---> 17_HOP_competitor_analysis.md
       |           |
       |           v
       +---> prompts/seo_taxonomy.md (block)
                   |
                   v
            data/quality_dimensions.yaml
```

### Config Dependencies

```
data/input_schema.yaml --------> prompts/orchestrator.md

data/marketplaces.yaml --------> prompts/marketplace_search.md
                                 s1-s5 horizontal agents

data/research_config.yaml -----> competitor analysis
                                 gap identification

data/execution_plan.yaml ------> prompts/orchestrator.md
```

---

## Quality Architecture

### 5D Scoring System (Research-Specific)

```
+-------------------------------------------------------------+
|                 5D QUALITY SCORING (RESEARCH)               |
+-------------------------------------------------------------+
|                                                             |
|  Data Coverage     Weight: 30% | Threshold: >= 3 MPs       |
|  Competitor Depth  Weight: 25% | Threshold: >= 3 competitors|
|  SEO Completeness  Weight: 20% | Threshold: >= 50 keywords  |
|  Freshness         Weight: 15% | Threshold: <= 7 days       |
|  Confidence        Weight: 10% | Threshold: >= 7.0          |
|                                                             |
|  OVERALL SCORE = Weighted Average                           |
|  PASS: >= 7.0 | WARN: 5.0-6.9 | FAIL: < 5.0               |
|                                                             |
+-------------------------------------------------------------+
```

### Validation Checkpoints

```yaml
checkpoint_1:
  after: "Query Generation"
  validate: "head_terms.count >= 10"
  on_fail: "retry_with_broader_category"

checkpoint_2:
  after: "Marketplace Search"
  validate: "queries_log.count >= 15"
  on_fail: "retry_different_marketplaces"

checkpoint_3:
  after: "Competitor Analysis"
  validate: "profiles.count >= 3"
  on_fail: "expand_search_criteria"

checkpoint_4:
  after: "SEO Taxonomy"
  validate: "inbound_clusters >= 5"
  on_fail: "add_regional_variations"
```

---

## Integration Points

### Upstream Agents

```
marca_agent -----------> pesquisa_agent (brand_voice.md)
user -----------------> pesquisa_agent (product_brief)
product_url ----------> pesquisa_agent (scraped_data)
```

### Downstream Agents

```
pesquisa_agent --------> anuncio_agent (research_notes.md, handoff_data)
pesquisa_agent --------> photo_agent (competitor_visuals, suggested_angles)
pesquisa_agent --------> ads_agent (keywords, negatives, benchmark)
pesquisa_agent --------> marca_agent (competitor_positioning, gaps)
```

---

## 9 Brazilian Marketplaces

| # | Marketplace | Domain | Priority |
|---|-------------|--------|----------|
| 1 | **Mercado Livre** | mercadolivre.com.br | Critical |
| 2 | **Shopee** | shopee.com.br | Critical |
| 3 | **Amazon BR** | amazon.com.br | Critical |
| 4 | **Magalu** | magazineluiza.com.br | High |
| 5 | **Americanas** | americanas.com.br | High |
| 6 | **Casas Bahia** | casasbahia.com.br | Medium |
| 7 | **Submarino** | submarino.com.br | Medium |
| 8 | **TikTok Shop** | tiktok.com/shop/br | Emerging |
| 9 | **Shein** | shein.com.br | Emerging |

---

## Technical Specifications

### Token Budget

| Component | Tokens | % Total |
|-----------|--------|---------|
| Core docs | 5,000 | 28% |
| Config | 3,500 | 19% |
| Execution | 1,800 | 10% |
| HOPs | 7,700 | 43% |
| **TOTAL** | **~18,000** | **100%** |

### Execution Timing

| Phase | Duration | Notes |
|-------|----------|-------|
| Input Validation | 5-10s | Local processing |
| Query Generation | 30-60s | LLM generation |
| Marketplace Search | 2-5min | Parallel web search |
| Competitor Analysis | 1-2min | Data processing |
| SEO Taxonomy | 30-60s | Consolidation |
| QA Validation | 10-20s | Scoring |
| **TOTAL** | **5-10min** | Full research |

---

## Version Control

```
v2.1.0 (current)
+-- Horizontal agent architecture (s0-s6)
+-- 9 Brazilian marketplaces
+-- 22-block output structure
+-- 5D quality scoring (research-specific)
+-- Parallel marketplace search

v2.0.0
+-- FRACTAL-LEGO block system
+-- 4 core blocks (query, search, competitor, seo)
+-- Handoff format standardization

v1.0.0
+-- Basic research orchestrator
+-- Single marketplace support
```

---

**Architecture**: HORIZONTAL AGENT (s0-s6)
**Pattern**: Parallel marketplace search + synthesis aggregation
**Quality**: 5D scoring with >= 7.0 threshold
**Output**: 22-block research notes + structured handoff
