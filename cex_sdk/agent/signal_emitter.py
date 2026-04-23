# cex_sdk.agent.signal_emitter -- F8 COLLABORATE: write completion signal JSON
# kind: signal / pillar: P12 / 8F: F8 COLLABORATE
# -*- coding: ascii -*-
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def _find_repo_root(start: Path) -> Path:
    current = start.resolve()
    for _ in range(10):
        if (current / "CLAUDE.md").exists():
            return current
        parent = current.parent
        if parent == current:
            break
        current = parent
    return start.resolve()


class SignalEmitter:
    """Writes a CEX completion signal to .cex/runtime/signals/."""

    def __init__(self, repo_root: str = "") -> None:
        if repo_root:
            self.root = Path(repo_root).resolve()
        else:
            self.root = _find_repo_root(Path(__file__).parent)
        self.signals_dir = self.root / ".cex" / "runtime" / "signals"

    def emit(
        self,
        nucleus: str,
        status: str,
        score: float,
        kind: str = "",
        mission: str = None,
        wave: int = None,
    ) -> str:
        """Write signal JSON and return the file path string."""
        self.signals_dir.mkdir(parents=True, exist_ok=True)
        now = datetime.now(timezone.utc)
        ts = now.strftime("%Y%m%d_%H%M%S")
        filename = f"signal_{nucleus}_{ts}.json"
        path = self.signals_dir / filename

        payload = {
            "nucleus": nucleus,
            "status": status,
            "quality_score": score,
            "mission": mission,
            "kind": kind,
            "timestamp": now.isoformat(),
            "source": "cex_sdk.agent",
        }
        if wave is not None:
            payload["wave"] = wave
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return str(path)
