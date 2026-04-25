---
id: kc_team_charter
kind: knowledge_card
8f: F3_inject
title: Team Charter
version: 1.0.0
quality: 8.9
pillar: P01
tldr: "Mission contract defining purpose, deliverables, budget, deadline, and quality gate for a crew"
when_to_use: "When instantiating a composable crew and need to bind mission scope to a crew template"
density_score: 1.0
related:
  - p03_sp_team_charter_builder
  - team-charter-builder
  - bld_knowledge_card_team_charter
  - bld_tools_team_charter
  - bld_schema_team_charter
  - bld_collaboration_team_charter
  - bld_examples_team_charter
  - bld_architecture_team_charter
  - bld_instruction_team_charter
  - bld_config_team_charter
---

# Team Charter

## Description
A team charter is a mission contract that defines the purpose, scope, and operational parameters for a crew instance. It bridges GDP decisions (WHAT) to autonomous execution (HOW) by establishing clear expectations, roles, and success criteria.

## Structure
```yaml
kind: team_charter
pillar: P01
llm_function: TOOL
max_bytes: 4096
naming: p01_team_charter_{{name}}.md + .yaml
core: true
```

## Key Parameters
| Field | Type | Description |
|-------|------|-------------|
| charter_id | string | Unique identifier for this charter instance |
| crew_template_ref | string | Reference to the crew template used as foundation |
| mission_statement | string | Clear, concise definition of the crew's purpose |
| deliverables | array | Specific outputs the crew is expected to produce |
| success_metrics | object | Quantifiable benchmarks for measuring achievement |
| budget | number | Financial resources allocated for the mission |
| deadline | datetime | Final date by which all deliverables must be completed |
| stakeholders | array | Key individuals/organizations with vested interest |
| quality_gate | number | Minimum quality threshold for deliverables |
| escalation_protocol | string | Process for resolving conflicts or issues |
| termination_criteria | string | Conditions under which the charter will end |

## Operational Semantics
- **Discovery**: Resolved via crew template matching
- **Validation**: Requires quality gate verification
- **Rotation**: Automatic charter renewal mechanism
- **Monitoring**: Health checks for deliverable progress

## Cross-Platform Compatibility
| System | Support | Notes |
|--------|--------|-------|
| Kubernetes | ✅ | Crew scheduling integration |
| Docker | ✅ | Containerized crew execution |
| Cloud Foundry | ⚠ | Requires adapter implementation |
| OpenStack | ⚠ | Needs custom scheduler |
| AWS | ✅ | ECS/Fargate support |
| Azure | ✅ | Container Instances integration |

## Security Considerations
- TLS 1.3+ encryption for charter exchange
- Access control via role-based permissions
- Audit logging for charter modifications
- Rate limiting for charter creation
```
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_team_charter_builder]] | downstream | 0.45 |
| [[team-charter-builder]] | downstream | 0.44 |
| [[bld_knowledge_card_team_charter]] | sibling | 0.39 |
| [[bld_tools_team_charter]] | downstream | 0.39 |
| [[bld_schema_team_charter]] | downstream | 0.37 |
| [[bld_collaboration_team_charter]] | downstream | 0.34 |
| [[bld_examples_team_charter]] | downstream | 0.32 |
| [[bld_architecture_team_charter]] | downstream | 0.27 |
| [[bld_instruction_team_charter]] | downstream | 0.26 |
| [[bld_config_team_charter]] | downstream | 0.26 |
