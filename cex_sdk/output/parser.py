"""
cex_sdk.output.parser -- Structured output parser for LLM responses.

kind: parser
pillar: P05
"""
# -*- coding: ascii -*-
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ParseResult:
    """Parsed artifact with frontmatter and body sections."""
    frontmatter: dict[str, Any] = field(default_factory=dict)
    body: str = ""
    sections: dict[str, str] = field(default_factory=dict)
    raw: str = ""
    parse_errors: list[str] = field(default_factory=list)

    @property
    def kind(self) -> str:
        return self.frontmatter.get("kind", "")

    @property
    def quality(self) -> float | None:
        q = self.frontmatter.get("quality")
        return float(q) if q is not None else None


_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
_SECTION_RE = re.compile(r"^#{1,3}\s+(.+)$", re.MULTILINE)


class Parser:
    """
    Parser extracts structured data from LLM output.

    8F position: F7 GOVERN (validate structure) + F3 INJECT (parse KC for retrieval).
    kind: parser
    pillar: P05
    """

    def parse_markdown(self, text: str) -> ParseResult:
        result = ParseResult(raw=text)
        m = _FRONTMATTER_RE.match(text)
        if m:
            result.frontmatter = self._parse_simple_yaml(m.group(1))
            result.body = text[m.end():]
        else:
            result.body = text
            result.parse_errors.append("no_frontmatter")
        result.sections = self._extract_sections(result.body)
        return result

    def parse_json_block(self, text: str) -> dict[str, Any]:
        """Extract JSON from a markdown code block."""
        m = re.search(r"```(?:json)?\n(.*?)```", text, re.DOTALL)
        if m:
            return json.loads(m.group(1))
        return json.loads(text)

    def _parse_simple_yaml(self, yaml_text: str) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for line in yaml_text.splitlines():
            if ":" in line:
                k, _, v = line.partition(":")
                result[k.strip()] = v.strip().strip('"').strip("'")
        return result

    def _extract_sections(self, body: str) -> dict[str, str]:
        sections: dict[str, str] = {}
        headings = list(_SECTION_RE.finditer(body))
        for i, m in enumerate(headings):
            start = m.end()
            end = headings[i + 1].start() if i + 1 < len(headings) else len(body)
            sections[m.group(1).strip()] = body[start:end].strip()
        return sections
