---
name: monitor
description: Autonomous dispatch monitoring via Monitor tool -- bash while-loop streams nucleus events, N07 keeps working
kind: skill
pillar: P12
nucleus: n07
quality: 7.9
version: 2.0.0
created: 2026-04-20
density_score: 1.0
updated: "2026-04-22"
---

# /monitor -- Autonomous Dispatch Monitoring

> **Mechanism**: Claude Code `Monitor` tool with a bash while-loop.
> Each stdout line is a notification. N07 keeps working between events.

## How It Works

After ANY dispatch, N07 starts a Monitor:

```
Monitor(
  description="N03+N04 dispatch health",
  persistent=true,
  timeout_ms=3600000,
  command="while true; do ..."
)
```

The bash loop runs every 60s, checks git log + process liveness + signals,
and emits one line per event. N07 receives notifications without polling.
The loop exits when all nuclei complete or all PIDs die.

## The Monitor Command

Template (replace NUCLEI and PIDS):

```bash
NUCLEI="n03 n04"
PIDS="14596 17300"
DONE_COUNT=0
TOTAL=$(echo $NUCLEI | wc -w)
while true; do
  for nuc in $NUCLEI; do
    NUC_UPPER=$(echo $nuc | tr 'a-z' 'A-Z')
    # Check commits
    COMMITS=$(git log --oneline --since="90 seconds ago" --all 2>/dev/null | grep -c "\[$NUC_UPPER\]" || true)
    if [ "$COMMITS" -gt 0 ]; then
      MSG=$(git log --oneline --since="90 seconds ago" --all 2>/dev/null | grep "\[$NUC_UPPER\]" | head -1)
      echo "[MONITOR] $NUC_UPPER committed: $MSG"
    fi
    # Check signals
    SIG=$(ls .cex/runtime/signals/signal_${nuc}_*.json 2>/dev/null | wc -l || true)
    if [ "$SIG" -gt 0 ]; then
      echo "[MONITOR] $NUC_UPPER COMPLETE (signal found)"
      DONE_COUNT=$((DONE_COUNT + 1))
    fi
  done
  # Check process liveness
  for pid in $PIDS; do
    if ! powershell -Command "Get-Process -Id $pid -EA SilentlyContinue" >/dev/null 2>&1; then
      echo "[MONITOR] PID $pid DEAD"
    fi
  done
  # All done?
  if [ "$DONE_COUNT" -ge "$TOTAL" ]; then
    echo "[MONITOR] ALL $TOTAL NUCLEI COMPLETE -- ready for /consolidate"
    break
  fi
  sleep 60
done
```

## Rules

1. **Always use Monitor tool**, never repeated Bash calls or ScheduleWakeup
2. **persistent: true** for session-length watches (grids can run 30+ min)
3. **timeout_ms: 3600000** (1 hour max safety net)
4. **sleep 60** between checks (per user feedback -- 60-90s intervals)
5. **Archive stale signals** before starting: `mv .cex/runtime/signals/signal_n0*.json .cex/runtime/signals/archive/`
6. **N07 keeps working** between notifications -- audit, plan, write memory
7. **On ALL COMPLETE**: immediately /consolidate (stop processes, doctor, commit)

## Anti-patterns

| Wrong | Right |
|-------|-------|
| `cex_signal_watch.py` (blocks N07) | Monitor tool (async notifications) |
| Repeated Bash tool calls every 60s | Single Monitor with while-loop |
| ScheduleWakeup during active grid | Monitor + keep working |
| `cex_monitor_bg.py` Python daemon | Native bash in Monitor tool |
| Polling then saying "I'll check later" | Monitor auto-notifies on events |
| Trusting signals alone | Check commits + PID liveness too |
