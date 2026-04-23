# -*- coding: utf-8 -*-
"""
cex_errors.py -- CEX Error Hierarchy

Typed exceptions for the entire CEX toolchain.
Every tool should raise specific error types instead of bare Exception.

Usage:
    from cex_errors import BuildError, ValidationError, LLMError

    try:
        artifact = runner.f6_produce()
    except LLMError as e:
        logger.error("LLM call failed: %s", e)
        # retry with backoff
    except ValidationError as e:
        logger.error("Artifact invalid: %s", e)
        # fix and retry
"""

from __future__ import annotations


class CEXError(Exception):
    """Base exception for all CEX operations."""

    def __init__(self, message: str, code: str = "CEX_ERROR", context: dict | None = None):
        self.message = message
        self.code = code
        self.context = context or {}
        super().__init__(message)

    def __str__(self) -> str:
        if self.context:
            ctx = ", ".join(f"{k}={v}" for k, v in self.context.items())
            return f"[{self.code}] {self.message} ({ctx})"
        return f"[{self.code}] {self.message}"


class BuildError(CEXError):
    """8F pipeline build failure -- artifact could not be produced."""

    def __init__(self, message: str, stage: str = "", **ctx: object):
        super().__init__(message, code="BUILD_ERROR", context={"stage": stage, **ctx})
        self.stage = stage


class ValidationError(CEXError):
    """Artifact validation failure -- frontmatter, schema, or quality gate."""

    def __init__(self, message: str, path: str = "", gate: str = "", **ctx: object):
        super().__init__(message, code="VALIDATION_ERROR", context={"path": path, "gate": gate, **ctx})
        self.path = path
        self.gate = gate


class CompileError(CEXError):
    """Compilation failure -- .md to .yaml conversion failed."""

    def __init__(self, message: str, path: str = "", **ctx: object):
        super().__init__(message, code="COMPILE_ERROR", context={"path": path, **ctx})
        self.path = path


class IntentError(CEXError):
    """Intent parsing failure -- could not resolve kind/pillar from input."""

    def __init__(self, message: str, intent: str = "", **ctx: object):
        super().__init__(message, code="INTENT_ERROR", context={"intent": intent, **ctx})
        self.intent = intent


class LLMError(CEXError):
    """LLM API call failure -- timeout, rate limit, or API error."""

    def __init__(self, message: str, model: str = "", **ctx: object):
        super().__init__(message, code="LLM_ERROR", context={"model": model, **ctx})
        self.model = model


class ConfigError(CEXError):
    """Configuration error -- missing env var, invalid config, bad path."""

    def __init__(self, message: str, key: str = "", **ctx: object):
        super().__init__(message, code="CONFIG_ERROR", context={"key": key, **ctx})
        self.key = key


class KindError(CEXError):
    """Kind resolution failure -- unknown kind or missing builder."""

    def __init__(self, message: str, kind: str = "", **ctx: object):
        super().__init__(message, code="KIND_ERROR", context={"kind": kind, **ctx})
        self.kind = kind
