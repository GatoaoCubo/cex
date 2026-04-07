---
id: p03_ap_cf_generate_ebook
kind: action_prompt
pillar: P03
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n02_marketing"
title: "Generate eBook from Topic and Chapter Plan"
action: "Generate a complete eBook with chapters, sections, and formatted content from a topic and structure definition"
input_required:
  - "topic: string — eBook subject"
  - "chapters_count: integer — number of chapters (3-15)"
  - "audience: string — target reader profile"
  - "brand_config: object — {{BRAND_*}} variables"
output_expected: "Complete eBook manuscript with frontmatter, chapters, sections, key takeaways, and lead magnet metadata"
purpose: "Produce full eBook drafts that serve as lead magnets or paid digital products without manual writing"
steps_count: 5
timeout: "180s"
edge_cases:
  - "chapters_count exceeds 15 — split into volume series"
  - "Topic overlaps existing eBook — deduplicate via content hash check"
  - "No audience specified — default to brand_config.ideal_customer"
constraints:
  - "Do NOT generate cover images — output text only, Canva handles design"
  - "Do NOT include external URLs — use placeholder {{REF_N}} for citations"
  - "Each chapter 1500-2500 words (total proportional to chapters_count)"
domain: "content_factory"
quality: 9.1
tags: [action_prompt, content_factory, ebook, lead_magnet, digital_product]
tldr: "Generate complete eBook manuscript (chapters + sections + takeaways) from topic and chapter count for lead magnet or sale"
density_score: 0.90
---

## Context
eBooks are a core content factory output — used as lead magnets, course companions,
and standalone digital products. This prompt generates the full manuscript ready for
design in Canva and distribution via email or Hotmart.
Purpose: eliminate the writing bottleneck in eBook production.

## Input
| Item | Type | Format | Required |
|------|------|--------|----------|
| topic | string | Free text, 3-100 chars | YES |
| chapters_count | integer | 3-15 | YES |
| audience | string | Reader profile description | YES |
| brand_config | object | {{BRAND_*}} YAML variables | YES |

## Execution
1. Analyze topic and audience to determine depth, tone, and vocabulary level
2. Generate table of contents with chapter titles and 3-5 section headings each
3. Write each chapter: introduction, sections (300-500 words each), key takeaways box
4. Generate frontmatter: title page text, about the author (from brand_config), disclaimer
5. Compile lead magnet metadata: landing page headline, 3 bullet benefits, CTA text

## Output
Format: Markdown
Structure:
```markdown
# {{eBook Title}}
## Sobre o Autor
{{from brand_config.about}}

## Capítulo 1: {{title}}
### {{section_1}}
{{300-500 words}}
### Principais Aprendizados
- {{takeaway_1}}
- {{takeaway_2}}

---
## Lead Magnet Metadata
headline: "{{headline}}"
bullets: ["{{benefit_1}}", "{{benefit_2}}", "{{benefit_3}}"]
cta: "{{cta_text}}"
```

## Validation
- All chapters present matching chapters_count
- Each chapter has 1500-2500 words with at least 3 sections
- Key takeaways box present in every chapter (2-4 items)
- Lead magnet metadata complete (headline + 3 bullets + CTA)
- Edge case: 15+ chapters triggers volume split recommendation

## References
- Canva API (cover design downstream)
- wf_cf_promote (promotion workflow)
- brand_config.yaml (author bio, voice)
