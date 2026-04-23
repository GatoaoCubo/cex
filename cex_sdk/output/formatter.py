"""
cex_sdk.output.formatter -- Artifact output formatter.

kind: formatter
pillar: P05
"""
# -*- coding: ascii -*-
from __future__ import annotations

import json
import textwrap
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class OutputFormat(str, Enum):
    MARKDOWN = "markdown"
    JSON = "json"
    YAML = "yaml"
    TABLE = "table"
    PLAIN = "plain"


@dataclass
class ResponseFormat:
    """kind: response_format -- typed output contract."""
    format: OutputFormat = OutputFormat.MARKDOWN
    max_chars: int = 8192
    include_frontmatter: bool = True
    structured: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)


class Formatter:
    """
    Formatter converts raw LLM output into typed artifact format.

    8F position: F6 PRODUCE (output shaping) + F8 COLLABORATE (file write).
    kind: formatter
    pillar: P05
    """

    def __init__(self, response_format: ResponseFormat | None = None) -> None:
        self.format = response_format or ResponseFormat()

    def format_markdown(self, content: str, frontmatter: dict[str, Any] | None = None) -> str:
        """Format content as Markdown with optional YAML frontmatter."""
        parts: list[str] = []
        if self.format.include_frontmatter and frontmatter:
            parts.append("---")
            for k, v in frontmatter.items():
                parts.append(f"{k}: {v}")
            parts.append("---")
            parts.append("")
        parts.append(content)
        result = "\n".join(parts)
        if self.format.max_chars and len(result) > self.format.max_chars:
            result = result[: self.format.max_chars]
        return result

    def format_json(self, data: Any, indent: int = 2) -> str:
        """Format data as pretty-printed JSON."""
        return json.dumps(data, indent=indent, ensure_ascii=True, default=str)

    def format_table(self, rows: list[dict[str, Any]], headers: list[str] | None = None) -> str:
        """Format list of dicts as Markdown table."""
        if not rows:
            return ""
        cols = headers or list(rows[0].keys())
        widths = {c: len(c) for c in cols}
        for row in rows:
            for c in cols:
                widths[c] = max(widths[c], len(str(row.get(c, ""))))
        sep = "| " + " | ".join("-" * widths[c] for c in cols) + " |"
        header = "| " + " | ".join(c.ljust(widths[c]) for c in cols) + " |"
        lines = [header, sep]
        for row in rows:
            line = "| " + " | ".join(str(row.get(c, "")).ljust(widths[c]) for c in cols) + " |"
            lines.append(line)
        return "\n".join(lines)

    def truncate(self, text: str, width: int = 80, placeholder: str = "...") -> str:
        return textwrap.shorten(text, width=width, placeholder=placeholder)
