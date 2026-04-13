---
id: p03_ins_doing_tasks
kind: instruction
pillar: P03
title: "Instruction: Doing Tasks"
version: 1.0.0
quality: 9.2
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

1. **Parse intent**: Extract verb, object, domain from the request  
   *Example*: "Refactor the user authentication module in Python" → verb: "refactor", object: "user authentication module", domain: "Python"  
2. **Map to CEX taxonomy**: Identify kind, pillar, and target nucleus  
   *Example*: "Refactor" maps to kind: instruction, pillar: P03, nucleus: code quality  
3. **Check dependencies**: Are prerequisite artifacts available?  
   *Example*: Verify existence of `auth.py` and `requirements.txt`  
4. **Plan approach**: Template-First (match >= 60%), hybrid, or fresh build  
   *Example*: If 75% of code matches existing templates, use Template-First  

## Tool Usage

- Use dedicated tools over shell commands (Read > cat, Grep > grep, Edit > sed)  
  *Example*: Use `git diff` instead of `cat` for code comparison  
- Run independent tool calls in parallel for efficiency  
  *Example*: Execute `lint` and `test` in parallel during CI  
- Break complex work into discrete steps with clear inputs/outputs  
  *Example*: Split "deploy application" into "build", "package", "push"  
- Validate tool results before proceeding to next step  
  *Example*: Confirm `pytest` passes before committing changes  

## Execution Standards

- Read existing code before modifying it  
  *Example*: Review `auth.py` for legacy comments or custom logic  
- Prefer editing existing files over creating new ones  
  *Example*: Update `models.py` instead of creating new `user_models.py`  
- Do not add features beyond what was requested  
  *Example*: Avoid adding rate-limiting if not specified  
- Do not add speculative abstractions or future-proofing  
  *Example*: Skip implementing OAuth2 if only basic auth is required  
- Write safe, secure code -- check for OWASP Top 10 vulnerabilities  
  *Example*: Validate user inputs to prevent SQL injection (A1)  
- Test the golden path and edge cases before reporting completion  
  *Example*: Test both valid and invalid login scenarios  

## Completion Criteria

A task is complete when:  
1. All requested artifacts are created/modified  
   *Example*: `auth.py`, `tests/test_auth.py`, and `README.md` updated  
2. Artifacts pass F7 GOVERN quality gates  
   *Example*: Code meets 85%+ coverage in `test_auth.py`  
3. Compilation succeeds (compiled YAML is valid)  
   *Example*: `git status` shows no uncommitted changes  
4. Changes are committed with descriptive message  
   *Example*: Commit message: "Refactor auth module to use JWT"  
5. Completion signal is sent to the orchestrator  
   *Example*: `curl -X POST http://orchestrator/api/complete`  

## Comparison of Task Execution Approaches

| Method          | Pros                                      | Cons                                      | Use Cases                              | Efficiency Score |
|-----------------|-------------------------------------------|-------------------------------------------|----------------------------------------|------------------|
| Template-First  | Fast, consistent, low risk                | Limited flexibility                      | Routine code generation                | 9.2              |
| Hybrid          | Balances speed and customization          | Requires judgment                        | Refactoring with minor changes       | 8.5              |
| Fresh Build     | Full control, no legacy debt              | Time-consuming, high risk                | New system implementation              | 6.8              |
| Manual          | No tooling dependencies                   | Error-prone, inconsistent                | Simple one-off tasks                   | 4.3              |
| Automated       | Scalable, repeatable                      | High initial setup cost                  | CI/CD pipelines                        | 9.0              |

## Boundary

This artifact defines the protocol for executing tasks through CEX agents. It **is** a technical specification for task execution, including tool usage and quality gates. It **is not** a strategic document, UI design guide, or high-level architecture plan.

## Related Kinds

- **Planning**: Provides task decomposition frameworks used in this instruction  
- **Validation**: Defines quality gates referenced in completion criteria  
- **Monitoring**: Tracks task execution metrics used for efficiency scoring  
- **Security**: Specifies OWASP vulnerability checks in execution standards  
- **CI/CD**: Integrates completion signals with automated pipelines  

## Advanced Considerations

### Dependency Management

| Dependency Type | Tool         | Check Command           | Expected Outcome         |
|-----------------|--------------|-------------------------|--------------------------|
| Codebase        | Git          | `git ls-files auth/`    | Returns existing files   |
| Dependencies    | Pip          | `pip list | grep flask` | Shows installed packages |
| Linting         | Flake8       | `flake8 auth/`          | No errors or warnings    |
| Testing         | Pytest       | `pytest auth/`          | 100% test coverage       |
| Documentation   | Sphinx       | `sphinx-build -b html`  | Generates docs           |

### Efficiency Metrics

| Metric               | Baseline | Target | Tool         | Example Value |
|----------------------|----------|--------|--------------|---------------|
| Code coverage        | 70%      | 85%    | pytest-cov   | 88%           |
| Build time           | 2.5m     | 1.8m   | time         | 1.9m          |
| Error rate           | 5%       | 2%     | CI logs      | 1.7%          |
| Documentation score  | 65/100   | 90/100 | sphinx       | 88/100        |
| Security scan score  | 7.2/10   | 9.5/10 | bandit       | 8.9/10        |

### Edge Case Handling

1. **Missing dependencies**:  
   *Example*: If `auth.py` is missing, create a minimal skeleton with placeholder functions  
2. **Conflicting changes**:  
   *Example*: Use `git merge` with conflict resolution strategy defined in `MERGE.md`  
3. **Inconsistent quality**:  
   *Example*: If `test_auth.py` fails, run `pytest --pdb` to debug failures  
4. **Tool failures**:  
   *Example*: If `flake8` crashes, use `pycodestyle` as fallback  
5. **Ambiguous requests**:  
   *Example*: Send clarification request to orchestrator via `curl -X POST http://orchestrator/api/clarify`  

### Quality Gate Examples

| Gate Name       | Tool         | Threshold | Description                                  |
|-----------------|--------------|-----------|----------------------------------------------|
| Code Coverage   | pytest-cov   | 85%       | All tests must pass with >=85% coverage      |
| Security Score  | bandit       | 9.0/10    | No high-severity vulnerabilities allowed     |
| Linting Score   | flake8       | 0 errors  | No style or syntax errors allowed            |
| Documentation   | sphinx       | 90/100    | API docs must score >=90/100                 |
| Test Stability  | pytest       | 100%      | No flaky tests in the repository             |