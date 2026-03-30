---
kind: examples
id: bld_examples_agent_package
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of agent_package artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: agent-package-builder
## Golden Example
INPUT: "Package the data-analyst agent as a standard ISO bundle"
OUTPUT:
```yaml
id: p02_iso_data_analyst
kind: agent_package
pillar: P02
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
agent_name: "data-analyst"
tier: "standard"
files_count: 7
domain: "data_analysis"
llm_function: BECOME
portable: true
lp_mapping:
  manifest.yaml: P02
  system_instruction.md: P03
  instructions.md: P03
  architecture.md: P08
  output_template.md: P05
  examples.md: P07
  error_handling.md: P11
system_instruction_tokens: 2840
quality: null
tags: [agent-package, data-analysis, analytics, P02]
tldr: "Standard 7-file ISO bundle for data-analyst agent with analysis pipeline and error handling"
density_score: 0.88
```
## Agent Identity
data-analyst is a data analysis specialist. Transforms raw datasets into structured
insights via statistical analysis, visualization, and pattern detection.
## File Inventory
| File | Pillar | Tier | Status |
|------|--------|------|--------|
| manifest.yaml | P02 | minimal | present |
| system_instruction.md | P03 | minimal | present |
| instructions.md | P03 | minimal | present |
| architecture.md | P08 | standard | present |
| output_template.md | P05 | standard | present |
| examples.md | P07 | standard | present |
| error_handling.md | P11 | standard | present |
| quick_start.md | P01 | complete | absent |
| input_schema.yaml | P06 | complete | absent |
| upload_kit.md | P04 | complete | absent |
## Tier Compliance
Declared: standard. Files present: 7/7. No gaps.
## Portability Notes
- Platform: platform_agnostic
- Hardcoded paths: none
- External dependencies: none (self-contained analysis prompts)
## References
- Source agent: agents/data_analyst/README.md
- Builder: agent-package-builder v1.0.0
WHY THIS IS GOLDEN:
- quality: null (H05 pass) | id p02_iso_ pattern (H02 pass) | kind: agent_package (H04 pass)
- 19 fields in frontmatter (H06 pass) | 3 required files present (H07 pass)
- files_count: 7 matches directory (H08 pass) | system_instruction: 2840 tokens (H09 pass)
- No hardcoded paths (H10 pass) | tier "standard" matches 7 files (S03 pass)
- tldr: 82ch (S01 pass) | tags: 4 items with "agent-package" (S02 pass) | density: 0.88 (S06 pass)
- lp_mapping present for all 7 files (S08 pass) | File Inventory table complete (S10 pass)
## Anti-Example
INPUT: "Package my helper agent"
BAD OUTPUT:
```yaml
id: helper_package
kind: package
tier: large
files_count: 3
quality: 9.0
tags: [helper]
tldr: "This is a comprehensive package that contains all the necessary files for the helper agent to function properly across various platforms."
```
Files included: manifest.yaml, prompt.txt, readme.md
FAILURES:
1. id: no `p02_iso_` prefix -> H02 FAIL
2. kind: "package" not "agent_package" -> H04 FAIL
3. quality: 9.0 (not null) -> H05 FAIL
4. Missing 10 required fields (pillar, version, created, updated, author, agent_name, domain, quality as null, tags proper, tldr proper) -> H06 FAIL
5. Required files wrong names (prompt.txt not system_instruction.md, readme.md not instructions.md) -> H07 FAIL
6. tier: "large" not in enum [minimal, standard, complete, whitelabel] -> S03 FAIL
7. tags: only 1 item, missing "agent-package" -> S02 FAIL
8. tldr: 134ch with filler ("This is a comprehensive package that contains") -> S01+S09 FAIL
9. No lp_mapping -> S08 FAIL
10. No File Inventory table -> S10 FAIL
11. No portability check -> S11 FAIL
12. No Agent Identity section -> body structure FAIL
