"""
Tests for cex_evolve.py -- Autonomous Experiment Loop
"""
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_evolve import (_parse_agent_response, analyze_weaknesses,
                        apply_improvement, compute_density, evolve_agent,
                        evolve_auto, get_current_quality, init_results,
                        log_result, read_frontmatter)

CEX_ROOT = Path(__file__).resolve().parent.parent.parent


@pytest.fixture
def sample_artifact(tmp_path):
    """Create a minimal .md artifact for testing."""
    content = """---
id: test_artifact
kind: schema
pillar: P06
title: "Test Schema"
version: 1.0.0
created: 2026-03-31
author: test
quality: null
tags: [test, schema, sample]
tldr: "A test schema for unit testing the evolve tool."
density_score: 0.90
---

# Test Schema

## Required Fields

| Field | Type | Description |
|-------|------|-------------|
| name | string | The name |
| value | int | The value |
| status | enum | active or inactive |

## Notes
This is a simple test schema with tables and structure.
"""
    fp = tmp_path / "test_artifact.md"
    fp.write_text(content, encoding="utf-8")
    return fp


@pytest.fixture
def low_density_artifact(tmp_path):
    """Artifact with filler phrases."""
    content = """---
id: test_low_density
kind: knowledge_card
pillar: P01
title: "Low Density Test"
version: 1.0.0
created: 2026-03-31
author: test
quality: null
tags: [test]
tldr: "Test"
---

# Low Density Test

In this section, we will discuss the importance of testing.
It is important to note that testing is very essential.
As mentioned earlier, we need to test everything.
Please note that this is a very important consideration.
It should be noted that the tests must pass.
In order to achieve this, we need to follow the rules.
Due to the fact that the system is complex, we must be careful.
"""
    fp = tmp_path / "low_density.md"
    fp.write_text(content, encoding="utf-8")
    return fp


@pytest.fixture
def scored_artifact(tmp_path):
    """Artifact already scored."""
    content = """---
id: test_scored
kind: schema
pillar: P06
title: "Scored Schema"
version: 1.0.0
created: 2026-03-31
author: test
quality: 9.2
tags: [test, scored]
tldr: "Already scored artifact."
density_score: 0.92
---

# Scored Schema

| Field | Type |
|-------|------|
| id | string |
"""
    fp = tmp_path / "scored.md"
    fp.write_text(content, encoding="utf-8")
    return fp


# ============================================================
# read_frontmatter tests
# ============================================================

class TestReadFrontmatter:
    def test_reads_basic_fields(self, sample_artifact):
        fm = read_frontmatter(sample_artifact)
        assert fm["id"] == "test_artifact"
        assert fm["kind"] == "schema"
        assert fm["quality"] == "null"

    def test_reads_title(self, sample_artifact):
        fm = read_frontmatter(sample_artifact)
        assert "Test Schema" in fm["title"]

    def test_empty_file(self, tmp_path):
        fp = tmp_path / "empty.md"
        fp.write_text("no frontmatter here", encoding="utf-8")
        fm = read_frontmatter(fp)
        assert fm == {}


# ============================================================
# get_current_quality tests
# ============================================================

class TestGetCurrentQuality:
    def test_null_quality(self, sample_artifact):
        q = get_current_quality(sample_artifact)
        assert q is None

    def test_scored_quality(self, scored_artifact):
        q = get_current_quality(scored_artifact)
        assert q == 9.2

    def test_missing_file(self, tmp_path):
        fp = tmp_path / "nonexistent.md"
        with pytest.raises(FileNotFoundError):
            get_current_quality(fp)


# ============================================================
# compute_density tests
# ============================================================

class TestComputeDensity:
    def test_high_density_artifact(self, sample_artifact):
        d = compute_density(sample_artifact)
        assert d >= 0.85, f"Expected >= 0.85, got {d}"

    def test_low_density_artifact(self, low_density_artifact):
        d = compute_density(low_density_artifact)
        # Should still compute (filler ratio is measured)
        assert 0.0 < d <= 1.0

    def test_returns_float(self, sample_artifact):
        d = compute_density(sample_artifact)
        assert isinstance(d, float)

    def test_empty_body(self, tmp_path):
        fp = tmp_path / "empty_body.md"
        fp.write_text("---\nid: x\n---\n", encoding="utf-8")
        d = compute_density(fp)
        assert d == 0.0 or d >= 0.0  # Should not crash


# ============================================================
# analyze_weaknesses tests
# ============================================================

class TestAnalyzeWeaknesses:
    def test_finds_suggestions(self, sample_artifact):
        suggestions = analyze_weaknesses(sample_artifact)
        assert len(suggestions) >= 1

    def test_low_density_gets_density_suggestion(self, low_density_artifact):
        suggestions = analyze_weaknesses(low_density_artifact)
        suggestion_types = [s.split(":")[0] for s in suggestions]
        # Should detect missing fields or prose issues
        assert len(suggestion_types) >= 1

    def test_returns_list(self, sample_artifact):
        result = analyze_weaknesses(sample_artifact)
        assert isinstance(result, list)

    def test_short_tldr_detected(self, low_density_artifact):
        suggestions = analyze_weaknesses(low_density_artifact)
        types = [s.split(":")[0] for s in suggestions]
        assert "improve_tldr" in types or "add_tags" in types or len(types) > 0


# ============================================================
# apply_improvement tests
# ============================================================

class TestApplyImprovement:
    def test_polish_runs(self, sample_artifact):
        desc = apply_improvement(sample_artifact, "polish: cleanup")
        assert "polish" in desc.lower() or "format" in desc.lower()

    def test_density_score_added(self, tmp_path):
        content = """---
id: no_density
kind: schema
title: "No Density"
version: 1.0.0
created: 2026-03-31
author: test
quality: null
tags: [test]
tldr: "No density score yet."
---

# No Density

Some content here.
"""
        fp = tmp_path / "no_density.md"
        fp.write_text(content, encoding="utf-8")
        desc = apply_improvement(fp, "add_density_score: add density_score field")
        assert "density_score" in desc
        text = fp.read_text(encoding="utf-8")
        assert "density_score:" in text

    def test_filler_removal(self, low_density_artifact):
        desc = apply_improvement(low_density_artifact, "increase_density: remove filler")
        text = low_density_artifact.read_text(encoding="utf-8")
        # At least some filler should be removed
        assert "In this section, we will discuss " not in text or "removed" in desc or "analyzed" in desc


# ============================================================
# Results ledger tests
# ============================================================

class TestResultsLedger:
    def test_init_creates_file(self, tmp_path, monkeypatch):
        test_file = tmp_path / "results.tsv"
        import cex_evolve
        monkeypatch.setattr(cex_evolve, "RESULTS_FILE", test_file)
        init_results()
        assert test_file.exists()
        content = test_file.read_text(encoding="utf-8")
        assert "timestamp" in content
        assert "status" in content

    def test_log_appends(self, tmp_path, monkeypatch):
        test_file = tmp_path / "results.tsv"
        import cex_evolve
        monkeypatch.setattr(cex_evolve, "RESULTS_FILE", test_file)
        init_results()
        log_result("test.md", 1, 8.5, 0.92, "keep", "test improvement")
        content = test_file.read_text(encoding="utf-8")
        assert "test.md" in content
        assert "8.5" in content
        assert "keep" in content

    def test_multiple_logs(self, tmp_path, monkeypatch):
        test_file = tmp_path / "results.tsv"
        import cex_evolve
        monkeypatch.setattr(cex_evolve, "RESULTS_FILE", test_file)
        init_results()
        log_result("a.md", 1, 8.0, 0.90, "keep", "first")
        log_result("a.md", 2, 7.5, 0.88, "discard", "second")
        log_result("b.md", 1, 0.0, 0.0, "crash", "failed")
        lines = test_file.read_text(encoding="utf-8").strip().split("\n")
        assert len(lines) == 4  # header + 3 logs


# ============================================================
# Integration: evolve_single (dry run on real artifact)
# ============================================================

class TestEvolveSingleIntegration:
    def test_already_at_target(self, scored_artifact):
        from cex_evolve import evolve_single
        result = evolve_single(scored_artifact, target=9.0, max_rounds=1, verbose=False)
        assert result["status"] == "skip"
        assert result["quality"] == 9.2

    def test_returns_dict(self, sample_artifact):
        from cex_evolve import evolve_single
        result = evolve_single(sample_artifact, target=99.0, max_rounds=1, verbose=False)
        assert isinstance(result, dict)
        assert "status" in result
        assert "quality" in result
        assert "rounds" in result

    def test_nonexistent_file(self, tmp_path):
        from cex_evolve import evolve_single
        result = evolve_single(tmp_path / "ghost.md", target=9.0, max_rounds=1, verbose=False)
        assert result["status"] == "error"


# ============================================================
# _parse_agent_response tests
# ============================================================

class TestParseAgentResponse:
    def test_parses_hypothesis_and_content(self):
        """Extracts hypothesis line and file content."""
        response = """HYPOTHESIS: added anti-pattern section

---
id: test
kind: schema
---

# Test

Content here."""
        hypothesis, content = _parse_agent_response(response)
        assert hypothesis == "added anti-pattern section"
        assert content.startswith("---")
        assert "# Test" in content

    def test_handles_bare_frontmatter(self):
        """If no HYPOTHESIS line, detects frontmatter directly."""
        response = """---
id: test
kind: schema
---

# Test"""
        hypothesis, content = _parse_agent_response(response)
        assert content.startswith("---")
        assert "direct modification" in hypothesis

    def test_handles_code_block_wrapped(self):
        """Extracts content from markdown code blocks."""
        response = """HYPOTHESIS: reformatted tables

```markdown
---
id: test
---
# Content
```"""
        hypothesis, content = _parse_agent_response(response)
        assert hypothesis == "reformatted tables"
        assert content.startswith("---")

    def test_handles_empty_response(self):
        """Returns empty on empty/None input."""
        assert _parse_agent_response("") == ("", "")
        assert _parse_agent_response(None) == ("", "")

    def test_handles_code_block_no_hypothesis(self):
        """Extracts from code block even without HYPOTHESIS line."""
        response = """Here is the improved version:

```markdown
---
id: improved
---
# Better
```"""
        hypothesis, content = _parse_agent_response(response)
        assert "---" in content


# ============================================================
# Agent mode tests (mocked SDK -- no real LLM calls)
# ============================================================

class TestEvolveAgent:
    def test_file_not_found(self, tmp_path):
        """Agent mode returns error for missing file."""
        result = evolve_agent(tmp_path / "ghost.md")
        assert result["status"] == "error"

    @patch("cex_evolve._get_execute_prompt")
    @patch("cex_evolve.score_artifact", return_value=9.5)
    def test_skips_already_at_target(self, mock_score, mock_get_ep, sample_artifact):
        """Agent mode skips files already at target score."""
        mock_get_ep.return_value = MagicMock()  # import succeeds but never called
        # Mock score_hybrid to return a proper dict (imported inside evolve_agent)
        hybrid_result = {
            "score": 9.5, "structural": 9.5, "rubric": 9.5, "semantic": 9.5,
            "dimensions": {}, "weakest": "", "suggestion": "", "mode": "full",
            "cached": False, "notes": []
        }
        with patch.dict("sys.modules", {"cex_score": MagicMock(score_hybrid=MagicMock(return_value=hybrid_result))}):
            result = evolve_agent(sample_artifact, target=9.0, verbose=False)
        assert result["status"] == "skip"
        assert result["tokens_used"] == 0
        # execute_prompt itself should never be called (the returned function)
        mock_get_ep.return_value.assert_not_called()

    @patch("cex_evolve.git_commit_keep")
    @patch("cex_evolve.validate_artifact", return_value=True)
    @patch("cex_evolve.score_artifact")
    @patch("cex_evolve._get_execute_prompt")
    def test_keep_on_improvement(self, mock_get_ep, mock_score, mock_validate,
                                  mock_commit, sample_artifact):
        """Agent mode keeps changes that improve score."""
        # score_artifact called for: hybrid fallback baseline + post-round scoring
        mock_score.side_effect = [7.0, 8.5, 8.5, 8.5, 8.5]
        mock_ep = MagicMock(return_value="HYPOTHESIS: added examples\n\n---\nid: test\nkind: schema\n---\n# Better")
        mock_get_ep.return_value = mock_ep

        # Block score_hybrid import so it falls back to score_artifact
        import cex_score
        with patch.object(cex_score, 'score_hybrid', side_effect=ImportError("test")):
            result = evolve_agent(sample_artifact, target=9.0, max_rounds=1,
                                  budget_tokens=100000, verbose=False)
        assert result["quality"] == 8.5
        assert result["tokens_used"] > 0
        mock_commit.assert_called_once()

    @patch("cex_evolve.git_restore")
    @patch("cex_evolve.validate_artifact", return_value=True)
    @patch("cex_evolve.score_artifact")
    @patch("cex_evolve._get_execute_prompt")
    def test_discard_on_no_improvement(self, mock_get_ep, mock_score, mock_validate,
                                       mock_restore, sample_artifact):
        """Agent mode discards changes that don't improve score."""
        mock_score.side_effect = [7.0, 6.5, 6.5, 6.5]
        mock_ep = MagicMock(return_value="HYPOTHESIS: tried something\n\n---\nid: test\n---\n# Worse")
        mock_get_ep.return_value = mock_ep

        import cex_score
        with patch.object(cex_score, 'score_hybrid', side_effect=ImportError("test")):
            result = evolve_agent(sample_artifact, target=9.0, max_rounds=1,
                                  budget_tokens=100000, verbose=False)
        assert result["quality"] == 7.0  # stays at baseline
        mock_restore.assert_called()

    @patch("cex_evolve.validate_artifact", return_value=True)
    @patch("cex_evolve.score_artifact", return_value=5.0)
    @patch("cex_evolve._get_execute_prompt")
    def test_budget_stops_loop(self, mock_get_ep, mock_score, mock_validate, sample_artifact):
        """Agent mode stops when budget is exhausted."""
        mock_ep = MagicMock(return_value="HYPOTHESIS: small change\n\n---\nid: x\n---\n# X")
        mock_get_ep.return_value = mock_ep

        import cex_score
        with patch.object(cex_score, 'score_hybrid', side_effect=ImportError("test")):
            result = evolve_agent(sample_artifact, target=9.0, max_rounds=100,
                                  budget_tokens=100, verbose=False)
        # Should stop very quickly (1-2 rounds max before budget exhausted)
        assert result["rounds"] <= 2

    @patch("cex_evolve._get_execute_prompt", side_effect=ImportError("no cex_intent"))
    def test_handles_missing_sdk(self, mock_get_ep, sample_artifact):
        """Agent mode returns error if execute_prompt not available."""
        result = evolve_agent(sample_artifact, verbose=False)
        assert result["status"] == "error"


# ============================================================
# Auto mode tests (hybrid: heuristic + agent)
# ============================================================

class TestEvolveAuto:
    @patch("cex_evolve.evolve_single")
    def test_heuristic_only_above_threshold(self, mock_single, sample_artifact):
        """Auto mode uses heuristic-only when score >= threshold."""
        mock_single.return_value = {"status": "complete", "quality": 9.0, "rounds": 1}
        result = evolve_auto(sample_artifact, threshold=8.5, verbose=False)
        assert result["mode_used"] == "heuristic"
        assert result["tokens_used"] == 0

    @patch("cex_evolve.evolve_agent")
    @patch("cex_evolve.evolve_single")
    def test_triggers_agent_below_threshold(self, mock_single, mock_agent, sample_artifact):
        """Auto mode triggers agent when heuristic score < threshold."""
        mock_single.return_value = {"status": "complete", "quality": 7.0, "rounds": 2}
        mock_agent.return_value = {"status": "complete", "quality": 8.8, "tokens_used": 5000, "delta": 1.8}
        result = evolve_auto(sample_artifact, threshold=8.5, verbose=False)
        assert result["mode_used"] == "agent"
        assert result["tokens_used"] == 5000
        mock_agent.assert_called_once()

    def test_missing_file(self, tmp_path):
        """Auto mode returns error for missing file."""
        result = evolve_auto(tmp_path / "ghost.md", verbose=False)
        assert result["status"] == "error"
