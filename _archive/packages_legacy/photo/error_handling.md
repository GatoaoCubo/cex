# PHOTO Agent - Error Handling Guide

**Version**: 3.0.0 | **Type**: Failure Modes & Solutions | **Quality**: >= 8.0

---

## Top 5 Failure Modes

### 1. Missing {user_image} Prefix (CRITICAL)

**Symptom**: AI generator invents completely different product instead of using reference image

**Example**:
```
# WRONG - Missing anchor
Professional product photography of cat window hammock...

# Result: Generator creates random cat bed, wrong color, wrong design
```

**Root Cause**: Without `{user_image}` tag, Gemini/Midjourney has NO reference to actual product appearance

**Solution**:
```
# CORRECT - With anchor
{user_image} {seed:[RANDOM]}
Professional product photography of cat window hammock...

# Result: Generator uses uploaded image as reference, maintains product fidelity
```

**Detection**:
- Check if prompt starts with `{user_image}`
- Validator regex: `^{user_image}\s+{seed:\[RANDOM\]}`

**Prevention**:
- All prompts in `prompts/prompt_generator.md` MUST include anchor
- Pre-flight validation in `prompts/output_validation.md`
- Quality gate: If missing = auto-reject (score 0.0/10)

---

### 2. Non-White Background for Marketplace Scenes

**Symptom**: Marketplace (Mercado Livre, Shopee, Amazon BR) rejects images or ranks them lower

**Example**:
```
# WRONG - Scene 1 with colored background
SCENE 1 - HERO TRUST:
Product on wooden table, warm ambient lighting...

# Result: Violates marketplace policy, image rejected or hidden
```

**Root Cause**: All major BR marketplaces require primary image (Scene 1) to have pure white #FFFFFF background

**Solution**:
```
# CORRECT - Scene 1 with white background
SCENE 1 - HERO TRUST:
[produto], white background #FFFFFF, centered composition 85%,
professional studio lighting, ultra sharp focus

# Result: Marketplace compliance, primary listing image accepted
```

**Marketplace Requirements**:
| Platform | Scene 1 BG | Scene 9 BG | Enforcement |
|----------|------------|------------|-------------|
| Mercado Livre | #FFFFFF | #FFFFFF | Strict (auto-reject) |
| Shopee | #FFFFFF | Recommended | Moderate (ranking penalty) |
| Amazon BR | #FFFFFF | #FFFFFF | Strict (auto-reject) |
| Magalu | #FFFFFF | Recommended | Moderate |

**Detection**:
- Check Scene 1 description for "white background #FFFFFF"
- Check Scene 9 description for "white background #FFFFFF"
- Validator: `validate_marketplace_compliance()`

**Prevention**:
- Hardcoded in `prompts/scene_descriptions.md`
- Scene 1 template ALWAYS includes white BG
- Scene 9 template ALWAYS includes white BG

---

### 3. Unrealistic Camera Specifications

**Symptom**: Prompts include impossible camera settings that confuse AI generator

**Example**:
```
# WRONG - Impossible specs
Shot with 500mm focal length, f/1.0 aperture, ISO 50000,
1/10000 shutter speed, macro lens at 10 meters distance

# Result: AI generator ignores specs or produces inconsistent results
```

**Root Cause**: Invalid camera specs break the technical framework that guides AI generation

**Solution**:
```
# CORRECT - Realistic specs
Shot with 85mm portrait lens, f/2.8 aperture, ISO 400,
natural window light, product 2 meters from camera

# Result: AI generator produces professional, consistent results
```

**Realistic Ranges** (from `data/camera_profiles.yaml`):
| Parameter | Realistic Range | Use Case |
|-----------|-----------------|----------|
| Focal Length | 24-200mm | 24-35mm wide, 50-85mm portrait, 100-200mm detail |
| Aperture | f/1.4 - f/16 | f/1.4-f/2.8 bokeh, f/5.6-f/8 sharp, f/11-f/16 deep |
| ISO | 100-6400 | 100-400 daylight, 800-1600 indoor, 3200-6400 low light |
| Shutter | 1/30 - 1/2000 | 1/60-1/250 standard, 1/500-1/2000 action |

**Detection**:
- Validate focal length in range [24, 200]
- Validate aperture in range [1.4, 16]
- Validate ISO in range [100, 6400]
- Validator: `validate_camera_specs()`

**Prevention**:
- Use pre-defined profiles from `data/camera_profiles.yaml`
- Map emotional context -> camera profile
- Example: "Trust" -> 85mm f/2.8 ISO 200

---

### 4. Missing [OPEN_VARIABLES] Section

**Symptom**: Prompts are rigid, cannot be customized without rewriting entire prompt

**Example**:
```
# WRONG - No customization options
Woman with blonde hair wearing blue shirt holding product
in modern kitchen with white walls...

# Result: User wants male model or different environment = rewrite entire prompt
```

**Root Cause**: Hardcoded details prevent flexible reuse

**Solution**:
```
# CORRECT - With open variables
[GENDER] with [HAIR_COLOR] hair wearing [CLOTHING_COLOR] shirt
holding product in [ENVIRONMENT] with [WALL_COLOR] walls...

[OPEN_VARIABLES]:
- GENDER: [mulher, homem, neutro]
- HAIR_COLOR: [loiro, moreno, ruivo, preto]
- CLOTHING_COLOR: [azul, branco, preto, vermelho]
- ENVIRONMENT: [cozinha-moderna, sala, escritorio, quarto]
- WALL_COLOR: [branco, bege, cinza, madeira]

# Result: LLM or user can customize 5 dimensions without prompt rewrite
```

**Required Variables**:
- **Model/Actor**: [gender, age, ethnicity, hair, clothing]
- **Environment**: [location, time-of-day, season, weather]
- **Props**: [additional-objects, background-elements]
- **Mood**: [lighting-style, color-palette, atmosphere]

**Detection**:
- Check for `[OPEN_VARIABLES]:` section
- Minimum 3 variables per prompt
- Validator: `validate_flexibility()`

**Prevention**:
- Template in `prompts/prompt_generator.md` includes variables
- Quality gate: If missing = -2.0 points on flexibility score

---

### 5. Product Inconsistency Across Scenes

**Symptom**: Product looks different in each scene (color, shape, size variations)

**Example**:
```
# WRONG - No consistency instructions
SCENE 1: Blue product bottle...
SCENE 2: Generate lifestyle scene with product...
SCENE 3: Generate detail shot of product...

# Result: Scene 1 = blue, Scene 2 = green, Scene 3 = purple (no consistency)
```

**Root Cause**: Each scene generated independently without cross-scene anchoring

**Solution**:
```
# CORRECT - Explicit consistency
{user_image} {seed:[RANDOM]}

CRITICAL REQUIREMENTS:
- Maintain EXACT product appearance across all 9 scenes
- Same color: #4A4A4A
- Same shape: rectangular 55x35cm
- Same material: Oxford 600D fabric texture
- Only CONTEXT changes, NOT product

SCENE 1: [produto] on white background...
SCENE 2: Same [produto] in lifestyle context...
SCENE 3: Same [produto] close-up detail...

# Result: Product visually consistent, only environment changes
```

**Consistency Checklist**:
- [ ] {user_image} anchor present (forces reference)
- [ ] "CRITICAL: Maintain EXACT product appearance" statement
- [ ] Specific product attributes repeated (color, shape, material)
- [ ] "Same [produto]" prefix in each scene description
- [ ] Validator: `validate_consistency()`

**Detection**:
- Check for "maintain exact product appearance" phrase
- Check for {user_image} anchor
- Check for explicit color/material specifications

**Prevention**:
- Template in `prompts/prompt_generator.md` includes consistency block
- Quality gate: If missing = -3.0 points on technical accuracy

---

## Error Recovery Strategies

### Strategy 1: Pre-Flight Validation

**When**: Before returning prompts to user

**How**:
```python
def validate_prompts(prompt_text):
    errors = []

    if not prompt_text.startswith("{user_image}"):
        errors.append("CRITICAL: Missing {user_image} anchor")

    if "white background #FFFFFF" not in prompt_text:
        errors.append("CRITICAL: Missing white background for Scene 1/9")

    if "[OPEN_VARIABLES]" not in prompt_text:
        errors.append("WARNING: No customization variables")

    if "maintain exact product appearance" not in prompt_text.lower():
        errors.append("WARNING: No consistency instructions")

    return errors
```

**Action**: If CRITICAL errors found -> Regenerate prompts automatically

### Strategy 2: User Feedback Loop

**When**: User reports generated images don't match expectations

**How**:
1. Ask user: "What aspect didn't match? (product appearance, color, style, context)"
2. Identify failure mode from this guide
3. Apply specific solution from above
4. Regenerate with corrected prompt

**Example**:
```
User: "The product color is wrong in all images"
Agent: [Identifies Failure Mode 5 - Product Inconsistency]
Agent: [Adds consistency block with specific color #HEXCODE]
Agent: [Regenerates with explicit color anchoring]
```

### Strategy 3: Marketplace-Specific Profiles

**When**: Target marketplace has specific requirements

**How**:
```yaml
# Marketplace compliance profiles
mercado_livre:
  scene_1_bg: "#FFFFFF"
  scene_9_bg: "#FFFFFF"
  min_resolution: "1000x1000"
  max_file_size: "5MB"
  format: ["JPG", "PNG"]

shopee:
  scene_1_bg: "#FFFFFF"
  scene_9_bg: "recommended"  # Not enforced
  min_resolution: "800x800"
  aspect_ratio: "1:1"
```

**Action**: Load profile based on `marketplace_target` input -> Apply constraints

### Strategy 4: Camera Spec Normalization

**When**: User provides unrealistic camera specs

**How**:
```python
def normalize_camera_specs(specs):
    # Clamp to realistic ranges
    focal = clamp(specs.focal_length, 24, 200)
    aperture = clamp(specs.aperture, 1.4, 16)
    iso = clamp(specs.iso, 100, 6400)

    # Select nearest valid profile
    return get_nearest_profile(focal, aperture, iso)
```

**Action**: Auto-correct invalid specs before prompt generation

### Strategy 5: Variable Injection

**When**: Prompt missing [OPEN_VARIABLES]

**How**:
```python
def inject_variables(prompt, product_category):
    # Auto-detect customizable elements
    variables = detect_customizable_elements(prompt)

    # Append variable section
    prompt += "\n\n[OPEN_VARIABLES]:\n"
    for var_name, options in variables.items():
        prompt += f"- {var_name}: {options}\n"

    return prompt
```

**Action**: Automatically add variables if missing

---

## Debugging Checklist

When prompts fail, check in order:

1. **Anchor Check** (Failure Mode 1)
   - [ ] Starts with `{user_image} {seed:[RANDOM]}`?

2. **Marketplace Check** (Failure Mode 2)
   - [ ] Scene 1 has "white background #FFFFFF"?
   - [ ] Scene 9 has "white background #FFFFFF"?

3. **Camera Check** (Failure Mode 3)
   - [ ] Focal length in [24, 200]mm?
   - [ ] Aperture in [f/1.4, f/16]?
   - [ ] ISO in [100, 6400]?

4. **Flexibility Check** (Failure Mode 4)
   - [ ] Has `[OPEN_VARIABLES]:` section?
   - [ ] Minimum 3 variables?

5. **Consistency Check** (Failure Mode 5)
   - [ ] Has "maintain exact product appearance"?
   - [ ] Specific color/material mentioned?
   - [ ] "Same [produto]" in each scene?

---

## Common User Errors

### User Error 1: Uploading Low-Res Image

**Symptom**: Generated prompts are good, but final images are pixelated

**Not Agent Fault**: Image quality depends on input image quality

**Solution**: Ask user to upload image >= 500x500px resolution

### User Error 2: Not Attaching Image to Gemini

**Symptom**: User complains "prompt doesn't work" but didn't attach reference image

**Not Agent Fault**: `{user_image}` requires actual image attachment

**Solution**: Emphasize in output: "CRITICAL: Attach original product image before generating"

### User Error 3: Wrong Tool for Prompt Type

**Symptom**: User tries Midjourney prompt in DALL-E without adaptation

**Not Agent Fault**: Different tools need different formats

**Solution**: Provide multi-tool adaptations in output (see `examples.md`)

---

## Quality Assurance

### Pre-Delivery Checklist

Run before returning prompts to user:

```yaml
validation:
  critical:
    - {user_image} anchor present
    - White background scenes 1 & 9
    - Consistency instructions

  warnings:
    - Camera specs in realistic range
    - [OPEN_VARIABLES] present
    - Brand colors incorporated (if provided)

  info:
    - Emotional progression clear
    - Lighting described per scene
    - Aspect ratio parameters present
```

**Pass Criteria**: 0 CRITICAL errors, <= 1 WARNING

### Confidence Score Mapping

| Validation Result | Confidence Score |
|-------------------|------------------|
| 0 errors, 0 warnings | 0.95-1.00 |
| 0 errors, 1 warning | 0.85-0.94 |
| 0 errors, 2 warnings | 0.75-0.84 |
| 1 critical error | Auto-reject (regenerate) |

---

## Emergency Rollback

If all validation fails:

1. **Fallback to Template**: Use generic template from `output_template.md`
2. **Minimal Safe Output**: Scene 1 (white BG) + Scene 9 (white BG) only
3. **User Notification**: "Generated minimal safe prompts. Please provide more details for full 9-scene grid."

---

**Created**: 2026-02-06
**Quality Score**: 9.0/10
**Framework**: Error Prevention + Recovery
**Satellite**: LILY
