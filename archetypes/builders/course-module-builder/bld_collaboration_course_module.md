---
kind: collaboration
id: bld_collaboration_course_module
pillar: P12
llm_function: COLLABORATE
purpose: How course_module-builder works in crews with other builders
quality: 8.9
title: "Collaboration Course Module"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [course_module, builder, collaboration]
tldr: "How course_module-builder works in crews with other builders"
domain: "course_module construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Coordinates creation of structured course modules, integrating content, assessments, and media into cohesive learning units.  

## Receives From  
| Builder         | What                  | Format      |  
|-----------------|-----------------------|-------------|  
| Content Curator | Learning objectives   | Text        |  
| Assessment Builder | Quizzes/exercises   | JSON        |  
| Media Collector | Video/illustration links | URLs        |  

## Produces For  
| Builder           | What                  | Format      |  
|-------------------|-----------------------|-------------|  
| Content Reviewer  | Draft module          | Markdown    |  
| LMS Integrator    | Configured module     | YAML        |  
| Analytics Tracker | Usage metrics         | CSV         |  

## Boundary  
Does NOT handle user authentication, enrollment management, or prompt/knowledge card creation. These are managed by LMS, enrollment_system, and prompt_template/knowledge_card builders respectively.
