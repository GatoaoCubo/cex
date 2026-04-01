---
id: p12_dr_creation
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: dispatch-rule-builder
domain: creation
quality: 8.5
tags: [dispatch, creation, build, edison, artifact]
tldr: Route creation, building and scaffolding tasks to builder agent_node
scope: creation
keywords: [create, criar, build, construir, scaffold, implementar, implement, generate, gerar, develop, desenvolver, construct, make, fazer, produce, produzir]
agent_node: edison
model: opus
priority: 9
confidence_threshold: 0.75
fallback: shaka
conditions:
  exclude_domains: [research, marketing, deployment]
routing_strategy: hybrid
density_score: 0.81
---
# creation Dispatch Rule

## Purpose
Routes artifact creation, building, and scaffolding tasks to the builder agent_node. Edison specializes in following the 8F pipeline to produce structured artifacts across all 99 CEX kinds with proper validation and compilation.

## Keyword Rationale
Bilingual PT/EN coverage captures both Portuguese commands ("criar", "construir", "implementar") and English task descriptions ("create", "build", "scaffold"). Action verbs like "generate", "develop", "construct", "produce" catch adjacent creation intents. "Make" and "fazer" handle casual creation requests.

## Fallback Logic
Researcher (shaka) handles creation requests when builder is unavailable, as research agents can analyze requirements and produce initial drafts, though without the specialized 8F pipeline enforcement that edison provides.