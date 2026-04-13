---
kind: instruction
id: bld_instruction_realtime_session
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for realtime_session
quality: null
title: "Instruction Realtime Session"
version: "1.0.0"
author: wave1_builder_gen
tags: [realtime_session, builder, instruction]
tldr: "Step-by-step production process for realtime_session"
domain: "realtime_session construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify required protocols (e.g., WebRTC, WebSocket) for bidirectional communication.  
2. Define session parameters: latency thresholds, bandwidth limits, and encryption standards.  
3. Analyze compatibility across client/server platforms and network conditions.  
4. Research error codes and recovery mechanisms for session interruptions.  
5. Evaluate security requirements (TLS, authentication, data obfuscation).  
6. Benchmark existing session management libraries for performance.  

## Phase 2: COMPOSE  
1. Reference SCHEMA.md to define session structure (ID, duration, endpoints).  
2. Use OUTPUT_TEMPLATE.md to format session initiation and termination messages.  
3. Implement bidirectional data channels with heartbeat intervals (per schema).  
4. Embed encryption layers (AES-256) and mutual TLS authentication.  
5. Configure dynamic reconfiguration hooks for parameter adjustments mid-session.  
6. Write session lifecycle handlers (start, pause, resume, close).  
7. Integrate latency compensation logic (buffering, jitter control).  
8. Add logging hooks for real-time metrics (throughput, packet loss).  
9. Document API endpoints for external systems to interact with the session.  

## Phase 3: VALIDATE  
- [ ] Validate schema compliance using SCHEMA.md against generated artifacts.  
- [ ] Test bidirectional data flow under simulated network stress (latency, dropout).  
- [ ] Audit encryption and authentication workflows for vulnerabilities.  
- [ ] Confirm heartbeat and reconnection logic triggers correct recovery actions.  
- [ ] Verify error codes map to real-world scenarios (e.g., 408 for timeout).
