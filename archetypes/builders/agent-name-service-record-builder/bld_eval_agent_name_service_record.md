---
kind: quality_gate
id: bld_quality_gate_agent_name_service_record
pillar: P11
llm_function: GOVERN
purpose: Hard gates H01-H08 and soft scoring dimensions for agent_name_service_record artifacts
quality: 9.1
title: "Agent Name Service Record Builder -- Quality Gate"
version: "1.0.0"
author: wave7_n05
tags: [agent_name_service_record, builder, quality_gate]
tldr: "8 hard gates + 5 soft dimensions. Minimum 8.0 to publish, target 9.0+."
domain: "agent_name_service_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_agent_name_service_record
  - bld_system_prompt_agent_name_service_record
  - bld_examples_agent_name_service_record
  - bld_output_template_agent_name_service_record
  - bld_knowledge_card_agent_name_service_record
  - bld_schema_agent_name_service_record
  - bld_manifest_agent_name_service_record
  - bld_memory_agent_name_service_record
  - bld_collaboration_agent_name_service_record
  - p11_qg_quality_gate
---

## Quality Gate

# Agent Name Service Record Builder -- Quality Gate

> Governs IETF ANS / CNCF AgentDNS registry-record quality. Hard gates enforce DNS-like name format, protocol-adapter presence, discovery-endpoint validity. Soft dimensions score PKI-cert + capability richness for GoDaddy, Salesforce, CNCF operators.

## Hard Gates (H01-H08)

All 8 must pass. Any failure blocks publication.

| ID | Gate | Check | Pass | Fix |
|----|------|-------|------|-----|
| H01 | Frontmatter | YAML parses | No errors, required fields present | Fix YAML |
| H02 | ID pattern | Regex on `id` | `^p04_ans_[a-z0-9_]+$` | Rename |
| H03 | Kind | String match | `kind=="agent_name_service_record"` | Correct |
| H04 | ANS name | DNS-like | lowercase, hyphens, ends `.agents`, no underscores | Reformat |
| H05 | Endpoint | URL check | HTTPS, not localhost, not empty | Add prod URL |
| H06 | Adapters | Array size | `protocol_adapters` >=1 | Declare MCP/A2A/gRPC |
| H07 | Discovery | Field + URL | `discovery_endpoint` present, HTTPS | Add well-known URL |
| H08 | Lifecycle | Date format | `lifecycle.registered` ISO 8601 | Add date |

**Logic**: H01 -> H08 sequential. Any FAIL -> BLOCK (do not publish). ALL PASS -> soft scoring.

## Soft Scoring Dimensions (5D)

**Used when all hard gates pass. Weighted sum targets 9.0+**

### D1: Name Resolution Quality (weight: 0.25)

| Score | Condition |
|-------|-----------|
| 1.0 | ANS name follows `{agent}.{org}.agents` 3-segment hierarchy, org matches registry_operator domain |
| 0.8 | 3-segment hierarchy correct, org does not clearly match registry_operator |
| 0.6 | 2-segment hierarchy (missing org segment) |
| 0.4 | 1 segment only, but lowercase and ends in `.agents` |
| 0.0 | Name fails DNS-like format (uppercase, underscore, wrong suffix) |

### D2: Protocol Coverage (weight: 0.25)

| Score | Condition |
|-------|-----------|
| 1.0 | 3+ protocol adapters declared (e.g., MCP + A2A + gRPC) |
| 0.8 | 2 protocol adapters declared (e.g., MCP + A2A) |
| 0.6 | 1 protocol adapter, current version pinned |
| 0.4 | 1 protocol adapter, version not specified |
| 0.0 | No protocol adapters (should have failed H06) |

### D3: PKI Completeness (weight: 0.20)

| Score | Condition |
|-------|-----------|
| 1.0 | PKI-cert reference present with issuer + SHA256 fingerprint, expiry in lifecycle |
| 0.8 | PKI-cert reference present, issuer only (no fingerprint) |
| 0.6 | PKI-cert field present but value is placeholder or empty string |
| 0.2 | PKI-cert field absent but record is for non-production operator (`self`) |
| 0.0 | PKI-cert field absent for GoDaddy or Salesforce registry operator |

### D4: Capability Richness (weight: 0.20)

| Score | Condition |
|-------|-----------|
| 1.0 | 3+ skills, max_concurrent >= 1, supported_tasks non-empty, response_time_p95_ms present |
| 0.8 | 3+ skills, max_concurrent >= 1, supported_tasks non-empty |
| 0.6 | 1-2 skills, max_concurrent present |
| 0.4 | skills array present but empty |
| 0.0 | capability_advertisement block absent entirely |

### D5: Lifecycle Completeness (weight: 0.10)

| Score | Condition |
|-------|-----------|
| 1.0 | registered + expires + renewal_policy + last_verified all present |
| 0.8 | registered + expires + renewal_policy present |
| 0.6 | registered + expires present, renewal_policy missing |
| 0.4 | registered only |
| 0.0 | lifecycle block absent (should have failed H08) |

## Scoring Formula

```
raw_score = (D1 * 0.25) + (D2 * 0.25) + (D3 * 0.20) + (D4 * 0.20) + (D5 * 0.10)
final_score = raw_score * 10
```

**Thresholds:**

| Score | Status | Action |
|-------|--------|--------|
| 9.0 - 10.0 | PUBLISH | Ready for registry submission |
| 8.0 - 8.9 | PUBLISH with warning | Acceptable, note soft gaps |
| 7.0 - 7.9 | REVISE | Return to Phase 2 COMPOSE, address D1+D2+D3 gaps |
| < 7.0 | REJECT | Full rebuild required -- review instruction ISO |

## Common Failure Patterns

| Failure | Root cause | Fix |
|---------|-----------|-----|
| H04 fail: ANS name has underscore | agent_slug copied from Python variable name | Replace `_` with `-` |
| H06 fail: no protocol adapters | Builder skipped Phase 1.2 | Go back to instruction ISO Phase 1.2 |
| D3 = 0.0: missing PKI-cert for GoDaddy | Forgot GoDaddy requirement | Add PKI-cert reference from secret_config |
| D4 < 0.6: empty skills | capability_advertisement block not populated | Enumerate at least 3 skills from agent spec |
| D2 = 0.6: only 1 protocol | Agent only exposes HTTP endpoint | Investigate if MCP server is available |

## Tooling

| Tool | Command | When |
|------|---------|------|
| Score artifact | `python _tools/cex_score.py --apply {path}` | After Phase 3 VALIDATE |
| Check gates only | `python _tools/cex_score.py --gates-only {path}` | Quick validation during composition |
| Doctor check | `python _tools/cex_doctor.py` | Full system health post-build |

## Examples

# Agent Name Service Record Builder -- Examples

## Golden Example: GoDaddy Customer-Service Agent

**Scenario**: Production ANS registry-record for a GoDaddy customer-service agent with MCP + A2A adapters, valid PKI-cert, 3 capabilities, and a CNCF AgentDNS discovery-endpoint. Salesforce MuleSoft Agent Fabric follows the same pattern. Passes all 8 hard gates; 9.5+ soft.

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
| Operator | GoDaddy (prod ANS, Feb 2026) |
| Primary Endpoint | https://agents.godaddy.com/customer-service |
| Discovery | https://godaddy.com/.well-known/agent/customer-service |
| Version | 1.0.0 |
| Spec | IETF draft-narajala-ans-00, CNCF draft-liang-agentdns-00 |
## Protocol Adapters
| Protocol | Version | Endpoint | Auth | Status |
|----------|---------|----------|------|--------|
| mcp | 2024-11-05 | https://agents.godaddy.com/customer-service/mcp | bearer | active |
| a2a | 0.3 | https://agents.godaddy.com/customer-service/a2a | mtls | active |
## Capability Advertisement
| Capability | Description |
|-----------|-------------|
| account-lookup | Retrieve customer account by domain or ID |
| billing-dispute | Accept + route billing disputes |
| domain-transfer-status | Check status of in-progress transfers |
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
| Resolution | HTTPS GET -> registry-record JSON |
| TTL (s) | 3600 |
| CNCF AgentDNS | draft-liang-agentdns-00 |
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
## Anti-Example 1: Invalid ANS Name Format

**What went wrong**: Name uses underscores instead of hyphens. Fails H04; invalid per IETF draft-narajala-ans-00.

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

**Lesson**: ANS names follow DNS label syntax (RFC 1035): lowercase, hyphens only. snake_case does not apply.
## Anti-Example 2: Missing Protocol Adapters

**What went wrong**: Only an endpoint URL; no protocol-adapter entries. Useless -- no way to know how to connect.

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

**Fix**: Add >=1 protocol-adapter (mcp|a2a), a capability_advertisement, and optionally a PKI-cert.

**Lesson**: A raw endpoint URL is NOT an ANS record. It must declare HOW to connect (adapter), WHAT the agent does (capabilities), and WHO speaks (PKI-cert). Without these: dead URL.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
