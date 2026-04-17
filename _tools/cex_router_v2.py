#!/usr/bin/env python3
"""cex_router_v2: Hybrid Claude/Ollama routing based on task characteristics.

Reads a task spec (YAML or JSON) describing the work, queries provider health,
and returns the recommended backend alias + reasoning.

Usage:
    python _tools/cex_router_v2.py --task .cex/runtime/handoffs/n01_task.md
    python _tools/cex_router_v2.py --signature production_kc --grid-size 6

Signatures:
    production_kc        -> citation-sensitive, no fabrication allowed
    structural_scaffold  -> frontmatter + skeleton, cheap OK
    evolve_loop          -> high volume, must be free
    smoke_test           -> trivial output verification
    brand_copy           -> voice-critical
    grid_parallel        -> multiple nuclei concurrent
    unknown              -> default free tier
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent.parent

# Backend aliases (match litellm_config.yaml and Anthropic API)
BACKEND_OLLAMA_SMALL = "ollama/qwen3:8b"
BACKEND_OLLAMA_LARGE = "ollama/qwen3:14b"
BACKEND_CLAUDE_SONNET = "claude-sonnet-4-6"
BACKEND_CLAUDE_OPUS = "claude-opus-4-6"


def anthropic_credit_ok() -> bool:
    """Quick check: does Anthropic API key exist AND credit > 0?

    Returns False if ANTHROPIC_API_KEY missing or last known status was 400.
    Checks cached quota state from cex_quota_check.py if present.
    """
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        return False

    cache = ROOT / ".cex" / "runtime" / "quota_state.json"
    if cache.exists():
        try:
            state = json.loads(cache.read_text())
            anthropic = state.get("anthropic", {})
            if anthropic.get("last_error_code") == 400:
                return False
            if anthropic.get("credit_exhausted"):
                return False
        except Exception:
            pass
    return True


def gemini_key_ok() -> bool:
    return bool(os.environ.get("GEMINI_API_KEY", "").strip())


def pick_backend(signature: str, grid_size: int = 1, require_accuracy: bool = False) -> dict:
    """Return {backend, reason, fallback} for given task characteristics."""
    credit = anthropic_credit_ok()

    if signature == "production_kc" or require_accuracy:
        if credit:
            return {
                "backend": BACKEND_CLAUDE_OPUS,
                "reason": "citation-sensitive; fabrication = bug",
                "fallback": BACKEND_OLLAMA_LARGE + " + human_review",
            }
        return {
            "backend": BACKEND_OLLAMA_LARGE,
            "reason": "no Anthropic credit; fabrication risk accepted with human review",
            "fallback": "human_only",
        }

    if signature == "structural_scaffold":
        return {
            "backend": BACKEND_OLLAMA_SMALL,
            "reason": "deterministic frontmatter + skeleton; small model sufficient",
            "fallback": BACKEND_OLLAMA_LARGE,
        }

    if signature == "evolve_loop":
        return {
            "backend": BACKEND_OLLAMA_LARGE,
            "reason": "high-volume iteration; cost forbids paid API",
            "fallback": BACKEND_OLLAMA_SMALL,
        }

    if signature == "smoke_test":
        return {
            "backend": BACKEND_OLLAMA_SMALL,
            "reason": "trivial verification; any free model works",
            "fallback": BACKEND_OLLAMA_LARGE,
        }

    if signature == "brand_copy":
        if credit:
            return {
                "backend": BACKEND_CLAUDE_SONNET,
                "reason": "voice-critical; Sonnet sufficient for copy",
                "fallback": BACKEND_OLLAMA_LARGE + " + N02_polish",
            }
        return {
            "backend": BACKEND_OLLAMA_LARGE,
            "reason": "no credit; voice may drift",
            "fallback": "human_only",
        }

    if signature == "grid_parallel" or grid_size >= 4:
        if credit:
            return {
                "backend": BACKEND_CLAUDE_SONNET,
                "reason": f"grid_size={grid_size}; paid API gives real parallelism",
                "fallback": BACKEND_OLLAMA_LARGE + " (serialized on GPU)",
            }
        return {
            "backend": BACKEND_OLLAMA_LARGE,
            "reason": f"grid_size={grid_size}; serialized on single GPU, ~{grid_size * 40}s",
            "fallback": BACKEND_OLLAMA_SMALL,
        }

    return {
        "backend": BACKEND_OLLAMA_LARGE,
        "reason": "default free tier; upgrade signature for better routing",
        "fallback": BACKEND_OLLAMA_SMALL,
    }


def infer_signature_from_handoff(handoff_path: Path) -> str:
    """Heuristic: parse handoff text for signature clues."""
    if not handoff_path.exists():
        return "unknown"
    text = handoff_path.read_text(encoding="utf-8", errors="ignore").lower()

    if "kind: knowledge_card" in text or "kind: decision_record" in text:
        return "production_kc"
    if "smoke" in text or "trivial" in text:
        return "smoke_test"
    if "/evolve" in text or "cycle" in text:
        return "evolve_loop"
    if "kind: tagline" in text or "kind: landing_page" in text or "brand" in text:
        return "brand_copy"
    if "frontmatter only" in text or "scaffold" in text:
        return "structural_scaffold"
    return "unknown"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--task", help="Path to handoff file for signature inference")
    p.add_argument("--signature", default=None)
    p.add_argument("--grid-size", type=int, default=1)
    p.add_argument("--require-accuracy", action="store_true")
    p.add_argument("--json", action="store_true", help="Emit raw JSON")
    args = p.parse_args()

    sig = args.signature
    if not sig and args.task:
        sig = infer_signature_from_handoff(Path(args.task))
    if not sig:
        sig = "unknown"

    decision = pick_backend(sig, grid_size=args.grid_size, require_accuracy=args.require_accuracy)
    decision["signature"] = sig
    decision["anthropic_credit_ok"] = anthropic_credit_ok()
    decision["gemini_key_ok"] = gemini_key_ok()

    if args.json:
        print(json.dumps(decision, indent=2))
    else:
        print(f"signature: {sig}")
        print(f"backend:   {decision['backend']}")
        print(f"reason:    {decision['reason']}")
        print(f"fallback:  {decision['fallback']}")
        print(f"anthropic_credit_ok: {decision['anthropic_credit_ok']}")
        print(f"gemini_key_ok:       {decision['gemini_key_ok']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
