# -*- coding: ascii -*-
"""
Tests for cex_skill_improve.py -- HERMES W4.2

Cases:
1. No-op: trace tools all already in skill -> no change, returns False
2. New edge case: trace has known tool with complex result -> edge case appended
3. New tool call: trace has tool not in skill -> procedure updated, count bumped
"""
from __future__ import annotations

import json
import tempfile
import types
import unittest
from pathlib import Path


# ---------------------------------------------------------------------------
# Module loader
# ---------------------------------------------------------------------------

def _load_module_with_tmp(tmp_dir: Path):
    """Import cex_skill_improve with paths redirected to tmp_dir."""
    repo_root = Path(__file__).resolve().parent.parent
    tool_path = repo_root / "_tools" / "cex_skill_improve.py"
    src = tool_path.read_text(encoding="ascii")
    module = types.ModuleType("cex_skill_improve_test_instance")
    module.__dict__["__file__"] = str(tool_path)
    exec(compile(src, str(tool_path), "exec"), module.__dict__)  # noqa: S102
    module._REPO_ROOT = tmp_dir
    module._TRACES_DIR = tmp_dir / "traces"
    module._SKILLS_DIR = tmp_dir / "skills" / "autocreated"
    module._INDEX_PATH = tmp_dir / "skills" / "index.json"
    return module


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

_SAMPLE_SKILL = """\
---
id: p04_skill_test_skill_abc123
kind: skill
pillar: P04
title: "Auto-Skill: test_skill"
auto_generated_from: abc123
self_improves: true
improvement_count: 0
created: "2026-01-01"
quality: null
tags: [skill, auto_generated]
---

## Goal

Test skill for unit tests.

## When to Apply

Use when testing.

## Prerequisites

- CEX repo context

## Procedure

1. **Read**  args: `file_path=/some/file.md`
2. **Write**  args: `file_path=/some/output.md`
"""


def _write_skill(tmp_dir: Path, content: str = _SAMPLE_SKILL) -> Path:
    skill_dir = tmp_dir / "skills" / "autocreated"
    skill_dir.mkdir(parents=True, exist_ok=True)
    skill_path = skill_dir / "skill_test_skill_abc123.md"
    skill_path.write_text(content, encoding="ascii")
    return skill_path


def _write_trace(tmp_dir: Path, events: list[dict], name: str = "trace_test.jsonl") -> Path:
    trace_dir = tmp_dir / "traces"
    trace_dir.mkdir(parents=True, exist_ok=True)
    trace_path = trace_dir / name
    with open(trace_path, "w", encoding="ascii") as fh:
        for ev in events:
            fh.write(json.dumps(ev) + "\n")
    return trace_path


def _make_events(
    tools: list[str],
    complex_result: bool = False,
    with_error_recovery: bool = False,
) -> list[dict]:
    events = []
    if with_error_recovery:
        # Error on first tool, then success -- tests recovery path detection
        events.append({
            "type": "tool_call",
            "tool": tools[0],
            "args": {},
            "result": "",
            "status": "error",
        })
    for tool in tools:
        result = "x" * 250 if complex_result else "ok"
        events.append({
            "type": "tool_call",
            "tool": tool,
            "args": {"file_path": f"/path/{tool.lower()}.md"},
            "result": result,
            "status": "success",
        })
    return events


# ---------------------------------------------------------------------------
# Case 1: No-op
# ---------------------------------------------------------------------------

class TestNoOp(unittest.TestCase):
    """Trace uses same tools as skill -> no change."""

    def test_noop_diff_is_empty(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            skill_path = _write_skill(tmp)
            events = _make_events(["Read", "Write"])
            trace_path = _write_trace(tmp, events)

            diff = mod.compute_diff(skill_path, trace_path)

            self.assertTrue(diff.is_empty(), f"Expected empty diff, got: {diff.summary()}")

    def test_noop_patch_returns_false(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            skill_path = _write_skill(tmp)
            original_content = skill_path.read_text(encoding="ascii")
            events = _make_events(["Read", "Write"])
            trace_path = _write_trace(tmp, events)

            diff = mod.compute_diff(skill_path, trace_path)
            result = mod.patch_skill(skill_path, diff)

            self.assertFalse(result)
            self.assertEqual(skill_path.read_text(encoding="ascii"), original_content)

    def test_noop_dry_run_returns_false(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            skill_path = _write_skill(tmp)
            original = skill_path.read_text(encoding="ascii")
            events = _make_events(["Read"])
            trace_path = _write_trace(tmp, events)

            diff = mod.compute_diff(skill_path, trace_path)
            result = mod.patch_skill(skill_path, diff, dry_run=True)

            self.assertFalse(result)
            # File must not change in dry-run noop
            self.assertEqual(skill_path.read_text(encoding="ascii"), original)


# ---------------------------------------------------------------------------
# Case 2: New edge case
# ---------------------------------------------------------------------------

class TestNewEdgeCase(unittest.TestCase):
    """Trace has known tool with complex result -> edge case appended."""

    def test_edge_case_detected(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            skill_path = _write_skill(tmp)
            # Read is in skill but with complex result (>200 chars) -> edge case
            events = _make_events(["Read"], complex_result=True)
            trace_path = _write_trace(tmp, events)

            diff = mod.compute_diff(skill_path, trace_path)

            self.assertFalse(diff.is_empty())
            self.assertGreater(len(diff.new_edge_cases), 0)

    def test_edge_case_section_written(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            skill_path = _write_skill(tmp)
            events = _make_events(["Read"], complex_result=True)
            trace_path = _write_trace(tmp, events)

            diff = mod.compute_diff(skill_path, trace_path)
            mod.patch_skill(skill_path, diff)

            content = skill_path.read_text(encoding="ascii")
            self.assertIn("Edge cases", content)

    def test_improvement_count_bumped_on_edge_case(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            skill_path = _write_skill(tmp)
            events = _make_events(["Write"], complex_result=True)
            trace_path = _write_trace(tmp, events)

            diff = mod.compute_diff(skill_path, trace_path)
            mod.patch_skill(skill_path, diff)

            content = skill_path.read_text(encoding="ascii")
            self.assertIn("improvement_count: 1", content)
            self.assertIn("updated:", content)

    def test_error_recovery_path_detected(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            skill_path = _write_skill(tmp)
            # Read: error then success -> recovery path
            events = _make_events(["Read"], with_error_recovery=True)
            trace_path = _write_trace(tmp, events)

            diff = mod.compute_diff(skill_path, trace_path)

            self.assertGreater(len(diff.new_error_paths), 0)

    def test_dry_run_edge_case_no_write(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            skill_path = _write_skill(tmp)
            original = skill_path.read_text(encoding="ascii")
            events = _make_events(["Read"], complex_result=True)
            trace_path = _write_trace(tmp, events)

            diff = mod.compute_diff(skill_path, trace_path)
            result = mod.patch_skill(skill_path, diff, dry_run=True)

            self.assertTrue(result)
            # File must not change in dry-run
            self.assertEqual(skill_path.read_text(encoding="ascii"), original)


# ---------------------------------------------------------------------------
# Case 3: New tool call
# ---------------------------------------------------------------------------

class TestNewToolCall(unittest.TestCase):
    """Trace contains tool not in skill procedure -> procedure updated."""

    def test_new_tool_detected(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            skill_path = _write_skill(tmp)
            # Bash is not documented in the sample skill
            events = _make_events(["Read", "Bash"])
            trace_path = _write_trace(tmp, events)

            diff = mod.compute_diff(skill_path, trace_path)

            self.assertIn("Bash", diff.new_tools)

    def test_new_tool_appended_to_procedure(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            skill_path = _write_skill(tmp)
            events = _make_events(["Read", "Bash"])
            trace_path = _write_trace(tmp, events)

            diff = mod.compute_diff(skill_path, trace_path)
            mod.patch_skill(skill_path, diff)

            content = skill_path.read_text(encoding="ascii")
            self.assertIn("**Bash**", content)

    def test_multiple_new_tools(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            skill_path = _write_skill(tmp)
            events = _make_events(["Read", "Bash", "Glob", "Edit"])
            trace_path = _write_trace(tmp, events)

            diff = mod.compute_diff(skill_path, trace_path)

            # Read and Write are in skill; Bash, Glob, Edit are new
            self.assertEqual(set(diff.new_tools), {"Bash", "Glob", "Edit"})

    def test_improvement_count_bumped_on_new_tool(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            skill_path = _write_skill(tmp)
            events = _make_events(["Bash"])
            trace_path = _write_trace(tmp, events)

            diff = mod.compute_diff(skill_path, trace_path)
            mod.patch_skill(skill_path, diff)

            content = skill_path.read_text(encoding="ascii")
            self.assertIn("improvement_count: 1", content)

    def test_improvement_count_increments_cumulatively(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            skill_path = _write_skill(tmp)

            # First improve: adds Bash
            events1 = _make_events(["Read", "Bash"])
            trace1 = _write_trace(tmp, events1, "trace1.jsonl")
            diff1 = mod.compute_diff(skill_path, trace1)
            mod.patch_skill(skill_path, diff1)

            # Second improve: adds Glob (Bash now in skill)
            events2 = _make_events(["Read", "Bash", "Glob"])
            trace2 = _write_trace(tmp, events2, "trace2.jsonl")
            diff2 = mod.compute_diff(skill_path, trace2)
            mod.patch_skill(skill_path, diff2)

            content = skill_path.read_text(encoding="ascii")
            self.assertIn("improvement_count: 2", content)
            self.assertIn("**Glob**", content)

    def test_dry_run_new_tool_no_write(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            mod = _load_module_with_tmp(tmp)
            skill_path = _write_skill(tmp)
            original = skill_path.read_text(encoding="ascii")
            events = _make_events(["Read", "Bash"])
            trace_path = _write_trace(tmp, events)

            diff = mod.compute_diff(skill_path, trace_path)
            result = mod.patch_skill(skill_path, diff, dry_run=True)

            self.assertTrue(result)
            # File must not change in dry-run
            self.assertEqual(skill_path.read_text(encoding="ascii"), original)


# ---------------------------------------------------------------------------
# Frontmatter helpers
# ---------------------------------------------------------------------------

class TestFrontmatterHelpers(unittest.TestCase):

    def setUp(self):
        tmp = Path(tempfile.mkdtemp())
        self.mod = _load_module_with_tmp(tmp)

    def test_parse_frontmatter_fields(self):
        fields, body = self.mod.parse_frontmatter(_SAMPLE_SKILL)
        self.assertEqual(fields.get("kind"), "skill")
        self.assertEqual(fields.get("improvement_count"), "0")
        self.assertIn("## Goal", body)

    def test_parse_frontmatter_quoted_title(self):
        fields, _ = self.mod.parse_frontmatter(_SAMPLE_SKILL)
        # Title value contains a colon -- must parse correctly
        self.assertIn("Auto-Skill", fields.get("title", ""))

    def test_bump_improvement_count_from_zero(self):
        fields: dict = {"improvement_count": "0", "created": "2026-01-01"}
        self.mod._bump_improvement_count(fields)
        self.assertEqual(fields["improvement_count"], "1")
        self.assertIn("updated", fields)

    def test_bump_improvement_count_accumulates(self):
        fields: dict = {"improvement_count": "5"}
        self.mod._bump_improvement_count(fields)
        self.assertEqual(fields["improvement_count"], "6")

    def test_bump_improvement_count_missing_field(self):
        fields: dict = {}
        self.mod._bump_improvement_count(fields)
        self.assertEqual(fields["improvement_count"], "1")

    def test_serialize_roundtrip(self):
        fields, _ = self.mod.parse_frontmatter(_SAMPLE_SKILL)
        serialized = self.mod.serialize_frontmatter(fields)
        self.assertTrue(serialized.startswith("---"))
        self.assertIn("kind: skill", serialized)

    def test_has_section_true(self):
        body = "## Procedure\n1. step\n## Notes\nmore"
        self.assertTrue(self.mod.has_section(body, "Procedure"))
        self.assertTrue(self.mod.has_section(body, "Notes"))

    def test_has_section_false(self):
        body = "## Procedure\n1. step"
        self.assertFalse(self.mod.has_section(body, "Edge cases"))

    def test_extract_procedure_tools(self):
        _, body = self.mod.parse_frontmatter(_SAMPLE_SKILL)
        tools = self.mod.extract_procedure_tools(body)
        self.assertIn("Read", tools)
        self.assertIn("Write", tools)
        self.assertEqual(len(tools), 2)


if __name__ == "__main__":
    unittest.main()
