"""Tests for cex_errors.py -- Error hierarchy."""

import pytest
from cex_errors import (BuildError, CEXError, CompileError, ConfigError,
                        IntentError, KindError, LLMError, ValidationError)


class TestErrorHierarchy:
    @pytest.mark.unit
    def test_all_inherit_from_cex_error(self):
        """All error types should be subclasses of CEXError."""
        for cls in [BuildError, ValidationError, CompileError, IntentError,
                     LLMError, ConfigError, KindError]:
            assert issubclass(cls, CEXError)
            assert issubclass(cls, Exception)

    @pytest.mark.unit
    def test_cex_error_basic(self):
        e = CEXError("test message")
        assert e.message == "test message"
        assert e.code == "CEX_ERROR"
        assert e.context == {}
        assert str(e) == "[CEX_ERROR] test message"

    @pytest.mark.unit
    def test_cex_error_with_context(self):
        e = CEXError("msg", code="TEST", context={"key": "val"})
        assert "key=val" in str(e)

    @pytest.mark.unit
    def test_build_error(self):
        e = BuildError("F6 failed", stage="F6")
        assert e.stage == "F6"
        assert e.code == "BUILD_ERROR"
        assert "F6" in str(e)

    @pytest.mark.unit
    def test_validation_error(self):
        e = ValidationError("missing id", path="test.md", gate="G1")
        assert e.path == "test.md"
        assert e.gate == "G1"

    @pytest.mark.unit
    def test_compile_error(self):
        e = CompileError("bad yaml", path="artifact.md")
        assert e.path == "artifact.md"

    @pytest.mark.unit
    def test_intent_error(self):
        e = IntentError("unknown kind", intent="create a foobar")
        assert e.intent == "create a foobar"

    @pytest.mark.unit
    def test_llm_error(self):
        e = LLMError("timeout", model="claude-opus-4-6")
        assert e.model == "claude-opus-4-6"

    @pytest.mark.unit
    def test_config_error(self):
        e = ConfigError("not set", key="ANTHROPIC_API_KEY")
        assert e.key == "ANTHROPIC_API_KEY"

    @pytest.mark.unit
    def test_kind_error(self):
        e = KindError("not found", kind="nonexistent")
        assert e.kind == "nonexistent"


class TestErrorCatching:
    @pytest.mark.unit
    def test_catch_specific(self):
        """Specific errors should be catchable by their type."""
        with pytest.raises(BuildError):
            raise BuildError("test")

    @pytest.mark.unit
    def test_catch_base(self):
        """All errors should be catchable via CEXError."""
        with pytest.raises(CEXError):
            raise LLMError("test")

    @pytest.mark.unit
    def test_catch_exception(self):
        """All errors should be catchable via Exception."""
        with pytest.raises(CEXError):
            raise ValidationError("test")
