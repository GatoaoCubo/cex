---
kind: tools
id: bld_tools_agent_name_service_record
pillar: P04
llm_function: CALL
purpose: Tool inventory for building, validating, and publishing IETF ANS registry records
quality: 9.1
title: "Agent Name Service Record Builder -- Tools"
version: "1.0.0"
author: wave7_n05
tags: [agent_name_service_record, builder, tools, ANS, IETF, CNCF]
tldr: "CEX tools for compile/score/index + external IETF ANS and CNCF AgentDNS spec references"
domain: "agent_name_service_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

# Agent Name Service Record Builder -- Tools

> Tool inventory for building IETF ANS / CNCF AgentDNS registry-records.
> Covers CEX production tools (compile, score, index) and external spec references
> for protocol-adapter versions (MCP, A2A) and PKI-cert infrastructure.
> Supports GoDaddy, Salesforce, and CNCF registry operators.

## Production Tools (CEX)

| Tool | Command | When to use | Output |
|------|---------|-------------|--------|
| cex_compile.py | `python _tools/cex_compile.py {path}` | After F6 PRODUCE -- compiles .md to .yaml | .yaml artifact in same directory |
| cex_score.py | `python _tools/cex_score.py --apply {path}` | After F7 GOVERN -- scores artifact | Score annotation in frontmatter |
| cex_retriever.py | `python _tools/cex_retriever.py --query "ANS registry"` | F3 INJECT -- find similar ANS records | Ranked list of existing records |
| cex_index.py | `python _tools/cex_index.py` | F8 COLLABORATE -- update search index | Index updated |
| signal_writer.py | See command below | F8 COLLABORATE -- signal completion | Signal file written |

**Signal command:**
```python
python -c "from _tools.signal_writer import write_signal; write_signal('n05', 'complete', 9.0)"
```

## Validation Tools

| Tool | Command | Check | Exit code |
|------|---------|-------|---------|
| cex_doctor.py | `python _tools/cex_doctor.py` | Full system health | 0 = healthy |
| cex_sanitize.py | `python _tools/cex_sanitize.py --check --scope P04_tools/` | ASCII compliance | 0 = clean |
| cex_score.py --gates-only | `python _tools/cex_score.py --gates-only {path}` | Hard gates H01-H08 only | 0 = all pass |
| bash wc | `wc -c {path}` | Byte count <= 3072 | -- |

## Quality Workflow

```
[artifact written]
       |
       v
cex_compile.py      -- compile .md to .yaml (F8)
       |
       v
cex_score.py --gates-only    -- quick gate check (H01-H08)
       |
  all pass?
  NO --> fix artifact, re-run
  YES -->
       |
       v
cex_score.py --apply    -- full scoring (5D soft dimensions)
       |
  score >= 8.0?
  NO --> return to F6 PRODUCE, improve weakest dimension
  YES -->
       |
       v
cex_sanitize.py --check    -- confirm ASCII compliance
       |
       v
git add + git commit    -- version the artifact
       |
       v
write_signal    -- notify orchestrator
```

## External References

### IETF ANS Specification

| Resource | URL / Reference | Notes |
|---------|----------------|-------|
| IETF draft-narajala-ans-00 | IETF Datatracker (search: draft-narajala-ans) | Core ANS protocol, DNS-like naming, registry-record format |
| ANS DNS-like name format | RFC 1035 (DNS label syntax) -- ANS reuses this | Lowercase, hyphens, max 63 chars per label |
| Well-known URIs | RFC 8615 -- `/.well-known/` URI convention | Base for discovery-endpoint pattern |

### CNCF AgentDNS

| Resource | URL / Reference | Notes |
|---------|----------------|-------|
| CNCF draft-liang-agentdns-00 | CNCF GitHub / CNCF Datatracker (search: agentdns) | Cloud-native AgentDNS, Kubernetes-native registry |
| CNCF Cloud Native Agentic Standards | CNCF GitHub (working group formed Mar 2026) | Broader agentic standards initiative |

### Protocol Adapter Specs

| Protocol | Version | Source | Notes |
|----------|---------|--------|-------|
| MCP (Model Context Protocol) | 2024-11-05 | Anthropic MCP server identity spec (Nov 2025) | Server identity, capability advertisement pattern |
| A2A (Agent-to-Agent) | 0.3 | Google A2A v0.3 specification | Security card signing, inter-agent auth |
| gRPC | 1.0 | grpc.io -- standard gRPC spec | Binary RPC, Protobuf-based |

### Production Integrations

| Integration | Organization | Date | Notes |
|-----------|-------------|------|-------|
| GoDaddy ANS registry | GoDaddy Inc. | Feb 2026 | First production ANS registry operator |
| Salesforce MuleSoft Agent Fabric | Salesforce | Feb 2026 | Enterprise ANS + A2A integration |
| CNCF AgentDNS pilot | CNCF | Mar 2026 | Cloud-native registry pilot |

## Tool Usage by 8F Stage

| 8F Stage | Tool used | Purpose |
|----------|----------|---------|
| F1 CONSTRAIN | cex_retriever.py | Find existing ANS records for reference |
| F3 INJECT | cex_retriever.py | Semantic search for similar registry patterns |
| F5 CALL | cex_score.py --gates-only | Quick gate validation mid-build |
| F7 GOVERN | cex_score.py --apply | Full quality scoring |
| F7 GOVERN | cex_sanitize.py --check | ASCII compliance check |
| F8 COLLABORATE | cex_compile.py | Compile to YAML |
| F8 COLLABORATE | cex_index.py | Update search index |
| F8 COLLABORATE | signal_writer.py | Completion signal |
| F8 COLLABORATE | cex_doctor.py | Post-build health check |

## Git Commit Convention

```bash
git commit -m "[N05] ANS record: {ans_name} -- {registry_operator} ({protocol_list})"

# Examples:
# [N05] ANS record: billing-bot.acme.agents -- godaddy (mcp, a2a)
# [N05] ANS record: support.example.agents -- cncf (mcp)
# [N05] ANS record: crm-sync.salesforce.agents -- salesforce (a2a)
```
