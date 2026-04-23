## Context Self-Selection Protocol (G8)

When you receive a task (via handoff or interactive), automatically discover and load relevant context BEFORE producing output.

### Priority Order

1. **Handoff file**: If `.cex/runtime/handoffs/{nucleus}_task.md` has `auto_composed: true` frontmatter, context is pre-resolved. Load the paths listed in its "Context (auto-discovered)" section.

2. **Manual scan**: If no auto-composed handoff, identify the artifact kinds in your task, then load:
   - **Knowledge Card**: `P01_knowledge/library/kind/kc_{kind}.md` — definitions, boundaries, naming
   - **Builder ISOs**: `archetypes/builders/{kind}-builder/bld_*.md` — instructions, templates, examples, scoring
   - **Pillar schema**: `P{XX}_*/_schema.yaml` — required frontmatter fields
   - **Examples**: `P01_knowledge/examples/ex_{kind}_*.md` — gold-standard references

3. **Programmatic discovery**: For complex or multi-kind tasks, run:
   ```
   python _tools/cex_handoff_composer.py --task "<your task>" --nucleus <your_id> --discover-only
   ```
   This outputs all relevant paths via TF-IDF + keyword scoring against the 117-kind registry.

### Rules

- **Load before produce**: Never generate an artifact without first reading its KC + at least the builder instruction ISO.
- **Kind registry**: `.cex/kinds_meta.json` maps every kind to its pillar, description, and naming convention.
- **Decision manifest**: `.cex/runtime/decisions/decision_manifest.yaml` contains user decisions. Do NOT re-ask what's already decided.
- **Frontmatter is mandatory**: Every artifact must have YAML frontmatter matching the pillar schema.
- **8F applies**: The context you load informs F2 (Frame) and F3 (Filter). Skip nothing.

### Prompt Compiler (Intent Resolution)
Source of truth: `P03_prompt/layers/p03_pc_cex_universal.md`
Always resolve user intent through this artifact before dispatching.
It maps natural language (PT-BR + EN) to `{kind, pillar, nucleus, verb}` tuples for all 124 CEX kinds.
