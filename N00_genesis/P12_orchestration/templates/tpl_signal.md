---
# TEMPLATE: Signal (P12 Orchestration)
# Valide contra P12_orchestration/_schema.yaml (types.signal)
# Max 4096 bytes

id: p12_sig_{{EVENT_SLUG}}
kind: signal
8f: F8_collaborate
pillar: P12
title: "Signal: {{EVENT_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Signal: {{EVENT_NAME}}

## Signal Mode: Event
```json
{
  "agent_group": "{{AGENT_GROUP_NAME}}",
  "mode": "event",
  "status": "{{complete|error|progress}}",
  "quality_score": {{QUALITY_SCORE}},
  "timestamp": "{{ISO_TIMESTAMP}}"
}
```

## Signal Mode: State Snapshot
<!-- Complementary to event mode — carries full position for cross-session resume -->
```json
{
  "agent_group": "{{AGENT_GROUP_NAME}}",
  "mode": "state_snapshot",
  "position": {
    "phase": "{{CURRENT_PHASE}}",
    "step": "{{CURRENT_STEP}}",
    "plan": "{{HANDOFF_FILE_OR_MISSION}}"
  },
  "progress_pct": {{0_TO_100}},
  "stopped_at": "{{DESCRIPTION_OF_LAST_ACTION}}",
  "blockers": ["{{BLOCKER_1}}", "{{BLOCKER_2}}"],
  "session_continuity": {
    "can_resume": {{true|false}},
    "resume_hint": "{{WHAT_TO_DO_NEXT}}"
  },
  "quality_score": {{QUALITY_SCORE}},
  "timestamp": "{{ISO_TIMESTAMP}}"
}
```

## Emission Rules
- Emit event when: {{EVENT_TRIGGER}} (task completion, error, progress milestone)
- Emit state_snapshot when: session stop, blocker hit, or progress >= 50%
- Consumer: {{EXPECTED_CONSUMER}}
- Retry: {{RETRY_RULE}}
