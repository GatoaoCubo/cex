---
id: kc_crew_template
kind: knowledge_card
title: Crew Template
version: 1.0.0
quality: 8.8
pillar: P01
density_score: 0.98
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