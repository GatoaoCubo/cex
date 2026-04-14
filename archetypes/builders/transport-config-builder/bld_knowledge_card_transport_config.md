---
kind: knowledge_card
id: bld_knowledge_card_transport_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for transport_config production
quality: 9.2
title: "Knowledge Card Transport Config"
version: "1.1.0"
author: n04_hybrid_review2
tags: [transport_config, builder, knowledge_card, webrtc, websocket, sse, grpc]
tldr: "Protocol coverage: WebRTC (SDP/ICE/STUN/TURN), WebSocket (RFC 6455), SSE, gRPC streaming, TCP/UDP/QUIC"
domain: "transport_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
---

## Domain Overview

Transport configuration defines how data traverses network boundaries — protocol selection,
connection establishment, NAT traversal, security, QoS, and flow control. Covers four primary
real-time transport families: WebRTC (browser-to-browser media), WebSocket (full-duplex
over HTTP), SSE (server-push event streams), and gRPC (HTTP/2 streaming RPC). Each has
distinct connection models, framing formats, and failure modes requiring separate config blocks.

The config_transport artifact governs: protocol-specific parameters (ICE candidates, stream
framing, keep-alive intervals), security (DTLS-SRTP, TLS 1.3), congestion control (QUIC BBR,
TCP CUBIC), QoS marking (DSCP), and NAT traversal (STUN/TURN server lists). Unlike
streaming_config (which governs buffer sizes and chunking) or realtime_session (which governs
connection lifecycle), transport_config owns the raw packet-level transmission parameters.

## WebRTC Transport

| Concept | Definition | RFC/Spec |
|---------|-----------|---------|
| SDP (Session Description Protocol) | Offer/answer negotiation of media codecs, ICE candidates, DTLS fingerprints | RFC 4566 |
| ICE (Interactive Connectivity Establishment) | NAT traversal framework — gathers host, server-reflexive, relay candidates | RFC 8445 |
| STUN | Server-reflexive address discovery for NAT traversal | RFC 5389 |
| TURN | Relay server fallback when direct path unavailable | RFC 5766 |
| DTLS-SRTP | DTLS handshake establishes SRTP keys for encrypted media | RFC 5764 |
| ICE Candidate Types | host (local NIC), srflx (STUN-reflected), relay (TURN) | RFC 8445 |
| Trickle ICE | Send ICE candidates incrementally during negotiation | RFC 8838 |
| Bundle Policy | Single transport for all tracks (max-bundle) vs. per-track | W3C WebRTC |
| RTCP | Control protocol alongside RTP — SSRC, jitter, loss reports | RFC 3550 |

**Config fields for WebRTC:**
- `ice_servers`: list of STUN/TURN URIs with credentials
- `ice_transport_policy`: "all" or "relay" (force TURN)
- `bundle_policy`: "max-bundle" | "balanced" | "max-compat"
- `rtcp_mux_policy`: "require" | "negotiate"
- `dtls_role`: "client" | "server" | "auto"
- `stun_urls`: array of `stun:host:port`
- `turn_urls`: array of `turn:host:port?transport=udp|tcp` with username/credential

## WebSocket Transport (RFC 6455)

| Concept | Definition | Source |
|---------|-----------|--------|
| HTTP Upgrade handshake | Sec-WebSocket-Key/Accept header exchange upgrades HTTP to WS | RFC 6455 §4 |
| Masking | Client-to-server frames MUST be masked with 4-byte key | RFC 6455 §5.3 |
| Frame opcodes | 0x1 text, 0x2 binary, 0x8 close, 0x9 ping, 0xA pong | RFC 6455 §5.2 |
| Subprotocols | Sec-WebSocket-Protocol negotiation (e.g., "mqtt", "graphql-ws") | RFC 6455 §1.9 |
| Extensions | Per-message deflate (RFC 7692), per-frame compression | RFC 7692 |
| Keep-alive | Ping/pong frames to detect stale connections | RFC 6455 §5.5 |
| Close handshake | Mutual close with status codes (1000=normal, 1001=going away) | RFC 6455 §7.4 |

**Config fields for WebSocket:**
- `ping_interval_ms`: frequency of ping frames (e.g., 30000)
- `ping_timeout_ms`: max wait for pong before closing
- `max_message_size_bytes`: prevent memory exhaustion
- `subprotocols`: negotiated application protocols
- `compression`: per-message deflate on/off + config
- `tls`: TLS 1.3 config for WSS connections

## SSE (Server-Sent Events)

| Concept | Definition | Source |
|---------|-----------|--------|
| Event stream format | `data: ...\n\n` with optional `id:`, `event:`, `retry:` fields | W3C SSE spec |
| Reconnection | Browser auto-reconnects with `Last-Event-ID` header | W3C SSE spec |
| Connection multiplexing | Single HTTP/2 stream per SSE channel | HTTP/2 RFC 9113 |
| Content-Type | Must be `text/event-stream; charset=utf-8` | W3C SSE spec |
| Heartbeat | Empty comment lines (`:\n\n`) keep connection alive through proxies | W3C SSE spec |

**Config fields for SSE:**
- `retry_ms`: client reconnect delay hint
- `heartbeat_interval_ms`: comment frequency (default 15000)
- `max_event_size_bytes`: limit per-event payload
- `buffer_timeout_ms`: server flush interval for event batching

## gRPC Streaming Transport

| Concept | Definition | Source |
|---------|-----------|--------|
| Server streaming | Client sends one request, server streams N responses | gRPC spec |
| Client streaming | Client streams N requests, server sends one response | gRPC spec |
| Bidirectional streaming | Both sides stream independently over single HTTP/2 stream | gRPC spec |
| Flow control | HTTP/2 WINDOW_UPDATE controls per-stream and connection-level | RFC 9113 |
| Keepalive pings | GRPC_ARG_KEEPALIVE_TIME_MS / GRPC_ARG_KEEPALIVE_TIMEOUT_MS | gRPC core |
| Max message size | GRPC_ARG_MAX_RECEIVE/SEND_MESSAGE_LENGTH | gRPC core |
| Deadlines | Per-call timeout propagated via grpc-timeout header | gRPC spec |
| Metadata | key: value headers sent before/after stream | gRPC spec |

**Config fields for gRPC:**
- `keepalive_time_ms`: interval between keepalive pings
- `keepalive_timeout_ms`: wait before closing unresponsive connection
- `max_receive_message_length`: per-message size cap
- `max_send_message_length`: per-message size cap
- `initial_window_size`: HTTP/2 flow control window
- `service_config`: retry/hedging/load-balancing policy (JSON)

## General Transport Concepts

| Concept | Definition | Source |
|---------|-----------|--------|
| MTU | Maximum Transmission Unit — largest packet before fragmentation | RFC 791 (IPv4), RFC 8200 (IPv6) |
| Congestion Control | BBR (bandwidth-delay product), CUBIC (loss-based), QUIC default | RFC 9002 (QUIC), Linux kernel |
| Jitter Buffer | Smooths packet arrival variance for real-time media | RFC 3550 (RTP) |
| FEC (Forward Error Correction) | Recover lost packets without retransmit | RFC 5144 |
| DSCP QoS Marking | DSCP EF (46) for voice, AF41 for video, CS0 for best-effort | RFC 2475 |
| Path MTU Discovery | Discover largest safe MTU on path | RFC 1981 (IPv6), RFC 1191 (IPv4) |
| Socket Buffer Sizes | SO_RCVBUF/SO_SNDBUF tuning for throughput | Linux kernel docs |
| TLS 1.3 | Mandatory for encrypted transports — 1-RTT handshake, AEAD ciphers | RFC 8446 |

## Industry Standards

| Standard | Domain | Key Clause |
|----------|--------|-----------|
| RFC 4566 | SDP | Session Description Protocol |
| RFC 8445 | ICE | NAT traversal for WebRTC |
| RFC 5389 | STUN | Server-reflexive address discovery |
| RFC 5766 | TURN | Relay for symmetric NAT |
| RFC 5764 | DTLS-SRTP | WebRTC media security |
| RFC 6455 | WebSocket | HTTP upgrade, framing, masking |
| RFC 7692 | WS permessage-deflate | WebSocket compression extension |
| RFC 9000 | QUIC | QUIC transport protocol |
| RFC 9002 | QUIC congestion | QUIC loss detection and congestion control |
| RFC 9113 | HTTP/2 | HTTP/2 framing (gRPC transport layer) |
| RFC 3550 | RTP/RTCP | Real-time transport protocol |
| RFC 8446 | TLS 1.3 | Transport Layer Security |
| RFC 2475 | DiffServ | QoS DSCP marking |
| W3C SSE | SSE | Server-Sent Events specification |

## Common Patterns

1. **WebRTC TURN fallback**: configure both STUN and TURN — STUN for direct path, TURN relay for symmetric NAT. Use `ice_transport_policy: relay` only in locked-down enterprise environments.
2. **WebSocket health check**: set `ping_interval_ms=30000`, `ping_timeout_ms=10000`. Proxies and load balancers may silently drop idle connections at 60s.
3. **gRPC keepalive**: configure `keepalive_time_ms=30000` on both client and server. Without this, HTTP/2 connections are dropped by stateful firewalls after ~4 min idle.
4. **SSE through proxies**: always include heartbeat comments (`:\n\n`) every 15s. Nginx and CloudFront buffer responses unless Transfer-Encoding: chunked is set and gzip is disabled.
5. **QoS marking**: mark WebRTC voice (DSCP 46/EF), WebRTC video (DSCP 34/AF41). Ignored by most cloud providers but critical in enterprise LANs.
6. **TLS for all**: WebSocket uses WSS (TLS 1.3), WebRTC uses DTLS-SRTP, gRPC uses TLS 1.3. Plain-text transport is a HARD gate failure.

## Pitfalls

- Configuring STUN-only without TURN fallback — fails behind symmetric NAT (~15% of users)
- Missing `bundle_policy: max-bundle` in WebRTC — creates multiple DTLS connections unnecessarily
- WebSocket max message size not set — enables OOM via single large frame
- gRPC missing deadlines — streaming calls hang indefinitely on server error
- SSE not setting `retry` field — browser default reconnect is 3s (may overwhelm server on restart)
- Assuming TLS is "application layer" — TLS terminates at transport layer (DTLS for DTLS-SRTP, TLS for WSS/gRPC)
