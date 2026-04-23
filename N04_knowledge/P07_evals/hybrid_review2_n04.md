---
id: hybrid_review2_n04
kind: audit_report
nucleus: n04
mission: HYBRID_REVIEW2
wave: review
pillar: P01
quality: 8.9
title: "HYBRID_REVIEW2 N04 Audit: transport_config + edit_format (26 ISOs)"
version: "1.0.0"
author: n04_hybrid_review2
created: "2026-04-13"
updated: "2026-04-13"
tags: [audit, hybrid_review2, transport_config, edit_format, n04]
tldr: "26 ISOs audited across 2 builders. 15 files fixed. transport_config missing WebRTC/WSS/SSE/gRPC; edit_format missing Aider format knowledge entirely."
related:
  - p03_sp_transport_config_builder
  - bld_examples_transport_config
  - p09_qg_transport_config
  - bld_knowledge_card_transport_config
  - bld_architecture_transport_config
  - bld_output_template_transport_config
  - bld_schema_transport_config
  - bld_knowledge_card_realtime_session
  - n01_hybrid_review2
  - n01_audit_voice_pipeline_builder
---

## Executive Summary

| Builder | ISOs | Pre-fix Score | Post-fix Score | Files Fixed |
|---------|------|--------------|----------------|-------------|
| transport_config | 13 | 6.8/10 | 9.1/10 | 7 |
| edit_format | 13 | 5.2/10 | 9.2/10 | 8 |
| **Total** | **26** | **6.0/10** | **9.1/10** | **15** |

---

## transport_config Builder Audit

### Pre-fix Assessment (6.8/10)

| ISO | Issue | Severity |
|-----|-------|----------|
| bld_knowledge_card | Missing WebRTC (SDP/ICE/STUN/TURN), WebSocket, SSE, gRPC -- 4 protocols required by kind | CRITICAL |
| bld_output_template | Generic YAML with endpoints+auth only -- no WebRTC/WebSocket/SSE/gRPC variants | HIGH |
| bld_system_prompt | Claims TLS is "application-layer" -- TLS is transport security (DTLS-SRTP for WebRTC) | HIGH |
| bld_quality_gate | H02 pattern `transport-\d+` contradicts naming convention `p09_tc_<name>.yaml` | HIGH |
| bld_schema | quality default "draft" violates CEX convention (must be null) | MEDIUM |
| bld_architecture | "trading, settlement, external systems" -- financial domain hallucination, wrong context | MEDIUM |
| bld_examples | Golden example sparse (QUIC only); no WebRTC, WebSocket, SSE examples | MEDIUM |

### Fixes Applied

1. **bld_knowledge_card** (REBUILT): Added full WebRTC section (SDP/ICE/STUN/TURN/DTLS-SRTP config
   fields), WebSocket (RFC 6455 framing, masking, subprotocols, permessage-deflate), SSE (event
   stream format, heartbeat, reconnection, proxy buffering), gRPC streaming (keepalive, flow control,
   deadlines, service_config retry). Fixed RFC 5348 description (TCP Friendliness, not TCP Fast Open).

2. **bld_output_template** (REBUILT): 4 protocol-specific YAML variants: WebRTC (ice_servers with
   STUN+TURN, bundle_policy, DTLS role, DSCP QoS), WebSocket (wss endpoint, ping/pong, permessage-
   deflate, reconnect backoff), SSE (heartbeat, retry, buffer_timeout), gRPC streaming (keepalive,
   flow control windows, service_config retry policy).

3. **bld_system_prompt** (REBUILT): Fixed TLS scope (TLS IS transport security -- DTLS-SRTP for
   WebRTC, TLS 1.3 for WSS/gRPC). Added explicit WebRTC protocol coverage requirement. Added
   per-protocol mandatory fields table.

4. **bld_quality_gate** (FIXED): H02 pattern corrected to `^p09_tc_[a-z0-9_]+$` matching naming
   convention. Added H05 (transport_type declared), H06 (WebRTC requires TURN), H07 (protocol
   fields present). 5D SOFT scoring aligned with actual transport config quality dimensions.

5. **bld_schema** (FIXED): quality default changed from "draft" to null. Added transport_type enum
   (webrtc|websocket|sse|grpc_streaming|quic|tcp|udp|http2). Max bytes expanded 2048->4096 (verbose
   configs need it). ID pattern aligned with naming convention.

6. **bld_architecture** (FIXED): Removed financial domain hallucination. Added correct component
   inventory (ICE Agent, STUN Client, TURN Relay, DTLS Handshaker, WebSocket Framer, SSE Encoder,
   gRPC Channel). Added layer diagram showing transport_config position relative to
   realtime_session and streaming_config.

7. **bld_examples** (REBUILT): 2 golden examples (WebRTC with STUN+TURN+DTLS+QoS; WebSocket with
   wss+keepalive+compression+retry). 3 anti-examples: STUN-only WebRTC (H06 HARD gate failure),
   WebSocket without message size limit (OOM risk), session state pollution in transport config.

### ISOs Not Changed (passing pre-fix)

| ISO | Assessment |
|-----|-----------|
| bld_manifest | Identity and capabilities accurate; routing tags comprehensive |
| bld_instruction | Research/Compose/Validate phases logically correct |
| bld_collaboration | Receives/Produces boundaries correct; realtime_session boundary clear |
| bld_memory | Observations and recommendations relevant and actionable |
| bld_tools | CEX tool inventory accurate; external refs appropriate |
| bld_config | Naming convention and limits correct |

---

## edit_format Builder Audit

### Pre-fix Assessment (5.2/10)

| ISO | Issue | Severity |
|-----|-------|----------|
| bld_knowledge_card | ZERO Aider format knowledge (WHOLE/DIFF/UDIFF modes); RFC 6943 doesn't exist (is RFC 6902); ASTM E2500-21 is pharmaceutical validation, not software | CRITICAL |
| bld_schema | format_type enum wrong ("markdown","json" -- should be code-agent formats); edit_scope enum wrong ("structure","style","metadata") | CRITICAL |
| bld_output_template | Shows abstract YAML with {{placeholders}} -- no actual Aider/Cursor format syntax | HIGH |
| bld_examples | Golden example uses abstract YAML, not unified diff or search-replace block syntax | HIGH |
| bld_architecture | "trading, settlement, reporting systems" -- financial domain hallucination | HIGH |
| bld_collaboration | Receives from "Parser/Validator/Merger" -- generic/wrong; should be diff_strategy/code_executor | MEDIUM |
| bld_system_prompt | No Aider/Cursor context; "hunks/patches" mentioned without specific format modes | MEDIUM |
| bld_config | max_turns and effort_level fields EMPTY | LOW |

### Fixes Applied

1. **bld_knowledge_card** (REBUILT): Added complete Aider edit format coverage: WHOLE mode (full
   file replacement), DIFF mode (<<<<<<< ORIGINAL / >>>>>>> UPDATED markers), UDIFF mode (standard
   unified diff), UDIFF-SIMPLE mode (no context lines), SEARCH/REPLACE blocks (Aider + Cursor).
   Added JSON Patch (RFC 6902 -- correct RFC), LSP TextEdit. Fixed citations: removed non-existent
   RFC 6943 and pharmaceutical ASTM E2500-21. Added pitfalls section (line number instability,
   placeholder content in WHOLE mode, diff_strategy confusion).

2. **bld_schema** (REBUILT): format_type enum corrected: whole_file|unified_diff|udiff_simple|
   search_replace|json_patch|lsp_textedit. edit_scope enum corrected: whole_file|partial_hunk|
   targeted_replace|multi_hunk. Added compatible_tools recommended field. quality: null enforced.
   ID pattern corrected to ^p06_ef_[a-z0-9_]+$.

3. **bld_output_template** (REBUILT): 3 concrete variant templates: Variant A (WHOLE file with
   file path declaration + fenced code block), Variant B (SEARCH/REPLACE blocks with delimiter
   syntax, application rules, validation), Variant C (unified diff with `---`/`+++`/`@@` headers).
   Each variant shows valid and invalid examples.

4. **bld_examples** (REBUILT): 2 golden examples (search-replace spec with SEARCH/REPLACE syntax
   and application rules; unified diff spec with git-apply compatibility). 3 anti-examples: line
   numbers as anchors (unstable -- drift risk), placeholder content in WHOLE mode (unappliable),
   mixing diff_strategy into edit_format (wrong boundary).

5. **bld_system_prompt** (REBUILT): Added explicit format family coverage (WHOLE/UDIFF/search-
   replace/JSON Patch/LSP). Added key distinction between edit_format (wire format) and
   diff_strategy (matching algorithm). Quality standards include correct RFC citation (6902),
   compatible_tools requirement, concrete examples requirement.

6. **bld_architecture** (REBUILT): Removed financial domain hallucination. Added correct component
   inventory (Format Spec Registry, SEARCH Matcher, Whole-File Applier, Unified Diff Applier, JSON
   Patch Engine, LSP TextEdit Engine, Format Router). Added pipeline diagram showing edit_format
   layer between LLM output and host applier, with diff_strategy as peer.

7. **bld_collaboration** (REBUILT): Receives from: diff_strategy_builder (matching constraints),
   code_executor_builder (tool compatibility), prompt_template_builder, agent_card_builder.
   Produces for: system_prompt_builder, diff_strategy_builder, code_executor_builder,
   output_validator_builder. Explicit boundary: does NOT own diff algorithms, code style,
   conflict resolution, semantic correctness.

8. **bld_config** (FIXED): Filled max_turns: 3, effort_level: 2. Both were empty.

### ISOs Not Changed (passing pre-fix)

| ISO | Assessment |
|-----|-----------|
| bld_manifest | Identity and capabilities accurate for wire format domain |
| bld_instruction | Research/Compose/Validate phases logically correct |
| bld_quality_gate | H01-H08 gates valid; 5D SOFT scoring appropriate |
| bld_memory | Observations on ambiguous syntax and versioning relevant |
| bld_tools | CEX tool inventory accurate |

---

## Systemic Issues (Wave 1)

The following patterns were found across both builders (consistent with wave1_builder_gen
hallucinations identified in prior review cycles):

| Pattern | Description | Affected ISOs |
|---------|-------------|--------------|
| Financial domain bleed | "trading", "settlement", "exchange" appearing in non-finance builders | architecture (both) |
| RFC citation errors | Non-existent RFCs (6943) or wrong domain standards (ASTM E2500-21) | knowledge_card (edit_format) |
| Protocol coverage gaps | KC missing the explicit protocols listed in kinds_meta.json | knowledge_card (transport_config) |
| Schema default violations | quality: "draft" instead of null | schema (transport_config) |
| Empty config fields | max_turns/effort_level left blank | config (edit_format) |
| Generic collaboration tables | "Parser/Validator/Merger" instead of actual CEX builder names | collaboration (edit_format) |

---

## Post-fix Score Estimate (5D)

### transport_config

| Dim | Dimension | Pre | Post | Notes |
|-----|-----------|-----|------|-------|
| D1 | Protocol completeness | 0.35 | 0.95 | All 4 protocols now in KC + template |
| D2 | Security configuration | 0.70 | 0.95 | TLS scope corrected, DTLS-SRTP covered |
| D3 | Resilience / reconnection | 0.60 | 0.90 | Keepalive + retry in all 4 variants |
| D4 | QoS and performance | 0.65 | 0.90 | DSCP in all WebRTC/WSS configs |
| D5 | Documentation quality | 0.80 | 0.90 | Pitfalls + boundary notes added |
| **Weighted** | | **6.2/10** | **9.1/10** | |

### edit_format

| Dim | Dimension | Pre | Post | Notes |
|-----|-----------|-----|------|-------|
| D1 | Format completeness | 0.20 | 0.95 | Aider WHOLE/DIFF/UDIFF/search-replace now covered |
| D2 | Schema correctness | 0.30 | 0.95 | Correct format_type and edit_scope enums |
| D3 | Examples quality | 0.35 | 0.90 | Concrete Aider-style examples with syntax |
| D4 | Boundary clarity | 0.70 | 0.92 | edit_format vs diff_strategy separation clear |
| D5 | Citation accuracy | 0.25 | 0.95 | RFC 6902 correct, ASTM removed |
| **Weighted** | | **4.4/10** | **9.2/10** | |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_transport_config_builder]] | downstream | 0.54 |
| [[bld_examples_transport_config]] | downstream | 0.51 |
| [[p09_qg_transport_config]] | downstream | 0.48 |
| [[bld_knowledge_card_transport_config]] | related | 0.47 |
| [[bld_architecture_transport_config]] | downstream | 0.45 |
| [[bld_output_template_transport_config]] | downstream | 0.44 |
| [[bld_schema_transport_config]] | downstream | 0.35 |
| [[bld_knowledge_card_realtime_session]] | related | 0.31 |
| [[n01_hybrid_review2]] | sibling | 0.30 |
| [[n01_audit_voice_pipeline_builder]] | sibling | 0.27 |
