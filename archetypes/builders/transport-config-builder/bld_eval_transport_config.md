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
related:
  - bld_examples_transport_config
  - bld_output_template_transport_config
  - p03_sp_transport_config_builder
  - bld_schema_transport_config
  - hybrid_review2_n04
  - bld_knowledge_card_transport_config
  - bld_architecture_transport_config
  - bld_knowledge_card_realtime_session
  - p10_lr_transport_config_builder
  - transport-config-builder
---

## Quality Gate
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

## Examples
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
