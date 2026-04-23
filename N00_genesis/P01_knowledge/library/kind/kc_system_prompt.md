---
id: kc_system_prompt
kind: knowledge_card
title: "System Prompt Engineering"
version: 1.0.0
quality: 9.0
pillar: P01
language: English
density_score: 0.99
related:
  - action-prompt-builder
  - system-prompt-builder
  - bld_memory_system_prompt
  - bld_collaboration_response_format
  - p03_sp_system-prompt-builder
  - p01_kc_prompt_engineering_best_practices
  - p11_qg_system_prompt
  - bld_collaboration_system_prompt
  - bld_collaboration_action_prompt
  - p03_ins_response_format
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

## Comparison of Prompt Types
| Prompt Type        | Purpose                  | Structure Complexity | Use Case                     | Example                                                                 |
|--------------------|--------------------------|----------------------|------------------------------|-------------------------------------------------------------------------|
| Technical Writing  | Documentation creation   | High                 | API specs, user manuals      | "Write a REST API endpoint specification with OpenAPI 3.0 format"       |
| Code Generation    | Software development     | Medium               | Algorithm implementation     | "Generate Python code for a Fibonacci sequence calculator with tests"   |
| Analysis Report    | Data interpretation      | High                 | Security audits, performance | "Analyze server logs for SQL injection attempts and output JSON report" |
| Customer Support   | User assistance          | Low                  | Helpdesk, FAQs               | "Explain how to reset a forgotten password in 3 steps"                  |
| Data Analysis      | Pattern recognition      | Medium               | Business intelligence        | "Identify trends in sales data from Q1 2023 and output a markdown chart"|

## Examples
1. **Technical Documentation**:  
   "Write a technical specification for a REST API endpoint"

2. **Code Generation**:  
   "Generate Python code for a Fibonacci sequence calculator with unit tests"

3. **Analysis Report**:  
   "Analyze this server log for performance bottlenecks"

4. **Customer Support**:  
   "Explain how to troubleshoot a failed login attempt on Windows 10"

5. **Data Analysis**:  
   "Identify correlations between user engagement and feature usage in this dataset"

## Anti-Patterns
Avoid these common mistakes:
- Vagueness: "Help me with something" ❌
- Overly broad instructions: "Do whatever you need to fix this" ❌
- Lack of format: "Just tell me what's wrong" ❌
- Ambiguous constraints: "Be helpful" ❌
- Missing context: "Analyze this" ❌

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
This artifact defines **system prompt engineering** as the practice of crafting structured instructions to guide AI behavior. It is **not** a general guide for AI training, user-facing prompts, or natural language processing fundamentals.

## Related Kinds
- **Prompt Templates**: Provide reusable structures for system prompts  
- **AI Ethics Guidelines**: Ensure prompts align with ethical constraints  
- **LLM Training Data**: Influences how prompts are interpreted by models  
- **User Query Classification**: Helps map user inputs to appropriate system prompts  
- **Technical Writing Standards**: Guides the clarity and structure of output formats

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[action-prompt-builder]] | downstream | 0.27 |
| [[system-prompt-builder]] | downstream | 0.26 |
| [[bld_memory_system_prompt]] | downstream | 0.25 |
| [[bld_collaboration_response_format]] | downstream | 0.25 |
| [[p03_sp_system-prompt-builder]] | downstream | 0.25 |
| [[p01_kc_prompt_engineering_best_practices]] | sibling | 0.25 |
| [[p11_qg_system_prompt]] | downstream | 0.25 |
| [[bld_collaboration_system_prompt]] | downstream | 0.24 |
| [[bld_collaboration_action_prompt]] | downstream | 0.22 |
| [[p03_ins_response_format]] | downstream | 0.22 |
