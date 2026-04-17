---
kind: examples
id: bld_examples_transport_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of transport_config artifacts
quality: 9.0
title: "Examples Transport Config"
version: "1.1.0"
author: n04_hybrid_review2
tags: [transport_config, builder, examples, webrtc, websocket, grpc]
tldr: "Golden and anti-examples of transport_config artifacts"
domain: "transport_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

## Golden Example 1: WebRTC Media Transport

```yaml
---
id: p09_tc_webrtc_media
kind: transport_config
pillar: P09
title: "WebRTC Media Transport - Production"
version: "1.0.0"
transport_type: webrtc
protocol: dtls-srtp
created: "2026-04-13"
author: "n04"
domain: "video_conferencing"
quality: null
tags: [transport_config, webrtc, dtls-srtp]
tldr: "WebRTC transport with STUN+TURN, max-bundle, DSCP QoS"
---

transport_type: webrtc
protocol: dtls-srtp

ice_servers:
  - urls: ["stun:stun.example.com:3478"]
  - urls:
      - "turn:turn.example.com:3478?transport=udp"
      - "turn:turn.example.com:5349?transport=tcp"
    username: "alice"
    credential: "${TURN_CREDENTIAL}"

ice_transport_policy: "all"
bundle_policy: "max-bundle"
rtcp_mux_policy: "require"
dtls_role: "auto"

qos:
  dscp_audio: 46      # EF for voice (<20ms jitter target)
  dscp_video: 34      # AF41 for video
  dscp_data: 0

tls:
  min_version: "1.2"
  preferred_version: "1.3"
  dtls_fingerprint_algorithm: "sha-256"

notes: "Force relay with ice_transport_policy: relay in restrictive enterprise firewalls"
```

## Golden Example 2: WebSocket Event Stream

```yaml
---
id: p09_tc_ws_events
kind: transport_config
pillar: P09
title: "WebSocket Event Transport"
version: "1.0.0"
transport_type: websocket
protocol: rfc6455
created: "2026-04-13"
author: "n04"
domain: "realtime_api"
quality: null
tags: [transport_config, websocket]
tldr: "WebSocket config with keepalive, compression, retry backoff"
---

transport_type: websocket
protocol: rfc6455

endpoint: "wss://api.example.com:443/events"
subprotocols: ["v4.json.example.com"]

keepalive:
  ping_interval_ms: 30000
  ping_timeout_ms: 10000
  max_missed_pings: 2

framing:
  max_message_size_bytes: 1048576
  compression:
    enabled: true
    algorithm: "permessage-deflate"

tls:
  version: "1.3"
  verify_peer: true

reconnect:
  initial_delay_ms: 1000
  max_delay_ms: 30000
  backoff_multiplier: 2.0
  max_attempts: 10

notes: "Subprotocol negotiated during Upgrade handshake via Sec-WebSocket-Protocol"
```

## Anti-Example 1: WebRTC Without TURN

```yaml
---
id: p09_tc_stun_only
kind: transport_config
transport_type: webrtc
---
ice_servers:
  - urls: ["stun:stun.l.google.com:19302"]
```

**Why it fails:**
STUN-only configuration fails behind symmetric NAT (~15% of enterprise users). Without TURN
relay servers, connectivity checks will fail silently. H06 HARD gate REJECTS this config.
Always pair STUN with at least one TURN server.

## Anti-Example 2: WebSocket Without Message Size Limit

```yaml
---
id: p09_tc_ws_no_limit
kind: transport_config
transport_type: websocket
---
endpoint: "wss://api.example.com/stream"
keepalive:
  ping_interval_ms: 30000
```

**Why it fails:**
Missing `max_message_size_bytes`. A single WebSocket frame can be up to 2^63 bytes by protocol
spec. Without a server-side limit, a malicious client can OOM the server with one message.
Also missing reconnect policy -- if the WSS connection drops, the client has no guidance on
retry behavior.

## Anti-Example 3: Session State Pollution

```yaml
---
id: p09_tc_grpc_polluted
kind: transport_config
transport_type: grpc_streaming
---
server_endpoint: "inference.example.com:443"
session_token: "Bearer eyJ..."
user_id: "user_123"
auth_callback_url: "https://auth.example.com/refresh"
```

**Why it fails:**
`session_token`, `user_id`, and `auth_callback_url` belong to `realtime_session` kind.
Transport config owns protocol parameters only. Session authentication and lifecycle are
a different boundary. Mixing them creates coupling that prevents session rotation without
transport config changes.
