# -*- coding: ascii -*-
"""
Tests for cex_skill_autocreate.py -- HERMES W4.1

Cases:
1. Below threshold: < 5 successful tool calls -> no skill written
2. Valid trace: >= 5 successful calls -> skill emitted, index updated
3. Duplicate trace_hash: skipped unless --force
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


# ---------------------------------------------------------------------------
# Helper: make trace events
# ---------------------------------------------------------------------------

def _make_events(n_success: int, has_error: bool = False) -> list[dict]:
    events = []
    for i in range(n_success):
        events.append({
            "type": "tool_call",
            "tool": f"Read",
            "args": {"file_path": f"/path/to/file_{i}.md"},
            "result": f"content_{i}",
            "status": "success",
        })
    if has_error:
        events.append({
            "type": "tool_call",
            "tool": "Bash",
            "args": {},
            "result": "",
            "status": "error",
            "terminal": True,
        })
    return events


def _write_trace(tmp_dir: Path, events: list[dict], name: str = "trace_test.jsonl") -> Path:
    trace_path = tmp_dir / name
    with open(trace_path, "w", encoding="ascii") as fh:
        for ev in events:
            fh.write(json.dumps(ev) + "\n")
    return trace_path


# ---------------------------------------------------------------------------
# Patch module-level paths before import
# ---------------------------------------------------------------------------

import importlib
import types


def _load_module_with_tmp(tmp_dir: Path):
    """Import cex_skill_autocreate with paths redirected to tmp_dir."""
    repo_root = Path(__file__).resolve().parent.parent
    tool_path = repo_root / "_tools" / "cex_skill_autocreate.py"
    src = tool_path.read_text(encoding="ascii")
    module = types.ModuleType("cex_skill_autocreate_test_instance")
    # Inject __file__ so module-level Path(__file__) resolves correctly
    module.__dict__["__file__"] = str(tool_path)
    exec(compile(src, str(tool_path), "exec"), module.__dict__)  # noqa: S102

    # Override paths to use isolated tmp dir
    module._TRACES_DIR = tmp_dir / "traces"
    module._SKILLS_DIR = tmp_dir / "skills" / "autocreated"
    module._INDEX_PATH = tmp_dir / "skills" / "index.json"
    module._SIGNALS_DIR = tmp_dir / "signals"
    return module


class TestBelowThreshold(unittest.TestCase):
    """Case 1: fewer than 5 successful tool calls -> no skill written."""

    def test_below_threshold_no_skill(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            events = _make_events(n_success=3)
            trace_path = _write_trace(tmp, events)

            result = mod.process_trace(trace_path)

            self.assertFalse(result)
            # No skill files should exist
            skill_files = list((tmp / "skills" / "autocreated").glob("*.md")) if (tmp / "skills" / "autocreated").exists() else []
            self.assertEqual(skill_files, [])

    def test_zero_calls_no_skill(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            events = _make_events(n_success=0)
            trace_path = _write_trace(tmp, events)

            result = mod.process_trace(trace_path)
            self.assertFalse(result)

    def test_terminal_error_no_skill(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            events = _make_events(n_success=5, has_error=True)
            trace_path = _write_trace(tmp, events)

            result = mod.process_trace(trace_path)
            self.assertFalse(result)


class TestValidTrace(unittest.TestCase):
    """Case 2: valid trace with >= 5 successful calls -> skill emitted."""

    def test_skill_emitted(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            events = _make_events(n_success=6)
            trace_path = _write_trace(tmp, events)

            result = mod.process_trace(trace_path)
            self.assertTrue(result)

            skill_files = list((tmp / "skills" / "autocreated").glob("*.md"))
            self.assertEqual(len(skill_files), 1)

    def test_index_updated(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            events = _make_events(n_success=5)
            trace_path = _write_trace(tmp, events)

            mod.process_trace(trace_path)

            index = mod.load_index()
            trace_hash = mod.compute_trace_hash(trace_path)
            self.assertIn(trace_hash, index.get("skills", {}))

    def test_skill_has_required_frontmatter_fields(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            events = _make_events(n_success=7)
            trace_path = _write_trace(tmp, events)

            mod.process_trace(trace_path)

            skill_files = list((tmp / "skills" / "autocreated").glob("*.md"))
            content = skill_files[0].read_text(encoding="ascii")
            for field in ("auto_generated_from", "self_improves", "kind: skill",
                          "quality: null", "trigger_tool_call_count_min"):
                self.assertIn(field, content, f"Missing field: {field}")

    def test_dry_run_no_files_written(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            events = _make_events(n_success=5)
            trace_path = _write_trace(tmp, events)

            result = mod.process_trace(trace_path, dry_run=True)
            self.assertTrue(result)

            skill_files = list((tmp / "skills" / "autocreated").glob("*.md")) if (tmp / "skills" / "autocreated").exists() else []
            self.assertEqual(skill_files, [])


class TestDuplicateTrace(unittest.TestCase):
    """Case 3: duplicate trace_hash -> skipped unless --force."""

    def test_duplicate_skipped(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            events = _make_events(n_success=5)
            trace_path = _write_trace(tmp, events)

            # First run: success
            r1 = mod.process_trace(trace_path)
            self.assertTrue(r1)

            # Second run: skip
            r2 = mod.process_trace(trace_path)
            self.assertFalse(r2)

            # Only 1 skill file
            skill_files = list((tmp / "skills" / "autocreated").glob("*.md"))
            self.assertEqual(len(skill_files), 1)

    def test_force_overwrites(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            events = _make_events(n_success=5)
            trace_path = _write_trace(tmp, events)

            r1 = mod.process_trace(trace_path)
            self.assertTrue(r1)

            r2 = mod.process_trace(trace_path, force=True)
            self.assertTrue(r2)


class TestParseSince(unittest.TestCase):
    """parse_since utility."""

    def setUp(self):
        tmp = Path(tempfile.mkdtemp())
        self.mod = _load_module_with_tmp(tmp)

    def test_hours(self):
        from datetime import timezone as tz
        from datetime import datetime as dt
        now = dt.now(tz.utc)
        result = self.mod.parse_since("2h")
        self.assertAlmostEqual((now - result).total_seconds(), 7200, delta=5)

    def test_minutes(self):
        from datetime import timezone as tz
        from datetime import datetime as dt
        now = dt.now(tz.utc)
        result = self.mod.parse_since("30m")
        self.assertAlmostEqual((now - result).total_seconds(), 1800, delta=5)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            self.mod.parse_since("bad")


if __name__ == "__main__":
    unittest.main()
