---
id: p12_dr_software_project
kind: dispatch_rule
pillar: P12
title: "Dispatch Rule — Software Project"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.0
tags: [dispatch-rule, software-project, n03, routing]
tldr: "Routes software engineering tasks to N03: implement, deploy, test, lint, docker, scaffold, review. Confidence 0.85-0.95. Excludes pure research (N01), marketing (N02), schema design (N04)."
density_score: 0.88
scope: software-engineering
keywords: [implement, deploy, test, scaffold, docker, cicd, review, lint, implementar, testar, deploy]
priority: 8
confidence_threshold: 0.75
fallback: clarify
routing_strategy: keyword_match
---

# Dispatch Rule: Software Project

## Routing Keywords

| Keywords | Language | Confidence |
|----------|----------|------------|
| implement, code, runtime, executable | EN | 0.95 |
| scaffold, project, setup, init | EN | 0.90 |
| test, pytest, coverage, fixture | EN | 0.90 |
| deploy, railway, docker, container | EN | 0.90 |
| lint, ruff, format, mypy | EN | 0.85 |
| review, PR, pull request, code review | EN | 0.85 |
| cicd, pipeline, workflow, actions | EN | 0.85 |
| implementar, testar, deploiar | PT | 0.90 |

## Decision Matrix

| Signal | Route | Conf |
|--------|-------|------|
| "implement [spec] in Python" | N03 software-project-builder | 0.95 |
| "scaffold new project for [X]" | N03 scaffold command | 0.90 |
| "write tests for [module]" | N03 test command | 0.90 |
| "deploy to Railway/staging" | N03 deploy command | 0.90 |
| "create Dockerfile for [project]" | N03 docker command | 0.85 |
| "setup CI/CD for [repo]" | N03 ci command | 0.85 |
| "review PR #42" | N03 review command | 0.85 |
| "research [topic]" | NOT N03 → N01 | 0.00 |
| "write marketing copy" | NOT N03 → N02 | 0.00 |
| "design database schema" | NOT N03 → N04 | 0.00 |
| "monitor production" | NOT N03 → N05 | 0.00 |

## Cross-Nucleus Handoffs

| From | To N03 | Trigger | What N03 Receives |
|------|--------|---------|-------------------|
| N01 | N03 | "implement pipeline" | Builder ISOs + instance config |
| N02 | N03 | "implement publisher" | Builder ISOs + instance config |
| N04 | N03 | "deploy migrations" | SQL files + Supabase config |
| N06 | N03 | "implement billing" | Integration spec |
| N07 | N03 | "update CEX tool" | Tool path + requirements |
