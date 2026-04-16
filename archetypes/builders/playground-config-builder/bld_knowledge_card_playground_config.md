---
kind: knowledge_card
id: bld_knowledge_card_playground_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for playground_config production
quality: 9.2
title: "Knowledge Card Playground Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [playground_config, builder, knowledge_card]
tldr: "Domain knowledge for playground_config production"
domain: "playground_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Domain Overview
Playground_config artifacts define interactive, try-before-buy evaluation environments for AI products, APIs, and SDKs. The pattern is proven by OpenAI Playground (prompt + model + sampling controls), Anthropic Console, Swagger/OpenAPI "Try It Out" in-browser explorers, Replit and CodeSandbox embed APIs, and JupyterLite WASM kernels. The goal is zero-friction first-touch: the user runs a representative workload with sane defaults, hits resource caps safely, and sees a clear upgrade path to paid tiers.

A playground_config differs from a sandbox_spec: playground optimizes for conversion (low friction, short sessions, shareable URLs), sandbox optimizes for enterprise procurement (strict isolation, audit trails, compliance). Playground sessions are typically rate-limited, time-boxed, stateless, and observable.

## Key Concepts
| Concept | Definition | Source |
|---|---|---|
| Rate-limited session | Per-IP or per-key caps on requests and tokens | OpenAI Playground, Anthropic Console |
| Interactive REPL | Read-eval-print loop in browser | JupyterLite, Replit, CodeSandbox |
| API Try-It-Out | Form-driven API call from docs | Swagger UI, Redoc, Stoplight |
| Embed snippet | iframe or script tag to host playground elsewhere | CodeSandbox, StackBlitz, Replit |
| Activation metric | Instrumented event signaling value realized | PLG literature (Reforge, OpenView) |
| Quota gate | Hard stop that surfaces upgrade prompt | Vercel, Supabase, Stripe test mode |
| Ephemeral state | No persistence across sessions | Firecracker-backed notebook kernels |
| Sharable reproduction | URL encodes prompt + config for collab | OpenAI Playground share links |

## Industry Standards
- OpenAI Playground (prompt + model + temperature + max_tokens reference UX)
- Anthropic Console playground controls
- Swagger UI / OpenAPI 3.1 "Try It Out" spec
- Replit + CodeSandbox embed API contracts
- JupyterLite (WASM Python, pyodide)
- Product-Led Growth activation metric frameworks (Reforge, OpenView)
- JSON Schema draft 2020-12 (config validation)
- 12-Factor App (externalized config principles)

## Common Patterns
1. Pre-filled example prompts that demonstrate the killer use case in under 10 seconds.
2. Hard quotas (token + rate) with inline upgrade CTA when exceeded.
3. Stateless, shareable URLs encoding the full config.
4. Embed mode via iframe with postMessage event bus for analytics.
5. Activation event fires on first successful run; feeds conversion funnel.
6. Ephemeral compute via WASM or Firecracker micro-VMs for isolation.

## Pitfalls
- Generous defaults burn compute budget with zero conversion signal.
- No activation metric -- unable to measure free-to-paid funnel effectiveness.
- Playground treated as a sandbox (over-isolated, slow boot, hurts first-touch UX).
- Missing upgrade CTA at quota wall -- friction without destination.
- No shareable reproduction -- blocks viral loop and support reproducibility.
