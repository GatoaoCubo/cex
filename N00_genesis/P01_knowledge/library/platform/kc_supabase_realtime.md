---
id: p01_kc_supabase_realtime
kind: knowledge_card
8f: F3_inject
type: platform
pillar: P01
title: "Supabase Realtime — Channels, Presence, Broadcast, DB Changes"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [supabase, realtime, websocket, channels, presence, broadcast, platform]
tldr: "WebSocket server with 4 modes: Channels (pub/sub), Presence (who is online), Broadcast (fire-and-forget), and Postgres Changes (subscribe to INSERT/UPDATE/DELETE)"
when_to_use: "When configuring real-time features in Supabase projects"
keywords: [supabase-realtime, websocket, channels, presence, postgres-changes]
long_tails:
  - How to receive real-time notification of INSERT in Supabase
  - Implement online users indicator with Supabase Presence
  - Difference between Broadcast and Postgres Changes in Supabase
axioms:
  - ALWAYS filter Postgres Changes by specific table and event
  - NEVER subscribe to all tables — causes WAL overhead
  - ALWAYS use RLS with Realtime — user only receives changes they can see
linked_artifacts:
  primary: null
  related: [p01_kc_supabase_database, p01_kc_supabase_auth]
density_score: 0.89
data_source: "https://supabase.com/docs/guides/realtime"
related:
  - bld_instruction_supabase_data_layer
  - bld_manifest_supabase_data_layer
  - bld_tools_supabase_data_layer
  - p01_kc_supabase_cli
  - p01_kc_supabase_database
  - p01_kc_supabase_self_hosting
  - bld_system_prompt_supabase_data_layer
  - p12_wf_supabase_setup
  - p05_fmt_marketing_report
  - p01_kc_brand_voice_consistency_channels
---

# Supabase Realtime — WebSocket Server

## Quick Reference
```yaml
topic: supabase_realtime
scope: WebSocket channels, presence, broadcast, DB changes
owner: n04_knowledge
criticality: high
service: realtime (port 4000)
protocol: WebSocket (Phoenix Channels)
```

## 4 Realtime Modes
| Mode | Function | Latency | RLS |
|------|----------|---------|-----|
| Broadcast | Fire-and-forget to all in channel | <100ms | No (channel-level) |
| Presence | Track who is online, sync state | <100ms | No (channel-level) |
| Postgres Changes | Subscribe to INSERT/UPDATE/DELETE on tables | 100-500ms | Yes (row-level) |
| Realtime Channels | Generic pub/sub (combines all 3 above) | Varies | Configurable |

## Limits per Tier
| Metric | Free | Pro | Team |
|---------|------|-----|------|
| Concurrent connections | 200 | 500 | 1000+ |
| Messages/segundo | 100 | 500 | 2000+ |
| Channel subscriptions | 100 | 500 | Unlimited |
| Postgres Changes (tables) | 10 | 100 | Unlimited |

## Broadcast (Chat, Notifications)
```javascript
// Send message to all in channel
const channel = supabase.channel('room-1')
channel.on('broadcast', { event: 'message' }, (payload) => {
  console.log(payload)  // {event:'message', payload:{text:'hello'}}
})
await channel.subscribe()

// Send
channel.send({
  type: 'broadcast',
  event: 'message',
  payload: { text: 'hello', user: 'alice' }
})
```

## Presence (Who Is Online)
```javascript
const channel = supabase.channel('online-users')
channel.on('presence', { event: 'sync' }, () => {
  const state = channel.presenceState()
  // { 'user-1': [{online_at: '...'}], 'user-2': [...] }
})
await channel.subscribe(async (status) => {
  if (status === 'SUBSCRIBED') {
    await channel.track({ user_id: 'user-1', online_at: new Date() })
  }
})
```

## Postgres Changes (DB Triggers)
```javascript
const channel = supabase.channel('db-changes')
  .on('postgres_changes',
    { event: 'INSERT', schema: 'public', table: 'orders',
      filter: 'status=eq.pending' },  // filtro opcional
    (payload) => {
      console.log('New order:', payload.new)
    }
  )
  .subscribe()
```

## Postgres Changes — How It Works
```text
[INSERT/UPDATE/DELETE] → [PostgreSQL WAL]
    → [Supabase Realtime server] reads WAL
    → [RLS check] filters by user
    → [WebSocket] sends to subscribers
```

| Config | Valor | Nota |
|--------|-------|------|
| Publication | `supabase_realtime` | Table must be in the publication |
| Enable | `ALTER PUBLICATION supabase_realtime ADD TABLE orders;` | Per table |
| Filter server-side | `filter: 'column=eq.value'` | Reduces traffic |
| RLS | Automatic if enabled | User only sees rows they can SELECT |

## Anti-Patterns
| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| Subscribe `*` (all tables) | WAL overhead, memory, CPU | Filter by table + event |
| No unsubscribe on unmount | Zombie connections, memory leak | `channel.unsubscribe()` in cleanup |
| Broadcast for critical notifications | Lost message = lost data | Use Postgres Changes + table |
| Presence without throttle | State sync on every keypress | Debounce 1-5s on track() |
| Ignoring RLS on Changes | User sees other users' data | Enable RLS on the table |

## Golden Rules
- USE Broadcast for ephemeral (typing indicators, cursor position)
- USE Postgres Changes for data that needs to persist
- USE Presence for "who is online" with automatic sync
- ALWAYS FILTER: table + event + filter column when possible
- ENABLE the table in the publication before subscribing

## References
- Docs: https://supabase.com/docs/guides/realtime
- Broadcast: https://supabase.com/docs/guides/realtime/broadcast
- Presence: https://supabase.com/docs/guides/realtime/presence
- Postgres Changes: https://supabase.com/docs/guides/realtime/postgres-changes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_supabase_data_layer]] | downstream | 0.26 |
| [[bld_manifest_supabase_data_layer]] | downstream | 0.23 |
| [[bld_tools_supabase_data_layer]] | downstream | 0.23 |
| [[p01_kc_supabase_cli]] | sibling | 0.22 |
| [[p01_kc_supabase_database]] | sibling | 0.22 |
| [[p01_kc_supabase_self_hosting]] | sibling | 0.21 |
| [[bld_system_prompt_supabase_data_layer]] | downstream | 0.21 |
| [[p12_wf_supabase_setup]] | downstream | 0.20 |
| [[p05_fmt_marketing_report]] | downstream | 0.20 |
| [[p01_kc_brand_voice_consistency_channels]] | sibling | 0.19 |
