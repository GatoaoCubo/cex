# TTS Free — Optional Features Note

**Domain**: llm_platforms
**Type**: concept
**Quality**: 0.82

## Voice & Audio (Optional)

> **IMPORTANT**: Voice features work WITHOUT any API keys!

Edge TTS (Microsoft) is the default free provider. No API key required.
ElevenLabs and OpenAI TTS are optional premium upgrades.

## Free Setup

```bash
pip install edge-tts
# No API key needed - works immediately
```

## Optional Premium

```bash
# ElevenLabs (better quality)
export ELEVENLABS_API_KEY=your_key_here

# OpenAI TTS (GPT ecosystem)
export OPENAI_API_KEY=your_key_here
```

---
**Imported**: 2025-12-10 | **From**: mentor_sistemas_agent
