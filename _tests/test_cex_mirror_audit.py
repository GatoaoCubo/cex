# -*- coding: ascii -*-
"""
Tests for cex_mirror_audit.py -- HERMES W4.6

Cases:
1. Orphan detection: mirror exists but N00 archetype is missing
2. Drift detection: mirror overrides a forbidden field
3. Missing mirror detection: dispatched kind/nucleus with no mirror file
4. Promotion candidate: mirror quality > N00 with overridable delta
5. Clean state: no orphans, no drift, no forbidden overrides
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


# ---------------------------------------------------------------------------
# Test harness: isolated temp directory tree
# ---------------------------------------------------------------------------

def _make_repo(tmp: Path) -> Path:
    """Create a minimal fake CEX repo structure under tmp."""
    (tmp / "N00_genesis" / "P01" ).mkdir(parents=True)
    (tmp / "N00_genesis" / "P02" ).mkdir(parents=True)
    (tmp / "N01_intelligence" / "P01").mkdir(parents=True)
    (tmp / "N02_marketing" / "P01").mkdir(parents=True)
    (tmp / ".cex" / "runtime" / "handoffs").mkdir(parents=True)
    return tmp


def _write_fm(path: Path, fields: dict) -> None:
    """Write a markdown file with YAML frontmatter."""
    lines = ["---"]
    for k, v in fields.items():
        if isinstance(v, str):
            lines.append(f'{k}: "{v}"')
        elif v is None:
            lines.append(f"{k}: null")
        else:
            lines.append(f"{k}: {v}")
    lines += ["---", "", "# body", ""]
    path.write_text("\n".join(lines), encoding="ascii")


# ---------------------------------------------------------------------------
# Import module with patched _REPO
# ---------------------------------------------------------------------------

import importlib
import types


def _load_module(repo_root: Path):
    """Load cex_mirror_audit with _REPO patched to repo_root."""
    spec_path = Path(__file__).resolve().parent.parent / "_tools" / "cex_mirror_audit.py"
    loader = importlib.machinery.SourceFileLoader("cex_mirror_audit", str(spec_path))
    mod = types.ModuleType("cex_mirror_audit")
    mod.__file__ = str(spec_path)
    loader.exec_module(mod)
    mod._REPO = repo_root
    mod._N00_DIR = repo_root / "N00_genesis"
    mod._KINDS_META = repo_root / ".cex" / "kinds_meta.json"
    mod._HANDOFFS_DIR = repo_root / ".cex" / "runtime" / "handoffs"
    return mod


# ---------------------------------------------------------------------------
# Test 1: Orphan detection
# ---------------------------------------------------------------------------

class TestOrphanDetection(unittest.TestCase):
    def test_orphan_reported(self):
        with tempfile.TemporaryDirectory() as td:
            repo = _make_repo(Path(td))
            mod = _load_module(repo)

            # Mirror for kind=ghost_tool but NO N00 archetype
            _write_fm(
                repo / "N01_intelligence" / "P01" / "ghost_tool_n01.md",
                {"kind": "ghost_tool", "pillar": "P01", "quality": 8.0},
            )

            result = {"orphans": [], "drift": [], "missing": [], "promotion_candidates": []}
            mirrors = mod._find_all_mirrors()
            for nuc_id, kind, path in mirrors:
                fm = mod._parse_frontmatter(path)
                pillar = str(fm.get("pillar", ""))
                n00 = mod._n00_tpl_for_kind(kind, pillar)
                if n00 is None:
                    result["orphans"].append({"kind": kind, "nucleus": nuc_id})

            self.assertEqual(len(result["orphans"]), 1)
            self.assertEqual(result["orphans"][0]["kind"], "ghost_tool")
            self.assertEqual(result["orphans"][0]["nucleus"], "n01")


# ---------------------------------------------------------------------------
# Test 2: Drift detection (forbidden field override)
# ---------------------------------------------------------------------------

class TestDriftDetection(unittest.TestCase):
    def test_forbidden_field_flagged(self):
        with tempfile.TemporaryDirectory() as td:
            repo = _make_repo(Path(td))
            mod = _load_module(repo)

            # N00 archetype
            _write_fm(
                repo / "N00_genesis" / "P01" / "tpl_widget.md",
                {"kind": "widget", "pillar": "P01", "quality": 7.0, "kind_name": "widget"},
            )
            # Mirror overrides forbidden field kind_name
            _write_fm(
                repo / "N01_intelligence" / "P01" / "widget_n01.md",
                {"kind": "widget", "pillar": "P01", "quality": 8.5, "kind_name": "super_widget"},
            )

            drift = []
            mirrors = mod._find_all_mirrors()
            for nuc_id, kind, path in mirrors:
                fm = mod._parse_frontmatter(path)
                pillar = str(fm.get("pillar", ""))
                n00_path = mod._n00_tpl_for_kind(kind, pillar)
                if n00_path is None:
                    continue
                n00_fm = mod._parse_frontmatter(n00_path)
                for field in mod.FORBIDDEN:
                    if field in fm and fm[field] != n00_fm.get(field):
                        drift.append({"field": field, "kind": kind, "nucleus": nuc_id})

            self.assertEqual(len(drift), 1)
            self.assertEqual(drift[0]["field"], "kind_name")
            self.assertEqual(drift[0]["kind"], "widget")


# ---------------------------------------------------------------------------
# Test 3: Missing mirror (dispatched but absent)
# ---------------------------------------------------------------------------

class TestMissingMirror(unittest.TestCase):
    def test_dispatched_without_mirror(self):
        with tempfile.TemporaryDirectory() as td:
            repo = _make_repo(Path(td))
            mod = _load_module(repo)

            # Handoff references kind=user_model nucleus=n02 but no mirror exists
            handoff = repo / ".cex" / "runtime" / "handoffs" / "test_handoff.md"
            handoff.write_text(
                "---\nnucleus: n02\n---\nkind=user_model nucleus=n02 dispatched 2x\n",
                encoding="ascii",
            )

            dispatched = mod._scan_dispatched()
            mirrors = mod._find_all_mirrors()
            existing = {(n, k) for n, k, _ in mirrors}

            missing = [
                (k, n) for k, n in dispatched
                if (n, k) not in existing
            ]

            self.assertTrue(any(k == "user_model" and n == "n02" for k, n in missing))


# ---------------------------------------------------------------------------
# Test 4: Promotion candidate (mirror quality > N00)
# ---------------------------------------------------------------------------

class TestPromotionCandidate(unittest.TestCase):
    def test_promotion_candidate_identified(self):
        with tempfile.TemporaryDirectory() as td:
            repo = _make_repo(Path(td))
            mod = _load_module(repo)

            # N00 archetype: quality 7.0, no tone
            _write_fm(
                repo / "N00_genesis" / "P01" / "tpl_tagline.md",
                {"kind": "tagline", "pillar": "P01", "quality": 7.0},
            )
            # Mirror: quality 9.2, adds tone (overridable)
            _write_fm(
                repo / "N02_marketing" / "P01" / "tagline_n02.md",
                {"kind": "tagline", "pillar": "P01", "quality": 9.2, "tone": "vibrant"},
            )

            mirrors = mod._find_all_mirrors()
            promos = []
            for nuc_id, kind, path in mirrors:
                fm = mod._parse_frontmatter(path)
                pillar = str(fm.get("pillar", ""))
                n00_path = mod._n00_tpl_for_kind(kind, pillar)
                if n00_path is None:
                    continue
                n00_fm = mod._parse_frontmatter(n00_path)
                try:
                    mq = float(fm.get("quality") or 0)
                    nq = float(n00_fm.get("quality") or 0)
                except (TypeError, ValueError):
                    continue
                delta = [f for f in mod.OVERRIDABLE if f in fm and fm.get(f) != n00_fm.get(f)]
                if mq > nq and delta:
                    promos.append({"kind": kind, "from": nuc_id, "delta_fields": delta})

            self.assertEqual(len(promos), 1)
            self.assertEqual(promos[0]["kind"], "tagline")
            self.assertIn("tone", promos[0]["delta_fields"])


# ---------------------------------------------------------------------------
# Test 5: Clean state -- no issues
# ---------------------------------------------------------------------------

class TestCleanState(unittest.TestCase):
    def test_clean_mirror_passes(self):
        with tempfile.TemporaryDirectory() as td:
            repo = _make_repo(Path(td))
            mod = _load_module(repo)

            # N00 archetype
            _write_fm(
                repo / "N00_genesis" / "P01" / "tpl_agent.md",
                {"kind": "agent", "pillar": "P01", "quality": 8.0, "kind_name": "agent"},
            )
            # Mirror: only overrides allowed field (tone)
            _write_fm(
                repo / "N01_intelligence" / "P01" / "agent_n01.md",
                {"kind": "agent", "pillar": "P01", "quality": 8.5,
                 "kind_name": "agent", "tone": "analytical"},
            )

            orphans = []
            drift_issues = []
            mirrors = mod._find_all_mirrors()
            for nuc_id, kind, path in mirrors:
                fm = mod._parse_frontmatter(path)
                pillar = str(fm.get("pillar", ""))
                n00_path = mod._n00_tpl_for_kind(kind, pillar)
                if n00_path is None:
                    orphans.append(kind)
                    continue
                n00_fm = mod._parse_frontmatter(n00_path)
                for field in mod.FORBIDDEN:
                    if field in fm and fm[field] != n00_fm.get(field):
                        drift_issues.append(field)

            self.assertEqual(orphans, [])
            self.assertEqual(drift_issues, [])


if __name__ == "__main__":
    unittest.main()
