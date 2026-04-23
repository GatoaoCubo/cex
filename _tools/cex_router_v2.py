#!/usr/bin/env python3
"""cex_router_v2: Hybrid Claude/Ollama routing based on task + kind metadata.

Two routing layers:
  1. Kind-based (from kinds_meta.json): requires_live_tools -> Claude-only,
     requires_external_context -> any runtime after N07 pre-flight.
  2. Signature-based (heuristic): production_kc, structural_scaffold, etc.

Kind routing takes precedence when --kind is provided. Signature routing is
the fallback for legacy callers and handoff-inferred tasks.

Usage:
    python _tools/cex_router_v2.py --kind browser_tool
    python _tools/cex_router_v2.py --kind knowledge_card --task handoff.md
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
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Backend aliases (resolved from nucleus_models.yaml via cex_model_resolver)
try:
    from cex_model_resolver import get_ollama_config as _get_ollama
    from cex_model_resolver import resolve_model_for_tool as _resolve_tool
    _ollama_cfg = _get_ollama()
    BACKEND_OLLAMA_SMALL = "ollama/" + _ollama_cfg["models"].get("light", "qwen3:8b")
    BACKEND_OLLAMA_LARGE = "ollama/" + _ollama_cfg["models"].get("heavy", "qwen3:14b")
    BACKEND_CLAUDE_SONNET = _resolve_tool("cex_router_v2", "standard")["model"]
    BACKEND_CLAUDE_OPUS = _resolve_tool("cex_router_v2", "heavy")["model"]
except Exception:
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


# ---------------------------------------------------------------------------
# Kind metadata routing (W4: PREFLIGHT_EXPANSION)
# ---------------------------------------------------------------------------

KINDS_META_PATH = ROOT / ".cex" / "kinds_meta.json"

_kinds_meta_cache: dict[str, Any] | None = None


def _load_kinds_meta() -> dict[str, Any]:
    """Load kinds_meta.json with single-load cache."""
    global _kinds_meta_cache
    if _kinds_meta_cache is not None:
        return _kinds_meta_cache
    if not KINDS_META_PATH.exists():
        return {}
    try:
        _kinds_meta_cache = json.loads(
            KINDS_META_PATH.read_text(encoding="utf-8"))
        return _kinds_meta_cache
    except Exception:
        return {}


def get_kind_metadata(kind: str) -> dict[str, Any]:
    """Return metadata dict for a kind, or empty dict if unknown."""
    if not kind:
        return {}
    meta = _load_kinds_meta()
    return meta.get(kind, {})


def route_by_kind(
    kind: str,
    grid_size: int = 1,
    signature: str = "",
) -> dict[str, Any] | None:
    """Kind-based routing decision tree (spec W4).

    Returns a routing dict if the kind triggers a rule, or None to fall
    through to signature-based routing.

    Decision tree:
      1. requires_live_tools=True  -> Claude-only (MCP needed at runtime)
      2. requires_external_context -> note in metadata (pre-flight handles it)
      3. Otherwise                 -> None (fall through to pick_backend)
    """
    km = get_kind_metadata(kind)
    if not km:
        return None

    credit = anthropic_credit_ok()

    # Rule 1: live tools required -> Claude-only
    if km.get("requires_live_tools", False):
        if credit:
            return {
                "backend": BACKEND_CLAUDE_OPUS,
                "reason": "kind=%s requires live MCP tools; Claude-only" % kind,
                "fallback": BACKEND_CLAUDE_SONNET,
                "kind_rule": "requires_live_tools",
                "preflight_needed": False,
            }
        return {
            "backend": BACKEND_CLAUDE_SONNET,
            "reason": "kind=%s requires live MCP tools; Claude-only (no Opus credit)" % kind,
            "fallback": "none (live tools mandatory)",
            "kind_rule": "requires_live_tools",
            "preflight_needed": False,
        }

    # Rule 2: external context -> any runtime OK after N07 pre-flight
    if km.get("requires_external_context", False):
        # Flag that pre-flight MCP gather should run before dispatch
        sig_decision = pick_backend(
            signature or "unknown", grid_size=grid_size
        )
        sig_decision["kind_rule"] = "requires_external_context"
        sig_decision["preflight_needed"] = True
        sig_decision["reason"] = (
            "kind=%s needs external context; "
            "N07 pre-flight gathers it, then %s handles generation"
            % (kind, sig_decision["backend"])
        )
        return sig_decision

    # No kind-level override -> fall through
    return None


def infer_kind_from_handoff(handoff_path: Path) -> str:
    """Extract kind from handoff frontmatter or body."""
    if not handoff_path.exists():
        return ""
    try:
        text = handoff_path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""
    match = re.search(r"kind[=:]\s*(\w+)", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return ""


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


def route_task(
    kind: str = "",
    signature: str = "",
    grid_size: int = 1,
    require_accuracy: bool = False,
    handoff_path: Path | None = None,
) -> dict[str, Any]:
    """Unified entry point: kind routing -> signature routing -> default.

    Callers can provide any combination of kind, signature, or handoff path.
    The function resolves missing values from the handoff and applies the
    decision tree in priority order.
    """
    # Resolve from handoff if needed
    if handoff_path and not kind:
        kind = infer_kind_from_handoff(handoff_path)
    if handoff_path and not signature:
        signature = infer_signature_from_handoff(handoff_path)
    if not signature:
        signature = "unknown"

    # Layer 1: kind-based routing (highest priority)
    if kind:
        kind_decision = route_by_kind(kind, grid_size=grid_size, signature=signature)
        if kind_decision:
            kind_decision.setdefault("signature", signature)
            kind_decision.setdefault("kind", kind)
            kind_decision["anthropic_credit_ok"] = anthropic_credit_ok()
            kind_decision["gemini_key_ok"] = gemini_key_ok()
            return kind_decision

    # Layer 2: signature-based routing (fallback)
    decision = pick_backend(signature, grid_size=grid_size, require_accuracy=require_accuracy)
    decision["signature"] = signature
    decision["kind"] = kind
    decision["kind_rule"] = "none"
    decision["preflight_needed"] = False
    decision["anthropic_credit_ok"] = anthropic_credit_ok()
    decision["gemini_key_ok"] = gemini_key_ok()
    return decision


def main() -> int:
    p = argparse.ArgumentParser(
        description="CEX Router v2: kind-based + signature-based backend routing"
    )
    p.add_argument("--task", help="Path to handoff file for inference")
    p.add_argument("--kind", default=None, help="CEX kind (e.g., knowledge_card, browser_tool)")
    p.add_argument("--signature", default=None)
    p.add_argument("--grid-size", type=int, default=1)
    p.add_argument("--require-accuracy", action="store_true")
    p.add_argument("--json", action="store_true", help="Emit raw JSON")
    p.add_argument("--check-kind", metavar="KIND",
                   help="Check kind metadata and exit (requires_external_context, requires_live_tools)")
    args = p.parse_args()

    # Quick metadata check mode
    if args.check_kind:
        km = get_kind_metadata(args.check_kind)
        info = {
            "kind": args.check_kind,
            "requires_external_context": km.get("requires_external_context", False),
            "requires_live_tools": km.get("requires_live_tools", False),
            "found": bool(km),
        }
        if args.json:
            print(json.dumps(info, indent=2))
        else:
            for k, v in info.items():
                print("%s: %s" % (k, v))
        return 0

    handoff = Path(args.task) if args.task else None
    decision = route_task(
        kind=args.kind or "",
        signature=args.signature or "",
        grid_size=args.grid_size,
        require_accuracy=args.require_accuracy,
        handoff_path=handoff,
    )

    if args.json:
        print(json.dumps(decision, indent=2))
    else:
        print("kind:      %s" % decision.get("kind", ""))
        print("kind_rule: %s" % decision.get("kind_rule", "none"))
        print("preflight: %s" % decision.get("preflight_needed", False))
        print("signature: %s" % decision.get("signature", ""))
        print("backend:   %s" % decision["backend"])
        print("reason:    %s" % decision["reason"])
        print("fallback:  %s" % decision["fallback"])
        print("anthropic_credit_ok: %s" % decision["anthropic_credit_ok"])
        print("gemini_key_ok:       %s" % decision["gemini_key_ok"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
