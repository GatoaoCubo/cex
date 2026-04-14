---
kind: instruction
id: bld_instruction_prosody_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for prosody_config
quality: 8.9
title: "Instruction Prosody Config"
version: "1.1.0"
author: n03_hybrid_review2
tags: [prosody_config, builder, instruction, ssml]
tldr: "Step-by-step production process -- determine emission path, map emotions, emit SSML or native payload"
domain: "prosody_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

## Phase 1: RESEARCH
1. Identify target tts_provider(s) -- SSML-compliant (Azure/Google/AWS/IBM) vs native-only (ElevenLabs/Cartesia/Hume/PlayHT).
2. Load provider matrix from KC; select emission path per target.
3. Gather emotion requirements -- name each emotion, map to circumplex (valence, arousal).
4. Check language/locale (BCP-47) -- pitch/rate norms differ across locales.
5. Review existing prosody_config artifacts in P09 for reusable baselines (template-first).
6. Document numeric ranges: pitch in Hz or %, rate 50-200%, volume in dB or enum.

## Phase 2: COMPOSE
1. Write frontmatter: id (p09_prs_*), kind, pillar=P09, version (semver), quality: null, emission enum.
2. Define `baseline` block with neutral pitch/rate/volume.
3. For each emotion, add a named entry under `emotions:` keyed by slug.
4. If emission=ssml: emit `ssml:` multiline block wrapping `{{text}}` with `<prosody>`, `<break>`, `<emphasis>`.
5. If emission=elevenlabs: emit `voice_settings: {stability, similarity_boost, style, use_speaker_boost}`.
6. If emission=playht: emit `emotion:` enum from [female_happy, male_happy, female_sad, ...] + `speed`.
7. If emission=cartesia: emit `text_template` with inline `[emotion]` and `[pause:Nms]` directives.
8. If emission=hume: emit free-text `description:` (e.g., "excited whisper at moderate pace").
9. Declare `target_providers:` array so downstream validators know which rendering paths to exercise.
10. Never embed API keys, model weights, agent persona text, or audio bytes.

## Phase 3: VALIDATE
- [ ] `quality: null` in frontmatter (peer review assigns).
- [ ] `id` matches `^p09_prs_[a-z0-9_-]+\.yaml$`.
- [ ] `emission` enum present and consistent with payload shape.
- [ ] SSML strings parse against W3C SSML 1.1 (when emission=ssml).
- [ ] Numeric ranges within provider limits (ElevenLabs sliders 0.0-1.0, pitch +/-50%).
- [ ] No tts_provider keys, no agent_profile text, no secrets.
- [ ] At least one emotion variant differs measurably from baseline.
- [ ] `target_providers` declared and reachable via tts_provider artifacts.
- [ ] Round-trip render test passes on primary target provider.
