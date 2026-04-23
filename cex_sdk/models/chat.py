# cex_sdk.models.chat -- thin synchronous LLM convenience API
# kind: model_provider / pillar: P02 / 8F: F5 CALL
# -*- coding: ascii -*-
from __future__ import annotations

import os
import sys
from typing import Any

# Resolve default model from nucleus_models.yaml (graceful fallback)
try:
    _tools_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_tools")
    if _tools_dir not in sys.path:
        sys.path.insert(0, os.path.normpath(_tools_dir))
    from cex_model_resolver import resolve_model_for_tool
    _CHAT_DEFAULT_MODEL = resolve_model_for_tool("chat", "standard")["model"]
except Exception:
    _CHAT_DEFAULT_MODEL = "claude-sonnet-4-6"


def chat(
    prompt: str,
    *,
    model: str = _CHAT_DEFAULT_MODEL,
    provider: str = "auto",
    max_tokens: int = 4096,
    system: str = "",
    **kwargs: Any,
) -> str:
    """
    Thin synchronous LLM call. Returns response text.
    provider: "auto" (detect from model name), "anthropic", "openai", "ollama"
    """
    resolved = _resolve_provider(provider, model)
    if resolved == "anthropic":
        return _call_anthropic(prompt, model=model, max_tokens=max_tokens, system=system, **kwargs)
    if resolved == "openai":
        return _call_openai(prompt, model=model, max_tokens=max_tokens, system=system, **kwargs)
    return _call_ollama(prompt, model=model, max_tokens=max_tokens, system=system, **kwargs)


def _resolve_provider(provider: str, model: str) -> str:
    if provider != "auto":
        return provider
    if model.startswith("claude-"):
        return "anthropic"
    if model.startswith(("gpt-", "o1-", "o3-")):
        return "openai"
    return "ollama"


def _call_anthropic(
    prompt: str,
    *,
    model: str,
    max_tokens: int,
    system: str,
    **kwargs: Any,
) -> str:
    import anthropic  # type: ignore[import]

    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    msgs: list[dict[str, str]] = [{"role": "user", "content": prompt}]
    create_kwargs: dict[str, Any] = dict(model=model, max_tokens=max_tokens, messages=msgs)
    if system:
        create_kwargs["system"] = system
    create_kwargs.update(kwargs)
    resp = client.messages.create(**create_kwargs)
    return resp.content[0].text


def _call_openai(
    prompt: str,
    *,
    model: str,
    max_tokens: int,
    system: str,
    **kwargs: Any,
) -> str:
    from openai import OpenAI  # type: ignore[import]

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    msgs: list[dict[str, str]] = []
    if system:
        msgs.append({"role": "system", "content": system})
    msgs.append({"role": "user", "content": prompt})
    create_kwargs: dict[str, Any] = dict(model=model, max_tokens=max_tokens, messages=msgs)
    create_kwargs.update(kwargs)
    resp = client.chat.completions.create(**create_kwargs)
    return resp.choices[0].message.content or ""


def _call_ollama(
    prompt: str,
    *,
    model: str,
    max_tokens: int,
    system: str,
    **kwargs: Any,
) -> str:
    import requests  # type: ignore[import]

    base_url = os.environ.get("OLLAMA_URL", "http://localhost:11434")
    msgs: list[dict[str, str]] = []
    if system:
        msgs.append({"role": "system", "content": system})
    msgs.append({"role": "user", "content": prompt})
    payload: dict[str, Any] = {"model": model, "messages": msgs, "stream": False}
    resp = requests.post(f"{base_url}/api/chat", json=payload, timeout=60)
    resp.raise_for_status()
    data: dict[str, Any] = resp.json()
    return data["message"]["content"]
