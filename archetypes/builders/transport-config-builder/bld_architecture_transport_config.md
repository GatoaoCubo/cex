---
kind: architecture
id: bld_architecture_transport_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of transport_config -- inventory, dependencies
quality: 9.1
title: "Architecture Transport Config"
version: "1.1.0"
author: n04_hybrid_review2
tags: [transport_config, builder, architecture]
tldr: "Component map of transport_config -- inventory, dependencies"
domain: "transport_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
---

## Component Inventory

| Name | Role | Domain | Status |
|------|------|--------|--------|
| ICE Agent | WebRTC NAT traversal -- gathers host/srflx/relay candidates, runs connectivity checks | WebRTC | Active |
| STUN Client | Discovers server-reflexive address via STUN binding request/response | WebRTC | Active |
| TURN Relay | Allocates relay address for symmetric NAT traversal | WebRTC | Active |
| DTLS Handshaker | Establishes DTLS session to derive SRTP keys for media encryption | WebRTC | Active |
| WebSocket Framer | Encodes/decodes RFC 6455 frames -- opcodes, masking, extensions | WebSocket | Active |
| SSE Encoder | Serializes events into `data: ...\n\n` format, injects heartbeat comments | SSE | Active |
| gRPC Channel | HTTP/2-based bidirectional streaming channel with flow control | gRPC | Active |
| TLS Terminator | Handles TLS 1.3 handshake for WSS, HTTPS/SSE, gRPC connections | All | Active |
| Keepalive Monitor | Sends ping/PING frames, tracks pong/PONG responses, closes stale connections | WS+gRPC | Active |
| QoS Marker | Applies DSCP values to outgoing packets via IP TOS field | All | Active |

## Dependencies

| From | To | Type | Notes |
|------|----|------|-------|
| ICE Agent | STUN Client | required | Candidate gathering phase |
| ICE Agent | TURN Relay | optional | Fallback when direct path fails |
| DTLS Handshaker | ICE Agent | required | Needs ICE-selected candidate pair |
| WebSocket Framer | TLS Terminator | required | WSS only (plain WS skips TLS) |
| gRPC Channel | TLS Terminator | required | gRPC mandates TLS in production |
| SSE Encoder | TLS Terminator | required | SSE over HTTPS |
| Keepalive Monitor | WebSocket Framer | data | Injects ping/pong frames |
| Keepalive Monitor | gRPC Channel | data | Sends HTTP/2 PING frames |

## Architectural Position

`transport_config` sits at the infrastructure boundary of real-time communication systems.
It owns the packet-level transmission layer between application logic and the network.

```
[Application Layer]     <-- NOT transport_config scope
      |
[realtime_session]      <-- session lifecycle: connect/disconnect/auth
      |
[transport_config]      <-- THIS BUILDER: protocol params, ICE, TLS, keepalive, QoS
      |
[streaming_config]      <-- buffer sizes, chunking (adjacent, not owned here)
      |
[Network / OS / NIC]
```

Adjacent builders:
- `realtime_session_builder`: connection lifecycle, authentication, session state
- `streaming_config_builder`: buffer management, chunking, codec parameters
- `security_policy_builder`: certificate management, CA chains, rotation policies
