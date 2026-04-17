---
id: p02_iso_organization_agent
kind: agent_package
pillar: P02
agent_name: organization
tier: complete
files_count: 12
quality_gates:
  score_min: 8.0
  density_min: 0.8
  no_hardcoded_paths: true
version: 1.0.0
created: 2026-03-24
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [agent-package, portable, agent-bundle, llm-agnostic]
---

# ISO Package: organization

## Required Files
| File | LP | Purpose |
|------|----|---------|
| manifest.yaml | P02 | Agent identity, capabilities, routing keywords |
| system_instruction.md | P03 | LLM system prompt (persona + guardrails) |
| instructions.md | P03 | Execution protocol (step-by-step workflow) |

Without these 3 files, the agent cannot be instantiated on any LLM provider.

## Recommended Files
| File | LP | Purpose |
|------|----|---------|
| architecture.md | P08 | System design (ASCII diagrams, component map) |
| output_template.md | P05 | Expected output format specification |
| examples.md | P07 | Input/output pairs for few-shot learning |
| error_handling.md | P11 | Recovery patterns and failure modes |

## Optional Files
| File | LP | Purpose |
|------|----|---------|
| quick_start.md | P01 | 5-minute onboarding guide |
| input_schema.yaml | P06 | Formal input validation schema |
| upload_kit.md | P04 | Deployment bundle instructions |
| upload_kit_whitelabel.md | P04 | Multi-brand variant |

## Tier
| Tier | Files | Use Case |
|------|-------|----------|
| minimal | 3 (required only) | Quick prototype, testing |
| standard | 7 (+recommended) | Production agent |
| complete | 10 (+optional) | Full deployment with onboarding |
| whitelabel | 12 (+whitelabel variants) | Multi-brand distribution |

## Quality Gates
- System instruction: max 4096 tokens (fits in any LLM context)
- Examples: min 2 input/output pairs per agent
- Density: >= 0.8 (no filler content)
- Score: >= 8.0 for pool promotion
- No hardcoded paths (LLM-agnostic portability)

## LP Mapping
Each ISO file maps to exactly one CEX LP, making agents inherently 12LP-compliant:

```
manifest.yaml        -> P02 Model (who)
system_instruction   -> P03 Prompt (how speaks)
instructions         -> P03 Prompt (how executes)
architecture         -> P08 Architecture (structure)
output_template      -> P05 Output (format)
examples             -> P07 Evals (validation)
error_handling       -> P11 Feedback (recovery)
quick_start          -> P01 Knowledge (onboarding)
input_schema         -> P06 Schema (validation)
upload_kit           -> P04 Tools (deployment)
```

Key insight: ISO packages are **LLM-agnostic**. Same package works with Claude, GPT, Gemini, Llama. The system_instruction adapts to provider capabilities but core identity is constant.

Source: `records/agents/organization/` (12 files, tier complete)
