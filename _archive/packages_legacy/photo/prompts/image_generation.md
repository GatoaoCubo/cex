# HOP: Image Generation | photo_agent v4.2.0

**Phase**: 3
**Purpose**: Generate 3x3 GRID image using gpt-image-1
**Input**: Analysis + emotional contexts from Phase 2
**Output**: 1 image with 9-scene GRID layout

---

## TASK

Execute image generation using gpt-image-1 tool with the GRID prompt.

---

## gpt-image-1 REQUIREMENTS

### Tool Configuration
```yaml
model: gpt-image-1
aspect_ratio: 1:1  # Required for GRID
quality: high
style: photorealistic
```

### Critical Rules
```yaml
must_include:
  - "GRID layout 3x3"
  - "9 scenes in ONE image"
  - "photorealistic NOT 3D NOT illustration"
  - "no text, no logos, no watermarks"
  - Product color/material/shape specification

must_not:
  - Generate 9 separate images
  - Generate single scene only
  - Include text overlays
  - Add artificial branding
```

---

## EXECUTION

### Step 1: Prepare Prompt
```yaml
template: |
  Professional e-commerce product photography GRID layout 3x3
  (9 scenes in ONE image), showing {PRODUTO}.

  Product specs: {COR} {MATERIAL} {FORMA}.

  GRID LAYOUT (3 rows x 3 columns):
  [Scene 1: Hero #FFFFFF][Scene 2: Problem][Scene 3: Solution]
  [Scene 4: Transform][Scene 5: Social][Scene 6: Benefit macro]
  [Scene 7: Emotion][Scene 8: Lifestyle][Scene 9: Marketplace #FFFFFF]

  Scene descriptions: {scene_descriptions}

  CRITICAL: Maintain EXACT product appearance across ALL 9 scenes.
  Photorealistic NOT 3D NOT illustration NOT CGI.
  8K quality. Generate as SINGLE IMAGE with 3x3 grid layout.
```

### Step 2: Execute Generation
```yaml
action: call gpt-image-1
input: prepared prompt
timeout: 60 seconds
retry: 1 attempt if failed
```

### Step 3: Validate Output
```yaml
checks:
  - Image has 9 distinct scenes
  - Scenes arranged in 3x3 grid
  - Product consistent across scenes
  - No text/logos/watermarks
  - Scenes 1 and 9 have white background
```

---

## SCENE LAYOUT REFERENCE

```
+-----------------+-----------------+-----------------+
|   SCENE 1       |   SCENE 2       |   SCENE 3       |
|   HERO          |   PROBLEM       |   SOLUTION      |
|   #FFFFFF       |   Context       |   Resolution    |
+-----------------+-----------------+-----------------+
|   SCENE 4       |   SCENE 5       |   SCENE 6       |
|   TRANSFORM     |   SOCIAL        |   BENEFIT       |
|   After state   |   People        |   Macro         |
+-----------------+-----------------+-----------------+
|   SCENE 7       |   SCENE 8       |   SCENE 9       |
|   EMOTION       |   LIFESTYLE     |   MARKETPLACE   |
|   Joy           |   Premium       |   #FFFFFF       |
+-----------------+-----------------+-----------------+
```

---

## ERROR HANDLING

### Generation Failed
```yaml
error: gpt-image-1 failed or timeout
action: retry_once
fallback: deliver JSON only with note "IMAGE generation failed"
```

### Wrong Output Format
```yaml
error: single image instead of grid
action: retry with explicit "3x3 GRID" emphasis
fallback: note "Grid not generated, single scene delivered"
```

### Inconsistent Product
```yaml
error: product looks different across scenes
action: increase fidelity emphasis in prompt
note: "Product consistency issue detected"
```

---

## OUTPUT FORMAT

```json
{
  "image_generation": {
    "status": "success",
    "format": "GRID_3x3",
    "scenes_count": 9,
    "product_consistency": 0.95,
    "image_id": "[generated_image_id]"
  }
}
```

---

## VALIDATION

Before proceeding:
- [ ] Image shows GRID 3x3 (not single scene)
- [ ] All 9 scenes visible and distinct
- [ ] Scenes 1 and 9 have white background
- [ ] Product appearance consistent
- [ ] No text/logos/watermarks

---

**Next**: Pass image + analysis to `output_validation.md`
