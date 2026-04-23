"""Tests for cex_materialize.py -- Sub-agent generation."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_materialize import generate_agent_md, kind_to_slug, load_kinds


class TestKindToSlug:
    @pytest.mark.unit
    @pytest.mark.parametrize("kind,expected", [
        ("knowledge_card", "knowledge-card"),
        ("agent", "agent"),
        ("cli_tool", "cli-tool"),
        ("dispatch_rule", "dispatch-rule"),
    ])
    def test_slug_conversion(self, kind, expected):
        assert kind_to_slug(kind) == expected


class TestGenerateAgentMd:
    @pytest.mark.unit
    def test_generates_markdown(self):
        meta = {
            "pillar": "P01",
            "function": "store",
            "description": "Typed knowledge unit",
        }
        result = generate_agent_md("knowledge_card", meta)
        assert isinstance(result, str)
        assert "knowledge" in result.lower()
        assert len(result) > 50


class TestLoadKinds:
    @pytest.mark.integration
    def test_loads_real_kinds(self):
        kinds = load_kinds()
        assert isinstance(kinds, dict)
        assert len(kinds) >= 90  # 99 kinds in registry
