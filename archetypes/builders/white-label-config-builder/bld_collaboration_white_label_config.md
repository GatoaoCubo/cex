---
kind: collaboration
id: bld_collaboration_white_label_config
pillar: P12
llm_function: COLLABORATE
purpose: How white_label_config-builder works in crews with other builders
quality: 8.9
title: "Collaboration White Label Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [white_label_config, builder, collaboration]
tldr: "How white_label_config-builder works in crews with other builders"
domain: "white_label_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role
Handles white-label configuration templates, enabling customization of UI/UX elements without altering brand identity or runtime environments.

## Receives From
| Builder       | What                  | Format      |
|---------------|-----------------------|-------------|
| Branding Team | Brand guidelines      | JSON        |
| Environment Team | Environment variables | YAML        |
| Product Team  | Feature flag schemas  | CSV         |

## Produces For
| Builder       | What                  | Format      |
|---------------|-----------------------|-------------|
| Deployment Team | Config files          | JSON        |
| QA Team       | Test scenario configs  | YAML        |
| Compliance Team | Audit trail templates | CSV         |

## Boundary
Does NOT handle brand identity assets (logos, color schemes) or runtime environment variables. Branding Team manages identity; Environment Team manages runtime configs.
