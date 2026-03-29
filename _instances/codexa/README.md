# CODEXA Instance

This directory contains a COMPLETE filled instance of the CEX framework
using the CODEXA project's specific configuration:

## Agent Names & Drives (7 Deadly Sins)

| Nucleus | Agent | Drive | Lens |
|---------|-------|-------|------|
| N01 | SHAKA | ANALYTICAL ENVY | "What do they know that I don't?" |
| N02 | LILY | STRATEGIC LUST | "What desire don't they know they have?" |
| N03 | EDISON | INVENTIVE PRIDE | "Is this the best ever produced?" |
| N04 | PYTHA | SYSTEMATIC GLUTTONY | "What haven't I consumed yet?" |
| N05 | ATLAS | ACHIEVING WRATH | "Why isn't this running RIGHT NOW?" |
| N06 | YORK | VISIONARY GREED | "What value is nobody capturing?" |
| N07 | STELLA | PRODUCTIVE SLOTH | "Who should do this instead of me?" |

## Contents

- `_seeds/` -- 7 filled seed files with CODEXA-specific names and concepts
- `N01_intelligence/` through `N07_admin/` -- 73 filled nucleus artifacts
- Each artifact has CODEXA-specific content replacing the {{VARIABLE}} templates

## How This Was Built

1. Extracted seeds from CODEXA PRIME documents + mental_model.yaml files
2. Ran `cex_nucleus_builder.py` for each nucleus with CODEXA seeds
3. Ran `cex_bootstrap.py --level 2` for vertical domain expansion
4. Fixed LLM output formatting (frontmatter closers, YAML codeblocks)

## To Create Your Own Instance

```bash
# 1. Copy seed templates
cp _seeds/seed_n{01-07}.txt _instances/myproject/_seeds/

# 2. Fill {{VARIABLES}} in each seed with YOUR names, drives, concepts

# 3. Run nucleus builder
bash _tools/build_all_nuclei.sh

# 4. Expand with domain kinds
python _tools/cex_bootstrap.py --all --level 2
```

Your instance lives alongside CODEXA's -- the framework is the same,
only the filling changes.
