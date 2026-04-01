"""
cex_sdk.models — Model Provider Abstraction Layer

Absorbed from: agno/models/
CEX version: 7.1.0
Pillar: P02 (Model)
8F function: CALL (F5)

Provides a unified interface for calling any LLM provider:
  - Claude (Anthropic)
  - GPT-4 (OpenAI)
  - Gemini (Google)
  - Ollama (local)
  - OpenRouter (multi-provider)
  - LiteLLM (universal fallback)

Usage:
  from cex_sdk.models import get_model
  model = get_model("claude-sonnet-4-20250514")
  response = model.invoke(messages=[...])
"""
