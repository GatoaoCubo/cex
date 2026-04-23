---
id: n04_naming_convention_mapping
kind: validation_schema
nucleus: N04
pillar: P06
domain: nomenclature
quality: 9.1
created: 2026-04-02
type: mapping_schema
scope: builders_to_kcs
density_score: 1.0
title: "Naming Convention Mapping"
version: 1.0.0
author: N04
tags: [validation_schema, knowledge, validation-schema, cex, artifact]
tldr: "Naming rules mapping CEX artifact types to filesystem paths and identifiers"
updated: 2026-04-07
related:
  - bld_architecture_kind
  - bld_collaboration_builder
  - bld_collaboration_kind
  - kind-builder
  - bld_tools_kind
  - _builder-builder
  - bld_collaboration_retriever
  - bld_knowledge_card_builder
  - bld_collaboration_naming_rule
  - bld_collaboration_knowledge_card
---

# Builder ↔ KC Naming Convention Mapping

## The Problem
- **Builders**: use hyphen format (`action-prompt-builder`)
- **KCs**: use underscore format (`kc_action_prompt.md`)
- **Impact**: Breaks automated cross-referencing and tooling

## Conversion Rules

### Builder → KC
```python
def builder_to_kc(builder_name):
    # Remove -builder suffix
    core_name = builder_name.replace('-builder', '')
    # Convert hyphens to underscores  
    kc_name = core_name.replace('-', '_')
    # Add kc_ prefix and .md suffix
    return f"kc_{kc_name}.md"

# Examples:
# action-prompt-builder → kc_action_prompt.md
# knowledge-card-builder → kc_knowledge_card.md
```

### KC → Builder  
```python
def kc_to_builder(kc_filename):
    # Remove kc_ prefix and .md suffix
    core_name = kc_filename[3:-3]  # Strip 'kc_' and '.md'
    # Convert underscores to hyphens
    builder_name = core_name.replace('_', '-')  
    # Add -builder suffix
    return f"{builder_name}-builder"

# Examples:
# kc_action_prompt.md → action-prompt-builder
# kc_knowledge_card.md → knowledge-card-builder  
```

## Special Cases
| Builder | KC | Notes |
|---------|----|----- |
| `_builder` | None | Meta-builder, no KC needed |
| `skill-builder` | `kc_skill.md` | ✅ Exists |
| None | `kc_supervisor.md` | ❌ Orphan KC, no builder |

## Validation Queries

```bash
# Find builders without KCs
find archetypes/builders/ -name "*-builder" | while read b; do
  builder=$(basename $b)
  kc_name="kc_$(echo $builder | sed 's/-builder//' | sed 's/-/_/g').md"
  if [ ! -f "P01_knowledge/library/kind/$kc_name" ]; then
    echo "MISSING KC: $kc_name (for $builder)"
  fi
done

# Find KCs without builders  
find P01_knowledge/library/kind/ -name "kc_*.md" | while read k; do
  kc_file=$(basename $k)
  builder_name="$(echo $kc_file | sed 's/kc_//' | sed 's/.md//' | sed 's/_/-/g')-builder"
  if [ ! -d "archetypes/builders/$builder_name" ]; then
    echo "ORPHAN KC: $kc_file (no $builder_name)"
  fi
done
```

## Tool Integration
This mapping should be used in:
- `cex_retriever.py` - cross-reference lookups
- `cex_8f_motor.py` - builder discovery  
- `cex_compile.py` - KC validation
- `cex_memory_select.py` - knowledge injection

## Recommended Fix
1. **Standardize on underscores** system-wide
2. **Create transition period** with dual lookup
3. **Update tooling** to handle both formats  
4. **Migrate builders** to underscore naming
5. **Establish naming rule enforcement** in validation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | downstream | 0.44 |
| [[bld_collaboration_builder]] | downstream | 0.40 |
| [[bld_collaboration_kind]] | downstream | 0.37 |
| [[kind-builder]] | downstream | 0.36 |
| [[bld_tools_kind]] | upstream | 0.32 |
| [[_builder-builder]] | upstream | 0.30 |
| [[bld_collaboration_retriever]] | downstream | 0.29 |
| [[bld_knowledge_card_builder]] | upstream | 0.28 |
| [[bld_collaboration_naming_rule]] | upstream | 0.28 |
| [[bld_collaboration_knowledge_card]] | downstream | 0.27 |
