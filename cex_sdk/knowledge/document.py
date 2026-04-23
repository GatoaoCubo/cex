"""
cex_sdk.knowledge.document -- Document dataclass for knowledge pipeline.

CEX version: 8.0.0 | Pillar: P01 | 8F: INJECT (F3)
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Document:
    """A chunk of knowledge content with metadata."""

    content: str = ""
    id: Optional[str] = None
    name: Optional[str] = None
    meta_data: Dict[str, Any] = field(default_factory=dict)
    embedding: Optional[List[float]] = None

    def __post_init__(self):
        if not self.id:
            self.id = hashlib.md5(self.content.encode(), usedforsecurity=False).hexdigest()

    @property
    def content_hash(self) -> str:
        return hashlib.md5(self.content.encode(), usedforsecurity=False).hexdigest()

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {"id": self.id, "content": self.content}
        if self.name:
            d["name"] = self.name
        if self.meta_data:
            d["meta_data"] = self.meta_data
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Document:
        return cls(
            content=data.get("content", ""),
            id=data.get("id"),
            name=data.get("name"),
            meta_data=data.get("meta_data", {}),
        )
