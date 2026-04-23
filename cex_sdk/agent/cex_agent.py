# cex_sdk.agent.cex_agent -- CEXAgent: 8F-aware build layer
# kind: agent / pillar: P02 / 8F: F1->F8
# -*- coding: ascii -*-
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List, Optional

from cex_sdk.agent.context_loader import ContextLoader
from cex_sdk.agent.f8_pipeline import build_system_prompt, resolve_kind_pillar
from cex_sdk.agent.signal_emitter import SignalEmitter
from cex_sdk.models.chat import chat
from cex_sdk.schema.validator import Validator, ValidatorResult


@dataclass
class BuildResult:
    """Result of a CEXAgent.build() call (F1->F8 trace)."""
    artifact: str
    kind: str
    pillar: str
    score: float
    passed: bool
    trace: str
    errors: List[str] = field(default_factory=list)
    signal_path: Optional[str] = None
    context_chars: int = 0


def _guess_kind(intent: str) -> str:
    """Heuristic kind detection from intent text."""
    lower = intent.lower()
    if "agent" in lower:
        return "agent"
    if "prompt" in lower:
        return "prompt_template"
    if "workflow" in lower:
        return "workflow"
    if "knowledge" in lower or "kc" in lower:
        return "knowledge_card"
    if "schema" in lower or "input" in lower:
        return "input_schema"
    if "landing" in lower:
        return "landing_page"
    if "system" in lower:
        return "system_prompt"
    return "knowledge_card"


def _artifact_to_payload(artifact: str, kind: str) -> dict[str, Any]:
    """Parse '---\\nkey: val\\n---\\nbody' into dict with body field."""
    payload: dict[str, Any] = {"kind": kind, "body": artifact}
    if not artifact.startswith("---"):
        return payload

    lines = artifact.split("\n")
    fm_lines: List[str] = []
    body_lines: List[str] = []
    in_fm = False
    fm_closed = False
    for i, line in enumerate(lines):
        if i == 0 and line.strip() == "---":
            in_fm = True
            continue
        if in_fm and line.strip() == "---":
            fm_closed = True
            in_fm = False
            body_lines = lines[i + 1:]
            break
        if in_fm:
            fm_lines.append(line)

    if fm_closed:
        for fm_line in fm_lines:
            if ":" in fm_line:
                k, _, v = fm_line.partition(":")
                payload[k.strip()] = v.strip().strip('"')
        payload["body"] = "\n".join(body_lines).strip()

    return payload


class CEXAgent:
    """
    CEX-aware agent that wraps chat() with the full 8F pipeline.

    F1: resolve kind + pillar
    F3: inject KC + examples from filesystem
    F4: build system prompt with context
    F5: call chat()
    F6: check artifact structure
    F7: Validator.for_kind() inline
    F8: emit signal to .cex/runtime/signals/
    """

    def __init__(
        self,
        nucleus: str = "n03",
        kind: str = "",
        model: str = "",
        repo_root: str = "",
        min_score: float = 8.0,
    ) -> None:
        if not model:
            try:
                from _tools.cex_model_resolver import get_model_string
                model = get_model_string(nucleus)
            except Exception:
                model = "claude-sonnet-4-6"
        self.nucleus = nucleus
        self.kind = kind
        self.model = model
        self.min_score = min_score
        self._context_loader = ContextLoader(repo_root=repo_root)
        self._signal_emitter = SignalEmitter(repo_root=repo_root)

    def build(self, intent: str, *, system: str = "", **kwargs: Any) -> BuildResult:
        """Run F1->F8 pipeline and return BuildResult."""
        trace_parts: List[str] = []

        # F1 CONSTRAIN
        resolved_kind = self.kind or _guess_kind(intent)
        kind, pillar = resolve_kind_pillar(resolved_kind)
        trace_parts.append(f"F1:{kind}/{pillar}")

        # F3 INJECT
        ctx = self._context_loader.load(kind)
        context_injection = ctx.as_injection()
        n_sources = len(ctx.sources)
        trace_parts.append(f"F3:{n_sources}srcs({ctx.total_chars}chars)")

        # F4 REASON -- build system prompt
        sys_prompt = system or build_system_prompt(kind, pillar, context_injection)

        # F5 CALL
        artifact = chat(intent, model=self.model, system=sys_prompt, **kwargs)
        trace_parts.append(f"F5:{len(artifact)}chars")

        # F6 PRODUCE -- basic check
        has_frontmatter = artifact.strip().startswith("---")

        # F7 GOVERN
        payload = _artifact_to_payload(artifact, kind)
        validator = Validator.for_kind(kind, pillar)
        vr: ValidatorResult = validator.validate(payload)
        score = vr.score
        passed = vr.passed and has_frontmatter
        trace_parts.append(f"F7:{score}/10({'pass' if passed else 'fail'})")

        # F8 COLLABORATE
        signal_path: Optional[str] = None
        try:
            signal_path = self._signal_emitter.emit(
                nucleus=self.nucleus,
                status="complete",
                score=score,
                kind=kind,
            )
            trace_parts.append("F8:signal_sent")
        except OSError:
            trace_parts.append("F8:signal_err")

        trace = " | ".join(trace_parts)

        return BuildResult(
            artifact=artifact,
            kind=kind,
            pillar=pillar,
            score=score,
            passed=passed,
            trace=trace,
            errors=vr.errors,
            signal_path=signal_path,
            context_chars=ctx.total_chars,
        )

    def validate(self, payload: dict[str, Any]) -> ValidatorResult:
        """F7 standalone: validate an artifact payload without generating."""
        kind = payload.get("kind", self.kind or "knowledge_card")
        kind, pillar = resolve_kind_pillar(kind)
        return Validator.for_kind(kind, pillar).validate(payload)

    def signal(self, score: float, status: str = "complete") -> str:
        """F8 standalone: emit a signal for this nucleus."""
        return self._signal_emitter.emit(
            nucleus=self.nucleus,
            status=status,
            score=score,
            kind=self.kind,
        )
