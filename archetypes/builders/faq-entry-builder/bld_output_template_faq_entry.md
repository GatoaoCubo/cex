---
kind: output_template
id: bld_output_template_faq_entry
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for faq_entry production
quality: null
title: "Output Template Faq Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [faq_entry, builder, output_template]
tldr: "Template with vars for faq_entry production"
domain: "faq_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p01_faq_{{name}}.md
title: {{title}}
pillar: P01
category: {{category}}
quality: null
---
```

<!-- FAQ entry title -->
<!-- Category (e.g., "Trading", "Account Management") -->
<!-- Must match naming pattern: p01_faq_[a-z][a-z0-9_]+.md -->

## Example Questions & Answers

| Question                          | Answer                                                                 |
|----------------------------------|------------------------------------------------------------------------|
| How do I withdraw funds?         | {{withdrawal_steps}}                                                   |
| What are trading fees?           | {{fee_structure}}                                                      |

<!-- Withdrawal steps as markdown list -->
<!-- Fee structure as plain text -->

```markdown
**Answer Example:**
1. Navigate to the 'Wallet' section
2. Select 'Withdraw' and choose asset
3. Enter amount and recipient address
```

<!-- Code block showing answer formatting -->
