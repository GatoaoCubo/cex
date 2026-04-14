---
kind: quality_gate
id: p09_qg_transport_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for transport_config
quality: 9.0
title: "Quality Gate Transport Config"
version: "1.1.0"
author: n04_hybrid_review2
tags: [transport_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for transport_config"
domain: "transport_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

## Definition

| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| TLS version | >= 1.2 | >= | All encrypted transports |
| WebRTC TURN server | >= 1 | >= | WebRTC configs |
| Keepalive / heartbeat | defined | present | WebSocket, gRPC, SSE |
| Message size limit | defined | present | WebSocket, gRPC |
| QoS markings | defined | present | Latency-sensitive configs |

## HARD Gates

| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML valid | Invalid YAML syntax |
| H02 | ID matches pattern | ID does not match `^p09_tc_[a-z0-9_]+$` |
| H03 | kind matches | kind != "transport_config" |
| H04 | TLS version | TLS/DTLS version < 1.2 |
| H05 | Transport type declared | transport_type field missing or empty |
| H06 | WebRTC: TURN present | WebRTC config has no TURN server (STUN-only blocked) |
| H07 | Mandatory protocol fields | Missing required fields for declared transport_type |

## SOFT Scoring (5D)

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|--------------|
| D1 | Protocol completeness | 0.30 | All mandatory fields for transport_type: 1.0; partial: 0.5; minimal: 0.2 |
| D2 | Security configuration | 0.25 | TLS 1.3 + proper certs + DTLS-SRTP: 1.0; TLS 1.2: 0.7; no TLS: 0.0 |
| D3 | Resilience / reconnection | 0.20 | Keepalive + retry policy + timeout defined: 1.0; partial: 0.5; none: 0.0 |
| D4 | QoS and performance | 0.15 | DSCP + limits + congestion control: 1.0; partial: 0.5; none: 0.2 |
| D5 | Documentation quality | 0.10 | tldr + notes + inline comments: 1.0; tldr only: 0.5; none: 0.0 |

## Actions

| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN: auto-approve, add to examples library |
| >= 8.0 | PUBLISH: deploy to production |
| >= 7.0 | REVIEW: manual check before deploy |
| < 7.0 | REJECT: rework required |

## Bypass

| Condition | Approver | Audit Trail |
|-----------|----------|------------|
| Emergency fix with known risk | Senior Engineer | Log reason, timestamp, PID |
| Legacy system lacking TLS support | Architecture Lead | Log reason + migration ticket |
| Third-party API constraint | Tech Lead | Log reason + external ticket ref |
