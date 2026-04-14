---
kind: examples
id: bld_examples_transport_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of transport_config artifacts
quality: null
title: "Examples Transport Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [transport_config, builder, examples]
tldr: "Golden and anti-examples of transport_config artifacts"
domain: "transport_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```markdown
---
kind: transport_config
name: example_transport
---
protocol: QUIC
port: 443
encryption: TLS1.3
qos: {
  "target_latency": "50ms",
  "bandwidth_limit": "100Mbps"
}
reliability: {
  "ack_timeout": "100ms",
  "max_retransmits": 3
}
```

## Anti-Example 1: Missing Critical Fields
```markdown
---
kind: transport_config
name: broken_transport
---
protocol: 
port: 80
encryption: TLS1.2
```
## Why it fails
Omits required protocol definition, making transport layer unusable. Port 80 is non-secure and incompatible with encryption setting.

## Anti-Example 2: Session Lifecycle Pollution
```markdown
---
kind: transport_config
name: polluted_transport
---
protocol: TCP
port: 5000
session_timeout: 30s
```
## Why it fails
Includes session management parameters (session_timeout) which belong to realtime_session CEX kind, violating boundary constraints.
