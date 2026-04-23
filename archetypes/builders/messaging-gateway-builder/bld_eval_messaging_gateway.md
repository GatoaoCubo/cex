---
kind: quality_gate
id: bld_quality_gate_messaging_gateway
pillar: P11
llm_function: GOVERN
purpose: F7 GOVERN quality gates for messaging_gateway artifacts
pattern: HARD gates block publish; SOFT gates inform score
quality: 9.1
title: "Quality Gate: messaging_gateway"
version: "1.0.0"
author: n03_builder
tags: [messaging_gateway, builder, quality_gate, p11, hermes_origin]
tldr: "8 HARD gates + 6 SOFT gates for messaging_gateway. Target score 9.0+. Key HARD: id pattern, transport declared, security declared, stub contract honored."
domain: "messaging gateway construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.91
related:
  - p11_qg_agent_computer_interface
  - bld_examples_cli_tool
  - p11_qg_creation_artifacts
  - bld_knowledge_card_quality_gate
  - p11_qg_quality_gate
  - p11_qg_mcp_server
  - bld_examples_axiom
  - p01_kc_artifact_quality_evaluation_methods
  - p11_qg_chunk_strategy
  - p11_qg_builder
---

## Quality Gate

# Quality Gate: messaging_gateway

## HARD Gates (FAIL = DO NOT PUBLISH)
| ID | Gate | Check | Fix |
|----|------|-------|-----|
| H01 | Frontmatter complete | All required fields present | Add missing fields from SCHEMA.md |
| H02 | ID pattern | `^p04_mg_[a-z][a-z0-9_]+$` | Rename to p04_mg_{platform_slug} |
| H03 | Kind correct | kind == "messaging_gateway" | Fix kind field |
| H04 | Pillar correct | pillar == "P04" | Fix pillar field |
| H05 | Quality null | quality: null (never self-score) | Remove any numeric value |
| H06 | Platforms declared | platforms_supported non-empty AND active_platforms non-empty AND active is subset | Declare both fields correctly |
| H07 | Transport declared | transport.protocol AND transport.auth_type present | Add transport block |
| H08 | Security declared | security.dm_pairing AND security.rate_limit_per_user_per_min present | Add security block |
| H09 | Stub contract | No live credentials or connection code in artifact | Move credentials to .cex/config/ |

## SOFT Gates (inform score, not blocking)
| ID | Gate | Weight | Check |
|----|------|--------|-------|
| S01 | 7 body sections present | 15% | Overview, Platform Config, Security, Features, Slash Commands, Integration Points, Stub Notice |
| S02 | Slash commands defined | 15% | At least /help, /status, /reset in table |
| S03 | Integration points wired | 20% | user_model (P10) and session_state (P10) referenced |
| S04 | Security rationale | 15% | Notes column populated in Security table |
| S05 | Voice dependency explicit | 15% | If voice=true, stt_provider dependency listed |
| S06 | Tags complete | 10% | >= 4 tags including messaging_gateway and hermes_origin |
| S07 | TLDR density | 10% | <= 160 chars, includes platform + security posture + DP5 |

## Score Calculation
| Gate Set | Weight | Method |
|----------|--------|--------|
| HARD (H01-H09) | pass/fail | Any FAIL = score 0, not published |
| SOFT (S01-S07) | weighted avg | Weighted sum of passed soft gates |
| Final | composite | HARD_pass * soft_score (0.0-10.0) |
| Target | >= 9.0 | Minimum for commit to main |

## Common Failure Patterns
1. **id has hyphens** -> `p04_mg_telegram` not `p04-mg-telegram` (H02)
2. **Live credentials in artifact** -> move to .cex/config/ (H09)
3. **active_platforms not subset of platforms_supported** -> declare platforms_supported first (H06)
4. **Missing Stub Notice section** -> add DP5 declaration (S01)
5. **No slash commands** -> add /help /status /reset minimum (S02)
6. **Missing user_model reference** -> wire to P10 in Integration Points (S03)

## Retry Protocol
If score < 9.0:
1. Identify which SOFT gate is failing
2. Add the missing section or expand the sparse one
3. Re-score via `python _tools/cex_score.py --apply {filename}`
4. Maximum 2 retries before escalating to human review

## Examples

# Examples: messaging-gateway-builder

## Golden Example 1 -- Telegram-only stub
INPUT: "Create a messaging gateway for a Telegram bot with DM pairing"
OUTPUT:
```yaml
id: p04_mg_telegram
kind: messaging_gateway
pillar: P04
nucleus: n05
title: "Messaging Gateway: Telegram"
version: 1.0.0
quality: null
created: "2026-04-18"
updated: "2026-04-18"
author: n03_builder
platforms_supported: [telegram, discord, slack, whatsapp, signal, email]
active_platforms: [telegram]
transport:
  protocol: webhook
  auth_type: bot_token
security:
  dm_pairing: true
  command_approval_list: []
  allowed_user_ids: []
  rate_limit_per_user_per_min: 30
features:
  voice_memo_transcription: false
  cross_platform_continuity: true
  shared_slash_commands: true
tags: [messaging_gateway, telegram, hermes_origin, stub, p04]
tldr: "Telegram gateway stub: webhook transport, DM pairing, 30/min rate limit. DP5 -- no live code."
```
WHY THIS IS GOLDEN:
- id matches `^p04_mg_` prefix and filename stem (H02 pass)
- kind: messaging_gateway (H04 pass)
- quality: null (H05 pass)
- active_platforms is subset of platforms_supported (H06 pass)
- transport fully declared: protocol + auth_type (H07 pass)
- security.dm_pairing: true (H08 pass)
- features all declared (H09 pass)
- stub contract honored -- no live code (DP5 pass)

## Golden Example 2 -- Multi-platform HERMES stub
INPUT: "Create a full HERMES gateway for Telegram + Discord + Slack"
OUTPUT:
```yaml
id: p04_mg_all
kind: messaging_gateway
pillar: P04
nucleus: n05
title: "Messaging Gateway: HERMES Full Stack"
version: 1.0.0
quality: null
created: "2026-04-18"
updated: "2026-04-18"
author: n03_builder
platforms_supported: [telegram, discord, slack, whatsapp, signal, email]
active_platforms: [telegram, discord, slack]
transport:
  protocol: webhook
  auth_type: bot_token
security:
  dm_pairing: true
  command_approval_list: ["/admin", "/reset"]
  allowed_user_ids: []
  rate_limit_per_user_per_min: 30
features:
  voice_memo_transcription: false
  cross_platform_continuity: true
  shared_slash_commands: true
tags: [messaging_gateway, telegram, discord, slack, hermes_origin, stub, p04]
tldr: "Full HERMES gateway stub: Telegram+Discord+Slack, DM pairing, cross-platform continuity, shared commands. DP5."
```
WHY THIS IS GOLDEN:
- 3 platforms active, all subset of platforms_supported (H06 pass)
- command_approval_list populated for privileged commands (S03 pass)
- cross_platform_continuity: true -- key HERMES property (S04 pass)

## Golden Example 3 -- Voice-enabled gateway
INPUT: "Create a Telegram gateway with voice memo transcription"
OUTPUT:
```yaml
id: p04_mg_telegram_voice
kind: messaging_gateway
pillar: P04
nucleus: n05
title: "Messaging Gateway: Telegram + Voice"
version: 1.0.0
quality: null
created: "2026-04-18"
updated: "2026-04-18"
author: n03_builder
platforms_supported: [telegram, discord, slack, whatsapp, signal, email]
active_platforms: [telegram]
transport:
  protocol: webhook
  auth_type: bot_token
security:
  dm_pairing: true
  command_approval_list: []
  allowed_user_ids: []
  rate_limit_per_user_per_min: 30
features:
  voice_memo_transcription: true
  cross_platform_continuity: true
  shared_slash_commands: true
tags: [messaging_gateway, telegram, voice, hermes_origin, stub, p04]
tldr: "Telegram+voice gateway: webhook, DM pairing, voice_memo_transcription enabled -- requires stt_provider. DP5."
```
WHY THIS IS GOLDEN:
- voice_memo_transcription: true with dependency documented in Integration Points (S05 pass)
- stt_provider integration linked (S06 pass)

## Anti-Example
INPUT: "Create a Telegram gateway"
BAD OUTPUT:
```yaml
id: telegram-gateway
kind: gateway
title: Telegram
auth: "BOT_TOKEN=abc123"
quality: 8.5
tags: [telegram]
```
FAILURES:
1. id: "telegram-gateway" has hyphens and no `p04_mg_` prefix -> H02 FAIL
2. kind: "gateway" not "messaging_gateway" -> H04 FAIL
3. quality: 8.5 (not null) -> H05 FAIL
4. platforms_supported missing -> H06 FAIL
5. transport block missing -> H07 FAIL
6. security block missing -> H08 FAIL
7. features block missing -> H09 FAIL
8. auth: "BOT_TOKEN=abc123" -- live credential in artifact -> security FAIL
9. Missing pillar, version, created, updated, author, tldr -> H01 FAIL
10. Body missing all required sections -> structure FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
