---
kind: config
id: bld_config_instruction
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: instruction Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p03_ins_{task_slug}.md` | `p03_ins_rebuild_brain_faiss.md` |
| Builder directory | kebab-case | `instruction-builder/` |
| Frontmatter fields | snake_case | `steps_count`, `validation_method` |
| Task slug | snake_case, lowercase | `rebuild_brain_faiss`, `deploy_api` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P03_prompt/examples/p03_ins_{task_slug}.md`
- Compiled: `cex/P03_prompt/compiled/p03_ins_{task_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5500 bytes
- Density: >= 0.80
## Validation Method Enum
| Value | When to use |
|-------|-------------|
| checklist | Manual verification via checkbox list (most common) |
| automated | Script or test validates outcome |
| manual | Human judgment required (subjective) |
| none | Fire-and-forget (rare, discouraged) |
## Step Writing Rules
- One action per step (verb + object + expected outcome)
- Steps numbered sequentially (1, 2, 3...)
- Include concrete commands where applicable (not "run the script" but `python build.py --all`)
- Expected outcome after dash: "1. Run build — output shows 0 errors"
- If step has conditional: split into sub-steps (1a, 1b) or separate steps
