---
kind: instruction
id: bld_instruction_messaging_gateway
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for messaging_gateway
pattern: 3-phase pipeline (configure -> compose -> validate)
quality: 8.9
title: "Instruction: messaging_gateway"
version: "1.0.0"
author: n03_builder
tags: [messaging_gateway, builder, instruction, p04, hermes_origin]
tldr: "3-phase build: identify active platforms + configure transport + set security posture. Stub only (DP5). Max 4096 bytes."
domain: "messaging gateway construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_instruction_memory_scope
  - bld_instruction_output_validator
  - bld_instruction_context_doc
  - bld_instruction_retriever_config
  - bld_instruction_handoff_protocol
  - bld_instruction_chunk_strategy
  - bld_instruction_prompt_version
  - bld_instruction_enum_def
  - bld_instruction_constraint_spec
  - bld_instruction_cli_tool
---

# Instructions: How to Produce a messaging_gateway

## Phase 1: CONFIGURE
1. Identify the deployment context: which platforms will this gateway serve?
2. Determine active_platforms (subset to configure now) vs platforms_supported (full enum)
3. Choose transport.protocol per platform: websocket (Discord), webhook (Telegram/Slack), polling (Signal/Email)
4. Choose transport.auth_type per platform: bot_token (Telegram/Discord), oauth (Slack), app_password (WhatsApp/Signal/Email)
5. Set security posture:
   - dm_pairing: always true for production
   - allowed_user_ids: empty for dev, populated for production
   - rate_limit_per_user_per_min: 30 default
   - command_approval_list: list any /commands requiring explicit operator approval
6. Declare feature flags:
   - cross_platform_continuity: true (HERMES default -- same peer_id across platforms)
   - shared_slash_commands: true (HERMES default -- same /commands on all platforms)
   - voice_memo_transcription: false unless stt_provider is configured
7. Confirm this is a STUB (DP5) -- no live platform code in the artifact
8. Confirm id slug: p04_mg_{platform} (primary platform slug, lowercase, underscores)

## Phase 2: COMPOSE
1. Read SCHEMA.md -- source of truth for all fields
2. Read OUTPUT_TEMPLATE.md -- fill template variables following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null -- never self-score)
4. Write platforms_supported list: all 6 HERMES platforms unless explicitly scoped
5. Write active_platforms: only the platforms with credentials ready
6. Write transport block: protocol + auth_type
7. Write security block: dm_pairing + command_approval_list + allowed_user_ids + rate_limit
8. Write features block: voice_memo_transcription + cross_platform_continuity + shared_slash_commands
9. Write Overview section: 2 sentences -- what platforms this gateway covers and why
10. Write Platform Configuration section: table with Platform | Status | Transport | Auth
11. Write Security section: table with Control | Value | Notes
12. Write Features section: table with Feature | Status | Dependency
13. Write Shared Slash Commands section: table with Command | Description
14. Write Integration Points section: link to user_model, session_state, stt_provider, agent_profile
15. Write Stub Notice: explain DP5 and how to activate
16. Verify body <= 4096 bytes
17. Verify id matches `^p04_mg_[a-z][a-z0-9_]+$`

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md -- verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p04_mg_` prefix
4. Confirm kind == messaging_gateway
5. Confirm platforms_supported is non-empty and subset of [telegram, discord, slack, whatsapp, signal, email]
6. Confirm active_platforms is a subset of platforms_supported
7. Confirm transport.protocol is one of: websocket, webhook, polling
8. Confirm transport.auth_type is one of: bot_token, oauth, app_password
9. Confirm security.dm_pairing is boolean (true for production)
10. HARD gates: frontmatter valid, id pattern matches, platforms_supported non-empty, transport declared
11. SOFT gates: score against QUALITY_GATES.md -- target >= 9.0
12. Cross-check kind boundaries: no live platform code (that is impl, not spec)? No session data (that is session_state)? Not a single-event callback (that is webhook)?
13. Revise if score < 9.0 -- most common fix: add slash commands table or security rationale


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_memory_scope]] | sibling | 0.39 |
| [[bld_instruction_output_validator]] | sibling | 0.39 |
| [[bld_instruction_context_doc]] | sibling | 0.38 |
| [[bld_instruction_retriever_config]] | sibling | 0.38 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.38 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.37 |
| [[bld_instruction_prompt_version]] | sibling | 0.36 |
| [[bld_instruction_enum_def]] | sibling | 0.36 |
| [[bld_instruction_constraint_spec]] | sibling | 0.36 |
| [[bld_instruction_cli_tool]] | sibling | 0.35 |
