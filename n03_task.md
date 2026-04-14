---
id: kc_role_assignment
kind: knowledge_card
title: Role Assignment in CEX Agents
version: 1.0.0
quality: null
pillar: P01
---

Role assignment in CEX agents follows CrewAI-style binding patterns, mapping roles to specialized agents with defined responsibilities. Key elements include:

1. **Role Definition**  
   A semantic label (e.g., "n03-builder") representing a functional archetype, not a human role. Roles are tied to nucleus capabilities via the 8F pipeline.

2. **Agent Binding**  
   Each role is statically bound to a nucleus (N01-N07) through the `P03_prompt` layer. This creates a persistent identity for task execution.

3. **Responsibilities**  
   Roles inherit predefined workflows from their nucleus's ISOs (e.g., N03-builder handles artifact creation via 8F pipeline). Responsibilities are enforced through GDP gates.

4. **Delegation Patterns**  
   Roles can delegate subtasks using the `dispatch` protocol. The `P05_model_options` system manages priority queues for parallel execution.

5. **Backstory Context**  
   Role-specific memory is stored in `P02_provider_profiles` and `P06_theme_system`, enabling context-aware decision making via the 8F pipeline.

This structure enables autonomous orchestration while maintaining human-in-the-loop governance through the GDP protocol.
