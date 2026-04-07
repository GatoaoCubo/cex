---
id: ex_component_map_pipeline
kind: component_map
pillar: P08
title: "Example — Pipeline Engine Component Map"
tags: [architecture, pipeline, components, 8f, engine]
tldr: "Maps the CEX 8F pipeline to concrete components: Python orchestrator, LLM call, YAML parser, Jinja2 templates, and git integration. Shows data flow between stages."
references:
  - tpl_component_map
  - ex_mental_model_pipeline
  - ex_dispatch_rule_research
quality: 9.0
---

# Pipeline Engine Component Map

## Architecture Overview
```
CAPTURE ──→ DECOMPOSE ──→ HYDRATE ──→ COMPILE ──→ ENVELOPE
(Python)    (LLM micro)   (YAML/Py)   (LLM gen)   (Git/Py)
```

## Component Detail

| Component | Technology | Responsibility | Files |
|-----------|-----------|----------------|-------|
| Intent Parser | Python (regex + rules) | Parse natural language → kind + intent | `cex_8f_motor.py` |
| Builder Loader | Python (YAML) | Load 13 ISOs from builder dir | `cex_8f_runner.py` |
| KC Injector | Python + YAML | Load knowledge cards for kind | `cex_8f_runner.py` F3 |
| Prompt Composer | Python (string concat) | Assemble ISOs → LLM prompt | `cex_8f_runner.py` F6 |
| LLM Engine | Anthropic API | Generate artifact content | `cex_intent.py` |
| Output Cleaner | Python (regex) | Strip LLM wrapper text | `_clean_llm_output()` |
| Gate Validator | Python + YAML | Check 6 hard gates on output | `cex_8f_runner.py` F7 |
| File Writer | Python (pathlib) | Save .md + compile .yaml | `cex_8f_runner.py` F8 |
| Git Integrator | subprocess (git) | Stage + commit + signal | `cex_8f_runner.py` F8 |

## Data Flow
```
Intent (str) → RunState{} → +constraints → +identity → +knowledge
  → prompt (str) → LLM → raw_output (str) → clean (str)
    → validate (pass/fail) → save (path) → commit (hash)
```

## Dependencies
```
cex_8f_runner.py
  ├── cex_8f_motor.py    (intent parsing, kind resolution)
  ├── cex_intent.py      (LLM API calls)
  ├── cex_shared.py      (frontmatter, file utilities)
  ├── cex_errors.py      (typed exceptions)
  ├── cex_compile.py     (md → yaml compilation)
  └── cex_score.py       (quality scoring)
```

## Quality Gate
- [ ] Every component has owner file identified
- [ ] Data flow shows transformations at each stage
- [ ] Dependencies are explicit (no hidden coupling)
- [ ] Technology choices documented
