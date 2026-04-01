---
id: p12_dr_engineering
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: dispatch-rule-builder
domain: engineering
quality: 8.5
tags: [dispatch, engineering, executor, code, development]
tldr: Route engineering, coding, and development tasks to executor agent with opus model for technical implementation
scope: engineering
keywords: [engineering, engenharia, code, código, develop, desenvolver, implement, implementar, build, construir, deploy, implantar, test, testar, debug, debugar, programa, program]
agent_node: executor
model: opus
priority: 8
confidence_threshold: 0.75
fallback: builder
conditions:
  exclude_domains: [research, marketing, knowledge_indexing]
routing_strategy: hybrid
---
# engineering Dispatch Rule

## Purpose
Routes engineering, software development, coding, testing, and deployment tasks to the executor agent. The executor specializes in technical implementation, code review, debugging, testing pipelines, and deployment automation with access to development tools and technical expertise.

## Keyword Rationale
Bilingual PT/EN coverage captures both Portuguese operator commands and English technical documentation. Keywords span the full engineering lifecycle from development (`desenvolver`/`develop`) through deployment (`implantar`/`deploy`) and maintenance (`debug`/`debugar`). Includes both high-level terms (`engineering`/`engenharia`) and specific technical actions (`code`/`código`, `test`/`testar`).

## Fallback Logic
Builder agent handles general construction tasks when executor is unavailable. While executor focuses on code-specific engineering, builder can handle broader technical implementation tasks without specialized development tooling. Provides graceful degradation for engineering requests when primary technical agent is overloaded.