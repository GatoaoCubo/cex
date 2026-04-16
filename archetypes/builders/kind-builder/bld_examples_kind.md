---
kind: examples
id: bld_examples_kind
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of builder package scaffolding
pattern: few-shot learning -- LLM reads these before producing
quality: 9.0
title: "Examples Kind Builder"
version: "1.0.0"
author: n03_builder
tags: [kind_builder, builder, examples, meta-builder]
tldr: "Golden example of a complete builder manifest ISO + anti-example showing common scaffolding failures."
domain: "kind builder construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Examples: kind-builder

## Golden Example

INPUT: "Create builder for kind: env_config (P09, GOVERN)"

OUTPUT (manifest ISO only -- showing quality standard for all 13):

```yaml
---
id: env-config-builder
kind: type_builder
pillar: P09
parent: null
domain: env_config
llm_function: GOVERN
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
tags: [kind-builder, env-config, P09, config, environment, variables]
keywords: [env, environment, variable, config, secret, dotenv, envvar, settings]
triggers: ["define environment variables", "create env config", "document system variables"]
capabilities: >
  L1: Specialist in building env_config artifacts.
  L2: Define environment variables with scope, type, default, and sensitivity.
  L3: When user needs to create or scaffold env config.
quality: null
title: "Manifest Env Config"
tldr: "Specialist in env_config artifacts: variable catalogs with scope, type, default, validation, sensitivity."
density_score: 0.90
---
# env-config-builder
## Identity
Specialist in building env_config artifacts -- specifications of environment
variables for a system scope. Masters scoping (global, agent_group, service),
sensitive var handling, defaults, validation rules, override precedence, and
the boundary between env_config (generic variables) and boot_config (P02,
per-provider) or feature_flag (P09, logical on/off).
## Capabilities
1. Define environment variables with scope, type, default, and sensitivity
2. Specify validation rules (regex, range, enum) per variable
3. Document override precedence (env > file > default)
4. Mark sensitive variables with masking rules
5. Validate against quality gates (HARD + SOFT)
6. Distinguish env_config from boot_config, feature_flag, path_config
## Routing
keywords: [env, environment, variable, config, secret, dotenv]
triggers: "define environment variables", "create env config"
## Crew Role
In a crew, I handle ENVIRONMENT VARIABLE SPECIFICATION.
I answer: "what environment variables does this scope need?"
I do NOT handle: boot_config, feature_flag, path_config, permission.
```

WHY THIS IS GOLDEN:
- quality: null (H01 pass -- never self-scored)
- kind: type_builder (H02 pass -- correct meta-kind)
- All required frontmatter fields present (H03 pass)
- 6 capabilities listed, each specific to the domain (H04 pass)
- Boundary section clearly states what this builder IS NOT (H05 pass)
- Routing keywords match the kind's domain vocabulary (S01 pass)
- Crew role defines scope and exclusions (S02 pass)
- tldr is 82 chars, under 160 limit (S03 pass)
- ASCII-only content, no emoji (S04 pass)

## Complete Package Checklist (all 13 files for env-config-builder)

| # | File | Exists | quality: null | Domain content |
|---|------|--------|---------------|----------------|
| 1 | bld_manifest_env_config.md | YES | YES | env_config identity + 6 capabilities |
| 2 | bld_schema_env_config.md | YES | YES | 15+ frontmatter fields + 4 body sections |
| 3 | bld_system_prompt_env_config.md | YES | YES | 13 rules for env_config production |
| 4 | bld_instruction_env_config.md | YES | YES | 3-phase process with 20+ steps |
| 5 | bld_output_template_env_config.md | YES | YES | YAML template + 4 body section templates |
| 6 | bld_examples_env_config.md | YES | YES | Golden + anti with gate analysis |
| 7 | bld_memory_env_config.md | YES | YES | 5-field variable pattern + evidence |
| 8 | bld_tools_env_config.md | YES | YES | brain_query, validate_artifact tools |
| 9 | bld_quality_gate_env_config.md | YES | YES | 10 HARD + 12 SOFT dimensions |
| 10 | bld_knowledge_card_env_config.md | YES | YES | 12-Factor, dotenv, K8s references |
| 11 | bld_architecture_env_config.md | YES | YES | 9 components + dependency graph |
| 12 | bld_collaboration_env_config.md | YES | YES | 2 crew compositions + handoff protocol |
| 13 | bld_config_env_config.md | YES | YES | naming, paths, size limits |

## Anti-Example

INPUT: "Create builder for kind: env_config"

BAD OUTPUT:

```
archetypes/builders/env-config-builder/
  bld_manifest_env_config.md    (3 lines, no frontmatter)
  bld_schema_env_config.md      (empty)
  bld_instruction_env_config.md (says "TODO: fill in")
```

FAILURES:
1. Only 3 of 13 files created -- H01 FAIL (incomplete package)
2. bld_manifest has no YAML frontmatter -- H03 FAIL
3. bld_schema is empty -- H04 FAIL (no domain content)
4. bld_instruction has placeholder text -- H04 FAIL (generic filler)
5. Missing 10 ISO files -- H01 FAIL
6. No sub-agent file at .claude/agents/ -- H05 FAIL
7. No quality: null field anywhere -- H01 FAIL
8. No boundary section in any file -- S05 FAIL
9. No cross-reference to related kinds -- S06 FAIL
10. No golden example to validate against gates -- S07 FAIL
