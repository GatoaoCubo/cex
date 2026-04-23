---
kind: tools
id: bld_tools_audio_tool
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for audio_tool production
quality: 9.0
title: "Tools Audio Tool"
version: "1.0.0"
author: n03_builder
tags: [audio_tool, builder, examples]
tldr: "Golden and anti-examples for audio tool construction, demonstrating ideal structure and common pitfalls."
domain: "audio tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_cli_tool
  - bld_tools_client
  - bld_tools_function_def
  - bld_tools_retriever_config
  - bld_tools_input_schema
  - bld_tools_memory_scope
  - bld_tools_output_validator
  - bld_tools_prompt_version
  - bld_tools_path_config
  - bld_tools_runtime_rule
---

# Tools: audio-tool-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing audio_tool artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P04_tools/_schema.yaml | Field definitions, audio_tool kind |
| CEX Examples | P04_tools/examples/ | Real audio_tool artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_audio_tool |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
## Provider Reference
| Provider | API | Models | Direction |
|----------|-----|--------|-----------|
| OpenAI | api.openai.com/v1/audio | whisper_large_v3, tts_1, tts_1_hd | input + output |
| ElevenLabs | api.elevenlabs.io/v1 | eleven_multilingual_v2, eleven_turbo_v2_5 | output |
| Google | speech.googleapis.com | google_chirp, google_chirp_2 | input + analysis |
| Azure | *.cognitiveservices.azure.com | azure_neural_hd, azure_whisper | input + output |
| Deepgram | api.deepgram.com/v1 | deepgram_nova_2, deepgram_nova_2_medical | input |
| AssemblyAI | api.assemblyai.com/v2 | assemblyai_best, assemblyai_nano | input |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern `p04_audio_*`, direction valid enum,
models list matches body section, formats within allowed enum, languages use BCP-47,
body <= 2048 bytes, quality == null.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_cli_tool]] | sibling | 0.58 |
| [[bld_tools_client]] | sibling | 0.57 |
| [[bld_tools_function_def]] | sibling | 0.57 |
| [[bld_tools_retriever_config]] | sibling | 0.55 |
| [[bld_tools_input_schema]] | sibling | 0.55 |
| [[bld_tools_memory_scope]] | sibling | 0.55 |
| [[bld_tools_output_validator]] | sibling | 0.54 |
| [[bld_tools_prompt_version]] | sibling | 0.53 |
| [[bld_tools_path_config]] | sibling | 0.53 |
| [[bld_tools_runtime_rule]] | sibling | 0.53 |
