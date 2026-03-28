# HOP: Scene Descriptions | photo_agent v4.2.0

**Purpose**: Reference guide for 9-scene CONVERSION grid
**Type**: Knowledge Base
**Framework**: Emotion-based (NOT angle-based)
**Version**: 4.2.0

---

## CRITICAL CHANGE v4.2

### Output Format (NAO confundir com as cenas)
```
- IMAGEM = GRID 3x3 (9 cenas em 1 imagem)
- PROMPT 2 = 1 BLOCO UNICO (IMAGE 1/9 ate IMAGE 9/9)
- NAO separar em 9 blocos diferentes
```

---

## CONVERSION FRAMEWORK: Emotion > Angle

### OLD Approach (v10)
```
- Flat Lay (aesthetic without purpose)
- Packaging (low conversion)
- Technical View (old "angles" approach)
- Scale Reference (informational, not emotional)
```

### NEW Approach (v4.2)
```
- Problem State (pain trigger)
- Transformation (desire trigger)
- Social Belonging (social proof)
- Emotional Peak (emotional connection)
- Lifestyle Dream (aspiration)
```

**100% of scenes have PSYCHOLOGICAL PURPOSE**

---

## 9-SCENE CONVERSION OVERVIEW

```
+-----------------+-----------------+-----------------+
|   SCENE 1       |   SCENE 2       |   SCENE 3       |
|   HERO TRUST    |   PROBLEM STATE |   SOLUTION      |
|   Trust         |   Pain          |   Relief        |
|   fidelity: 5   |   fidelity: 4   |   fidelity: 4   |
+-----------------+-----------------+-----------------+
|   SCENE 4       |   SCENE 5       |   SCENE 6       |
|   TRANSFORMATION|   SOCIAL        |   BENEFIT PROOF |
|   Desire        |   Belonging     |   Curiosity     |
|   fidelity: 4   |   fidelity: 3   |   fidelity: 4   |
+-----------------+-----------------+-----------------+
|   SCENE 7       |   SCENE 8       |   SCENE 9       |
|   EMOTIONAL PEAK|   LIFESTYLE     |   MARKETPLACE   |
|   Pleasure      |   Aspiration    |   Action        |
|   fidelity: 3   |   fidelity: 3   |   fidelity: 5   |
+-----------------+-----------------+-----------------+
```

---

## SCENE 1: HERO TRUST

**Position**: Top-left
**Purpose**: Establish trust and professionalism
**Emotional Trigger**: Trust + Authority
**Fidelity**: 5 (MAXIMUM)
**Background**: #FFFFFF

### Characteristics
```yaml
proposito: Establish trust and professionalism
gatilho: Trust + Authority
prompt_focus: "Product centered, pure white background, professional lighting"
visual: Clean, sharp, high quality
camera: 85mm f/8-f/11 ISO 100
lighting: High-key softbox
```

### Psychological Mechanism
"Professional seller = trustworthy"

### E-commerce Use
- Search thumbnails
- Category pages
- Product comparison
- Main listing image

---

## SCENE 2: PROBLEM STATE

**Position**: Top-center
**Purpose**: Create identification - "I HAVE this problem!"
**Emotional Trigger**: Pain + Recognition
**Fidelity**: 4 (HIGH)
**Background**: Realistic context

### Characteristics
```yaml
proposito: Create identification with pain
gatilho: Pain + Recognition
prompt_focus: "Context showing the PROBLEM this product solves"
visual: Frustrating situation, inconvenience, discomfort
camera: 35-50mm f/2.8-f/4 ISO 400
lighting: Natural/ambient
```

### Psychological Mechanism
"This is MY problem" = relevance

### Category Examples
```yaml
pet: "Cat scratching furniture / no place to lie in sun"
kitchen: "Disorganized kitchen / warm drink"
fitness: "Tired person / no energy"
tech: "Tangled cables / low battery"
```

---

## SCENE 3: SOLUTION MOMENT

**Position**: Top-right
**Purpose**: Show product SOLVING the problem
**Emotional Trigger**: Relief + Satisfaction
**Fidelity**: 4 (HIGH)
**Background**: Active use

### Characteristics
```yaml
proposito: Show product RESOLVING the problem
gatilho: Relief + Satisfaction
prompt_focus: "Product in action, MOMENT of resolution"
visual: Transition, relief, functioning
camera: 50mm f/4-f/5.6 ISO 200
lighting: Balanced, natural
```

### Psychological Mechanism
"This WORKS" = confidence

### Category Examples
```yaml
pet: "Cat using window bed, relaxed"
kitchen: "Perfect drink being served from thermos"
fitness: "Person using product during exercise"
tech: "Device working, problem solved"
```

---

## SCENE 4: TRANSFORMATION

**Position**: Middle-left
**Purpose**: Show the RESULT, dream achieved
**Emotional Trigger**: Aspiration + Desire
**Fidelity**: 4 (HIGH)
**Background**: Visible result

### Characteristics
```yaml
proposito: Show the AFTER - ideal state after using product
gatilho: Aspiration + Desire
prompt_focus: "The AFTER - dream achieved"
visual: Satisfaction, positive result, achievement
camera: 50mm f/2.8-f/4 ISO 200
lighting: Warm, welcoming
```

### Psychological Mechanism
"I WANT this result" = motivation

### Category Examples
```yaml
pet: "Happy cat sunbathing in window bed"
kitchen: "Satisfied person enjoying hot coffee at gym"
fitness: "Fit body, high energy"
tech: "Productivity, organization, control"
```

---

## SCENE 5: SOCIAL BELONGING

**Position**: Middle-center
**Purpose**: Social proof - "People like me use this"
**Emotional Trigger**: Belonging + Validation
**Fidelity**: 3 (MEDIUM)
**Background**: Social environment

### Characteristics
```yaml
proposito: Social proof - "People like me use this"
gatilho: Belonging + Validation
prompt_focus: "REAL people using product naturally"
visual: Group, family, friends, social context
camera: 35mm f/2.8-f/4 ISO 400
lighting: Natural window
```

### Psychological Mechanism
"People like me use it" = validation

### Category Examples
```yaml
pet: "Family admiring cat in window bed"
kitchen: "Friends sharing drinks with thermos"
fitness: "Workout group using equipment"
tech: "Colleagues in office using device"
```

---

## SCENE 6: BENEFIT PROOF

**Position**: Middle-right
**Purpose**: Visual proof of main benefit
**Emotional Trigger**: Curiosity + Trust
**Fidelity**: 4 (HIGH)
**Background**: Macro feature

### Characteristics
```yaml
proposito: Visual proof of main benefit
gatilho: Curiosity + Trust
prompt_focus: "Close-up of FEATURE that delivers benefit"
visual: Detail that proves quality/functionality
camera: 100mm macro f/2.8-f/4 ISO 100
lighting: Ring light or diffused
```

### Psychological Mechanism
"I can SEE quality" = conviction

### Category Examples
```yaml
pet: "Industrial suction cups showing grip strength"
kitchen: "Thermal insulation, seal, material"
fitness: "Reinforced stitching, breathable material"
tech: "Connectors, finish, LED indicators"
```

---

## SCENE 7: EMOTIONAL PEAK

**Position**: Bottom-left
**Purpose**: Create emotional connection - "I'll FEEL like this"
**Emotional Trigger**: Pleasure + Joy
**Fidelity**: 3 (MEDIUM)
**Background**: Happy moment

### Characteristics
```yaml
proposito: Create emotional connection
gatilho: Pleasure + Joy
prompt_focus: "Moment of PLEASURE/HAPPINESS using product"
visual: Genuine smile, satisfaction expression, joy
camera: 85mm f/2.8 ISO 400
lighting: Warm, golden hour
```

### Psychological Mechanism
"I'll FEEL like this" = emotional anchor

### Category Examples
```yaml
pet: "Owner smiling watching happy cat"
kitchen: "Person enjoying perfect drink with pleasure expression"
fitness: "Feeling of achievement post-workout"
tech: "Satisfaction when solving problem"
```

---

## SCENE 8: LIFESTYLE DREAM

**Position**: Bottom-center
**Purpose**: Aspiration - "This is the life I want"
**Emotional Trigger**: Aspiration + Status
**Fidelity**: 3 (MEDIUM)
**Background**: Premium environment

### Characteristics
```yaml
proposito: Aspiration - "This is the life I want"
gatilho: Aspiration + Status
prompt_focus: "Product in PREMIUM/ASPIRATIONAL environment"
visual: Elevated, premium, life goals
camera: 24-35mm f/4 ISO 400
lighting: Natural elegant
```

### Psychological Mechanism
"This is MY future life" = desire

### Category Examples
```yaml
pet: "Modern apartment with view, cat in window bed"
kitchen: "Gourmet kitchen, sophisticated lifestyle"
fitness: "Premium gym, healthy life"
tech: "Elegant home office, productivity"
```

---

## SCENE 9: MARKETPLACE

**Position**: Bottom-right
**Purpose**: Closure with trust, ready to buy
**Emotional Trigger**: Trust + Action
**Fidelity**: 5 (MAXIMUM)
**Background**: #FFFFFF

### Characteristics
```yaml
proposito: Trust closure, ready to buy
gatilho: Trust + Action
prompt_focus: "Clean, professional, ready for cart"
visual: Isolated product, pure white background
camera: 85mm f/8-f/11 ISO 100
lighting: High-key soft-even
```

### Psychological Mechanism
"Ready to buy" = closure

### E-commerce Use
- Alternative main image
- Platform compliance
- A/B testing with Scene 1
- Category requirements

---

## FIDELITY WEIGHT GUIDE

| Weight | Level | Creative Freedom |
|--------|-------|-----------------|
| 5 | Maximum | Exact replication |
| 4 | High | Minor variation OK |
| 3 | Medium | Styled variation OK |
| 2 | Low | Significant variation |
| 1 | Minimal | Loose reference only |

### Weight Assignment by Scene
- **Scenes 1 & 9**: Weight 5 (critical for sales, marketplace compliance)
- **Scenes 2, 3, 4, 6**: Weight 4 (product clarity + emotional trigger)
- **Scenes 5, 7, 8**: Weight 3 (creative flexibility for emotional scenes)

---

## PNL TRIGGER MAPPING

| Scene | Primary | Secondary | Psychological Mechanism |
|-------|---------|-----------|------------------------|
| 1 | Trust | Authority | "Professional = trustworthy" |
| 2 | Pain | Recognition | "MY problem" = relevance |
| 3 | Relief | Solution | "WORKS" = confidence |
| 4 | Aspiration | Desire | "I WANT" = motivation |
| 5 | Belonging | Social Proof | "People like me" = validation |
| 6 | Curiosity | Trust | "I SEE quality" = conviction |
| 7 | Pleasure | Connection | "I'll FEEL" = anchor |
| 8 | Aspiration | Status | "MY future" = desire |
| 9 | Trust | Action | "Ready to buy" = closure |

---

## 5 LIGHTING SETUPS

| Setup | Scenes | Purpose |
|-------|--------|---------|
| High-Key Softbox | 1, 9 | Trust, marketplace compliance |
| Natural Window | 2, 3, 5 | Realism, authenticity |
| Golden Hour Warm | 4, 7 | Emotion, pleasure |
| Ring Light | 6 | Detail, proof |
| Elegant Ambient | 8 | Lifestyle, aspiration |

---

## CAMERA PROFILES BY EMOTION

| Scene Type | Lens | Aperture | ISO |
|------------|------|----------|-----|
| Hero/Marketplace (1, 9) | 50-85mm | f/8-f/11 | 100 |
| Problem/Solution (2, 3) | 35-50mm | f/2.8-f/5.6 | 200-400 |
| Transformation/Social (4, 5) | 35-85mm | f/2.8-f/4 | 200-400 |
| Benefit Proof (6) | 85-100mm | f/2.8-f/4 | 100-200 |
| Emotional/Lifestyle (7, 8) | 24-85mm | f/2.8-f/4 | 400-800 |

---

**Reference Version**: 4.2.0
**Last Updated**: 2025-12-18
**Framework**: CONVERSION + 3x3 GRID + MONOBLOCO
