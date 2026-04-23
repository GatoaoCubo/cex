---
kind: knowledge_card
id: bld_knowledge_card_guardrail
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for guardrail production — safety boundary specification
sources: NIST AI RMF, OWASP LLM Top 10, Anthropic Usage Policy, AWS Bedrock Guardrails
quality: 9.1
title: "Knowledge Card Guardrail"
version: "1.0.0"
author: n03_builder
tags: [guardrail, builder, examples]
tldr: "Golden and anti-examples for guardrail construction, demonstrating ideal structure and common pitfalls."
domain: "guardrail construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Domain Knowledge: guardrail
## Executive Summary
Guardrails are external safety boundaries that prevent agents from causing damage. They define what must NEVER happen, with enforcement modes (block, warn, log) and severity levels. Guardrails are applied externally — agents cannot disable their own guardrails. They differ from permissions (access control), laws (operational rules), quality gates (scoring barriers), and lifecycle rules (temporal policies).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P11 (governance/safety) |
| Enforcement modes | block, warn, log |
| Severity levels | critical, high, medium, low |
| Key fields | scope, rules, severity, enforcement, bypass_policy |
| Required | Concrete violation examples |
| Emergency bypass | Allowed with audit trail |
## Patterns
- **Severity determines response**: enforcement escalates with severity
| Severity | Enforcement | Response |
|----------|-------------|----------|
| critical | block + alert | Immediate halt, notify operator |
| high | block | Prevent action, log violation |
| medium | warn | Allow with warning, log |
| low | log | Record only, no interruption |
- **External application**: guardrails are imposed ON agents, not BY agents — prevents self-disabling
| Source | Concept | Application |
|--------|---------|-------------|
| NIST AI RMF | Risk management framework | Severity classification |
| OWASP LLM Top 10 | LLM security risks | Violation categories |
| Anthropic Usage Policy | Acceptable use constraints | Content boundaries |
| AWS Bedrock | Content filters, denied topics | Block/warn/log modes |
- **Concrete rules**: "NEVER execute rm -rf on production paths" not "be careful with deletions"
- **Specific violation examples**: each rule includes 2+ concrete violations that would trigger it
- **Emergency bypass**: every guardrail has a documented bypass procedure with mandatory audit trail
- **Scope declaration**: each guardrail declares what it protects (agent, pipeline, output, or system)
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Vague rule ("be responsible") | Not enforceable; no clear trigger |
| No violation examples | Cannot test enforcement; ambiguous scope |
| No bypass procedure | Emergencies blocked with no recovery path |
| Agent self-managed guardrails | Agent disables own safety; defeats purpose |
| critical severity with log-only | Critical violations logged but not blocked |
| No severity classification | All violations treated equally; alert fatigue |
## Application
1. Identify risk: what damage could this agent/pipeline cause?
2. Write concrete rules: specific, enforceable, with measurable triggers
3. Classify severity: critical, high, medium, or low per rule
4. Set enforcement: block/warn/log matching severity
5. Document violation examples: 2+ concrete cases per rule
6. Define bypass: emergency procedure with audit trail
## References
- NIST AI RMF: AI Risk Management Framework
- OWASP: Top 10 for Large Language Model Applications
- AWS Bedrock: Guardrails configuration and content filtering
- Anthropic: Usage Policy and safety boundaries
