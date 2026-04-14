---
kind: output_template
id: bld_output_template_contributor_guide
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for contributor_guide production
quality: null
title: "Output Template Contributor Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [contributor_guide, builder, output_template]
tldr: "Template with vars for contributor_guide production"
domain: "contributor_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
title: {{title}} <!-- Guide title -->
description: {{description}} <!-- Brief overview of guide purpose -->
quality: null <!-- Always null -->
id: p05_cg_{{name}}.md <!-- Filename: p05_cg_<lowercase alphanumeric>_md -->
---
```

## Contributing Process

| Step | Description |
|------|-------------|
| 1    | {{step1}} <!-- Initial setup instructions -->
| 2    | {{step2}} <!-- Code submission workflow -->

```markdown
<!-- Sample contribution format -->
## Example Pull Request

**Title:** {{pr_title}} <!-- Clear, concise PR title -->

**Body:**
- Fixes: {{issue_number}} <!-- Reference related issue -->
- Changes: {{changes_summary}} <!-- Summary of modifications -->
```

## Code Standards

```python
# Example function structure
def {{function_name}}(params):
    """{{docstring}} <!-- Function purpose -->"""
    # {{implementation}} <!-- Logic here -->
    return result
```
