"""
Tests for cex_nudge.py -- curation nudge runtime (HERMES W4.5)

3 test cases:
  1. Below threshold -- no nudge fires
  2. Above threshold, cadence OK -- nudge fires
  3. Above threshold, cadence blocked (too soon after last nudge) -- nudge blocked
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from cex_nudge import (NudgePolicy, _get_or_create_session, _open_db,
                       cmd_check, cmd_fire, cmd_stats)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_policy(
    policy_id: str = "test_policy",
    trigger_type: str = "turn_count",
    threshold: int = 10,
    min_interval_turns: int = 5,
    max_per_session: int = 3,
) -> NudgePolicy:
    data = {
        "id": policy_id,
        "trigger": {"type": trigger_type, "threshold": threshold},
        "cadence": {
            "min_interval_turns": min_interval_turns,
            "max_per_session": max_per_session,
        },
        "prompt_template": "Notei {{observation}}. Persistir em MEMORY.md?",
        "target_memory": {"destination": "MEMORY.md", "auto_write_if_confirmed": False},
    }
    return NudgePolicy(data, Path(f"{policy_id}.yaml"))


def _seed_session(
    db,
    session_id: str,
    turn_count: int = 0,
    tool_call_count: int = 0,
    last_nudge_turn: int = 0,
    nudge_count: int = 0,
) -> None:
    """Insert session state directly for testing."""
    from cex_nudge import _now_iso
    db.execute(
        "INSERT OR REPLACE INTO nudge_sessions"
        "(session_id, turn_count, tool_call_count, last_nudge_turn, nudge_count, created, updated)"
        " VALUES(?,?,?,?,?,?,?)",
        (session_id, turn_count, tool_call_count, last_nudge_turn, nudge_count,
         _now_iso(), _now_iso()),
    )
    db.commit()


# ---------------------------------------------------------------------------
# Case 1: Below threshold -- no nudge fires
# ---------------------------------------------------------------------------

def test_below_threshold_no_nudge(tmp_path):
    """When turn_count < threshold, should_fire returns False."""
    db_path = tmp_path / "nudge_state.db"
    pol = _make_policy(threshold=10)

    # Session has only 5 turns -- below threshold of 10
    fires = pol.should_fire(
        turn_count=5,
        tool_call_count=0,
        last_nudge_turn=0,
        nudge_count=0,
    )
    assert fires is False

    # Verify via cmd_check: create a real DB with low turn count
    db = _open_db(db_path)
    _seed_session(db, "sess_low", turn_count=5, last_nudge_turn=0, nudge_count=0)
    db.close()

    # Monkeypatch load_policies to return only our controlled policy
    import cex_nudge as mod
    original = mod.load_policies

    def _mock_policies():
        return [pol]

    mod.load_policies = _mock_policies
    try:
        results = cmd_check("sess_low", db_path=db_path)
    finally:
        mod.load_policies = original

    assert results == [], f"Expected no nudges, got: {results}"


# ---------------------------------------------------------------------------
# Case 2: Above threshold, cadence OK -- nudge fires
# ---------------------------------------------------------------------------

def test_above_threshold_cadence_ok_fires(tmp_path):
    """When turn_count hits exact threshold multiple and cadence is clear, fires."""
    db_path = tmp_path / "nudge_state.db"
    pol = _make_policy(threshold=10, min_interval_turns=5, max_per_session=3)

    # turn_count=10, threshold=10 -- 10 % 10 == 0 -> fires
    # last_nudge_turn=0, gap=10 >= min_interval_turns=5 -> OK
    fires = pol.should_fire(
        turn_count=10,
        tool_call_count=0,
        last_nudge_turn=0,
        nudge_count=0,
    )
    assert fires is True, "Policy should fire at turn_count == threshold"

    # Verify cmd_fire emits the nudge text
    db = _open_db(db_path)
    _seed_session(db, "sess_fire", turn_count=10, last_nudge_turn=0, nudge_count=0)
    db.close()

    import cex_nudge as mod
    original = mod.load_policies

    def _mock_policies():
        return [pol]

    mod.load_policies = _mock_policies
    try:
        result = cmd_fire("sess_fire", observation="user prefers terse output",
                          db_path=db_path)
    finally:
        mod.load_policies = original

    assert "user prefers terse output" in result
    assert "Persistir" in result

    # nudge_count should have incremented
    db = _open_db(db_path)
    row = _get_or_create_session(db, "sess_fire")
    assert row["nudge_count"] == 1
    db.close()


# ---------------------------------------------------------------------------
# Case 3: Above threshold, cadence blocked -- no nudge
# ---------------------------------------------------------------------------

def test_above_threshold_cadence_blocked(tmp_path):
    """When cadence min_interval_turns not satisfied, nudge is suppressed."""
    db_path = tmp_path / "nudge_state.db"
    pol = _make_policy(threshold=10, min_interval_turns=8, max_per_session=3)

    # turn_count=20, last_nudge_turn=15 -> gap=5 < min_interval_turns=8 -> blocked
    fires = pol.should_fire(
        turn_count=20,
        tool_call_count=0,
        last_nudge_turn=15,
        nudge_count=1,
    )
    assert fires is False, "Cadence check should block nudge (gap too small)"

    # Also verify max_per_session cap
    fires_capped = pol.should_fire(
        turn_count=30,
        tool_call_count=0,
        last_nudge_turn=0,
        nudge_count=3,  # at max
    )
    assert fires_capped is False, "max_per_session cap should block nudge"

    # Verify cmd_check returns empty when cadence blocked
    db = _open_db(db_path)
    _seed_session(db, "sess_blocked", turn_count=20, last_nudge_turn=15, nudge_count=1)
    db.close()

    import cex_nudge as mod
    original = mod.load_policies

    def _mock_policies():
        return [pol]

    mod.load_policies = _mock_policies
    try:
        results = cmd_check("sess_blocked", db_path=db_path)
    finally:
        mod.load_policies = original

    assert results == [], f"Expected cadence-blocked result, got: {results}"


# ---------------------------------------------------------------------------
# Bonus: stats returns session data
# ---------------------------------------------------------------------------

def test_stats_returns_sessions(tmp_path):
    db_path = tmp_path / "nudge_state.db"
    db = _open_db(db_path)
    _seed_session(db, "sess_alpha", turn_count=15, nudge_count=2)
    _seed_session(db, "sess_beta", turn_count=5, nudge_count=0)
    db.close()

    rows = cmd_stats(db_path=db_path)
    session_ids = {r["session_id"] for r in rows}
    assert "sess_alpha" in session_ids
    assert "sess_beta" in session_ids
