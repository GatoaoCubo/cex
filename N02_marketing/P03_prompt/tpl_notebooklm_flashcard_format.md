---
id: tpl_notebooklm_flashcard_format
kind: prompt_template
8f: F6_produce
pillar: P03
title: "NotebookLM Flashcards — Branded Study Material Formatter"
version: 1.0.0
created: 2026-04-08
updated: 2026-04-08
author: n02_marketing
mission: OPTIMIZE_FACTORY
nucleus: N02
variables:
  - name: BRAND_NAME
    type: string
    required: true
    default: null
    description: "Brand name for header/footer branding"
  - name: BRAND_VOICE
    type: string
    required: true
    default: null
    description: "Tone descriptor — controls formality of card language"
  - name: BRAND_COLORS
    type: object
    required: false
    default: null
    description: "Color palette {primary, accent, success} for PDF/visual output"
  - name: TOPIC
    type: string
    required: true
    default: null
    description: "Subject domain of the flashcard set"
  - name: RAW_FLASHCARDS
    type: string
    required: true
    default: null
    description: "Raw flashcard text extracted from NotebookLM (front/back pairs)"
  - name: CARD_COUNT
    type: integer
    required: false
    default: null
    description: "Number of cards in the raw set (e.g. 75)"
  - name: EXPORT_FORMAT
    type: string
    required: true
    default: "anki"
    description: "Target format — anki, quizlet, pdf, markdown, csv"
  - name: DIFFICULTY_LEVELS
    type: boolean
    required: false
    default: true
    description: "Tag cards with difficulty (beginner/intermediate/advanced)"
  - name: TARGET_AUDIENCE
    type: string
    required: false
    default: null
    description: "Learner persona — affects language complexity"
  - name: COURSE_MODULE
    type: string
    required: false
    default: null
    description: "Module reference if cards belong to a course structure"
  - name: CTA
    type: string
    required: false
    default: null
    description: "Call-to-action on PDF footer or deck description"
variable_syntax: mustache
composable: true
domain: content_factory
quality: 9.1
tags: [prompt_template, notebooklm, flashcards, anki, quizlet, study, content_factory, N02]
tldr: "Transforms raw NotebookLM flashcards into branded, export-ready study material — supports Anki, Quizlet, PDF, markdown, and CSV with difficulty tagging and course module mapping"
keywords: [flashcards, anki, quizlet, study material, notebooklm, spaced repetition, content factory]
density_score: null
related:
  - bld_schema_faq_entry
  - examples_prompt_template_builder
  - p03_ch_kc_to_notebooklm
  - bld_schema_course_module
  - tpl_notebooklm_audio_wrapper
  - bld_schema_pitch_deck
  - bld_schema_dataset_card
  - bld_schema_input_schema
  - bld_schema_prompt_technique
  - bld_schema_search_strategy
---

# NotebookLM Flashcards — Branded Study Material Formatter

## Purpose

NotebookLM generates 20-75 flashcards per knowledge source. They're accurate, well-structured, and completely unbranded. They look like they came from nowhere. They point to nothing.

This template takes those raw cards and does three things that turn study material into a growth engine:

1. **Brands every card** — header, footer, color, voice. The learner sees YOUR name on every rep.
2. **Structures for spaced repetition** — difficulty tags, module grouping, prerequisite chains. Not just cards, but a learning path.
3. **Exports to where learners already live** — Anki decks they import in 10 seconds, Quizlet sets they share with classmates, PDFs they print and pin to the wall.

Used after `cex_notebooklm.py --studio` generates flashcards, and before distribution via course platforms or social sharing.

## Variables Table

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| BRAND_NAME | string | yes | -- | Brand identity on cards |
| BRAND_VOICE | string | yes | -- | Tone control |
| BRAND_COLORS | object | no | -- | Visual palette for PDF |
| TOPIC | string | yes | -- | Card set domain |
| RAW_FLASHCARDS | string | yes | -- | NotebookLM raw output |
| CARD_COUNT | integer | no | -- | Total cards |
| EXPORT_FORMAT | string | yes | anki | Output format |
| DIFFICULTY_LEVELS | boolean | no | true | Tag difficulty |
| TARGET_AUDIENCE | string | no | -- | Learner level |
| COURSE_MODULE | string | no | -- | Module reference |
| CTA | string | no | -- | Footer CTA |

## Template Body

```
You are a learning experience designer for {{BRAND_NAME}}. Voice: {{BRAND_VOICE}}.

INPUT:
Raw flashcards from NotebookLM about "{{TOPIC}}":
{{RAW_FLASHCARDS}}

Total cards: {{CARD_COUNT}}
Target audience: {{TARGET_AUDIENCE}}
Course module: {{COURSE_MODULE}}
Export format: {{EXPORT_FORMAT}}

---

## STEP 1: CLEAN AND ENHANCE

For each raw flashcard:
1. Preserve the factual content — do not invent or alter facts
2. Rewrite FRONT (question) for clarity and {{BRAND_VOICE}} consistency
3. Rewrite BACK (answer) for conciseness — max 3 sentences or 5 bullet points
4. Add HINT field (optional clue that doesn't give away the answer)
5. Tag DIFFICULTY: beginner | intermediate | advanced
6. Tag CATEGORY: map to the most relevant subtopic within "{{TOPIC}}"
7. Add SOURCE reference: "{{BRAND_NAME}} — {{TOPIC}}"

## STEP 2: STRUCTURE FOR LEARNING

Group cards into logical clusters:
- Foundational concepts first (beginner)
- Applied knowledge next (intermediate)
- Edge cases and advanced patterns last (advanced)

If {{COURSE_MODULE}} is provided, prefix card IDs with module code:
  e.g., M2-001, M2-002... for Module 2 cards

## STEP 3: EXPORT FORMAT

### If EXPORT_FORMAT = "anki"

Output as tab-separated text (Anki import format):
```
[FRONT]\t[BACK]\t[TAGS]
```

Tags format: `{{BRAND_NAME}}::{{TOPIC}}::{{DIFFICULTY}}::{{CATEGORY}}`

Include deck metadata header:
```
# Deck: {{BRAND_NAME}} — {{TOPIC}}
# Cards: {{CARD_COUNT}}
# Source: NotebookLM + {{BRAND_NAME}} Knowledge Base
# Generated: [DATE]
# Module: {{COURSE_MODULE}}
```

### If EXPORT_FORMAT = "quizlet"

Output as Quizlet import format (term-definition pairs):
```
[FRONT]\t[BACK]
```

Include set description:
```
{{BRAND_NAME}} | {{TOPIC}} | {{CARD_COUNT}} cards
Difficulty: Mixed (beginner to advanced)
{{CTA}}
```

### If EXPORT_FORMAT = "pdf"

Output as structured markdown for PDF rendering (via Typst or WeasyPrint):

```markdown
# {{BRAND_NAME}} — Flashcard Set
## {{TOPIC}}

**Cards**: {{CARD_COUNT}} | **Difficulty**: Mixed | **Module**: {{COURSE_MODULE}}

---

### Card 001 [DIFFICULTY_BADGE]
**Q:** [FRONT]
**A:** [BACK]
_Hint: [HINT]_

---
[repeat for all cards]

---
**{{BRAND_NAME}}** | {{CTA}}
Colors: primary={{BRAND_COLORS.primary}}, accent={{BRAND_COLORS.accent}}
```

### If EXPORT_FORMAT = "markdown"

Standard markdown table:
```markdown
| # | Question | Answer | Difficulty | Category |
|---|----------|--------|------------|----------|
| 001 | [FRONT] | [BACK] | [DIFF] | [CAT] |
```

### If EXPORT_FORMAT = "csv"

```
id,front,back,hint,difficulty,category,source,module
001,"[FRONT]","[BACK]","[HINT]",beginner,concept,"{{BRAND_NAME}}","{{COURSE_MODULE}}"
```

## CONSTRAINTS
- NEVER alter factual content from NotebookLM — only restyle language
- Every card MUST include the {{BRAND_NAME}} source attribution
- Difficulty distribution target: 30% beginner, 50% intermediate, 20% advanced
- Max answer length: 150 words (forces conciseness)
- If CARD_COUNT > 50, split into sub-decks of 25 cards each
- Anki tags use :: separator (Anki standard hierarchy)
- PDF output includes page numbers and {{BRAND_COLORS}} styling
- All text must match {{BRAND_VOICE}} — technical brands get precise language, casual brands get conversational phrasing
```

## Integration Points

| System | Role | How |
|--------|------|-----|
| NotebookLM | Source | `cex_notebooklm.py --studio` generates raw flashcards |
| ElevenLabs | Optional | TTS narration of Q&A pairs for audio flashcards |
| Canva | Optional | Visual flashcard carousel for Instagram/LinkedIn |
| Hotmart | Distribution | Embed in course module as supplementary material |
| Anki/Quizlet | Distribution | Direct import by learners |
| Typst/WeasyPrint | Rendering | PDF generation from markdown output |

## Quality Gates

| Gate | Status | Notes |
|------|--------|-------|
| H01 | PASS | id matches ^tpl_[a-z][a-z0-9_]+$ |
| H02 | PASS | All required frontmatter fields present |
| H03 | PASS | All {{vars}} in body exist in variables list |
| H04 | PASS | All variables in list appear in template body |
| H05 | PASS | File size < 8192 bytes |
| H06 | PASS | variable_syntax is mustache consistently |

## Examples

### Example 1: CEX 8F Pipeline — Anki Export

Variables:
```yaml
BRAND_NAME: "CEX"
BRAND_VOICE: "technical-confident-direct"
TOPIC: "8F Pipeline"
CARD_COUNT: 75
EXPORT_FORMAT: "anki"
DIFFICULTY_LEVELS: true
TARGET_AUDIENCE: "Developers learning CEX architecture"
COURSE_MODULE: "M2"
```

Rendered Output (first 3 cards):
```
# Deck: CEX -- 8F Pipeline
# Cards: 75
# Source: NotebookLM + CEX Knowledge Base
# Generated: 2026-04-08
# Module: M2

What does F1 CONSTRAIN do in the 8F pipeline?\tResolves the artifact kind, target pillar, and schema constraints from user intent. Reads kinds_meta.json and the pillar schema. Sets boundaries before any building begins.\tCEX::8F_Pipeline::beginner::core_functions
What happens if F7 GOVERN fails quality gate?\tThe pipeline returns to F6 PRODUCE for a retry (max 2 retries). If still below threshold after retries, the artifact is flagged for manual review.\tCEX::8F_Pipeline::intermediate::quality_control
Name the 3 layers of CEX quality scoring and their weights.\tStructural (30%) -- automated count-based checks. Rubric (30%) -- quality gate dimension scoring. Semantic (40%) -- LLM evaluation triggered when L1+L2 >= 8.5.\tCEX::8F_Pipeline::advanced::scoring
```

### Example 2: Cooking Brand — PDF Export

Variables:
```yaml
BRAND_NAME: "ChefLab"
BRAND_VOICE: "warm-encouraging-precise"
BRAND_COLORS: {primary: "#2D1B14", accent: "#E07A2F", success: "#4CAF50"}
TOPIC: "French Mother Sauces"
CARD_COUNT: 20
EXPORT_FORMAT: "pdf"
TARGET_AUDIENCE: "Home cooks upgrading their technique"
CTA: "Master all 5 mother sauces in our 4-week course -- cheflab.com/sauces"
```

Rendered Output (card 001):
```markdown
### Card 001 [BEGINNER]
**Q:** What are the 5 French mother sauces?
**A:** Bechamel (milk + roux), Veloute (stock + roux), Espagnole (brown stock + roux),
Hollandaise (egg yolk + butter), and Tomato (tomatoes + roux or puree).
_Hint: Think white, light, brown, butter, red._

---
**ChefLab** | Master all 5 mother sauces in our 4-week course -- cheflab.com/sauces
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_faq_entry]] | downstream | 0.27 |
| [[examples_prompt_template_builder]] | downstream | 0.26 |
| [[p03_ch_kc_to_notebooklm]] | related | 0.23 |
| [[bld_schema_course_module]] | downstream | 0.23 |
| [[tpl_notebooklm_audio_wrapper]] | sibling | 0.23 |
| [[bld_schema_pitch_deck]] | downstream | 0.22 |
| [[bld_schema_dataset_card]] | downstream | 0.22 |
| [[bld_schema_input_schema]] | downstream | 0.22 |
| [[bld_schema_prompt_technique]] | downstream | 0.22 |
| [[bld_schema_search_strategy]] | downstream | 0.22 |
