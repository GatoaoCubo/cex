---
kind: output_template
id: bld_output_template_diff_strategy
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for diff_strategy production
quality: 9.1
title: "Output Template Diff Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [diff_strategy, builder, output_template]
tldr: "Template with vars for diff_strategy production"
domain: "diff_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

```yaml
---
kind: diff_strategy
id: p04_ds_{{name}}
pillar: P04
title: "{{strategy_title}}"
version: "1.0"
algorithm_type: "{{Myers|LCS|patience|histogram|Ratcliff-Obershelp|custom}}"
granularity: "{{line|token|character|AST|semantic}}"
comparison_basis: "{{edit_distance|unique_lines_LCS|gestalt}}"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{application_domain}}"
quality: null
tags: [diff_strategy, {{algorithm_type}}, {{granularity}}]
tldr: "{{one-sentence summary of algorithm choice and target use case}}"
---

## Overview
{{Purpose of this diff strategy. Which code-agent or pipeline uses it.
Which algorithm and why it was chosen over alternatives.}}

## Algorithm
| Property          | Value                              |
|:------------------|:-----------------------------------|
| Algorithm         | {{Myers|patience|histogram|...}}   |
| Time complexity   | {{O(ND) | O(N log N) | O(NM)}}    |
| Space complexity  | {{O(D) | O(N)}}                    |
| Granularity       | {{line|token|AST}}                 |
| Patch format      | {{unified diff | context diff | custom}} |

## Patch Application
{{How this strategy's output is applied. Tool used (git apply / patch / difflib).
Whether --3way fallback is enabled. Whitespace handling.}}

## Edge Cases
| Case               | Handling                                        |
|:-------------------|:------------------------------------------------|
| Empty diff         | {{return identity / no-op}}                     |
| Binary file        | {{detect NUL bytes; fall back to bsdiff}}       |
| CRLF/LF mismatch   | {{normalize before diff; restore on apply}}     |
| Identical files    | {{short-circuit; emit empty script}}            |
| Partial match      | {{apply clean hunks; flag conflicts}}           |

## Use Cases
{{When to choose this strategy. Comparison with alternatives.}}
```
