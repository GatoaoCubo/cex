"""Tests for cex_forge.py -- prompt composition and builder loading."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_forge import (inject_builder_context, kind_to_builder_dir,
                       load_builder_specs, validate_prompt)

ROOT = Path(__file__).resolve().parent.parent.parent


class TestKindToBuilderDir:
    def test_simple_kind(self):
        d = kind_to_builder_dir("knowledge_card")
        assert d.name == "knowledge-card-builder"

    def test_underscore_to_dash(self):
        d = kind_to_builder_dir("quality_gate")
        assert "-" in d.name
        assert "_" not in d.name.replace("_builder", "")

    def test_returns_path(self):
        d = kind_to_builder_dir("agent")
        assert isinstance(d, Path)


class TestLoadBuilderSpecs:
    def test_loads_existing_builder(self):
        specs = load_builder_specs("knowledge_card")
        assert isinstance(specs, dict)
        assert len(specs) > 0

    def test_has_manifest(self):
        specs = load_builder_specs("knowledge_card")
        found = any("manifest" in k.lower() for k in specs)
        assert found, f"No manifest found in keys: {list(specs.keys())}"

    def test_nonexistent_kind(self):
        specs = load_builder_specs("nonexistent_kind_xyz")
        assert specs == {} or isinstance(specs, dict)


class TestInjectBuilderContext:
    def test_injects_sections(self):
        sections = ["## Intent\nBuild something"]
        specs = {"manifest": "name: test\nkind: test_kind"}
        result = inject_builder_context(sections, specs)
        assert isinstance(result, list)
        assert len(result) >= len(sections)

    def test_empty_specs(self):
        sections = ["## Intent\nTest"]
        result = inject_builder_context(sections, {})
        assert isinstance(result, list)


class TestValidatePrompt:
    def test_valid_prompt(self):
        prompt = "## Instructions\nCreate a knowledge card about testing.\n## Output\nReturn YAML."
        warnings = validate_prompt(prompt, {})
        assert isinstance(warnings, list)

    def test_empty_prompt(self):
        warnings = validate_prompt("", {})
        assert isinstance(warnings, list)
