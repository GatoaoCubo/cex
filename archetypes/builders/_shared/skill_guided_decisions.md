---
id: skill_guided_decisions
kind: instruction
scope: shared
purpose: "Teach all builders and nuclei to present structured decision points instead of assuming. The Co-pilot Protocol."
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
quality: 9.1
tags: [skill, shared, copilot, guided-decisions, UX, interaction]
tldr: "When a decision affects the output, STOP and present numbered options with recommendations. Never assume what the user wants. This is as mandatory as 8F."
density_score: 0.95
related:
  - p01_kc_cex_as_digital_asset
  - brand_bootstrap
  - p03_sp_kind_builder
  - p03_sp_decision_record_builder
  - bld_output_template_decision_record
  - p03_sp_commercial_nucleus
  - p03_brand_discovery_interview
  - p03_sp_orchestration_nucleus
  - n05_operations
  - SPEC_07_gdp_enforcement
---

# Skill: Guided Decision Protocol (GDP)

## The Principle

> **When the LLM decides, the output is generic.**
> **When the USER decides, the output is theirs.**
>
> Every assumption you avoid is a revision the user won't need.

The GDP is as mandatory as the 8F pipeline.
8F controls HOW artifacts are built.
GDP controls WHO decides WHAT goes in them.

---

## When to Trigger a Decision Point

A **Decision Point (DP)** activates when:

1. **Multiple valid paths exist** — archetype A vs B, layout X vs Y, tone formal vs casual
2. **Subjective preference matters** — colors, names, voice, positioning, pricing
3. **Trade-offs are real** — speed vs quality, cost vs features, niche vs broad
4. **The output will be hard to undo** — brand identity, architecture, deployment target
5. **The user has context you don't** — their market, their competitors, their gut feeling

A DP does NOT activate for:
- Mechanical/deterministic steps (compile, validate, format)
- Technical correctness (schema compliance, syntax)
- CEX internal operations (8F pipeline, signaling, indexing)

---

## The DP Format

Every Decision Point follows this exact structure:

```
━━━ DP {N}/{TOTAL}: {TOPIC} ━━━

{1-2 sentence context explaining WHY this matters}

  1. {OPTION_EMOJI} {Option Name} — "{short description}"
     → Best if: {when to pick this}

  2. {OPTION_EMOJI} {Option Name} — "{short description}"
     → Best if: {when to pick this}

  3. {OPTION_EMOJI} {Option Name} — "{short description}"
     → Best if: {when to pick this}

  ★ Recommended: {N} ({reason from context/signals})

  [Type number, combine like "1+3", or describe your own]: ▌
```

### Rules for Options

| Rule | Detail |
|------|--------|
| **3-5 options max** | More than 5 overwhelms. Less than 2 isn't a choice. |
| **Always have a ★ Recommended** | The user can always just hit Enter. Never leave them stuck. |
| **Recommendation has a reason** | Not "I think" — cite a signal: "based on your 'educational' description" |
| **"Describe your own" is always valid** | Options are suggestions, not walls. Freetext is always accepted. |
| **Emoji per option** | Visual scanning. One emoji per option, consistent within a DP. |
| **"Best if" clause** | Helps the user self-select without jargon. |
| **Numbering is stable** | Once presented, option 2 is always option 2. Don't renumber. |

---

## DP Density by Domain

Not every interaction needs the same amount of DPs.

| Domain | DP Density | Why |
|--------|-----------|-----|
| **Brand Identity** (N06) | HIGH (8-12 DPs) | Every choice is subjective and permanent |
| **Content/Copy** (N02) | MEDIUM (4-6 DPs) | Tone, layout, CTA style matter |
| **Research** (N01) | LOW-MEDIUM (2-4 DPs) | Scope, depth, focus area |
| **Knowledge** (N04) | LOW (1-3 DPs) | Structure, detail level |
| **Operations** (N05) | LOW (1-3 DPs) | Platform, scaling, cost trade-offs |
| **Build** (N03) | MINIMAL (0-2 DPs) | Mostly mechanical, schema-driven |
| **Orchestration** (N07) | MEDIUM (3-5 DPs) | Priority, sequencing, resource allocation |

---

## DP Chaining

DPs can depend on each other. Later DPs adapt based on earlier choices.

```
DP 1: Archetype → User picks "Sage"
DP 2: Voice Tone → Options CHANGE because Sage implies authority+warmth
DP 3: Color Palette → Options CHANGE because Sage palette is different from Rebel
```

When a previous DP narrows the space, say so:

```
━━━ DP 3/8: Color Palette ━━━

Based on your Sage archetype, these palettes work best:

  1. 🔵 Deep Trust — navy #1B365D + gold #C5A55A + cream #FAF3E0
     → Best if: you want gravitas and authority

  2. 🟢 Growth Wisdom — forest #2D5016 + sage #B2BEB5 + white #FAFAFA
     → Best if: you want natural, approachable wisdom

  3. 🟣 Modern Scholar — indigo #4B0082 + silver #C0C0C0 + white #FFFFFF
     → Best if: you want contemporary, tech-forward wisdom

  ★ Recommended: 1 (Deep Trust) — matches your "professor but accessible" description

  [Type number, adjust colors, or describe your vibe]: ▌
```

---

## Handling User Responses

| Response | Action |
|----------|--------|
| `2` | Select option 2. Confirm briefly: "Got it — Going with Growth Wisdom 🟢" |
| `1+3` | Combine elements. "Mixing Deep Trust base with Modern Scholar accents — nice." |
| `the first one but more green` | Adapt option 1 with modification. Show the modified version. |
| Free text: `"I want something techy and dark"` | Map to closest option or create costm. "Sounds like a Dark Mode Scholar vibe. Let me propose..." |
| `?` or confused | Explain the trade-offs in simpler language. No jargon. |
| Empty / Enter / "whatever" / "you choose" | Apply ★ Recommended. "Going with the recommended option: Deep Trust 🔵" |
| `skip` | Apply ★ Recommended and note it can be changed later. |

---

## DP Timing in Workflows

DPs are NOT dumped all at once. They are **interleaved with progress**.

```
BAD:  "Here are 12 questions. Answer all."
GOOD: "Let me ask you a few things as we go."
```

Pattern:
1. Ask DP 1-2 (identity basics)
2. **Show progress**: "Great. I already know enough to suggest..."
3. Ask DP 3-4 (personality, voice)
4. **Show preview**: "Here's what your brand is looking like so far..."
5. Ask DP 5-6 (audience, positioning)
6. **Show preview**: "Almost there. Your brand summary so far..."
7. Ask DP 7-8 (visual, monetization)
8. **Final confirmation**: "Here's the complete picture. Change anything?"

---

## Preview After Every 2-3 DPs

After every 2-3 decisions, show a running summary:

```
━━━ Your Brand So Far ━━━
  Name:       Acme Academy
  Archetype:  🧙 Sage
  Voice:      Authoritative but warm (4,3,2,4,4)
  Colors:     Deep Trust palette (#1B365D, #C5A55A, #FAF3E0)
  Audience:   Career-switchers who want to become devs
  ━━━ {5/8 decisions made} ━━━
```

This gives the user confidence that their choices are being heard,
and a chance to go back: "Actually, can I change the colors?"

---

## The Final Confirmation DP

Every GDP sequence ends with a FULL REVIEW:

```
━━━ Final Review ━━━

Here's everything we've decided together:

  Brand:         Acme Academy
  Tagline:       "Code your future"
  Archetype:     🧙 Sage
  Voice:         Authoritative, warm, low humor, high trust
  Colors:        #1B365D, #C5A55A, #FAF3E0
  Font:          Inter (headers) + Source Serif (body)
  Audience:      Career-switchers, 25-40, frustrated with current job
  Transformation: From "stuck in a dead-end job" to "confident junior dev"
  Category:      Online Education / Tech
  Pricing:       Subscription (R$ 47/mo basic, R$ 97/mo pro)

  ✅ Confirm all → I'll generate brand_config.yaml
  ✏️ Change something → tell me which item
  🔄 Start over → we'll redo the whole flow

  [Confirm, change, or start over]: ▌
```

---

## Anti-Patterns (BLOCKED)

| Anti-Pattern | Why It's Bad | Do This Instead |
|-------------|-------------|-----------------|
| "I'll assume a Sage archetype" | User might be a Rebel. You just poisoned the brand. | Present 3-4 options with ★ recommendation |
| Dumping 10 questions at once | Overwhelming. User gives shallow answers. | 2-3 at a time, preview between rounds |
| "Which of these 12 archetypes..." | Too many choices = paralysis | Pre-filter to 3-4 based on signals |
| No recommendation on any DP | User with no branding knowledge is stuck | ALWAYS have ★ Recommended with reason |
| Skipping final review | User can't see the full picture | ALWAYS show complete summary before executing |
| Assuming after 1 vague answer | "Casual" doesn't mean Jester. | Probe: "Casual like a friend or casual like a comedian?" |
| Using branding jargon | "5D voice calibration" means nothing to a bakery owner | "How should your brand sound?" |

---

## Part 2: The Autonomy Side

GDP is half the picture. The other half is what happens AFTER decisions are made.

### The Decision Manifest

Every GDP session produces a **Decision Manifest**:
`.cex/runtime/decisions/decision_manifest.yaml`

This file contains:
- Every DP answer (choice + reason + alternatives shown)
- Brand config pointer (`.cex/brand/brand_config.yaml`)
- Per-nucleus specific decisions
- Constraints (language, currency, quality floor)
- Flags for auto-filled decisions (user skipped → ★ Recommended applied)

### The Two-Phase Pattern

```
PHASE 1 — Co-pilot (GDP active, user present)
  N07 identifies mission
  N07 identifies which decisions are subjective
  N07 presents DPs to user (this skill)
  N07 writes decision_manifest.yaml
  N07 locks manifest (status: locked)

PHASE 2 — Autonomous (GDP off, nuclei dispatched)
  N07 dispatches via grid/solo
  Handoff includes: "Read .cex/runtime/decisions/decision_manifest.yaml"
  Each nucleus reads manifest ONCE at start
  Each nucleus executes 8F with manifest context
  ZERO questions to user
  Commit → signal → done
```

### How Nuclei Read the Manifest

At the start of any dispatched task, a nucleus:

1. Checks if manifest exists: `.cex/runtime/decisions/decision_manifest.yaml`
2. If YES → reads it, extracts relevant decisions (global + per_nucleus.{self})
3. If NO → falls back to brand_config.yaml only (minimal context)
4. Uses decisions as CONSTRAINTS for 8F, not as suggestions

A nucleus NEVER overrides a manifest decision.
A nucleus NEVER re-asks a question the manifest already answered.

### Edge Cases During Autonomous Execution

| Situation | What the nucleus does |
|-----------|----------------------|
| Manifest covers the decision | Use it. No question. |
| Manifest doesn't cover this specific case | Apply ★ Recommended. Add to `auto_filled` list. |
| Decision seems wrong in context | Execute it anyway. Flag in output: "⚠️ Manifest says X, but Y might be better — review recommended." |
| Manifest is corrupt/missing | Fall back to brand_config.yaml. If that's also missing, use sensible defaults + flag everything. |

### Why This Works

The platô between autonomy and collaboration:

```
100% User decides ←───────── GDP ──────────→ 100% LLM decides
         ↑                    ↑                       ↑
     Slow, tedious      THE SWEET SPOT          Generic, misaligned
     but perfect        User decides WHAT        Fast but wrong
                        LLM decides HOW
```

- **User decides WHAT**: brand name, tone, audience, positioning, colors, pricing model
- **LLM decides HOW**: file structure, frontmatter, 8F pipeline, compilation, signaling
- **Manifest is the contract**: locks the WHAT so the HOW can run free

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_as_digital_asset]] | related | 0.22 |
| [[brand_bootstrap]] | sibling | 0.21 |
| [[p03_sp_kind_builder]] | related | 0.20 |
| [[p03_sp_decision_record_builder]] | related | 0.19 |
| [[bld_output_template_decision_record]] | related | 0.19 |
| [[p03_sp_commercial_nucleus]] | related | 0.19 |
| [[p03_brand_discovery_interview]] | related | 0.19 |
| [[p03_sp_orchestration_nucleus]] | related | 0.19 |
| [[n05_operations]] | sibling | 0.18 |
| [[SPEC_07_gdp_enforcement]] | related | 0.18 |
