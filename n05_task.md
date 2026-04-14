---
mission: WAVE7
nucleus: n05
wave: compliance-discovery
created: 2026-04-14
model: claude-opus-4-6
---

# N05 -- Build 3 compliance/discovery/observability kinds (39 ISOs): EU Conformity + ANS + Grounding

## Your kinds (ops-facing compliance + discovery)

1. **conformity_assessment** (P11/GOVERN, max 5120B) -- EU AI Act Annex IV conformity assessment (deadline Aug 2026 for high-risk systems). Provider declaration, risk-management-system, data-governance, logging-capability, post-market-monitoring, human-oversight, accuracy-robustness-cybersecurity.

2. **agent_name_service_record** (P04/CALL, max 3072B) -- IETF ANS + CNCF AgentDNS (GoDaddy+Salesforce prod). Agent name (DNS-like), registry record, PKI cert reference, protocol adapter, capability advertisement, discovery endpoint. Consolidates 3 ANS sub-objects.

3. **agent_grounding_record** (P10/PRODUCE, max 4096B) -- OTel/C2PA hybrid emerging standard. Per-inference provenance record: tool calls, retrieved chunks (RAG), KB sources, model signature, timestamp, output hash, downstream use tracking. Closes the loop on output->source traceability.

## Gold template to clone

Read ALL 13 files in `archetypes/builders/partner-listing-builder/`. Clone SHAPE.

## Required ISOs per kind (13 each = 39 total)

Same 13-ISO structure in `archetypes/builders/{kind}-builder/`.

## Domain keywords (validator check)

- **conformity_assessment**: EU-AI-Act, Annex-IV, Article-43, conformity, risk-management-system, data-governance, human-oversight, high-risk, post-market-monitoring, Aug-2026
- **agent_name_service_record**: ANS, IETF, AgentDNS, CNCF, registry-record, PKI-cert, protocol-adapter, GoDaddy, Salesforce, discovery-endpoint
- **agent_grounding_record**: grounding, provenance, tool-call, RAG-chunk, model-signature, output-hash, traceability, OTel, C2PA, per-inference

## 8F protocol

1. Read partner-listing-builder/ (gold)
2. Read kinds_meta.json (add 3 kinds)
3. Read N01_intelligence/research/ai2ai_exhaustive_scan_20260414.md (EU AI Act + ANS + OTel sections)
4. For each kind x 13 ISOs: clone gold, inject compliance/discovery content
5. Compile + Validate + Fix FAILs
6. Commit: `git add archetypes/builders/{conformity-assessment,agent-name-service-record,agent-grounding-record}-builder/ && git commit -m "[N05] WAVE7: 3 compliance/discovery kinds (39 ISOs) -- EU-Conformity+ANS+Grounding"`

## ON COMPLETION

```
python -c "from _tools.signal_writer import write_signal; write_signal('n05', 'complete', 9.0)"
```
