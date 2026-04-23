"""Tests for cex_8f_runner.py -- 8F Stateful Artifact Pipeline."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_8f_runner import (F_LABELS, PILLAR_DIRS, EightFRunner, RunState,
                           extract_frontmatter_dict, find_builder_dir,
                           list_kinds, load_pillar_schema, print_banner,
                           strip_frontmatter)

# =============================================================================
# RunState
# =============================================================================

class TestRunState:
    @pytest.mark.unit
    def test_default_state(self):
        s = RunState()
        assert s.intent == ""
        assert s.kind == ""
        assert s.pillar == ""
        assert s.artifact == ""
        assert s.builder_dir is None
        assert isinstance(s.constraints, dict)
        assert isinstance(s.timings, dict)
        assert isinstance(s.errors, list)

    @pytest.mark.unit
    def test_state_with_values(self):
        s = RunState(intent="create agent", kind="agent", pillar="P02")
        assert s.intent == "create agent"
        assert s.kind == "agent"
        assert s.pillar == "P02"


# =============================================================================
# Constants
# =============================================================================

class TestConstants:
    @pytest.mark.unit
    def test_pillar_dirs_populated(self):
        assert len(PILLAR_DIRS) >= 12
        assert "P01" in PILLAR_DIRS
        assert "P12" in PILLAR_DIRS

    @pytest.mark.unit
    def test_f_labels_complete(self):
        assert len(F_LABELS) == 8
        assert F_LABELS["F1"] == "CONSTRAIN"
        assert F_LABELS["F8"] == "COLLABORATE"


# =============================================================================
# Helpers (delegates to cex_shared)
# =============================================================================

class TestHelpers:
    @pytest.mark.unit
    def test_find_builder_dir_known_kind(self):
        bdir = find_builder_dir("agent")
        assert bdir is not None
        assert bdir.exists()
        assert "agent-builder" in bdir.name

    @pytest.mark.unit
    def test_find_builder_dir_unknown(self):
        bdir = find_builder_dir("nonexistent_kind_xyz")
        assert bdir is None

    @pytest.mark.unit
    def test_strip_frontmatter_with_fm(self):
        text = "---\nid: test\n---\n# Body content"
        body = strip_frontmatter(text)
        assert body.startswith("# Body content")

    @pytest.mark.unit
    def test_strip_frontmatter_without_fm(self):
        text = "# No frontmatter here"
        body = strip_frontmatter(text)
        assert body == text

    @pytest.mark.unit
    def test_extract_frontmatter_dict_valid(self):
        text = "---\nid: test\nkind: agent\n---\n# Body"
        fm = extract_frontmatter_dict(text)
        assert fm["id"] == "test"
        assert fm["kind"] == "agent"

    @pytest.mark.unit
    def test_extract_frontmatter_dict_empty(self):
        fm = extract_frontmatter_dict("just text")
        assert fm == {}

    @pytest.mark.unit
    def test_load_pillar_schema_valid(self):
        schema = load_pillar_schema("P01")
        # May be empty dict if no schema, but should not error
        assert isinstance(schema, dict)

    @pytest.mark.unit
    def test_load_pillar_schema_invalid(self):
        schema = load_pillar_schema("P99")
        assert schema == {}


# =============================================================================
# EightFRunner -- Initialization
# =============================================================================

class TestRunnerInit:
    @pytest.mark.unit
    def test_init_with_known_kind(self):
        runner = EightFRunner(intent="create agent", kind="agent", dry_run=True)
        assert runner.state.kind == "agent"
        assert runner.state.pillar == "P02"
        assert runner.state.builder_dir is not None

    @pytest.mark.unit
    def test_init_with_intent_only(self):
        runner = EightFRunner(intent="create a knowledge card", dry_run=True)
        assert runner.state.kind != ""
        assert runner.state.pillar != ""

    @pytest.mark.unit
    def test_init_unknown_kind_fallback(self):
        runner = EightFRunner(intent="do something weird", kind="nonexistent_xyz", dry_run=True)
        # Should still initialize (may fall back)
        assert runner.state.kind is not None

    @pytest.mark.unit
    def test_init_with_context(self):
        runner = EightFRunner(intent="create agent", kind="agent", dry_run=True, context="test context")
        assert runner.state.context == "test context"


# =============================================================================
# EightFRunner -- F1 CONSTRAIN
# =============================================================================

class TestF1Constrain:
    @pytest.mark.unit
    def test_f1_loads_constraints(self):
        runner = EightFRunner(intent="create agent", kind="agent", dry_run=True)
        runner.f1_constrain()
        c = runner.state.constraints
        assert isinstance(c, dict)
        assert "frontmatter_required" in c

    @pytest.mark.unit
    def test_f1_with_schema(self):
        runner = EightFRunner(intent="create agent", kind="agent", dry_run=True)
        runner.f1_constrain()
        # Agent kind should have constraints from schema
        c = runner.state.constraints
        assert isinstance(c.get("frontmatter_required"), list)


# =============================================================================
# EightFRunner -- F2 BECOME
# =============================================================================

class TestF2Become:
    @pytest.mark.unit
    def test_f2_loads_identity(self):
        runner = EightFRunner(intent="create agent", kind="agent", dry_run=True)
        runner.f1_constrain()
        runner.f2_become()
        ident = runner.state.identity
        assert isinstance(ident, dict)
        assert len(ident) > 0

    @pytest.mark.unit
    def test_f2_has_system_prompt(self):
        runner = EightFRunner(intent="create agent", kind="agent", dry_run=True)
        runner.f1_constrain()
        runner.f2_become()
        # Agent builder should have a system prompt
        assert "system_prompt" in runner.state.identity


# =============================================================================
# EightFRunner -- F3 INJECT
# =============================================================================

class TestF3Inject:
    @pytest.mark.unit
    def test_f3_loads_knowledge(self):
        runner = EightFRunner(intent="create agent", kind="agent", dry_run=True)
        runner.f1_constrain()
        runner.f2_become()
        runner.f3_inject()
        k = runner.state.knowledge
        assert isinstance(k, dict)
        assert len(k) > 0

    @pytest.mark.unit
    def test_f3_injects_domain_context(self):
        runner = EightFRunner(
            intent="create agent", kind="agent", dry_run=True,
            context="N03 engineering domain context"
        )
        runner.f1_constrain()
        runner.f2_become()
        runner.f3_inject()
        assert "domain_context" in runner.state.knowledge


# =============================================================================
# EightFRunner -- _clean_llm_output
# =============================================================================

class TestCleanLLMOutput:
    @pytest.mark.unit
    def test_clean_removes_preamble(self):
        runner = EightFRunner(intent="test", kind="agent", dry_run=True)
        text = "Here is the artifact:\n---\nid: test\n---\n# Body"
        result = runner._clean_llm_output(text)
        assert result.startswith("---")

    @pytest.mark.unit
    def test_clean_strips_code_fences(self):
        runner = EightFRunner(intent="test", kind="agent", dry_run=True)
        text = "```yaml\nid: test\nkind: agent\n```\n# Body"
        result = runner._clean_llm_output(text)
        assert "```" not in result

    @pytest.mark.unit
    def test_clean_already_clean(self):
        runner = EightFRunner(intent="test", kind="agent", dry_run=True)
        text = "---\nid: test\n---\n# Body"
        result = runner._clean_llm_output(text)
        assert result.startswith("---")

    @pytest.mark.unit
    def test_clean_adds_missing_delimiter(self):
        runner = EightFRunner(intent="test", kind="agent", dry_run=True)
        text = "no frontmatter at all"
        result = runner._clean_llm_output(text)
        assert result.startswith("---")


# =============================================================================
# EightFRunner -- _state_summary
# =============================================================================

class TestStateSummary:
    @pytest.mark.unit
    def test_summary_f1(self):
        runner = EightFRunner(intent="create agent", kind="agent", dry_run=True)
        runner.f1_constrain()
        summary = runner._state_summary("F1")
        assert "constraints" in summary

    @pytest.mark.unit
    def test_summary_f2(self):
        runner = EightFRunner(intent="create agent", kind="agent", dry_run=True)
        runner.f1_constrain()
        runner.f2_become()
        summary = runner._state_summary("F2")
        assert "identity" in summary

    @pytest.mark.unit
    def test_summary_unknown_fn(self):
        runner = EightFRunner(intent="test", kind="agent", dry_run=True)
        summary = runner._state_summary("F99")
        assert summary == ""


# =============================================================================
# EightFRunner -- F7 GOVERN (gate validation)
# =============================================================================

class TestF7Govern:
    def _make_runner(self):
        """Create a runner with minimal constraints for isolated F7 testing."""
        runner = EightFRunner(intent="create agent", kind="agent", dry_run=True)
        # Set minimal constraints so we only test the gate we care about
        runner.state.constraints = {"frontmatter_required": [], "id_pattern": ""}
        return runner

    @pytest.mark.unit
    def test_f7_validates_good_artifact(self):
        runner = self._make_runner()
        runner.state.artifact = "---\nid: test\nkind: agent\nquality: null\n---\n# Test Agent\n\nBody content."
        runner.f7_govern()
        v = runner.state.verdict
        assert v["passed"] is True
        assert len(v["issues"]) == 0

    @pytest.mark.unit
    def test_f7_fails_missing_frontmatter(self):
        runner = self._make_runner()
        runner.state.artifact = "no frontmatter here"
        runner.f7_govern()
        v = runner.state.verdict
        assert v["passed"] is False
        assert any("H01" in issue for issue in v.get("issues", []))

    @pytest.mark.unit
    def test_f7_fails_wrong_kind(self):
        runner = self._make_runner()
        runner.state.artifact = "---\nid: test\nkind: workflow\nquality: null\n---\n# Wrong kind"
        runner.f7_govern()
        v = runner.state.verdict
        # F7 retries via F6 (dry-run replaces artifact), so check final verdict
        assert v["passed"] is False
        assert v["retries"] > 0  # Confirmed it attempted retries

    @pytest.mark.unit
    def test_f7_fails_quality_not_null(self):
        runner = self._make_runner()
        runner.state.artifact = "---\nid: test\nkind: agent\nquality: 9.0\n---\n# Body"
        runner.f7_govern()
        v = runner.state.verdict
        assert v["passed"] is False
        assert v["retries"] > 0


# =============================================================================
# EightFRunner -- Dry-Run Pipeline
# =============================================================================

class TestDryRunPipeline:
    @pytest.mark.unit
    def test_full_dry_run(self):
        runner = EightFRunner(intent="create agent for testing", kind="agent", dry_run=True)
        state = runner.run()
        # Dry-run should complete without errors
        assert state.kind == "agent"
        assert state.pillar == "P02"
        assert len(state.artifact) > 0
        assert len(state.timings) > 0

    @pytest.mark.unit
    def test_dry_run_stop_at_step(self):
        runner = EightFRunner(intent="create agent", kind="agent", dry_run=True)
        state = runner.run(stop_at=3)
        # Should have timings for F1, F2, F3 only
        assert "F1" in state.timings
        assert "F2" in state.timings
        assert "F3" in state.timings
        assert "F6" not in state.timings

    @pytest.mark.unit
    def test_dry_run_result_mode(self):
        runner = EightFRunner(intent="create agent", kind="agent", dry_run=True)
        state = runner.run()
        assert state.result.get("mode") == "dry-run"


# =============================================================================
# print_banner (smoke test)
# =============================================================================

class TestPrintBanner:
    @pytest.mark.unit
    def test_banner_does_not_crash(self, capsys):
        state = RunState(intent="test", kind="agent", pillar="P02")
        state.result = {"mode": "dry-run", "path": None}
        state.timings = {"F1": 10.0}
        print_banner(state, 100.0)
        captured = capsys.readouterr()
        assert "CEX 8F Runner" in captured.out
        assert "agent" in captured.out


# =============================================================================
# list_kinds (smoke test)
# =============================================================================

class TestListKinds:
    @pytest.mark.unit
    def test_list_kinds_runs(self, capsys):
        list_kinds()
        captured = capsys.readouterr()
        assert "Total:" in captured.out
        assert "99" in captured.out or "kinds" in captured.out
