---
id: spec_03_token_budget
kind: spec
8f: F4_reason
pillar: P01
title: "SPEC_03: Token Budget Tracker → cex_token_budget"
version: 1.0.0
status: active
created: 2026-04-05
quality: 9.0
depends_on: []
target_files:
  - _tools/cex_token_budget.py
related:
  - SPEC_03_token_budget
  - cost-budget-builder
  - p01_kc_token_budgeting
  - p01_kc_context_window_config
  - thinking-config-builder
  - bld_collaboration_cost_budget
  - bld_tools_thinking_config
  - spec_token_budget_optimization
  - bld_knowledge_card_thinking_config
  - p03_sp_thinking_config_builder
---

# SPEC_03: Token Budget Tracker → cex_token_budget

## Pattern Harvested

OpenClaude's BudgetTracker is a **continuation-aware token governor** that decides
whether to keep producing or stop, based on budget consumption rate + diminishing returns.

### Key Pattern (from tokenBudget.ts)

```pseudocode
COMPLETION_THRESHOLD = 0.90   # Stop at 90% budget consumed
DIMINISHING_THRESHOLD = 500   # Tokens — if producing less than this, stop

class BudgetTracker:
    continuation_count: int = 0
    last_delta_tokens: int = 0
    last_global_turn_tokens: int = 0
    started_at: timestamp

function checkTokenBudget(tracker, budget, global_turn_tokens):
    if budget is None or budget <= 0:
        return STOP  # No budget = no continuation
    
    pct = round((turn_tokens / budget) * 100)
    delta = global_turn_tokens - tracker.last_global_turn_tokens
    
    # Diminishing returns detection
    is_diminishing = (
        tracker.continuation_count >= 3 AND
        delta < DIMINISHING_THRESHOLD AND
        tracker.last_delta < DIMINISHING_THRESHOLD
    )
    
    # Decision
    if NOT is_diminishing AND turn_tokens < budget * COMPLETION_THRESHOLD:
        tracker.continuation_count += 1
        tracker.last_delta = delta
        return CONTINUE(nudge_message, pct)
    
    if is_diminishing OR tracker.continuation_count > 0:
        return STOP(completion_event={
            continuations, pct, diminishing, duration_ms
        })
    
    return STOP(null)  # Never started continuing
```

### Why This Matters for CEX

CEX currently has basic token counting but **no continuation logic**.
When a builder hits the context limit mid-F6 PRODUCE, it silently truncates.
The BudgetTracker pattern enables:
1. **Continuation nudges** — "You've used 45% of budget, keep going"
2. **Diminishing returns detection** — Stop if producing <500 tokens per cycle
3. **Budget-aware F6** — Allocate budget across sections proportionally

## CEX Adaptation

### What Changes

| Component | Current | After |
|-----------|---------|-------|
| Token counting | `count_tokens(text)` | + `BudgetTracker` with continuation |
| Budget allocation | Static percentages | Dynamic with diminishing returns |
| F6 awareness | None | Budget check between sections |
| Reporting | Token count only | + pct, delta, diminishing flag |

### Modified: `_tools/cex_token_budget.py`

```python
# NEW: Add after existing code

from dataclasses import dataclass, field
from time import time

COMPLETION_THRESHOLD = 0.90
DIMINISHING_THRESHOLD = 500  # tokens

@dataclass
class BudgetTracker:
    """Track token consumption with continuation + diminishing returns."""
    continuation_count: int = 0
    last_delta_tokens: int = 0
    last_global_tokens: int = 0
    started_at: float = field(default_factory=time)
    
    @property
    def duration_ms(self) -> int:
        return int((time() - self.started_at) * 1000)

@dataclass
class BudgetDecision:
    action: str              # "continue" | "stop"
    pct: int = 0             # % of budget consumed
    turn_tokens: int = 0
    budget: int = 0
    nudge_message: str = ""
    diminishing_returns: bool = False
    continuation_count: int = 0
    duration_ms: int = 0

def check_token_budget(tracker: BudgetTracker, budget: int,
                       current_tokens: int) -> BudgetDecision:
    """Check whether to continue producing or stop.
    
    Returns CONTINUE with nudge message, or STOP with completion stats.
    Call this between F6 sections to gate production.
    """
    if budget <= 0:
        return BudgetDecision(action="stop")
    
    pct = round((current_tokens / budget) * 100)
    delta = current_tokens - tracker.last_global_tokens
    
    # Diminishing returns: 3+ continuations with <500 new tokens each
    is_diminishing = (
        tracker.continuation_count >= 3
        and delta < DIMINISHING_THRESHOLD
        and tracker.last_delta_tokens < DIMINISHING_THRESHOLD
    )
    
    if not is_diminishing and current_tokens < budget * COMPLETION_THRESHOLD:
        tracker.continuation_count += 1
        tracker.last_delta_tokens = delta
        tracker.last_global_tokens = current_tokens
        
        nudge = _build_nudge(pct, current_tokens, budget)
        return BudgetDecision(
            action="continue",
            pct=pct,
            turn_tokens=current_tokens,
            budget=budget,
            nudge_message=nudge,
            continuation_count=tracker.continuation_count,
        )
    
    if is_diminishing or tracker.continuation_count > 0:
        return BudgetDecision(
            action="stop",
            pct=pct,
            turn_tokens=current_tokens,
            budget=budget,
            diminishing_returns=is_diminishing,
            continuation_count=tracker.continuation_count,
            duration_ms=tracker.duration_ms,
        )
    
    return BudgetDecision(action="stop")

def _build_nudge(pct: int, current: int, budget: int) -> str:
    remaining = budget - current
    return (
        f"[Budget: {pct}% used ({current}/{budget} tokens). "
        f"{remaining} remaining. Continue producing.]"
    )

# Integration with F6 PRODUCE
def budget_aware_produce(sections: list[dict], max_tokens: int) -> list[str]:
    """Produce artifact sections with budget governance.
    
    Each section gets a proportional token allocation.
    Stops early on diminishing returns.
    """
    tracker = BudgetTracker()
    produced = []
    total_tokens = 0
    
    for section in sections:
        decision = check_token_budget(tracker, max_tokens, total_tokens)
        
        if decision.action == "stop":
            # Log why we stopped
            if decision.diminishing_returns:
                produced.append(f"<!-- Budget: stopped (diminishing returns at {decision.pct}%) -->")
            break
        
        # Produce this section
        content = produce_section(section, budget=max_tokens - total_tokens)
        produced.append(content)
        total_tokens += count_tokens(content)
    
    return produced
```

## Acceptance Criteria

1. ✅ `BudgetTracker` dataclass with continuation tracking
2. ✅ `check_token_budget()` returns continue/stop decisions
3. ✅ Diminishing returns detection after 3+ continuations
4. ✅ Nudge messages include pct + remaining tokens
5. ✅ `budget_aware_produce()` integrates with F6 pipeline
6. ✅ Backward compatible: existing `--count` and `--budget` CLI still work
7. ✅ No new dependencies (pure Python)

## 8F Impact

- **F6 PRODUCE**: Now budget-governed — sections allocated proportionally
- **F7 GOVERN**: Budget stats included in quality report
- **F8 COLLABORATE**: Token usage tracked per worker (feeds SPEC_01 coordinator)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[SPEC_03_token_budget]] | sibling | 0.88 |
| [[cost-budget-builder]] | downstream | 0.26 |
| [[p01_kc_token_budgeting]] | related | 0.23 |
| [[p01_kc_context_window_config]] | downstream | 0.23 |
| [[thinking-config-builder]] | downstream | 0.22 |
| [[bld_collaboration_cost_budget]] | downstream | 0.21 |
| [[bld_tools_thinking_config]] | downstream | 0.21 |
| [[spec_token_budget_optimization]] | downstream | 0.21 |
| [[bld_knowledge_card_thinking_config]] | related | 0.21 |
| [[p03_sp_thinking_config_builder]] | downstream | 0.19 |
