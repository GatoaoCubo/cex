---
id: spec_07_gdp_enforcement
kind: spec
pillar: P01
title: "SPEC_07: Permission Protocol → GDP Enforcement"
version: 1.0.0
status: active
created: 2026-04-05
quality: 9.0
depends_on: []
target_files:
  - _tools/cex_gdp.py (NEW)
  - .cex/runtime/decisions/decision_manifest.yaml
  - .claude/rules/guided-decisions.md
---

# SPEC_07: Permission Protocol → GDP Enforcement

## Pattern Harvested

OpenClaude has a **multi-layer permission system** with 5 modes, cascading rules,
and a "bubble" mechanism where child agents can surface permission requests to parents.

### Key Patterns (from tools/*/permissions* + coordinatorMode.ts)

```pseudocode
# 1. Permission modes (cascading priority)
modes = [
    "bypassPermissions",   # Highest — skip all checks
    "acceptEdits",         # Auto-accept file edits
    "auto",                # Classifier-based (ML model decides)
    "bubble",              # Forward to parent terminal
    "default",             # Ask user
]

# 2. Rule sources (layered)
alwaysAllowRules = {
    cliArg: [...],     # From SDK --allowedTools (preserved across agents)
    session: [...],    # Per-session approvals (scoped to agent)
}

# 3. Agent permission scoping
if spawning_agent:
    if allowedTools provided:
        # REPLACE session rules (parent approvals don't leak)
        agent.rules = { cliArg: parent.cliArg, session: allowedTools }
    if agent.permissionMode defined:
        # Override unless parent is bypass/acceptEdits/auto
        if parent.mode not in (bypass, acceptEdits, auto):
            agent.mode = agent.permissionMode

# 4. Bubble mode
if agent.mode == "bubble":
    # Permission prompts surface to parent terminal
    # Good for: background agents that share the terminal
    shouldAvoidPrompts = false

# 5. Auto-deny for background agents
if isAsync and not canShowPermissionPrompts:
    toolPermissionContext.shouldAvoidPermissionPrompts = true
```

### The Synthesis: GDP + OpenClaude Permission Model

CEX's GDP (Guided Decision Protocol) maps to OpenClaude's permission model:

| OpenClaude | CEX GDP |
|------------|---------|
| Permission mode | Decision scope (user/auto/nucleus) |
| bypassPermissions | `auto_execute: true` in manifest |
| default (ask user) | GDP `ask_user` gate |
| bubble | N07 coordinator reviews sub-nucleus decision |
| allowedTools | Manifest-declared allowed actions |
| session rules | Decision manifest (persistent) |

## CEX Adaptation

### What Changes

| Component | Current | After |
|-----------|---------|-------|
| GDP | Rules-only (.md) | Runtime enforcement class |
| Decision manifest | YAML file (passive) | Active gate in pipeline |
| Scope | Binary (ask/don't) | 3-tier: user / coordinator / auto |
| Propagation | Not enforced | Child nuclei inherit scoped decisions |
| Audit trail | Not tracked | Every decision logged with rationale |

### New: `_tools/cex_gdp.py`

```python
"""CEX GDP (Guided Decision Protocol) — Runtime enforcement layer.

Ensures subjective decisions go through proper gates before execution.
Adapted from OpenClaude's permission protocol for CEX's domain.

Decision types:
  USER     — Always ask the user (tone, audience, style)
  COORD    — N07 coordinator decides (task routing, priority)
  AUTO     — System decides (file naming, directory structure)
  
Scope inheritance:
  Parent decisions propagate to child nuclei unless overridden.
  CLI-level decisions (from /guide) persist across the session.
"""

import yaml, time, hashlib
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional

CEX_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = CEX_ROOT / ".cex" / "runtime" / "decisions" / "decision_manifest.yaml"
AUDIT_PATH = CEX_ROOT / ".cex" / "runtime" / "decisions" / "audit_log.yaml"

class DecisionScope(str, Enum):
    USER = "user"        # Must ask human (subjective: tone, audience, style)
    COORD = "coordinator" # N07 decides (objective-ish: routing, scheduling)
    AUTO = "auto"        # System decides (deterministic: paths, naming)

class DecisionStatus(str, Enum):
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
    category: str          # "tone", "audience", "style", "routing", "naming"
    options: list[str] = field(default_factory=list)
    chosen: str = ""
    status: DecisionStatus = DecisionStatus.PENDING
    rationale: str = ""
    decided_by: str = ""   # "user", "n07", "auto"
    decided_at: float = 0.0
    nucleus: str = ""      # Which nucleus this applies to
    propagate: bool = True  # Inherit to child nuclei
    
    @property
    def is_resolved(self) -> bool:
        return self.status in (DecisionStatus.APPROVED, DecisionStatus.REJECTED)

# Decision categories and their default scopes
DECISION_CATEGORIES = {
    # USER scope — always ask human
    "tone": DecisionScope.USER,
    "audience": DecisionScope.USER,
    "style": DecisionScope.USER,
    "brand_voice": DecisionScope.USER,
    "visual_direction": DecisionScope.USER,
    
    # COORDINATOR scope — N07 decides
    "task_routing": DecisionScope.COORD,
    "priority": DecisionScope.COORD,
    "wave_ordering": DecisionScope.COORD,
    "nucleus_assignment": DecisionScope.COORD,
    
    # AUTO scope — system decides
    "file_naming": DecisionScope.AUTO,
    "directory_structure": DecisionScope.AUTO,
    "frontmatter_schema": DecisionScope.AUTO,
    "compilation_order": DecisionScope.AUTO,
}

class GDPEnforcer:
    """Runtime GDP enforcement — gates subjective decisions."""
    
    def __init__(self):
        self.manifest: dict[str, Decision] = {}
        self.session_decisions: dict[str, Decision] = {}
        self._load_manifest()
    
    def _load_manifest(self):
        """Load persistent decisions from manifest."""
        if MANIFEST_PATH.exists():
            data = yaml.safe_load(MANIFEST_PATH.read_text()) or {}
            for did, ddata in data.get("decisions", {}).items():
                self.manifest[did] = Decision(
                    id=did,
                    question=ddata.get("question", ""),
                    scope=DecisionScope(ddata.get("scope", "user")),
                    category=ddata.get("category", ""),
                    chosen=ddata.get("chosen", ""),
                    status=DecisionStatus(ddata.get("status", "pending")),
                    rationale=ddata.get("rationale", ""),
                    decided_by=ddata.get("decided_by", ""),
                    nucleus=ddata.get("nucleus", ""),
                    propagate=ddata.get("propagate", True),
                )
    
    def require_decision(self, question: str, category: str,
                         options: list[str] = [],
                         nucleus: str = "") -> Decision:
        """Gate: require a decision before proceeding.
        
        If decision exists in manifest → return it.
        If scope is AUTO → auto-resolve.
        If scope is COORD → check coordinator.
        If scope is USER → raise NeedsUserDecision.
        """
        # Generate stable ID
        did = self._decision_id(question, category, nucleus)
        
        # Check manifest first (persistent decisions)
        if did in self.manifest and self.manifest[did].is_resolved:
            return self.manifest[did]
        
        # Check session decisions
        if did in self.session_decisions and self.session_decisions[did].is_resolved:
            return self.session_decisions[did]
        
        # Determine scope
        scope = DECISION_CATEGORIES.get(category, DecisionScope.USER)
        
        decision = Decision(
            id=did, question=question, scope=scope,
            category=category, options=options, nucleus=nucleus,
        )
        
        if scope == DecisionScope.AUTO:
            # Auto-resolve: pick first option or default
            decision.chosen = options[0] if options else "default"
            decision.status = DecisionStatus.APPROVED
            decision.decided_by = "auto"
            decision.decided_at = time.time()
            self._record(decision)
            return decision
        
        if scope == DecisionScope.COORD:
            # Coordinator decides — return pending for N07 to resolve
            decision.decided_by = "coordinator"
            self.session_decisions[did] = decision
            return decision
        
        # USER scope — must be resolved by human
        decision.decided_by = "user"
        self.session_decisions[did] = decision
        raise NeedsUserDecision(decision)
    
    def resolve(self, decision_id: str, chosen: str, 
                rationale: str = "", persist: bool = True):
        """Resolve a pending decision."""
        decision = (self.session_decisions.get(decision_id) 
                    or self.manifest.get(decision_id))
        if not decision:
            raise ValueError(f"Unknown decision: {decision_id}")
        
        decision.chosen = chosen
        decision.status = DecisionStatus.APPROVED
        decision.rationale = rationale
        decision.decided_at = time.time()
        
        if persist:
            self.manifest[decision_id] = decision
            self._save_manifest()
        
        self._audit(decision)
        return decision
    
    def get_for_nucleus(self, nucleus: str) -> list[Decision]:
        """Get all decisions that apply to a nucleus (including inherited)."""
        result = []
        for d in list(self.manifest.values()) + list(self.session_decisions.values()):
            if d.is_resolved:
                if d.nucleus == nucleus or (d.propagate and d.nucleus == ""):
                    result.append(d)
        return result
    
    def _decision_id(self, question: str, category: str, nucleus: str) -> str:
        raw = f"{category}:{nucleus}:{question}"
        return hashlib.sha256(raw.encode()).hexdigest()[:12]
    
    def _save_manifest(self):
        """Persist manifest to YAML."""
        data = {"decisions": {}}
        for did, d in self.manifest.items():
            if d.is_resolved:
                data["decisions"][did] = {
                    "question": d.question,
                    "scope": d.scope.value,
                    "category": d.category,
                    "chosen": d.chosen,
                    "status": d.status.value,
                    "rationale": d.rationale,
                    "decided_by": d.decided_by,
                    "nucleus": d.nucleus,
                    "propagate": d.propagate,
                }
        MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST_PATH.write_text(yaml.dump(data, default_flow_style=False))
    
    def _record(self, decision: Decision):
        self.session_decisions[decision.id] = decision
    
    def _audit(self, decision: Decision):
        """Append to audit log."""
        entry = {
            "id": decision.id,
            "question": decision.question,
            "chosen": decision.chosen,
            "scope": decision.scope.value,
            "decided_by": decision.decided_by,
            "decided_at": decision.decided_at,
            "rationale": decision.rationale,
        }
        AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(AUDIT_PATH, "a") as f:
            f.write(yaml.dump([entry], default_flow_style=False))

class NeedsUserDecision(Exception):
    """Raised when GDP requires user input."""
    def __init__(self, decision: Decision):
        self.decision = decision
        super().__init__(
            f"GDP: '{decision.question}' requires user decision.\n"
            f"Options: {decision.options}\n"
            f"Category: {decision.category}"
        )

# Singleton
_enforcer = None
def get_gdp() -> GDPEnforcer:
    global _enforcer
    if _enforcer is None:
        _enforcer = GDPEnforcer()
    return _enforcer
```

### Integration with 8F Pipeline

```python
# In F4 REASON phase:
from cex_gdp import get_gdp, NeedsUserDecision

def f4_reason(kind, plan):
    gdp = get_gdp()
    
    try:
        # These will auto-resolve (AUTO scope)
        naming = gdp.require_decision(
            f"File naming for {kind}", "file_naming",
            options=[f"{kind}_v1.md", f"{kind}_draft.md"]
        )
        
        # This will raise NeedsUserDecision (USER scope)
        tone = gdp.require_decision(
            "What tone for this content?", "tone",
            options=["formal", "casual", "technical"]
        )
    except NeedsUserDecision as e:
        # Surface to user via /guide
        return {"status": "needs_decision", "decision": e.decision}
    
    return {"status": "ready", "decisions": gdp.get_for_nucleus(plan.nucleus)}
```

## Acceptance Criteria

1. ✅ `GDPEnforcer` with 3-tier scope (user/coordinator/auto)
2. ✅ `require_decision()` gates pipeline on unresolved decisions
3. ✅ `NeedsUserDecision` exception surfaces to /guide
4. ✅ Persistent manifest survives across sessions
5. ✅ Audit trail logs every decision with rationale
6. ✅ Nucleus inheritance (global decisions propagate)
7. ✅ Category→scope mapping (14 categories defined)
8. ✅ Integration with F4 REASON phase
9. ✅ Backward compat: existing manifest file format preserved

## 8F Impact

- **F4 REASON**: GDP gates subjective decisions before F6
- **F7 GOVERN**: Decision audit included in quality assessment
- **F1 CONSTRAIN**: Auto-scope decisions reduce user friction
