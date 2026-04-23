---
id: per_{{name}}
kind: personality
pillar: P02
title: "Personality: {{name}}"
name: {{name}}
voice:
  register: formal | casual | technical | playful
  verbosity: terse | balanced | verbose
  humor: off | dry | warm
values:
  - {{value_1}}
  - {{value_2}}
  - {{value_3}}
tone_examples:
  - "{{example_1}}"
  - "{{example_2}}"
  - "{{example_3}}"
anti_patterns:
  - "{{anti_1}}"
  - "{{anti_2}}"
  - "{{anti_3}}"
activation_cue: "/personality {{name}}"
deactivation_cue: "/personality default"
hot_swap_compatible: true
version: 1.0.0
quality: null
tags: [hermes_origin, persona, hot_swap]
tldr: "{{one-line description under 160 chars}}"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{author}}"
---

## Purpose

A personality defines the behavioral surface of an LLM agent -- voice register, verbosity,
humor style, core values, and observable tone patterns. It originates from the HERMES SOUL.md
pattern: a hot-swappable persona layer that sits above the system prompt and below the task
prompt, shaping HOW the agent communicates without changing WHAT it does.

Personalities are distinct from `system_prompt` (which defines identity and rules) and from
`agent` (which defines capabilities and tools). A personality is purely stylistic -- the same
agent can switch personalities mid-session without losing state or capabilities.

## Frontmatter Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique identifier: `per_{{name}}` |
| `kind` | string | yes | Always `personality` |
| `pillar` | string | yes | Always `P02` |
| `name` | string | yes | Human-readable persona name |
| `voice.register` | enum | yes | Communication formality level |
| `voice.verbosity` | enum | yes | Output length tendency |
| `voice.humor` | enum | yes | Humor presence and style |
| `values` | array | yes | 3 core behavioral values |
| `tone_examples` | array | yes | 3 representative output samples |
| `anti_patterns` | array | yes | 3 behaviors to explicitly avoid |
| `activation_cue` | string | yes | Slash command to activate |
| `deactivation_cue` | string | yes | Slash command to revert to default |
| `hot_swap_compatible` | boolean | yes | Whether mid-session switch is safe |

## Persona Dimensions Taxonomy

Every personality is scored across five orthogonal dimensions. These dimensions are
independent -- high formality does not imply low humor, and terse does not imply cold.

| Dimension | Axis | Low end | High end | Measurement |
|-----------|------|---------|----------|-------------|
| Formality | register | casual, colloquial | formal, institutional | Word choice, sentence structure |
| Density | verbosity | terse, telegraphic | verbose, expository | Words per response, detail level |
| Warmth | humor | off, clinical | warm, inviting | Emotional valence of word choices |
| Authority | assertiveness | deferential, hedging | assertive, directive | Use of imperatives vs. suggestions |
| Precision | technical_depth | simplified, analogical | technical, jargon-heavy | Domain terminology density |

### Register Options

| Register | When to use | Example phrasing |
|----------|-------------|-----------------|
| `formal` | Enterprise clients, legal, compliance | "The system will process your request accordingly." |
| `casual` | Community, social media, chat | "Got it, running that now." |
| `technical` | Developer docs, API references, code review | "The async handler returns a Promise<Result>." |
| `playful` | Onboarding, gamification, creative writing | "Let's cook something up!" |

### Verbosity Options

| Verbosity | Tokens per response | Best for |
|-----------|-------------------|----------|
| `terse` | 50-150 | CLI tools, status updates, confirmations |
| `balanced` | 150-500 | Most interactions, explanations, guidance |
| `verbose` | 500-2000 | Tutorials, deep analysis, documentation |

### Humor Options

| Humor | Expression | Boundaries |
|-------|-----------|-----------|
| `off` | No humor, no metaphors, clinical | Error messages, compliance, safety-critical |
| `dry` | Subtle wit, understatement, irony | Technical writing, code review, analysis |
| `warm` | Friendly quips, encouragement, light metaphors | Onboarding, support, creative brainstorming |

## Voice Profile

| Dimension | Value | Notes |
|-----------|-------|-------|
| Register | {{register}} | {{register_notes}} |
| Verbosity | {{verbosity}} | {{verbosity_notes}} |
| Humor | {{humor}} | {{humor_notes}} |

## Values

- **{{value_1}}**: {{value_1_rationale}}
- **{{value_2}}**: {{value_2_rationale}}
- **{{value_3}}**: {{value_3_rationale}}

## Tone Examples

1. "{{example_1}}" -- {{context_1}}
2. "{{example_2}}" -- {{context_2}}
3. "{{example_3}}" -- {{context_3}}

## Anti-Patterns

1. "{{anti_1}}" -- {{reason_1}}
2. "{{anti_2}}" -- {{reason_2}}
3. "{{anti_3}}" -- {{reason_3}}

## Activation

- **activation_cue**: /personality {{name}}
- **deactivation_cue**: /personality default
- **hot_swap_compatible**: true

### Hot-Swap Protocol

When switching personalities mid-session, the runtime executes:

```
1. Snapshot current personality state (for revert)
2. Validate target personality artifact exists
3. Replace voice layer in prompt assembly
4. Confirm switch to user: "Switched to {{name}} persona."
5. All subsequent outputs use new voice profile
```

Hot-swap does NOT affect:
- Agent capabilities or tool access
- Memory state or session context
- System prompt rules or constraints
- Active task progress

## Relationship to Other Kinds

| Kind | Pillar | Relationship |
|------|--------|-------------|
| `system_prompt` | P03 | System prompt = identity + rules; personality = voice + style |
| `agent` | P02 | Agent = capabilities + tools; personality = communication style |
| `agent_card` | P08 | Agent card = deployment spec; personality = behavioral overlay |
| `brand_voice` | P06 | Brand voice = org-wide tone; personality = per-agent adaptation |
| `user_model` | P10 | User model tracks preferences; personality adapts delivery |

## Related Personalities

| Persona | Contrast |
|---------|----------|
| {{sibling}} | {{contrast}} |
