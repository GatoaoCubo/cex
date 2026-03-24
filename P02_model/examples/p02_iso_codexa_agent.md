---
id: p02_iso_codexa_agent
type: iso_package
lp: P02
agent_name: codexa
tier: complete
files_count: 12
quality_gates:
  score_min: 8.0
  density_min: 0.8
  no_hardcoded_paths: true
  system_instruction_max_tokens: 4096
  min_examples: 2
version: 1.0.0
created: 2026-03-24
author: EDISON
domain: meta-construction
quality: 9.0
tags: [iso-package, portable, agent-bundle, llm-agnostic]
---

# CODEXA Agent ISO Package

## Package Structure
```
records/agents/codexa/
  README.md
  iso_vectorstore/
    ISO_EDISON_060_MANIFEST.md
    ISO_EDISON_060_PRIME.md
    ISO_EDISON_060_INSTRUCTIONS.md
    ISO_EDISON_060_ARCHITECTURE.md
    ISO_EDISON_060_QUICK_START.md
    ISO_EDISON_060_OUTPUT_TEMPLATE.md
    ISO_EDISON_060_EXAMPLES.md
    ISO_EDISON_060_ERROR_HANDLING.md
    ISO_EDISON_060_UPLOAD_KIT.md
    ISO_EDISON_060_SYSTEM_INSTRUCTION.md
  prompts/
    HOP_EDISON_004_BUILDER_HOP.md
    HOP_EDISON_009_TEMPLATE_DISTILLER_HOP.md
```

## Tier System
| Tier | Files | Use Case |
|------|-------|----------|
| minimal | 3 | Quick prototype |
| standard | 7 | Production agent |
| complete | 10 | Full deployment |
| whitelabel | 12 | Multi-brand |

## LP Mapping
| File | LP | Domain |
|------|----|--------|
| manifest.yaml | P02 | Model identity |
| system_instruction.md | P03 | Prompt |
| architecture.md | P08 | Architecture |
| output_template.md | P05 | Output |
| examples.md | P07 | Evals |
| error_handling.md | P11 | Feedback |

ISO packages are LLM-agnostic. Same package works with Claude, GPT, Gemini.
