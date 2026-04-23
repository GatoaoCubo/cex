---
name: New Builder
about: Propose or claim a builder for a kind that has none yet
labels: "good first issue, builder"
related:
  - bld_architecture_kind
  - kind-builder
  - bld_collaboration_kind
  - bld_tools_kind
  - bld_instruction_kind
  - bld_collaboration_builder
  - p03_sp_kind_builder
  - _builder-builder
  - bld_schema_kind
  - bld_knowledge_card_kind
---

## Kind

<!-- Which kind? Run: python -c "import json; from pathlib import Path; meta=json.loads(Path('.cex/kinds_meta.json').read_text(encoding='utf-8')); built={p.name.replace('-builder','') for p in Path('archetypes/builders').iterdir() if p.is_dir()}; [print(k) for k in sorted(meta) if k not in built]" -->

**Kind name:** 

## Why it matters

<!-- One sentence: what problem does this builder solve or what artifact does it produce? -->

## Pre-flight checklist

Before opening a PR:

- [ ] Kind exists in `.cex/kinds_meta.json`
- [ ] No builder directory exists at `archetypes/builders/{kind}-builder/`
- [ ] All 13 ISO files are present and non-empty
- [ ] `python _tools/cex_doctor.py` shows 0 FAIL
- [ ] PR title follows format: `[builder] add {kind}-builder`
- [ ] `quality: null` in every frontmatter (no self-scoring)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | related | 0.51 |
| [[kind-builder]] | related | 0.49 |
| [[bld_collaboration_kind]] | related | 0.40 |
| [[bld_tools_kind]] | related | 0.38 |
| [[bld_instruction_kind]] | related | 0.35 |
| [[bld_collaboration_builder]] | related | 0.32 |
| [[p03_sp_kind_builder]] | related | 0.29 |
| [[_builder-builder]] | related | 0.27 |
| [[bld_schema_kind]] | related | 0.26 |
| [[bld_knowledge_card_kind]] | related | 0.26 |
