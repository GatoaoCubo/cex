---
id: n00_p04_kind_index
kind: knowledge_card
pillar: P04
nucleus: n00
title: "P04 Tools -- Kind Index"
version: 1.0
quality: null
tags: [index, p04, archetype, n00]
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+schema F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Master index of all 34 kinds in pillar P04. Reference for /mentor, nucleus builders, and the 8F pipeline.

## Pillar: P04 Tools
Executable capabilities: API clients, browser automation, code executors, MCP servers, search tools, and social publishers. The action layer that extends agent reach into external systems.

## Kinds in P04

| Kind | Purpose | Primary Nucleus | Builder |
|------|---------|-----------------|---------|
| `action_paradigm` | How agents execute actions in environments | N05 | `action_paradigm-builder` |
| `agent_name_service_record` | IETF ANS + CNCF AgentDNS registry record for agent discovery: name, en | N05 | `agent_name_service_record-builder` |
| `api_client` | Typed REST/GraphQL/gRPC API client | N05 | `api_client-builder` |
| `audio_tool` | Speech-to-text, text-to-speech, audio analysis | N05 | `audio_tool-builder` |
| `browser_tool` | Browser automation: DOM parsing, navigation, interaction, screenshot | N05 | `browser_tool-builder` |
| `cli_tool` | Ferramenta CLI | N05 | `cli_tool-builder` |
| `code_executor` | Sandboxed runtime for code execution (Docker, E2B, Jupyter) | N05 | `code_executor-builder` |
| `computer_use` | Screen, keyboard, and mouse control by LLM (Anthropic, browser-use) | N05 | `computer_use-builder` |
| `daemon` | Processo background | N05 | `daemon-builder` |
| `db_connector` | Structured database connector (SQL, GraphQL, REST-to-DB) | N05 | `db_connector-builder` |
| `diff_strategy` | Change application and matching algorithm | N05 | `diff_strategy-builder` |
| `document_loader` | Ingere arquivos e converte em chunks (PDF, HTML, CSV, etc) | N05 | `document_loader-builder` |
| `function_def` | LLM-callable function definition (JSON Schema tool) | N05 | `function_def-builder` |
| `hook` | Pre/post processing hook | N05 | `hook-builder` |
| `hook_config` | Hook lifecycle configuration for builder execution | N05 | `hook_config-builder` |
| `mcp_app_extension` | MCP Apps Extension (SEP-1865): app manifest, install/launch/terminate  | N05 | `mcp_app_extension-builder` |
| `mcp_server` | Servidor MCP (tools + resources) | N05 | `mcp_server-builder` |
| `multi_modal_config` | Input format, resolution, encoding, and routing rules for multi-modal  | N05 | `multi_modal_config-builder` |
| `notifier` | Push notification delivery (email, SMS, Slack, Discord) | N05 | `notifier-builder` |
| `plugin` | Extensao plugavel | N05 | `plugin-builder` |
| `research_pipeline` | 7-stage research engine: INTENT>PLAN>RETRIEVE>RESOLVE>SCORE>SYNTHESIZE | N05 | `research_pipeline-builder` |
| `retriever` | Busca vetorial/keyword/hibrida sobre store local (RAG core) | N05 | `retriever-builder` |
| `sdk_example` | SDK code example showing canonical integration patterns per language | N05 | `sdk_example-builder` |
| `search_strategy` | Inference-time compute allocation strategy | N05 | `search_strategy-builder` |
| `search_tool` | Busca web, semantica ou hibrida (Tavily, Serper, Perplexity) | N05 | `search_tool-builder` |
| `skill` | Reusable capability with trigger + phases (AgentSkills.io / Semantic K | N05 | `skill-builder` |
| `social_publisher` | Automatic publishing agent: LOAD>FETCH>SELECT>GENERATE>OPTIMIZE>HASHTA | N02 | `social_publisher-builder` |
| `stt_provider` | Speech-to-text provider integration | N05 | `stt_provider-builder` |
| `supabase_data_layer` | Supabase-specific data layer — tables, RLS policies, edge functions, s | N05 | `supabase_data_layer-builder` |
| `toolkit` | Collection of callable tools with auto JSON Schema | N05 | `toolkit-builder` |
| `tts_provider` | Text-to-speech provider integration | N05 | `tts_provider-builder` |
| `vision_tool` | Image analysis, OCR, screenshot interpretation | N05 | `vision_tool-builder` |
| `voice_pipeline` | End-to-end voice agent architecture definition | N05 | `voice_pipeline-builder` |
| `webhook` | Endpoint HTTP event-driven inbound/outbound | N05 | `webhook-builder` |

## Usage
```python
# Build any of these via 8F:
python _tools/cex_8f_runner.py "your intent" --kind {kind} --execute
```

## CoC Hierarchy Note
These 34 kinds follow the convention-over-configuration hierarchy: each instance
(N01-N07) inherits this schema and fills the variables for its sin lens.
N00_genesis holds the canonical archetype; nuclei hold the instantiated versions.
