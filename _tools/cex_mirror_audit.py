#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
cex_mirror_audit.py -- Fractal mirror enforcement (HERMES W4.6)

Audits nucleus-specific mirror artifacts against N00 archetype templates.
Detects orphans (no N00 archetype), forbidden-field drift, missing mirrors,
and reports promotion candidates.

N00 is authoritative. Mirrors may override ONLY:
  tone, voice, required_fields, quality_threshold, density_target,
  sin_lens, example_corpus

Mirrors MAY NOT override:
  kind_name, pillar, frontmatter_schema, 8F_hooks

Usage:
    python _tools/cex_mirror_audit.py --check
    python _tools/cex_mirror_audit.py --list <kind>
    python _tools/cex_mirror_audit.py --diff <kind> <n0X>
    python _tools/cex_mirror_audit.py --promote <kind>
    python _tools/cex_mirror_audit.py --coverage
    python _tools/cex_mirror_audit.py --check --json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_REPO = Path(__file__).resolve().parent.parent
_N00_DIR = _REPO / "N00_genesis"
_BUILDERS_DIR = _REPO / "archetypes" / "builders"
_KINDS_META = _REPO / ".cex" / "kinds_meta.json"
_HANDOFFS_DIR = _REPO / ".cex" / "runtime" / "handoffs"

# ---------------------------------------------------------------------------
# Policy
# ---------------------------------------------------------------------------
# Kinds exempt from orphan check: internal audit/review artifacts with no builder
ORPHAN_EXEMPT_KINDS = frozenset({
    "audit_report", "audit",
})

OVERRIDABLE = frozenset({
    "tone", "voice", "required_fields", "quality_threshold",
    "density_target", "sin_lens", "example_corpus",
})
FORBIDDEN = frozenset({
    "kind_name", "pillar", "frontmatter_schema", "8f_hooks",
})

# ---------------------------------------------------------------------------
# Frontmatter parser (stdlib-only, flat YAML)
# ---------------------------------------------------------------------------

def _parse_frontmatter(path: Path) -> Dict[str, Any]:
    """Extract YAML frontmatter block (--- ... ---) as flat dict."""
    try:
        text = path.read_text(encoding="ascii", errors="replace")
    except OSError:
        return {}
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.DOTALL)
    if not m:
        return {}
    return _parse_yaml_flat(m.group(1))


def _parse_yaml_flat(text: str) -> Dict[str, Any]:
    """Parse flat (top-level keys only) YAML into a dict."""
    result: Dict[str, Any] = {}
    for line in text.splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        indent = len(line) - len(line.lstrip())
        if indent > 0:
            continue  # skip nested lines
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key and key[0].isalpha() or (key and key[0] == "_"):
            result[key] = _cast(val)
    return result


def _cast(v: str) -> Any:
    if v.lower() in ("true", "yes"):
        return True
    if v.lower() in ("false", "no"):
        return False
    if v.lower() in ("null", "~", ""):
        return None
    try:
        return int(v)
    except ValueError:
        pass
    try:
        return float(v)
    except ValueError:
        pass
    return v

# ---------------------------------------------------------------------------
# Discovery helpers
# ---------------------------------------------------------------------------

_MIRROR_RE = re.compile(r"_n0([1-7])\.md$", re.IGNORECASE)
_PREFIX_RE = re.compile(r"^(?:kno|tpl|pro|mkr|ops|adm|eng|act|scm|cfg|mem|fbk|orch)_")


def _nucleus_dirs() -> Dict[str, Path]:
    out: Dict[str, Path] = {}
    for d in sorted(_REPO.iterdir()):
        m = re.match(r"^N0([1-7])_", d.name)
        if m and d.is_dir():
            out[f"n0{m.group(1)}"] = d
    return out


def _kind_from_filename(name: str) -> str:
    base = _MIRROR_RE.sub("", name)
    base = _PREFIX_RE.sub("", base)
    return base


def _find_all_mirrors() -> List[Tuple[str, str, Path]]:
    """Return [(nucleus_id, kind, path), ...] for all *_n0[1-7].md files."""
    results: List[Tuple[str, str, Path]] = []
    for nuc_id, nuc_dir in _nucleus_dirs().items():
        for fpath in sorted(nuc_dir.rglob("*.md")):
            if not _MIRROR_RE.search(fpath.name):
                continue
            fm = _parse_frontmatter(fpath)
            kind = str(fm.get("kind") or _kind_from_filename(fpath.name))
            results.append((nuc_id, kind, fpath))
    return results


def _n00_tpl_for_kind(kind: str, pillar: str = "") -> Optional[Path]:
    """Return path to N00 archetype template, or None.

    Search order:
    1. N00_genesis/{pillar}/tpl_{kind}.md (exact pillar match)
    2. N00_genesis/**/tpl_{kind}.md (any N00 subdir)
    3. archetypes/builders/{kind}-builder/ (pre-HERMES canonical archetype)
    """
    if pillar:
        p = _N00_DIR / pillar / f"tpl_{kind}.md"
        if p.exists():
            return p
    for candidate in _N00_DIR.rglob(f"tpl_{kind}.md"):
        return candidate
    # Fallback: pre-HERMES builders are canonical archetypes too
    kind_dash = kind.replace("_", "-")
    builder_dir = _BUILDERS_DIR / f"{kind_dash}-builder"
    if builder_dir.is_dir():
        for stem in (f"bld_model_{kind}", f"bld_prompt_{kind}"):
            p = builder_dir / f"{stem}.md"
            if p.exists():
                return p
        # Any .md in builder dir suffices as archetype marker
        for p in sorted(builder_dir.glob("*.md")):
            return p
    return None


def _load_kinds_meta() -> Dict[str, Any]:
    if not _KINDS_META.exists():
        return {}
    try:
        return json.loads(_KINDS_META.read_text(encoding="ascii", errors="replace"))
    except (json.JSONDecodeError, OSError):
        return {}


def _scan_dispatched() -> List[Tuple[str, str]]:
    """Return [(kind, nucleus), ...] found in handoff files."""
    pairs: List[Tuple[str, str]] = []
    if not _HANDOFFS_DIR.exists():
        return pairs
    kind_re = re.compile(r"kind[=:]\s*['\"]?([a-z_]+)['\"]?", re.IGNORECASE)
    nuc_re = re.compile(r"nucleus[=:]\s*['\"]?(n0[1-7])['\"]?", re.IGNORECASE)
    for fpath in sorted(_HANDOFFS_DIR.rglob("*.md")):
        try:
            text = fpath.read_text(encoding="ascii", errors="replace")
        except OSError:
            continue
        kinds = kind_re.findall(text)
        nucs = nuc_re.findall(text)
        for k in kinds:
            for n in nucs:
                pairs.append((k, n.lower()))
    return pairs

# ---------------------------------------------------------------------------
# Command: --check
# ---------------------------------------------------------------------------

def cmd_check(emit_json: bool) -> int:
    mirrors = _find_all_mirrors()
    dispatched = _scan_dispatched()
    existing_pairs = {(nuc, kind) for nuc, kind, _ in mirrors}

    orphans: List[Dict[str, Any]] = []
    drift_issues: List[Dict[str, Any]] = []
    missing: List[Dict[str, Any]] = []
    promotion_candidates: List[Dict[str, Any]] = []

    # Check each mirror
    for nuc_id, kind, path in mirrors:
        fm = _parse_frontmatter(path)
        pillar = str(fm.get("pillar", ""))
        if not pillar:
            m = re.search(r"[/\\](P\d{2})[/\\]", str(path))
            pillar = m.group(1) if m else ""

        n00_path = _n00_tpl_for_kind(kind, pillar)
        if n00_path is None:
            if kind in ORPHAN_EXEMPT_KINDS:
                continue  # internal audit kind, not a fractal mirror
            orphans.append({
                "kind": kind,
                "nucleus": nuc_id,
                "mirror_path": str(path.relative_to(_REPO)),
                "reason": "no N00 archetype",
            })
            continue

        n00_fm = _parse_frontmatter(n00_path)

        # Forbidden field drift
        for field in FORBIDDEN:
            mv = fm.get(field)
            nv = n00_fm.get(field)
            if mv is not None and mv != nv:
                drift_issues.append({
                    "kind": kind,
                    "nucleus": nuc_id,
                    "mirror_path": str(path.relative_to(_REPO)),
                    "field": field,
                    "mirror_value": mv,
                    "n00_value": nv,
                })

        # Promotion candidate: mirror quality > N00
        try:
            mq = float(fm.get("quality") or 0)
            nq = float(n00_fm.get("quality") or 0)
        except (TypeError, ValueError):
            mq, nq = 0.0, 0.0
        override_fields = [f for f in OVERRIDABLE if fm.get(f) != n00_fm.get(f) and f in fm]
        if mq > nq and override_fields:
            promotion_candidates.append({
                "kind": kind,
                "from": nuc_id,
                "delta_fields": override_fields,
            })

    # Missing: dispatched but no mirror
    dispatch_counts: Dict[Tuple[str, str], int] = {}
    for k, n in dispatched:
        dispatch_counts[(k, n)] = dispatch_counts.get((k, n), 0) + 1
    for (kind, nuc_id), count in dispatch_counts.items():
        if (nuc_id, kind) not in existing_pairs:
            missing.append({
                "kind": kind,
                "nucleus": nuc_id,
                "reason": f"no mirror, but dispatched {count}x",
            })

    report = {
        "orphans": orphans,
        "drift": drift_issues,
        "missing": missing,
        "coverage_pct_by_nucleus": {},
        "promotion_candidates": promotion_candidates,
    }

    if emit_json:
        print(json.dumps(report, indent=2))
    else:
        _print_check_report(report, len(mirrors))

    return 1 if (orphans or drift_issues) else 0


def _print_check_report(report: Dict[str, Any], total_mirrors: int) -> None:
    orphans = report["orphans"]
    drift = report["drift"]
    missing = report["missing"]
    promos = report["promotion_candidates"]

    print("=== Mirror Audit Report ===")
    print(f"Total mirrors scanned: {total_mirrors}")
    print(f"Orphans:              {len(orphans)}  [FAIL if > 0]")
    print(f"Drift (forbidden):    {len(drift)}   [FAIL if > 0]")
    print(f"Missing mirrors:      {len(missing)}  [WARN]")
    print(f"Promotion candidates: {len(promos)}")
    print()

    if orphans:
        print("ORPHAN MIRRORS (no N00 archetype):")
        for o in orphans:
            print(f"  [FAIL] {o['nucleus']}/{o['kind']}  {o['mirror_path']}")
        print()

    if drift:
        print("DRIFT -- forbidden field overrides:")
        for d in drift:
            print(f"  [FAIL] {d['nucleus']}/{d['kind']}  field={d['field']}"
                  f"  mirror={d['mirror_value']!r}  n00={d['n00_value']!r}")
        print()

    if missing:
        print("MISSING MIRRORS (dispatched but no mirror exists):")
        for item in missing:
            print(f"  [WARN] {item['nucleus']}/{item['kind']}  {item['reason']}")
        print()

    if promos:
        print("PROMOTION CANDIDATES (mirror quality > N00):")
        for p in promos:
            print(f"  [INFO] {p['from']}/{p['kind']}  delta={p['delta_fields']}")
        print()

    issues = len(orphans) + len(drift)
    if issues == 0:
        print("[OK] No blocking issues found.")
    else:
        print(f"[FAIL] {issues} issue(s). Run --diff to inspect, --promote to fix.")

# ---------------------------------------------------------------------------
# Command: --list
# ---------------------------------------------------------------------------

def cmd_list(kind: str) -> int:
    mirrors = _find_all_mirrors()
    matches = [(nuc, path) for nuc, k, path in mirrors if k == kind]
    if not matches:
        print(f"No mirrors found for kind={kind!r}")
        return 0
    print(f"Mirrors for kind={kind!r}:")
    for nuc, path in sorted(matches):
        fm = _parse_frontmatter(path)
        q = fm.get("quality", "null")
        pillar = fm.get("pillar", "?")
        print(f"  {nuc}  {pillar}  quality={q}  {path.relative_to(_REPO)}")
    return 0

# ---------------------------------------------------------------------------
# Command: --diff
# ---------------------------------------------------------------------------

def cmd_diff(kind: str, nucleus: str) -> int:
    nuc_id = nucleus.lower()
    mirrors = _find_all_mirrors()
    match_path = next((p for n, k, p in mirrors if k == kind and n == nuc_id), None)
    if match_path is None:
        print(f"[FAIL] No mirror found for kind={kind!r} nucleus={nuc_id!r}")
        return 1

    mirror_fm = _parse_frontmatter(match_path)
    pillar = str(mirror_fm.get("pillar", ""))
    if not pillar:
        m = re.search(r"[/\\](P\d{2})[/\\]", str(match_path))
        pillar = m.group(1) if m else ""

    n00_path = _n00_tpl_for_kind(kind, pillar)
    if n00_path is None:
        print(f"[FAIL] No N00 archetype found for kind={kind!r}")
        return 1

    n00_fm = _parse_frontmatter(n00_path)
    all_keys = sorted(set(mirror_fm) | set(n00_fm))
    deltas = [
        (k, mirror_fm.get(k), n00_fm.get(k))
        for k in all_keys
        if mirror_fm.get(k) != n00_fm.get(k)
    ]
    if not deltas:
        print(f"[OK] No delta: {nuc_id}/{kind} matches N00 archetype.")
        return 0

    print(f"Diff: {nuc_id}/{kind}  vs  {n00_path.relative_to(_REPO)}")
    print(f"{'Field':<28} {'Status':<12} {'N00':<28} {'Mirror':<28}")
    print("-" * 96)
    for key, mv, nv in deltas:
        if key in FORBIDDEN:
            status = "FORBIDDEN"
            flag = "[FAIL]"
        elif key in OVERRIDABLE:
            status = "ALLOWED"
            flag = "[OK]  "
        else:
            status = "NEUTRAL"
            flag = "      "
        print(f"{flag} {key:<22} {status:<12} {str(nv):<28} {str(mv):<28}")
    return 0

# ---------------------------------------------------------------------------
# Command: --promote
# ---------------------------------------------------------------------------

def cmd_promote(kind: str) -> int:
    mirrors = _find_all_mirrors()
    matches = [(nuc, path) for nuc, k, path in mirrors if k == kind]
    if not matches:
        print(f"[FAIL] No mirrors found for kind={kind!r}")
        return 1

    # Pick highest-quality mirror
    best_nuc: Optional[str] = None
    best_quality = -1.0
    best_path: Optional[Path] = None
    for nuc, path in matches:
        fm = _parse_frontmatter(path)
        try:
            q = float(fm.get("quality") or 0)
        except (TypeError, ValueError):
            q = 0.0
        if q > best_quality:
            best_quality, best_nuc, best_path = q, nuc, path

    if best_path is None:
        print(f"[FAIL] Could not score mirrors for kind={kind!r}")
        return 1

    best_fm = _parse_frontmatter(best_path)
    pillar = str(best_fm.get("pillar", ""))
    if not pillar:
        m = re.search(r"[/\\](P\d{2})[/\\]", str(best_path))
        pillar = m.group(1) if m else ""

    n00_path = _n00_tpl_for_kind(kind, pillar)
    if n00_path is None:
        print(f"[FAIL] No N00 archetype for kind={kind!r}")
        return 1

    n00_fm = _parse_frontmatter(n00_path)
    try:
        n00_quality = float(n00_fm.get("quality") or 0)
    except (TypeError, ValueError):
        n00_quality = 0.0

    if best_quality <= n00_quality:
        print(f"[OK] N00 quality ({n00_quality}) >= best mirror ({best_quality}). No promotion.")
        return 0

    to_promote = {
        f: best_fm[f]
        for f in OVERRIDABLE
        if f in best_fm and best_fm.get(f) != n00_fm.get(f)
    }
    if not to_promote:
        print(f"[OK] No overridable deltas to promote from {best_nuc}/{kind}.")
        return 0

    text = n00_path.read_text(encoding="ascii", errors="replace")
    text = _bump_patch_version(text)
    text = _inject_annotation(text, best_nuc, list(to_promote.keys()))
    for field, val in to_promote.items():
        text = _set_field(text, field, val)
    n00_path.write_text(text, encoding="ascii", errors="replace")

    print(f"[OK] Promoted {len(to_promote)} field(s) from {best_nuc} to N00/{kind}")
    for k, v in to_promote.items():
        print(f"  {k}: {v!r}")
    print(f"Updated: {n00_path.relative_to(_REPO)}")

    # Redundancy check for remaining mirrors
    updated_n00 = _parse_frontmatter(n00_path)
    for nuc, path in matches:
        if nuc == best_nuc:
            continue
        fm = _parse_frontmatter(path)
        redundant = all(
            fm.get(f) == updated_n00.get(f)
            for f in OVERRIDABLE
            if f in fm
        )
        if redundant:
            print(f"  [INFO] {nuc}/{kind} may now be redundant")
    return 0


def _bump_patch_version(text: str) -> str:
    def _inc(m: re.Match) -> str:
        parts = m.group(1).split(".")
        if len(parts) == 3:
            try:
                parts[2] = str(int(parts[2]) + 1)
                return f'version: "{".".join(parts)}"'
            except ValueError:
                pass
        return m.group(0)
    return re.sub(r'version:\s*"([0-9][^"]*)"', _inc, text)


def _inject_annotation(text: str, nuc: str, fields: List[str]) -> str:
    annotation = (
        f'promoted_from: "{nuc}"\n'
        f'promoted_fields: [{", ".join(fields)}]\n'
    )
    return re.sub(r"(^---\r?\n)", r"\g<1>" + annotation, text, count=1)


def _set_field(text: str, field: str, value: Any) -> str:
    rep = f'{field}: "{value}"' if isinstance(value, str) else f"{field}: {value}"
    pattern = re.compile(rf"^{re.escape(field)}:.*$", re.MULTILINE)
    if pattern.search(text):
        return pattern.sub(rep, text, count=1)
    # Insert before closing ---
    return re.sub(r"(\n---\n)", f"\n{rep}\\1", text, count=1)

# ---------------------------------------------------------------------------
# Command: --coverage
# ---------------------------------------------------------------------------

def cmd_coverage(emit_json: bool) -> int:
    kinds_meta = _load_kinds_meta()
    all_kinds = sorted(kinds_meta.keys())
    nuclei = [f"n0{i}" for i in range(1, 8)]

    mirrors = _find_all_mirrors()
    covered = {(nuc, kind) for nuc, kind, _ in mirrors}

    cov_by_nuc: Dict[str, float] = {}
    for nuc in nuclei:
        n = sum(1 for k in all_kinds if (nuc, k) in covered)
        cov_by_nuc[nuc] = round(n / len(all_kinds), 4) if all_kinds else 0.0

    report = {
        "total_kinds": len(all_kinds),
        "total_mirrors": len(mirrors),
        "coverage_pct_by_nucleus": cov_by_nuc,
    }

    if emit_json:
        print(json.dumps(report, indent=2))
    else:
        print("=== Mirror Coverage ===")
        print(f"Total kinds registered: {len(all_kinds)}")
        print(f"Total mirror files:     {len(mirrors)}")
        print()
        print(f"{'Nucleus':<10} {'Mirrors':<10} {'Coverage'}")
        print("-" * 35)
        for nuc in nuclei:
            n = sum(1 for k in all_kinds if (nuc, k) in covered)
            pct = cov_by_nuc[nuc] * 100
            print(f"{nuc:<10} {n:<10} {pct:.1f}%")
    return 0

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="cex_mirror_audit.py",
        description="Fractal mirror enforcement -- HERMES W4.6",
    )
    p.add_argument("--check", action="store_true",
                   help="Scan orphans + drift (exit 1 if issues)")
    p.add_argument("--list", metavar="KIND",
                   help="List all mirrors of a kind")
    p.add_argument("--dif", nargs=2, metavar=("KIND", "NUCLEUS"),
                   help="Show override delta between mirror and N00")
    p.add_argument("--promote", metavar="KIND",
                   help="Back-port best mirror delta into N00 tpl")
    p.add_argument("--coverage", action="store_true",
                   help="Coverage matrix: kinds x nuclei")
    p.add_argument("--json", action="store_true",
                   help="Emit JSON to stdout (--check and --coverage)")
    return p


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    emit_json = args.json

    if args.check:
        return cmd_check(emit_json)
    if args.list:
        return cmd_list(args.list)
    if args.diff:
        return cmd_diff(args.diff[0], args.diff[1])
    if args.promote:
        return cmd_promote(args.promote)
    if args.coverage:
        return cmd_coverage(emit_json)

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
