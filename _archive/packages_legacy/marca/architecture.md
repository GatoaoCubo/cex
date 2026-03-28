# ARCHITECTURE | marca_agent v2.0.0

**Version**: 2.0.0 | **Date**: 2025-12-20
**Pattern**: META-HOP ORCHESTRATOR (32-Block Brand Strategy)

---

## System Overview

```
+===============================================================================+
|                          marca_agent v2.0.0                                   |
|                    COMPREHENSIVE BRAND STRATEGY BUILDER                       |
+===============================================================================+
|                                                                               |
|   INPUT (Brand Brief)                                                         |
|        |                                                                      |
|        v                                                                      |
|   +-------------------------------------------------------------------+      |
|   |                    PHASE 1: FOUNDATION                            |      |
|   |   +-------------+     +-------------+     +-------------+         |      |
|   |   |   HOP 10    |---->|   HOP 11    |---->|   HOP 12    |         |      |
|   |   |  Identity   |     | Positioning |     | Brand Voice |         |      |
|   |   | (Blocks 1-5)|     |(Blocks 6-10)|     |(Blocks 11-15)|        |      |
|   |   +------+------+     +------+------+     +------+------+         |      |
|   |          |                   |                   |                |      |
|   |          v                   v                   v                |      |
|   |   $identity_output    $positioning_output  $voice_output         |      |
|   +-------------------------------------------------------------------+      |
|        |                                                                      |
|        v                                                                      |
|   +-------------------------------------------------------------------+      |
|   |                    PHASE 2: VISUAL (Planned)                      |      |
|   |   +-------------+     +-------------+                             |      |
|   |   |   HOP 13    |---->|   HOP 14    |                             |      |
|   |   |   Visual    |     |  Narrative  |                             |      |
|   |   |(Blocks 16-19)|    |(Blocks 20-24)|                            |      |
|   |   +-------------+     +-------------+                             |      |
|   +-------------------------------------------------------------------+      |
|        |                                                                      |
|        v                                                                      |
|   +-------------------------------------------------------------------+      |
|   |                    PHASE 3: GOVERNANCE (Planned)                  |      |
|   |   +-------------+     +-------------+                             |      |
|   |   |   HOP 15    |---->|   HOP 16    |                             |      |
|   |   | Guidelines  |     | Validation  |                             |      |
|   |   |(Blocks 25-28)|    |(Blocks 29-32)|                            |      |
|   |   +-------------+     +-------------+                             |      |
|   +-------------------------------------------------------------------+      |
|        |                                                                      |
|        v                                                                      |
|   OUTPUT (32-Block Brand Strategy)                                            |
|                                                                               |
+===============================================================================+
```

---

## Input/Output Schema

### Input Layer

```
+==============================================================================+
|                           INPUT SOURCES                                       |
+==============================================================================+
|                                                                              |
|  pesquisa_agent -------> market_research.md ----+                            |
|                          (confidence: 0.95)     |                            |
|                                                 |                            |
|  competitor_analysis --> competitor_data.json --+-----> {$BRAND_BRIEF}       |
|                          (confidence: 0.85)     |                            |
|                                                 |                            |
|  user_brief -----------> manual_input ---------+                             |
|                          (confidence: 0.70)                                  |
|                                                                              |
+==============================================================================+
```

### Required Inputs

```yaml
required:
  product_name: string           # "Cosmeticos Organicos para Pele Sensivel"
  category: string               # "Beleza > Cosmeticos Naturais"
  target_audience: string        # "Mulheres 25-40, conscientes, urbanas"
  price_range: string            # "Premium (R$ 80-200)"

optional:
  competitors: array[3+]         # ["Natura", "Granado", "Simple Organic"]
  inspirations: array            # ["Aesop", "Glossier"]
  product_category: string       # For ANVISA/INMETRO compliance
```

---

## 8-Step Workflow Pipeline

### Complete Pipeline (32 Blocks)

```
INPUT (Brief)
    |
    v
+=========================================================================+
| STEP 1: IDENTITY BUILDER (HOP 10)                              Blocks 1-5|
| Input:  $product_name, $category, $target_audience, $price_range        |
| Output: $brand_names, $taglines, $archetype, $traits, $essence          |
| Status: PRODUCTION                                                       |
+=========================================================================+
    |
    v
+=========================================================================+
| STEP 2: POSITIONING (HOP 11)                                  Blocks 6-10|
| Input:  $identity_output, $category, $competitors, $price_range         |
| Output: $uvp, $target_segment, $differentiation, $promise, $statement   |
| Status: PRODUCTION                                                       |
+=========================================================================+
    |
    v
+=========================================================================+
| STEP 3: BRAND VOICE (HOP 12)                                 Blocks 11-15|
| Input:  $identity_output, $positioning_output                            |
| Output: $dimensions, $language_style, $dos, $donts, $phrases            |
| Status: PRODUCTION                                                       |
+=========================================================================+
    |
    v
+=========================================================================+
| STEP 4: VISUAL IDENTITY (HOP 13 - Planned)                   Blocks 16-19|
| Input:  $identity_output, $positioning_output, $voice_output             |
| Output: $colors, $typography, $mood_board, $visual_guidelines           |
| Status: PLANNED                                                          |
+=========================================================================+
    |
    v
+=========================================================================+
| STEP 5: BRAND NARRATIVE (HOP 14 - Planned)                   Blocks 20-24|
| Input:  $identity_output, $positioning_output, $voice_output             |
| Output: $origin_story, $mission, $vision, $values, $manifesto           |
| Status: PLANNED                                                          |
+=========================================================================+
    |
    v
+=========================================================================+
| STEP 6: BRAND GUIDELINES (HOP 15 - Planned)                  Blocks 25-28|
| Input:  All previous outputs                                             |
| Output: $messaging_rules, $compliance, $checklist                        |
| Status: PLANNED                                                          |
+=========================================================================+
    |
    v
+=========================================================================+
| STEP 7: CROSS-VALIDATION                                     Internal QA |
| Input:  All section outputs                                              |
| Output: Consistency checks, alignment verification                       |
| Status: AUTO (runs after each step)                                      |
+=========================================================================+
    |
    v
+=========================================================================+
| STEP 8: FINAL VALIDATION (HOP 16 - Planned)                  Blocks 29-32|
| Input:  Complete brand_strategy                                          |
| Output: $consistency_score, $uniqueness_score, $audit, $integration      |
| Status: PLANNED                                                          |
+=========================================================================+
    |
    v
OUTPUT (brand_strategy.md + validation_report.txt)
```

---

## Integration Points

### Upstream Agents (Input Sources)

- pesquisa_agent: market_research.md (industry trends, consumer insights, market size)
- user_brief: brand_brief (product name, category, target audience, price range)

### Downstream Agents (Output Consumers)

- anuncio_agent: brand_voice (tone, do's, don'ts), positioning (UVP, differentiation)
- photo_agent: visual_identity (colors, mood), archetype (for mood board)
- curso_agent: brand_strategy (complete document), narrative (origin, mission, values)
- ads_agent: positioning_statement, UVP, target_segment, example_phrases
- video_agent: brand_essence, narrative (origin story, manifesto), voice dimensions

### Agent Chain Patterns

```
PATTERN 1: Full Brand-to-Content Pipeline
  pesquisa_agent --> marca_agent --> anuncio_agent --> photo_agent

PATTERN 2: Course Creation Pipeline
  marca_agent --> curso_agent --> video_agent

PATTERN 3: E-commerce Launch Pipeline
  pesquisa_agent --> marca_agent --> anuncio_agent + photo_agent + ads_agent
```

---

## Quality Gates

### 5D Scoring System

| Dimension | Weight | Threshold |
|-----------|--------|-----------|
| Consistency | 20% | >= 0.85 |
| Uniqueness | 25% | >= 8.0/10 |
| Completeness | 20% | >= 0.90 |
| Actionability | 20% | >= 0.80 |
| Compliance | 15% | >= 0.95 |

**Overall**: PASS >= 8.5/10 | PARTIAL >= 7.0/10 | FAIL < 7.0/10

### Cross-Validation Matrix

| Validation | Elements | Threshold |
|------------|----------|-----------|
| Archetype <-> Positioning | Archetype values in positioning claims | >= 0.80 |
| Traits <-> Voice | Personality traits in voice dimensions | >= 0.85 |
| Essence <-> Promise | Brand essence aligns with brand promise | >= 0.90 |
| Visual <-> Personality | Color psychology matches archetype | >= 0.80 |
| Narrative <-> Values | Origin story exemplifies core values | >= 0.85 |

---

## Technical Specifications

### Token Budget

| Component | Tokens | % Total |
|-----------|--------|---------|
| Core docs (PRIME, INSTRUCTIONS) | 3,500 | 23% |
| iso_vectorstore | 2,500 | 17% |
| HOPs (3 active) | 6,000 | 40% |
| Config files | 1,500 | 10% |
| Execution overhead | 1,500 | 10% |
| **TOTAL** | **15,000** | **100%** |

### Character Limits (Output)

| Block Type | Min | Max | Strict |
|------------|-----|-----|--------|
| Tagline | 40 | 60 | YES |
| Brand Essence | 50 | 150 | YES |
| Mission Statement | 100 | 150 | YES |
| Vision Statement | 100 | 150 | YES |
| Origin Story | 500 | - | MIN |
| Brand Manifesto | 300 | - | MIN |

### Retry Logic

```yaml
retry_strategy:
  on_validation_fail:
    - identify_failed_criteria
    - backtrack_to_responsible_step
    - inject_feedback_into_context
    - re_execute_step
    - re_validate

  max_retries_per_step: 2
  max_total_retries: 6

  escalation:
    after_max_retries: return_partial_with_warnings
```

---

## Version History

```
v2.0.0 (current)
+-- 8-step workflow architecture (3 active, 5 planned)
+-- 32-block brand strategy framework
+-- 3 production HOPs (Identity, Positioning, Voice)
+-- Cross-validation matrix
+-- 5D quality scoring

v1.0.0
+-- Initial 3-step workflow
+-- 15-block output (Sections 1-3)
+-- Basic quality gates
```

---

**Architecture Pattern**: META-HOP ORCHESTRATOR
**Blocks Covered**: 1-15 (Production) | 16-32 (Planned)
**Quality Target**: >= 8.5/10 (brand strategy threshold)
**Satellite**: LILY (Marketing)
**Entry Point**: `/prime-marca` or `Task(subagent_type="marca-agent")`
