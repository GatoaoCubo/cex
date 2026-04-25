---
id: p01_kc_brand_voice_systems
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Brand Voice Systems — Universal Frameworks for Brand Voice and Tone"
version: 1.0.0
created: 2026-04-01
author: shaka_research
domain: brand-identity
quality: 9.2
updated: 2026-04-07
tags: [brand, voice, tone, brand-voice, nngroup, content-design, governance, messaging]
tldr: "Universal frameworks for brand voice systems: NNGroup 4D model, voice/tone distinction, channel matrix, attributes, Do/Don't, governance, and scoring."
when_to_use: "When calibrating brand voice dimensions, building tone matrix per channel, or writing voice governance guidelines."
keywords: [brand-voice, tone-matrix, nngroup-4d, voice-governance, channel-calibration]
density_score: 0.94
axioms:
  - "Voice is WHO you are (constant). Tone is HOW you adjust (contextual). Never confuse them."
  - "ALWAYS include Do/Don't examples — guidelines without examples get ignored."
  - "NEVER calibrate voice without testing on 3+ channels — what works on social may fail in support."
linked_artifacts:
  primary: n06_output_brand_voice_guide
  related: [p01_kc_brand_archetypes, n06_schema_brand_voice_contract, p03_sp_commercial_nucleus]
related:
  - p01_kc_brand_book_patterns
  - ex_feedback_tone_correction
  - p01_kc_brand_frameworks
  - p01_kc_brand_archetypes
  - p01_kc_brand_voice_consistency_channels
  - brand_voice_templates
---

# Brand Voice Systems — Universal Frameworks

## 1. Fundamental Distinction: Voice vs Tone

| | Voice | Tone |
|--|-------|------|
| **What it is** | Brand personality | Contextual expression of that personality |
| **Consistency** | Constant — never changes | Varies by context, channel, and user emotional state |
| **Analogy** | How you speak to anyone | How you adjust depending on who, when, and where |
| **Example** | Brand is "encouraging and direct" (always) | More formal in legal terms; more casual on social media |

> "You have the same voice all the time, but your tone changes. You might use one tone when out to dinner with your closest friends, and a different tone in a meeting with your boss." — Mailchimp Style Guide

**Practical rule**: If a voice attribute changes depending on channel, it is tone, not voice.

---

## 2. NNGroup 4 Tone-of-Voice Dimensions

Kate Moran model (NNg, 2016, updated 2023). Each dimension is a spectrum — not binary.

### The 4 Dimensions

| # | Dimension | Pole A | Pole B |
|---|---------|--------|--------|
| 1 | Formality | Formal | Casual |
| 2 | Seriousness | Serious | Playful / Humorous |
| 3 | Respect | Respectful | Irreverent |
| 4 | Enthusiasm | Factual / Matter-of-fact | Enthusiastic |

**Measurement scale**: each dimension uses a 3-to-5-point Likert scale for user testing.

### Tone Profile (how to position the brand)

The brand profile is its position across all 4 dimensions simultaneously — expressed as a point in 4D space.

```
EXAMPLE: Modern fintech brand
  Formality:     [===o=] Casual (4/5)
  Seriousness:   [==o==] Neutral (3/5)
  Respect:       [o====] Respectful (1/5)
  Enthusiasm:    [====o] Enthusiastic (5/5)
```

### How Tone Shifts by Situation

**One error, four tones** (NNg canonical example):

| Perfil | Copy |
|--------|------|
| Formal + serio + respeitoso + factual | *"We apologize, but we are experiencing a problem."* |
| + Casual | *"We're sorry, but we're experiencing a problem on our end."* |
| + Entusiastico | *"Oops! We're sorry, but we're experiencing a problem on our end."* |
| + Divertido + irreverente | *"What did you do!? You broke it! (Just kidding. We're experiencing a problem on our end.)"* |

### Critical Research Insight (NNg)

**Trustworthiness explains 52% of willingness-to-recommend. Friendliness adds only 8% on top.**

Implications:
- Playful tone in serious industries (insurance) **increased** friendliness but **decreased** trustworthiness
- Conversational language in "dry" industries (banking) improved **both** friendliness AND trustworthiness
- Conclusion: calibrate tone to industry context, not just brand preference

---

## 3. Extended 5-Dimension System (5D)

For brands needing additional granularity beyond the NNg model:

| # | Dimension | Scale 1-5 | Description |
|---|---------|-----------|-----------|
| 1 | Formality | 1 (very formal) — 5 (very casual) | Language register and protocol level |
| 2 | Seriousness | 1 (grave/serious) — 5 (humorous) | Presence of levity and humor |
| 3 | Warmth | 1 (distant/institutional) — 5 (intimate/warm) | Warmth and relationship closeness |
| 4 | Authority | 1 (humble/learner) — 5 (expert/leader) | Projected expertise level |
| 5 | Intensity | 1 (factual/neutral) — 5 (very enthusiastic) | Emotional energy |

**Profile template**:
```yaml
voice_profile:
  formality: 4      # casual, not colloquial
  seriousness: 3    # moderate levity, contextual humor
  warmth: 4         # warm, approachable
  authority: 4      # expert without arrogance
  intensity: 3      # energetic but not excessive
```

---

## 4. Voice Attribute Framework: "We are X, not Y"

Universal pattern for defining voice with precision. Each attribute needs its anti-attribute.

### Structure

```
Attribute: [POSITIVE WORD]
Not: [NEGATIVE DISTORTION OF ATTRIBUTE]
What it means: [1-2 SENTENCE DESCRIPTION]
Example: [DEMONSTRATING PHRASE]
```

### Complete Example (B2B technology brand)

| We are | We are not | Meaning |
|-------|-----------|-------------|
| **Clear** | Oversimplified | We eliminate jargon but don't underestimate the customer's intelligence |
| **Trustworthy** | Rigid | We promise only what we deliver, with data supporting every claim |
| **Human** | Too informal | We write as people, not as a corporation — but maintain professionalism |
| **Direct** | Blunt | We get to the point without hedging, but always with sufficient context |
| **Enthusiastic** | Over-the-top | Genuinely excited, but without hyperbole or empty superlatives |

### Common Anti-Patterns (what to avoid defining as attributes)

| Don't use | Why | Use instead |
|---------|---------|------------|
| "Innovative" | Every company says this | "Hands-on with experimentation" |
| "Passionate" | Cliche without substance | "Committed to [specific outcome]" |
| "Authentic" | Vague and self-declared | "Transparent about limitations" |
| "World-class" | Meaningless without evidence | "Tested by X clients in Y countries" |

---

## 5. Tone-by-Channel Matrix

How consistent VOICE expresses itself with different TONES per channel:

| Channel | Tone | Formality | Humor | Length | Priority |
|-------|-----|-------------|-------|-------------|------------|
| **Twitter/X** | Sharp, witty, fast | 4/5 casual | Yes (if natural) | <280 chars | Relevance + timing |
| **LinkedIn** | Substantive, professional | 2/5 formal | Rare | 150-300 words | Credibility |
| **Instagram** | Aspirational, visual-first | 4/5 casual | Yes | 1-3 sentences | Emotion + aesthetics |
| **TikTok** | Conversational, authentic | 5/5 casual | Essential | Hook in 3s | Entertainment |
| **Email marketing** | Personal, actionable | 3/5 neutral | Contextual | 50-150 words | Open rate + CTR |
| **Support** | Empathetic, resolution-focused | 3/5 neutral | Never | Clear and brief | Fast resolution |
| **Documentation** | Precise, neutral | 2/5 formal | No | Complete | Technical clarity |
| **Ads** | Urgent, benefit-first | 3/5 neutral | Contextual | Headline < 6 words | Conversion |
| **Push notification** | Imperative, direct | 4/5 casual | Never | < 30 chars | Open rate |

---

## 6. World-Class Voice Models

### 6A. Mailchimp Voice (4 Traits)

| Trait | Definition | Anti-pattern |
|-------|-----------|-------------|
| **Plainspoken** | Clarity above all; no flowery metaphors | Marketing jargon, cheap emotional plays |
| **Genuine** | Relates to real challenges; warm and approachable | Corporate, cold, distant |
| **Translators** | Demystifies B2B-speak; genuinely educates | Oversimplification, condescension |
| **Dry humor** | Subtle, stoic, a touch eccentric; winking not shouting | Forced humor, insider jokes, condescension |

**Mailchimp golden rule**: "Always more important to be clear than entertaining."

### 6B. Shopify Polaris Voice (4 Principles)

| Principle | Core Rule | Example |
|-----------|--------------|---------|
| **Content + design** | Words are part of the design; weigh every word | "+" not "+ Add" |
| **Keep it lean** | Shortest clear path (Jenga approach) | Remove punctuation if unnecessary |
| **Write like merchants talk** | Simple language, contractions, 7th-grade level | "don't" not "do not" |
| **Inspire action** | Start with verbs; one direction per instruction | "add apps" not "you can add apps" |

**Shopify quality test**: *"Read it out loud. Does it sound like something a human would say? Ship it."*

### 6C. Adobe Spectrum Voice (3 Characteristics + 5-Tone Spectrum)

**Voice Characteristics**:

| Characteristic | Definition | Governance Rule |
|----------------|-----------|---------------------|
| **Rational** | Clear and understandable | Grammar decisions based on research and testing |
| **Human** | Friendly, honest, responsible | Vary sentence style and structure for readability |
| **Focused** | Concise and simple | Describe only what is necessary, no unnecessary decoration |

**Tone Spectrum (5 positions)**:

```
MOTIVATIONAL <-------------------------> SUPPORTIVE
  Positive and     Polished and   Neutral and    Professional    Concerned and
  encouraging      respectful     direct         and reliable    empathetic
  
[Motivational] [Helpful]     [Instructive]  [Reassuring]    [Supportive]
```

Tone can fall between positions (not binary). Correct position depends on contextual needs and user emotional state.

---

## 7. Do/Don't Pattern for Voice Guidelines

Universal structure for documenting voice guidelines in actionable form:

### Template

```markdown
### [VOICE ATTRIBUTE]

**DO:**
- [Specific behavior with example]
- [Specific behavior with example]
- [Specific behavior with example]

**DON'T:**
- [Specific behavior with example]
- [Specific behavior with example]
- [Specific behavior with example]

**EXAMPLE (same message, two tones):**
| Wrong | Right |
|--------|-------|
| [off-voice version] | [on-voice version] |
```

### Example: Online Education Brand

**Encouraging (not condescending)**:

**DO:**
- "You've already done the hardest part — keep going when it gets challenging."
- "Every mistake is data for the next attempt."
- "It's not about how long it takes, it's about what you build."

**DON'T:**
- "Simple! Just follow these easy steps..." (minimizes real difficulty)
- "Anyone can do this." (unnecessary pressure)
- "You're not the first to struggle here." (patronizing)

| Wrong | Right |
|--------|-------|
| "Error! Please try again." | "That didn't work. Let's try another way?" |
| "You CAN do this! [emoji]" | "You're getting there." |

---

## 8. 10-Phrase Pattern: Same Message, Different Tones

Technique for calibrating and documenting voice. Write the same message in 5-10 tones to demonstrate the difference:

**Base message**: "There was a problem with your payment."

| Tone | Version |
|-----|--------|
| Formal + serious | "Your transaction was not processed. Please contact your financial institution." |
| Neutral direct | "There was a problem with your payment. Check your details and try again." |
| Casual empathetic | "Oops, your payment didn't go through. It happens! Check your card details and try again." |
| Enthusiastic | "Almost there! We just need to sort out a small payment detail — two seconds." |
| Support empathetic | "We noticed the payment wasn't completed. We can help — whatever works best for you." |
| Humorous (contextual) | "Your bank disagreed with this purchase. (Happens to the best of us.) Let's try again?" |

**Usage**: Include 3-5 of these phrases in brand guidelines to calibrate writers and LLMs.

---

## 9. Voice Governance: Maintaining Consistency

### 9A. Responsibility Structure

```
LEVEL 1 — Brand Owner (Head of Content / CMO)
  Defines: voice principles, minimum score, approval process

LEVEL 2 — Voice Champions (per-team representatives)
  Applies: guidelines day-to-day, reviews copy before publishing
  Training: 1h onboarding + weekly checklist

LEVEL 3 — All Writers / Contributors
  Executes: uses guidelines and templates
  Access: brand book + per-channel examples
```

### 9B. Voice Onboarding

```
Week 1: Read brand voice section (30 min) + 10 examples per channel
Week 2: Write 5 copy pieces, reviewed by voice champion
Week 3: Calibration session (group) — compare versions and discuss
Ongoing: Quarterly voice audit (sample of 20 published copy pieces)
```

### 9C. Voice for LLMs / AI Content

To ensure AI-generated content follows brand voice:

```markdown
## SYSTEM PROMPT TEMPLATE (brand voice block)

You write on behalf of [BRAND]. Our voice is:
- [ATTRIBUTE 1]: [description + example]
- [ATTRIBUTE 2]: [description + example]
- [ATTRIBUTE 3]: [description + example]

ALWAYS:
- [specific rule]
- [specific rule]

NEVER:
- [specific anti-pattern]
- [specific anti-pattern]

Tone per channel:
- Email: [description]
- Social: [description]
- Support: [description]

Approved copy example:
"[real phrase in brand voice]"
```

---

## 10. Voice Consistency Scoring

### 10A. Manual Scoring Method (periodic audit)

Evaluate a sample of 20 published copy pieces against checklist:

```
CHECKLIST PER PIECE (0/1 per item):

[ ] Uses approved vocabulary (no prohibited terms)
[ ] Correct length for channel
[ ] Correct tone for channel
[ ] Active, not passive (active voice preferred)
[ ] Avoids jargon (or uses correct industry jargon if appropriate)
[ ] Voice attribute #1 present
[ ] Voice attribute #2 present
[ ] Voice attribute #3 present
[ ] No anti-patterns identified
[ ] Passes "sounds like a human" test (read aloud)
```

`Voice Consistency Score = (total checkmarks) / (20 pieces * 10 items) = 0-100%`

Benchmark: >85% = excellent | 70-85% = good | <70% = requires training

### 10B. Automated Method (for high-volume teams)

```python
# Schema for LLM-assisted evaluation
{
  "piece_id": "...",
  "channel": "social|email|support|docs|ads",
  "voice_score": 0-10,  # holistic evaluation
  "attributes_present": ["list of detected attributes"],
  "anti_patterns_found": ["list of issues"],
  "tone_match": true/false,  # correct tone for channel
  "recommendations": ["suggested adjustments"]
}
```

**Prompt for LLM evaluator**:
```
Evaluate this copy against brand voice for [BRAND]:
[COPY]

Brand voice: [BRAND VOICE BLOCK]
Channel: [CHANNEL]

Return JSON with: voice_score (0-10), attributes_present, anti_patterns_found, tone_match, recommendations.
```

---

## 11. Voice Development Process (Building from Scratch)

```
PHASE 1: DISCOVERY (1-2 weeks)
  a) Collect existing copy examples (30+ pieces from all channels)
  b) Interview 5-10 stakeholders: "Describe the brand in 3 adjectives"
  c) Customer research: "What word describes how we communicate?"
  d) Benchmark: analyze voice of 3-5 direct competitors

PHASE 2: DEFINITION (1 week)
  a) Cluster collected adjectives (affinity map)
  b) Select 3-5 distinct attributes (remove generic ones)
  c) For each attribute: define + anti-attribute + 3 examples
  d) Position on 4 NNg dimensions

PHASE 3: CALIBRATION (1 week)
  a) Write 10 versions of the same message (different tones)
  b) Team workshop: which version sounds "like us"?
  c) Adjust attributes based on feedback
  d) Create initial bank of approved examples (20+ pieces)

PHASE 4: DOCUMENTATION
  a) Write voice section of brand book
  b) Create Do/Don't per attribute
  c) Create tone-by-channel matrix
  d) Record 5-min video "our voice in practice"

PHASE 5: ACTIVATION
  a) Training with all writers (1h)
  b) Add voice block to AI prompt system
  c) Create voice champion per team
  d) Schedule quarterly voice audit
```

---

## 12. Vocabulary: Approved and Prohibited Words

### Brand Vocabulary Template

**USE:**
| Category | Approved Words/Phrases |
|-----------|--------------------------|
| Action | [verbs reflecting personality] |
| Benefit | [value descriptions without hyperbole] |
| Support | [approved empathy phrases] |
| Technical | [industry jargon, if appropriate] |

**AVOID:**
| Category | Prohibited Words/Phrases | Why |
|-----------|--------------------------|---------|
| Corporate-speak | "synergy", "leverage", "holistic" | Vague and impersonal |
| Hyperbole | "incredible", "revolutionary", "never seen before" | Destroys credibility |
| Passivity | "was implemented", "it is possible that" | Weak and indirect |
| Condescension | "simple", "just", "all you need to do" | Minimizes real difficulty |
| False alarm | "WARNING:", "CRITICAL:", "URGENT:" in normal contexts | Creates unnecessary anxiety |

---

## 13. Application for N06 Brand Architect

**For each company passing through N06**:

### Required Input to Generate Voice System
```yaml
company: [name]
industry: [sector]
audience: [ICP description]
archetype: [Brand Core result — block 11 of 32-block model]
desired_tone:
  formality: [1-5]
  seriousness: [1-5]
  warmth: [1-5]
  authority: [1-5]
  intensity: [1-5]
competitors: [3 brands for benchmark]
approved_examples: [3-5 phrases that "sound like the brand"]
```

### N06 Output (Voice Section of Brand Book)
```
1. Voice Profile (5 dimensions with positioning)
2. 3-5 Attributes with anti-attributes and examples
3. Tone-by-Channel Matrix (8 channels)
4. Do/Don't per attribute (3 items each)
5. Bank of 10 calibrated phrases
6. Approved and prohibited vocabulary
7. System prompt template for AI/LLMs
8. Voice Consistency Checklist
```

---

## Referencias

- NNGroup — "The Four Dimensions of Tone of Voice" — Kate Moran (2016, rev. 2023)
- Mailchimp Content Style Guide — Voice and Tone (styleguide.mailchimp.com)
- Shopify Polaris Design System — Voice and Tone
- Adobe Spectrum — Voice and Tone
- Content Design London — Voice and Tone
- Frontify Brand Guidelines Guide 2026

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_brand_book_patterns]] | sibling | 0.23 |
| [[ex_feedback_tone_correction]] | downstream | 0.22 |
| [[p01_kc_brand_frameworks]] | sibling | 0.21 |
| [[p01_kc_brand_archetypes]] | sibling | 0.19 |
| [[p01_kc_brand_voice_consistency_channels]] | sibling | 0.15 |
| [[brand_voice_templates]] | downstream | 0.15 |
