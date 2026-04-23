---
kind: output_template
id: bld_output_template_code_of_conduct
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for code_of_conduct production
quality: 9.1
title: "Output Template Code of Conduct"
version: "1.0.0"
author: n04_knowledge
tags: [code_of_conduct, builder, output_template]
tldr: "Template with vars for code_of_conduct production"
domain: "code_of_conduct construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_examples_code_of_conduct
  - code-of-conduct-builder
  - bld_knowledge_card_code_of_conduct
  - bld_instruction_code_of_conduct
  - p03_sp_code_of_conduct_builder
  - bld_collaboration_code_of_conduct
  - p05_qg_code_of_conduct
  - bld_schema_code_of_conduct
  - bld_tools_code_of_conduct
  - p10_mem_code_of_conduct_builder
---

```markdown
---
id: p05_coc_{{name}}.md
<!-- name: lowercase project identifier, e.g., "myproject" -->
kind: code_of_conduct
pillar: P05
title: "{{project_name}} Code of Conduct"
<!-- project_name: Display name of the project, e.g., "MyProject" -->
contact_email: "{{contact_email}}"
<!-- contact_email: Reporting channel, e.g., "conduct@myproject.org" -->
enforcement_version: "2.1"
<!-- enforcement_version: Contributor Covenant version used as base (default: "2.1") -->
scope: "online_and_offline"
<!-- scope: "online_and_offline" (recommended) or "online_only" -->
response_sla: "{{response_sla}}"
<!-- response_sla: Max response time for reports, e.g., "48h" -->
quality: null
version: "1.0.0"
created: "{{created_date}}"
updated: "{{created_date}}"
---

# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders of **{{project_name}}** pledge to make
participation in our community a harassment-free experience for everyone,
regardless of age, body size, visible or invisible disability, ethnicity, sex
characteristics, gender identity and expression, level of experience, education,
socio-economic status, nationality, personal appearance, race, caste, color,
religion, or sexual identity and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members
- Acknowledging and crediting the contributions of others

Examples of unacceptable behavior:

- The use of sexualized language or imagery, and sexual attention or advances
- Trolling, insulting or derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information without their explicit permission
- Sustained disruption of community discussions or events
- Other conduct which could reasonably be considered inappropriate in a professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards
and will take appropriate and fair corrective action in response to any behavior
deemed inappropriate, threatening, offensive, or harmful.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces (online
and offline, including events and conferences).

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at **{{contact_email}}**.
All complaints will be reviewed and investigated promptly and fairly.
All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

### Enforcement Guidelines

**1. Correction**
Community Impact: Use of inappropriate language or other unprofessional behavior.
Consequence: A private written warning and clarification of expected behavior.

**2. Warning**
Community Impact: A violation through a single incident or series of actions.
Consequence: A warning with consequences for continued behavior. No interaction
with the people involved for a specified period.

**3. Temporary Ban**
Community Impact: A serious violation of community standards, including sustained inappropriate behavior.
Consequence: Temporary ban from any form of interaction or public communication with the community.

**4. Permanent Ban**
Community Impact: Demonstrating a pattern of violation or harassment of individuals.
Consequence: A permanent ban from all forms of public interaction within the community.

## Attribution

This Code of Conduct is adapted from the
[Contributor Covenant](https://www.contributor-covenant.org), version {{enforcement_version}}.

Community Impact Guidelines were inspired by
[Mozilla's code of conduct enforcement ladder](https://github.com/mozilla/diversity).
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_code_of_conduct]] | downstream | 0.60 |
| [[code-of-conduct-builder]] | related | 0.46 |
| [[bld_knowledge_card_code_of_conduct]] | upstream | 0.43 |
| [[bld_instruction_code_of_conduct]] | upstream | 0.35 |
| [[p03_sp_code_of_conduct_builder]] | upstream | 0.34 |
| [[bld_collaboration_code_of_conduct]] | downstream | 0.28 |
| [[p05_qg_code_of_conduct]] | downstream | 0.27 |
| [[bld_schema_code_of_conduct]] | downstream | 0.26 |
| [[bld_tools_code_of_conduct]] | upstream | 0.22 |
| [[p10_mem_code_of_conduct_builder]] | downstream | 0.21 |
