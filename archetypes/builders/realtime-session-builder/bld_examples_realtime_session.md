---
kind: examples
id: bld_examples_realtime_session
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of realtime_session artifacts
quality: null
title: "Examples Realtime Session"
version: "1.0.0"
author: wave1_builder_gen
tags: [realtime_session, builder, examples]
tldr: "Golden and anti-examples of realtime_session artifacts"
domain: "realtime_session construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```markdown
---
kind: realtime_session
name: video_conference_123
description: "Live bidirectional video session with QoS guarantees"
parameters:
  session_id: "sess_456"
  media_type: "video"
  codecs:
    - "H264"
    - "VP9"
  qos:
    min_bandwidth: 1024
    max_latency: 200
  participants:
    - "userA"
    - "userB"
```

## Anti-Example 1: Missing Required Fields
```markdown
---
kind: realtime_session
name: broken_session
parameters:
  media_type: "audio"
  codecs: ["G711"]
```
## Why it fails
Lacks essential session_id and qos parameters required for session initialization and quality management.

## Anti-Example 2: Incompatible Codec Configuration
```markdown
---
kind: realtime_session
name: codec_mismatch
parameters:
  session_id: "bad_sess"
  media_type: "video"
  codecs: ["G711", "H264"]
```
## Why it fails
Mixes audio (G711) and video (H264) codecs in a single session configuration, creating incompatible media handling requirements.
