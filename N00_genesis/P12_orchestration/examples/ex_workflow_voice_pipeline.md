---
id: p12_wf_voice_pipeline
name: voice-pipeline
description: Pipeline completo de voz via WhatsApp - boot/shutdown de Bridge + Daemon + Monitor
version: 1.0.0
pillar: P12
kind: workflow
8f: F8_collaborate
created: 2026-03-22
updated: 2026-03-22
author: operations_agent
domain: execution
quality: 9.1
tags: [voice, whatsapp, pipeline, stt, tts, bridge]
tldr: Pipeline WhatsApp Voice end-to-end - Audio>Bridge(:3847)>STT(whisper)>Intent(Claude)>Plan>TTS(edge-tts)>Audio
user_invocable: true
trigger: /voice-pipeline
when_to_use: Ligar/desligar pipeline de voz WhatsApp, checar status, troubleshoot
when_not_to_use: Voice em browser (usar MCP voice), TTS isolado (usar tts_engine.py)
phases:
  - Boot (wa_boot.cmd)
  - Monitor (wa_health.cmd)
  - Shutdown (wa_shutdown.cmd)
examples:
  - /voice-pipeline start
  - /voice-pipeline status
  - /voice-pipeline stop
density_score: 0.85
linked_artifacts:
  agent: records/agents/voice-agent/README.md
  kc: records/pool/knowledge/KC_VOICE_PIPELINE.md
related:
  - p01_kc_audio_tool
  - p01_kc_perception_tools
  - voice-pipeline-builder
  - bld_collaboration_audio_tool
  - bld_collaboration_voice_pipeline
  - bld_knowledge_card_audio_tool
  - bld_memory_voice_pipeline
  - tts-provider-builder
  - p04_webhook_whatsapp_bridge
  - bld_knowledge_card_voice_pipeline
---

# Voice Pipeline Skill

## Purpose

Pipeline completo de voz via WhatsApp: Audio recebido > Bridge Node.js (porta 3847) > STT (faster-whisper, local CUDA) > Intent detection (Claude) > Plan execution > TTS (edge-tts, Microsoft gratis) > Audio de volta ao WhatsApp. 3 componentes: Bridge, Voice Daemon, Monitor.

## Workflow Phases

### Phase 1: Boot
**Input**: nenhum (ou `--component bridge|daemon|monitor`)
**Action**: Executar `wa_boot.cmd` que inicia Bridge + Daemon + Monitor em janelas separadas
**Output**: 3 processos rodando, `localhost:3847/health` respondendo

### Phase 2: Monitor
**Input**: nenhum
**Action**: Executar `wa_health.cmd` para checar status de todos componentes
**Output**: Status report (connected, uptime, msgs processadas, memoria)

### Phase 3: Shutdown
**Input**: nenhum
**Action**: Executar `wa_shutdown.cmd` que para todos componentes gracefully
**Output**: Todos processos encerrados

## Components

| Componente | Funcao | Processo | Porta |
|------------|--------|----------|-------|
| Bridge | Conexao WhatsApp via whatsapp-web.js | `node bridge.js` | 3847 |
| Voice Daemon | STT + Intent + Plan + TTS + Dispatch | `python voice_daemon.py` | - |
| Monitor | Health check periodico | `pythonw wa_monitor.py --daemon` | - |

## API Endpoints

| Endpoint | Metodo | Funcao |
|----------|--------|--------|
| `localhost:3847/health` | GET | Status completo |
| `localhost:3847/status` | GET | Conexao + QR |
| `localhost:3847/messages` | GET | Mensagens pendentes |
| `localhost:3847/send/text` | POST | Enviar texto `{to, text}` |
| `localhost:3847/send/audio` | POST | Enviar audio `{to, filePath}` |

## Tech Stack

| Layer | Tecnologia | Nota |
|-------|-----------|------|
| STT | faster-whisper (local) | `large-v3` (CUDA) ou `base` (CPU) |
| STT fallback | OpenAI Whisper API | Se local falhar |
| TTS | edge-tts (Microsoft) | Gratis, `pt-BR-FranciscaNeural` |
| Intent | Claude API | Classificacao de intent do audio |
| Bridge | whatsapp-web.js | Node.js, reconexao automatica |

## Anti-Patterns

- Boot sem checar porta 3847 ocupada: conflito de processo — `netstat -aon | findstr 3847`
- Pular QR scan na primeira vez: bridge fica em loop de retry — escanear manualmente
- Rodar STT large-v3 sem CUDA: lento demais para real-time — usar `base` em CPU
- Nao configurar grupo filtro: processa mensagens de todos os chats — filtrar por group ID

## Troubleshooting

| Problema | Solucao |
|----------|---------|
| Bridge nao conecta | Checar janela, pode pedir QR |
| Daemon nao responde | `wa_health.cmd`, restart com `wa_boot.cmd` |
| Audio nao chega | `localhost:3847/health` connected=true |
| QR pedido | Sessao expirou, escanear novamente |
| Porta ocupada | `netstat -aon \| findstr 3847` achar PID |

## Cross-References

- `voice-agent`: Interface de voz para Claude Code (MCP voice)
- `tts_engine.py`: TTS engine standalone multi-backend
- `voice_bridge.py`: Mic voice bridge para uso local (nao WhatsApp)

## Usage

```bash
/voice-pipeline start               # Boot all 3 components
/voice-pipeline status              # Health check
/voice-pipeline stop                # Graceful shutdown
/voice-pipeline start --component bridge  # Single component
```

## Input / Output

```yaml
input:
  command: enum         # start|stop|status
  component: enum      # bridge|daemon|monitor|all (default: all)

output:
  status: object       # {bridge: connected, daemon: running, monitor: active}
  health_url: string   # localhost:3847/health
```

## Metrics
| Metrica | Threshold | Acao |
|---------|-----------|------|
| Bridge uptime | > 99% | Restart if disconnected > 60s |
| STT latency | < 3s (GPU), < 10s (CPU) | Switch model size |
| TTS generation | < 2s per message | Check edge-tts availability |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_audio_tool]] | upstream | 0.33 |
| [[p01_kc_perception_tools]] | upstream | 0.30 |
| [[voice-pipeline-builder]] | upstream | 0.28 |
| [[bld_collaboration_audio_tool]] | related | 0.27 |
| [[bld_collaboration_voice_pipeline]] | related | 0.26 |
| [[bld_knowledge_card_audio_tool]] | upstream | 0.26 |
| [[bld_memory_voice_pipeline]] | upstream | 0.25 |
| [[tts-provider-builder]] | upstream | 0.23 |
| [[p04_webhook_whatsapp_bridge]] | upstream | 0.23 |
| [[bld_knowledge_card_voice_pipeline]] | upstream | 0.23 |
