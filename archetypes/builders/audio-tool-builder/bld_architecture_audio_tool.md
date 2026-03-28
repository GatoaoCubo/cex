---
kind: architecture
id: bld_architecture_audio_tool
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of audio_tool — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| direction | Processing direction — input (STT), output (TTS), analysis, bidirectional | audio_tool | required |
| model | Named audio model identifier — bound to specific provider and capability | audio_tool | required |
| format | Audio format for input/output — mp3, wav, ogg, flac, webm, m4a, aac, pcm | audio_tool | required |
| language | BCP-47 language code scoping model support | audio_tool | required |
| sample_rate | Hz value normalizing audio input for model accuracy | audio_tool | recommended |
| streaming | Real-time chunk processing flag — affects integration pattern | audio_tool | recommended |
| word_timestamps | Per-word timing output — enables subtitle sync and diarization | audio_tool | recommended |
| voice_id | Default TTS voice identifier for output direction tools | audio_tool | conditional |
| guardrail | Execution constraints — max_duration, rate caps, content filters | P11 | external |
| agent | Runtime caller that invokes the audio tool via API | P02 | consumer |
| notifier | Downstream consumer that delivers TTS audio output | P04 | consumer |
## Dependency Graph
```
format      --depends-->  model
language    --depends-->  model
sample_rate --depends-->  model
model       --produces--> transcript (direction: input)
model       --produces--> audio_bytes (direction: output)
model       --produces--> features (direction: analysis)
streaming   --modifies--> model
word_timestamps --modifies--> model
guardrail   --constrains--> model
agent       --invokes-->  direction
notifier    --consumes--> audio_bytes
```
| From | To | Type | Data |
|------|----|------|------|
| format | model | depends | audio format must be accepted by model |
| language | model | depends | language must be in model's supported list |
| sample_rate | model | depends | Hz value affects transcription accuracy |
| model | transcript | produces | text output for direction: input |
| model | audio_bytes | produces | audio output for direction: output |
| model | features | produces | JSON features for direction: analysis |
| streaming | model | modifies | enables chunked real-time processing |
| guardrail | model | constrains | max_duration, rate limit enforcement |
| agent | direction | invokes | agent selects direction and submits payload |
| notifier | audio_bytes | consumes | TTS output delivered to user channel |
## Boundary Table
| audio_tool IS | audio_tool IS NOT |
|---------------|------------------|
| Processes audio signals (speech, sound, music) | A visual processor — that is vision_tool |
| Converts speech to text (STT / direction: input) | A message delivery system — that is notifier |
| Generates speech from text (TTS / direction: output) | A terminal utility — that is cli_tool |
| Analyzes audio features (diarization, emotion, lang detect) | A generic HTTP client — that is api_client |
| Bound to specific audio models with known providers | A background persistent process — that is daemon |
| Format and language scoped at spec time | A video processor — that is vision_tool (video frames) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| configuration | language, sample_rate, voice_id | Scope model behavior — language, fidelity, voice |
| interface | direction, format, streaming | Define the audio surface — what callers send/receive |
| execution | model, word_timestamps | Process signal, produce output with optional metadata |
| governance | guardrail | Apply duration limits, rate caps, content filters |
| callers | agent, notifier | Runtime consumers that invoke the audio tool |
