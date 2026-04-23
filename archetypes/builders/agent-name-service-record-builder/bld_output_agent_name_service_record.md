---
kind: output_template
id: bld_output_template_agent_name_service_record
pillar: P05
llm_function: PRODUCE
purpose: Canonical output template for agent_name_service_record artifacts
quality: 9.1
title: "Agent Name Service Record Builder -- Output Template"
version: "1.0.0"
author: wave7_n05
tags: [agent_name_service_record, builder, output_template]
tldr: "Copy this template and fill in the placeholders to produce a valid ANS registry record"
domain: "agent_name_service_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_agent_name_service_record
  - bld_system_prompt_agent_name_service_record
  - bld_knowledge_card_agent_name_service_record
  - bld_schema_agent_name_service_record
  - bld_examples_agent_name_service_record
  - bld_manifest_agent_name_service_record
  - bld_collaboration_agent_name_service_record
  - bld_tools_agent_name_service_record
  - bld_memory_agent_name_service_record
  - bld_quality_gate_agent_name_service_record
---

# Agent Name Service Record Builder -- Output Template

## Usage

Copy the template below verbatim. Replace all `{{PLACEHOLDER}}` tokens.
Do not remove any section -- each maps to a hard gate or soft dimension.
See `bld_schema_agent_name_service_record.md` for field validation rules.

---

## Template

```markdown
---
kind: agent_name_service_record
id: p04_ans_{{AGENT_SLUG}}
pillar: P04
title: "ANS Record: {{ANS_NAME}}"
version: "1.0.0"
quality: null
agent_name: "{{ANS_NAME}}"
registry_id: "{{UUID_V4}}"
endpoint_url: "{{PRIMARY_ENDPOINT_URL}}"
registry_operator: "{{OPERATOR}}"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
pki_cert_reference: "cert:{{CA_ISSUER}}:SHA256:{{FINGERPRINT}}"
discovery_endpoint: "{{DISCOVERY_ENDPOINT_URL}}"
tags: [ANS, AgentDNS, IETF, CNCF, {{OPERATOR}}, {{PROTOCOLS}}]
---

# ANS Record: {{ANS_NAME}}

> IETF ANS registry-record for {{HUMAN_AGENT_NAME}}.
> Registry operator: {{OPERATOR}} | Protocol adapters: {{PROTOCOL_LIST}}

## Agent Identity

| Field | Value |
|-------|-------|
| ANS Name | `{{ANS_NAME}}` |
| Registry ID | `{{UUID_V4}}` |
| Registry Operator | {{OPERATOR}} |
| Primary Endpoint | {{PRIMARY_ENDPOINT_URL}} |
| Discovery Endpoint | {{DISCOVERY_ENDPOINT_URL}} |
| Record Version | 1.0.0 |
| Spec Reference | IETF draft-narajala-ans-00, CNCF draft-liang-agentdns-00 |

## Protocol Adapters

| Protocol | Version | Endpoint | Auth | Status |
|----------|---------|----------|------|--------|
| {{PROTOCOL_1}} | {{VERSION_1}} | {{ENDPOINT_1}} | {{AUTH_1}} | active |
| {{PROTOCOL_2}} | {{VERSION_2}} | {{ENDPOINT_2}} | {{AUTH_2}} | active |

> Minimum 1 protocol-adapter required (H06). Target: 2+ for production ANS records.
> Supported protocols: mcp, a2a, grpc, http, websocket.

## Capability Advertisement

| Capability | Description |
|-----------|-------------|
| {{SKILL_1}} | {{SKILL_1_DESC}} |
| {{SKILL_2}} | {{SKILL_2_DESC}} |
| {{SKILL_3}} | {{SKILL_3_DESC}} |

**Concurrency**: max_concurrent = {{MAX_CONCURRENT}}

**Supported task types:**
- {{TASK_TYPE_1}}
- {{TASK_TYPE_2}}

**Performance**: response_time_p95_ms = {{P95_MS}} (optional)

## PKI Certificate

| Field | Value |
|-------|-------|
| Reference | `cert:{{CA_ISSUER}}:SHA256:{{FINGERPRINT}}` |
| Issuer | {{CA_ISSUER}} |
| Fingerprint (SHA256) | {{FINGERPRINT}} |
| Expires | {{CERT_EXPIRY_DATE}} |
| Required by | GoDaddy, Salesforce (production ANS registration) |

> PKI-cert enables mTLS authentication and satisfies A2A v0.3 security card signing.
> Omitting PKI-cert blocks GoDaddy and Salesforce production registration.

## Discovery Endpoint

| Field | Value |
|-------|-------|
| URL | {{DISCOVERY_ENDPOINT_URL}} |
| Convention | `https://{{ORG_DOMAIN}}/.well-known/agent/{{AGENT_LABEL}}` |
| Resolution method | HTTPS GET -- returns this registry-record as JSON |
| TTL (seconds) | {{TTL}} |
| CNCF AgentDNS compatible | Yes -- draft-liang-agentdns-00 |

> The discovery-endpoint is distinct from endpoint_url (H07).
> Other agents and orchestrators resolve this URL to locate and authenticate this agent.

## Lifecycle

| Field | Value |
|-------|-------|
| Registered | {{REGISTERED_DATE}} |
| Expires | {{EXPIRY_DATE}} |
| Renewal Policy | {{RENEWAL_POLICY}} |
| Last Verified | {{LAST_VERIFIED_DATE}} |
| Status | active |

```yaml
lifecycle:
  registered: "{{REGISTERED_DATE}}"
  expires: "{{EXPIRY_DATE}}"
  renewal_policy: {{RENEWAL_POLICY}}
  last_verified: "{{LAST_VERIFIED_DATE}}"
  status: active
```
```

---

## Placeholder Reference

| Placeholder | Description | Example |
|------------|-------------|---------|
| `{{ANS_NAME}}` | DNS-like ANS name (lowercase, `.agents` suffix) | `billing-bot.acme.agents` |
| `{{AGENT_SLUG}}` | Underscored version of ANS label for file ID | `billing_bot_acme` |
| `{{UUID_V4}}` | Generated UUID v4 for registry uniqueness | `550e8400-e29b-41d4-a716-446655440000` |
| `{{PRIMARY_ENDPOINT_URL}}` | Main HTTPS endpoint for agent communication | `https://agents.acme.com/billing` |
| `{{OPERATOR}}` | Registry operator enum value | `godaddy` |
| `{{PROTOCOL_1}}` | First protocol adapter name | `mcp` |
| `{{VERSION_1}}` | Protocol version | `2024-11-05` |
| `{{ENDPOINT_1}}` | Protocol-specific endpoint URL | `https://agents.acme.com/billing/mcp` |
| `{{AUTH_1}}` | Auth method for this protocol | `bearer` |
| `{{SKILL_1}}` | Capability identifier | `invoice-lookup` |
| `{{MAX_CONCURRENT}}` | Max concurrent tasks integer | `10` |
| `{{CA_ISSUER}}` | Certificate authority name | `letsencrypt` |
| `{{FINGERPRINT}}` | SHA256 certificate fingerprint | `AB12CD34EF56GH78` |
| `{{DISCOVERY_ENDPOINT_URL}}` | Well-known agent resolution URL | `https://acme.com/.well-known/agent/billing-bot` |
| `{{RENEWAL_POLICY}}` | Enum: auto, manual, none | `auto` |
| `{{REGISTERED_DATE}}` | ISO 8601 date | `2026-04-14` |
| `{{EXPIRY_DATE}}` | ISO 8601 date (typically +1 year) | `2027-04-14` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_agent_name_service_record]] | upstream | 0.66 |
| [[bld_system_prompt_agent_name_service_record]] | upstream | 0.60 |
| [[bld_knowledge_card_agent_name_service_record]] | upstream | 0.59 |
| [[bld_schema_agent_name_service_record]] | downstream | 0.57 |
| [[bld_examples_agent_name_service_record]] | downstream | 0.56 |
| [[bld_manifest_agent_name_service_record]] | upstream | 0.55 |
| [[bld_collaboration_agent_name_service_record]] | downstream | 0.53 |
| [[bld_tools_agent_name_service_record]] | upstream | 0.50 |
| [[bld_memory_agent_name_service_record]] | downstream | 0.49 |
| [[bld_quality_gate_agent_name_service_record]] | downstream | 0.48 |
