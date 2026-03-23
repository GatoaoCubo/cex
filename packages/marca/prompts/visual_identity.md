# HOP: Visual Identity | marca_agent v2.0.0

**Phase**: 5
**Purpose**: Define color palette, typography, logo direction, and photo style
**Input**: All phases 1-4 (especially archetype)
**Output**: `{color_palette, typography, logo_direction, photo_style, mood_board_prompts}`

---

## TASK

Create the complete visual identity system: how the brand looks across all touchpoints.

---

## COLOR PALETTE

### Requirements
```yaml
primary_colors: 2-3
  - Main brand colors
  - Include HEX + RGB
  - Psychology rationale

secondary_colors: 2-3
  - Support colors
  - Less dominant usage

accent_color: 1
  - CTAs and highlights
  - High contrast

validation:
  - WCAG contrast (aim for AA minimum)
  - Test primary on secondary
```

### Color Psychology Reference
```yaml
blue: trust, stability, professionalism
green: growth, health, nature
red: energy, passion, urgency
orange: creativity, enthusiasm, warmth
purple: luxury, creativity, wisdom
yellow: optimism, clarity, warmth
black: sophistication, power, elegance
white: purity, simplicity, cleanliness
teal: innovation, calmness, technology
```

---

## TYPOGRAPHY

### Requirements
```yaml
primary_font:
  - Headlines
  - Google Fonts preferred
  - Weights: 600, 700

secondary_font:
  - Body text
  - High readability
  - Weights: 400, 500

accent_font: (optional)
  - Special uses
  - Distinctive moments

fallbacks:
  - System fonts
  - Cross-platform compatibility
```

---

## LOGO DIRECTION

### Style Options
```yaml
styles:
  - wordmark: Text-based logo
  - symbol: Icon/mark only
  - combination: Text + symbol
  - lettermark: Initials only

moods:
  - modern: Clean, minimal, geometric
  - classic: Timeless, serif, traditional
  - playful: Fun, rounded, colorful
  - minimal: Essential, spacious
```

---

## PHOTO STYLE

### Guidelines
```yaml
aesthetic: bright | dark | neutral
treatment: saturated | muted | filtered
subjects: product | lifestyle | abstract
lighting: natural | studio | dramatic
composition: centered | rule-of-thirds | dynamic
```

---

## EXECUTION

### Step 1: Color Selection
```
1. Reference archetype colors
2. Select primary palette
3. Add secondary and accent
4. Validate WCAG contrast
5. Document psychology
```

### Step 2: Typography
```
1. Match fonts to brand personality
2. Test readability
3. Define hierarchy
4. Include fallbacks
```

### Step 3: Logo Direction
```
1. Choose style based on category
2. Define mood
3. List key elements
4. Note what to avoid
```

### Step 4: Photo Guidelines
```
1. Define overall aesthetic
2. Specify color treatment
3. Describe ideal subjects
4. Create AI prompts
```

### Step 5: Mood Board Prompts
```
1. Write 3-5 AI image prompts
2. Include brand colors (HEX)
3. Specify aesthetic
4. Reference mood
```

---

## OUTPUT FORMAT

```json
{
  "visual_identity": {
    "color_palette": {
      "primary": [
        {"name": "Color Name", "hex": "#XXXXXX", "rgb": "R,G,B", "psychology": "Why", "usage": "Where"}
      ],
      "secondary": [],
      "accent": {"name": "Accent", "hex": "#XXXXXX", "usage": "CTAs"}
    },
    "wcag_validation": [
      {"pair": "BG + Text", "contrast": "X.X:1", "level": "AA"}
    ],
    "typography": {
      "primary": {"font": "Inter", "weights": [600, 700], "fallback": "sans-serif"},
      "secondary": {"font": "Inter", "weights": [400, 500], "fallback": "sans-serif"}
    },
    "logo_direction": {
      "style": "wordmark | symbol | combination",
      "mood": "modern | classic | playful",
      "include": ["key elements"],
      "avoid": ["what not to do"]
    },
    "photo_style": {
      "aesthetic": "bright/dark/neutral",
      "treatment": "saturated/muted",
      "subjects": ["product", "lifestyle"],
      "mood_board_prompts": ["prompt1", "prompt2", "prompt3"]
    }
  },
  "confidence": 0.88
}
```

---

## DISPLAY FORMAT

```markdown
## VISUAL IDENTITY

### Color Palette

**Primary Colors**:
| Color | HEX | RGB | Psychology | Usage |
|-------|-----|-----|------------|-------|
| [Name] | #XXXXXX | R,G,B | [why this color] | [where to use] |

**Secondary Colors**:
| Color | HEX | RGB | Psychology | Usage |
|-------|-----|-----|------------|-------|
| [Name] | #XXXXXX | R,G,B | [why] | [where] |

**Accent**:
| Color | HEX | Usage |
|-------|-----|-------|
| [Name] | #XXXXXX | CTAs, highlights |

**WCAG Validation**:
| Pair | Contrast | Level |
|------|----------|-------|
| [BG + Text] | X.X:1 | AA/AAA |

### Typography

**Primary (Headlines)**:
- Font: [Name] (Google Fonts)
- Weights: [600, 700]
- Fallback: [system fonts]

**Secondary (Body)**:
- Font: [Name]
- Weights: [400, 500]
- Fallback: [system fonts]

### Logo Direction
- **Style**: [Wordmark/Symbol/Combination]
- **Mood**: [Modern/Classic/Minimal]
- **Include**: [key elements]
- **Avoid**: [what not to do]

### Photo Style
- **Aesthetic**: [bright/lifestyle/product-focused]
- **Color Treatment**: [description]
- **Subjects**: [what to photograph]

**Mood Board Prompts** (for AI image generation):
1. "[detailed prompt 1]"
2. "[detailed prompt 2]"
3. "[detailed prompt 3]"
```

---

## VALIDATION

Before proceeding:
- [ ] 2-3 primary colors with HEX + RGB
- [ ] WCAG contrast validated (AA minimum)
- [ ] Typography from Google Fonts
- [ ] Logo direction defined
- [ ] 3+ mood board prompts

---

**Next**: Compile all phases into final brand strategy document
