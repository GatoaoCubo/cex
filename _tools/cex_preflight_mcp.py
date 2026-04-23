#!/usr/bin/env python3
# coding: utf-8
"""CEX Pre-flight Phase 0: external context gather for N07 handoff enrichment.

Gathers external context BEFORE nucleus dispatch so non-Claude runtimes
(Codex, Gemini, Ollama) receive rich handoffs without live MCP access.

Architecture:
  Runs in N07 context (Claude, sole MCP gateway). Two modes:
    1. Direct HTTP: GitHub REST API + URL fetch via urllib (zero extra deps)
    2. MCP-injected: accepts pre-gathered data from N07 agent tool calls

  Output is baked into the handoff under ## External Context section.

Sources (tiered):
  DEFAULT (free): GitHub REST API + direct HTTP fetch
  OPTIONAL: brave-search (BRAVE_API_KEY), firecrawl (FIRECRAWL_API_KEY)

Config: .cex/config/nucleus_models.yaml -> preflight_mcp section
Output: .cex/cache/preflight/{nucleus}_{hash}_external.md
Audit:  .cex/cache/preflight/{hash}_audit.json

Security:
  - GITHUB_TOKEN from env only (never hardcoded)
  - No secrets logged
  - Graceful skip when keys absent
  - Read-only operations only

Usage:
    # Check if kind needs external context
    python cex_preflight_mcp.py --kind knowledge_card --check

    # Generate queries only
    python cex_preflight_mcp.py --kind knowledge_card --task "..." --queries

    # Gather context (direct HTTP, no live MCP dependency)
    python cex_preflight_mcp.py --nucleus n01 --kind knowledge_card --task "..." --gather

    # Inject pre-gathered MCP data from N07 agent tools
    python cex_preflight_mcp.py --nucleus n01 --task "..." --input-json path/to/data.json

Exit codes: 0 = success/skipped, 1 = error, 2 = no context gathered
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cex_shared import CEX_ROOT, ensure_dir, load_kinds_meta, load_yaml

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CONFIG_PATH = CEX_ROOT / ".cex" / "config" / "nucleus_models.yaml"
CACHE_DIR = CEX_ROOT / ".cex" / "cache" / "preflight"

GITHUB_API_BASE = "https://api.github.com"
DEFAULT_TIMEOUT = 60
DEFAULT_MAX_TOKENS = 8192
DEFAULT_MAX_QUERIES = 3
DEFAULT_DELAY_MS = 1000

_WORD_RE = re.compile(r"[a-zA-Z][a-zA-Z0-9_]{2,}")
_STOPWORDS = frozenset([
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "shall",
    "should", "may", "might", "can", "could", "and", "or", "but", "i",
    "in", "on", "at", "to", "for", "from", "by", "with", "o", "as",
    "not", "no", "all", "each", "every", "any", "build", "create", "make",
    "using", "via", "into", "this", "that", "which", "when", "where",
])

_TAG_RE = re.compile(r"<(script|style)[^>]*>.*?</(script|style)>",
                     re.IGNORECASE | re.DOTALL)
_ANY_TAG_RE = re.compile(r"<[^>]+>")


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

def load_mcp_config() -> dict[str, Any]:
    """Load preflight_mcp config from nucleus_models.yaml."""
    if CONFIG_PATH.exists():
        try:
            cfg = load_yaml(CONFIG_PATH)
            if "preflight_mcp" in cfg:
                return cfg["preflight_mcp"]
        except Exception:
            pass
    return _default_mcp_config()


def _default_mcp_config() -> dict[str, Any]:
    return {
        "enabled": True,
        "max_external_tokens": DEFAULT_MAX_TOKENS,
        "timeout_seconds": DEFAULT_TIMEOUT,
        "max_queries_per_provider": DEFAULT_MAX_QUERIES,
        "delay_between_queries_ms": DEFAULT_DELAY_MS,
        "audit_log": True,
        "providers": {
            "github": {"enabled": True, "requires_key": "GITHUB_TOKEN"},
            "fetch": {"enabled": True, "requires_key": None},
            "brave_search": {"enabled": False, "requires_key": "BRAVE_API_KEY"},
            "firecrawl": {"enabled": False, "requires_key": "FIRECRAWL_API_KEY"},
        },
    }


# ---------------------------------------------------------------------------
# Kind metadata
# ---------------------------------------------------------------------------

def requires_external_context(kind: str) -> bool:
    """Return True if this kind benefits from external context injection."""
    if not kind:
        return False
    try:
        meta = load_kinds_meta()
        return bool(meta.get(kind, {}).get("requires_external_context", False))
    except Exception:
        return False


def requires_live_tools(kind: str) -> bool:
    """Return True if this kind needs live MCP at runtime (cannot pre-compile)."""
    if not kind:
        return False
    try:
        meta = load_kinds_meta()
        return bool(meta.get(kind, {}).get("requires_live_tools", False))
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Token counting (lightweight, no tiktoken required)
# ---------------------------------------------------------------------------

def count_tokens(text: str) -> int:
    """Estimate token count. Tries tiktoken, falls back to word-based."""
    try:
        from cex_token_budget import count_tokens as _ct
        return _ct(text)
    except Exception:
        return int(len(text.split()) * 1.3)


# ---------------------------------------------------------------------------
# Query generation
# ---------------------------------------------------------------------------

def generate_queries(task: str, kind: str, domain: str = "") -> list[str]:
    """Generate up to 3 search queries from task description and kind.

    Extracts significant terms from the task, combines with kind context.
    Returns 1-3 distinct queries ordered from specific to general.
    """
    raw_terms = _WORD_RE.findall(task.lower())
    terms = [t for t in raw_terms if t not in _STOPWORDS and len(t) > 3]

    # Deduplicate preserving order
    seen: set[str] = set()
    unique_terms: list[str] = []
    for t in terms:
        if t not in seen:
            seen.add(t)
            unique_terms.append(t)

    kind_label = kind.replace("_", " ")
    queries: list[str] = []

    # Primary: key task terms + kind label
    if unique_terms:
        primary = " ".join(unique_terms[:5])
        queries.append(("%s %s" % (primary, kind_label)).strip())

    # Secondary: domain-focused (if domain provided)
    if domain and len(queries) < DEFAULT_MAX_QUERIES:
        queries.append(("%s %s best practices" % (domain, kind_label)).strip())

    # Tertiary: broader task terms only
    if unique_terms and len(queries) < DEFAULT_MAX_QUERIES:
        broader = " ".join(unique_terms[:3])
        if broader not in " ".join(queries):
            queries.append(broader)

    # Fallback when no meaningful terms extracted
    if not queries:
        queries.append(kind_label or "knowledge")

    return queries[:DEFAULT_MAX_QUERIES]


# ---------------------------------------------------------------------------
# GitHub REST API gather (direct HTTP, no MCP dependency)
# ---------------------------------------------------------------------------

def _build_headers(token: str | None = None) -> dict[str, str]:
    headers: dict[str, str] = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "cex-preflight-mcp/1.0",
    }
    if token:
        headers["Authorization"] = "token %s" % token
    return headers


def _http_get_json(url: str, headers: dict[str, str], timeout: int) -> dict[str, Any] | None:
    """HTTP GET returning parsed JSON, or None on any error."""
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8", errors="replace"))
    except Exception:
        return None


def _http_get_text(url: str, headers: dict[str, str], timeout: int) -> str | None:
    """HTTP GET returning raw text, or None on any error."""
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            ct = resp.headers.get("Content-Type", "")
            enc = "utf-8"
            if "charset=" in ct:
                enc = ct.split("charset=")[-1].split(";")[0].strip()
            return raw.decode(enc, errors="replace")
    except Exception:
        return None


def gather_github(
    queries: list[str],
    config: dict[str, Any],
    timeout: int = DEFAULT_TIMEOUT,
    delay_ms: int = DEFAULT_DELAY_MS,
) -> list[dict[str, str]]:
    """Search GitHub repositories using REST API. Returns result list.

    Requires GITHUB_TOKEN env var. Returns [] if token absent.
    Performs READ-ONLY search_repositories queries per query term.
    """
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        return []

    headers = _build_headers(token)
    max_q = config.get("max_queries_per_provider", DEFAULT_MAX_QUERIES)
    results: list[dict[str, str]] = []
    seen_urls: set[str] = set()

    for query in queries[:max_q]:
        encoded = urllib.parse.quote(query)
        url = "%s/search/repositories?q=%s&sort=stars&per_page=5" % (
            GITHUB_API_BASE, encoded)
        data = _http_get_json(url, headers, timeout)
        if data and "items" in data:
            for item in data["items"][:3]:
                repo_url = item.get("html_url", "")
                if repo_url and repo_url not in seen_urls:
                    seen_urls.add(repo_url)
                    desc = (item.get("description") or "")[:300]
                    results.append({
                        "title": item.get("full_name", "unknown"),
                        "url": repo_url,
                        "snippet": desc,
                        "source": "github",
                    })

        if delay_ms > 0 and query != queries[-1]:
            time.sleep(delay_ms / 1000.0)

    return results


# ---------------------------------------------------------------------------
# Direct URL fetch
# ---------------------------------------------------------------------------

def _html_to_text(html: str, max_chars: int = 3000) -> str:
    """Naive HTML to plain text: strip script/style blocks then tags."""
    clean = _TAG_RE.sub(" ", html)
    clean = _ANY_TAG_RE.sub(" ", clean)
    clean = (clean
             .replace("&amp;", "&")
             .replace("&lt;", "<")
             .replace("&gt;", ">")
             .replace("&quot;", '"')
             .replace("&nbsp;", " "))
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:max_chars]


def gather_fetch(
    urls: list[str],
    timeout: int = DEFAULT_TIMEOUT,
) -> list[dict[str, str]]:
    """Fetch provided URLs and extract readable text snippets."""
    results: list[dict[str, str]] = []
    headers = {"User-Agent": "cex-preflight-mcp/1.0 (context-gather)"}

    for url in urls[:3]:
        text = _http_get_text(url, headers, timeout)
        if text:
            snippet = _html_to_text(text, max_chars=2000)
            if snippet:
                results.append({
                    "title": url,
                    "url": url,
                    "snippet": snippet[:500],
                    "source": "fetch",
                })

    return results


# ---------------------------------------------------------------------------
# MCP result injection (N07 agent tool calls -> this module)
# ---------------------------------------------------------------------------

def inject_mcp_results(mcp_data: dict[str, Any]) -> list[dict[str, str]]:
    """Accept pre-gathered MCP results from N07 agent tool calls.

    N07 agent calls MCP tools directly (github, brave-search, fetch,
    markitdown) and passes results here as structured JSON for formatting.

    Expected mcp_data format:
    {
        "search_results": [{"title": ..., "url": ..., "snippet": ...}],
        "github_results": [{"title": ..., "url": ..., "body": ...}],
        "fetch_results":  [{"url": ..., "content": ...}],
    }
    """
    results: list[dict[str, str]] = []

    for item in mcp_data.get("search_results", []):
        results.append({
            "title": str(item.get("title", "?")),
            "url": str(item.get("url", "")),
            "snippet": str(item.get("snippet", ""))[:500],
            "source": "mcp:search",
        })

    for item in mcp_data.get("github_results", []):
        results.append({
            "title": str(item.get("title", "?")),
            "url": str(item.get("url", "")),
            "snippet": str(item.get("body", ""))[:500],
            "source": "mcp:github",
        })

    for item in mcp_data.get("fetch_results", []):
        results.append({
            "title": str(item.get("url", "?")),
            "url": str(item.get("url", "")),
            "snippet": str(item.get("content", ""))[:500],
            "source": "mcp:fetch",
        })

    return results


# ---------------------------------------------------------------------------
# Context assembly
# ---------------------------------------------------------------------------

def assemble_external_context(
    results: list[dict[str, str]],
    queries: list[str],
    max_tokens: int = DEFAULT_MAX_TOKENS,
    gathered_at: str | None = None,
) -> str:
    """Format gathered results as markdown for handoff ## External Context section.

    Truncates output to max_tokens budget. Returns empty string if no results.
    """
    if not results:
        return ""

    ts = gathered_at or datetime.now(timezone.utc).isoformat()
    source_set = sorted({r.get("source", "?").split(":")[0] for r in results})
    sources_str = " + ".join(source_set)

    lines: list[str] = [
        "## External Context (pre-compiled by N07 via MCP)",
        "Source: %s (gathered %s)" % (sources_str, ts),
        "",
    ]

    for result in results:
        title = result.get("title", "?")
        url = result.get("url", "")
        snippet = (result.get("snippet") or "").strip()
        src = result.get("source", "?")

        lines.append("### [%s] %s" % (src, title))
        if url and url != title:
            lines.append("URL: %s" % url)
        if snippet:
            lines.append(snippet)
        lines.append("")

    full_text = "\n".join(lines)

    # Truncate to token budget
    tokens = count_tokens(full_text)
    if tokens > max_tokens:
        ratio = max_tokens / max(tokens, 1)
        char_limit = int(len(full_text) * ratio * 0.9)
        full_text = full_text[:char_limit] + "\n\n[... truncated to token budget ...]"

    return full_text


# ---------------------------------------------------------------------------
# Cache I/O
# ---------------------------------------------------------------------------

def _gather_hash(nucleus: str, task_prefix: str) -> str:
    h = hashlib.sha256(("mcp:%s:%s" % (nucleus, task_prefix)).encode()).hexdigest()[:12]
    return h


def write_external_cache(
    nucleus: str,
    task_prefix: str,
    context_md: str,
    audit: dict[str, Any],
) -> tuple[Path, Path]:
    """Write context markdown + audit JSON to cache directory."""
    ensure_dir(CACHE_DIR)
    h = _gather_hash(nucleus, task_prefix)
    context_path = CACHE_DIR / ("%s_%s_external.md" % (nucleus, h))
    audit_path = CACHE_DIR / ("%s_audit.json" % h)

    context_path.write_text(context_md, encoding="utf-8")
    audit_path.write_text(
        json.dumps(audit, indent=2, ensure_ascii=True), encoding="utf-8"
    )
    return context_path, audit_path


def read_external_cache(nucleus: str, task_prefix: str) -> str | None:
    """Read cached external context if present."""
    h = _gather_hash(nucleus, task_prefix)
    context_path = CACHE_DIR / ("%s_%s_external.md" % (nucleus, h))
    if context_path.exists():
        try:
            return context_path.read_text(encoding="utf-8")
        except OSError:
            return None
    return None


# ---------------------------------------------------------------------------
# Main gather pipeline
# ---------------------------------------------------------------------------

def _skipped(reason: str) -> dict[str, Any]:
    return {
        "skipped": True,
        "skipped_reason": reason,
        "has_context": False,
        "context_md": "",
        "tokens_used": 0,
        "sources_used": [],
        "queries": [],
        "result_count": 0,
        "context_path": "",
        "audit_path": "",
        "elapsed_ms": 0,
    }


def gather_external_context(
    nucleus: str,
    kind: str,
    task: str,
    domain: str = "",
    config: dict[str, Any] | None = None,
    dry_run: bool = False,
    force: bool = False,
    mcp_data: dict[str, Any] | None = None,
    fetch_urls: list[str] | None = None,
) -> dict[str, Any]:
    """Phase 0 external context gather pipeline.

    Args:
        nucleus:    Nucleus ID (e.g., 'n01')
        kind:       CEX kind (e.g., 'knowledge_card')
        task:       Task description text
        domain:     Optional domain hint (e.g., 'edtech')
        config:     preflight_mcp config dict (loaded if None)
        dry_run:    Generate queries only, skip HTTP calls
        force:      Ignore cached results, re-gather
        mcp_data:   Pre-gathered MCP data from N07 agent tool calls
        fetch_urls: Specific URLs to fetch directly

    Returns dict with keys:
        skipped, skipped_reason, has_context, context_md, tokens_used,
        sources_used, queries, result_count, context_path, audit_path,
        elapsed_ms, cache_hit
    """
    start = time.monotonic()

    if config is None:
        config = load_mcp_config()

    if not config.get("enabled", True):
        return _skipped("preflight_mcp disabled in config")

    if not requires_external_context(kind):
        return _skipped(
            "kind=%s: requires_external_context=false (structural generation only)" % kind
        )

    task_key = task[:200]

    # Serve from cache if available
    if not force and not dry_run:
        cached = read_external_cache(nucleus, task_key)
        if cached:
            return {
                "skipped": False,
                "has_context": True,
                "context_md": cached,
                "tokens_used": count_tokens(cached),
                "sources_used": ["cache"],
                "queries": [],
                "result_count": 1,
                "context_path": "",
                "audit_path": "",
                "elapsed_ms": int((time.monotonic() - start) * 1000),
                "cache_hit": True,
            }

    max_tokens = config.get("max_external_tokens", DEFAULT_MAX_TOKENS)
    timeout = config.get("timeout_seconds", DEFAULT_TIMEOUT)
    delay_ms = config.get("delay_between_queries_ms", DEFAULT_DELAY_MS)

    queries = generate_queries(task, kind, domain)

    if dry_run:
        return {
            "skipped": False,
            "has_context": False,
            "context_md": "",
            "tokens_used": 0,
            "sources_used": [],
            "queries": queries,
            "result_count": 0,
            "context_path": "",
            "audit_path": "",
            "elapsed_ms": int((time.monotonic() - start) * 1000),
            "dry_run": True,
        }

    all_results: list[dict[str, str]] = []
    providers_used: list[str] = []

    if mcp_data:
        # Mode 1: Accept pre-gathered data from N07 agent tool calls
        injected = inject_mcp_results(mcp_data)
        all_results.extend(injected)
        if injected:
            providers_used.append("mcp_injected")
    else:
        # Mode 2: Direct HTTP sources (GitHub REST + URL fetch)
        providers = config.get("providers", {})

        gh_cfg = providers.get("github", {})
        if gh_cfg.get("enabled", True) and os.environ.get("GITHUB_TOKEN"):
            gh_results = gather_github(queries, config, timeout=timeout, delay_ms=delay_ms)
            all_results.extend(gh_results)
            if gh_results:
                providers_used.append("github")

        if fetch_urls:
            fetch_results = gather_fetch(fetch_urls, timeout=timeout)
            all_results.extend(fetch_results)
            if fetch_results:
                providers_used.append("fetch")

    # Assemble context markdown
    gathered_at = datetime.now(timezone.utc).isoformat()
    context_md = assemble_external_context(
        all_results, queries, max_tokens=max_tokens, gathered_at=gathered_at
    )

    tokens_used = count_tokens(context_md) if context_md else 0
    sources_used = list({r.get("source", "?").split(":")[0] for r in all_results})

    audit: dict[str, Any] = {
        "nucleus": nucleus,
        "kind": kind,
        "task_prefix": task_key,
        "gathered_at": gathered_at,
        "queries": queries,
        "result_count": len(all_results),
        "tokens_consumed": tokens_used,
        "sources": sources_used,
        "providers_attempted": providers_used,
        "elapsed_ms": int((time.monotonic() - start) * 1000),
        "has_context": bool(context_md),
        "github_token_present": bool(os.environ.get("GITHUB_TOKEN")),
        "brave_key_present": bool(os.environ.get("BRAVE_API_KEY")),
    }

    context_path_str = ""
    audit_path_str = ""
    if context_md and config.get("audit_log", True):
        cp, ap = write_external_cache(nucleus, task_key, context_md, audit)
        context_path_str = str(cp)
        audit_path_str = str(ap)

    return {
        "skipped": False,
        "has_context": bool(context_md),
        "context_md": context_md,
        "tokens_used": tokens_used,
        "sources_used": sources_used,
        "queries": queries,
        "result_count": len(all_results),
        "context_path": context_path_str,
        "audit_path": audit_path_str,
        "elapsed_ms": int((time.monotonic() - start) * 1000),
        "cache_hit": False,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _print_result(result: dict[str, Any], verbose: bool = False) -> None:
    if result.get("skipped"):
        print("[SKIP] %s" % result.get("skipped_reason", ""))
        return
    if result.get("dry_run"):
        print("[DRY-RUN] Queries generated:")
        for q in result.get("queries", []):
            print("  - %s" % q)
        return

    print("=" * 60)
    print("  CEX Preflight Phase 0 -- MCP Gather Result")
    print("=" * 60)
    print("  has_context:  %s" % result.get("has_context", False))
    print("  tokens_used:  %d" % result.get("tokens_used", 0))
    print("  result_count: %d" % result.get("result_count", 0))
    print("  sources:      %s" % ", ".join(result.get("sources_used", [])))
    print("  elapsed:      %dms" % result.get("elapsed_ms", 0))
    print("  cache_hit:    %s" % result.get("cache_hit", False))
    if result.get("queries"):
        print("")
        print("  Queries used:")
        for q in result.get("queries", []):
            print("    - %s" % q)
    if result.get("context_path"):
        print("")
        print("  Context: %s" % result["context_path"])
    if result.get("audit_path"):
        print("  Audit:   %s" % result["audit_path"])
    if verbose and result.get("context_md"):
        print("")
        print("  Context preview (first 500 chars):")
        preview = result["context_md"][:500].replace("\n", "\n  ")
        print("  %s" % preview)
    print("=" * 60)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="CEX Preflight Phase 0 -- MCP external context gather"
    )
    parser.add_argument("--nucleus", "-n", default="n07", help="Nucleus ID (default: n07)")
    parser.add_argument("--kind", "-k", help="CEX kind (e.g., knowledge_card)")
    parser.add_argument("--task", "-t", help="Task description text")
    parser.add_argument("--domain", "-d", default="", help="Domain hint (e.g., edtech)")
    parser.add_argument("--check", action="store_true",
                        help="Check if kind requires external context, then exit")
    parser.add_argument("--queries", action="store_true",
                        help="Print generated queries only, do not gather")
    parser.add_argument("--gather", action="store_true",
                        help="Run full gather pipeline (default when --task provided)")
    parser.add_argument("--input-json", metavar="PATH_OR_JSON",
                        help="JSON file path or inline JSON with pre-gathered MCP data")
    parser.add_argument("--fetch-urls", nargs="+", metavar="URL",
                        help="Specific URLs to fetch directly")
    parser.add_argument("--dry-run", action="store_true",
                        help="Generate queries only, skip all HTTP calls")
    parser.add_argument("--force", action="store_true",
                        help="Ignore cached results, re-gather")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show context preview in output")
    parser.add_argument("--json", action="store_true", help="Output result as JSON")
    args = parser.parse_args()

    # --check mode
    if args.check:
        if not args.kind:
            print("[ERR] --kind required for --check")
            return 1
        needs = requires_external_context(args.kind)
        live = requires_live_tools(args.kind)
        if args.json:
            print(json.dumps({
                "kind": args.kind,
                "requires_external_context": needs,
                "requires_live_tools": live,
            }))
        else:
            print("kind=%s  requires_external_context=%s  requires_live_tools=%s" % (
                args.kind, needs, live))
        return 0

    # --queries mode
    if args.queries:
        if not args.kind or not args.task:
            print("[ERR] --kind and --task required for --queries")
            return 1
        qs = generate_queries(args.task, args.kind, args.domain)
        if args.json:
            print(json.dumps({"kind": args.kind, "queries": qs}))
        else:
            print("Queries for kind=%s:" % args.kind)
            for q in qs:
                print("  - %s" % q)
        return 0

    # Require kind + task for all remaining modes
    if not args.kind:
        parser.print_help()
        return 1
    if not args.task:
        print("[ERR] --task is required")
        return 1

    # Load pre-gathered MCP data if provided
    mcp_data: dict[str, Any] | None = None
    if args.input_json:
        raw = args.input_json.strip()
        try:
            if raw.startswith("{") or raw.startswith("["):
                mcp_data = json.loads(raw)
            else:
                mcp_data = json.loads(Path(raw).read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            print("[ERR] Failed to parse --input-json: %s" % exc)
            return 1

    config = load_mcp_config()
    result = gather_external_context(
        nucleus=args.nucleus,
        kind=args.kind,
        task=args.task,
        domain=args.domain,
        config=config,
        dry_run=args.dry_run,
        force=args.force,
        mcp_data=mcp_data,
        fetch_urls=args.fetch_urls,
    )

    if args.json:
        out = {k: v for k, v in result.items() if k != "context_md"}
        print(json.dumps(out, indent=2))
    else:
        _print_result(result, verbose=args.verbose)

    if result.get("skipped") or result.get("dry_run"):
        return 0
    return 0 if result.get("has_context") else 2


if __name__ == "__main__":
    sys.exit(main())
