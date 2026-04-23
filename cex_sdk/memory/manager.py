"""
cex_sdk.memory.manager -- LLM-powered memory extraction and management.

Absorbed from: agno/memory/manager.py + agno/learn/machine.py
CEX version: 9.2.0 | Pillar: P10 | 8F: INJECT (F3)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional

from cex_sdk.utils.log import log_debug


class LearningMode(str, Enum):
    """How memory is extracted and saved."""
    ALWAYS = "always"       # Auto-extract after each response
    AGENTIC = "agentic"     # Agent decides when to learn via tools
    PROPOSE = "propose"     # Agent proposes, human confirms (= GDP)
    HITL = "hitl"           # Human-in-the-loop


@dataclass
class MemoryEntry:
    """A single memory item."""
    id: str = ""
    content: str = ""
    memory_type: str = "observation"  # observation | fact | preference | decision
    confidence: float = 1.0
    source: str = ""
    created_at: str = ""
    tags: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in self.__dict__.items() if v}


@dataclass
class MemoryManager:
    """LLM-powered memory extraction and management.

    Maps to CEX P10 memory kinds:
    - user_profile -> entity_memory (P10)
    - user_memory -> learning_record (P10)
    - session_context -> session_state (P10)
    - learned_knowledge -> knowledge_card (P01, auto-generated)
    - decision_log -> GDP decision_manifest
    """

    memories: List[MemoryEntry] = field(default_factory=list)
    mode: LearningMode = LearningMode.ALWAYS
    max_memories: int = 100

    # Persistence
    _store_path: Optional[str] = None

    def __init__(
        self,
        mode: LearningMode = LearningMode.ALWAYS,
        max_memories: int = 100,
        store_path: Optional[str] = None,
    ):
        self.memories = []
        self.mode = mode
        self.max_memories = max_memories
        self._store_path = store_path
        if store_path:
            self._load()

    def add(self, content: str, memory_type: str = "observation", **kwargs) -> MemoryEntry:
        """Add a memory entry."""
        from datetime import datetime
        from uuid import uuid4
        entry = MemoryEntry(
            id=str(uuid4())[:8],
            content=content,
            memory_type=memory_type,
            created_at=datetime.now().isoformat(),
            **kwargs,
        )
        self.memories.append(entry)
        self._prune()
        self._save()
        log_debug(f"Memory added: [{memory_type}] {content[:80]}")
        return entry

    def search(self, query: str, top_k: int = 5) -> List[MemoryEntry]:
        """Simple keyword search over memories."""
        query_lower = query.lower()
        scored = []
        for m in self.memories:
            score = sum(1 for word in query_lower.split() if word in m.content.lower())
            if score > 0:
                scored.append((score, m))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [m for _, m in scored[:top_k]]

    def get_context(self, query: str = "", max_tokens: int = 2000) -> str:
        """Get memory context string for prompt injection (F3 INJECT)."""
        relevant = self.search(query, top_k=10) if query else self.memories[-10:]
        if not relevant:
            return ""

        lines = ["## Memory Context"]
        total = 0
        for m in relevant:
            line = f"- [{m.memory_type}] {m.content}"
            total += len(line) // 4  # rough token estimate
            if total > max_tokens:
                break
            lines.append(line)
        return "\n".join(lines)

    def update(self, memory_id: str, content: str) -> bool:
        """Update an existing memory."""
        for m in self.memories:
            if m.id == memory_id:
                m.content = content
                self._save()
                return True
        return False

    def delete(self, memory_id: str) -> bool:
        """Delete a memory by ID."""
        before = len(self.memories)
        self.memories = [m for m in self.memories if m.id != memory_id]
        if len(self.memories) < before:
            self._save()
            return True
        return False

    def clear(self) -> None:
        """Clear all memories."""
        self.memories = []
        self._save()

    def _prune(self) -> None:
        """Remove oldest memories if over limit."""
        if len(self.memories) > self.max_memories:
            self.memories = self.memories[-self.max_memories:]

    def _save(self) -> None:
        if not self._store_path:
            return
        import os
        os.makedirs(os.path.dirname(self._store_path), exist_ok=True)
        with open(self._store_path, "w", encoding="utf-8") as f:
            json.dump([m.to_dict() for m in self.memories], f, ensure_ascii=False, indent=2)

    def _load(self) -> None:
        if not self._store_path:
            return
        import os
        if not os.path.exists(self._store_path):
            return
        with open(self._store_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.memories = [MemoryEntry(**d) for d in data]

    def __len__(self) -> int:
        return len(self.memories)
