---
id: p01_kc_supabase_realtime
kind: knowledge_card
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
tldr: "WebSocket server com 4 modos: Channels (pub/sub), Presence (quem esta online), Broadcast (fire-and-forget), e Postgres Changes (subscribe a INSERT/UPDATE/DELETE)"
when_to_use: "Quando configurar funcionalidades real-time em projetos Supabase"
keywords: [supabase-realtime, websocket, channels, presence, postgres-changes]
long_tails:
  - Como receber notificacao em tempo real de INSERT no Supabase
  - Implementar indicador de usuarios online com Supabase Presence
  - Diferenca entre Broadcast e Postgres Changes no Supabase
axioms:
  - SEMPRE filtre Postgres Changes por tabela e evento especifico
  - NUNCA subscribe a todas as tabelas — causa overhead no WAL
  - SEMPRE use RLS com Realtime — user só recebe changes que pode ver
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
service: realtime (porta 4000)
protocol: WebSocket (Phoenix Channels)
```

## 4 Modos de Realtime
| Modo | Funcao | Latencia | RLS |
|------|--------|----------|-----|
| Broadcast | Fire-and-forget para todos no channel | <100ms | Não (channel-level) |
| Presence | Track quem está online, sync state | <100ms | Não (channel-level) |
| Postgres Changes | Subscribe a INSERT/UPDATE/DELETE em tabelas | 100-500ms | Sim (row-level) |
| Realtime Channels | Pub/sub genérico (combina os 3 acima) | Varia | Configável |

## Limites por Tier
| Metrica | Free | Pro | Team |
|---------|------|-----|------|
| Concurrent connections | 200 | 500 | 1000+ |
| Messages/segundo | 100 | 500 | 2000+ |
| Channel subscriptions | 100 | 500 | Ilimitado |
| Postgres Changes (tables) | 10 | 100 | Ilimitado |

## Broadcast (Chat, Notificacoes)
```javascript
// Enviar mensagem para todos no channel
const channel = supabase.channel('room-1')
channel.on('broadcast', { event: 'message' }, (payload) => {
  console.log(payload)  // {event:'message', payload:{text:'hello'}}
})
await channel.subscribe()

// Enviar
channel.send({
  type: 'broadcast',
  event: 'message',
  payload: { text: 'hello', user: 'alice' }
})
```

## Presence (Quem Esta Online)
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

## Postgres Changes — Como Funciona
```text
[INSERT/UPDATE/DELETE] → [PostgreSQL WAL]
    → [Supabase Realtime server] lê WAL
    → [RLS check] filtra por user
    → [WebSocket] envia para subscribers
```

| Config | Valor | Nota |
|--------|-------|------|
| Publication | `supabase_realtime` | Tabela deve estar na publication |
| Habilitar | `ALTER PUBLICATION supabase_realtime ADD TABLE orders;` | Por tabela |
| Filter server-side | `filter: 'column=eq.value'` | Reduz tráfego |
| RLS | Automático se habilitado | User só vê rows que pode SELECT |

## Anti-Patterns
| Anti-Pattern | Risco | Fix |
|-------------|-------|-----|
| Subscribe `*` (todas tabelas) | WAL overhead, memória, CPU | Filtrar por tabela + evento |
| Sem unsubscribe em unmount | Conexões zumbi, memory leak | `channel.unsubscribe()` em cleanup |
| Broadcast para notificações críticas | Mensagem perdida = dado perdido | Usar Postgres Changes + tabela |
| Presence sem throttle | Estado sync a cada keypress | Debounce 1-5s no track() |
| Ignorar RLS em Changes | User vê dados de outros users | Habilitar RLS na tabela |

## Golden Rules
- USE Broadcast para efêmero (typing indicators, cursor position)
- USE Postgres Changes para dados que precisam persistir
- USE Presence para "quem está online" com sync automático
- FILTRE sempre: tabela + evento + filter column quando possível
- HABILITE a tabela na publication antes de subscribir

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
