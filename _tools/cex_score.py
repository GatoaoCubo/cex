#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CEX Hybrid Scorer -- 3-layer scoring: structural + rubric + semantic (LLM).

Layer 1: STRUCTURAL (free, instant) -- bytes, headings, tables, frontmatter
Layer 2: RUBRIC (free, instant) -- builder's quality_gate hard/soft checks
Layer 3: SEMANTIC (1 LLM call, ~2K tokens) -- only if layers 1+2 >= 8.5

Weights (GDP D01): structural 30% + rubric 30% + semantic 40%
Cache (GDP D03): by content hash -- re-score only if file changed
Evolve sees dimension breakdown (GDP D04) for targeted improvements.

Score ranges:
  9.0-9.3: Excellent -- semantically rich, domain-specific, well-structured
  8.5-8.9: Good -- solid structure, may lack semantic depth
  8.0-8.4: Acceptable -- adequate but thin
  <8.0: Needs rebuild
"""

import hashlib
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE_FILE = ROOT / ".cex" / "score_cache.json"
BUILDERS_DIR = ROOT / "archetypes" / "builders"


# ================================================================
# LAYER 1: STRUCTURAL SCORER (original, free, instant)
# ================================================================

def score_structural(path: str) -> tuple[float, list[str]]:
    """Count-based structural scoring. Returns (score 0-10 raw, notes)."""
    if not os.path.exists(path):
        return (0.0, ["MISSING"])

    content = open(path, 'r', encoding='utf-8').read()
    size = len(content.encode('utf-8'))
    notes = []

    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return (0.0, ["NO_FRONTMATTER"])

    fm = fm_match.group(1)
    body = content[fm_match.end():]

    score = 0.0

    # Frontmatter (max 2.0)
    required = ['id:', 'kind:', 'pillar:', 'quality:']
    desired = ['title:', 'version:', 'author:', 'tags:', 'tldr:', 'domain:', 'created:', 'updated:']
    for field in required:
        if field in fm:
            score += 0.3
        else:
            notes.append(f"missing {field}")
    for field in desired:
        if field in fm:
            score += 0.1

    # Content depth (max 2.5)
    if size >= 1000: score += 0.3
    if size >= 2000: score += 0.4
    if size >= 3000: score += 0.3

    headings = len(re.findall(r'^#{1,3} ', body, re.MULTILINE))
    if headings >= 2: score += 0.3
    if headings >= 5: score += 0.2

    table_rows = len(re.findall(r'^\|.*\|', body, re.MULTILINE))
    if table_rows >= 3: score += 0.3
    if table_rows >= 8: score += 0.2

    list_items = len(re.findall(r'^[-*\d]+[.)] ', body, re.MULTILINE))
    if list_items >= 3: score += 0.2

    code_blocks = len(re.findall(r'```', body))
    if code_blocks >= 2: score += 0.1

    # Domain specificity (max 1.5)
    bad_placeholders = len(re.findall(r'(?i)\b(TODO|TBD|FIXME|insert here|add later)\b', body))
    if bad_placeholders == 0:
        score += 0.5
    else:
        notes.append(f"{bad_placeholders} placeholders")
        score -= 0.3 * bad_placeholders

    body_words = len(body.split())
    if body_words >= 100: score += 0.3
    if body_words >= 200: score += 0.3
    if body_words >= 400: score += 0.2

    tldr_match = re.search(r'tldr:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    if tldr_match and len(tldr_match.group(1)) >= 30:
        score += 0.2

    # Structure (max 1.2)
    if headings >= 3: score += 0.3
    paragraphs = len(re.findall(r'\n\n', body))
    if paragraphs >= 3: score += 0.3
    format_types = sum([headings > 0, table_rows > 0, list_items > 0, code_blocks > 0])
    if format_types >= 2: score += 0.3
    if format_types >= 3: score += 0.2

    # Normalize to 0-10 scale (raw max ~7.6)
    normalized = min(score / 7.6 * 10.0, 10.0)
    return (round(normalized, 2), notes)


# ================================================================
# LAYER 2: RUBRIC SCORER (builder quality gate, free, instant)
# ================================================================

def _find_quality_gate(kind: str) -> str | None:
    """Find the quality gate file for a given kind."""
    if not kind:
        return None
    # Try direct match: {kind}-builder/bld_quality_gate_{kind}.md
    slug = kind.replace("_", "-")
    gate_path = BUILDERS_DIR / f"{slug}-builder" / f"bld_quality_gate_{kind}.md"
    if gate_path.exists():
        return str(gate_path)
    # Fallback: search
    for p in BUILDERS_DIR.rglob(f"bld_quality_gate_{kind}.md"):
        return str(p)
    # Broader search
    kind_under = kind.replace("-", "_")
    for p in BUILDERS_DIR.rglob(f"bld_quality_gate_{kind_under}.md"):
        return str(p)
    return None


def _parse_soft_dimensions(gate_content: str) -> list[dict]:
    """Extract soft scoring dimensions from quality gate file."""
    dims = []
    for m in re.finditer(
        r'^\|\s*(S\d+)\s*\|\s*(.*?)\s*\|\s*([\d.]+)\s*\|',
        gate_content, re.MULTILINE
    ):
        dims.append({
            "id": m.group(1),
            "description": m.group(2).strip(),
            "weight": float(m.group(3)),
        })
    return dims


def _parse_hard_gates(gate_content: str) -> list[dict]:
    """Extract hard gates from quality gate file.

    Supports optional severity column: | H01 | check | fail_cond | CRITICAL |
    Severity levels: CRITICAL (blocks), HIGH (warns), MEDIUM (documents), LOW (ignored).
    If no severity column, defaults to HIGH.
    """
    gates = []
    for m in re.finditer(
        r'^\|\s*(H\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*(?:\|\s*(CRITICAL|HIGH|MEDIUM|LOW)\s*)?\|',
        gate_content, re.MULTILINE
    ):
        severity = m.group(4).upper() if m.group(4) else "HIGH"
        gates.append({
            "id": m.group(1),
            "check": m.group(2).strip(),
            "fail_condition": m.group(3).strip(),
            "severity": severity,
        })
    return gates


# Severity weights for scoring impact
SEVERITY_WEIGHTS = {
    "CRITICAL": 1.0,   # full impact -- blocks publish
    "HIGH": 0.7,       # strong impact -- warns
    "MEDIUM": 0.3,     # partial impact -- documents
    "LOW": 0.0,        # no scoring impact -- informational
}


def score_rubric(path: str) -> tuple[float, list[dict], list[str]]:
    """Score against builder's quality gate rubric.
    Returns (score 0-10, dimensions_with_scores, notes).
    """
    if not os.path.exists(path):
        return (0.0, [], ["MISSING"])

    content = open(path, 'r', encoding='utf-8').read()
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return (0.0, [], ["NO_FRONTMATTER"])

    fm = fm_match.group(1)
    body = content[fm_match.end():]
    notes = []

    # Extract kind
    kind_match = re.search(r'kind:\s*(\S+)', fm)
    kind = kind_match.group(1).strip().strip('"\'') if kind_match else None

    # Find quality gate
    gate_path = _find_quality_gate(kind)
    if not gate_path:
        # No rubric available -- return neutral score
        return (7.5, [], [f"no quality gate for kind={kind}"])

    gate_content = open(gate_path, 'r', encoding='utf-8').read()

    # Hard gates -- binary pass/fail
    hard_gates = _parse_hard_gates(gate_content)
    hard_pass = 0
    for gate in hard_gates:
        check = gate["check"].lower()
        passed = True
        # Programmatic checks for common hard gates
        if "frontmatter" in check and "yaml" in check:
            passed = fm_match is not None
        elif "id matches" in check or "id equals" in check:
            id_match = re.search(r'id:\s*(\S+)', fm)
            passed = id_match is not None
        elif "kind equals" in check:
            passed = kind is not None
        elif "quality field" in check:
            passed = "quality:" in fm
        elif "required fields" in check:
            passed = all(f in fm for f in ['id:', 'kind:', 'pillar:'])
        elif "density_score" in check and "range" in check:
            ds = re.search(r'density_score:\s*([\d.]+)', fm)
            if ds:
                passed = 0.0 <= float(ds.group(1)) <= 1.0
            else:
                passed = False
        elif "file size" in check:
            passed = len(content.encode('utf-8')) <= 10240  # generous 10KB
        elif "tldr" in check and "160" in check:
            tldr = re.search(r'tldr:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
            passed = tldr is not None and len(tldr.group(1)) <= 160
        elif "tldr" in check and "present" in check:
            tldr = re.search(r'tldr:\s*.+', fm)
            passed = tldr is not None and len(tldr.group(0)) > 10
        elif "tags" in check and ("list" in check or "present" in check):
            passed = bool(re.search(r'tags:\s*\[.+\]', fm))
        elif "version" in check:
            passed = bool(re.search(r'version:\s*\d+\.\d+', fm))
        elif "no placeholder" in check or "no todo" in check:
            bad = len(re.findall(r'(?i)\b(TODO|TBD|FIXME|insert here|add later)\b', body))
            passed = bad == 0
        elif "has example" in check or "example" in check:
            passed = bool(re.search(r'(?i)## (Example|Usage|Sample)', body))
        elif "has table" in check or "table" in check:
            passed = bool(re.search(r'^\|.*\|', body, re.MULTILINE))
        elif "code block" in check or "```" in check:
            passed = "```" in body
        elif "body length" in check or ("min" in check and "words" in check):
            words = len(body.split())
            passed = words >= 100
        elif "no filler" in check or "filler" in check:
            fillers = re.findall(r'(?i)\b(this document|in summary|it.?s worth noting|as mentioned)\b', body)
            passed = len(fillers) == 0
        else:
            passed = True

        severity = gate.get("severity", "HIGH")
        weight = SEVERITY_WEIGHTS.get(severity, 0.7)

        if passed:
            hard_pass += weight
        else:
            if severity == "CRITICAL":
                notes.append(f"BLOCK {gate['id']} [{severity}]: {gate['check'][:50]}")
            elif severity != "LOW":
                notes.append(f"FAIL {gate['id']} [{severity}]: {gate['check'][:50]}")

    max_weight = sum(SEVERITY_WEIGHTS.get(g.get("severity", "HIGH"), 0.7)
                     for g in hard_gates) or 1.0
    hard_ratio = hard_pass / max_weight

    # Soft dimensions -- pattern-based scoring
    soft_dims = _parse_soft_dimensions(gate_content)
    dim_scores = []
    total_weight = sum(d["weight"] for d in soft_dims) or 1.0

    for dim in soft_dims:
        desc = dim["description"].lower()
        dim_score = 5.0  # default: middling

        # Score each dimension by checking artifact content
        if "tldr" in desc:
            tldr = re.search(r'tldr:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
            if tldr and 30 <= len(tldr.group(1)) <= 160:
                dim_score = 9.0
            elif tldr:
                dim_score = 6.0
            else:
                dim_score = 2.0

        elif "tags" in desc:
            tags = re.search(r'tags:\s*\[(.*?)\]', fm)
            tag_count = len(tags.group(1).split(',')) if tags else 0
            dim_score = min(10, tag_count * 2.5)

        elif "density" in desc:
            ds = re.search(r'density_score:\s*([\d.]+)', fm)
            if ds:
                dim_score = float(ds.group(1)) * 10
            else:
                dim_score = 5.0

        elif "filler" in desc or "no padding" in desc or "placeholder" in desc:
            fillers = len(re.findall(
                r'(?i)\b(this document|in summary|it.?s worth noting|as mentioned|'
                r'can help with|in conclusion|TODO|TBD|FIXME)\b', body
            ))
            dim_score = max(0, 10 - fillers * 2)

        elif "source" in desc or "attribution" in desc:
            has_sources = bool(re.search(r'sources?:', fm)) or bool(re.search(r'## (References?|Sources?)', body))
            dim_score = 8.0 if has_sources else 3.0

        elif "structure" in desc or "section" in desc:
            headings = len(re.findall(r'^#{1,3} ', body, re.MULTILINE))
            dim_score = min(10, headings * 1.5)

        elif "domain" in desc or "specific" in desc:
            has_domain = bool(re.search(r'domain:\s*\S', fm))
            body_words = len(body.split())
            dim_score = 8.0 if (has_domain and body_words >= 200) else 5.0

        elif "factual" in desc or "concrete" in desc:
            # Check for numbers, specific values, technical terms
            numbers = len(re.findall(r'\b\d+(?:\.\d+)?(?:%|ms|KB|MB|GB|px|rem|em)?\b', body))
            dim_score = min(10, 4 + numbers * 0.5)

        elif "atomic" in desc or "one concept" in desc:
            headings = len(re.findall(r'^## ', body, re.MULTILINE))
            dim_score = 8.0 if headings <= 6 else 5.0

        elif "when to use" in desc or "not-when" in desc:
            has_when = bool(re.search(r'(?i)## When|## Use Case|## Not', body))
            dim_score = 8.0 if has_when else 3.0

        dim_scores.append({
            "id": dim["id"],
            "description": dim["description"][:80],
            "weight": dim["weight"],
            "score": round(dim_score, 1),
        })

    # Weighted soft score
    if dim_scores:
        weighted = sum(d["score"] * d["weight"] for d in dim_scores) / total_weight
    else:
        weighted = 7.5

    # Combine: 60% soft dims + 40% hard gates
    rubric_score = (weighted * 0.6) + (hard_ratio * 10 * 0.4)
    rubric_score = round(min(rubric_score, 10.0), 2)

    return (rubric_score, dim_scores, notes)


# ================================================================
# LAYER 3: SEMANTIC SCORER (LLM-based, 1 call per artifact)
# ================================================================

def score_semantic(path: str, structural: float, rubric_dims: list[dict]) -> tuple[float, dict, str]:
    """LLM-based semantic scoring via execute_prompt().
    Returns (score 0-10, dimension_scores, reason).
    """
    content = open(path, 'r', encoding='utf-8').read()
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    fm = fm_match.group(1) if fm_match else ""
    kind_match = re.search(r'kind:\s*(\S+)', fm)
    kind = kind_match.group(1).strip().strip('"\'') if kind_match else "unknown"

    # Build dimension list for LLM
    dim_list = ""
    if rubric_dims:
        dim_list = "\n".join(
            f"  {d['id']}: {d['description']} (heuristic={d['score']}/10)"
            for d in rubric_dims
        )
    else:
        dim_list = """  S01: Factual concreteness -- specific values, numbers, verifiable facts
  S02: Atomicity -- covers one concept without scope creep
  S03: Searchability -- tags and tldr enable retrieval
  S04: Actionability -- reader knows what to DO after reading
  S05: Density -- no filler, no padding, every sentence earns its place
  S06: Domain expertise -- shows deep knowledge, not surface-level"""

    prompt = f"""You are a quality reviewer scoring a knowledge artifact (kind: {kind}).

## Artifact
```markdown
{content[:3000]}
```

## Dimensions to score (0-10 each)
{dim_list}

## Additional dimensions (always score these)
  ACTIONABILITY: Reader can immediately act on the content
  INSIGHT_DEPTH: Contains non-obvious insights, not just definitions
  COMPLETENESS: Covers the topic adequately for its scope

## Instructions
Score each dimension 0-10. Be STRICT:
- 10 = exceptional, publishable in a technical reference
- 8 = solid, useful, minor improvements possible  
- 6 = adequate but generic, could be better
- 4 = thin, mostly filler or surface-level
- 2 = poor, largely unhelpful

Return ONLY valid JSON (no markdown, no explanation):
{{
  "dimensions": {{
    "ACTIONABILITY": 7,
    "INSIGHT_DEPTH": 6,
    "COMPLETENESS": 8,
    ...
  }},
  "overall": 7.5,
  "weakest": "INSIGHT_DEPTH",
  "suggestion": "one specific improvement that would raise the weakest dimension"
}}"""

    try:
        # Import execute_prompt from cex_intent
        sys.path.insert(0, str(ROOT / "_tools"))
        from cex_intent import execute_prompt
        response = execute_prompt(prompt)

        # Parse JSON from response
        # Try to find JSON in the response
        json_match = re.search(r'\{[\s\S]*\}', response)
        if json_match:
            data = json.loads(json_match.group())
            overall = float(data.get("overall", 7.0))
            dims = data.get("dimensions", {})
            weakest = data.get("weakest", "")
            suggestion = data.get("suggestion", "")
            reason = f"weakest={weakest}: {suggestion}" if weakest else ""
            return (round(overall, 1), dims, reason)
        else:
            return (7.0, {}, f"LLM response not JSON: {response[:100]}")

    except Exception as e:
        return (7.0, {}, f"semantic error: {str(e)[:100]}")


# ================================================================
# CACHE -- by content hash (GDP D03)
# ================================================================

def _content_hash(path: str) -> str:
    """SHA256 of file content."""
    content = open(path, 'rb').read()
    return hashlib.sha256(content).hexdigest()[:16]


def _load_cache() -> dict:
    """Load score cache from disk."""
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding='utf-8'))
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def _save_cache(cache: dict):
    """Save score cache to disk."""
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(json.dumps(cache, indent=2), encoding='utf-8')


# ================================================================
# HYBRID SCORER -- combines all 3 layers
# ================================================================

def score_hybrid(path: str, use_cache: bool = True, force_semantic: bool = False,
                 verbose: bool = False) -> dict:
    """
    3-layer hybrid scoring. Returns dict with full breakdown.

    Returns:
        {
            "score": 8.7,           # final weighted score
            "structural": 8.5,      # layer 1
            "rubric": 8.2,          # layer 2
            "semantic": 9.0,        # layer 3 (None if skipped)
            "dimensions": {...},    # per-dimension breakdown
            "weakest": "...",       # weakest dimension
            "suggestion": "...",    # how to improve weakest
            "mode": "hybrid",       # "structural_only" | "hybrid" | "full"
            "cached": False,
            "notes": [...]
        }
    """
    path = str(path)
    if not os.path.exists(path):
        return {"score": 0.0, "structural": 0, "rubric": 0, "semantic": None,
                "dimensions": {}, "weakest": "", "suggestion": "",
                "mode": "error", "cached": False, "notes": ["MISSING"]}

    # Check cache
    if use_cache:
        cache = _load_cache()
        h = _content_hash(path)
        cache_key = f"{path}:{h}"
        if cache_key in cache:
            cached = cache[cache_key]
            cached["cached"] = True
            if verbose:
                print(f"  [CACHE] {Path(path).name}: {cached['score']}")
            return cached

    # Layer 1: Structural (always)
    struct_raw, struct_notes = score_structural(path)
    structural = round(struct_raw, 2)

    if verbose:
        print(f"  [L1] structural: {structural}")

    # Layer 2: Rubric (always)
    rubric_raw, rubric_dims, rubric_notes = score_rubric(path)
    rubric = round(rubric_raw, 2)

    if verbose:
        print(f"  [L2] rubric: {rubric} ({len(rubric_dims)} dims)")

    all_notes = struct_notes + rubric_notes

    # Layer 3: Semantic (only if structural+rubric avg >= 8.5 OR forced)
    # Token optimization: check cache for same-kind scored artifacts first.
    # If a cached artifact of the same kind scored 9.0+, and L1+L2 are also
    # strong (>= 8.8), skip the LLM call and inherit the cached semantic score.
    avg_12 = (structural + rubric) / 2
    semantic = None
    sem_dims = {}
    weakest = ""
    suggestion = ""

    if force_semantic or avg_12 >= 8.5:
        # Cache hit only if exact content hash matches (no kind-inheritance)
        skip_llm = False
        if not force_semantic and use_cache:
            cache = _load_cache()
            h = _content_hash(path)
            cache_key = f"{path}:{h}"
            if cache_key in cache and cache[cache_key].get("semantic") is not None:
                semantic_raw = cache[cache_key]["semantic"]
                sem_dims = cache[cache_key].get("dimensions", {})
                reason = "exact content-hash cache hit"
                skip_llm = True
                if verbose:
                    print(f"  [L3] semantic: CACHED (exact hash match)")

        if not skip_llm:
            if verbose:
                print(f"  [L3] semantic: calling LLM (avg_12={avg_12:.1f})...")
            semantic_raw, sem_dims, reason = score_semantic(path, structural, rubric_dims)
        semantic = round(semantic_raw, 2)

        if verbose:
            print(f"  [L3] semantic: {semantic} ({reason[:60]})")

        # Extract weakest dimension
        if sem_dims:
            weakest_dim = min(sem_dims.items(), key=lambda x: x[1] if isinstance(x[1], (int, float)) else 10)
            weakest = weakest_dim[0]
        if "weakest=" in reason:
            parts = reason.split("weakest=", 1)
            if len(parts) > 1:
                wr = parts[1]
                if ":" in wr:
                    weakest = wr.split(":")[0].strip()
                    suggestion = wr.split(":", 1)[1].strip()

        # Weighted blend: 30% structural + 30% rubric + 40% semantic
        final = structural * 0.3 + rubric * 0.3 + semantic * 0.4
        mode = "full"
    else:
        # No semantic layer -- blend structural + rubric only
        final = structural * 0.5 + rubric * 0.5
        mode = "structural_only" if not rubric_dims else "hybrid"
        if verbose:
            print(f"  [L3] semantic: SKIPPED (avg_12={avg_12:.1f} < 8.5)")

    final = round(min(final, 10.0), 1)

    # Merge dimension info
    dimensions = {}
    for d in rubric_dims:
        dimensions[d["id"]] = {"description": d["description"], "heuristic": d["score"]}
    for k, v in sem_dims.items():
        if k in dimensions:
            dimensions[k]["semantic"] = v
        else:
            dimensions[k] = {"description": k, "semantic": v}

    result = {
        "score": final,
        "structural": structural,
        "rubric": rubric,
        "semantic": semantic,
        "dimensions": dimensions,
        "weakest": weakest,
        "suggestion": suggestion,
        "mode": mode,
        "cached": False,
        "notes": all_notes,
    }

    # Save to cache
    if use_cache:
        cache = _load_cache()
        h = _content_hash(path)
        cache[f"{path}:{h}"] = result
        _save_cache(cache)

    return result


# ================================================================
# BACKWARD COMPAT -- score_artifact() still works everywhere
# ================================================================

def score_artifact(path, hybrid: bool = False) -> tuple[float, str]:
    """Score a single artifact. Returns (score, notes).

    If hybrid=True, uses 3-layer scoring with LLM.
    If hybrid=False (default), uses fast structural-only scoring.
    This keeps backward compatibility with all existing callers.
    """
    if hybrid:
        result = score_hybrid(str(path))
        notes = "; ".join(result["notes"]) if result["notes"] else "OK"
        if result["weakest"]:
            notes += f" | weakest={result['weakest']}"
        if result["suggestion"]:
            notes += f" | fix={result['suggestion'][:80]}"
        return (result["score"], notes)
    else:
        # Fast structural-only path (original behavior)
        raw, notes = score_structural(str(path))
        if "MISSING" in notes:
            return (0.0, "MISSING")
        if "NO_FRONTMATTER" in notes:
            return (round(raw * 0.5, 1), "no frontmatter")
        score = round(raw, 1)
        return (score, "; ".join(notes) if notes else "OK")


def update_quality(path, score):
    """Replace quality: null or quality: X.X with quality: Y.Y in file."""
    content = open(path, 'r', encoding='utf-8').read()
    # Update both null and numeric quality values
    updated = re.sub(
        r'^quality:\s*(?:null|[\d.]+)\s*$',
        f'quality: {score}',
        content, count=1, flags=re.MULTILINE
    )
    if updated != content:
        open(path, 'w', encoding='utf-8').write(updated)
        return True
    return False


# ================================================================
# CLI
# ================================================================

def main():
    import argparse
    parser = argparse.ArgumentParser(description='CEX Hybrid Scorer')
    parser.add_argument('--dry-run', action='store_true', help='Score but do not update files')
    parser.add_argument('--apply', action='store_true', help='Apply scores to files')
    parser.add_argument('--hybrid', action='store_true', help='Use 3-layer hybrid scoring (includes LLM)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show scoring details')
    parser.add_argument('--no-cache', action='store_true', help='Skip score cache')
    parser.add_argument('--nucleus', type=str, help='Score only artifacts in N0X_*/ directory (e.g. n01)')
    parser.add_argument('--null-only', action='store_true', help='Skip artifacts that already have quality != null')
    parser.add_argument('--apply-null-only', action='store_true', help='Shorthand for --apply --null-only')
    parser.add_argument('files', nargs='*', help='Files to score (default: all N0* artifacts)')
    args = parser.parse_args()

    if args.apply_null_only:
        args.apply = True
        args.null_only = True

    # Restrict to specific nucleus directory if --nucleus given
    if args.nucleus and not args.files:
        nuc = args.nucleus.lower().replace('n', 'n0') if not args.nucleus.lower().startswith('n0') else args.nucleus.lower()
        nuc_num = nuc.replace('n', '').replace('0', '', 1) if len(nuc) == 3 else nuc[-1]
        nuc_dirs = [d for d in os.listdir('.') if d.lower().startswith(f'n0{nuc_num}') and os.path.isdir(d)]
        if not nuc_dirs:
            print(f"No directory found for nucleus {args.nucleus}")
            return
        args.files = []
        for nd in nuc_dirs:
            for root_dir, _dirs, fnames in os.walk(nd):
                for fn in fnames:
                    if fn.endswith('.md'):
                        fpath = os.path.join(root_dir, fn)
                        try:
                            head = open(fpath, 'r', encoding='utf-8').read(2000)
                            if 'quality:' in head:
                                args.files.append(fpath)
                        except (OSError, UnicodeDecodeError):
                            pass
        args.files.sort()

    # Find files if none specified
    if not args.files:
        import subprocess
        targets = [d for d in os.listdir('.') if d.startswith('N0') and os.path.isdir(d)]
        if not targets:
            print("No nucleus directories found.")
            return
        result = subprocess.run(
            ['grep', '-r', '-l', r'^quality:', '--include=*.md'] + targets,
            capture_output=True, text=True
        )
        args.files = sorted(set(result.stdout.strip().split('\n'))) if result.stdout.strip() else []

    # Filter to null-only if requested (frontmatter only)
    if args.null_only and args.files:
        filtered = []
        for f in args.files:
            try:
                content = open(f, 'r', encoding='utf-8').read()
                fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
                if fm_match:
                    fm = fm_match.group(1)
                    if re.search(r'^quality:\s*null\s*$', fm, re.MULTILINE):
                        filtered.append(f)
            except (OSError, UnicodeDecodeError):
                pass
        args.files = filtered

    if not args.files:
        print("No artifacts found.")
        return

    if args.hybrid:
        # Hybrid mode -- full 3-layer scoring
        print(f"{'Score':>5} | {'Str':>4} | {'Rub':>4} | {'Sem':>4} | {'Mode':<10} | {'Weakest':<20} | Path")
        print("-" * 110)

        scores = {}
        for f in args.files:
            f = f.strip()
            if not f:
                continue
            result = score_hybrid(f, use_cache=not args.no_cache, verbose=args.verbose)
            scores[f] = result
            sem_str = f"{result['semantic']:.1f}" if result['semantic'] else "skip"
            print(f"{result['score']:5.1f} | {result['structural']:4.1f} | {result['rubric']:4.1f} | "
                  f"{sem_str:>4} | {result['mode']:<10} | {result['weakest'][:20]:<20} | {f}")

            if args.apply:
                update_quality(f, result['score'])

        print(f"\n{'='*110}")
        all_scores = [r['score'] for r in scores.values()]
        print(f"Total: {len(scores)} artifacts")
        print(f"Avg: {sum(all_scores)/len(all_scores):.2f}")
        print(f"9.0+: {sum(1 for s in all_scores if s >= 9.0)}")
        print(f"8.5-8.9: {sum(1 for s in all_scores if 8.5 <= s < 9.0)}")
        print(f"<8.5: {sum(1 for s in all_scores if s < 8.5)}")

    else:
        # Classic mode -- structural only (fast)
        print(f"{'Score':>5} | {'Size':>6} | {'Notes':<40} | Path")
        print("-" * 100)

        scores = {}
        for f in args.files:
            f = f.strip()
            if not f:
                continue
            score, notes = score_artifact(f)
            scores[f] = score
            size = os.path.getsize(f) if os.path.exists(f) else 0
            print(f"{score:5.1f} | {size:5d}B | {notes:<40} | {f}")

        if not scores:
            return

        print(f"\n{'='*100}")
        print(f"Total: {len(scores)} artifacts")
        print(f"Avg score: {sum(scores.values())/len(scores):.1f}")
        print(f"Min: {min(scores.values()):.1f} | Max: {max(scores.values()):.1f}")
        print(f"9.0+: {sum(1 for s in scores.values() if s >= 9.0)}")
        print(f"8.5-8.9: {sum(1 for s in scores.values() if 8.5 <= s < 9.0)}")

        if args.apply:
            updated = 0
            for f, score in scores.items():
                if update_quality(f, score):
                    updated += 1
            print(f"\nApplied scores to {updated}/{len(scores)} files.")


if __name__ == '__main__':
    main()
