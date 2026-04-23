#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Preflight -- Hybrid local/cloud context pre-compiler for token budget optimization.

Pre-compiles minimal, surgical context BEFORE nucleus boot using cheap/local
models (Ollama qwen3:8b/14b or Claude Haiku). Reduces token consumption on
the main model (Sonnet/Opus) by 60-70%.

Architecture:
  Phase 1 (LOCAL, $0): TF-IDF ranking + file scanning via Ollama
  Phase 2 (CLOUD, cheap): Haiku semantic rerank (only if local uncertain)

Config: .cex/P09_config/nucleus_models.yaml -> preflight: section
Output: .cex/cache/preflight/{nucleus}_{task_hash}.json

Usage:
    python _tools/cex_preflight.py --nucleus n03 --task "build agent for sales"
    python _tools/cex_preflight.py --handoff .cex/runtime/handoffs/MISSION_n03.md
    python _tools/cex_preflight.py --mission PREFLIGHT
    python _tools/cex_preflight.py --stats
    python _tools/cex_preflight.py --clean
    python _tools/cex_preflight.py --nucleus n03 --task "build agent" --dry-run
    python _tools/cex_preflight.py --compress-boot --dry-run
    python _tools/cex_preflight.py --compress-boot --in-place --ratio 0.7

Exit codes: 0 = success, 1 = error, 2 = cache stale
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cex_shared import (CEX_ROOT, ensure_dir, find_builder_dir, load_all_isos,
                        load_yaml, parse_frontmatter, strip_frontmatter)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CONFIG_PATH = CEX_ROOT / ".cex" / "config" / "nucleus_models.yaml"
CACHE_DIR = CEX_ROOT / ".cex" / "cache" / "preflight"
HANDOFFS_DIR = CEX_ROOT / ".cex" / "runtime" / "handoffs"
KC_DIR = CEX_ROOT / "N00_genesis" / "P01_knowledge" / "library" / "kind"

# TF-IDF stopwords (EN minimal set for ranking)
_STOPWORDS = frozenset([
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "shall",
    "should", "may", "might", "can", "could", "and", "or", "but", "i",
    "then", "else", "when", "where", "which", "that", "this", "these",
    "those", "it", "its", "in", "on", "at", "to", "for", "from", "by",
    "with", "o", "as", "not", "no", "all", "each", "every", "any",
])

_WORD_RE = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]{2,}")


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

def load_preflight_config() -> dict[str, Any]:
    """Load preflight config from nucleus_models.yaml."""
    if not CONFIG_PATH.exists():
        return _default_config()
    cfg = load_yaml(CONFIG_PATH)
    return cfg.get("preflight", _default_config())


def _get_preflight_cloud_model() -> str:
    """Resolve preflight cloud model via resolver, fallback to hardcoded."""
    try:
        from _tools.cex_model_resolver import get_preflight_model
        return get_preflight_model("cloud").get("model", "claude-haiku-4-5-20251001")
    except Exception:
        return "claude-haiku-4-5-20251001"


def _default_config() -> dict[str, Any]:
    """Fallback config when YAML is missing."""
    return {
        "enabled": True,
        "strategy": "local",
        "local": {
            "cli": "ollama",
            "model": "qwen3:14b",
            "fallback_model": "qwen3:8b",
            "base_url": "http://localhost:11434/v1",
            "timeout_seconds": 30,
        },
        "cloud": {
            "cli": "claude",
            "model": _get_preflight_cloud_model(),
        },
        "cloud_token_budget": 4000,
        "cache_dir": ".cex/cache/preflight",
        "targets": {
            "max_isos_per_build": 5,
            "max_kcs_per_build": 3,
            "max_context_tokens": 15000,
            "original_avg_tokens": 50000,
        },
    }


# ---------------------------------------------------------------------------
# Tokenization (TF-IDF, no deps)
# ---------------------------------------------------------------------------

def tokenize(text: str) -> list[str]:
    """Extract lowercase tokens, no stopwords."""
    return [w for w in _WORD_RE.findall(text.lower()) if w not in _STOPWORDS]


def tfidf_similarity(query_tokens: list[str], doc_tokens: list[str]) -> float:
    """Compute cosine similarity between query and document using TF-IDF-like scoring."""
    if not query_tokens or not doc_tokens:
        return 0.0
    q_counts = Counter(query_tokens)
    d_counts = Counter(doc_tokens)
    # Intersection terms
    common = set(q_counts.keys()) & set(d_counts.keys())
    if not common:
        return 0.0
    # Simple TF dot product normalized by vector magnitudes
    dot = sum(q_counts[t] * d_counts[t] for t in common)
    mag_q = math.sqrt(sum(v * v for v in q_counts.values()))
    mag_d = math.sqrt(sum(v * v for v in d_counts.values()))
    if mag_q == 0 or mag_d == 0:
        return 0.0
    return dot / (mag_q * mag_d)


# ---------------------------------------------------------------------------
# Token counting (lightweight, no tiktoken required)
# ---------------------------------------------------------------------------

def count_tokens(text: str) -> int:
    """Count tokens. Uses tiktoken if available, else word-based estimate."""
    try:
        from cex_token_budget import count_tokens as _ct
        return _ct(text)
    except Exception:
        # Fallback: ~1.3 tokens per word
        return int(len(text.split()) * 1.3)


# ---------------------------------------------------------------------------
# Phase 1: LOCAL (TF-IDF + optional Ollama)
# ---------------------------------------------------------------------------

def extract_task_info(handoff_text: str) -> dict[str, str]:
    """Extract kind, pillar, domain, and task description from handoff text."""
    info: dict[str, str] = {"kind": "", "pillar": "", "domain": "", "task": ""}

    # Try frontmatter first
    fm = parse_frontmatter(handoff_text)
    if fm:
        info["kind"] = fm.get("kind", "")
        info["pillar"] = fm.get("pillar", "")
        info["domain"] = fm.get("domain", "")
        info["task"] = fm.get("task", "")

    # Extract from body if frontmatter incomplete
    body = strip_frontmatter(handoff_text) if handoff_text.startswith("---") else handoff_text

    if not info["kind"]:
        # Look for kind= or kind: patterns
        m = re.search(r"kind[=:]\s*(\w+)", body, re.IGNORECASE)
        if m:
            info["kind"] = m.group(1)

    if not info["task"]:
        # Use first non-empty, non-header line as task summary
        for line in body.split("\n"):
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith("---"):
                info["task"] = line[:200]
                break

    return info


def rank_isos(kind: str, task_text: str, max_isos: int = 5) -> list[dict[str, Any]]:
    """Rank builder ISOs by TF-IDF relevance to task. Returns top-K with scores."""
    builder_dir = find_builder_dir(kind)
    if not builder_dir:
        return []

    all_isos = load_all_isos(builder_dir, kind.replace("-", "_"))
    if not all_isos:
        return []

    query_tokens = tokenize(task_text + " " + kind)
    scored = []

    for prefix, content in all_isos.items():
        doc_tokens = tokenize(content)
        score = tfidf_similarity(query_tokens, doc_tokens)
        # Boost critical ISOs (manifest, instruction, system_prompt always relevant)
        if prefix in ("manifest", "instruction", "system"):
            score = max(score, 0.5)  # Floor at 0.5 for essential ISOs
        scored.append({
            "prefix": prefix,
            "filename": f"bld_{prefix}_{kind.replace('-', '_')}.md",
            "score": round(score, 4),
            "tokens": count_tokens(content),
            "path": str(builder_dir / f"bld_{prefix}_{kind.replace('-', '_')}.md"),
        })

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:max_isos]


def select_kcs(kind: str, task_text: str, max_kcs: int = 3) -> list[dict[str, Any]]:
    """Select most relevant Knowledge Cards using TF-IDF similarity."""
    results = []

    # Always include the kind's own KC if it exists
    kind_kc = KC_DIR / f"kc_{kind.replace('-', '_')}.md"
    if kind_kc.exists():
        content = kind_kc.read_text(encoding="utf-8")
        results.append({
            "path": str(kind_kc),
            "name": kind_kc.name,
            "score": 1.0,  # Own KC always top relevance
            "tokens": count_tokens(content),
        })

    # Scan for additional relevant KCs
    if KC_DIR.exists():
        query_tokens = tokenize(task_text + " " + kind)
        for kc_file in KC_DIR.glob("kc_*.md"):
            if kc_file == kind_kc:
                continue
            try:
                content = kc_file.read_text(encoding="utf-8")
                doc_tokens = tokenize(content[:2000])  # First 2K chars for speed
                score = tfidf_similarity(query_tokens, doc_tokens)
                if score > 0.1:  # Minimum relevance threshold
                    results.append({
                        "path": str(kc_file),
                        "name": kc_file.name,
                        "score": round(score, 4),
                        "tokens": count_tokens(content),
                    })
            except Exception:
                continue

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:max_kcs]


def dedup_context(texts: list[str]) -> str:
    """Remove redundant content across assembled context pieces."""
    if not texts:
        return ""
    # Simple line-level dedup preserving order
    seen_lines: set[str] = set()
    deduped: list[str] = []
    for text in texts:
        for line in text.split("\n"):
            normalized = line.strip().lower()
            # Skip empty lines and very short lines (headers are fine to repeat)
            if len(normalized) < 10 or normalized not in seen_lines:
                deduped.append(line)
                if len(normalized) >= 10:
                    seen_lines.add(normalized)
    return "\n".join(deduped)


def run_local_phase(
    task_info: dict[str, str],
    config: dict[str, Any],
    dry_run: bool = False,
) -> dict[str, Any]:
    """Phase 1: Local TF-IDF ranking. Zero cost."""
    targets = config.get("targets", {})
    max_isos = targets.get("max_isos_per_build", 5)
    max_kcs = targets.get("max_kcs_per_build", 3)
    max_tokens = targets.get("max_context_tokens", 15000)

    kind = task_info.get("kind", "")
    task = task_info.get("task", "")

    # Rank ISOs
    ranked_isos = rank_isos(kind, task, max_isos) if kind else []

    # Select KCs
    selected_kcs = select_kcs(kind, task, max_kcs) if kind else []

    # Load selected ISO content
    iso_contents = []
    for iso in ranked_isos:
        p = Path(iso["path"])
        if p.exists():
            iso_contents.append(p.read_text(encoding="utf-8"))

    # Load selected KC content
    kc_contents = []
    for kc in selected_kcs:
        p = Path(kc["path"])
        if p.exists():
            kc_contents.append(p.read_text(encoding="utf-8"))

    # Dedup and assemble
    all_content = iso_contents + kc_contents
    compiled = dedup_context(all_content) if not dry_run else ""
    compiled_tokens = count_tokens(compiled) if compiled else sum(
        i.get("tokens", 0) for i in ranked_isos
    ) + sum(k.get("tokens", 0) for k in selected_kcs)

    # Estimate original tokens (all 13 ISOs + all KCs)
    original_tokens = targets.get("original_avg_tokens", 50000)
    if kind:
        builder_dir = find_builder_dir(kind)
        if builder_dir:
            all_iso_data = load_all_isos(builder_dir, kind.replace("-", "_"))
            original_tokens = sum(count_tokens(v) for v in all_iso_data.values())
            # Add estimated KC tokens
            if KC_DIR.exists():
                kc_file = KC_DIR / f"kc_{kind.replace('-', '_')}.md"
                if kc_file.exists():
                    original_tokens += count_tokens(kc_file.read_text(encoding="utf-8"))

    # Confidence: high if TF-IDF scores are clearly separated
    confidence = 0.0
    if ranked_isos:
        top_score = ranked_isos[0]["score"]
        if len(ranked_isos) > 1:
            gap = top_score - ranked_isos[-1]["score"]
            confidence = min(1.0, top_score * 0.6 + gap * 0.4)
        else:
            confidence = top_score * 0.7

    return {
        "selected_isos": [i["filename"] for i in ranked_isos],
        "iso_details": ranked_isos,
        "selected_kcs": [k["name"] for k in selected_kcs],
        "kc_details": selected_kcs,
        "compiled_prompt": compiled,
        "context_tokens": compiled_tokens,
        "original_tokens": original_tokens,
        "confidence": round(confidence, 3),
        "strategy_used": "local",
        "needs_cloud": confidence < 0.7,
    }


# ---------------------------------------------------------------------------
# Phase 2: CLOUD (Haiku semantic rerank -- only when confidence < 0.7)
# ---------------------------------------------------------------------------

def call_ollama(prompt: str, config: dict[str, Any]) -> str | None:
    """Call Ollama via OpenAI-compatible API. Returns response text or None."""
    local_cfg = config.get("local", {})
    base_url = local_cfg.get("base_url", "http://localhost:11434/v1")
    model = local_cfg.get("model", "qwen3:14b")
    timeout = local_cfg.get("timeout_seconds", 30)

    try:
        from openai import OpenAI
        client = OpenAI(base_url=base_url, api_key="ollama")
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            timeout=timeout,
        )
        return response.choices[0].message.content
    except Exception:
        # Try fallback model
        fallback = local_cfg.get("fallback_model")
        if fallback and fallback != model:
            try:
                client = OpenAI(base_url=base_url, api_key="ollama")
                response = client.chat.completions.create(
                    model=fallback,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.1,
                    timeout=timeout,
                )
                return response.choices[0].message.content
            except Exception:
                pass
    return None


def call_haiku(prompt: str, config: dict[str, Any]) -> str | None:
    """Call Claude Haiku for semantic reranking. Returns response text or None."""
    cloud_cfg = config.get("cloud", {})
    model = cloud_cfg.get("model", _get_preflight_cloud_model())

    try:
        from cex_sdk.models.chat import chat
        return chat(prompt, model=model, max_tokens=1024)
    except Exception:
        return None


def run_cloud_phase(
    local_result: dict[str, Any],
    task_info: dict[str, str],
    config: dict[str, Any],
) -> dict[str, Any]:
    """Phase 2: Semantic rerank via Haiku (only if local confidence < 0.7)."""
    if not local_result.get("needs_cloud", False):
        return local_result

    strategy = config.get("strategy", "hybrid")
    if strategy == "local":
        # User configured local-only, skip cloud
        return local_result

    task = task_info.get("task", "")
    kind = task_info.get("kind", "")
    iso_names = local_result.get("selected_isos", [])

    # Build reranking prompt
    rerank_prompt = (
        "You are a context relevance scorer for an LLM agent build system.\n"
        "Task: %s\n"
        "Kind: %s\n\n"
        "Rate each builder ISO file 0-1 for relevance to this task.\n"
        "Return ONLY a JSON object mapping filename to score.\n"
        "Files:\n%s"
    ) % (task, kind, "\n".join(f"- {n}" for n in iso_names))

    # Try Ollama first (free), then Haiku (cheap)
    response = None
    if strategy in ("hybrid", "local"):
        response = call_ollama(rerank_prompt, config)

    if response is None and strategy in ("hybrid", "cloud"):
        response = call_haiku(rerank_prompt, config)

    if response is None:
        # Both failed -- return local result as-is
        local_result["strategy_used"] = "local_fallback"
        return local_result

    # Parse reranked scores
    try:
        # Extract JSON from response (may have surrounding text)
        json_match = re.search(r"\{[^}]+\}", response)
        if json_match:
            scores = json.loads(json_match.group())
            # Re-sort ISOs by cloud scores
            for iso in local_result.get("iso_details", []):
                cloud_score = scores.get(iso["filename"], iso["score"])
                if isinstance(cloud_score, (int, float)):
                    iso["score"] = round(float(cloud_score), 4)
            local_result["iso_details"].sort(key=lambda x: x["score"], reverse=True)
            local_result["selected_isos"] = [
                i["filename"] for i in local_result["iso_details"]
            ]
            local_result["strategy_used"] = "hybrid" if strategy == "hybrid" else "cloud"
            local_result["confidence"] = 0.85  # Cloud rerank boosts confidence
    except (json.JSONDecodeError, ValueError):
        local_result["strategy_used"] = "local_fallback"

    return local_result


# ---------------------------------------------------------------------------
# Cache I/O
# ---------------------------------------------------------------------------

def task_hash(nucleus: str, task: str) -> str:
    """Generate deterministic hash for cache key."""
    h = hashlib.sha256(f"{nucleus}:{task}".encode()).hexdigest()[:12]
    return h


def write_cache(nucleus: str, result: dict[str, Any], config: dict[str, Any]) -> Path:
    """Write preflight result to cache."""
    cache_dir = CEX_ROOT / config.get("cache_dir", ".cex/cache/preflight")
    ensure_dir(cache_dir)

    t_hash = task_hash(nucleus, result.get("task", ""))
    cache_path = cache_dir / f"{nucleus}_{t_hash}.json"

    cache_data = {
        "nucleus": nucleus,
        "kind": result.get("kind", ""),
        "task_hash": t_hash,
        "compiled_at": datetime.now(timezone.utc).isoformat(),
        "selected_isos": result.get("selected_isos", []),
        "selected_kcs": result.get("selected_kcs", []),
        "context_tokens": result.get("context_tokens", 0),
        "original_tokens": result.get("original_tokens", 0),
        "reduction_pct": round(
            (1 - result.get("context_tokens", 0) / max(result.get("original_tokens", 1), 1)) * 100,
            1,
        ),
        "strategy_used": result.get("strategy_used", "local"),
        "confidence": result.get("confidence", 0.0),
        "compiled_prompt": result.get("compiled_prompt", ""),
    }

    cache_path.write_text(json.dumps(cache_data, indent=2, ensure_ascii=True), encoding="utf-8")
    return cache_path


def read_cache(nucleus: str, task: str, config: dict[str, Any]) -> dict[str, Any] | None:
    """Read preflight cache if fresh. Returns None if stale or missing."""
    cache_dir = CEX_ROOT / config.get("cache_dir", ".cex/cache/preflight")
    t_hash = task_hash(nucleus, task)
    cache_path = cache_dir / f"{nucleus}_{t_hash}.json"

    if not cache_path.exists():
        return None

    try:
        data = json.loads(cache_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None

    # Check staleness: if any selected ISO has mtime > compiled_at
    compiled_at = data.get("compiled_at", "")
    if not compiled_at:
        return None

    try:
        compiled_ts = datetime.fromisoformat(compiled_at).timestamp()
    except ValueError:
        return None

    kind = data.get("kind", "")
    if kind:
        builder_dir = find_builder_dir(kind)
        if builder_dir:
            for iso_file in builder_dir.glob("bld_*.md"):
                if iso_file.stat().st_mtime > compiled_ts:
                    return None  # Stale

    return data


# ---------------------------------------------------------------------------
# Cache Stats
# ---------------------------------------------------------------------------

def cache_stats() -> dict[str, Any]:
    """Compute cache statistics."""
    if not CACHE_DIR.exists():
        return {"total": 0, "total_bytes": 0, "entries": []}

    entries = []
    total_bytes = 0
    for f in sorted(CACHE_DIR.glob("*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            size = f.stat().st_size
            total_bytes += size
            entries.append({
                "file": f.name,
                "nucleus": data.get("nucleus", "?"),
                "kind": data.get("kind", "?"),
                "tokens": data.get("context_tokens", 0),
                "original": data.get("original_tokens", 0),
                "reduction": data.get("reduction_pct", 0),
                "strategy": data.get("strategy_used", "?"),
                "compiled_at": data.get("compiled_at", "?"),
                "bytes": size,
            })
        except Exception:
            continue

    return {
        "total": len(entries),
        "total_bytes": total_bytes,
        "entries": entries,
    }


# ---------------------------------------------------------------------------
# Main Preflight Pipeline
# ---------------------------------------------------------------------------

def preflight(
    nucleus: str,
    task: str,
    config: dict[str, Any] | None = None,
    dry_run: bool = False,
    force: bool = False,
    phase0: bool = False,
) -> dict[str, Any]:
    """Run full preflight pipeline for a nucleus task.

    Args:
        nucleus: Nucleus ID (e.g., 'n03')
        task: Task description
        config: Preflight config (loaded from YAML if None)
        dry_run: If True, skip LLM calls and prompt assembly
        force: If True, ignore cache
        phase0: If True, run Phase 0 MCP external context gather (N07 only)

    Returns:
        Preflight result dict (also written to cache)
    """
    if config is None:
        config = load_preflight_config()

    if not config.get("enabled", True):
        return {"skipped": True, "reason": "preflight disabled in config"}

    # Check cache first
    if not force and not dry_run:
        cached = read_cache(nucleus, task, config)
        if cached:
            cached["cache_hit"] = True
            return cached

    # Extract task info
    task_info = extract_task_info(task)
    if not task_info.get("task"):
        task_info["task"] = task

    # Phase 0: External MCP context gather (N07 only, opt-in via phase0=True)
    external_ctx: dict[str, Any] = {}
    external_context_md = ""
    if phase0 and not dry_run:
        try:
            from cex_preflight_mcp import \
                gather_external_context as _mcp_gather
            external_ctx = _mcp_gather(
                nucleus=nucleus,
                kind=task_info.get("kind", ""),
                task=task,
                domain=task_info.get("domain", ""),
                force=force,
            )
            if not external_ctx.get("skipped") and external_ctx.get("has_context"):
                external_context_md = external_ctx.get("context_md", "")
        except ImportError:
            external_ctx = {"skipped": True, "skipped_reason": "cex_preflight_mcp not installed"}
        except Exception as exc:
            external_ctx = {"skipped": True, "skipped_reason": "phase0 error: %s" % exc}

    # Phase 1: Local TF-IDF ranking
    result = run_local_phase(task_info, config, dry_run=dry_run)
    result["task"] = task
    result["kind"] = task_info.get("kind", "")
    result["nucleus"] = nucleus

    # Phase 2: Cloud rerank (only if needed and not dry-run)
    if not dry_run and result.get("needs_cloud", False):
        result = run_cloud_phase(result, task_info, config)

    # Phase 3: Merge external context (Phase 0) with local context
    if external_context_md:
        merged = external_context_md + "\n\n" + result.get("compiled_prompt", "")
        result["compiled_prompt"] = merged
        result["context_tokens"] = count_tokens(merged)
        result["phase0_tokens"] = external_ctx.get("tokens_used", 0)
        result["phase0_sources"] = external_ctx.get("sources_used", [])
        result["phase0_queries"] = external_ctx.get("queries", [])
        result["phase0_result_count"] = external_ctx.get("result_count", 0)
    elif phase0:
        result["phase0_skipped"] = external_ctx.get("skipped_reason", "no context gathered")

    # Write cache (unless dry-run)
    if not dry_run:
        cache_path = write_cache(nucleus, result, config)
        result["cache_path"] = str(cache_path)

    result["cache_hit"] = False
    return result


def preflight_from_handoff(handoff_path: str | Path, config: dict[str, Any] | None = None,
                           dry_run: bool = False) -> dict[str, Any]:
    """Run preflight from a handoff file."""
    path = Path(handoff_path)
    if not path.exists():
        return {"error": f"Handoff not found: {path}"}

    content = path.read_text(encoding="utf-8")

    # Extract nucleus from filename (e.g., MISSION_n03.md -> n03)
    nucleus = "n00"
    name = path.stem.lower()
    for nuc in ["n01", "n02", "n03", "n04", "n05", "n06", "n07"]:
        if nuc in name:
            nucleus = nuc
            break

    # Also check frontmatter
    fm = parse_frontmatter(content)
    if fm and fm.get("nucleus"):
        nucleus = fm["nucleus"].lower()

    return preflight(nucleus, content, config=config, dry_run=dry_run)


def preflight_mission(mission_name: str, config: dict[str, Any] | None = None,
                      dry_run: bool = False) -> list[dict[str, Any]]:
    """Run preflight for all handoffs in a mission."""
    results = []
    pattern = f"{mission_name}_n*.md"
    for handoff in sorted(HANDOFFS_DIR.glob(pattern)):
        result = preflight_from_handoff(handoff, config=config, dry_run=dry_run)
        results.append(result)

    # Also check n0X_task.md files in root
    if not results:
        for nuc in ["n01", "n02", "n03", "n04", "n05", "n06"]:
            task_file = CEX_ROOT / f"{nuc}_task.md"
            if task_file.exists():
                result = preflight_from_handoff(task_file, config=config, dry_run=dry_run)
                results.append(result)

    return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _print_result(result: dict[str, Any]) -> None:
    """Pretty-print a preflight result."""
    if result.get("skipped"):
        print("[SKIP] Preflight disabled: %s" % result.get("reason", ""))
        return
    if result.get("error"):
        print("[FAIL] %s" % result["error"])
        return

    nucleus = result.get("nucleus", "?")
    kind = result.get("kind", "?")
    strategy = result.get("strategy_used", "?")
    ctx_tokens = result.get("context_tokens", 0)
    orig_tokens = result.get("original_tokens", 0)
    reduction = round((1 - ctx_tokens / max(orig_tokens, 1)) * 100, 1)
    confidence = result.get("confidence", 0)
    cache_hit = result.get("cache_hit", False)

    print("=" * 60)
    print("  CEX Preflight Result")
    print("=" * 60)
    print("  Nucleus:     %s" % nucleus)
    print("  Kind:        %s" % kind)
    print("  Strategy:    %s" % strategy)
    print("  Cache hit:   %s" % cache_hit)
    print("  Confidence:  %.1f%%" % (confidence * 100))
    print("")
    print("  Token Budget:")
    print("    Original:  %s tokens" % f"{orig_tokens:,}")
    print("    Compiled:  %s tokens" % f"{ctx_tokens:,}")
    print("    Reduction: %.1f%%" % reduction)
    print("")

    isos = result.get("iso_details", [])
    if isos:
        print("  Selected ISOs (%d):" % len(isos))
        for iso in isos:
            print("    [%.3f] %s (%d tok)" % (iso["score"], iso["filename"], iso.get("tokens", 0)))

    kcs = result.get("kc_details", [])
    if kcs:
        print("")
        print("  Selected KCs (%d):" % len(kcs))
        for kc in kcs:
            print("    [%.3f] %s (%d tok)" % (kc["score"], kc["name"], kc.get("tokens", 0)))

    # Phase 0 summary (if run)
    if result.get("phase0_tokens") is not None:
        print("")
        print("  Phase 0 (MCP external):")
        print("    tokens:  %d" % result.get("phase0_tokens", 0))
        print("    sources: %s" % ", ".join(result.get("phase0_sources", [])))
        print("    results: %d" % result.get("phase0_result_count", 0))
    elif result.get("phase0_skipped"):
        print("")
        print("  Phase 0: skipped (%s)" % result["phase0_skipped"])

    if result.get("cache_path"):
        print("")
        print("  Cache: %s" % result["cache_path"])
    print("=" * 60)


def _print_stats() -> None:
    """Print cache statistics."""
    stats = cache_stats()
    print("=" * 60)
    print("  CEX Preflight Cache Stats")
    print("=" * 60)
    print("  Total entries: %d" % stats["total"])
    print("  Total size:    %s bytes" % f"{stats['total_bytes']:,}")
    print("")

    if stats["entries"]:
        print("  %-10s %-20s %8s %8s %7s %-8s" % (
            "Nucleus", "Kind", "Tokens", "Original", "Reduce", "Strategy"))
        print("  " + "-" * 65)
        total_saved = 0
        for e in stats["entries"]:
            saved = e["original"] - e["tokens"]
            total_saved += saved
            print("  %-10s %-20s %8s %8s %6.1f%% %-8s" % (
                e["nucleus"], e["kind"][:20],
                f"{e['tokens']:,}", f"{e['original']:,}",
                e["reduction"], e["strategy"],
            ))
        print("")
        print("  Total tokens saved: %s" % f"{total_saved:,}")
    print("=" * 60)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="CEX Preflight -- hybrid local/cloud context pre-compiler"
    )
    parser.add_argument("--nucleus", "-n", help="Nucleus ID (e.g., n03)")
    parser.add_argument("--task", "-t", help="Task description")
    parser.add_argument("--kind", "-k", help="CEX kind (e.g., agent, knowledge_card)")
    parser.add_argument("--handof", help="Path to handoff file")
    parser.add_argument("--mission", help="Mission name (pre-compiles all handoffs)")
    parser.add_argument("--stats", action="store_true", help="Show cache statistics")
    parser.add_argument("--clean", action="store_true", help="Clear preflight cache")
    parser.add_argument("--dry-run", action="store_true", help="Show selections without LLM calls")
    parser.add_argument("--force", action="store_true", help="Ignore cache, recompute")
    parser.add_argument("--phase0", action="store_true",
                        help="Run Phase 0 MCP external context gather before local ranking (N07 only)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--compress-boot", action="store_true",
                        help="Run LLMLingua-2 on boot context (CLAUDE.md + .claude/rules/*.md) via cex_compress.py")
    parser.add_argument("--ratio", type=float, default=0.7,
                        help="Compression ratio for --compress-boot (default 0.7, lower = more aggressive)")
    parser.add_argument("--in-place", action="store_true",
                        help="With --compress-boot: rewrite source files (DESTRUCTIVE)")
    args = parser.parse_args()

    # Compress-boot mode: thin pass-through to cex_compress.py
    if args.compress_boot:
        cmd = [sys.executable, str(Path(__file__).resolve().parent / "cex_compress.py"),
               "--target", "boot", "--ratio", str(args.ratio)]
        if args.dry_run:
            cmd.append("--dry-run")
        if args.in_place:
            cmd.append("--in-place")
        print("[preflight] delegating to cex_compress: %s" % " ".join(cmd[1:]))
        return subprocess.run(cmd, check=False).returncode

    # Stats mode
    if args.stats:
        if args.json:
            print(json.dumps(cache_stats(), indent=2))
        else:
            _print_stats()
        return 0

    # Clean mode
    if args.clean:
        if CACHE_DIR.exists():
            count = 0
            for f in CACHE_DIR.glob("*.json"):
                f.unlink()
                count += 1
            print("[OK] Cleaned %d preflight cache entries" % count)
        else:
            print("[OK] No cache to clean")
        return 0

    # Mission mode
    if args.mission:
        config = load_preflight_config()
        results = preflight_mission(args.mission, config=config, dry_run=args.dry_run)
        if not results:
            print("[WARN] No handoffs found for mission: %s" % args.mission)
            return 1
        for r in results:
            if args.json:
                # Strip compiled_prompt for readable JSON output
                r_copy = {k: v for k, v in r.items() if k != "compiled_prompt"}
                print(json.dumps(r_copy, indent=2))
            else:
                _print_result(r)
        return 0

    # Handoff mode
    if args.handoff:
        config = load_preflight_config()
        result = preflight_from_handoff(args.handoff, config=config, dry_run=args.dry_run)
        if args.json:
            r_copy = {k: v for k, v in result.items() if k != "compiled_prompt"}
            print(json.dumps(r_copy, indent=2))
        else:
            _print_result(result)
        return 0 if not result.get("error") else 1

    # Direct mode
    if args.nucleus and args.task:
        config = load_preflight_config()
        task_text = args.task
        if args.kind and "kind=" not in task_text and "kind:" not in task_text:
            task_text = "kind=%s %s" % (args.kind, task_text)
        result = preflight(
            args.nucleus, task_text,
            config=config, dry_run=args.dry_run, force=args.force,
            phase0=getattr(args, "phase0", False),
        )
        if args.json:
            r_copy = {k: v for k, v in result.items() if k != "compiled_prompt"}
            print(json.dumps(r_copy, indent=2))
        else:
            _print_result(result)
        return 0 if not result.get("error") else 1

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
