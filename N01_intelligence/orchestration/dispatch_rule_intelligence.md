---
id: p12_dr_research
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2023-10-15
updated: 2023-10-15
author: dispatch-rule-builder
domain: research
quality: null
tags: [dispatch, research, shaka]
tldr: Route research-related tasks to the agent_node specializing in research
scope: research
keywords: [pesquisar, research, mercado, market, concorrente, competitor, analise, analysis]
agent_node: shaka
model: sonnet
priority: 8
confidence_threshold: 0.70
fallback: pytha
routing_strategy: hybrid

---
# Research Dispatch Rule

## Purpose
Routes research-related tasks, including market analysis and competitor intelligence, to the researcher agent_node. This ensures tasks are handled by specialized resources suited for in-depth analyses and research processes.

## Keyword Rationale
Keywords are selected to cover research-related terminology in both English and Portuguese. This bilingual approach allows for catching tasks that involve "pesquisar" in Portuguese or "research" and similar tasks in English, ensuring broad coverage within the research scope.

## Fallback Logic
If the agent_node `shaka` is unavailable, tasks are routed to `pytha` as a fallback, which can perform generalized tasks and handle research outputs effectively without specialized research-optimized capabilities.

---