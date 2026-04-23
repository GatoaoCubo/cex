---
kind: collaboration
id: bld_collaboration_code_of_conduct
pillar: P12
llm_function: COLLABORATE
purpose: How code_of_conduct-builder works in crews with other builders
quality: 8.9
title: "Collaboration Code of Conduct"
version: "1.0.0"
author: n04_knowledge
tags: [code_of_conduct, builder, collaboration]
tldr: "How code_of_conduct-builder works in crews with other builders"
domain: "code_of_conduct construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_architecture_kind
  - bld_collaboration_github_issue_template
  - bld_collaboration_ai_rmf_profile
  - bld_collaboration_safety_hazard_taxonomy
  - code-of-conduct-builder
  - bld_collaboration_builder
  - bld_collaboration_llm_evaluation_scenario
  - bld_collaboration_gpai_technical_doc
  - kind-builder
  - bld_collaboration_agent_computer_interface
---

## Crew Role
Produces code of conduct documents defining behavioral standards and enforcement procedures for OSS projects. The code of conduct is the community safety layer, placed before contributor_guide-builder (technical onboarding) and github_issue_template-builder (issue reporting).

## Receives From
| Builder                    | What                          | Format   |
|----------------------------|-------------------------------|----------|
| contributor_guide-builder  | Project community norms input | Markdown |
| context_doc-builder        | Project scope + team structure| Markdown |
| knowledge_card-builder     | Community governance KC       | Markdown |

## Produces For
| Builder                         | What                           | Format   |
|---------------------------------|--------------------------------|----------|
| github_issue_template-builder   | CoC reference for issue bodies | Markdown |
| landing_page-builder            | Community health badge signal  | Markdown |
| contributor_guide-builder       | CoC link + enforcement summary | Markdown |

## Boundary
Does NOT handle technical contribution workflows (contributor_guide-builder), governance/voting processes (governance artifacts), or legal compliance documentation. Enforcement decisions remain with human maintainers; this builder produces the framework, not the decisions.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | upstream | 0.34 |
| [[bld_collaboration_github_issue_template]] | sibling | 0.31 |
| [[bld_collaboration_ai_rmf_profile]] | sibling | 0.31 |
| [[bld_collaboration_safety_hazard_taxonomy]] | sibling | 0.31 |
| [[code-of-conduct-builder]] | upstream | 0.31 |
| [[bld_collaboration_builder]] | sibling | 0.30 |
| [[bld_collaboration_llm_evaluation_scenario]] | sibling | 0.30 |
| [[bld_collaboration_gpai_technical_doc]] | sibling | 0.30 |
| [[kind-builder]] | upstream | 0.29 |
| [[bld_collaboration_agent_computer_interface]] | sibling | 0.28 |
