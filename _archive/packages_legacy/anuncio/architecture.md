# ARCHITECTURE | anuncio_agent v3.5.0

**Version**: 3.5.0 | **Date**: 2025-12-16
**Pattern**: META-HOP ORCHESTRATOR

---

## System Architecture

```
+-------------------------------------------------------------+
|                    anuncio_agent v3.5.0                     |
|                   META-HOP ORCHESTRATOR                     |
+-------------------------------------------------------------+
|                                                             |
|  +---------+   +---------+   +---------+   +---------+     |
|  | STEP 1  |-->| STEP 2  |-->| STEP 3  |-->| STEP 4  |     |
|  | Parse   |   | Titles  |   |Keywords |   | Bullets |     |
|  +----+----+   +----+----+   +----+----+   +----+----+     |
|       |             |             |             |           |
|       v             v             v             v           |
|  {parsed}      {titulos}    {keywords}    {bullets}         |
|       |             |             |             |           |
|       +-------------+-------------+-------------+           |
|                           |                                 |
|                           v                                 |
|                    +---------+                              |
|                    | STEP 5  |                              |
|                    |  Desc   |                              |
|                    +----+----+                              |
|                         |                                   |
|                         v                                   |
|                   {descricao}                               |
|                         |                                   |
|                         v                                   |
|                    +---------+                              |
|                    | STEP 6  |                              |
|                    |   QA    |                              |
|                    +----+----+                              |
|                         |                                   |
|                    +----+----+                              |
|                    | >= 0.90?|                              |
|                    +----+----+                              |
|                    YES  |  NO                               |
|                    +----+----+                              |
|                    v         v                              |
|              +---------+ +---------+                        |
|              | STEP 7  | |  RETRY  |                        |
|              | Output  | |  LOOP   |                        |
|              +----+----+ +---------+                        |
|                   |                                         |
|                   v                                         |
|              PART 1 + PART 2 + SOURCE                       |
|                                                             |
+-------------------------------------------------------------+
```

---

## Data Flow

### Input Layer

```
+--------------------------------------------------+
|                 INPUT SOURCES                    |
+--------------------------------------------------+
|                                                  |
|  pesquisa_agent ----> research_notes.md ----+    |
|                      (confidence: 0.95)     |    |
|                                             |    |
|  product_url -------> scraped_data ---------+--> {$INPUT}
|                      (confidence: 0.80)     |    |
|                                             |    |
|  product_brief -----> manual_input ---------+    |
|                      (confidence: 0.65)          |
|                                                  |
+--------------------------------------------------+
```

### Processing Layer

```
+--------------------------------------------------+
|              PROCESSING PIPELINE                 |
+--------------------------------------------------+
|                                                  |
|  prompts/main_agent.md                           |
|       |                                          |
|       v                                          |
|  +----------------------------------------+      |
|  | data/input_schema.yaml                 |      |
|  | - Validate required fields             |      |
|  | - Calculate confidence                 |      |
|  | - Determine fallback action            |      |
|  +----------------------------------------+      |
|       |                                          |
|       v                                          |
|  prompts/titulo_generator.md                     |
|       |                                          |
|       v                                          |
|  +----------------------------------------+      |
|  | data/copy_rules.yaml                   |      |
|  | - 58-60 char limit                     |      |
|  | - ZERO connectors                      |      |
|  | - Keywords first                       |      |
|  +----------------------------------------+      |
|       |                                          |
|       v                                          |
|  [Continue through all HOPs...]                  |
|                                                  |
+--------------------------------------------------+
```

### Output Layer

```
+--------------------------------------------------+
|                OUTPUT FORMAT                     |
+--------------------------------------------------+
|                                                  |
|  +-------------------------------------------+  |
|  | PART 1: Visual Review                     |  |
|  | - Titulos (3)                             |  |
|  | - Keywords (2 blocks)                     |  |
|  | - Bullets (10)                            |  |
|  | - Descricao (1)                           |  |
|  +-------------------------------------------+  |
|                                                  |
|  +-------------------------------------------+  |
|  | PART 2: Markdown Code Block               |  |
|  | ```markdown                               |  |
|  | [Copy-ready content]                      |  |
|  | ```                                       |  |
|  +-------------------------------------------+  |
|                                                  |
|  +-------------------------------------------+  |
|  | SOURCE ATTRIBUTION                        |  |
|  | - Source type                             |  |
|  | - Confidence score                        |  |
|  | - Origin agent                            |  |
|  +-------------------------------------------+  |
|                                                  |
+--------------------------------------------------+
```

---

## Component Dependencies

### HOPs Dependency Graph

```
prompts/main_agent.md
       |
       +--> prompts/titulo_generator.md
       |           |
       |           v
       +--> prompts/keywords_expander.md
       |           |
       |           v
       +--> prompts/bullet_points.md
       |           |
       |           v
       +--> prompts/descricao_builder.md
                   |
                   v
            prompts/qa_validation.md
```

### Config Dependencies

```
data/copy_rules.yaml ------+--> prompts/titulo_generator.md
                           |
                           +--> prompts/keywords_expander.md
                           |
                           +--> prompts/bullet_points.md

data/marketplace_specs.yaml --> prompts/titulo_generator.md

data/persuasion_patterns.yaml -+--> prompts/keywords_expander.md
                               |
                               +--> prompts/descricao_builder.md

data/quality_dimensions.yaml --> prompts/qa_validation.md
```

---

## Quality Architecture

### 5D Scoring System

```
+-------------------------------------------------+
|              5D QUALITY SCORING                 |
+-------------------------------------------------+
|                                                 |
|  +---------+   Weight: 20%                      |
|  | Clarity |   Threshold: >= 0.75               |
|  +---------+                                    |
|                                                 |
|  +-----------+ Weight: 25%                      |
|  | Persuasion| Threshold: >= 0.75               |
|  +-----------+                                  |
|                                                 |
|  +-----+       Weight: 25%                      |
|  | SEO |       Threshold: >= 0.75               |
|  +-----+                                        |
|                                                 |
|  +------------+ Weight: 20%                     |
|  | Compliance | Threshold: >= 0.90              |
|  +------------+                                 |
|                                                 |
|  +-----------+ Weight: 10%                      |
|  | Coherence | Threshold: >= 0.75               |
|  +-----------+                                  |
|                                                 |
|  =============================================  |
|  OVERALL SCORE = Weighted Average               |
|  PASS: >= 0.90 | FAIL: < 0.90                   |
|                                                 |
+-------------------------------------------------+
```

---

## Integration Points

### Upstream Agents

```
pesquisa_agent -------> anuncio_agent
                        (research_notes.md)

marca_agent ----------> anuncio_agent
                        (brand_voice.md)

photo_agent ----------> anuncio_agent
                        (image_analysis.json)
```

### Downstream Agents

```
anuncio_agent -------> photo_agent
                       (product_specs.json)

anuncio_agent -------> ads_agent
                       (listing_copy.md)

anuncio_agent -------> video_agent
                       (product_benefits.json)
```

---

## Technical Specifications

### Token Budget

| Component | Tokens | % Total |
|-----------|--------|---------|
| Core docs | 4,500 | 30% |
| Config | 3,000 | 20% |
| Execution | 1,500 | 10% |
| HOPs | 6,000 | 40% |
| **TOTAL** | **15,000** | **100%** |

### Character Limits (by Platform)

| Platform | Title | Description | Keywords |
|----------|-------|-------------|----------|
| Mercado Livre | 60 | 50,000 | Unlimited |
| Shopee | 120 | 3,000 | 12 tags |
| Magalu | 150 | 4,000 | 20 tags |
| Amazon BR | 200 | 2,000 | 250 bytes |

---

## Version Control

```
v3.5.0 (current)
+-- META-HOP ORCHESTRATOR architecture
+-- 7-step chained workflow
+-- 5D quality scoring
+-- Python validator v3.1.0

v3.0.0
+-- Initial orchestrator pattern
+-- Basic quality gates

v2.0.0
+-- Standalone prompts
+-- Manual validation
```

---

**Architecture**: META-HOP ORCHESTRATOR
**Pattern**: Chained outputs between HOPs
**Quality**: 5D scoring with >= 0.90 threshold
