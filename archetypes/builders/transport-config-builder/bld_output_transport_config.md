---
kind: output_template
id: bld_output_template_transport_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for transport_config production
quality: 9.0
title: "Output Template Transport Config"
version: "1.1.0"
author: n04_hybrid_review2
tags: [transport_config, builder, output_template]
tldr: "Template with vars for transport_config production — WebRTC/WebSocket/SSE/gRPC variants"
domain: "transport_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_examples_transport_config
  - bld_schema_transport_config
  - p09_qg_transport_config
  - p03_sp_transport_config_builder
  - bld_knowledge_card_transport_config
  - hybrid_review2_n04
  - bld_architecture_transport_config
  - bld_config_transport_config
  - bld_examples_streaming_config
  - bld_collaboration_streaming_config
---

## Variant A: WebRTC Transport Config

```yaml
---
id: p09_tc_{{name}}
kind: transport_config
pillar: P09
title: "{{title}}"
version: "1.0.0"
transport_type: webrtc
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{domain}}"
quality: null
tags: [transport_config, webrtc]
tldr: "{{tldr}}"
---

transport_type: webrtc
protocol: dtls-srtp

ice_servers:
  - urls:
      - "stun:{{stun_host}}:3478"
    # STUN-only entry -- no credentials needed
  - urls:
      - "turn:{{turn_host}}:3478?transport=udp"
      - "turn:{{turn_host}}:5349?transport=tcp"
    username: "{{turn_username}}"
    credential: "{{turn_credential}}"

ice_transport_policy: "all"       # "relay" to force TURN only
bundle_policy: "max-bundle"       # single DTLS connection for all tracks
rtcp_mux_policy: "require"        # multiplex RTP and RTCP on same port
dtls_role: "auto"                 # auto-negotiate client/server role

qos:
  dscp_audio: 46      # EF -- Expedited Forwarding for voice
  dscp_video: 34      # AF41 for video
  dscp_data: 0        # Best-effort for data channels

tls:
  min_version: "1.2"
  preferred_version: "1.3"
  dtls_fingerprint_algorithm: "sha-256"

notes: "{{additional_notes}}"
```

## Variant B: WebSocket Transport Config

```yaml
---
id: p09_tc_{{name}}
kind: transport_config
pillar: P09
title: "{{title}}"
version: "1.0.0"
transport_type: websocket
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{domain}}"
quality: null
tags: [transport_config, websocket]
tldr: "{{tldr}}"
---

transport_type: websocket
protocol: rfc6455

endpoint: "wss://{{host}}:{{port}}{{path}}"
subprotocols:
  - "{{subprotocol}}"   # e.g., "graphql-ws", "mqtt", "v4.json.rabbitmq.com"

keepalive:
  ping_interval_ms: 30000
  ping_timeout_ms: 10000
  max_missed_pings: 2

framing:
  max_message_size_bytes: 1048576   # 1 MB
  compression:
    enabled: true
    algorithm: "permessage-deflate"  # RFC 7692
    client_max_window_bits: 15
    server_max_window_bits: 15

tls:
  version: "1.3"
  verify_peer: true

reconnect:
  initial_delay_ms: 1000
  max_delay_ms: 30000
  backoff_multiplier: 2.0
  max_attempts: 10

notes: "{{additional_notes}}"
```

## Variant C: SSE Transport Config

```yaml
---
id: p09_tc_{{name}}
kind: transport_config
pillar: P09
title: "{{title}}"
version: "1.0.0"
transport_type: sse
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{domain}}"
quality: null
tags: [transport_config, sse]
tldr: "{{tldr}}"
---

transport_type: sse
protocol: w3c-sse

endpoint: "https://{{host}}:{{port}}{{path}}"
content_type: "text/event-stream; charset=utf-8"

keepalive:
  heartbeat_interval_ms: 15000    # Empty comment line ": \n\n" to bypass proxy buffering

buffering:
  max_event_size_bytes: 65536
  buffer_timeout_ms: 100          # Server flush interval (0 = immediate)

reconnection:
  retry_ms: 3000                   # Sent via "retry:" field to client
  last_event_id_header: "Last-Event-ID"

tls:
  version: "1.3"
  verify_peer: true

notes: "{{additional_notes}}"
```

## Variant D: gRPC Streaming Transport Config

```yaml
---
id: p09_tc_{{name}}
kind: transport_config
pillar: P09
title: "{{title}}"
version: "1.0.0"
transport_type: grpc_streaming
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{domain}}"
quality: null
tags: [transport_config, grpc]
tldr: "{{tldr}}"
---

transport_type: grpc_streaming
protocol: grpc-over-http2      # HTTP/2 RFC 9113

server_endpoint: "{{host}}:{{port}}"
streaming_type: "{{streaming_type}}"   # server | client | bidirectional

keepalive:
  time_ms: 30000               # GRPC_ARG_KEEPALIVE_TIME_MS
  timeout_ms: 10000            # GRPC_ARG_KEEPALIVE_TIMEOUT_MS
  permit_without_calls: false  # GRPC_ARG_KEEPALIVE_PERMIT_WITHOUT_CALLS

message_limits:
  max_receive_message_length_bytes: 4194304   # 4 MB
  max_send_message_length_bytes: 4194304

flow_control:
  initial_window_size_bytes: 65535            # HTTP/2 default; increase for high-throughput
  initial_connection_window_size_bytes: 1048576

deadline_ms: {{deadline_ms}}    # Per-call deadline; 0 = no deadline (not recommended)

tls:
  version: "1.3"
  cert_file: "{{cert_path}}"
  key_file: "{{key_path}}"
  ca_file: "{{ca_path}}"

service_config: |
  {
    "methodConfig": [{
      "name": [{"service": "{{service_name}}"}],
      "retryPolicy": {
        "maxAttempts": 3,
        "initialBackoff": "0.1s",
        "maxBackoff": "1s",
        "backoffMultiplier": 2,
        "retryableStatusCodes": ["UNAVAILABLE"]
      }
    }]
  }

notes: "{{additional_notes}}"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_transport_config]] | downstream | 0.53 |
| [[bld_schema_transport_config]] | downstream | 0.44 |
| [[p09_qg_transport_config]] | downstream | 0.38 |
| [[p03_sp_transport_config_builder]] | upstream | 0.34 |
| [[bld_knowledge_card_transport_config]] | upstream | 0.33 |
| [[hybrid_review2_n04]] | upstream | 0.30 |
| [[bld_architecture_transport_config]] | downstream | 0.27 |
| [[bld_config_transport_config]] | downstream | 0.25 |
| [[bld_examples_streaming_config]] | downstream | 0.23 |
| [[bld_collaboration_streaming_config]] | downstream | 0.22 |
