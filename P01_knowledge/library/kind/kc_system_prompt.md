---
id: kc_system_prompt
kind: knowledge_card
title: "System Prompt Engineering"
version: 1.0.0
quality: 8.9
pillar: P01
language: English
density_score: 0.95
---

# System Prompt Engineering

## Identity
A system prompt defines the AI's role, constraints, and behavior during task execution. It establishes:
- Core identity (e.g., "You are a technical writer")
- Operational boundaries
- Decision-making framework

## Constraints
Common system prompt constraints include:
- Role definition: "You are a cybersecurity analyst"
- Task scope: "Analyze this network traffic for threats"
- Format requirements: "Output in JSON with severity levels"

## Output Format
Use structured formats for clarity:
```json
{
  "analysis": "Threat detected in port 22",
  "severity": "high",
  "recommendation": "Enable firewall rule 4567"
}
```

## Tone
Adapt tone based on context:
- Professional: "The system detected an anomaly requiring immediate attention"
- Conversational: "Hey, I noticed something unusual on port 22"
- Technical: "SSH brute force attempt detected on 19.2.168.1.10"

## Examples
| Task Type           | Role                | Constraints                          | Output Format               |
|---------------------|---------------------|--------------------------------------|-----------------------------|
| Technical Docs      | Technical Writer    | Use markdown, avoid jargon           | Structured markdown         |
| Code Generation     | Developer           | Python 3.10, include unit tests      | Code + test files           |
| Security Analysis   | Cybersecurity Analyst | Scan for SQLi, output JSON          | JSON with risk scores       |
| Customer Support    | Support Agent       | Use friendly tone, English only     | Text response               |
| Data Processing     | Data Scientist      | Process CSV, output analysis in CSV | CSV with metadata           |

## Anti-Patterns
Avoid these common mistakes:
- Vagueness: "Help me with something" ❌
- Overly broad instructions: "Do whatever you need to fix this" ❌
- Lack of format: "Just tell me what's wrong" ❌

## Template Structure
```markdown
# [Task Title]

## Role
[Define AI's role]

## Constraints
- [Specific limitation 1]
- [Specific limitation 2]

## Output Format
[Specify structure and requirements]

## Example
[Show expected output format]
```

## Boundary
This artifact defines how to structure system prompts to guide AI behavior. It does not dictate the AI's capabilities or the user's input requirements.

## Related Kinds
- **Knowledge Card (Technical Writing)**: Provides templates for documenting system prompts  
- **Prompt Template (Code Generation)**: Focuses on code-specific structure and syntax requirements  
- **Constraint Framework (Cybersecurity)**: Defines security-specific limitations and compliance rules  
- **Tone Guide (Customer Support)**: Focuses on language style and communication protocols  
- **Format Specification (Data Processing)**: Details structured output requirements for analytical tasks