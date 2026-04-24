---
id: p04_ce_n03
kind: code_executor
8f: F5_call
pillar: P04
title: "Code Executor -- N03 Sandboxed Build Validation"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 9.1
tags: [code-executor, N03, sandbox, validation, build, compile, 8F]
tldr: "Sandboxed code execution environment for N03 build validation. Executes cex_compile.py, cex_doctor.py, cex_sanitize.py, and cex_score.py in a controlled context. Captures stdout/stderr, enforces timeout, and reports structured results to F7 GOVERN."
density_score: 0.90
updated: "2026-04-17"
related:
  - p10_lr_cli_tool_builder
  - p11_qg_cli_tool
  - p03_sp_cli_tool_builder
  - bld_knowledge_card_cli_tool
  - bld_examples_cli_tool
  - bld_collaboration_code_executor
  - bld_instruction_cli_tool
  - bld_examples_code_executor
  - p11_qg_artifact
  - p11_qg_admin_orchestration
---

# Code Executor: N03 Sandboxed Build Validation

## Purpose

N03 produces artifacts and VALIDATES them by executing Python tools.
The code executor defines HOW those tools run -- what's sandboxed, what's timeout-enforced,
what counts as a pass, and how results feed back into the pipeline.

## Execution Contexts

| Context | When Used | Tools | Timeout |
|---------|----------|-------|---------|
| post_produce | After F6 generates draft | cex_compile.py (dry) | 30s |
| govern | F7 GOVERN validation | cex_doctor.py + cex_score.py | 60s |
| post_f8 | After artifact saved | cex_compile.py (write) + cex_sanitize.py | 45s |
| bugloop | Auto error correction | cex_compile.py + cex_doctor.py | 30s |
| regression | Regression detection | cex_retriever.py --vocab-check | 15s |

## Tool Specifications

### cex_compile.py

```bash
python _tools/cex_compile.py {artifact_path}
# OR
python _tools/cex_compile.py --all

# Success: exit code 0
# Failure: exit code 1 + error message on stderr
# Output: {artifact_path}.yaml created on success
```

**Pass condition:** exit code 0 + .yaml file created  
**Fail condition:** exit code 1 OR missing .yaml  
**Common failures:** YAML parse error, missing required frontmatter field, invalid kind

### cex_doctor.py

```bash
python _tools/cex_doctor.py --file {artifact_path}
# OR
python _tools/cex_doctor.py --nucleus n03

# Success: exit code 0 + "PASS" count >= total count
# Failure: exit code 1 + FAIL lines on stdout
```

**Pass condition:** exit code 0 + zero FAIL lines  
**Warn condition:** exit code 0 + WARN lines  
**Fail condition:** exit code 1 OR FAIL lines present

### cex_sanitize.py

```bash
python _tools/cex_sanitize.py --check --scope N03_engineering/
# OR single file:
python _tools/cex_sanitize.py --check {artifact_path}

# Success: exit code 0
# Failure: exit code 1 + list of non-ASCII positions
```

**Pass condition:** exit code 0  
**Only runs on:** .py, .ps1, .sh code blocks extracted from artifacts

### cex_score.py

```bash
python _tools/cex_score.py {artifact_path} --nucleus n03
# Returns: JSON score object {score, dimensions, gates}
# Never sets quality in the file (read-only analysis)
```

**Returns:** structured score object; does NOT write to file  
**Used by:** scoring_rubric_n03.md D1-D5 composite calculation

## Execution Protocol

```python
def execute_build_validation(artifact_path: str, context: str) -> ExecutionResult:
    """Execute all tools for the given context."""
    tools = CONTEXT_TOOLS[context]
    results = []
    
    for tool in tools:
        cmd = build_command(tool, artifact_path)
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=CONTEXT_TIMEOUTS[context],
            cwd=REPO_ROOT
        )
        results.append(ToolResult(
            tool=tool,
            exit_code=proc.returncode,
            stdout=proc.stdout[:4096],   # truncate excessive output
            stderr=proc.stderr[:2048],
            passed=proc.returncode == 0
        ))
    
    return ExecutionResult(
        context=context,
        artifact_path=artifact_path,
        tools=results,
        all_passed=all(r.passed for r in results),
        failure_count=sum(1 for r in results if not r.passed)
    )
```

## Error Classification

| Exit Code | stdout pattern | Classification | Action |
|-----------|---------------|----------------|--------|
| 0 | "PASS" | success | Continue pipeline |
| 1 | "SyntaxError" | yaml_error | bugloop: heuristic fix |
| 1 | "FAIL" + field name | missing_field | bugloop: field injection |
| 1 | "non-ASCII" | ascii_violation | bugloop: cex_sanitize fix |
| 1 | "UnknownKind" | unknown_kind | Escalate to N07 |
| timeout | — | timeout | Retry once; if again -> escalate |

## Output Format

```yaml
execution_result:
  context: govern
  artifact_path: N03_engineering/P06_schema/input_schema_build_contract.md
  all_passed: true
  failure_count: 0
  tools:
    - tool: cex_compile.py
      exit_code: 0
      passed: true
      stdout: "Compiled: N03_engineering/P06_schema/input_schema_build_contract.yaml"
    - tool: cex_doctor.py
      exit_code: 0
      passed: true
      stdout: "1/1 PASS"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_cli_tool_builder]] | downstream | 0.27 |
| [[p11_qg_cli_tool]] | downstream | 0.25 |
| [[p03_sp_cli_tool_builder]] | related | 0.24 |
| [[bld_knowledge_card_cli_tool]] | upstream | 0.23 |
| [[bld_examples_cli_tool]] | downstream | 0.23 |
| [[bld_collaboration_code_executor]] | downstream | 0.22 |
| [[bld_instruction_cli_tool]] | upstream | 0.22 |
| [[bld_examples_code_executor]] | downstream | 0.21 |
| [[p11_qg_artifact]] | downstream | 0.21 |
| [[p11_qg_admin_orchestration]] | downstream | 0.21 |
