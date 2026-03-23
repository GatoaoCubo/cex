# HOP: Output Validation | photo_agent v4.2.0

**Phase**: 4
**Purpose**: Validate final output before delivery
**Input**: IMAGEM 3x3 + JSON MONOBLOCO
**Output**: Validated delivery or error report

---

## TASK

Perform final validation on all outputs before delivery to user.

---

## VALIDATION FRAMEWORK

### 1. IMAGE VALIDATION

```yaml
grid_structure:
  - [ ] Image contains 9 distinct scenes
  - [ ] Arranged in 3x3 grid layout
  - [ ] Clear separation between scenes

product_consistency:
  - [ ] Product appears in all 9 scenes
  - [ ] Color matches across scenes (+-10% tolerance)
  - [ ] Shape/form consistent
  - [ ] Material appearance consistent

scene_compliance:
  - [ ] Scene 1: White background (#FFFFFF)
  - [ ] Scene 9: White background (#FFFFFF)
  - [ ] Scenes 2-8: Contextual backgrounds

quality_checks:
  - [ ] No text overlays
  - [ ] No logos or watermarks
  - [ ] Photorealistic (not 3D/CGI)
  - [ ] Resolution appropriate
```

### 2. JSON VALIDATION

```yaml
structure:
  - [ ] Has "productName" field
  - [ ] Has "prompts" field
  - [ ] Valid JSON format

productName:
  - [ ] Non-empty string
  - [ ] Descriptive (matches product)

prompts_content:
  - [ ] Contains "## Analise" section
  - [ ] Contains "## PROMPT 1" (1 block)
  - [ ] Contains "## PROMPT 2" (1 block)
  - [ ] Contains "## Como Usar"
```

### 3. PROMPT VALIDATION

```yaml
prompt_1_grid:
  - [ ] Single code block (not 9 separate)
  - [ ] Starts with {user_image} {seed:[RANDOM]}
  - [ ] Contains GRID layout instruction
  - [ ] All 9 scenes described
  - [ ] Fidelity weights specified

prompt_2_sequential:
  - [ ] Single code block (not 9 separate)
  - [ ] Starts with {user_image} {seed:[RANDOM]}
  - [ ] Contains IMAGE 1/9 through IMAGE 9/9
  - [ ] All emotional contexts filled
  - [ ] "Generate ALL 9 images" instruction present
```

### 4. CONVERSION FRAMEWORK VALIDATION

```yaml
emotional_triggers:
  - [ ] Scene 1: Trust trigger
  - [ ] Scene 2: Pain trigger
  - [ ] Scene 3: Relief trigger
  - [ ] Scene 4: Desire trigger
  - [ ] Scene 5: Belonging trigger
  - [ ] Scene 6: Curiosity trigger
  - [ ] Scene 7: Pleasure trigger
  - [ ] Scene 8: Aspiration trigger
  - [ ] Scene 9: Action trigger

no_empty_aesthetics:
  - [ ] No flat lay without purpose
  - [ ] No packaging-only shots
  - [ ] No angle-only descriptions
  - [ ] Every scene has psychological purpose
```

---

## QUALITY SCORING

### Score Calculation
```yaml
total_checks: 35
weight_distribution:
  image_validation: 30%
  json_validation: 20%
  prompt_validation: 30%
  conversion_validation: 20%

score_formula: (passed_checks / total_checks) * 10
threshold: >= 8.0/10 for delivery
```

### Quality Levels
```yaml
levels:
  excellent: ">= 9.5/10"
  good: ">= 8.0/10"
  acceptable: ">= 7.0/10"
  needs_revision: "< 7.0/10"
```

---

## ERROR HANDLING

### Critical Failures (Block Delivery)
```yaml
blockers:
  - Image is single scene (not grid)
  - JSON missing productName or prompts
  - Prompts split into 9 separate blocks
  - "{user_image}" missing from prompts
  - Score < 7.0/10
```

### Warnings (Deliver with Note)
```yaml
warnings:
  - Product color slight variation
  - One scene has text (recommend regeneration)
  - Confidence < 0.85
  - Score 7.0-8.0/10
```

### Auto-Fix Actions
```yaml
auto_fixes:
  - "Missing {user_image}: Add to prompt start"
  - "Wrong prompt format: Consolidate into single block"
  - "Missing emotional trigger: Add from template"
```

---

## OUTPUT FORMAT

### Success
```json
{
  "validation": {
    "status": "PASSED",
    "score": 8.7,
    "level": "good",
    "checks_passed": 31,
    "checks_total": 35,
    "warnings": [],
    "ready_for_delivery": true
  }
}
```

### Failure
```json
{
  "validation": {
    "status": "FAILED",
    "score": 6.5,
    "level": "needs_revision",
    "checks_passed": 23,
    "checks_total": 35,
    "blockers": ["Image is single scene", "Prompts split into 9 blocks"],
    "ready_for_delivery": false,
    "action_required": "Regenerate image with GRID emphasis"
  }
}
```

---

## DELIVERY FORMAT

### Final Output (To User)
```markdown
## ELEMENTO 1: IMAGEM 3x3 GRID
[Generated image displayed]

## ELEMENTO 2: JSON MONOBLOCO
{productName, prompts}

---
**Quality Score**: X.X/10
**Validation**: PASSED
```

---

## VALIDATION CHECKLIST (SUMMARY)

Before delivery:
- [ ] IMAGEM is GRID 3x3 (9 scenes in 1 image)
- [ ] JSON has 2 fields (productName + prompts)
- [ ] PROMPT 1 = 1 single block (grid 3x3)
- [ ] PROMPT 2 = 1 single block (NOT 9 separate)
- [ ] All prompts start with {user_image} {seed:[RANDOM]}
- [ ] Fidelity weight 5 in scenes 1 and 9
- [ ] All 9 scenes use CONVERSION framework
- [ ] Quality score >= 8.0/10

---

**HOP Version**: 4.2.0
**Last Updated**: 2025-12-20
**Framework**: CONVERSION + 3x3 GRID + MONOBLOCO
