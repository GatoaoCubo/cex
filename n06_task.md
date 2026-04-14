---
mission: WAVE7
nucleus: n06
wave: eval-verticals
created: 2026-04-14
model: claude-opus-4-6
---

# N06 -- Build 2 eval/vertical kinds (26 ISOs): HELM + FHIR

## Your kinds (evaluation + healthcare vertical)

1. **llm_evaluation_scenario** (P07/GOVERN, max 4096B) -- HELM Stanford CRFM scenario specification. Task instances, metrics mapping, adapter config, subject area, capability tested, few-shot pool, canonicalization rules. Bridges eval_dataset + benchmark.

2. **fhir_agent_capability** (P08/CONSTRAIN, max 5120B) -- HL7 AI Office FHIR R5 agent capability advertisement (healthcare vertical WG 2026). Agent-as-Resource, capabilities (clinical decision support / summarization / coding / ...), authorization scopes, SMART on FHIR integration, PHI-handling declaration.

## Gold template to clone

Read ALL 13 files in `archetypes/builders/partner-listing-builder/`. Clone SHAPE.

## Required ISOs per kind (13 each = 26 total)

Same 13-ISO structure in `archetypes/builders/{kind}-builder/`.

## Domain keywords (validator check)

- **llm_evaluation_scenario**: HELM, Stanford-CRFM, scenario, task-instance, metric-mapping, adapter, subject-area, canonicalization, few-shot-pool
- **fhir_agent_capability**: FHIR, HL7, SMART-on-FHIR, agent-as-resource, clinical-decision-support, authorization-scope, PHI, R5, healthcare-vertical

## 8F protocol

1. Read partner-listing-builder/ (gold)
2. Read kinds_meta.json (add 2 kinds)
3. Read N01_intelligence/research/ai2ai_exhaustive_scan_20260414.md (HELM + FHIR sections)
4. For each kind x 13 ISOs: clone gold, inject eval/healthcare content
5. Compile + Validate + Fix FAILs
6. Commit: `git add archetypes/builders/{llm-evaluation-scenario,fhir-agent-capability}-builder/ && git commit -m "[N06] WAVE7: 2 eval/vertical kinds (26 ISOs) -- HELM+FHIR"`

## ON COMPLETION

```
python -c "from _tools.signal_writer import write_signal; write_signal('n06', 'complete', 9.0)"
```
