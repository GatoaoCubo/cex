---
id: p01_kc_skill_references
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Skill References Pattern — Lightweight Interface + On-Demand Depth"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: knowledge_engineering
quality: 9.1
tags: [skill-references, token-efficiency, progressive-disclosure, information-architecture]
tldr: "Lightweight SKILL.md (workflow + quick ref) + deep sub-files (tables, examples) optimizes tokens and keeps depth accessible"
when_to_use: "Decide how to structure skill content between lightweight interface and deep reference"
keywords: [skill-references, progressive-disclosure, token-efficiency, information-architecture]
long_tails:
  - "How to separate skill interface from deep references to optimize tokens"
  - "When to create auxiliary reference files for an agent skill"
axioms:
  - "ALWAYS keep SKILL.md below 200 lines — depth goes to sub-files"
  - "NEVER duplicate content between SKILL.md and reference files"
linked_artifacts:
  primary: p01_kc_skill_format_universal
  related: [p01_kc_cex_function_become]
density_score: null
data_source: "https://github.com/kepano/obsidian-skills"
related:
  - p01_kc_agentskills_spec
  - p01_kc_skill_format_universal
  - bld_collaboration_skill
  - p01_kc_query_decomposition
  - bld_architecture_skill
  - bld_memory_skill
  - bld_knowledge_card_procedural_memory
  - procedural-memory-builder
  - bld_system_prompt_skill
  - skill-builder
---

## Summary

Two-level pattern for LLM agent skills: SKILL.md as lightweight interface (always loaded) + reference sub-files as on-demand depth.
Reduces token cost by 60-80% while maintaining full access to details when needed.
Originated in obsidian-skills (kepano), replicated in multi-agent systems with ISO vectorstore.

## Spec

| Layer | Content | Loading | Target Size |
|-------|---------|---------|-------------|
| SKILL.md | Workflow, quick ref, links, simple examples | Always (context) | < 200 lines |
| sub-files | Complete tables, edge cases, extensive examples | On-demand | No fixed limit |

Criteria for creating a reference sub-file:

| Condition | Action |
|-----------|--------|
| SKILL.md would exceed 200 lines | Extract to sub-file |
| Table with more than 10 items | Move complete table |
| Heavy complete examples | Keep synthesis inline, complete in sub-file |

SKILL.md faz links explicitos para sub-arquivos:
```markdown
See [CALLOUTS.md](sub-arquivo/CALLOUTS.md) for the full list.
```

## Patterns

| Trigger | Action |
|---------|--------|
| Skill with >200 lines of total content | Extract tables and examples to sub-files |
| Reference table with >10 entries | Dedicated sub-file with link from SKILL.md |
| Agent needs edge-case details | Explicit link in SKILL.md points to detail |
| Multiple complete examples | Inline has synthesis, sub-file has complete |
| New skill being created in multi-agent system | Plan SKILL.md + sub-files from the start |

## Anti-Patterns

- Monolithic skill without sub-files (bloated context, wasted tokens)
- Sub-files without explicit links from SKILL.md (inaccessible depth)
- Content duplication between SKILL.md and sub-files (inconsistency)
- Critical content only in sub-file (agent misses essential info)
- Sub-file with 1-2 lines (file overhead without real benefit)

## Code

<!-- lang: text | purpose: real examples from obsidian-skills -->
```
# obsidian-markdown/ (kepano/obsidian-skills)
SKILL.md                  # Workflow 6 steps, wikilinks, basic callouts
  sub-files/
    CALLOUTS.md           # 13 types + aliases, foldable, nested, custom CSS
    EMBEDS.md             # Audio, video, PDF, search embeds, external images
    PROPERTIES.md         # All property types, tag syntax rules

# obsidian-bases/
SKILL.md                  # Schema YAML, filter/formula syntax, view types
  sub-files/
    FUNCTIONS_REFERENCE.md  # Functions by type: Date, String, Number, List

# json-canvas/
SKILL.md                  # Complete spec: nodes, edges, colors, layout
  sub-files/
    EXAMPLES.md           # 4 JSON examples: mind map, project board, flowchart
```

```yaml
# Equivalente em sistema multi-agente:
agent_structure:
  interface: "README.md"           # Overview, quick ref
  depth:
    - "MANIFEST.md"                # Capabilities list
    - "INSTRUCTIONS.md"            # Execution protocol
    - "EXAMPLES.md"                # Input/output samples
    - "SCHEMA.md"                  # JSON schema
  principle: "lightweight interface + on-demand depth"
```

## References

- source: https://github.com/kepano/obsidian-skills
- source: https://docs.anthropic.com/en/docs/claude-code
- related: p01_kc_skill_format_universal
- related: p01_kc_cex_function_become

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_agentskills_spec]] | sibling | 0.43 |
| [[p01_kc_skill_format_universal]] | sibling | 0.40 |
| [[bld_collaboration_skill]] | downstream | 0.38 |
| [[p01_kc_query_decomposition]] | sibling | 0.33 |
| [[bld_architecture_skill]] | downstream | 0.33 |
| [[bld_memory_skill]] | downstream | 0.32 |
| [[bld_knowledge_card_procedural_memory]] | sibling | 0.30 |
| [[procedural-memory-builder]] | downstream | 0.30 |
| [[bld_system_prompt_skill]] | downstream | 0.30 |
| [[skill-builder]] | downstream | 0.28 |
