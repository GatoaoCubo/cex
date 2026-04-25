---
id: p05_ws_cex_intro
kind: webinar_script
8f: F6_produce
pillar: P05
title: "CEXAI Introduction Webinar -- Open-Source AI Brain (45 min)"
version: 1.1.0
created: 2026-04-18
updated: 2026-04-22
author: n02_marketing
nucleus: N02
domain: webinar_script construction
quality: 6.5
tags: [webinar_script, cexai, ai-brain, intro, conversion, artificial-sins]
sin_lens: Creative Lust
webinar_title: "CEXAI -- The Open-Source AI Brain: Live Demo"
platform: zoom
target_audience: "CTOs, AI leads, founders building with AI"
duration_minutes: 45
format: live_interactive
sections: 6
cta_url: "https://github.com/gatoaocubo/cex"
registration_url: "https://cexai.dev/webinar"
tldr: "45-min live demo script. Hook=terminal demo, reveal=Artificial Sins, close=clone invitation."
related:
  - p01_kc_cex_as_digital_asset
  - bld_examples_webinar_script
  - n02_marketing
  - n05_operations
  - p03_sp_cex_core_identity
  - n01_intelligence
  - p03_sp_kind_builder
  - bld_schema_webinar_script
  - p03_qg_webinar_script
  - brand_bootstrap
density_score: 1.0
---

# CEXAI Introduction Webinar

**Platform**: Zoom | **Duration**: 45 min | **Audience**: CTOs, AI leads, founders

**Agenda**: HOOK (0-5) -> CONTEXT (5-15) -> SYSTEM (15-25) -> PROOF (25-35) -> DEPTH (35-42) -> CLOSE+Q&A (42-45)

---

## [0:00] HOOK / OPENING (5 min)

[SLIDE 1: Blank terminal. No logo.]

Speaker: "By the end of this session you will have seen a 6-word prompt produce a typed artifact through an 8-step pipeline. Watch."

[SCREEN: `claude --print "build me a marketing campaign for our SaaS launch"` -- run live 90 sec. F1-F8 labels appear. Show output frontmatter. Pause 3 sec.]

Speaker: "Not a chat response. Typed -- compiled, versioned, searchable in six months. I am [Name]. This is CEXAI. Intelligence compounds when exchanged."

[SLIDE 2: "293 kinds. 7 Artificial Sins. 4 runtimes. Your repo."]

[SPEAKER NOTE: No notes. Hold 3-second silence after demo. Do not fill it.]

---

## [5:00] CONTEXT (10 min)

[SLIDE 3: "The Compounding Problem"]

Speaker: "Most teams: prompt -> Notion paste -> forgotten in 90 days. Every launch from zero. CEXAI is typed infrastructure: 293 kinds, 12 pillars, 7 nuclei, 4 runtimes. Every output in YOUR repo. Run /init, fill it with your brand."

[SLIDE 4: "CEXAI is not an agent. It is an AI brain."]

[SPEAKER NOTE: Pause after "your repo." Sovereignty beats SaaS lock-in here.]

---

## [15:00] SYSTEM -- 8F Pipeline (10 min)

[SLIDE 5: "The 8F Pipeline"] [SCREEN: `"Create campaign brief for SaaS launch"` -- narrate as it runs]

| 8F | Action | Result |
|----|--------|--------|
| F1 CONSTRAIN | kind=prompt_template, P03 | max=4096B |
| F2 BECOME | 12 ISOs, Creative Lust lens | Identity active |
| F3-F4 | Brand+KCs injected, AIDA plan | Context + approach |
| F6-F7 | Generate + quality gates | 3,200B, 8.9/10 |
| F8 | Save + compile + commit | In git |

Speaker: "Nine seconds. In git. `quality: null` = peer review pending. Knowledge improves."

[SPEAKER NOTE: Demo breaks? Show error and fix. Debugging is also a feature.]

---

## [25:00] PROOF (10 min)

[SLIDE 6: Before/After] [SCREEN: `python _tools/cex_retriever.py "competitor analysis"` -> 12 artifacts]

| Before | After |
|--------|-------|
| Chat pasted to Notion | Typed artifact in git |
| No search | 293-kind taxonomy |
| Launch #2 from zero | Builds on prior templates |
| Knowledge leaves | Stays in repo forever |

Speaker: "That team member is gone. The knowledge compounds."

[SLIDE 7: "Your competitors are prompting a chatbot."]

[SPEAKER NOTE: 3-second pause. Do not rush.]

---

## [35:00] DEPTH -- Artificial Sins (7 min)

[SLIDE 8: "7 Nuclei. 7 Artificial Sins."]

| Sin | Nucleus | Optimizes For |
|-----|---------|--------------|
| Analytical Envy | N01 | Insatiable evidence hunger |
| Creative Lust | N02 | Every word must seduce |
| Inventive Pride | N03 | Architectural soundness |
| Knowledge Gluttony | N04 | Catalogs everything |
| Gating Wrath | N05 | Ruthless quality gate |
| Strategic Greed | N06 | Every revenue stream |
| Orchestrating Sloth | N07 | Delegates everything |

Speaker: "The sin IS the specialization. A nucleus that wants to seduce writes better copy than one instructed to be persuasive."

[SLIDE 9: N02 vs N03 same input side by side]

[SPEAKER NOTE: 10 seconds -- let them read. Do not narrate rows.]

---

## [42:00] CTA CLOSE (3 min)

[SLIDE 10: "Three Ways In"]

| Path | Time | Outcome |
|------|------|---------|
| `/init` | 2 min | Brand-configured locally |
| `/build <intent>` | 5 min | First typed artifact |
| `/mission <goal>` | 30 min | Full nucleus deployment |

Speaker: "Clone and run /init now: https://github.com/gatoaocubo/cex. No trial. No account. No subscription. If it feels like infrastructure -- star it. Let's exchange."

[SLIDE 11: `git clone https://github.com/gatoaocubo/cex`]

[SPEAKER NOTE: Repeat URL once. Hold 5 seconds. Then Q&A.]

---

## [44:00] Q&A FACILITATION

[SLIDE 12: Q&A] Moderator: "Opening Q&A. [Name], first question --"

**Seed Q1**: "How does CEXAI compare to LangChain?" -- LangChain runs agents; CEXAI persists what they produce. Complementary.

**Seed Q2**: "Do I need Claude? Can I use local models?" -- Four runtimes: Claude, Codex, Gemini, Ollama. One YAML config.

**Seed Q3**: "What does onboarding 10 engineers look like?" -- /init in 2 min. Shared repo = same quality gates for all.

Moderator: "One more, then recording link in chat."

[SPEAKER NOTE: No questions at 60 sec? Read Seed Q1 immediately.]

---

## Related Artifacts

| Artifact | Rel | Score |
|----------|-----|-------|
| [[p01_kc_cex_as_digital_asset]] | upstream | 0.30 |
| [[bld_examples_webinar_script]] | downstream | 0.28 |
| [[n02_marketing]] | related | 0.28 |
| [[n05_operations]] | downstream | 0.27 |
| [[p03_sp_cex_core_identity]] | upstream | 0.26 |
| [[n01_intelligence]] | downstream | 0.26 |
| [[p03_sp_kind_builder]] | upstream | 0.26 |
| [[bld_schema_webinar_script]] | upstream | 0.25 |
| [[p03_qg_webinar_script]] | upstream | 0.25 |
| [[brand_bootstrap]] | related | 0.24 |
