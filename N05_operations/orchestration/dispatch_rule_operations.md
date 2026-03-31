---
id: p12_dr_operations_nucleus
kind: dispatch_rule
pillar: P12
version: 3.0.0
created: 2026-03-30
updated: 2026-03-31
author: n05_operations
domain: operations-engineering
quality: null
tags: [dispatch_rule, N05, operations, devops, routing]
tldr: Route execution-heavy repository tasks to N05 when the answer depends on code inspection, testing, debugging, deploy safety, CI/CD, or infrastructure validation.
scope: operations
keywords: [review, code-review, reviewer, test, testar, pytest, flaky, failing, debug, bug, traceback, deploy, release, ci, cd, pipeline, workflow, docker, logs, rollback, monitor]
agent_node: operations_nucleus
model: gpt-5.4
priority: 9
confidence_threshold: 0.82
fallback: builder_hub
routing_strategy: intent_plus_execution_requirement
---

# Operations Dispatch Rule

## Purpose

Dispatch to N05 when the user needs an answer grounded in repository execution,
runtime evidence, release safety, or delivery-system diagnosis.

## Route To N05 When

- The task requires running tests, builds, linters, containers, or validation commands.
- The user asks for code review, especially with risk analysis, blockers, or missing tests.
- The task involves debugging a failure, reproducing a bug, or reading traces/logs.
- CI/CD is red, unstable, or suspected to be misconfigured.
- Deployment readiness, rollback planning, or environment compatibility must be assessed.
- Infra, Docker, health checks, observability, or startup sequencing are part of the problem.

## Strong Positive Signals

- "review this diff"
- "fix failing tests"
- "debug this bug"
- "pipeline is broken"
- "validate this deploy"
- "check docker/compose"
- "is this safe to release?"
- "why is CI flaky?"

## Do Not Route To N05 When

- The primary work is authoring or redesigning artifacts without execution pressure
- The task is research-heavy and not tied to repository behavior
- The request is commercial, persuasive, or pricing-oriented

## Mixed-Intent Policy

If the request includes both artifact synthesis and operational execution:

- N05 owns the execution, review, test, debug, and deploy portions.
- `builder_hub` is fallback only for pure artifact construction that does not depend on runtime evidence.

## Decision Rule

If answering correctly requires touching the actual repo state or proving runtime
behavior, dispatch to N05.
