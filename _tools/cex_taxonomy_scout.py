#!/usr/bin/env python3
"""
cex_taxonomy_scout.py -- Weekly Taxonomy Discovery Engine

Scans configured sources (GitHub, arXiv, IETF, W3C, community), extracts
candidate kinds, scores them, deduplicates against kinds_meta.json, and
writes candidates to .cex/runtime/taxonomy_candidates/ for N07 review.

Usage:
  python _tools/cex_taxonomy_scout.py --source all --since 7
  python _tools/cex_taxonomy_scout.py --source github --since 1 --dry-run
  python _tools/cex_taxonomy_scout.py --source arxiv --since 14
  python _tools/cex_taxonomy_scout.py --report
  python _tools/cex_taxonomy_scout.py --deprecate kind_name --successor new_kind
  python _tools/cex_taxonomy_scout.py --recheck-all --since 180

Config: .cex/P09_config/taxonomy_sources.yaml
Output: .cex/runtime/taxonomy_candidates/YYYY-MM-DD_{source}_{slug}.md
Log:    .cex/runtime/taxonomy_candidates/scout_log.tsv

ASCII-only output. See .claude/rules/ascii-code-rule.md.
"""

import argparse
import datetime
import hashlib
import json
import math
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

CEX_ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(CEX_ROOT))

CANDIDATES_DIR = CEX_ROOT / ".cex" / "runtime" / "taxonomy_candidates"
REJECTED_DIR = CANDIDATES_DIR / "rejected"
APPLIED_DIR = CANDIDATES_DIR / "applied"
SCOUT_LOG = CANDIDATES_DIR / "scout_log.tsv"
KINDS_META = CEX_ROOT / ".cex" / "kinds_meta.json"
SOURCES_CONFIG = CEX_ROOT / ".cex" / "config" / "taxonomy_sources.yaml"
KINDS_ARCHIVE = CEX_ROOT / ".cex" / "kinds_archive.json"

TODAY = datetime.date.today().isoformat()

SCORE_THRESHOLD_NOTIFY = 6.0
SCORE_THRESHOLD_AUTO = 8.0

# ---------------------------------------------------------------------------
# YAML minimal parser (no dependency on PyYAML)
# ---------------------------------------------------------------------------

def load_yaml_simple(path: Path) -> dict:
    """
    Minimal YAML loader that handles the taxonomy_sources.yaml structure.
    Handles: top-level keys, list items (- key: value), nested keys.
    Not a full YAML parser -- only covers what the config file needs.
    """
    import yaml as _yaml
    try:
        with open(path, encoding="utf-8") as fh:
            return _yaml.safe_load(fh)
    except ImportError:
        pass
    # Fallback: very basic hand-rolled parser for simple YAML
    result = {}
    current_section = None
    current_item = None
    with open(path, encoding="utf-8") as fh:
        for raw_line in fh:
            line = raw_line.rstrip()
            if not line or line.lstrip().startswith("#"):
                continue
            if not line.startswith(" ") and not line.startswith("-"):
                if ":" in line:
                    key = line.split(":")[0].strip()
                    val_raw = line.split(":", 1)[1].strip()
                    if not val_raw or val_raw == "|":
                        result[key] = []
                        current_section = key
                        current_item = None
                    else:
                        result[key] = val_raw.strip('"')
                        current_section = None
            elif line.startswith("  - ") or line.startswith("- "):
                stripped = line.lstrip("- ").strip()
                if current_section and isinstance(result.get(current_section), list):
                    current_item = {}
                    result[current_section].append(current_item)
                    if ":" in stripped:
                        k, v = stripped.split(":", 1)
                        current_item[k.strip()] = v.strip().strip('"')
            elif line.startswith("    ") and current_item is not None:
                stripped = line.strip()
                if stripped.startswith("- "):
                    pass  # skip sub-lists for now
                elif ":" in stripped:
                    k, v = stripped.split(":", 1)
                    current_item[k.strip()] = v.strip().strip('"')
    return result


# ---------------------------------------------------------------------------
# kinds_meta.json loader
# ---------------------------------------------------------------------------

def load_kinds_meta() -> dict:
    if not KINDS_META.exists():
        return {}
    with open(KINDS_META, encoding="utf-8") as fh:
        return json.load(fh)


def save_kinds_meta(data: dict) -> None:
    with open(KINDS_META, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


# ---------------------------------------------------------------------------
# TF-IDF deduplication (no external deps)
# ---------------------------------------------------------------------------

def tokenize(text: str) -> list:
    return re.findall(r"[a-z][a-z0-9_]+", text.lower())


def build_tfidf_vectors(docs: list) -> list:
    """docs: list of strings. Returns list of {term: tfidf} dicts."""
    N = len(docs)
    tokenized = [tokenize(d) for d in docs]
    df = {}
    for tokens in tokenized:
        for t in set(tokens):
            df[t] = df.get(t, 0) + 1
    idf = {t: math.log(N / (1 + c)) for t, c in df.items()}
    vectors = []
    for tokens in tokenized:
        tf = {}
        for t in tokens:
            tf[t] = tf.get(t, 0) + 1
        total = max(len(tokens), 1)
        vec = {t: (c / total) * idf.get(t, 0) for t, c in tf.items()}
        vectors.append(vec)
    return vectors


def cosine_sim(a: dict, b: dict) -> float:
    keys = set(a) & set(b)
    if not keys:
        return 0.0
    dot = sum(a[k] * b[k] for k in keys)
    mag_a = math.sqrt(sum(v * v for v in a.values()))
    mag_b = math.sqrt(sum(v * v for v in b.values()))
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return dot / (mag_a * mag_b)


def is_duplicate(candidate_desc: str, kinds_meta: dict, threshold: float = 0.85) -> tuple:
    """
    Returns (is_dup: bool, similar_kind: str or None, sim_score: float).
    """
    if not kinds_meta:
        return False, None, 0.0
    kind_descs = [
        f"{k} {v.get('description', '')} {v.get('boundary', '')}"
        for k, v in kinds_meta.items()
    ]
    all_docs = [candidate_desc] + kind_descs
    vectors = build_tfidf_vectors(all_docs)
    cand_vec = vectors[0]
    best_sim = 0.0
    best_kind = None
    for i, kind_name in enumerate(kinds_meta.keys()):
        sim = cosine_sim(cand_vec, vectors[i + 1])
        if sim > best_sim:
            best_sim = sim
            best_kind = kind_name
    if best_sim >= threshold:
        return True, best_kind, best_sim
    return False, best_kind, best_sim


# ---------------------------------------------------------------------------
# Candidate scoring
# ---------------------------------------------------------------------------

def score_candidate(
    adoption_signal: float = 5.0,
    stability: float = 5.0,
    urgency: float = 5.0,
    relevance: float = 5.0,
) -> float:
    """Composite score 0-10 using weighted dimensions."""
    return (
        adoption_signal * 0.35
        + stability * 0.30
        + urgency * 0.20
        + relevance * 0.15
    )


# ---------------------------------------------------------------------------
# HTTP helpers (stdlib only)
# ---------------------------------------------------------------------------

def http_get(url: str, headers: dict = None, timeout: int = 15) -> Optional[str]:
    req = urllib.request.Request(url, headers=headers or {})
    req.add_header("User-Agent", "cex-taxonomy-scout/1.0 (+https://github.com/cex)")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, urllib.error.HTTPError) as exc:
        print(f"  [WARN] HTTP error for {url}: {exc}")
        return None


def http_get_json(url: str, headers: dict = None, timeout: int = 15) -> Optional[dict]:
    raw = http_get(url, headers=headers, timeout=timeout)
    if raw is None:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"  [WARN] JSON decode error: {exc}")
        return None


# ---------------------------------------------------------------------------
# GitHub source scanner
# ---------------------------------------------------------------------------

GITHUB_API = "https://api.github.com"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")


def github_headers() -> dict:
    h = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        h["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return h


def github_list_changed_files(repo: str, since_days: int) -> list:
    """Return list of (path, content_url) changed in the last since_days."""
    since_dt = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=since_days)
    since_iso = since_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    url = f"{GITHUB_API}/repos/{repo}/commits?since={since_iso}&per_page=30"
    commits = http_get_json(url, headers=github_headers())
    if not commits or not isinstance(commits, list):
        return []
    changed = []
    seen_shas = set()
    for commit in commits[:10]:
        sha = commit.get("sha", "")
        if sha in seen_shas:
            continue
        seen_shas.add(sha)
        detail_url = f"{GITHUB_API}/repos/{repo}/commits/{sha}"
        detail = http_get_json(detail_url, headers=github_headers())
        if not detail:
            continue
        for f in detail.get("files", []):
            fname = f.get("filename", "")
            raw_url = f.get("raw_url", "")
            changed.append((fname, raw_url))
    return changed


def extract_candidates_from_text(
    text: str, patterns: list, source_name: str, source_url: str
) -> list:
    """Extract candidate kind names from raw text using regex patterns."""
    candidates = []
    for pattern in patterns:
        try:
            matches = re.findall(pattern, text)
        except re.error:
            continue
        for match in matches:
            # Normalize to snake_case kind name
            raw = re.sub(r"[^a-zA-Z0-9_]", "", match)
            if len(raw) < 4 or len(raw) > 60:
                continue
            # Convert PascalCase to snake_case
            kind_name = re.sub(r"([A-Z])", r"_\1", raw).lower().strip("_")
            kind_name = re.sub(r"_+", "_", kind_name)
            candidates.append({
                "raw_match": match,
                "kind_name": kind_name,
                "source": source_name,
                "upstream_url": source_url,
                "context": text[:200].replace("\n", " "),
            })
    return candidates


def scan_github_source(source_cfg: dict, since_days: int, dry_run: bool) -> list:
    """Scan a GitHub source and return list of candidate dicts."""
    repo_url = source_cfg.get("url", "")
    # Extract org/repo from URL
    m = re.search(r"github.com/([^/]+/[^/]+)", repo_url)
    if not m:
        print(f"  [WARN] Cannot parse repo from URL: {repo_url}")
        return []
    repo = m.group(1).rstrip("/")
    watch_paths = source_cfg.get("watch_paths", [])
    patterns = source_cfg.get("extract_patterns", [])
    name = source_cfg.get("name", repo)
    print(f"  Scanning GitHub: {repo} (last {since_days}d)")
    changed_files = github_list_changed_files(repo, since_days)
    if not changed_files:
        print(f"    No changes found.")
        return []
    raw_candidates = []
    for fpath, raw_url in changed_files:
        # Filter to watch_paths
        if watch_paths and not any(fpath.startswith(wp) for wp in watch_paths):
            continue
        if not raw_url:
            continue
        content = http_get(raw_url, headers=github_headers())
        if not content:
            continue
        found = extract_candidates_from_text(content, patterns, name, repo_url)
        raw_candidates.extend(found)
    print(f"    Raw candidates: {len(raw_candidates)}")
    return raw_candidates


# ---------------------------------------------------------------------------
# arXiv source scanner
# ---------------------------------------------------------------------------

ARXIV_API = "http://export.arxiv.org/api/query"


def scan_arxiv_source(source_cfg: dict, since_days: int, dry_run: bool) -> list:
    """Scan arXiv feed and return candidate dicts."""
    categories = source_cfg.get("categories", ["cs.AI"])
    keywords = source_cfg.get("keywords", {})
    required_any = keywords.get("required_any", [])
    name = source_cfg.get("name", "arxiv")
    cat_query = " OR ".join(f"cat:{c}" for c in categories)
    kw_query = " OR ".join(f'ti:"{k}" OR abs:"{k}"' for k in required_any[:4])
    full_query = f"({cat_query}) AND ({kw_query})"
    since_dt = datetime.datetime.utcnow() - datetime.timedelta(days=since_days)
    params = urllib.parse.urlencode({
        "search_query": full_query,
        "start": 0,
        "max_results": 20,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    })
    url = f"{ARXIV_API}?{params}"
    print(f"  Scanning arXiv: {' '.join(categories)} (last {since_days}d)")
    content = http_get(url)
    if not content:
        return []
    candidates = []
    # Extract titles and abstracts
    titles = re.findall(r"<title>(.*?)</title>", content, re.DOTALL)
    abstracts = re.findall(r"<summary>(.*?)</summary>", content, re.DOTALL)
    links = re.findall(r"<id>(http://arxiv.org/abs/[^<]+)</id>", content)
    for i, title in enumerate(titles[1:], 0):  # skip feed title
        abs_text = abstracts[i] if i < len(abstracts) else ""
        link = links[i] if i < len(links) else ""
        text = f"{title} {abs_text}"
        # Look for proposed protocols/schemas in abstracts
        proto_matches = re.findall(
            r"(?:propose|present|introduce|novel)\s+(?:a\s+)?([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+){0,3})"
            r"(?:\s+(?:protocol|schema|framework|format|standard|specification|interface))",
            text
        )
        for raw in proto_matches:
            kind_name = re.sub(r"\s+", "_", raw.lower().strip())
            kind_name = re.sub(r"[^a-z0-9_]", "", kind_name)
            if len(kind_name) < 4:
                continue
            candidates.append({
                "raw_match": raw,
                "kind_name": kind_name,
                "source": name,
                "upstream_url": link,
                "context": title.strip()[:200],
            })
    print(f"    Raw candidates: {len(candidates)}")
    return candidates


# ---------------------------------------------------------------------------
# Community scanner (HackerNews)
# ---------------------------------------------------------------------------

HN_SEARCH = "https://hn.algolia.com/api/v1/search"


def scan_hackernews(source_cfg: dict, since_days: int, dry_run: bool) -> list:
    """Scan HackerNews for Show HN posts matching query."""
    query = source_cfg.get("query", "agent protocol schema")
    # Simplify: strip boolean operators
    clean_query = re.sub(r"\b(AND|OR|NOT)\b", "", query)
    clean_query = re.sub(r"[()]", "", clean_query).strip()
    min_points = source_cfg.get("min_points", 100)
    since_ts = int(
        (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=since_days)).timestamp()
    )
    params = urllib.parse.urlencode({
        "query": clean_query,
        "tags": "show_hn",
        "numericFilters": f"points>{min_points},created_at_i>{since_ts}",
        "hitsPerPage": 20,
    })
    url = f"{HN_SEARCH}?{params}"
    print(f"  Scanning HackerNews Show HN (last {since_days}d)")
    data = http_get_json(url)
    if not data:
        return []
    hits = data.get("hits", [])
    candidates = []
    for hit in hits:
        title = hit.get("title", "")
        url_hit = hit.get("url", "")
        # Look for protocol/schema/tool mentions
        m = re.search(
            r"([A-Z][a-zA-Z]+(?:\s[A-Z][a-zA-Z]+){0,2})"
            r"(?:\s*[-:]\s*|\s+(?:for|a|an|the)\s+)"
            r"(?:agent|protocol|schema|API|SDK|framework|tool|interface)",
            title,
            re.IGNORECASE
        )
        if m:
            raw = m.group(1)
            kind_name = re.sub(r"\s+", "_", raw.lower())
            kind_name = re.sub(r"[^a-z0-9_]", "", kind_name)
            if len(kind_name) >= 4:
                candidates.append({
                    "raw_match": raw,
                    "kind_name": kind_name,
                    "source": "hackernews",
                    "upstream_url": url_hit or f"https://news.ycombinator.com/item?id={hit.get('objectID', '')}",
                    "context": title[:200],
                })
    print(f"    Raw candidates: {len(candidates)}")
    return candidates


# ---------------------------------------------------------------------------
# Candidate file writer
# ---------------------------------------------------------------------------

def write_candidate(
    candidate: dict,
    score: float,
    score_breakdown: dict,
    similar_kind: Optional[str],
    sim_score: float,
    dry_run: bool,
) -> Optional[Path]:
    """Write candidate .md file to taxonomy_candidates/. Returns path or None."""
    CANDIDATES_DIR.mkdir(parents=True, exist_ok=True)
    kind_slug = candidate["kind_name"][:50]
    source_slug = re.sub(r"[^a-z0-9]", "_", candidate["source"].lower())[:20]
    filename = f"{TODAY}_{source_slug}_{kind_slug}.md"
    dest = CANDIDATES_DIR / filename
    # Idempotent: skip if exists
    if dest.exists():
        return dest
    suggested_pillar = "P04"  # default tool/protocol
    # Rough heuristic: memory->P10, schema->P06, config->P09, etc.
    if any(x in kind_slug for x in ["memory", "index", "embed", "chunk", "retriev"]):
        suggested_pillar = "P10"
    elif any(x in kind_slug for x in ["schema", "type", "validation", "contract"]):
        suggested_pillar = "P06"
    elif any(x in kind_slug for x in ["config", "env", "secret", "feature_flag"]):
        suggested_pillar = "P09"
    elif any(x in kind_slug for x in ["agent", "model", "provider", "boot"]):
        suggested_pillar = "P02"
    elif any(x in kind_slug for x in ["prompt", "template", "chain", "system"]):
        suggested_pillar = "P03"
    elif any(x in kind_slug for x in ["eval", "score", "bench", "test", "judge"]):
        suggested_pillar = "P07"
    similar_line = similar_kind if similar_kind else "null"
    breakdown_lines = "\n".join(
        f"  {k}: {v:.1f}" for k, v in score_breakdown.items()
    )
    content = f"""---
candidate_id: {kind_slug}
source: {candidate["source"]}
discovered: {TODAY}
score: {score:.1f}
score_breakdown:
{breakdown_lines}
suggested_kind: {kind_slug}
suggested_pillar: {suggested_pillar}
suggested_boundary: "TBD -- review upstream spec for precise boundary definition."
similar_kinds: [{similar_line}]
similarity_score: {sim_score:.3f}
merge_candidate: null
upstream_url: {candidate["upstream_url"]}
status: pending_review
---

## Summary

Candidate `{kind_slug}` discovered via {candidate["source"]}.
Raw match: `{candidate["raw_match"]}`
Context: {candidate["context"][:300]}

## Evidence

- Upstream: {candidate["upstream_url"]}
- Similarity to existing kinds: {sim_score:.1%} (vs {similar_line})
- Score: {score:.1f}/10

## Review Notes

Fill in after reviewing upstream spec:
- Adoption signals (stars, downloads, implementations)
- Spec version and stability
- Precise boundary vs similar kinds

## Decision (N07 fills)

- [ ] Build now
- [ ] Wait for stabilization
- [ ] Merge into existing kind: ___
- [ ] Reject -- reason: ___
"""
    if dry_run:
        print(f"    [dry-run] Would write: {dest.name} (score={score:.1f})")
        return None
    dest.write_text(content, encoding="utf-8")
    return dest


# ---------------------------------------------------------------------------
# Main dedup + score pipeline
# ---------------------------------------------------------------------------

def dedupe_and_score(raw_candidates: list, kinds_meta: dict) -> list:
    """
    Deduplicate candidates against each other and against existing kinds.
    Score each and return list of (candidate, score, breakdown, similar_kind, sim_score).
    """
    seen_slugs = set(kinds_meta.keys())
    seen_new = set()
    results = []
    for cand in raw_candidates:
        slug = cand["kind_name"]
        if slug in seen_slugs or slug in seen_new:
            continue
        seen_new.add(slug)
        # Build description for similarity check
        desc = f"{slug} {cand['raw_match']} {cand['context']}"
        is_dup, similar_kind, sim_score = is_duplicate(desc, kinds_meta, threshold=0.85)
        if is_dup:
            print(f"    [skip] {slug} -- similar to {similar_kind} ({sim_score:.1%})")
            continue
        # Scoring heuristics (real signals require network; defaults are neutral)
        adoption = 5.0
        stability = 4.0  # unknown -> cautious
        urgency = 7.0 if similar_kind is None else 5.0
        relevance = 7.0  # found via CEX-targeted query -> assumed relevant
        total = score_candidate(adoption, stability, urgency, relevance)
        breakdown = {
            "adoption_signal": adoption,
            "stability": stability,
            "urgency": urgency,
            "relevance": relevance,
        }
        results.append((cand, total, breakdown, similar_kind, sim_score))
    return results


# ---------------------------------------------------------------------------
# Log writer
# ---------------------------------------------------------------------------

def append_log(source: str, found: int, new_written: int, merged: int, rejected: int, errors: int) -> None:
    CANDIDATES_DIR.mkdir(parents=True, exist_ok=True)
    header = "run_date\tsource\tcandidates_found\tcandidates_new\tcandidates_merged\tcandidates_rejected\terrors\n"
    if not SCOUT_LOG.exists():
        SCOUT_LOG.write_text(header, encoding="utf-8")
    row = f"{TODAY}\t{source}\t{found}\t{new_written}\t{merged}\t{rejected}\t{errors}\n"
    with open(SCOUT_LOG, "a", encoding="utf-8") as fh:
        fh.write(row)


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def report() -> None:
    """Print taxonomy health dashboard."""
    kinds_meta = load_kinds_meta()
    total_kinds = len(kinds_meta)
    stable = sum(1 for v in kinds_meta.values() if v.get("status", "stable") == "stable")
    deprecated = sum(1 for v in kinds_meta.values() if v.get("status") == "deprecated")
    archived = sum(1 for v in kinds_meta.values() if v.get("status") == "archived")
    draft = sum(1 for v in kinds_meta.values() if v.get("status") == "draft")
    pending = list(CANDIDATES_DIR.glob("*.md"))
    # Freshness
    stale_180 = 0
    stale_90 = 0
    for v in kinds_meta.values():
        lr = v.get("last_reviewed")
        if not lr:
            stale_180 += 1
            continue
        try:
            age = (datetime.date.today() - datetime.date.fromisoformat(lr)).days
            if age > 180:
                stale_180 += 1
            elif age > 90:
                stale_90 += 1
        except ValueError:
            pass
    # Last scout run
    last_run = "never"
    if SCOUT_LOG.exists():
        lines = SCOUT_LOG.read_text(encoding="utf-8").strip().split("\n")
        if len(lines) > 1:
            last_row = lines[-1].split("\t")
            if last_row:
                last_run = last_row[0]
    print("=== CEX Taxonomy Health ===")
    print(f"Active kinds:       {stable:>5} ({total_kinds} total with {draft} draft)")
    print(f"Deprecated:         {deprecated:>5}")
    print(f"Archived:           {archived:>5}")
    print(f"Stale >180d:        {stale_180:>5} {'[RED]' if stale_180 > 10 else '[YELLOW]' if stale_180 > 0 else '[GREEN]'}")
    print(f"Stale 90-180d:      {stale_90:>5} {'[YELLOW]' if stale_90 > 0 else '[GREEN]'}")
    print(f"Candidates pending: {len(pending):>5}")
    print(f"Scout last run:     {last_run}")
    print("===========================")


# ---------------------------------------------------------------------------
# Deprecation helper
# ---------------------------------------------------------------------------

def cmd_deprecate(kind_name: str, successor: str, dry_run: bool) -> None:
    kinds_meta = load_kinds_meta()
    if kind_name not in kinds_meta:
        print(f"[FAIL] Kind not found: {kind_name}")
        sys.exit(1)
    if successor not in kinds_meta:
        print(f"[WARN] Successor kind not found in meta: {successor}")
    if dry_run:
        print(f"[dry-run] Would deprecate {kind_name} -> {successor}")
        return
    kinds_meta[kind_name]["status"] = "deprecated"
    kinds_meta[kind_name]["deprecated_by"] = successor
    save_kinds_meta(kinds_meta)
    # Write migration file
    mig_dir = CEX_ROOT / "N04_knowledge" / "migrations"
    mig_dir.mkdir(parents=True, exist_ok=True)
    mig_file = mig_dir / f"deprecation_{kind_name}_{TODAY}.md"
    mig_file.write_text(
        f"---\nkind: {kind_name}\ndeprecated_by: {successor}\n"
        f"deprecated_since: {TODAY}\narchived_after: TBD\n"
        f"reason: 'Manually deprecated via cex_taxonomy_scout.py'\n---\n\n"
        f"## Migration Guide\n\nReplace `{kind_name}` with `{successor}`.\n\n"
        f"Auto-migration:\n  python _tools/cex_migrate.py --from {kind_name} --to {successor}\n",
        encoding="utf-8"
    )
    print(f"[OK] Deprecated {kind_name} -> {successor}")
    print(f"     Migration file: {mig_file}")


# ---------------------------------------------------------------------------
# Recheck stale kinds
# ---------------------------------------------------------------------------

def cmd_recheck_all(since_days: int, dry_run: bool) -> None:
    kinds_meta = load_kinds_meta()
    cutoff = datetime.date.today() - datetime.timedelta(days=since_days)
    stale_kinds = []
    for kind_name, meta in kinds_meta.items():
        lr = meta.get("last_reviewed")
        if not lr:
            stale_kinds.append(kind_name)
            continue
        try:
            if datetime.date.fromisoformat(lr) < cutoff:
                stale_kinds.append(kind_name)
        except ValueError:
            stale_kinds.append(kind_name)
    print(f"[OK] Found {len(stale_kinds)} kinds with last_reviewed > {since_days}d ago")
    if dry_run:
        for k in stale_kinds[:10]:
            print(f"  {k}")
        if len(stale_kinds) > 10:
            print(f"  ... and {len(stale_kinds) - 10} more")
        return
    # Write stale-review candidates
    CANDIDATES_DIR.mkdir(parents=True, exist_ok=True)
    for kind_name in stale_kinds:
        meta = kinds_meta[kind_name]
        fname = f"{TODAY}_stale_review_{kind_name}.md"
        dest = CANDIDATES_DIR / fname
        if dest.exists():
            continue
        content = (
            f"---\ncandidate_id: {kind_name}\nsource: stale_review\n"
            f"discovered: {TODAY}\nscore: 5.0\n"
            f"suggested_kind: {kind_name}\nstatus: stale_review\n"
            f"last_reviewed: {meta.get('last_reviewed', 'never')}\n---\n\n"
            f"## Stale Review\n\nKind `{kind_name}` has not been reviewed in >{since_days} days.\n"
            f"Check if upstream spec has changed and update `last_reviewed` in kinds_meta.json.\n"
        )
        dest.write_text(content, encoding="utf-8")
    print(f"[OK] Wrote {len(stale_kinds)} stale-review candidates to {CANDIDATES_DIR}")


# ---------------------------------------------------------------------------
# Main scan orchestrator
# ---------------------------------------------------------------------------

def run_scan(source_filter: str, since_days: int, dry_run: bool) -> None:
    if not SOURCES_CONFIG.exists():
        print(f"[FAIL] Sources config not found: {SOURCES_CONFIG}")
        sys.exit(1)
    config = load_yaml_simple(SOURCES_CONFIG)
    kinds_meta = load_kinds_meta()
    print(f"[OK] Loaded {len(kinds_meta)} existing kinds")
    all_raw = []
    errors = 0
    # GitHub
    if source_filter in ("all", "github"):
        gh_sources = config.get("github", [])
        for src in gh_sources:
            try:
                raw = scan_github_source(src, since_days, dry_run)
                all_raw.extend(raw)
            except Exception as exc:
                print(f"  [FAIL] GitHub {src.get('name', '?')}: {exc}")
                errors += 1
    # arXiv
    if source_filter in ("all", "arxiv"):
        ax_sources = config.get("arxiv", [])
        for src in ax_sources:
            try:
                raw = scan_arxiv_source(src, since_days, dry_run)
                all_raw.extend(raw)
            except Exception as exc:
                print(f"  [FAIL] arXiv {src.get('name', '?')}: {exc}")
                errors += 1
    # HackerNews
    if source_filter in ("all", "community"):
        comm_sources = config.get("community", [])
        for src in comm_sources:
            if src.get("type") == "hackernews":
                try:
                    raw = scan_hackernews(src, since_days, dry_run)
                    all_raw.extend(raw)
                except Exception as exc:
                    print(f"  [FAIL] HN: {exc}")
                    errors += 1
    print(f"\n[OK] Total raw candidates: {len(all_raw)}")
    print("[OK] Deduplicating and scoring...")
    scored = dedupe_and_score(all_raw, kinds_meta)
    print(f"[OK] Net new candidates after dedup: {len(scored)}")
    # Write candidates above threshold
    written = 0
    above_notify = [c for c in scored if c[1] >= SCORE_THRESHOLD_NOTIFY]
    print(f"[OK] Candidates >= {SCORE_THRESHOLD_NOTIFY}: {len(above_notify)}")
    for cand, score, breakdown, similar_kind, sim_score in above_notify:
        path = write_candidate(cand, score, breakdown, similar_kind, sim_score, dry_run)
        if path:
            written += 1
            print(f"    [WRITTEN] {path.name} (score={score:.1f})")
    # Signal if high-scoring candidates found
    high_score_cands = [c for c in scored if c[1] >= SCORE_THRESHOLD_AUTO]
    if high_score_cands and not dry_run:
        try:
            sys.path.insert(0, str(CEX_ROOT / "_tools"))
            from signal_writer import write_signal  # noqa: F401
            write_signal("n04", "taxonomy_candidate_ready", high_score_cands[0][1])
            print(f"[OK] Signal sent: {len(high_score_cands)} high-score candidates ready for N07")
        except Exception as exc:
            print(f"  [WARN] Signal write failed: {exc}")
    append_log(source_filter, len(all_raw), written, 0, 0, errors)
    print(f"\n=== Scout complete ===")
    print(f"  Raw found:  {len(all_raw)}")
    print(f"  Written:    {written}")
    print(f"  Errors:     {errors}")
    if above_notify:
        print(f"  Top candidate: {above_notify[0][0]['kind_name']} (score={above_notify[0][1]:.1f})")


# ---------------------------------------------------------------------------
# kinds_meta.json backfill
# ---------------------------------------------------------------------------

def backfill_kinds_meta(dry_run: bool) -> None:
    """Add lifecycle fields to all existing kinds that lack them."""
    kinds_meta = load_kinds_meta()
    changed = 0
    for kind_name, meta in kinds_meta.items():
        needs_update = False
        if "status" not in meta:
            meta["status"] = "stable"
            needs_update = True
        if "upstream_source" not in meta:
            meta["upstream_source"] = None
            needs_update = True
        if "spec_version" not in meta:
            meta["spec_version"] = None
            needs_update = True
        if "last_reviewed" not in meta:
            meta["last_reviewed"] = TODAY
            needs_update = True
        if "deprecated_by" not in meta:
            meta["deprecated_by"] = None
            needs_update = True
        if needs_update:
            changed += 1
    print(f"[OK] Backfill: {changed} kinds updated with lifecycle fields")
    if dry_run:
        print("[dry-run] No changes written.")
        return
    save_kinds_meta(kinds_meta)
    print(f"[OK] kinds_meta.json saved ({len(kinds_meta)} kinds total)")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="CEX Taxonomy Discovery Scout",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--source",
        choices=["all", "github", "arxiv", "ietf", "w3c", "community"],
        default="all",
        help="Source category to scan (default: all)",
    )
    parser.add_argument(
        "--since",
        type=int,
        default=7,
        help="Days to look back (default: 7)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print candidates without writing files",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Print taxonomy health dashboard and exit",
    )
    parser.add_argument(
        "--backfill",
        action="store_true",
        help="Add lifecycle fields to all existing kinds in kinds_meta.json",
    )
    parser.add_argument(
        "--deprecate",
        metavar="KIND",
        help="Mark a kind as deprecated",
    )
    parser.add_argument(
        "--successor",
        metavar="KIND",
        help="Successor kind for deprecation (required with --deprecate)",
    )
    parser.add_argument(
        "--recheck-all",
        action="store_true",
        dest="recheck_all",
        help="Write stale-review candidates for all kinds older than --since days",
    )
    parser.add_argument(
        "--harvest-first",
        action="store_true",
        dest="harvest_first",
        help="Run cex_source_harvester --apply before scanning (expands sources config)",
    )
    args = parser.parse_args()
    if args.harvest_first:
        import subprocess
        harvester = CEX_ROOT / "_tools" / "cex_source_harvester.py"
        print("[OK] Running source harvester first...")
        result = subprocess.run(
            [sys.executable, str(harvester), "--apply"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print(result.stdout.strip())
            print("[OK] Harvester complete. Proceeding with scout scan.")
        else:
            print("[WARN] Harvester exited non-zero:", result.stderr[:200])
    if args.report:
        report()
        return
    if args.backfill:
        backfill_kinds_meta(args.dry_run)
        return
    if args.deprecate:
        if not args.successor:
            print("[FAIL] --successor is required with --deprecate")
            sys.exit(1)
        cmd_deprecate(args.deprecate, args.successor, args.dry_run)
        return
    if args.recheck_all:
        cmd_recheck_all(args.since, args.dry_run)
        return
    run_scan(args.source, args.since, args.dry_run)


if __name__ == "__main__":
    main()
