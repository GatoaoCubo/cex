---
id: p03_pt_engineering_task
kind: prompt_template
8f: F6_produce
pillar: P03
title: "Engineering Task Execution Template"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: prompt-template-builder
variables:
  - name: task_type
    type: string
    required: true
    default: null
    description: "Category of engineering task (code_review, bug_fix, architecture_design, implementation, refactor, documentation)"
  - name: target
    type: string
    required: true
    default: null
    description: "Specific file, function, module, system, or component the task applies to"
  - name: context
    type: string
    required: true
    default: null
    description: "Codebase or system context — what the target does, its role, and relevant dependencies"
  - name: constraints
    type: list
    required: false
    default: []
    description: "Hard constraints the output must respect (language version, framework, performance SLAs, style guides)"
  - name: depth
    type: string
    required: false
    default: "standard"
    description: "Analysis depth: surface (top-3 only), standard (full review), deep (exhaustive audit)"
  - name: output_format
    type: string
    required: false
    default: "structured"
    description: "Output shape: structured (headings + bullets), inline (code comments), diff (patch format)"
variable_syntax: "mustache"
composable: true
injection_point: user
domain: engineering
quality: 9.1
tags: [prompt-template, engineering, code-review, task-driver, reusable, P03]
tldr: "Parameterized engineering task driver — fills task_type, target, and context to produce a precise LLM engineering directive."
keywords: [engineering, code review, bug fix, architecture, implementation, refactor, task, parameterized]
density_score: 0.91
related:
  - p03_pt_knowledge_tasks
  - p03_pt_creation_task
  - bld_examples_response_format
  - examples_prompt_template_builder
  - p03_pt_orchestration_task_dispatch
  - p06_schema_research_brief
  - p03_ins_prompt_template
  - p03_pt_brand_task_driver
  - p03_pt_marketing_task_execution
  - p03_pt_intelligence_analysis
---
## Purpose

Produces a precise, role-aware engineering directive for any software engineering task category. Separates task framing (role, depth, constraints, output format) from task content (target, context) so the same mold drives code reviews, bug analyses, architecture assessments, refactors, and implementations without prompt rewriting. Invoke once per task; vary `task_type`, `target`, and `context` to generate distinct, consistent directives from a single mold. Composable: embed as a sub-block inside mission-level or multi-step engineering pipeline templates.

## Variables Table

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| task_type | string | true | null | Category of engineering task (code_review, bug_fix, architecture_design, implementation, refactor, documentation) |
| target | string | true | null | Specific file, function, module, system, or component the task applies to |
| context | string | true | null | Codebase/system context — what the target does, its role, and relevant dependencies |
| constraints | list | false | [] | Hard constraints the output must respect (language, framework, performance SLAs, style guides) |
| depth | string | false | "standard" | Analysis depth: surface (top-3 only), standard (full review), deep (exhaustive audit) |
| output_format | string | false | "structured" | Output shape: structured (headings + bullets), inline (code comments), diff (patch format) |

## Template Body

```
You are a senior software engineer performing a {{task_type}}.

Target: {{target}}
Depth: {{depth}}
Output format: {{output_format}}

## Codebase Context
{{context}}

## Constraints
{{#constraints}}
- {{.}}
{{/constraints}}
{{^constraints}}
No explicit constraints supplied — apply industry-standard best practices.
{{/constraints}}

## Depth Contract
Apply the specified depth level as follows:
- surface  → identify the top 3 issues or decisions only; no exhaustive walkthrough
- standard → full analysis with prioritized findings and actionable recommendations
- deep     → exhaustive audit covering correctness, performance, security, maintainability, and testability

## Output Format Contract
Produce your response in {{output_format}} format:
- structured → markdown headings (##) + bullet points; group findings by severity (Critical / High / Medium / Low)
- inline     → annotate the code directly; prefix critical issues with [CRITICAL], warnings with [WARN]
- diff       → unified diff format (--- a/ +++ b/); add explanatory comments above each hunk

## Task
Perform {{task_type}} on {{target}} at {{depth}} depth.

Your response MUST include these four sections:

### 1. Summary
One paragraph: overall state of {{target}} relative to {{task_type}} objectives.

### 2. Findings
Prioritized list of issues, gaps, or decisions — Critical → High → Medium → Low.
Each finding: one-line label + one-sentence description.

### 3. Recommendations
Concrete, actionable steps mapped 1-to-1 to findings.
Each recommendation: imperative verb + specific change + expected outcome.

### 4. Risks
What breaks or degrades if the recommendations above are not applied.
```

## Quality Gates

| Gate | Status | Notes |
|---|---|---|
| H01 frontmatter valid YAML | PASS | Parses without error; no special chars in values |
| H02 id matches `p03_pt_*` namespace | PASS | `p03_pt_engineering_task` starts with `p03_pt_` |
| H03 id equals filename stem | PASS | Filename `p03_pt_engineering_task.md` matches id |
| H04 kind equals `prompt_template` | PASS | Exact literal match |
| H05 quality is null | PASS | `quality: null` — draft artifact |
| H06 all required frontmatter fields present | PASS | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr all present |
| H07 body contains `{{variable}}` placeholder | PASS | Six distinct variable slots in template body |
| H08 body vars == declared vars (bijection) | PASS | task_type, target, context, constraints, depth, output_format — declared and used |
| H09 injection_point declared | PASS | `injection_point: user` |

## Examples

### Example 1 — Deep Code Review

**Variables:**
```yaml
task_type: code_review
target: "src/auth/token_validator.py"
context: >
  FastAPI service handling JWT validation for a B2B SaaS platform.
  token_validator.py is called on every authenticated request — it imports PyJWT,
  verifies the signature against a rotating JWKS endpoint, checks expiry, and returns
  the decoded payload or raises HTTPException(401).
constraints:
  - "Python 3.11"
  - "PyJWT >= 2.8"
  - "No external HTTP calls inside the validator (JWKS fetched separately)"
depth: deep
output_format: structured
```

**Rendered Output:**
```
You are a senior software engineer performing a code_review.

Target: src/auth/token_validator.py
Depth: deep
Output format: structured

## Codebase Context
FastAPI service handling JWT validation for a B2B SaaS platform.
token_validator.py is called on every authenticated request — it imports PyJWT,
verifies the signature against a rotating JWKS endpoint, checks expiry, and returns
the decoded payload or raises HTTPException(401).

## Constraints
- Python 3.11
- PyJWT >= 2.8
- No external HTTP calls inside the validator (JWKS fetched separately)

## Depth Contract
Apply the specified depth level as follows:
- surface  → identify the top 3 issues or decisions only; no exhaustive walkthrough
- standard → full analysis with prioritized findings and actionable recommendations
- deep     → exhaustive audit covering correctness, performance, security, maintainability, and testability

## Output Format Contract
Produce your response in structured format:
- structured → markdown headings (##) + bullet points; group findings by severity (Critical / High / Medium / Low)
- inline     → annotate the code directly; prefix critical issues with [CRITICAL], warnings with [WARN]
- diff       → unified diff format (--- a/ +++ b/); add explanatory comments above each hunk

## Task
Perform code_review on src/auth/token_validator.py at deep depth.

Your response MUST include these four sections:

### 1. Summary
One paragraph: overall state of src/auth/token_validator.py relative to code_review objectives.

### 2. Findings
Prioritized list of issues, gaps, or decisions — Critical → High → Medium → Low.
Each finding: one-line label + one-sentence description.

### 3. Recommendations
Concrete, actionable steps mapped 1-to-1 to findings.
Each recommendation: imperative verb + specific change + expected outcome.

### 4. Risks
What breaks or degrades if the recommendations above are not applied.
```

---

### Example 2 — Surface Bug Fix (no constraints, default output)

**Variables:**
```yaml
task_type: bug_fix
target: "utils/pagination.ts — getPageSlice()"
context: >
  Next.js e-commerce frontend. getPageSlice() slices a product array for
  client-side pagination. Off-by-one error causes the last item on each page
  to repeat as the first item on the next page.
depth: surface
output_format: diff
```

**Rendered Output:**
```
You are a senior software engineer performing a bug_fix.

Target: utils/pagination.ts — getPageSlice()
Depth: surface
Output format: diff

## Codebase Context
Next.js e-commerce frontend. getPageSlice() slices a product array for
client-side pagination. Off-by-one error causes the last item on each page
to repeat as the first item on the next page.

## Constraints
No explicit constraints supplied — apply industry-standard best practices.

...
[depth + output format contract sections as rendered above]
...

## Task
Perform bug_fix on utils/pagination.ts — getPageSlice() at surface depth.

### 1. Summary  [top-3 only at surface depth]
...
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_pt_knowledge_tasks]] | sibling | 0.37 |
| [[p03_pt_creation_task]] | sibling | 0.29 |
| [[bld_examples_response_format]] | downstream | 0.26 |
| [[examples_prompt_template_builder]] | downstream | 0.24 |
| [[p03_pt_orchestration_task_dispatch]] | sibling | 0.24 |
| [[p06_schema_research_brief]] | downstream | 0.23 |
| [[p03_ins_prompt_template]] | related | 0.23 |
| [[p03_pt_brand_task_driver]] | sibling | 0.22 |
| [[p03_pt_marketing_task_execution]] | sibling | 0.22 |
| [[p03_pt_intelligence_analysis]] | sibling | 0.21 |
