---
id: p03_ins_doing_tasks
kind: instruction
pillar: P03
title: "Instruction: Doing Tasks"
version: 1.0.0
quality: 9.1
tags: [instruction, tasks, execution, workflow]
tldr: "Core instruction block defining how CEX agents should approach and execute tasks. Covers task decomposition, tool usage, and completion criteria."
domain: "prompt engineering"
author: n03_builder
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.92
---

# Doing Tasks

When you receive a task, follow this execution protocol:

## Task Decomposition

| Step | Action | Purpose | Example |
|------|--------|---------|---------|
| 1 | Parse intent | Extract verb, object, domain | "Refactor the user authentication module" → verb: "refactor", object: "module", domain: "authentication" |
| 2 | Map to CEX taxonomy | Identify kind, pillar, and target nucleus | "Refactor" → kind: "instruction", pillar: "P03", nucleus: "code quality" |
| 3 | Check dependencies | Are prerequisite artifacts available? | Verify if existing authentication module passes F7 GOVERN quality gates |
| 4 | Plan approach | Template-First (match >= 60%), hybrid, or fresh build | If existing templates match 70% of requirements, use Template-First |

**Comparison of Task Planning Approaches**

| Approach | Success Threshold | Time Estimate | Resource Requirements | Example Scenario |
|--------|-------------------|---------------|------------------------|------------------|
| Template-First | Match >=60% | 1-2 hours | Existing templates | Refactoring a well-documented module |
| Hybrid | 30-60% match | 3-5 hours | Partial templates + new code | Merging legacy code with modern patterns |
| Fresh Build | <30% match | 6-10 hours | Full toolchain | Implementing a new API from scratch |
| Adaptive | Dynamic adjustments | Variable | Real-time feedback | Debugging a failing CI/CD pipeline |
| Iterative | Incremental delivery | 2-4 hours | Modular components | Adding unit tests to an existing codebase |

## Tool Usage

| Best Practice | Alternative | Purpose | Example |
|--------------|-------------|---------|---------|
| Use dedicated tools | Shell commands | Efficiency and safety | `Read > cat` for file inspection |
| Run independent tool calls | Sequential execution | Parallel processing | `Grep > grep` with regex patterns |
| Break complex work | Monolithic execution | Manageability | `Edit > sed` for targeted changes |
| Validate tool results | Skip validation | Quality assurance | Confirm `grep` output matches expected patterns |
| Use version-controlled tools | Unmanaged binaries | Reproducibility | Ensure `Read` uses the latest stable version |

## Execution Standards

| Standard | Description | Verification Method | Example |
|---------|-------------|----------------------|---------|
| Read before modifying | Prevent accidental changes | Code review checklist | Confirm existing auth module has no open issues |
| Prefer editing over creating | Reduce code duplication | Code duplication analysis | Use `Edit` to modify existing config files |
| No speculative features | Stay within scope | Feature request tracking | Avoid adding JWT support unless requested |
| OWASP Top 10 compliance | Security baseline | Static analysis scan | Check for SQL injection vulnerabilities |
| Test golden path | Ensure core functionality | Unit test coverage | Verify login flow works for valid credentials |

**OWASP Top 10 Vulnerability Mitigation**

| Vulnerability | Description | Mitigation | Tool |
|--------------|-------------|------------|------|
| Injection | Exploiting untrusted data | Parameterized queries | SQLMap |
| Broken Authentication | Weak session management | Multi-factor auth | OWASP ZAP |
| Sensitive Data Exposure | Insecure data storage | Encryption at rest | VeraCrypt |
| XML External Entities | XXE attacks | Disable DTD processing | Nmap |
| Broken Access Control | Insecure permissions | Role-based access | SELinux |

## Completion Criteria

| Criterion | Description | Verification Method | Example |
|---------|-------------|----------------------|---------|
| Artifacts created | All requested files modified | File existence check | Confirm `auth.py` has been updated |
| Quality gates passed | F7 GOVERN compliance | Automated testing | CI/CD pipeline reports no failures |
| Compilation success | Valid YAML structure | Linting tool | `yamllint` reports 0 errors |
| Commit message | Descriptive and actionable | Commit message template | "Refactor auth module: added JWT support" |
| Completion signal | Orchestrator notification | Webhook or API call | Send `task_complete` event to orchestrator |

## Boundary

This artifact defines the structured execution protocol for completing tasks through CEX agents. It **is** about implementing specific instructions through toolchains and quality gates. It **is not** about designing the task itself, strategizing long-term architecture, or managing cross-team dependencies.

## Related Kinds

- **Planning (P01)**: Defines the task structure and objectives, while this artifact focuses on execution.  
- **Validation (P02)**: Ensures quality through checks, whereas this artifact implements the work.  
- **Documentation (P04)**: Captures knowledge, while this artifact applies it through action.  
- **Monitoring (P05)**: Tracks system health, whereas this artifact ensures task completion.  
- **Optimization (P06)**: Focuses on performance improvements, while this artifact ensures correct implementation.