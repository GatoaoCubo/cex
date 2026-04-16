---
kind: output_template
id: bld_output_template_faq_entry
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for faq_entry production
quality: 8.8
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

```markdown
---
id: p01_faq_{{topic_slug}}.md
kind: faq_entry
pillar: P01
title: "{{question_text}}"
version: "1.0.0"
created: {{created_date}}
updated: {{updated_date}}
author: {{author}}
domain: {{domain}}           <!-- e.g., account_management | billing | product | security -->
quality: null
tags: [{{tag_1}}, {{tag_2}}, faq]
tldr: "{{one_sentence_answer_summary}}"
question: "{{question_text}}"
answer: "{{canonical_answer}}"
category: {{category}}       <!-- e.g., getting_started | billing | troubleshooting | account -->
related_topics:
  - {{related_faq_1}}
  - {{related_faq_2}}
---

## {{question_text}}

{{canonical_answer_paragraph_1}}

{{canonical_answer_paragraph_2_if_needed}}

**Steps (if procedural):**
1. {{step_1}}
2. {{step_2}}
3. {{step_3}}

**Related:** [{{related_topic_1}}]({{related_link_1}}) | [{{related_topic_2}}]({{related_link_2}})
```

<!-- Schema.org FAQPage structured data snippet (inject in HTML <head>) -->
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "{{question_text}}",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "{{canonical_answer}}"
    }
  }]
}
```
