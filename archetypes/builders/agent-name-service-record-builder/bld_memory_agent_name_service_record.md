---
kind: learning_record
id: bld_memory_agent_name_service_record
pillar: P10
llm_function: INJECT
purpose: Accumulated observations, pitfalls, and recommendations for building ANS registry records
quality: 9.0
title: "Agent Name Service Record Builder -- Memory"
version: "1.0.0"
author: wave7_n05
tags: [agent_name_service_record, builder, memory, learning_record]
tldr: "Pitfalls: ANS vs agent_card confusion, missing protocol-adapters, incomplete PKI chain. Evidence and fixes."
domain: "agent_name_service_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

# Agent Name Service Record Builder -- Memory

## Learning Record Index

| ID | Category | Status | Date |
|----|---------|--------|------|
| L001 | Pitfall | Active | 2026-04-14 |
| L002 | Pitfall | Active | 2026-04-14 |
| L003 | Pitfall | Active | 2026-04-14 |
| L004 | Pattern | Active | 2026-04-14 |
| L005 | Pattern | Active | 2026-04-14 |
| L006 | Recommendation | Active | 2026-04-14 |
| L007 | Recommendation | Active | 2026-04-14 |

---

## L001: ANS Record vs Agent Card Confusion

**Category**: Pitfall | **Frequency**: High | **Impact**: Wrong artifact produced

**Observation**: Builders conflate `agent_name_service_record` (P04) with `agent_card` (P08). Field overlap (endpoint_url, capabilities) without boundary awareness -> builder defaults to whichever it has more training examples for.

**Evidence**:
- "Register my agent in the ANS" -> produces agent_card instead
- "Create an agent card" -> sometimes produces ANS records

**Fix**:

| Question | ANS record | Agent card |
|---------|-----------|-----------|
| Reader | Agents+orchestrators at runtime | Devs+N07 at design time |
| Enables | Runtime discovery + connection | Design-time deploy decisions |
| Location | P04_tools/ | P08_architecture/ |
| Pillar | P04 (CALL) | P08 (Architecture) |

**Rule**: "Register", "discover", "ANS", "AgentDNS" = ANS. "Define", "spec", "deploy", "agent card" = agent_card.

---

## L002: Missing Protocol Adapters for Production Use

**Category**: Pitfall | **Frequency**: High | **Impact**: H06 fail, record unusable

**Observation**: Builders produce records with only `endpoint_url` and no `protocol_adapters`. Passes H01-H05, H07, H08; fails H06. Even bypassed, no agent can connect without protocol.

**Evidence**:
- GoDaddy prod ANS: >=1 adapter (MCP or A2A) required
- Salesforce Agent Fabric: A2A v0.3 required
- CNCF AgentDNS: protocol_adapters mandatory for record validity

**Root cause**: Builder treats endpoint_url as sufficient (REST assumption). In ANS, endpoint_url is base -- adapters specify HOW.

**Fix**: Phase 1.2 of bld_instruction requires protocol resolution before compose. Claude/MCP stack -> MCP adapter. Enterprise/Salesforce stack -> A2A adapter. If uncertain, ask.

---

## L003: PKI Cert Chain Not Included

**Category**: Pitfall | **Frequency**: Medium | **Impact**: D3=0.0, GoDaddy/Salesforce blocked

**Observation**: Builders omit `pki_cert_reference` or use placeholder `"cert:unknown:SHA256:TBD"`. Passes H01-H08 (PKI soft); scores D3=0.0 for GoDaddy/Salesforce operators -> prod registration blocked.

**Evidence**:
- GoDaddy prod ANS: PKI-cert mandatory since Feb 2026
- Salesforce MuleSoft: PKI-cert mandatory for enterprise A2A
- A2A v0.3 security card signing uses same PKI

**Root cause**: PKI cert material in secret_config (P09) not loaded during ANS construction. Builder skips F3 INJECT for secret_config.

**Fix**: bld_collaboration lists `secret_config` as required input. Load before Phase 2 when operator=godaddy|salesforce. If unavailable, flag + note prod registration blocked.

---

## L004: Protocol Version Pinning Improves Interoperability

**Category**: Pattern | **Frequency**: Medium | **Impact**: Better D2, clearer contracts

**Observation**: Records pinning exact versions (`mcp: 2024-11-05`, `a2a: 0.3`) have fewer connection failures than vague (`mcp: latest`).

**Evidence**: GoDaddy docs recommend pinning MCP=2024-11-05, A2A=0.3 for stable inter-agent comms.

**Rule**: Pin `protocol_adapters[].version`. Discovery follows `/.well-known/agent/{label}`. Use KC protocol table as defaults.

---

## L005: 3-Segment ANS Name Hierarchy Improves Discovery

**Category**: Pattern | **Frequency**: Medium | **Impact**: D1 from 0.6 to 1.0

**Observation**: 3-segment names (`{agent}.{org}.agents`) are more discoverable in CNCF AgentDNS + resolve uniquely across namespaces vs 2-segment (`{agent}.agents`).

**Evidence**: CNCF draft-liang-agentdns-00 recommends 3-segment. GoDaddy uses customer's registered domain as org.

**Rule**: Derive org segment from registry_operator's domain or deploying org's domain. Never use `corp`/`org` -- collide.

---

## L006: Pre-Check for Existing Records Before Building

**Category**: Recommendation | **Impact**: Prevents duplicate registry entries

Before Phase 2 COMPOSE:
```bash
ls P04_tools/p04_ans_*.md | grep {agent_slug}
```
If exists: UPDATE (bump version + `updated`) OR CREATE NEW (new ANS name). Never silently overwrite.

---

## L007: discovery_endpoint Distinct from endpoint_url

**Category**: Recommendation | **Impact**: Prevents H07 false-pass

Many builders set `discovery_endpoint` = `endpoint_url`. Passes H07 syntactically; violates semantic intent:

- `endpoint_url`: where agent ACCEPTS REQUESTS (business endpoint)
- `discovery_endpoint`: where registry-record JSON is SERVED (metadata endpoint)

**Correct pattern**:
```
endpoint_url:       https://agents.acme.com/billing
discovery_endpoint: https://acme.com/.well-known/agent/billing-bot
```

Follows `/.well-known/agent/{label}` per IETF RFC 8615. MUST be distinct from endpoint_url.
