---

id: p12_dr_engineering_nucleus
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2023-10-30
updated: 2023-10-30
author: codex
domain: engineering
quality: null
tags: [dispatch, edison, build, engineering]
tldr: Route engineering tasks to Edison Engineering nucleus for construction and component design.
scope: engineering
keywords: [build, construir, create, criar, component, componente, template, modelo, infra, infraestrutura]
satellite: edison
model: opus
priority: 7
confidence_threshold: 0.75
fallback: gateway
conditions: 
load_balance: false
routing_strategy: keyword_match

---
# Engineering Dispatch Rule

## Purpose
Routes tasks related to engineering, construction, and component design to the Edison Engineering nucleus. This ensures that specialized tasks are handled by a nucleus optimized for construction and meta-construction processes.

## Keyword Rationale
Keywords are selected to cover both English and Portuguese variants, ensuring comprehensive triggering. They focus on terms commonly associated with engineering and construction tasks.

## Fallback Logic
The fallback satellite, gateway, takes over when the primary target, Edison, is unavailable. This ensures tasks don't stall and are rerouted to a general-purpose handler that can address a broad range of execution contexts.

---

This dispatch rule is structured to provide precise routing for engineering tasks, ensuring tasks related to construction and component design reach the correct executor. The bilingual coverage enhances trigger accuracy, and the fallback logic maintains operational continuity.