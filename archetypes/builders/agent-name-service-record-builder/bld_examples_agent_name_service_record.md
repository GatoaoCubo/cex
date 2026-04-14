---
kind: examples
id: bld_examples_agent_name_service_record
pillar: P07
llm_function: GOVERN
purpose: Golden example and anti-examples for agent_name_service_record quality calibration
quality: null
title: "Agent Name Service Record Builder -- Examples"
version: "1.0.0"
author: wave7_n05
tags: [agent_name_service_record, builder, examples]
tldr: "1 production-grade golden example (GoDaddy MCP+A2A) + 2 anti-examples with annotated failures"
domain: "agent_name_service_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

# Agent Name Service Record Builder -- Examples

## Golden Example: GoDaddy Customer-Service Agent

**Scenario**: Production ANS registry-record for a GoDaddy customer-service agent
that supports both MCP and A2A protocols, has a valid PKI-cert, and exposes 3 capabilities.
This record would pass all 8 hard gates and score 9.5+ on soft dimensions.

```markdown
---
kind: agent_name_service_record
id: p04_ans_customer_service_godaddy
pillar: P04
title: "ANS Record: customer-service.godaddy.agents"
version: "1.0.0"
quality: null
agent_name: "customer-service.godaddy.agents"
registry_id: "7f3c8d2a-1b4e-4f9a-8c6d-2e5a7b9f1c3e"
endpoint_url: "https://agents.godaddy.com/customer-service"
registry_operator: "godaddy"
created: "2026-04-14"
updated: "2026-04-14"
pki_cert_reference: "cert:digicert:SHA256:3A7F2B9C1D4E8F0A6B5C3D2E1F4A9B8C7D6E5F4A3B2C1D0E9F8A7B6C5D4E3F2"
discovery_endpoint: "https://godaddy.com/.well-known/agent/customer-service"
tags: [ANS, AgentDNS, IETF, CNCF, godaddy, mcp, a2a, customer-service]
---

# ANS Record: customer-service.godaddy.agents

> IETF ANS registry-record for GoDaddy Customer Service Agent.
> Registry operator: GoDaddy | Protocol adapters: MCP 2024-11-05, A2A 0.3

## Agent Identity

| Field | Value |
|-------|-------|
| ANS Name | `customer-service.godaddy.agents` |
| Registry ID | `7f3c8d2a-1b4e-4f9a-8c6d-2e5a7b9f1c3e` |
| Registry Operator | GoDaddy (production ANS integration, Feb 2026) |
| Primary Endpoint | https://agents.godaddy.com/customer-service |
| Discovery Endpoint | https://godaddy.com/.well-known/agent/customer-service |
| Record Version | 1.0.0 |
| Spec Reference | IETF draft-narajala-ans-00, CNCF draft-liang-agentdns-00 |

## Protocol Adapters

| Protocol | Version | Endpoint | Auth | Status |
|----------|---------|----------|------|--------|
| mcp | 2024-11-05 | https://agents.godaddy.com/customer-service/mcp | bearer | active |
| a2a | 0.3 | https://agents.godaddy.com/customer-service/a2a | mtls | active |

## Capability Advertisement

| Capability | Description |
|-----------|-------------|
| account-lookup | Retrieve customer account details by domain or account ID |
| billing-dispute | Accept and route billing dispute submissions |
| domain-transfer-status | Check status of in-progress domain transfer requests |

**Concurrency**: max_concurrent = 50

**Supported task types:**
- account-query
- billing-action
- domain-status-check

**Performance**: response_time_p95_ms = 340

## PKI Certificate

| Field | Value |
|-------|-------|
| Reference | `cert:digicert:SHA256:3A7F2B9C...` |
| Issuer | DigiCert Inc. |
| Expires | 2027-04-14 |

## Discovery Endpoint

| Field | Value |
|-------|-------|
| URL | https://godaddy.com/.well-known/agent/customer-service |
| Resolution method | HTTPS GET -- returns registry-record JSON |
| TTL (seconds) | 3600 |
| CNCF AgentDNS compatible | Yes -- draft-liang-agentdns-00 |

## Lifecycle

| Field | Value |
|-------|-------|
| Registered | 2026-02-01 |
| Expires | 2027-02-01 |
| Renewal Policy | auto |
| Last Verified | 2026-04-14 |
| Status | active |
```

**Score breakdown**: D1=1.0, D2=1.0 (2 adapters), D3=1.0 (PKI-cert full), D4=1.0 (3 skills), D5=1.0
**Final score**: 10.0/10 -- all hard gates pass, all soft dimensions maxed.

---

## Anti-Example 1: Invalid ANS Name Format

**What went wrong**: The agent name uses underscores (Python variable style) instead
of hyphens. This fails H04 and makes the record invalid per IETF draft-narajala-ans-00.

```markdown
---
kind: agent_name_service_record
id: p04_ans_billing_agent_acme
pillar: P04
quality: null
agent_name: "billing_agent.acme_corp.agents"   # WRONG: underscores not allowed
endpoint_url: "https://agents.acme.com/billing"
registry_operator: "cncf"
...
---
```

**Failure analysis:**

| Gate | Result | Reason |
|------|--------|--------|
| H04 | FAIL | `billing_agent.acme_corp.agents` -- underscores violate DNS-like format |
| H02 | PASS | (id is valid -- id uses underscores, name must not) |

**Fix**: Replace `billing_agent.acme_corp.agents` with `billing-agent.acme-corp.agents`

**Lesson**: ANS names follow DNS label syntax (RFC 1035): lowercase, hyphens only,
no underscores. Python variable naming habits (snake_case) do not apply here.

---

## Anti-Example 2: Missing Protocol Adapters

**What went wrong**: The record only provides an endpoint URL but declares no
protocol-adapter entries. This makes the record useless -- agents cannot connect
without knowing which protocol to use.

```markdown
---
kind: agent_name_service_record
id: p04_ans_support_example
pillar: P04
quality: null
agent_name: "support.example.agents"
endpoint_url: "https://agents.example.com/support"
registry_operator: "self"
discovery_endpoint: "https://example.com/.well-known/agent/support"
lifecycle:
  registered: "2026-04-14"
---

# ANS Record: support.example.agents

The support agent is available at https://agents.example.com/support.
Contact it for any help requests.
```

**Failure analysis:**

| Gate | Result | Reason |
|------|--------|--------|
| H06 | FAIL | `protocol_adapters` array absent -- 0 adapters declared |
| H08 | PASS | lifecycle.registered present |
| H07 | PASS | discovery_endpoint present |

**Score with H06 fixed (hypothetically):**

| Dimension | Score | Reason |
|-----------|-------|--------|
| D2 Protocol coverage | 0.0 | Still 0 adapters -- H06 was the symptom |
| D3 PKI completeness | 0.0 | No pki_cert_reference, self-hosted operator |
| D4 Capability richness | 0.0 | No capability_advertisement block |
| Overall | < 5.0 | Well below publish threshold |

**Fix**: Add at minimum one protocol-adapter block (mcp or a2a), a capability_advertisement
section, and optionally a PKI-cert reference.

**Lesson**: A raw endpoint URL is NOT an ANS registry-record. The record must
declare HOW to connect (protocol-adapter), WHAT the agent can do (capability advertisement),
and WHO is speaking (PKI-cert). Without these, the record is a dead URL, not a discovery entry.
