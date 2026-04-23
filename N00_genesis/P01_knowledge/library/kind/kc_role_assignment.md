---
id: kc_role_assignment
kind: knowledge_card
title: Role Assignment
version: 1.0.0
quality: 8.7
pillar: P01
density_score: 0.96
related:
  - role-assignment-builder
  - bld_knowledge_card_role_assignment
  - p03_sp_role_assignment_builder
  - p11_qg_role_assignment
  - bld_instruction_crew_template
  - p01_kc_crewai_patterns
  - crew-template-builder
  - p03_ins_permission
  - agent-profile-builder
  - p12_ct_product_launch.md
---

# Role Assignment

Role assignment is a structured approach to defining agent responsibilities and interactions, inspired by CrewAI's agent-centric model. This pattern establishes:

## Key Components
- **Role**: A named function with specific objectives (e.g., "Market Researcher")
- **Agent**: The entity executing the role (human or AI)
- **Responsibilities**: Clear tasks and deliverables for the role
- **Delegation**: Rules for task distribution between agents
- **Backstory**: Contextual narrative to inform decision-making

## Implementation
1. Define roles with distinct functions and constraints
2. Assign agents to roles based on capabilities
3. Establish delegation protocols for task escalation
4. Create backstory narratives to guide ethical/strategic choices
5. Maintain role boundaries to prevent scope creep

## Benefits
- Clear accountability for tasks
- Enhanced collaboration through defined roles
- Better resource allocation
- Improved conflict resolution through structured delegation

## Best Practices
- Use specific, measurable role descriptions
- Document delegation rules explicitly
- Regularly review role effectiveness
- Maintain role flexibility for evolving needs
- Ensure backstory aligns with organizational values
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[role-assignment-builder]] | downstream | 0.43 |
| [[bld_knowledge_card_role_assignment]] | sibling | 0.29 |
| [[p03_sp_role_assignment_builder]] | downstream | 0.23 |
| [[p11_qg_role_assignment]] | downstream | 0.22 |
| [[bld_instruction_crew_template]] | downstream | 0.22 |
| [[p01_kc_crewai_patterns]] | sibling | 0.21 |
| [[crew-template-builder]] | downstream | 0.21 |
| [[p03_ins_permission]] | downstream | 0.20 |
| [[agent-profile-builder]] | downstream | 0.20 |
| [[p12_ct_product_launch.md]] | downstream | 0.19 |
