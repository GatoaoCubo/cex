---
kind: collaboration_config
id: bld_collaboration_personality
pillar: P12
llm_function: COLLABORATE
purpose: F8 collaboration protocol for personality-builder -- save, compile, signal
quality: 8.6
title: "Collaboration: personality-builder"
version: "1.0.0"
author: n03_builder
tags: [personality, builder, collaboration, P12, hermes_origin, F8]
tldr: "F8 protocol: save to P02, compile .md->.yaml, run doctor, commit, signal n03 complete."
domain: "persona construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.87
related:
  - agent_card_engineering_nucleus
  - p02_agent_creation_nucleus
  - p12_ho_admin_template
  - p03_sp_n03_creation_nucleus
  - bld_collaboration_kind
  - p12_dr_builder_nucleus
  - p12_wf_create_orchestration_agent
  - p12_dr_software_project
  - p04_output_github_actions
  - spec_mission_100pct_coverage
---

# Collaboration: personality-builder

## F8 COLLABORATE Checklist

```
[ ] 1. Save artifact to correct pillar directory
[ ] 2. Run cex_compile.py on saved file
[ ] 3. Run cex_doctor.py (quick health check)
[ ] 4. git add + git commit with standard message
[ ] 5. Signal complete via signal_writer
```

## Save Location
```
Archetype:  N00_genesis/P02_model/p02_per_{{name}}.md
Nucleus:    N0X_*/P02_model/p02_per_{{name}}.md
Compiled:   same dir / compiled/p02_per_{{name}}.yaml
```

## Compile
```bash
python _tools/cex_compile.py N00_genesis/P02_model/p02_per_{{name}}.md
# OR for all:
python _tools/cex_compile.py --all
```

## Commit Message Format
```
[N03] personality: add per_{{name}} ({{register}}/{{verbosity}}/{{humor}}, {{value_count}} values)
```

## Signal
```python
from _tools.signal_writer import write_signal
write_signal('n03', 'complete', 9.0, mission='personality_built', kind='personality', name='{{name}}')
```

## Cross-Nucleus Handoff

| Consumer | How they use personality |
|----------|------------------------|
| N03 (builder) | Produces personality artifacts via this builder |
| Any agent (N01-N07) | Reads p02_per_{{name}}.md from P02 at runtime via /personality command |
| N07 (orchestrator) | Dispatches personality build tasks to N03 |
| user_model (N04) | May store preferred_personality in user_model.preferences collection |

## A2A Signal Schema
```json
{
  "nucleus": "n03",
  "status": "complete",
  "score": 9.0,
  "mission": "personality_built",
  "kind": "personality",
  "artifact_id": "per_{{name}}",
  "path": "N00_genesis/P02_model/p02_per_{{name}}.md"
}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent_card_engineering_nucleus]] | upstream | 0.29 |
| [[p02_agent_creation_nucleus]] | upstream | 0.27 |
| [[p12_ho_admin_template]] | related | 0.26 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.25 |
| [[bld_collaboration_kind]] | related | 0.25 |
| [[p12_dr_builder_nucleus]] | related | 0.23 |
| [[p12_wf_create_orchestration_agent]] | related | 0.22 |
| [[p12_dr_software_project]] | related | 0.22 |
| [[p04_output_github_actions]] | upstream | 0.21 |
| [[spec_mission_100pct_coverage]] | upstream | 0.21 |
