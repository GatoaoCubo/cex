---
kind: collaboration
id: bld_collaboration_quickstart_guide
pillar: P12
llm_function: COLLABORATE
purpose: How quickstart_guide-builder works in crews with other builders
quality: 8.9
title: "Collaboration Quickstart Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [quickstart_guide, builder, collaboration]
tldr: "How quickstart_guide-builder works in crews with other builders"
domain: "quickstart_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Creates concise, user-friendly quickstart guides that enable end-users to achieve first-value outcomes with minimal friction. Collaborates with designers, engineers, and product managers to ensure accuracy and clarity.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Engineers     | Technical specifications | Markdown    |  
| Designers     | UI/UX assets          | Figma       |  
| Product Mgmt  | Feature requirements  | Comments    |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Technical Writers | Guide drafts        | Markdown    |  
| Designers     | Visual preview        | HTML        |  
| Product Mgmt  | Summary for review    | Plain text  |  

## Boundary  
Does NOT handle integration details (handled by integration_guide-builder), code examples (handled by sdk_example-builder), or localization (handled by localization-team).
