---
id: p12_dr_operations_nucleus
kind: dispatch_rule
pillar: P12
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: n05_operations
domain: operations-engineering
quality: null
tags: [dispatch, N05, operations, devops]
tldr: Route execution-heavy coding tasks to N05 when the user needs review, tests, debugging, deployment, CI/CD, infrastructure, or monitoring work.
scope: operations
keywords: [review, code-review, testar, test, pytest, debug, bug, failing, deploy, release, ci, cd, pipeline, docker, logs, rollback, monitor]
agent_node: operations_nucleus
model: gpt-5.4
priority: 9
confidence_threshold: 0.78
fallback: builder_hub
routing_strategy: keyword_plus_intent
---

# Operations Dispatch Rule

## Purpose

Send tasks to N05 when the user expects the agent to inspect code, run or fix tests, diagnose failures, harden pipelines, validate deploys, or reason about runtime behavior with operational evidence.

## Positive Routing Signals

- The request mentions failing tests, flaky CI, debugging, logs, stack traces, containers, release readiness, rollout, rollback, or monitoring.
- The task requires shell execution, build/test commands, or repo-level validation instead of pure artifact authoring.
- The user asks for a review and the likely output is findings, risks, and missing validation.

## Negative Routing Signals

- Requests focused on creating new knowledge artifacts without execution urgency route to N03.
- Research-heavy requests without direct repo execution route to N01.
- Commercial or persuasive writing requests route to N06.

## Fallback Logic

Fallback to `builder_hub` only when the task is primarily artifact construction rather than execution. If intent is mixed, N05 keeps ownership of the operational portion and leaves artifact synthesis to the fallback only when necessary.
