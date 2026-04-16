---
kind: schema
id: bld_schema_agent_name_service_record
pillar: P06
llm_function: CONSTRAIN
purpose: Field definitions and validation rules for the agent_name_service_record kind
quality: 9.1
title: "Agent Name Service Record Builder -- Schema"
version: "1.0.0"
author: wave7_n05
tags: [agent_name_service_record, builder, schema]
tldr: "Complete field schema for IETF ANS + CNCF AgentDNS registry-record artifacts"
domain: "agent_name_service_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

# Agent Name Service Record Builder -- Schema

## Top-Level Fields

| Field | Type | Required | Validation | Description |
|-------|------|----------|-----------|-------------|
| kind | string | YES | `agent_name_service_record` | Fixed value -- identifies artifact type |
| id | string | YES | `^p04_ans_[a-z0-9_]+$` | Pillar-prefixed unique ID |
| pillar | string | YES | `P04` | Fixed -- CALL pillar |
| title | string | YES | Non-empty | Human-readable record title |
| version | string | YES | Semver `\d+\.\d+\.\d+` | Artifact version |
| quality | null | YES | Must be null | Peer-review assigned only |
| agent_name | string | YES | DNS-like format (see below) | Canonical ANS name for this agent |
| registry_id | string | YES | UUID v4 format | Unique registry entry identifier |
| endpoint_url | string | YES | Valid HTTPS URL | Primary agent communication endpoint |
| registry_operator | string | YES | Enum (see below) | Organization operating this registry entry |
| created | string | YES | ISO 8601 date | Record creation date |
| updated | string | YES | ISO 8601 date | Last modification date |
| tags | array | YES | Non-empty | Searchability keywords |

## agent_name Field

**Format**: `{agent-label}.{org-label}.agents`

| Rule | Valid | Invalid |
|------|-------|---------|
| lowercase alphanumeric + hyphens | `billing-bot` | `billing_bot` |
| `.` separator only | `billing-bot.acme.agents` | `billing-bot/acme/agents` |
| Suffix `.agents` | `support.corp.agents` | `support.corp.ai` |
| All lowercase | `crm.example.agents` | `CRM.Example.Agents` |
| Each label 1-63 chars | `a.b.agents` | (63+ char label) |
| No reserved labels | any other | `_ans.corp.agents` |

## registry_operator Enum

| Value | Organization | Notes |
|-------|-------------|-------|
| `godaddy` | GoDaddy Inc. | Production ANS integration since Feb 2026 |
| `salesforce` | Salesforce MuleSoft Agent Fabric | Production integration since Feb 2026 |
| `cncf` | CNCF AgentDNS registry | Cloud-native default |
| `self` | Self-hosted registry | Requires discovery-endpoint public URL |
| `other` | Custom operator | Must document operator URL |

## protocol_adapters Array

**Minimum cardinality**: 1 entry. Each entry is a protocol-adapter object:

| Field | Type | Required | Validation |
|-------|------|----------|-----------|
| protocol | string | YES | Enum: `mcp`, `a2a`, `grpc`, `http`, `websocket` |
| version | string | YES | Protocol version string |
| endpoint | string | YES | Full URL for this protocol |
| status | string | YES | Enum: `active`, `deprecated`, `experimental` |
| auth | string | NO | Auth method: `bearer`, `mtls`, `apikey`, `none` |

**Protocol version references:**

| Protocol | Current version | Source |
|----------|----------------|--------|
| mcp | 2024-11-05 | MCP server identity spec Nov 2025 |
| a2a | 0.3 | A2A v0.3 spec with security card signing |
| grpc | 1.0 | gRPC standard |

## pki_cert_reference Field

`pki_cert_reference: string, RECOMMENDED, format `cert:{issuer}:{fingerprint}` -- PKI-cert binding.

Examples: `cert:letsencrypt:SHA256:AB12CD34` | `cert:digicert:SHA256:EF56GH78` | `cert:internal-pki:SHA256:IJ90KL12`.

**Omitting**: allowed per draft-narajala-ans-00 but blocks GoDaddy + Salesforce prod registration. Soft warning.

## capability_advertisement Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| skills | array of strings | YES | List of capability identifiers (max 10) |
| max_concurrent | integer | YES | Maximum simultaneous tasks the agent handles |
| supported_tasks | array of strings | YES | Task type identifiers the agent accepts |
| response_time_p95_ms | integer | NO | 95th percentile response time in milliseconds |
| context_window_tokens | integer | NO | Max context window if applicable |

## discovery_endpoint Field

`discovery_endpoint: string, YES, HTTPS URL -- well-known URL for runtime resolution.`

**Convention**: `https://{org-domain}/.well-known/agent/{agent-label}`. MUST differ from `endpoint_url`. Serves registry-record JSON for runtime discovery by agents + orchestrators.

## lifecycle Object

| Field | Type | Required | Format | Description |
|-------|------|----------|--------|-------------|
| registered | string | YES | ISO 8601 date | Date the agent was first registered |
| expires | string | RECOMMENDED | ISO 8601 date | Record expiry date |
| renewal_policy | string | RECOMMENDED | Enum | `auto`, `manual`, `none` |
| last_verified | string | NO | ISO 8601 date | Last live health check date |
| status | string | NO | Enum | `active`, `suspended`, `deprecated` |

## Complete Example (Minimal Valid Record)

```yaml
kind: agent_name_service_record
id: p04_ans_billing_bot_acme
pillar: P04
title: "ANS Record: billing-bot.acme.agents"
version: "1.0.0"
quality: null
agent_name: "billing-bot.acme.agents"
registry_id: "550e8400-e29b-41d4-a716-446655440000"
endpoint_url: "https://agents.acme.com/billing"
registry_operator: "godaddy"
created: "2026-04-14"
updated: "2026-04-14"
tags: [ANS, AgentDNS, IETF, CNCF, mcp, a2a]
protocol_adapters:
  - protocol: mcp
    version: "2024-11-05"
    endpoint: "https://agents.acme.com/billing/mcp"
    status: active
pki_cert_reference: "cert:letsencrypt:SHA256:AB12CD34"
discovery_endpoint: "https://acme.com/.well-known/agent/billing-bot"
lifecycle:
  registered: "2026-04-14"
  expires: "2027-04-14"
  renewal_policy: auto
```
