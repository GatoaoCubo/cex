# cex_sdk.agent.context_loader -- lazy KC + examples loader for 8F F3 INJECT
# kind: document_loader / pillar: P01 / 8F: F3 INJECT
# -*- coding: ascii -*-
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import List


@dataclass
class LoadedContext:
    """Context assembled from KC + template + examples for a given kind."""
    kc_text: str = ""
    template_text: str = ""
    examples: List[str] = field(default_factory=list)
    sources: List[str] = field(default_factory=list)

    @property
    def total_chars(self) -> int:
        return len(self.kc_text) + len(self.template_text) + sum(len(e) for e in self.examples)

    def as_injection(self, max_chars: int = 8000) -> str:
        """Assemble context string for LLM prompt injection (truncated to max_chars)."""
        parts: List[str] = []
        if self.kc_text:
            parts.append("=== Kind Context (KC) ===\n" + self.kc_text)
        if self.template_text:
            parts.append("=== Template ===\n" + self.template_text)
        for i, ex in enumerate(self.examples[:3], 1):
            parts.append(f"=== Example {i} ===\n" + ex)
        combined = "\n\n".join(parts)
        if len(combined) > max_chars:
            combined = combined[:max_chars] + "\n...[truncated]"
        return combined


def _find_repo_root(start: Path) -> Path:
    """Walk up from start until CLAUDE.md is found; return that dir."""
    current = start.resolve()
    for _ in range(10):
        if (current / "CLAUDE.md").exists():
            return current
        parent = current.parent
        if parent == current:
            break
        current = parent
    return start.resolve()


class ContextLoader:
    """Loads KC, template, and builder examples for a kind from the CEX repo."""

    def __init__(self, repo_root: str = "") -> None:
        if repo_root:
            self.root = Path(repo_root).resolve()
        else:
            self.root = _find_repo_root(Path(__file__).parent)

    def load(self, kind: str) -> LoadedContext:
        ctx = LoadedContext()

        # 1. KC: N00_genesis/P01_knowledge/library/kind/kc_{kind}.md
        kc_path = self.root / "N00_genesis" / "P01_knowledge" / "library" / "kind" / f"kc_{kind}.md"
        if kc_path.exists():
            ctx.kc_text = self._read(kc_path)
            ctx.sources.append(str(kc_path.relative_to(self.root)))

        # 2. Template: N00_genesis/compiled/tpl_{kind}.yaml
        tpl_path = self.root / "N00_genesis" / "compiled" / f"tpl_{kind}.yaml"
        if tpl_path.exists():
            ctx.template_text = self._read(tpl_path)
            ctx.sources.append(str(tpl_path.relative_to(self.root)))

        # 3. Builder prompt: archetypes/builders/{kind}-builder/bld_prompt_{kind}.md
        instr_path = (
            self.root / "archetypes" / "builders" / f"{kind}-builder" / f"bld_prompt_{kind}.md"
        )
        if instr_path.exists():
            ctx.template_text = ctx.template_text or self._read(instr_path)
            ctx.sources.append(str(instr_path.relative_to(self.root)))

        # 4. Eval: first 3 bld_eval_*.md from builder dir (merged quality_gate + examples)
        builder_dir = self.root / "archetypes" / "builders" / f"{kind}-builder"
        if builder_dir.exists():
            ex_files = sorted(builder_dir.glob("bld_eval_*.md"))[:3]
            for ex_file in ex_files:
                text = self._read(ex_file)
                if text:
                    ctx.examples.append(text)
                    ctx.sources.append(str(ex_file.relative_to(self.root)))

        return ctx

    @staticmethod
    def _read(path: Path) -> str:
        try:
            return path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return ""
