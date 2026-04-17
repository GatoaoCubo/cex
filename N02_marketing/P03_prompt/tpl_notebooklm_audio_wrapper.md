---
id: tpl_notebooklm_audio_wrapper
kind: prompt_template
pillar: P03
title: "NotebookLM Audio Overview — Brand Intro/Outro Wrapper"
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
    description: "Company or brand name injected into intro/outro"
  - name: BRAND_VOICE
    type: string
    required: true
    default: null
    description: "Tone descriptor (e.g. casual-technical, warm-professional)"
  - name: BRAND_TAGLINE
    type: string
    required: false
    default: null
    description: "Brand tagline for cold opens and closings"
  - name: TOPIC
    type: string
    required: true
    default: null
    description: "Subject covered in the audio overview"
  - name: DURATION
    type: string
    required: true
    default: "12min"
    description: "Total audio duration (e.g. 5min, 12min, 30min)"
  - name: CTA
    type: string
    required: true
    default: null
    description: "Call-to-action at the end of the episode"
  - name: EPISODE_NUMBER
    type: integer
    required: false
    default: null
    description: "Episode number for series continuity"
  - name: TARGET_AUDIENCE
    type: string
    required: false
    default: null
    description: "Who this episode serves"
  - name: VARIANT
    type: string
    required: false
    default: "formal"
    description: "Tone variant — formal or casual (A/B testing)"
  - name: DISTRIBUTION_CHANNELS
    type: list
    required: false
    default: ["spotify", "youtube", "website"]
    description: "Where this episode will be published"
variable_syntax: mustache
composable: true
domain: content_factory
quality: 9.1
tags: [prompt_template, notebooklm, audio, podcast, wrapper, intro, outro, content_factory, N02]
tldr: "Wraps NotebookLM Audio Overview output with branded intro/outro scripts — two A/B variants (formal authority vs casual peer) with per-channel adaptation"
keywords: [audio overview, podcast, notebooklm, intro, outro, brand voice, wrapper, content factory]
density_score: null
---

# NotebookLM Audio Overview — Brand Intro/Outro Wrapper

## Purpose

NotebookLM generates raw Audio Overviews — two AI hosts discussing your knowledge cards in a conversational podcast format. The output is compelling but anonymous. It has no brand. No signature. No reason for the listener to come back.

This template wraps that raw audio with a branded intro and outro that transforms a generic AI discussion into YOUR show. The intro hooks the listener before the hosts begin. The outro converts passive listening into action after the hosts finish. Between them, NotebookLM does the heavy lifting — but your brand owns the frame.

Used in the Content Factory pipeline after `cex_notebooklm.py --studio` generates audio, and before FFmpeg assembles the final publishable file.

## Variables Table

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| BRAND_NAME | string | yes | -- | Brand name for intro/outro |
| BRAND_VOICE | string | yes | -- | Tone descriptor |
| BRAND_TAGLINE | string | no | -- | Tagline for cold opens |
| TOPIC | string | yes | -- | Episode subject |
| DURATION | string | yes | 12min | Total audio length |
| CTA | string | yes | -- | End call-to-action |
| EPISODE_NUMBER | integer | no | -- | Series numbering |
| TARGET_AUDIENCE | string | no | -- | Listener persona |
| VARIANT | string | no | formal | A/B tone variant |
| DISTRIBUTION_CHANNELS | list | no | spotify, youtube, website | Publish targets |

## Template Body

```
You are a podcast producer for {{BRAND_NAME}}. Voice: {{BRAND_VOICE}}.

CONTEXT:
NotebookLM has generated an Audio Overview about "{{TOPIC}}" lasting {{DURATION}}.
Two AI hosts discuss the topic in depth. Your job is NOT to rewrite their conversation.
Your job is to write the INTRO (before they start) and OUTRO (after they finish)
that brands this episode and converts listeners.

VARIANT: {{VARIANT}}
AUDIENCE: {{TARGET_AUDIENCE}}

---

## OUTPUT: INTRO SCRIPT (15-30 seconds when read aloud)

### If VARIANT = "formal" (A — Authority positioning)

[COLD OPEN — 5 seconds]
"{{BRAND_TAGLINE}}"

[INTRO — 10-20 seconds]
"Welcome to [SHOW_NAME] by {{BRAND_NAME}} — where we break down [DOMAIN] into
something you can actually use. I'm your host, and today we're diving into
{{TOPIC}}.

What you're about to hear is a deep conversation between two experts who've
digested everything {{BRAND_NAME}} knows about this subject. {{DURATION}} of
pure signal, zero filler.

Let's get into it."

### If VARIANT = "casual" (B — Peer connection)

[COLD OPEN — 5 seconds]
"Hey — you're listening to {{BRAND_NAME}}."

[INTRO — 10-20 seconds]
"So here's the thing about {{TOPIC}} — most people overcomplicate it.
We asked our research team to break it down, debate it, and pull out
the parts that actually matter to you.

What you'll hear next is a {{DURATION}} conversation that cuts through
the noise. Grab your coffee, let's go."

---

## OUTPUT: OUTRO SCRIPT (20-40 seconds when read aloud)

### If VARIANT = "formal" (A)

[TRANSITION — 3 seconds]
"And that's a wrap on {{TOPIC}}."

[VALUE RECAP — 10 seconds]
"If this episode helped you understand [KEY_CONCEPT_1] and [KEY_CONCEPT_2],
you'll want to save it — the kind of clarity you just heard compounds
when you revisit it."

[CTA — 10 seconds]
"{{CTA}}"

[SIGN-OFF — 5 seconds]
"This has been [SHOW_NAME] by {{BRAND_NAME}}. Until next time —
keep building, keep learning."

### If VARIANT = "casual" (B)

[TRANSITION — 3 seconds]
"Alright, that was a lot — in the best way."

[VALUE RECAP — 10 seconds]
"Quick recap: you now know more about {{TOPIC}} than 95% of people
who just scroll past it. That's not hype — that's what happens
when you actually listen."

[CTA — 10 seconds]
"{{CTA}}"

[SIGN-OFF — 5 seconds]
"Thanks for spending your {{DURATION}} with {{BRAND_NAME}}.
See you in the next one."

---

## CHANNEL-SPECIFIC ADAPTATIONS

### Spotify
- Intro includes: "You're listening on Spotify — hit follow so you never miss an episode."
- Outro includes: "Rate us 5 stars if this helped. It takes 2 seconds and means everything."

### YouTube
- Intro includes: "[VISUAL: animated logo + waveform] Subscribe and hit the bell."
- Outro includes: "[VISUAL: end screen with next episode + subscribe button]"
- Add: chapter markers in description matching discussion segments.

### Website/RSS
- Intro includes: "Show notes and resources at {{BRAND_NAME}}.com/[EPISODE_SLUG]"
- Outro includes: "Full transcript and flashcards available on our site."

## CONSTRAINTS
- Intro MUST be under 30 seconds when read at 150 WPM (max 75 words)
- Outro MUST be under 40 seconds when read at 150 WPM (max 100 words)
- Never summarize the NotebookLM content — the hosts already did that
- Intro creates ANTICIPATION, not a preview
- Outro creates ACTION, not a recap
- Match {{BRAND_VOICE}} — if the brand is technical, no "Hey guys!"
- Include [KEY_CONCEPT_1] and [KEY_CONCEPT_2] placeholders — fill from NotebookLM output
- Both variants (formal/casual) must be produced for A/B testing
```

## FFmpeg Assembly Reference

```bash
# Final audio assembly order:
# 1. Brand jingle (2-3s, optional)
# 2. INTRO (from this template, narrated via ElevenLabs TTS)
# 3. NotebookLM Audio Overview (raw, unmodified)
# 4. OUTRO (from this template, narrated via ElevenLabs TTS)
# 5. Brand jingle reprise (2-3s, optional)

ffmpeg -i jingle.mp3 -i intro.mp3 -i notebooklm_audio.mp3 -i outro.mp3 -i jingle_short.mp3 \
  -filter_complex "[0][1][2][3][4]concat=n=5:v=0:a=1" \
  -metadata title="{{TOPIC}} — {{BRAND_NAME}}" \
  -metadata artist="{{BRAND_NAME}}" \
  -metadata album="[SHOW_NAME]" \
  output_episode.mp3
```

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

### Example 1: CEX Course Podcast — Formal Variant

Variables:
```yaml
BRAND_NAME: "CEX"
BRAND_VOICE: "technical-confident-direct"
BRAND_TAGLINE: "The typed knowledge system that builds itself"
TOPIC: "8F Pipeline — How 5 Words Become a Professional Artifact"
DURATION: "12min"
CTA: "Start building with CEX today — link in the description. Or type /init and let the system configure itself."
EPISODE_NUMBER: 1
TARGET_AUDIENCE: "Developers who want to monetize knowledge as digital products"
VARIANT: "formal"
DISTRIBUTION_CHANNELS: ["spotify", "youtube", "website"]
```

Rendered Intro:
```
"The typed knowledge system that builds itself."

"Welcome to CEX Deep Dives — where we break down AI-native knowledge systems
into something you can actually ship. Today we're diving into the 8F Pipeline:
how five words of user input become a production-ready artifact.

What you're about to hear is a 12-minute deep conversation between two experts
who've digested everything CEX knows about this subject. Pure signal, zero filler.

Let's get into it."
```

### Example 2: Fashion Brand — Casual Variant

Variables:
```yaml
BRAND_NAME: "MODAVIVA"
BRAND_VOICE: "warm-energetic-aspirational"
BRAND_TAGLINE: "Dress the life you want"
TOPIC: "Capsule Wardrobes That Actually Work for Brazilian Weather"
DURATION: "8min"
CTA: "Screenshot your favorite tip and share it on Stories — tag us @modaviva for a repost"
VARIANT: "casual"
TARGET_AUDIENCE: "Women 25-40 who want style without closet overwhelm"
DISTRIBUTION_CHANNELS: ["spotify", "instagram"]
```

Rendered Intro:
```
"Hey — you're listening to MODAVIVA."

"So here's the thing about capsule wardrobes — most advice comes from people
who've never dealt with 35-degree humidity in January. We asked our style team
to break it down for real Brazilian weather, debate the pieces that actually
pull their weight, and cut the Pinterest fantasy.

What you'll hear next is an 8-minute conversation that cuts through the noise.
Grab your coffee, let's go."
```
