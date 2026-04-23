"""Runtime Evolution smoke tests -- 11 tests covering all Phase 1-3 features.

Tests:
  1. Memory scanner returns correct headers
  2. LLM selector returns top-5 (or keyword fallback)
  3. Memory injection in Motor 8F works
  4. Effort maps to correct model
  5. Tool deny-list blocks denied tool
  6. Hook pre_build executes before
  7. Hook on_quality_fail triggers on low score
  8. Permission scope blocks out-of-scope path
  9. Fork execution produces output metadata
  10. Memory update appends + decays + prunes
  11. Turn counter enforces max_turns budget
"""

import sys
from pathlib import Path

import pytest

# Ensure _tools is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
CEX_ROOT = Path(__file__).resolve().parent.parent.parent


# ---------------------------------------------------------------------------
# Test 1: Memory scanner returns correct headers
# ---------------------------------------------------------------------------


def test_memory_scanner_returns_headers():
    from cex_memory import MemoryHeader, scan_builder_memories

    headers = scan_builder_memories("agent-builder")
    assert isinstance(headers, list)
    if headers:
        h = headers[0]
        assert isinstance(h, MemoryHeader)
        assert h.builder_id == "agent-builder"
        assert h.confidence >= 0.3
        assert h.observation_preview
        assert h.type in ("user", "feedback", "project", "reference")
        # Sorted by confidence DESC
        confs = [h.confidence for h in headers]
        assert confs == sorted(confs, reverse=True)


# ---------------------------------------------------------------------------
# Test 2: LLM selector returns top-5 (or keyword fallback)
# ---------------------------------------------------------------------------


def test_memory_selector_keyword_fallback():
    from cex_memory import scan_builder_memories
    from cex_memory_select import SelectedMemory, select_relevant_memories

    headers = scan_builder_memories("agent-builder")
    if not headers:
        pytest.skip("No agent-builder memories found")

    results = select_relevant_memories(
        query="create agent for sales with persona separation",
        memories=headers,
        builder_id="agent-builder",
        top_k=5,
        use_cache=False,
    )
    assert isinstance(results, list)
    assert len(results) <= 5
    if results:
        assert isinstance(results[0], SelectedMemory)
        assert results[0].path
        assert results[0].confidence >= 0.3


# ---------------------------------------------------------------------------
# Test 3: Memory injection format works
# ---------------------------------------------------------------------------


def test_memory_injection_format():
    from cex_memory_select import SelectedMemory, format_memory_injection

    memories = [
        SelectedMemory(
            path="test/path.md",
            content="---\nobservation: test obs\noutcome: SUCCESS\n---\n# Body",
            type="feedback",
            confidence=0.85,
            builder_id="agent-builder",
        )
    ]
    block = format_memory_injection(memories, total_observations=10)
    assert "## Builder Memory" in block
    assert "top-1 relevant from 10 observations" in block
    assert "feedback" in block
    assert "0.85" in block


# ---------------------------------------------------------------------------
# Test 4: Effort maps to correct model
# ---------------------------------------------------------------------------


def test_effort_maps_to_correct_model():
    from cex_8f_motor import resolve_effort_model

    low = resolve_effort_model("low")
    assert "haiku" in low["model"]
    assert low["extended_thinking"] is False

    medium = resolve_effort_model("medium")
    # Medium maps to n02 model from nucleus_models.yaml.
    # Since 2026-04-06 upgrade, all nuclei use opus-4-6.
    assert "opus" in medium["model"] or "sonnet" in medium["model"]

    high = resolve_effort_model("high")
    assert "opus" in high["model"]
    assert high["extended_thinking"] is False

    max_effort = resolve_effort_model("max")
    assert "opus" in max_effort["model"]
    assert max_effort["extended_thinking"] is True

    # Crew override takes precedence
    overridden = resolve_effort_model("low", crew_override="high")
    assert "opus" in overridden["model"]


# ---------------------------------------------------------------------------
# Test 5: Tool deny-list blocks denied tool
# ---------------------------------------------------------------------------


def test_tool_deny_list_blocks():
    from cex_8f_motor import check_tool_allowed

    # No deny list = allowed
    allowed, reason = check_tool_allowed("Bash", None)
    assert allowed is True

    allowed, reason = check_tool_allowed("Bash", [])
    assert allowed is True

    # Denied tool
    allowed, reason = check_tool_allowed("Bash", ["Bash", "Write"])
    assert allowed is False
    assert "deny list" in reason

    # Case insensitive
    allowed, reason = check_tool_allowed("bash", ["Bash"])
    assert allowed is False

    # Not denied
    allowed, reason = check_tool_allowed("Read", ["Bash", "Write"])
    assert allowed is True


# ---------------------------------------------------------------------------
# Test 6: Hook pre_build executes before
# ---------------------------------------------------------------------------


def test_hook_pre_build_executes():
    from cex_hooks import run_builder_hooks

    hooks_config = {"pre_build": "validate_inputs", "post_build": None}

    # Missing required field
    result = run_builder_hooks(
        hooks_config, "pre_build",
        builder_id="test-builder",
        input_data={"frontmatter": {"kind": "agent"}}
    )
    assert result is not None
    assert result["proceed"] is False
    assert len(result["issues"]) > 0

    # All required fields present
    result = run_builder_hooks(
        hooks_config, "pre_build",
        builder_id="test-builder",
        input_data={"frontmatter": {"id": "x", "kind": "agent", "pillar": "P02", "quality": None}}
    )
    assert result["proceed"] is True

    # Null hook = skip
    result = run_builder_hooks(hooks_config, "post_build", builder_id="test")
    assert result is None


# ---------------------------------------------------------------------------
# Test 7: Hook on_quality_fail triggers on low score
# ---------------------------------------------------------------------------


def test_hook_quality_fail_triggers():
    from cex_hooks import run_builder_hooks

    hooks_config = {"on_quality_fail": "retry_with_feedback"}

    result = run_builder_hooks(
        hooks_config, "on_quality_fail",
        builder_id="test-builder",
        score=5.5,
        gates_failed=["H01", "H03"],
    )
    assert result is not None
    assert result["retry"] is True
    assert "H01" in result["feedback"]
    assert "H03" in result["feedback"]

    # Log quality failure hook
    hooks_config2 = {"on_quality_fail": "log_quality_failure"}
    result2 = run_builder_hooks(
        hooks_config2, "on_quality_fail",
        builder_id="test-builder",
        score=4.0,
        gates_failed=["H02"],
    )
    assert result2 is not None
    assert "retry" in result2


# ---------------------------------------------------------------------------
# Test 8: Permission scope blocks out-of-scope path
# ---------------------------------------------------------------------------


def test_permission_scope_blocks():
    from cex_8f_motor import check_permission_scope

    # Global = always allowed
    allowed, reason = check_permission_scope("agent-builder", "N01_intelligence/foo.md", "global")
    assert allowed is True

    # Restricted = only own builder dir
    allowed, reason = check_permission_scope(
        "agent-builder", "archetypes/builders/agent-builder/bld_config.md", "restricted"
    )
    assert allowed is True

    allowed, reason = check_permission_scope(
        "agent-builder", "N03_engineering/P02_model/foo.md", "restricted"
    )
    assert allowed is False

    # None = global (default)
    allowed, reason = check_permission_scope("agent-builder", "anything/foo.md", None)
    assert allowed is True


# ---------------------------------------------------------------------------
# Test 9: Fork execution produces output metadata
# ---------------------------------------------------------------------------


def test_fork_execution_metadata():
    from cex_crew_runner import CrewRunner, RunState

    plan = {
        "intent": "test fork",
        "parsed": {"verb": "cria", "object": "agent", "domain": "test", "quality": 9.0},
        "functions": [],
    }
    runner = CrewRunner(plan)

    # Test fork context resolution
    assert runner._resolve_fork_context({"fork_context": "fork"}) == "fork"
    assert runner._resolve_fork_context({"fork_context": "inline"}) == "inline"
    assert runner._resolve_fork_context({"fork_context": None}) == "inline"
    assert runner._resolve_fork_context({}) == "inline"

    # Test model resolution
    model, tokens = runner._resolve_model({"model": "claude-opus-4-6", "model_max_tokens": 16000})
    assert "opus" in model
    assert tokens == 16000

    # Default model (falls back to LLM_MODEL constant or router config)
    model, tokens = runner._resolve_model({})
    # Accept either sonnet (default constant) or opus (router override)
    assert "sonnet" in model or "opus" in model

    # Test max turns
    state = RunState(intent="test", plan=plan)
    runner.functions = [{"builders": [{"id": "test-builder", "max_turns": 3}]}]
    for i in range(3):
        allowed, turns = runner._check_max_turns("test-builder", state)
        assert allowed is True
    allowed, turns = runner._check_max_turns("test-builder", state)
    assert allowed is False


# ---------------------------------------------------------------------------
# Test 10: Memory update appends + decays + prunes
# ---------------------------------------------------------------------------


def test_memory_update_functions():
    from cex_memory_update import (append_observation, apply_decay,
                                   prune_low_confidence)

    # Test decay
    fm = {"confidence": 0.8, "memory_scope": "project"}
    content = "---\nconfidence: 0.8\n---\n# Body"
    _, updated_fm, pruned = apply_decay(content, fm)
    assert updated_fm["confidence"] < 0.8  # project decay = 0.05
    assert updated_fm["confidence"] == 0.75

    # Feedback = no decay
    fm2 = {"confidence": 0.8, "memory_scope": "feedback"}
    _, fm2_out, _ = apply_decay(content, fm2)
    assert fm2_out["confidence"] == 0.8

    # Test append
    fm3 = {"confidence": 0.5, "observation_count": 1, "observation": "old", "pattern": "", "evidence": "", "outcome": "UNKNOWN"}
    content3 = "---\nconfidence: 0.5\n---\n# Body"
    new_content, new_fm = append_observation(
        content3, fm3, "new obs", "new pattern", "new evidence",
        0.9, "SUCCESS", "feedback"
    )
    assert "## Observation" in new_content
    assert new_fm["observation_count"] == 2
    assert new_fm["confidence"] == 0.9  # higher conf replaces

    # Test prune
    body_with_low = """---
confidence: 0.5
---
# Summary
Some text

## Observation (2026-03-01T10:00:00)
- **Confidence**: 0.05
Low conf observation

## Observation (2026-03-02T10:00:00)
- **Confidence**: 0.80
High conf observation
"""
    fm4 = {"observation_count": 3}
    pruned_content, pruned_fm, pruned_count = prune_low_confidence(body_with_low, fm4)
    assert pruned_count >= 1  # Low conf observation pruned
    assert "0.80" in pruned_content


# ---------------------------------------------------------------------------
# Test 11: Turn counter enforces max_turns budget
# ---------------------------------------------------------------------------


def test_turn_counter_enforces_max_turns():
    """TurnCounter tracks turns and signals exhaustion."""
    from cex_8f_motor import TurnCounter

    tc = TurnCounter()

    # Register with budget of 5
    tc.register("test-builder", max_turns=5)

    # First 2 turns: no warning
    r1 = tc.increment("test-builder")
    assert r1["current"] == 1
    assert r1["remaining"] == 4
    assert not r1["exhausted"]
    assert r1["warning"] is None

    r2 = tc.increment("test-builder")
    assert r2["current"] == 2
    assert not r2["exhausted"]

    # Turn 3: remaining=2, should warn BUDGET_LOW
    tc.increment("test-builder")  # 3
    r4 = tc.increment("test-builder")  # 4
    assert r4["remaining"] == 1
    assert "TURN_BUDGET_LOW" in (r4["warning"] or "")

    # Turn 5: exhausted
    r5 = tc.increment("test-builder")
    assert r5["current"] == 5
    assert r5["exhausted"]
    assert r5["remaining"] == 0
    assert "TURN_BUDGET_EXHAUSTED" in r5["warning"]

    # Status check without incrementing
    status = tc.status("test-builder")
    assert status["current"] == 5
    assert status["exhausted"]

    # Reset
    tc.reset("test-builder")
    status2 = tc.status("test-builder")
    assert status2["current"] == 0
    assert not status2["exhausted"]

    # Auto-register on unknown builder
    r_auto = tc.increment("unknown-builder")
    assert r_auto["max_turns"] == 25
    assert r_auto["current"] == 1
