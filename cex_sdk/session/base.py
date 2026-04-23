"""
cex_sdk.session.base -- Session state management.

CEX version: 10.4.0 | Pillar: P10 | 8F: INJECT (F3)
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import uuid4


@dataclass
class Session:
    """Per-user, per-session state container.

    Persists to .cex/runtime/sessions/ as JSON.
    """

    session_id: str = field(default_factory=lambda: str(uuid4())[:12])
    user_id: Optional[str] = None
    state: Dict[str, Any] = field(default_factory=dict)
    history: List[Dict[str, Any]] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

    _store_dir: Optional[str] = field(default=None, repr=False)

    def __post_init__(self):
        if self._store_dir is None:
            self._store_dir = os.path.join(".cex", "runtime", "sessions")

    def set(self, key: str, value: Any) -> None:
        self.state[key] = value
        self.updated_at = datetime.now().isoformat()

    def get(self, key: str, default: Any = None) -> Any:
        return self.state.get(key, default)

    def add_message(self, role: str, content: str) -> None:
        self.history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
        })
        self.updated_at = datetime.now().isoformat()

    def get_history(self, last_n: int = 10) -> List[Dict[str, Any]]:
        return self.history[-last_n:]

    def save(self) -> str:
        """Persist session to disk."""
        os.makedirs(self._store_dir, exist_ok=True)
        path = os.path.join(self._store_dir, f"{self.session_id}.json")
        data = {
            "session_id": self.session_id,
            "user_id": self.user_id,
            "state": self.state,
            "history": self.history[-100:],  # Keep last 100 messages
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return path

    @classmethod
    def load(cls, session_id: str, store_dir: Optional[str] = None) -> Optional[Session]:
        """Load session from disk."""
        store = store_dir or os.path.join(".cex", "runtime", "sessions")
        path = os.path.join(store, f"{session_id}.json")
        if not os.path.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(
            session_id=data["session_id"],
            user_id=data.get("user_id"),
            state=data.get("state", {}),
            history=data.get("history", []),
            created_at=data.get("created_at", ""),
            updated_at=data.get("updated_at", ""),
            _store_dir=store,
        )

    def clear(self) -> None:
        self.state = {}
        self.history = []
        self.updated_at = datetime.now().isoformat()
