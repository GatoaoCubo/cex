# ADW: Brand Strategy Orchestrator | marca_agent v2.0.0

**Type**: Sequential Workflow
**Purpose**: Orchestrate 5-phase brand strategy creation
**Token Estimate**: ~1500 (orchestrator only)

---

## WORKFLOW IDENTITY

```yaml
workflow: MARCA_STRATEGY_ORCHESTRATOR
version: 2.0.0
kind: sequential
satellite: LILY
agent: marca-agent
phases: 5
quality_threshold: 8.5
```

---

## INPUT SCHEMA

```yaml
required:
  product_name: string       # "Cosmeticos Organicos para Pele Sensivel"
  category: string           # "Beleza > Cosmeticos Naturais"
  target_audience: string    # "Mulheres 25-40, conscientes, urbanas"
  price_range: string        # "popular" | "premium" | "luxury"

optional:
  competitors: array         # ["Natura", "Granado", "Simple Organic"]
  inspirations: array        # ["Aesop", "Glossier"]
  brand_brief: string        # Additional context/story
  existing_name: string      # If brand already has a name
```

---

## PHASE SEQUENCE

```
+-------------------------------------------------------------+
|                    MARCA STRATEGY PIPELINE                   |
+-------------------------------------------------------------+
|                                                              |
|  INPUT (brand brief)                                         |
|       |                                                      |
|       v                                                      |
|  [PHASE 1] prompts/brand_discovery.md                        |
|       |    -> core_benefit, persona, transformation          |
|       v                                                      |
|  [PHASE 2] prompts/archetype_selection.md                    |
|       |    -> primary + secondary archetype                   |
|       v                                                      |
|  [PHASE 3] prompts/brand_positioning.md                      |
|       |    -> UVP, competitive map, positioning              |
|       v                                                      |
|  [PHASE 4] prompts/verbal_identity.md                        |
|       |    -> names, taglines, voice, messaging              |
|       v                                                      |
|  [PHASE 5] prompts/visual_identity.md                        |
|       |    -> colors, typography, logo, photos               |
|       v                                                      |
|  OUTPUT: brand_strategy.md (32 blocks)                       |
|                                                              |
+-------------------------------------------------------------+
```

---

## EXECUTION RULES

### Phase Transitions
```yaml
phase_1_to_2:
  condition: discovery.confidence >= 0.80
  pass: core_benefit, audience_persona, transformation_promise

phase_2_to_3:
  condition: archetype.confidence >= 0.85
  pass: primary_archetype, secondary_archetype, justification

phase_3_to_4:
  condition: positioning.confidence >= 0.80
  pass: uvp, differentiation_statement, positioning_statement

phase_4_to_5:
  condition: verbal.confidence >= 0.85
  pass: brand_names, taglines, voice_dimensions

phase_5_to_output:
  condition: visual.confidence >= 0.80
  pass: color_palette, typography, logo_direction
```

### Quality Gates
```yaml
per_phase:
  - Confidence >= 0.80
  - All required outputs present
  - No placeholder values

final_output:
  - 32 blocks complete
  - consistency_score >= 0.85
  - uniqueness_score >= 8.0/10
  - WCAG AA compliance
```

---

## OUTPUT TEMPLATE

```markdown
# BRAND STRATEGY: [BRAND_NAME]

**Generated**: [DATE]
**Agent**: marca-agent v2.0.0
**Quality Score**: [X.X]/10

---

## 1. DISCOVERY BRIEF
{phase_1_output}

---

## 2. ARCHETYPE
{phase_2_output}

---

## 3. POSITIONING
{phase_3_output}

---

## 4. VERBAL IDENTITY
{phase_4_output}

---

## 5. VISUAL IDENTITY
{phase_5_output}

---

## BRAND ESSENCE
> "[One sentence that captures the brand identity]"

---

## 32-BLOCK SUMMARY
[Consolidated 32 blocks across all sections]

---

## VALIDATION
| Criterio | Status |
|----------|--------|
| Discovery complete | [check] |
| Archetype justified | [check] |
| UVP differentiated | [check] |
| 3 taglines 40-60 chars | [check] |
| Voice dimensions defined | [check] |
| Color palette WCAG valid | [check] |
| 32 blocks present | [check] |

**Quality Score**: [X.X]/10
**Brand Consistency**: [0.XX]
**Brand Uniqueness**: [X.X]/10
```

---

## ERROR HANDLING

```yaml
phase_failure:
  action: retry_with_enhanced_context
  max_retries: 2
  fallback: partial_output_with_gaps_marked

low_confidence:
  action: request_user_clarification
  threshold: 0.70

missing_input:
  action: infer_from_category_defaults
  log: "Inferred [field] from category norms"
```

---

## INTEGRATION

```yaml
upstream:
  - pesquisa_agent: Market data for positioning
  - user_brief: Direct input

downstream:
  - anuncio_agent: brand_voice, tone_dimensions
  - photo_agent: color_palette, mood_board_prompts
  - curso_agent: brand_narrative, values
```

---

**Version**: 2.0.0 | **Type**: ADW Orchestrator | **Tokens**: ~1500
