---
id: p02_iso_codexa_agent
type: iso_package
lp: P02
agent_name: codexa
tier: complete
files_count: 10
quality_gates:
  score_min: 8.0
  density_min: 0.8
  no_hardcoded_paths: true
  system_instruction_max_tokens: 4096
  min_examples: 2
version: 1.1.0
created: 2026-03-24
author: EDISON
domain: meta-construction
quality: 9.0
tags: [iso-package, portable, agent-bundle, llm-agnostic]
---

# CODEXA Agent — ISO Package

## Package Structure
```
records/agents/codexa/
  README.md                                # Agent overview (P02)
  iso_vectorstore/
    ISO_EDISON_054_MANIFEST.md             # Capabilities index
    ISO_EDISON_055_INSTRUCTIONS.md         # Execution protocol
    ISO_EDISON_055_QUICK_START.md          # 5-min onboarding
    ISO_EDISON_056_PRIME.md                # Core identity
    ISO_EDISON_057_ARCHITECTURE.md         # System design
    ISO_EDISON_058_ERROR_HANDLING.md       # Recovery patterns
    ISO_EDISON_059_OUTPUT_TEMPLATE.md      # Output format spec
    ISO_EDISON_060_EXAMPLES.md             # Input/output pairs
    ISO_EDISON_061_UPLOAD_KIT.md           # Deployment bundle
    ISO_EDISON_062_SYSTEM_INSTRUCTION.md   # LLM system prompt
  blocks/
    BLK_EDISON_001_BUILDER.md              # Construction patterns
    BLK_EDISON_002_PROMPT_BUILDER.md       # TAC-7 patterns
    BLK_EDISON_003_VALIDATOR_12LP.md       # 12LP validation logic
```

## Tier System
| Tier | Files | Use Case |
|------|-------|----------|
| minimal | 3 (manifest, system_instruction, instructions) | Quick prototype |
| standard | 7 (+architecture, output, examples, errors) | Production agent |
| complete | 10 (+quick_start, input_schema, upload_kit) | Full distribution |
| whitelabel | 12 (+whitelabel variants) | Client-branded agent |

## LP Mapping
| File | LP | Domain |
|------|----|--------|
| manifest.yaml | P02 | Model identity |
| system_instruction.md | P03 | Prompt/Voice |
| instructions.md | P03 | Execution protocol |
| architecture.md | P08 | Topology |
| output_template.md | P05 | Output format |
| examples.md | P07 | Few-Shot evals |
| error_handling.md | P11 | Escalation/Feedback |

ISO packages are LLM-agnostic. Same package works with Claude, GPT, Gemini.
Quality: score >= 8.0, density >= 0.8. Maturity: 10=baseline, 17=mature, 22+=golden.
