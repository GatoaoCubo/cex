---
kind: instruction
id: bld_instruction_agent_name_service_record
pillar: P03
llm_function: REASON
purpose: Step-by-step build phases for constructing IETF ANS/AgentDNS registry records
quality: null
title: "Agent Name Service Record Builder -- Instructions"
version: "1.0.0"
author: wave7_n05
tags: [agent_name_service_record, builder, instruction]
tldr: "3-phase build process: RESEARCH agent identity, COMPOSE registry-record, VALIDATE ANS/AgentDNS compliance"
domain: "agent_name_service_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

# Agent Name Service Record Builder -- Instructions

## Overview

Build an `agent_name_service_record` in 3 phases. Each phase has explicit inputs,
actions, and outputs. Do not skip phases -- Phase 1 data feeds Phase 2 composition.

## Phase 1: RESEARCH -- Resolve Agent Identity

**Goal**: Gather all facts needed before writing a single field.

### 1.1 Resolve ANS Name

| Step | Action | Output |
|------|--------|--------|
| 1.1.1 | Identify agent's human name or system identifier | raw_name string |
| 1.1.2 | Convert to DNS-like format: `{agent}.{org}.agents` (lowercase, hyphens only) | ans_name string |
| 1.1.3 | Verify no reserved words: `_dmarc`, `_well-known`, `_ans` | validation pass/fail |
| 1.1.4 | Check CNCF AgentDNS registry for name collision | collision: yes/no |

**ANS name format examples:**
- `customer-service.acme-corp.agents` -- valid
- `billing_agent.acme.agents` -- INVALID (underscore not allowed)
- `SUPPORT.Acme.agents` -- INVALID (must be lowercase)

### 1.2 Identify Supported Protocols

| Step | Action | Output |
|------|--------|--------|
| 1.2.1 | Check if agent exposes MCP server endpoint | mcp: yes/no + URL |
| 1.2.2 | Check if agent supports A2A protocol (v0.3+) | a2a: yes/no + URL |
| 1.2.3 | Check if agent exposes gRPC interface | grpc: yes/no + URL |
| 1.2.4 | Record protocol_adapters array with at least one entry | protocol_adapters[] |

**Minimum**: at least one protocol-adapter MUST be declared. A record with no adapters
fails H06 quality gate and cannot reach production status.

### 1.3 Gather PKI Certificate Reference

| Step | Action | Output |
|------|--------|--------|
| 1.3.1 | Locate agent's TLS/mTLS certificate or signing key reference | cert_path or cert_id |
| 1.3.2 | Confirm cert is from trusted CA (Let's Encrypt, DigiCert, internal PKI) | ca_name |
| 1.3.3 | Record PKI-cert reference as `cert:{issuer}:{fingerprint}` | pki_cert_reference string |
| 1.3.4 | Note expiry date for lifecycle block | cert_expires date |

**Note**: PKI-cert is optional per draft-narajala-ans-00 but REQUIRED for GoDaddy
and Salesforce production registration. Omitting it triggers H05 soft warning.

### 1.4 Enumerate Capability Endpoints

| Step | Action | Output |
|------|--------|--------|
| 1.4.1 | List agent's declared skills (max 10 for readability) | skills[] |
| 1.4.2 | Record max_concurrent tasks the agent can handle | max_concurrent int |
| 1.4.3 | List supported_tasks (task type identifiers) | supported_tasks[] |
| 1.4.4 | Identify primary discovery-endpoint URL | discovery_endpoint URL |

### 1.5 Check CNCF AgentDNS Compatibility

| Step | Action | Output |
|------|--------|--------|
| 1.5.1 | Confirm record structure matches draft-liang-agentdns-00 schema | compatible: yes/no |
| 1.5.2 | Identify registry_operator: godaddy / salesforce / cncf / other | registry_operator |
| 1.5.3 | Check if operator requires additional metadata fields | extra_fields[] |

---

## Phase 2: COMPOSE -- Populate Registry Record

**Goal**: Produce a complete, well-formed agent_name_service_record artifact.

### 2.1 Frontmatter Block

```yaml
---
kind: agent_name_service_record
id: p04_ans_{agent_slug}
pillar: P04
title: "ANS Record: {human_name}"
version: "1.0.0"
quality: null
agent_name: "{ans_name}"
registry_id: "{uuid_v4}"
endpoint_url: "{primary_endpoint}"
registry_operator: "{operator}"
created: "{YYYY-MM-DD}"
updated: "{YYYY-MM-DD}"
tags: [ANS, AgentDNS, IETF, CNCF, {operator}, {protocol_list}]
---
```

### 2.2 Body Sections (in order)

| Section | Required | Content |
|---------|----------|---------|
| ## Agent Identity | YES | ANS name, registry ID, operator, endpoint URL |
| ## Protocol Adapters | YES | Table of mcp/a2a/grpc with URLs and versions |
| ## Capability Advertisement | YES | Skills table, max_concurrent, supported_tasks |
| ## PKI Certificate | RECOMMENDED | Cert reference, issuer, fingerprint, expiry |
| ## Discovery Endpoint | YES | URL, resolution method, TTL |
| ## Lifecycle | YES | registered date, expires, renewal_policy |

### 2.3 Protocol Adapters Block

```markdown
## Protocol Adapters

| Protocol | Version | Endpoint | Status |
|----------|---------|----------|--------|
| mcp | 2024-11-05 | https://agent.example.com/mcp | active |
| a2a | 0.3 | https://agent.example.com/a2a | active |
| grpc | 1.0 | grpc://agent.example.com:50051 | optional |
```

### 2.4 Lifecycle Block

```yaml
lifecycle:
  registered: "YYYY-MM-DD"
  expires: "YYYY-MM-DD"
  renewal_policy: auto  # auto | manual | none
  last_verified: "YYYY-MM-DD"
```

---

## Phase 3: VALIDATE -- ANS/AgentDNS Compliance

**Goal**: Confirm all hard gates pass before the artifact is ready for registry submission.

### 3.1 Hard Gate Checklist

| Gate | Check | Pass condition |
|------|-------|----------------|
| H01 | Frontmatter valid YAML | All required fields present, no parse errors |
| H02 | ID pattern | Matches `^p04_ans_[a-z0-9_]+$` |
| H03 | kind field | Exactly `agent_name_service_record` |
| H04 | agent_name format | DNS-like: `{label}.{label}.agents` lowercase + hyphens |
| H05 | endpoint_url present | Valid HTTPS URL (not localhost) |
| H06 | protocol_adapters | At least one entry in array |
| H07 | discovery_endpoint | Present and distinct from endpoint_url |
| H08 | lifecycle.registered | Present and ISO 8601 date format |

### 3.2 Soft Quality Checks

| Dimension | Weight | Check |
|-----------|--------|-------|
| Name resolution quality | 0.25 | ANS name follows org.agents hierarchy |
| Protocol coverage | 0.25 | 2+ protocol adapters declared |
| PKI completeness | 0.20 | pki_cert_reference present with issuer + fingerprint |
| Capability richness | 0.20 | 3+ skills, max_concurrent >= 1, supported_tasks non-empty |
| Lifecycle completeness | 0.10 | expires + renewal_policy both present |

### 3.3 Post-Validation Actions

| Action | Command |
|--------|---------|
| Compile to YAML | `python _tools/cex_compile.py {path}` |
| Score artifact | `python _tools/cex_score.py --apply {path}` |
| Index for retrieval | `python _tools/cex_index.py` |
| Signal completion | `python -c "from _tools.signal_writer import write_signal; write_signal('n05', 'complete', 9.0)"` |
