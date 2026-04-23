# -*- coding: utf-8 -*-
"""
cex_shared.py -- Shared library for all CEX tools.

Single source of truth for common operations:
  - CEX_ROOT resolution
  - YAML frontmatter parsing/stripping
  - Builder spec loading
  - File I/O utilities
  - Signal writing

Every CEX tool should import from here instead of reimplementing.

Usage:
    from cex_shared import CEX_ROOT, parse_frontmatter, find_builder_dir
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from cex_errors import ConfigError

# =============================================================================
# CEX_ROOT -- Single resolution point
# =============================================================================

CEX_ROOT: Path = Path(__file__).resolve().parent.parent
"""Root directory of the CEX repository. All paths are relative to this."""

BUILDER_DIR: Path = CEX_ROOT / "archetypes" / "builders"
"""Directory containing all builder archetypes."""

KINDS_META_PATH: Path = CEX_ROOT / ".cex" / "kinds_meta.json"
"""Path to the kind registry."""

RUNTIME_DIR: Path = CEX_ROOT / ".cex" / "runtime"
"""Path to runtime state (handoffs, signals, pids)."""


# =============================================================================
# Frontmatter Operations (was duplicated 6x)
# =============================================================================


def parse_frontmatter(content: str) -> dict[str, Any] | None:
    """Parse YAML frontmatter from markdown content.

    Returns dict of frontmatter fields, or None if no valid frontmatter found.
    Handles standard --- delimiters.

    Args:
        content: Full markdown content with optional frontmatter.

    Returns:
        Dict of parsed YAML fields, or None if invalid/missing.
    """
    content = content.strip()
    if not content.startswith("---"):
        return None
    end = content.find("---", 3)
    if end < 0:
        return None
    try:
        result = yaml.safe_load(content[3:end])
        return result if isinstance(result, dict) else None
    except yaml.YAMLError:
        return None


def strip_frontmatter(text: str) -> str:
    """Remove YAML frontmatter, returning only the body content.

    Args:
        text: Full markdown text with optional frontmatter.

    Returns:
        Body content after the closing --- delimiter, stripped.
    """
    if text.startswith("---"):
        end = text.find("---", 3)
        if end > 0:
            return text[end + 3:].strip()
    return text


def extract_frontmatter_dict(text: str) -> dict[str, Any]:
    """Parse frontmatter with LLM-output tolerance.

    Handles:
    - Standard --- delimiters
    - Code-fenced YAML (```yaml ... ```)
    - Bare YAML (no delimiters, first line has key:)

    Args:
        text: Raw text that may contain frontmatter in various formats.

    Returns:
        Dict of parsed YAML fields. Empty dict if unparseable.
    """
    t = text.strip()
    bt = "```"

    # Case 1: code-fenced YAML (LLM wraps in ```yaml ... ```)
    if t.startswith(bt):
        nl = t.find("\n")
        if nl > 0:
            t = t[nl + 1:]
        close = t.find(bt)
        if close > 0:
            yaml_part = t[:close].strip()
            body_part = t[close + 3:].strip()
            t = f"---\n{yaml_part}\n---\n{body_part}"

    # Case 2: bare YAML (no --- delimiters, first line has "key:")
    if not t.startswith("---") and t and ":" in t.split("\n")[0]:
        lines = t.split("\n")
        for i, ln in enumerate(lines):
            if ln.startswith("#") or (i > 3 and ln.strip() == ""):
                t = "---\n" + "\n".join(lines[:i]) + "\n---\n" + "\n".join(lines[i:])
                break

    # Case 3: standard --- delimiters
    if not t.startswith("---"):
        return {}
    end = t.find("---", 3)
    if end < 0:
        return {}
    try:
        return yaml.safe_load(t[3:end]) or {}
    except yaml.YAMLError:
        return {}


def split_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    """Split content into frontmatter dict and body text.

    Args:
        content: Full markdown with frontmatter.

    Returns:
        Tuple of (frontmatter_dict, body_text). If no frontmatter, returns ({}, content).
    """
    fm = parse_frontmatter(content)
    body = strip_frontmatter(content) if fm else content
    return fm or {}, body


# =============================================================================
# Builder Operations (was duplicated 6x)
# =============================================================================


def find_builder_dir(kind: str) -> Path | None:
    """Locate the builder directory for a CEX kind.

    Tries exact match first (kind-slug-builder/), then partial match.

    Args:
        kind: CEX kind name (e.g., 'knowledge_card', 'agent').

    Returns:
        Path to builder directory, or None if not found.
    """
    slug = kind.replace("_", "-")
    direct = BUILDER_DIR / f"{slug}-builder"
    if direct.exists():
        return direct
    # Partial match fallback
    for d in BUILDER_DIR.iterdir():
        if d.is_dir() and slug in d.name:
            return d
    return None


def load_iso(builder_dir: Path, prefix: str, kind_slug: str) -> str:
    """Read a single builder builder spec.

    Tries exact match (prefix_kind_slug.md) first, then any file matching prefix.

    Args:
        builder_dir: Path to builder directory.
        prefix: Builder spec prefix (e.g., 'bld_prompt').
        kind_slug: Kind name with underscores (e.g., 'knowledge_card').

    Returns:
        File content as string, or empty string if not found.
    """
    target = builder_dir / f"{prefix}_{kind_slug}.md"
    if target.exists():
        return target.read_text(encoding="utf-8")
    # Fallback: any file matching prefix
    for f in builder_dir.glob(f"{prefix}_*.md"):
        return f.read_text(encoding="utf-8")
    return ""


def load_all_isos(builder_dir: Path, kind_slug: str) -> dict[str, str]:
    """Load all builder specs for a kind.

    Args:
        builder_dir: Path to builder directory.
        kind_slug: Kind name with underscores.

    Returns:
        Dict mapping prefix to content. E.g., {'prompt': '...', 'schema': '...'}.
    """
    isos: dict[str, str] = {}
    for f in sorted(builder_dir.glob("bld_*.md")):
        # Extract prefix: bld_prompt_agent.md -> prompt
        name = f.stem  # bld_prompt_agent
        parts = name.split("_", 2)  # ['bld', 'instruction', 'agent']
        if len(parts) >= 2:
            prefix = parts[1]
            isos[prefix] = f.read_text(encoding="utf-8")
    return isos


# =============================================================================
# YAML Utilities
# =============================================================================


def load_yaml(path: Path) -> dict[str, Any]:
    """Load and parse a YAML file.

    Args:
        path: Path to .yaml or .yml file.

    Returns:
        Parsed dict.

    Raises:
        ConfigError: If file not found or invalid YAML.
    """
    if not path.exists():
        raise ConfigError(f"YAML file not found: {path}", key=str(path))
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        raise ConfigError(f"Invalid YAML in {path}: {e}", key=str(path)) from e


def load_kinds_meta() -> dict[str, Any]:
    """Load the kind registry (.cex/kinds_meta.json).

    Returns:
        Dict of kind definitions.

    Raises:
        ConfigError: If registry not found.
    """
    if not KINDS_META_PATH.exists():
        raise ConfigError("kinds_meta.json not found", key=str(KINDS_META_PATH))
    return json.loads(KINDS_META_PATH.read_text(encoding="utf-8"))


# =============================================================================
# File I/O Utilities
# =============================================================================


def ensure_dir(path: Path) -> Path:
    """Create directory and parents if they don't exist.

    Args:
        path: Directory path to ensure exists.

    Returns:
        The path (for chaining).
    """
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_signal(nucleus: str, task: str, status: str = "complete",
                 details: dict | None = None) -> Path:
    """Write a completion signal to .cex/runtime/signals/.

    Args:
        nucleus: Nucleus ID (e.g., 'N03').
        task: Task name.
        status: Signal status ('complete', 'failed', 'blocked').
        details: Optional extra info.

    Returns:
        Path to the written signal file.
    """
    signals_dir = ensure_dir(RUNTIME_DIR / "signals")
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    signal_path = signals_dir / f"{nucleus}_{task}_{ts}.json"
    signal_data = {
        "nucleus": nucleus,
        "task": task,
        "status": status,
        "timestamp": ts,
        **(details or {}),
    }
    signal_path.write_text(json.dumps(signal_data, indent=2), encoding="utf-8")
    return signal_path


def slugify(text: str) -> str:
    """Convert text to a URL/filename-safe slug.

    Args:
        text: Input text.

    Returns:
        Lowercase slug with hyphens.
    """
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


# =============================================================================
# Learning Record
# =============================================================================


def write_learning_record(
    kind: str,
    intent: str,
    verdict: dict[str, Any],
    timings: dict[str, float],
    builder_dir: Path | None = None,
    logger: Any = None,
) -> Path | None:
    """Write a build learning record and optionally append to builder memory.

    Args:
        kind: CEX kind that was built.
        intent: Original intent string (truncated to 100 chars).
        verdict: F7 verdict dict with passed, retries, hard_gates, issues.
        timings: Dict of function timings in ms.
        builder_dir: Optional builder directory for memory append.
        logger: Optional callable(tag, msg) for logging.

    Returns:
        Path to the written learning record, or None on failure.
    """
    if not verdict:
        return None

    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    gates_passed = sum(1 for g in verdict.get("hard_gates", []) if g.get("passed"))
    gates_total = len(verdict.get("hard_gates", []))
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "kind": kind,
        "intent": intent[:100],
        "passed": verdict.get("passed", False),
        "retries": verdict.get("retries", 0),
        "gates_passed": gates_passed,
        "gates_total": gates_total,
        "issues": verdict.get("issues", []),
        "timing_ms": sum(timings.values()),
    }

    lr_dir = ensure_dir(CEX_ROOT / ".cex" / "learning_records")
    lr_path = lr_dir / f"lr_{kind}_{ts}.json"
    lr_path.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    if logger:
        logger("LR", f"learning record saved to {lr_path.name}")

    # Append summary to builder's bld_memory if exists
    if builder_dir:
        mem_files = list(builder_dir.glob("bld_memory_*.md"))
        if mem_files:
            mem_path = mem_files[0]
            outcome = "PASS" if verdict.get("passed") else "FAIL"
            issues_str = "; ".join(verdict.get("issues", []))[:100]
            entry = (
                f"\n- [{ts}] {outcome} kind={kind} "
                f"retries={verdict.get('retries', 0)} "
                f"gates={gates_passed}/{gates_total}"
            )
            if issues_str:
                entry += f" issues=[{issues_str}]"

            content = mem_path.read_text(encoding="utf-8")
            if "## Production Log" not in content:
                content += "\n\n## Production Log\n"
            content += entry + "\n"

            if len(content.encode("utf-8")) <= 4096:
                mem_path.write_text(content, encoding="utf-8")
                if logger:
                    logger("LR", f"appended to {mem_path.name}")
            elif logger:
                logger("LR", "bld_memory at size limit, skipped append")

    return lr_path
