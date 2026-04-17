---
id: p02_ms_conversational_agent
kind: memory_scope
pillar: P02
title: Conversational Agent Memory (Buffer + Summary + Entity)
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: agent_memory
quality: 9.1
tags: [memory-scope, conversational, buffer, summary, entity, redis, session, mem0]
tldr: Configuracao de memoria para agente conversacional com 3 camadas — buffer (ultimas 10 msgs), summary (compressao apos 10), entity (entidades extraidas) — backend Redis com TTL 3600s
when_to_use: Agentes que mantam conversa multi-turn com usuario e precisam lembrar contexto recente + entidades mencionadas
---

# Memory Scope: Conversational Agent (3-Layer)

## Overview
Define o escopo de memoria para um agente conversacional multi-turn (ex: mentor-agent, gateway-agent). Tres camadas complementares garantem que o agente lembra o contexto imediato (buffer), o resumo da conversa ate agora (summary), e entidades especificas mencionadas (entity). Backend Redis garante persistencia entre requests com TTL de sessao.

## Memory Types
| Layer | Type | Purpose | Token Budget |
|-------|------|---------|-------------|
| 1 | Buffer | Ultimas N mensagens raw | ~2000 tokens (10 msgs) |
| 2 | Summary | Compressao progressiva de msgs antigas | ~500 tokens (fixo) |
| 3 | Entity | Entidades extraidas (pessoas, produtos, datas) | ~300 tokens (top 20 entities) |

## Parameters
| Param | Value | Rationale |
|-------|-------|-----------|
| buffer_size | 10 messages | 10 msgs = ~2000 tokens. Alem disso, custo > beneficio |
| summary_trigger | buffer > 10 msgs | Quando buffer excede 10, msgs antigas sao sumarizadas |
| summary_model | haiku | Sumarizacao e tarefa simples, haiku e suficiente e 10x mais barato |
| summary_max_tokens | 500 | Resumo compacto, nao transcript |
| entity_types | [person, product, date, price, marketplace, agent] | Tipos relevantes para e-commerce organization |
| entity_max | 20 | Top 20 entidades por recencia + frequencia |
| backend | Redis | Sub-ms latency, TTL nativo, pub/sub para multi-instance |
| redis_url | redis://localhost:6379/0 | Instancia local para dev; Railway Redis para prod |
| ttl | 3600 | 1 hora de inatividade = sessao expirada |
| scope | session | Memoria isolada por session_id, nao compartilhada entre usuarios |
| serialization | JSON | Simples, debuggavel, compativel com Redis strings |

## Architecture
```text
[User Message] --> [Entity Extractor] --> [Entity Store (Redis)]
       |                                        |
       v                                        |
[Buffer Memory (last 10)]                       |
       |                                        |
       |-- buffer > 10? --> [Summary Generator]  |
       |                         |               |
       |                    [Summary Store]      |
       |                         |               |
       v                         v               v
[Context Assembly: buffer + summary + entities]
       |
       v
[LLM Call with assembled context]
```

## Implementation
```python
from langchain.memory import ConversationBufferWindowMemory, ConversationSummaryMemory
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_anthropic import ChatAnthropic

# Redis-backed message history
history = RedisChatMessageHistory(
    session_id="user_abc_session_001",
    url="redis://localhost:6379/0",
    ttl=3600,
)

# Layer 1: Buffer (last 10)
buffer_memory = ConversationBufferWindowMemory(
    k=10,
    chat_memory=history,
    return_messages=True,
    memory_key="buffer_context",
)

# Layer 2: Summary (compressed history)
summary_memory = ConversationSummaryMemory(
    llm=ChatAnthropic(model="claude-haiku-4-5-20251001"),
    chat_memory=history,
    return_messages=False,
    memory_key="summary_context",
    max_token_limit=500,
)

# Layer 3: Entity (extracted entities)
entity_memory = ConversationEntityMemory(
    llm=ChatAnthropic(model="claude-haiku-4-5-20251001"),
    chat_memory=history,
    memory_key="entity_context",
    entity_store=RedisEntityStore(
        session_id="user_abc_session_001",
        url="redis://localhost:6379/0",
        ttl=3600,
    ),
)
```

## Context Assembly Order
```python
def assemble_context(buffer, summary, entities):
    """Ordem importa: summary primeiro (background), entities (referencia), buffer por ultimo (recente)."""
    return f"""## Conversation Summary
{summary}

## Known Entities
{format_entities(entities)}

## Recent Messages
{format_buffer(buffer)}"""
```

## Redis Key Schema
```
organization:memory:{session_id}:messages     -> List<JSON>   (buffer)
organization:memory:{session_id}:summary      -> String       (summary text)
organization:memory:{session_id}:entities     -> Hash          (entity_name -> description)
organization:memory:{session_id}:metadata     -> Hash          (created_at, last_active, msg_count)
```

## Lifecycle
| Event | Action |
|-------|--------|
| Session start | Create Redis keys, initialize empty buffer |
| Message received | Append to buffer, extract entities, update last_active |
| Buffer > 10 | Summarize oldest 5 msgs, remove from buffer, append to summary |
| TTL expired (1h idle) | Redis auto-deletes all session keys |
| Explicit logout | Flush all keys for session_id immediately |

## When NOT to Use
- Stateless single-turn agents (ex: formatter, parser) — sem necessidade de memoria
- Long-term cross-session memory — usar Mem0 ou organization learning memory
- Shared memory between agents — usar session_state (P10) com pub/sub

## Related
- `ex_agent_gateway.md` — Gateway agent que usa este memory scope
- `ex_boot_config_edison_claude.md` — Boot config (memoria e efemera por sessao de agent_group)
- `records/core/learning/memory/` — organization long-term memory (diferente de session memory)
