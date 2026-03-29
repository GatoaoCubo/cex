---

id: p12_dr_operations
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2023-10-23
updated: 2023-10-23
author: dispatch-rule-specialist
domain: operations
quality: null
tags: [dispatch, operations, vector]
tldr: Route operational tasks to the operations satellite vector with fallback to compass
scope: operations
keywords: [executar, execute, depurar, debug, testar, test, implementar, deploy, pipeline, wire]
satellite: vector
model: opus
priority: 7
confidence_threshold: 0.70
fallback: compass

---

# Operations Dispatch Rule

## Purpose
Routes core operational tasks such as executing, deploying, and debugging to the operations satellite "vector". Ensures tasks are efficiently handled by models equipped for execution and pipeline management.

## Keyword Rationale
The keywords cover both Portuguese and English, capturing typical operational command verbs and related terms used in task descriptions. This includes synonyms and action-oriented verbs ensuring wide trigger coverage.

## Fallback Logic
Fallback to the "compass" satellite is activated if the confidence in keyword matching drops below 0.70 or if "vector" is unreachable. This ensures continuity of operations using a capable general-purpose executor.