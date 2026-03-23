# ARCHITECTURE | photo_agent v10.1.0

**Version**: 10.1.0 | **Date**: 2025-12-16
**Pattern**: Image Analysis -> Prompt Generation

---

## System Architecture

```
+-------------------------------------------------------------+
|                    photo_agent v10.1.0                      |
|              IMAGE -> ANALYSIS -> PROMPTS                   |
+-------------------------------------------------------------+
|                                                             |
|  +-------------+   +-------------+   +-------------+       |
|  |   INPUT     |-->|  ANALYSIS   |-->|   OUTPUT    |       |
|  |  (Image)    |   |  (Extract)  |   |  (Prompts)  |       |
|  +-------------+   +-------------+   +-------------+       |
|        |                  |                  |              |
|        v                  v                  v              |
|  product.jpg       {PRODUTO}          PROMPT 1 (Grid)      |
|                    {COR}              PROMPT 2 (9 Scenes)  |
|                    {MATERIAL}                              |
|                    {FORMA}                                 |
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
|  product_image ------> JPG/PNG/WebP -----> {$IMAGE}
|                                                  |
|  optional:                                       |
|    brand_colors --> #HEX codes                   |
|    style_pref --> minimalist | dramatic | ...    |
|    marketplace --> ML | Shopee | Amazon          |
|                                                  |
+--------------------------------------------------+
```

### Processing Layer
```
+--------------------------------------------------+
|              ANALYSIS PHASE                      |
+--------------------------------------------------+
|                                                  |
|  Image Analysis                                  |
|       |                                          |
|       v                                          |
|  Extract:                                        |
|    PRODUTO --> "Arranhador de gato sisal"        |
|    COR ------> "#8B7355"                        |
|    MATERIAL -> "sisal natural com MDF"           |
|    FORMA ----> "torre vertical 3 plataformas"   |
|                                                  |
+--------------------------------------------------+
```

### Output Layer
```
+--------------------------------------------------+
|              OUTPUT GENERATION                   |
+--------------------------------------------------+
|                                                  |
|  PROMPT 1: Grid 3x3                              |
|  +-----------------------------------------+    |
|  | {user_image} {seed:[RANDOM]}            |    |
|  | [GENERATE_ALL_9_SCENES_AS_GRID]...      |    |
|  +-----------------------------------------+    |
|                                                  |
|  PROMPT 2: 9 Individual Scenes                   |
|  +-----------------------------------------+    |
|  | IMAGE 1/9 - HERO TRUST: [specs...]      |    |
|  | IMAGE 2/9 - PROBLEM STATE: [specs...]   |    |
|  | ...                                     |    |
|  | IMAGE 9/9 - MARKETPLACE: [specs...]     |    |
|  +-----------------------------------------+    |
|                                                  |
+--------------------------------------------------+
```

---

## 9-Scene Grid Structure

```
+-----------------+-----------------+-----------------+
|     SCENE 1     |     SCENE 2     |     SCENE 3     |
|   Hero Shot     |   Lifestyle     |  Macro Detail   |
|   White BG      |   Environment   |   Texture       |
|   f/8-f/11      |   f/2.8-f/5.6   |   f/2.8-f/4     |
|   fidelity: 5   |   fidelity: 4   |   fidelity: 4   |
+-----------------+-----------------+-----------------+
|     SCENE 4     |     SCENE 5     |     SCENE 6     |
|   Usage Demo    |    Flat Lay     |   Packaging     |
|   Hands/Action  |   Overhead 90   |   Gift Ready    |
|   f/4-f/8       |   f/8-f/11      |   f/4-f/8       |
|   fidelity: 4   |   fidelity: 3   |   fidelity: 3   |
+-----------------+-----------------+-----------------+
|     SCENE 7     |     SCENE 8     |     SCENE 9     |
|   Technical     |  Scale Ref      |  Marketplace    |
|   Front View    |   Size Context  |   White BG      |
|   f/8-f/16      |   f/5.6-f/8     |   f/8-f/11      |
|   fidelity: 4   |   fidelity: 3   |   fidelity: 5   |
+-----------------+-----------------+-----------------+
```

---

## Component Dependencies

```
prompts/orchestrator.md
       |
       +-->  prompts/product_analysis.md
       |           |
       |           v
       |    {PRODUTO, COR, MATERIAL, FORMA}
       |           |
       +-->  prompts/prompt_generator.md
                   |
                   +-- data/camera_profiles.yaml
                   |
                   +-- data/photography_styles.yaml
                   |
                   +-- prompts/scene_descriptions.md
                              |
                              v
                        PROMPT 1 + PROMPT 2
```

---

## Fidelity System

### Weight Scale
```
fidelity weight 5: Maximum - exact replication
fidelity weight 4: High - minor creative freedom
fidelity weight 3: Medium - styled variation
fidelity weight 2: Low - significant variation
fidelity weight 1: Minimal - loose reference
```

### Scene Fidelity Assignment
```
Critical (weight 5):
  - Scene 1: Hero (main listing image)
  - Scene 9: Marketplace (compliance required)

High (weight 4):
  - Scene 3: Macro (texture accuracy)
  - Scene 4: Usage (product recognition)
  - Scene 7: Technical (specs visible)

Medium (weight 3):
  - Scene 2: Lifestyle (environment flex)
  - Scene 5: Flat lay (prop flex)
  - Scene 6: Packaging (creative)
  - Scene 8: Scale (context object)
```

---

## Token Budget

| Component | Tokens | % Total |
|-----------|--------|---------|
| Core docs | 3,500 | 35% |
| Config JSONs | 3,000 | 30% |
| Execution | 2,000 | 20% |
| HOPs | 1,500 | 15% |
| **TOTAL** | **10,000** | **100%** |

---

## Platform Compatibility

| Generator | Anchor Method | Notes |
|-----------|---------------|-------|
| Gemini 2.5 Flash | `{user_image}` | Native support |
| Midjourney v6 | `--sref [url]` | Style reference |
| DALL-E 3 | Vision input | Simplify prompts |
| Flux | Reference image | Good fidelity |
| Ideogram | Variable | Test first |

---

## Integration Points

### Upstream
```
pesquisa_agent --> photo_agent (product_specs)
marca_agent ----> photo_agent (brand_colors)
anuncio_agent --> photo_agent (product_name)
```

### Downstream
```
photo_agent --> anuncio_agent (image_analysis)
photo_agent --> video_agent (scene_specs)
photo_agent --> ads_agent (creative_assets)
```

---

**Architecture Version**: 10.1.0
**Last Updated**: 2025-12-16
