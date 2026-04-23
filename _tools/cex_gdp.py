#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX GDP (Guided Decision Protocol) -- Runtime enforcement layer.

Pattern: OpenClaude permission protocol (tools/*/permissions + coordinatorMode)
Adapted for CEX's domain: ensures subjective decisions go through proper gates.

Decision scopes:
  USER        -- Always ask the human (tone, audience, style, brand voice)
  COORDINATOR -- N07 decides (task routing, priority, wave ordering)
  AUTO        -- System decides (file naming, directory structure)

Usage:
    from cex_gdp import get_gdp, NeedsUserDecision

    gdp = get_gdp()
    try:
        d = gdp.require_decision("What tone?", "tone", ["formal", "casual"])
    except NeedsUserDecision as e:
        # Surface to user via /guide
        print(e.decision.question, e.decision.options)
"""

import hashlib
import time
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import List, Optional

import yaml

CEX_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = CEX_ROOT / ".cex" / "runtime" / "decisions" / "decision_manifest.yaml"
AUDIT_PATH = CEX_ROOT / ".cex" / "runtime" / "decisions" / "audit_log.yaml"


class DecisionScope(str, Enum):
    """Who decides."""
    USER = "user"              # Must ask human (subjective: tone, audience, style)
    COORDINATOR = "coordinator"  # N07 decides (objective-ish: routing, scheduling)
    AUTO = "auto"              # System decides (deterministic: paths, naming)


class DecisionStatus(str, Enum):
    """Decision lifecycle state."""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    DEFERRED = "deferred"


@dataclass
class Decision:
    """A guided decision with scope, status, and audit trail."""
    id: str
    question: str
    scope: DecisionScope
    category: str              # "tone", "audience", "style", "routing", "naming"
    options: List[str] = field(default_factory=list)
    chosen: str = ""
    status: DecisionStatus = DecisionStatus.PENDING
    rationale: str = ""
    decided_by: str = ""       # "user", "n07", "auto"
    decided_at: float = 0.0
    nucleus: str = ""          # Which nucleus this applies to ("" = global)
    kind: str = ""             # Which artifact kind this applies to ("" = any)
    propagate: bool = True     # Inherit to child nuclei

    @property
    def is_resolved(self) -> bool:
        return self.status in (DecisionStatus.APPROVED, DecisionStatus.REJECTED)

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "scope": self.scope.value,
            "category": self.category,
            "options": self.options,
            "chosen": self.chosen,
            "status": self.status.value,
            "rationale": self.rationale,
            "decided_by": self.decided_by,
            "decided_at": self.decided_at,
            "nucleus": self.nucleus,
            "propagate": self.propagate,
        }


# Category -> Default scope mapping
# USER = subjective (human must decide)
# COORDINATOR = tactical (N07 can decide)
# AUTO = deterministic (system decides)
DECISION_CATEGORIES = {
    # USER scope -- always ask human
    "tone": DecisionScope.USER,
    "audience": DecisionScope.USER,
    "style": DecisionScope.USER,
    "brand_voice": DecisionScope.USER,
    "visual_direction": DecisionScope.USER,
    "content_depth": DecisionScope.USER,

    # COORDINATOR scope -- N07 decides
    "task_routing": DecisionScope.COORDINATOR,
    "priority": DecisionScope.COORDINATOR,
    "wave_ordering": DecisionScope.COORDINATOR,
    "nucleus_assignment": DecisionScope.COORDINATOR,

    # AUTO scope -- system decides
    "file_naming": DecisionScope.AUTO,
    "directory_structure": DecisionScope.AUTO,
    "frontmatter_schema": DecisionScope.AUTO,
    "compilation_order": DecisionScope.AUTO,
}


class NeedsUserDecision(Exception):
    """Raised when GDP requires user input before proceeding."""
    def __init__(self, decision: Decision):
        self.decision = decision
        opts = ", ".join(decision.options) if decision.options else "open-ended"
        super().__init__(
            f"GDP gate: '{decision.question}'\n"
            f"  Category: {decision.category}\n"
            f"  Options: {opts}\n"
            f"  Resolve via /guide or gdp.resolve('{decision.id}', chosen)"
        )


class GDPEnforcer:
    """Runtime GDP enforcement -- gates subjective decisions in the 8F pipeline.

    Integration points:
      F4 REASON  -- require_decision() gates plan on unresolved subjective choices
      /guide     -- surfaces NeedsUserDecision to the user
      /grid      -- workers inherit resolved decisions from coordinator
    """

    def __init__(self):
        self.manifest: dict[str, Decision] = {}
        self.session_decisions: dict[str, Decision] = {}
        self._load_manifest()

    def _load_manifest(self):
        """Load persistent decisions from YAML manifest."""
        if not MANIFEST_PATH.exists():
            return
        try:
            data = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8")) or {}
            for did, ddata in data.get("decisions", {}).items():
                self.manifest[did] = Decision(
                    id=did,
                    question=ddata.get("question", ""),
                    scope=DecisionScope(ddata.get("scope", "user")),
                    category=ddata.get("category", ""),
                    options=ddata.get("options", []),
                    chosen=ddata.get("chosen", ""),
                    status=DecisionStatus(ddata.get("status", "pending")),
                    rationale=ddata.get("rationale", ""),
                    decided_by=ddata.get("decided_by", ""),
                    decided_at=ddata.get("decided_at", 0.0),
                    nucleus=ddata.get("nucleus", ""),
                    propagate=ddata.get("propagate", True),
                )
        except Exception:
            pass  # Corrupt manifest -> start fresh

    def require_decision(
        self,
        question: str,
        category: str,
        options: Optional[List[str]] = None,
        nucleus: str = "",
    ) -> Decision:
        """Gate: require a decision before proceeding.

        If already resolved (manifest or session) -> return it.
        If AUTO scope -> auto-resolve immediately.
        If COORDINATOR scope -> return pending (N07 will resolve).
        If USER scope -> raise NeedsUserDecision.
        """
        did = self._decision_id(question, category, nucleus)
        options = options or []

        # Check manifest (persistent)
        if did in self.manifest and self.manifest[did].is_resolved:
            return self.manifest[did]

        # Check session (ephemeral)
        if did in self.session_decisions and self.session_decisions[did].is_resolved:
            return self.session_decisions[did]

        # Determine scope from category
        scope = DECISION_CATEGORIES.get(category, DecisionScope.USER)

        decision = Decision(
            id=did, question=question, scope=scope,
            category=category, options=options, nucleus=nucleus,
        )

        if scope == DecisionScope.AUTO:
            decision.chosen = options[0] if options else "default"
            decision.status = DecisionStatus.APPROVED
            decision.decided_by = "auto"
            decision.decided_at = time.time()
            self.session_decisions[did] = decision
            self._audit(decision)
            return decision

        if scope == DecisionScope.COORDINATOR:
            decision.decided_by = "coordinator"
            self.session_decisions[did] = decision
            return decision  # Pending -- coordinator resolves later

        # USER scope -- must be resolved by human
        self.session_decisions[did] = decision
        raise NeedsUserDecision(decision)

    def resolve(
        self,
        decision_id: str,
        chosen: str,
        rationale: str = "",
        decided_by: str = "user",
        persist: bool = True,
    ) -> Decision:
        """Resolve a pending decision."""
        decision = (
            self.session_decisions.get(decision_id)
            or self.manifest.get(decision_id)
        )
        if not decision:
            raise ValueError(f"Unknown decision: {decision_id}")

        decision.chosen = chosen
        decision.status = DecisionStatus.APPROVED
        decision.rationale = rationale
        decision.decided_by = decided_by
        decision.decided_at = time.time()

        if persist:
            self.manifest[decision_id] = decision
            self._save_manifest()

        self._audit(decision)
        return decision

    def reject(self, decision_id: str, rationale: str = "") -> Decision:
        """Reject a pending decision."""
        decision = (
            self.session_decisions.get(decision_id)
            or self.manifest.get(decision_id)
        )
        if not decision:
            raise ValueError(f"Unknown decision: {decision_id}")

        decision.status = DecisionStatus.REJECTED
        decision.rationale = rationale
        decision.decided_at = time.time()
        self._audit(decision)
        return decision

    def get_for_nucleus(self, nucleus: str) -> List[Decision]:
        """Get all resolved decisions that apply to a nucleus.

        Returns:
          - Decisions specific to this nucleus
          - Global decisions with propagate=True
        """
        result = []
        all_decisions = {**self.manifest, **self.session_decisions}
        for d in all_decisions.values():
            if d.is_resolved:
                if d.nucleus == nucleus or (d.propagate and d.nucleus == ""):
                    result.append(d)
        return result

    def get_pending(self) -> List[Decision]:
        """Get all unresolved decisions (for /guide display)."""
        all_decisions = {**self.manifest, **self.session_decisions}
        return [d for d in all_decisions.values() if not d.is_resolved]

    def summary(self) -> dict:
        """Status summary for /status dashboard."""
        all_d = {**self.manifest, **self.session_decisions}
        return {
            "total": len(all_d),
            "resolved": sum(1 for d in all_d.values() if d.is_resolved),
            "pending": sum(1 for d in all_d.values() if not d.is_resolved),
            "by_scope": {
                scope.value: sum(1 for d in all_d.values() if d.scope == scope)
                for scope in DecisionScope
            },
        }

    def _decision_id(self, question: str, category: str, nucleus: str) -> str:
        """Generate stable decision ID from content."""
        raw = f"{category}:{nucleus}:{question}"
        return hashlib.sha256(raw.encode()).hexdigest()[:12]

    def _save_manifest(self):
        """Persist resolved decisions to YAML."""
        data = {"decisions": {}}
        for did, d in self.manifest.items():
            if d.is_resolved:
                data["decisions"][did] = d.to_dict()

        MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST_PATH.write_text(
            yaml.dump(data, default_flow_style=False, allow_unicode=True),
            encoding="utf-8",
        )

    def _audit(self, decision: Decision):
        """Append to immutable audit log."""
        entry = {
            "id": decision.id,
            "question": decision.question,
            "category": decision.category,
            "chosen": decision.chosen,
            "scope": decision.scope.value,
            "status": decision.status.value,
            "decided_by": decision.decided_by,
            "decided_at": decision.decided_at,
            "rationale": decision.rationale,
        }
        AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(AUDIT_PATH, "a", encoding="utf-8") as f:
            f.write(yaml.dump([entry], default_flow_style=False, allow_unicode=True))


# ---------------------------------------------------------------------------
# Singleton
# ---------------------------------------------------------------------------

_enforcer: Optional[GDPEnforcer] = None


def get_gdp() -> GDPEnforcer:
    """Get the singleton GDP enforcer."""
    global _enforcer
    if _enforcer is None:
        _enforcer = GDPEnforcer()
    return _enforcer


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="CEX GDP -- Guided Decision Protocol")
    parser.add_argument("--status", action="store_true", help="Show decision status")
    parser.add_argument("--pending", action="store_true", help="Show pending decisions")
    parser.add_argument("--resolve", nargs=2, metavar=("ID", "CHOSEN"), help="Resolve a decision")
    parser.add_argument("--rationale", default="", help="Rationale for resolution")
    args = parser.parse_args()

    gdp = get_gdp()

    if args.status:
        s = gdp.summary()
        print("\n=== GDP Status ===")
        print(f"  Total:    {s['total']}")
        print(f"  Resolved: {s['resolved']}")
        print(f"  Pending:  {s['pending']}")
        for scope, count in s['by_scope'].items():
            print(f"  {scope:15s}: {count}")

    elif args.pending:
        pending = gdp.get_pending()
        if not pending:
            print("No pending decisions.")
        else:
            for d in pending:
                opts = ", ".join(d.options) if d.options else "open-ended"
                print(f"\n  [{d.id}] {d.question}")
                print(f"    Category: {d.category} | Scope: {d.scope.value}")
                print(f"    Options: {opts}")

    elif args.resolve:
        did, chosen = args.resolve
        d = gdp.resolve(did, chosen, rationale=args.rationale)
        print(f"[OK] Resolved: {d.question} -> '{d.chosen}'")

    else:
        parser.print_help()
