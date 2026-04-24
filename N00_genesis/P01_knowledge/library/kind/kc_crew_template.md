---
id: kc_crew_template
kind: knowledge_card
8f: F3_inject
title: Crew Template
version: 1.0.0
quality: 8.8
pillar: P01
density_score: 0.98
related:
  - quality-gate-builder
  - p01_kc_steps
  - bld_collaboration_quality_gate
  - bld_instruction_crew_template
  - p01_kc_skill
  - p01_kc_hook
  - bld_knowledge_card_skill
  - kc_eval_framework
  - p01_kc_server_tools
  - p11_qg_crew_template
---

# Crew Template

A reusable blueprint for defining crew structures that bridges GDP decisions (WHAT) to autonomous execution (HOW). Key components:

## Core Structure
- **template_id**: Unique identifier for the template
- **crew_name**: Human-readable name for the crew
- **roles**: List of roles with responsibilities and skills
- **process**: Workflow definition with sequential/hierarchical steps
- **memory**: Memory management system for context retention
- **success_criteria**: Clear indicators for successful mission completion
- **quality_gate**: Reference to associated quality gate configuration
- **dependencies**: External systems or data sources required

## Example Roles
| Role | Responsibilities | Skills |
|------|------------------|--------|
| Planner | Define objectives, allocate resources | Strategic thinking, resource management |
| Executor | Carry out tasks, monitor progress | Task execution, problem-solving |
| Validator | Assess quality, ensure compliance | Critical thinking, quality assurance |
| Communicator | Maintain stakeholder engagement | Interpersonal skills, communication |

## Quality Integration
- **Validation Phases**: Must include at least the `validate`, `score`, and `approve` phases from the quality gate framework
- **Trigger Conditions**: Should align with quality gate trigger types (user_invocable, agent_only)
- **Metrics**: Include success metrics that feed into quality scoring systems

## Implementation Notes
- Templates should be versioned with semantic versioning (e.g., `v1.0.0`)
- Include a `quality_gate` field referencing the associated quality gate configuration
- Ensure memory systems support the required context retention for validation phases
- Define clear success criteria that align with quality gate thresholds
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[quality-gate-builder]] | downstream | 0.25 |
| [[p01_kc_steps]] | sibling | 0.21 |
| [[bld_collaboration_quality_gate]] | downstream | 0.20 |
| [[bld_instruction_crew_template]] | downstream | 0.19 |
| [[p01_kc_skill]] | sibling | 0.19 |
| [[p01_kc_hook]] | sibling | 0.18 |
| [[bld_knowledge_card_skill]] | sibling | 0.18 |
| [[kc_eval_framework]] | sibling | 0.18 |
| [[p01_kc_server_tools]] | sibling | 0.18 |
| [[p11_qg_crew_template]] | downstream | 0.17 |
