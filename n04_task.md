---
id: kc_role_assignment
kind: knowledge_card
title: Role Assignment in CEX Agents
version: 1.0.0
quality: null
pillar: P01
---

Role assignment in CEX agents follows CrewAI-style binding patterns, mapping roles to specialized agents with defined responsibilities. Key components include:

1. **Role Definition**  
   - Unique identifier for agent function (e.g., "n03-builder", "n04-librarian")
   - Alignment with 8F pipeline stages (F1-F8)

2. **Agent Configuration**  
   - Technical specifications: model, context window, token budget
   - Execution parameters: parallelism, priority, resource constraints

3. **Responsibility Scope**  
   - Task delegation boundaries (e.g., "n01-analyst" handles research, "n05-operator" executes code)
   - Error handling protocols for failed tasks

4. **Delegation Mechanisms**  
   - Chain-of-command structures for sequential task execution
   - Parallel processing patterns for independent tasks

5. **Backstory Context**  
   - Historical task performance metrics
   - Quality feedback patterns from GDP protocol

This framework enables autonomous orchestration while maintaining human-in-the-loop governance through guided decisions (GDP) and quality gates. Role assignments are versioned and audited via the decision_manifest.yaml, ensuring traceability across 8F pipeline executions.
