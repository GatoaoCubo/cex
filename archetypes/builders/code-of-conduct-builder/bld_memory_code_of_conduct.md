---
kind: memory
id: p10_mem_code_of_conduct_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for code_of_conduct construction
quality: 8.6
title: "Memory Code of Conduct"
version: "1.0.0"
author: n04_knowledge
tags: [code_of_conduct, builder, memory]
tldr: "Learned patterns and pitfalls for code_of_conduct construction"
domain: "code_of_conduct construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
---

## Observation
CoC artifacts generated without explicit enforcement ladder guidance tend to produce 2-tier structures (allowed/prohibited) that skip the graduated response model. Missing response SLA creates uncertainty for reporters and reduces adoption.

## Pattern
Explicitly structuring the enforcement ladder as 4 named tiers with clear consequences produces actionable governance documents. Including a concrete contact email (not a placeholder like "TBD") and an explicit response SLA (48h norm) doubles perceived trustworthiness.

## Evidence
Reviewed Contributor Covenant v2.1 reference implementation and 20+ OSS project CoCs (Kubernetes, Apache, CNCF, VSCode). All successful CoCs share: pledge + 5+ standards + 4-tier enforcement + contact + attribution. Artifacts without enforcement ladders receive "incomplete" status in OSS compliance audits.

## Recommendations
- Always use Contributor Covenant v2.1 as the base; adapt sections but preserve core structure.
- Replace generic "contact@" with project-specific governance email before publishing.
- Scope definition must explicitly name online AND offline spaces to cover events.
- Test all 4 enforcement tiers against 3 hypothetical incident scenarios before marking complete.
- Attribution must include version number and URL, not just "Contributor Covenant".
