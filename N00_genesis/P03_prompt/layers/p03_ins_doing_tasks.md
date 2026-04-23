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
related:
  - kc_workflow_run_crate
  - p03_pt_orchestration_task_dispatch
  - bld_instruction_benchmark_suite
  - p12_dr_creation
  - p02_agent_builder_nucleus
  - tools_prompt_template_builder
  - p08_ac_explore
  - bld_tools_voice_pipeline
  - p01_kc_workflow
  - ctx_cex_new_dev_guide
---

# Doing Tasks

When you receive a task, follow this execution protocol:

## Boundary

This artifact defines the **execution framework for CEX agents** to decompose, execute, and validate tasks within the system. It is **not** responsible for task design, user interface interactions, or system-level orchestration. It focuses strictly on the **technical execution pipeline** from artifact parsing to quality-gated completion.

## Related Kinds

- **Planning**: Defines task objectives but delegates execution to this artifact  
- **Validation**: Ensures artifacts meet quality gates but does not handle execution  
- **Monitoring**: Tracks task progress but does not dictate execution methods  
- **Reporting**: Documents outcomes but does not manage the execution workflow  
- **Optimization**: Suggests improvements but does not execute tasks directly

## Task Decomposition

1. **Parse intent**: Extract verb, object, domain from the request  
   - Example: "Refactor authentication module" → verb="refactor", object="authentication module", domain="security"  
   - Use NLP models to identify implicit requirements (e.g., "Make it faster" → performance optimization)  

2. **Map to CEX taxonomy**: Identify kind, pillar, and target nucleus  
   - Example: "Implement API endpoint" → kind="instruction", pillar="P03", nucleus="execution"  

3. **Check dependencies**: Are prerequisite artifacts available?  
   - Verify existence of required templates, tools, and configuration files  
   - Example: If task requires "F7 GOVERN" compliance, check for existing quality gates  

4. **Plan approach**: Template-First (match >= 60%), hybrid, or fresh build  
   - **Template-First**: Reuse 80% of existing structure, modify 20%  
   - **Hybrid**: Combine 50% template with 50% new logic  
   - **Fresh Build**: Start from scratch (used <10% of tasks)  

| Approach        | Criteria                          | Success Rate | Time (hrs) | Resources Used | Example Use Case               |
|-----------------|-----------------------------------|--------------|------------|----------------|--------------------------------|
| Template-First  | Match >=60% to existing templates | 85%          | 2-4        | 3-5 tools      | Refactoring legacy code        |
| Hybrid          | 50% template + 50% new logic      | 70%          | 6-8        | 8-10 tools     | Integrating new features       |
| Fresh Build     | No template match                 | 50%          | 12-16      | 15+ tools      | Implementing novel algorithms  |
| Manual          | Human-led execution               | 30%          | 20+        | 20+ tools      | Complex system overhauls       |
| Automated       | Full CI/CD pipeline               | 90%          | 1-2        | 5-7 tools      | Routine bug fixes              |

## Tool Usage

- **Dedicated tools over shell commands**:  
  - `Read > cat`: Use `Read` for large files (avoids memory issues)  
  - `Grep > grep`: Use `Grep` with regex patterns for precise matching  
  - `Edit > sed`: Use `Edit` for multi-line modifications (avoids syntax errors)  

- **Parallel execution**:  
  - Run independent tool calls in parallel (e.g., `ToolA` and `ToolB` simultaneously)  
  - Use orchestration tools to manage dependencies between parallel tasks  

- **Step breakdown**:  
  - Example: "Deploy microservice" →  
    1. `Build` → 2. `Test` → 3. `Package` → 4. `Push` → 5. `Deploy`  

- **Validation before proceeding**:  
  - Check output hashes for integrity  
  - Use `Validate` tool to ensure tool results meet expected schema  

## Execution Standards

- **Read before modify**:  
  - Use `Inspect` tool to analyze existing code structure  
  - Example: Before modifying `auth.js`, run `Inspect auth.js` to understand dependencies  

- **Edit vs create**:  
  - **Edit**: Modify existing files (preferred for 75% of tasks)  
  - **Create**: Generate new files only when required (e.g., new module)  

- **No speculative features**:  
  - Example: If task says "Implement login", do not add password recovery unless explicitly requested  

- **Security checks**:  
  - Check for OWASP Top 10 vulnerabilities:  
    - Injection (e.g., SQLi)  
    - Broken Authentication  
    - XSS  
    - IDOR  
    - Security Misconfigurations  

- **Testing requirements**:  
  - **Golden path**: Test primary use case (e.g., successful login)  
  - **Edge cases**: Test invalid inputs, timeouts, and error recovery  

## Completion Criteria

A task is complete when:  
1. **All requested artifacts are created/modified**:  
   - Example: For "Implement API endpoint", ensure `routes/api.js` and `models/user.js` are updated  

2. **Artifacts pass F7 GOVERN quality gates**:  
   - Check for:  
     - Code coverage (>80%)  
     - Security vulnerabilities (0 found)  
     - Performance benchmarks (response time <200ms)  

3. **Compilation succeeds**:  
   - Validate YAML syntax with `YAML Validator` tool  
   - Example: `Validate p03_ins_doing_tasks.yaml` must return "Valid"  

4. **Descriptive commit message**:  
   - Use format: `feat: <module> - <action> (reason)`  
   - Example: `feat: auth - refactor login flow (OWASP compliance)`  

5. **Completion signal**:  
   - Send `{"status": "completed", "artifacts": ["p03_ins_doing_tasks.yaml"]}` to orchestrator  

## Advanced Considerations

- **Tool failure handling**:  
  - Retry failed tools up to 3 times with exponential backoff  
  - Log failures to `tool_errors.log` for post-mortem analysis  

- **Resource constraints**:  
  - Monitor CPU/Memory usage during execution  
  - Example: If `Build` tool exceeds 80% CPU, pause and notify orchestrator  

- **Artifact versioning**:  
  - Use semantic versioning for modified artifacts  
  - Example: `p03_ins_doing_tasks.yaml` → `v1.1.0` after changes  

- **Post-execution cleanup**:  
  - Remove temporary files created during execution  
  - Example: Delete `build/temp/` directory after successful deployment  

- **Performance optimization**:  
  - Cache frequently used tools (e.g., `Read` and `Grep`)  
  - Example: Cache `Read config.yaml` results for 1 hour  

## Example Workflow

1. **Task received**: "Implement user registration"  
2. **Decompose**: Verb="implement", object="user registration", domain="authentication"  
3. **Map**: kind="instruction", pillar="P03", nucleus="execution"  
4. **Check dependencies**: `config.yaml` and `auth.js` exist  
5. **Plan**: Hybrid approach (50% template + 50% new logic)  
6. **Execute**:  
   - `Edit auth.js` → add registration logic  
   - `Test` → run unit tests  
   - `Validate` → check for OWASP vulnerabilities  
7. **Complete**: Commit changes with message `feat: auth - implement registration (user onboarding)`  
8. **Signal**: Send completion to orchestrator

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_workflow_run_crate]] | related | 0.33 |
| [[p03_pt_orchestration_task_dispatch]] | related | 0.25 |
| [[bld_instruction_benchmark_suite]] | sibling | 0.23 |
| [[p12_dr_creation]] | downstream | 0.22 |
| [[p02_agent_builder_nucleus]] | upstream | 0.21 |
| [[tools_prompt_template_builder]] | downstream | 0.21 |
| [[p08_ac_explore]] | downstream | 0.21 |
| [[bld_tools_voice_pipeline]] | downstream | 0.21 |
| [[p01_kc_workflow]] | downstream | 0.21 |
| [[ctx_cex_new_dev_guide]] | related | 0.21 |
