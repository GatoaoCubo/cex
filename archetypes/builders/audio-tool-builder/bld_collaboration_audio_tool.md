---
kind: collaboration
id: bld_collaboration_audio_tool
pillar: P12
llm_function: COLLABORATE
purpose: How audio-tool-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: audio-tool-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what audio direction does this tool handle, and what models, formats, and languages does it support?"
I do not build vision tools. I do not define notifiers. I do not build CLI utilities.
I specify audio processing tools so agents and pipelines can invoke STT, TTS, and audio analysis operations.
## Crew Compositions
### Crew: "Voice Interface"
```
  1. audio-tool-builder -> "STT tool spec (models, formats, languages, streaming)"
  2. input-schema-builder -> "input validation for audio upload parameters"
  3. formatter-builder -> "transcript output formatting (json, srt, vtt)"
```
### Crew: "Multimedia Pipeline"
```
  1. audio-tool-builder -> "audio processing tool (STT or TTS)"
  2. vision-tool-builder -> "visual processing tool (OCR, image analysis)"
  3. formatter-builder -> "unified output format for combined media results"
```
### Crew: "Content Production"
```
  1. audio-tool-builder -> "TTS synthesis tool (voice, format, language)"
  2. notifier-builder -> "delivery tool (sends audio to user channel)"
  3. hook-builder -> "event trigger on TTS completion"
```
## Handoff Protocol
### I Receive
- seeds: audio use case, direction (STT/TTS/analysis), required languages, latency requirement
- optional: preferred provider, format constraints, streaming requirement, voice_id for TTS
### I Produce
- audio_tool artifact (.md + .yaml frontmatter)
- committed to: `cex/P04/examples/p04_audio_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Audio tools can be defined standalone.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| hook-builder | Hooks may trigger audio tools on speech events |
| notifier-builder | Notifiers may invoke TTS to generate audio for delivery |
| instruction-builder | Recipes reference audio tools as voice I/O steps |
| agent-builder | Agents use audio_tool for voice input/output capabilities |
