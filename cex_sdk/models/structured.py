"""
cex_sdk.models.structured -- Pydantic structured output parsing.

CEX version: 7.4.0 | Pillar: P06 | 8F: PRODUCE (F6)

Parses LLM text output into validated Pydantic models.
"""

from __future__ import annotations

import json
import re
from typing import Any, Optional, Type, TypeVar

from pydantic import BaseModel, ValidationError

from cex_sdk.utils.log import log_warning

T = TypeVar("T", bound=BaseModel)


def parse_structured_output(
    text: str,
    model_class: Type[T],
    *,
    strict: bool = False,
) -> Optional[T]:
    """Parse LLM text response into a Pydantic model.

    Tries multiple extraction strategies:
    1. Direct JSON parse
    2. Extract JSON from markdown code blocks
    3. Extract JSON from text (first { to last })
    4. If strict=False, attempt partial field extraction

    Args:
        text: Raw LLM response text.
        model_class: Pydantic model class to parse into.
        strict: If True, raise on failure. If False, return None.

    Returns:
        Validated model instance, or None if parsing fails.
    """
    # Strategy 1: Direct parse
    try:
        data = json.loads(text)
        return model_class.model_validate(data)
    except (json.JSONDecodeError, ValidationError):
        pass

    # Strategy 2: Extract from markdown code block
    code_block = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", text, re.DOTALL)
    if code_block:
        try:
            data = json.loads(code_block.group(1).strip())
            return model_class.model_validate(data)
        except (json.JSONDecodeError, ValidationError):
            pass

    # Strategy 3: Find JSON object in text
    brace_start = text.find("{")
    brace_end = text.rfind("}")
    if brace_start != -1 and brace_end > brace_start:
        try:
            data = json.loads(text[brace_start : brace_end + 1])
            return model_class.model_validate(data)
        except (json.JSONDecodeError, ValidationError):
            pass

    # Strategy 4: Find JSON array in text
    arr_start = text.find("[")
    arr_end = text.rfind("]")
    if arr_start != -1 and arr_end > arr_start:
        try:
            data = json.loads(text[arr_start : arr_end + 1])
            return model_class.model_validate(data)
        except (json.JSONDecodeError, ValidationError):
            pass

    if strict:
        raise ValueError(f"Failed to parse structured output from text into {model_class.__name__}")

    log_warning(f"Could not parse structured output into {model_class.__name__}")
    return None


# ---------------------------------------------------------------------------
# Common CEX models for structured output
# ---------------------------------------------------------------------------


class KnowledgeCardOutput(BaseModel):
    """Structured output for P01 knowledge_card kind."""
    id: str
    title: str
    kind: str = "knowledge_card"
    pillar: str = "P01"
    domain: str = ""
    tldr: str = ""
    tags: list[str] = []
    content: str = ""
    quality: Optional[float] = None


class AgentSpecOutput(BaseModel):
    """Structured output for P02 agent kind."""
    id: str
    name: str
    kind: str = "agent"
    pillar: str = "P02"
    domain: str = ""
    capabilities: list[str] = []
    tools: list[str] = []
    system_prompt: str = ""


class FunctionDefOutput(BaseModel):
    """Structured output for P04 function_def kind."""
    name: str
    description: str
    parameters: dict[str, Any] = {}
    returns: str = "string"


class EvalResultOutput(BaseModel):
    """Structured output for P07 eval results."""
    passed: bool
    score: float = 0.0
    notes: list[str] = []
    issues: list[str] = []
