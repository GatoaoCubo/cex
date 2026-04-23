"""Tests for cex_token_budget.py -- token counting + budget allocation."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_token_budget import (allocate_budget, analyze_prompt, count_tokens,
                              count_tokens_by_section, get_encoder,
                              truncate_to_tokens)

# =============================================================================
# Token Counting
# =============================================================================

class TestCountTokens:
    @pytest.mark.unit
    def test_count_basic(self):
        tokens = count_tokens("Hello, world!")
        assert tokens > 0
        assert tokens < 20

    @pytest.mark.unit
    def test_count_empty(self):
        assert count_tokens("") == 0

    @pytest.mark.unit
    def test_count_longer_text(self):
        text = "The quick brown fox jumps over the lazy dog. " * 10
        tokens = count_tokens(text)
        words = len(text.split())
        # Token count should be roughly close to word count
        assert tokens > words * 0.5
        assert tokens < words * 3

    @pytest.mark.unit
    def test_count_by_section(self):
        sections = {
            "identity": "You are a helpful assistant.",
            "task": "Create a knowledge card about RAG.",
        }
        counts = count_tokens_by_section(sections)
        assert "identity" in counts
        assert "task" in counts
        assert all(v > 0 for v in counts.values())


class TestGetEncoder:
    @pytest.mark.unit
    def test_claude_encoder(self):
        enc = get_encoder("claude-sonnet-4-6")
        assert enc is not None

    @pytest.mark.unit
    def test_unknown_model_fallback(self):
        enc = get_encoder("unknown-model-xyz")
        # Falls back to cl100k_base
        assert enc is not None


# =============================================================================
# Budget Allocation
# =============================================================================

class TestAllocateBudget:
    @pytest.mark.unit
    def test_small_prompt_no_truncation(self):
        sections = {
            "identity": "You are an agent builder.",
            "task": "Create an agent.",
        }
        result = allocate_budget(sections, max_tokens=8192)
        for name, info in result.items():
            assert info["truncated"] is False
            assert info["text"] == sections[name]

    @pytest.mark.unit
    def test_budget_keys(self):
        sections = {"identity": "test", "task": "test"}
        result = allocate_budget(sections)
        for info in result.values():
            assert "tokens_actual" in info
            assert "tokens_budget" in info
            assert "truncated" in info
            assert "text" in info

    @pytest.mark.unit
    def test_oversized_prompt_truncates(self):
        # Create a prompt that exceeds budget
        big_text = "word " * 5000  # ~5000 tokens
        sections = {
            "identity": "short identity",
            "knowledge": big_text,
            "task": "short task",
        }
        result = allocate_budget(sections, max_tokens=2000, reserve_output=500)
        # Knowledge should be truncated
        assert result["knowledge"]["truncated"] is True


# =============================================================================
# Truncation
# =============================================================================

class TestTruncateToTokens:
    @pytest.mark.unit
    def test_short_text_unchanged(self):
        text = "This is short."
        result = truncate_to_tokens(text, max_tokens=100)
        assert result == text

    @pytest.mark.unit
    def test_long_text_truncated(self):
        text = "word " * 1000
        result = truncate_to_tokens(text, max_tokens=50)
        assert len(result) < len(text)
        assert "truncated" in result.lower()


# =============================================================================
# Prompt Analysis
# =============================================================================

class TestAnalyzePrompt:
    @pytest.mark.unit
    def test_analyze_sectioned_prompt(self):
        prompt = "# IDENTITY\n\nYou are a builder.\n\n---\n\n# TASK\n\nBuild an agent."
        analysis = analyze_prompt(prompt)
        assert "total_tokens" in analysis
        assert analysis["total_tokens"] > 0
        assert "sections" in analysis

    @pytest.mark.unit
    def test_analyze_unsectioned_prompt(self):
        prompt = "Just a plain prompt without sections."
        analysis = analyze_prompt(prompt)
        assert analysis["total_tokens"] > 0
        assert "full_prompt" in analysis["sections"]
