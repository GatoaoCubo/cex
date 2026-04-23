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
related:
  - course-module-builder
  - bld_collaboration_content_filter
  - p03_sp_course_module_builder
  - bld_collaboration_faq_entry
  - p05_kc_course_module
  - bld_collaboration_response_format
  - bld_collaboration_multimodal_prompt
  - bld_tools_course_module
  - bld_collaboration_prompt_technique
  - bld_collaboration_agentic_rag
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[course-module-builder]] | upstream | 0.34 |
| [[bld_collaboration_content_filter]] | sibling | 0.26 |
| [[p03_sp_course_module_builder]] | upstream | 0.25 |
| [[bld_collaboration_faq_entry]] | sibling | 0.23 |
| [[p05_kc_course_module]] | upstream | 0.23 |
| [[bld_collaboration_response_format]] | sibling | 0.23 |
| [[bld_collaboration_multimodal_prompt]] | sibling | 0.22 |
| [[bld_tools_course_module]] | upstream | 0.22 |
| [[bld_collaboration_prompt_technique]] | sibling | 0.22 |
| [[bld_collaboration_agentic_rag]] | sibling | 0.22 |
