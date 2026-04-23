"""
cex_sdk.models.providers.google -- Google Gemini provider.

CEX version: 7.1.0 | Pillar: P02 | 8F: CALL (F5)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Type, Union

from pydantic import BaseModel

from cex_sdk.models.base import Model
from cex_sdk.models.message import Message
from cex_sdk.models.response import ModelResponse
from cex_sdk.utils.timer import Timer


@dataclass
class Gemini(Model):
    """Google Gemini models."""

    id: str = "gemini-2.5-pro"
    provider: str = "Google"
    api_key: Optional[str] = None

    def _get_client(self):
        try:
            from google import genai
        except ImportError:
            raise ImportError("pip install google-genai")
        import os
        return genai.Client(api_key=self.api_key or os.environ.get("GOOGLE_API_KEY"))

    def invoke(
        self,
        messages: List[Message],
        *,
        tools: Optional[List[Dict[str, Any]]] = None,
        tool_choice: Optional[Union[str, Dict[str, Any]]] = None,
        response_model: Optional[Type[BaseModel]] = None,
        **kwargs: Any,
    ) -> ModelResponse:
        client = self._get_client()
        timer = Timer().start()

        contents = []
        system_instruction = None
        for m in messages:
            if m.role == "system":
                system_instruction = m.get_content_string()
            else:
                role = "model" if m.role == "assistant" else "user"
                contents.append({"role": role, "parts": [{"text": m.get_content_string()}]})

        config: Dict[str, Any] = {}
        if self.max_tokens:
            config["max_output_tokens"] = self.max_tokens
        if self.temperature is not None:
            config["temperature"] = self.temperature
        if system_instruction:
            config["system_instruction"] = system_instruction

        response = client.models.generate_content(
            model=self.id,
            contents=contents,
            config=config if config else None,
        )

        content = response.text or ""
        usage = {}
        if hasattr(response, "usage_metadata") and response.usage_metadata:
            um = response.usage_metadata
            usage = {
                "input_tokens": getattr(um, "prompt_token_count", 0) or 0,
                "output_tokens": getattr(um, "candidates_token_count", 0) or 0,
                "total_tokens": getattr(um, "total_token_count", 0) or 0,
            }

        return ModelResponse(
            role="assistant",
            content=content,
            response_usage=self._make_metrics(usage, timer),
            input_tokens=usage.get("input_tokens", 0),
            output_tokens=usage.get("output_tokens", 0),
            total_tokens=usage.get("total_tokens", 0),
        )
