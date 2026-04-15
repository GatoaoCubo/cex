# Report: Agent Builder

## Overview
The `agent-builder` is a type builder responsible for creating and managing agent artifacts. It follows the 8F pipeline, ensuring that agents are well-defined, structured, and validated.

## Key Features
- **Identity**: Defines the persona, capabilities, and constraints of an agent.
- **Capabilities**: Specifies the actions an agent can perform and the quality gates it must meet.
- **Routing**: Ensures agents are correctly positioned within the agent_group map and routing system.
- **Validation**: Manually checks against hard and soft quality gates to ensure compliance.

## Instructions
The `agent-builder` follows a 3-phase pipeline:
1. **RESEARCH**: Identifies the agent's domain, persona, capabilities, constraints, and tools required.
2. **COMPOSE**: Creates the agent artifact with complete frontmatter and navigable agent_package.
3. **VALIDATE**: Manually checks against quality gates to ensure compliance.

## Quality Gates
- **ID Pattern**: Must match `p02_agent_` pattern.
- **Kind**: Must be `agent`.
- **Quality**: Must be `null`.
- **Agent Package**: Must list >= 10 files.
- **Capabilities**: Must have >= 4 bullets in the body.
- **LLM Function**: Must be `BECOME`.
- **Agent Group**: Must be set (not blank).

## Conclusion
The `agent-builder` is a critical component of the agent construction process, ensuring that agents are well-defined and meet high quality standards.