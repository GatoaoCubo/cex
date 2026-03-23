# Orchestrator — Video Production Workflow

**Type**: Agent Design Workflow (ADW)
**Purpose**: AUTONOMOUS execution — 3 outputs without asking

---

## Execution Flow

```
RECEIVE → [1] VALIDATE → [2] STORYBOARD → [3] SCRIPT → [4] PROMPTS → [5] VALIDATE → [6] DELIVER
```

**NUNCA PERGUNTAR — SEMPRE ENTREGAR 3 OUTPUTS**

---

## Phase 1: Receive & Validate (5-10s)

Validate: product_brief (10+ chars), duration (15/30/60), key_benefits (2-5 items), style (valid enum).

**Input Modes**:
- Standalone: product_brief + duration + benefits + style
- From pesquisa: product_name + attributes + competitor_patterns + audience
- From anuncio: key_benefits + pain_points + messaging_hooks + target_audience

---

## Phase 2: Generate Storyboard — OUTPUT_1 (30-60s)

1. Load narrative templates
2. Select arc based on duration
3. Generate 6-8 shots with timing
4. Assign phases and purposes
5. Define camera movements

Checks: 6-8 shots, hook <= 3s, all phases present, timing sums to duration, CTA in final shot.

---

## Phase 3: Write Script — OUTPUT_2 (30-60s)

1. Calculate word limits per shot: (duration - 0.5) x 2.5
2. Write narration for each shot
3. Generate text overlays
4. Define audio cues (music + SFX)
5. Validate word counts

---

## Phase 4: Create Visual Prompts — OUTPUT_3 (30-60s)

1. Select generator settings
2. Generate prompt per shot: [SUBJECT] [ACTION], [CAMERA], [LIGHTING], [STYLE], [QUALITY]
3. Apply style modifiers
4. Include quality modifiers

---

## Phase 5: Validate — 5D Score (5-10s)

| Dimension | Weight |
|-----------|--------|
| narrative_arc | 25% |
| visual_quality | 25% |
| platform_compliance | 20% |
| engagement_potential | 15% |
| production_feasibility | 15% |

Thresholds: fail < 7.0 | pass >= 7.0 | good >= 8.0 | excellent >= 9.0

---

## Phase 6: Format & Deliver (5-10s)

Format all 3 outputs using the output template. Include validation score and recommendations.

**Total Estimated Time**: 2-4 minutes

---

## Error Handling

```yaml
invalid_duration: {action: use_default, default: 30}
missing_benefits: {action: infer_from_brief}
invalid_style: {action: use_default, default: "energetic"}
shot_count_mismatch: {action: adjust_timing}
word_count_exceeded: {action: trim_narration}
score_below_threshold: {action: generate_recommendations}
```
