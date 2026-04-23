---
kind: instruction
id: bld_instruction_agent_name_service_record
pillar: P03
llm_function: REASON
purpose: Step-by-step build phases for constructing IETF ANS/AgentDNS registry records
quality: 9.1
title: "Agent Name Service Record Builder -- Instructions"
version: "1.0.0"
author: wave7_n05
tags: [agent_name_service_record, builder, instruction]
tldr: "3-phase build process: RESEARCH agent identity, COMPOSE registry-record, VALIDATE ANS/AgentDNS compliance"
domain: "agent_name_service_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_output_template_agent_name_service_record
  - bld_schema_agent_name_service_record
  - bld_quality_gate_agent_name_service_record
  - bld_system_prompt_agent_name_service_record
  - bld_examples_agent_name_service_record
  - bld_knowledge_card_agent_name_service_record
  - bld_manifest_agent_name_service_record
  - bld_collaboration_agent_name_service_record
  - bld_memory_agent_name_service_record
  - bld_tools_agent_name_service_record
---
# Agent Name Service Record Builder -- Instructions
## Overview
Build an `agent_name_service_record` in 3 phases. Phase 1 feeds Phase 2; do not skip.
## Phase 1: RESEARCH -- Resolve Agent Identity

**Goal**: Gather all facts needed before writing a single field.

### 1.1 Resolve ANS Name

| Step | Action | Output |
|------|--------|--------|
| 1.1.1 | Identify agent's human or system name | raw_name |
| 1.1.2 | Convert to `{agent}.{org}.agents` (lowercase, hyphens) | ans_name |
| 1.1.3 | Verify no reserved words (`_dmarc`, `_well-known`, `_ans`) | pass/fail |
| 1.1.4 | Check CNCF AgentDNS for collision | yes/no |

**Examples**: `customer-service.acme-corp.agents` (valid); `billing_agent.acme.agents` (INVALID: underscore); `SUPPORT.Acme.agents` (INVALID: must be lowercase).

### 1.2 Identify Supported Protocols

| Step | Action | Output |
|------|--------|--------|
| 1.2.1 | MCP server endpoint? | mcp:y/n+URL |
| 1.2.2 | A2A v0.3+? | a2a:y/n+URL |
| 1.2.3 | gRPC? | grpc:y/n+URL |
| 1.2.4 | Record adapters array (>=1) | protocol_adapters[] |

**Minimum**: >=1 protocol-adapter required. Zero adapters = H06 fail, blocks production.

### 1.3 Gather PKI Certificate Reference

| Step | Action | Output |
|------|--------|--------|
| 1.3.1 | Locate TLS/mTLS cert or signing-key ref | cert_path|id |
| 1.3.2 | Confirm trusted CA (LE, DigiCert, internal) | ca_name |
| 1.3.3 | Record ref as `cert:{issuer}:{fingerprint}` | pki_cert_reference |
| 1.3.4 | Note expiry for lifecycle block | cert_expires |

**Note**: PKI-cert is optional in draft-narajala-ans-00 but REQUIRED for GoDaddy/Salesforce prod. Omission = H05 soft warning.

### 1.4 Enumerate Capability Endpoints

| Step | Action | Output |
|------|--------|--------|
| 1.4.1 | List declared skills (max 10) | skills[] |
| 1.4.2 | Record max_concurrent | int |
| 1.4.3 | List supported_tasks (type IDs) | supported_tasks[] |
| 1.4.4 | Identify primary discovery-endpoint | URL |

### 1.5 Check CNCF AgentDNS Compatibility

| Step | Action | Output |
|------|--------|--------|
| 1.5.1 | Confirm record structure matches draft-liang-agentdns-00 schema | compatible: yes/no |
| 1.5.2 | Identify registry_operator: godaddy / salesforce / cncf / other | registry_operator |
| 1.5.3 | Check if operator requires additional metadata fields | extra_fields[] |
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
## Phase 3: VALIDATE -- ANS/AgentDNS Compliance

**Goal**: Confirm all hard gates pass before registry submission.

### 3.1 Hard Gate Checklist

| Gate | Check | Pass condition |
|------|-------|----------------|
| H01 | Frontmatter valid YAML | Required fields present, no parse errors |
| H02 | ID pattern | `^p04_ans_[a-z0-9_]+$` |
| H03 | kind | `agent_name_service_record` |
| H04 | agent_name | DNS-like `{label}.{label}.agents` lowercase+hyphens |
| H05 | endpoint_url | Valid HTTPS (not localhost) |
| H06 | protocol_adapters | >=1 entry |
| H07 | discovery_endpoint | Present, distinct from endpoint_url |
| H08 | lifecycle.registered | ISO 8601 date |

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


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_agent_name_service_record]] | downstream | 0.57 |
| [[bld_schema_agent_name_service_record]] | downstream | 0.56 |
| [[bld_quality_gate_agent_name_service_record]] | downstream | 0.51 |
| [[bld_system_prompt_agent_name_service_record]] | related | 0.50 |
| [[bld_examples_agent_name_service_record]] | downstream | 0.50 |
| [[bld_knowledge_card_agent_name_service_record]] | upstream | 0.49 |
| [[bld_manifest_agent_name_service_record]] | downstream | 0.48 |
| [[bld_collaboration_agent_name_service_record]] | downstream | 0.44 |
| [[bld_memory_agent_name_service_record]] | downstream | 0.41 |
| [[bld_tools_agent_name_service_record]] | downstream | 0.41 |
