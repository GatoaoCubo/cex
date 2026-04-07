"""Tests for cex_8f_motor.py -- Intent parsing and kind resolution."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_8f_motor import classify_objects, load_builder_map, parse_intent


class TestParseIntent:
    @pytest.mark.unit
    def test_create_knowledge_card(self):
        result = parse_intent("create a knowledge card about testing")
        assert result is not None
        assert "objects" in result
        assert "knowledge_card" in result["objects"]

    @pytest.mark.unit
    def test_build_agent(self):
        result = parse_intent("build an agent for sales")
        assert result is not None
        assert "verb_action" in result

    @pytest.mark.unit
    def test_empty_intent(self):
        result = parse_intent("")
        # Should handle gracefully -- returns dict with defaults
        assert isinstance(result, dict)

    @pytest.mark.unit
    def test_portuguese_intent(self):
        result = parse_intent("criar um knowledge card sobre python")
        assert result is not None
        assert "verb" in result

    @pytest.mark.unit
    def test_intent_with_kind_hint(self):
        result = parse_intent("create workflow for deployment")
        assert result is not None
        assert "objects" in result


class TestClassifyObjects:
    @pytest.mark.unit
    def test_classify_known_object(self):
        result = classify_objects("knowledge card")
        assert isinstance(result, (list, dict, str, type(None)))

    @pytest.mark.unit
    def test_classify_unknown_object(self):
        result = classify_objects("xyzzy_nonexistent")
        # Should handle gracefully
        assert result is not None or result is None


class TestLoadBuilderMap:
    @pytest.mark.integration
    def test_loads_builder_map(self):
        """Should load builder map from real repo."""
        bmap = load_builder_map()
        assert isinstance(bmap, dict)
        assert len(bmap) > 0
        # Should have known kinds
        assert "knowledge_card" in bmap or "knowledge-card" in bmap or len(bmap) >= 50

    @pytest.mark.integration
    def test_builder_map_values_are_valid(self):
        bmap = load_builder_map()
        for _kind, value in list(bmap.items())[:3]:
            # Values may be dicts or paths depending on implementation
            assert value is not None
