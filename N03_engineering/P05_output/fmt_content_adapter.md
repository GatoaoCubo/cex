---
id: p05_fmt_content_adapter
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-04-08"
updated: "2026-04-08"
author: "n03_builder"
target_format: "multi"
input_type: "structured_data"
rule_count: 12
domain: "content_factory"
quality: 9.0
tags: [formatter, content-factory, multi-format, adapter, publishing]
tldr: "Universal adapter: CEX artifact (md+frontmatter) -> 5 publishable formats (clean md, HTML, PPTX outline, video script, podcast script)"
template_engine: "mustache"
pretty_print: true
escaping: "html"
encoding: "utf8"
locale: "pt-BR"
streaming: false
keywords: [content-adapter, multi-format, publishing, conversion, pandoc, marp, typst]
density_score: 0.93
---

## Formatting Rules

| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| strip_frontmatter | raw_artifact | regex_remove | `^---[\s\S]*?---\n` | Remove YAML frontmatter block |
| normalize_headers | body_markdown | regex_replace | `^(#{1,6})\s+` -> normalized levels | Ensure H1 = title, H2 = sections |
| inject_brand_vars | body_markdown | template_expand | `{{BRAND_*}}` -> brand_config values | Resolve all mustache brand variables |
| extract_sections | body_markdown | split_by_header | `^## (.+)$` | Returns ordered list of {title, content} |
| to_clean_markdown | sections[] | reassemble | `# {title}\n\n{content}` per section | Strip internal refs, tables of quality scores |
| to_html | clean_markdown | pandoc_convert | `pandoc -f markdown -t html5 --standalone` | Add brand CSS inline, responsive meta |
| to_pptx_outline | sections[] | slide_transform | 1 section = 1 slide, bullets from paragraphs | Max 5 bullets/slide, speaker notes from detail |
| to_video_script | sections[] | temporal_map | section -> segment(duration, narration, visual_cue) | 90s total, hook/build/benefit/proof/CTA structure |
| to_podcast_script | sections[] | dialogue_map | section -> talking_point(host_a, host_b, duration) | 15-25 min, intro/body/outro, 2-host format |
| apply_brand_colors | html_output | css_inject | `--primary: {BRAND_COLORS.primary}` | Inject CSS custom properties from brand_config |
| sanitize_emojis | all_outputs | regex_replace | Unicode emoji -> ASCII tags | `[OK]`, `[WARN]`, `[!!]` per ascii-code-rule |
| validate_length | all_outputs | length_check | per-format max bytes | video: 2KB, podcast: 5KB, slides: 10KB, html: 50KB |

## Input Specification

Type: structured_data (CEX artifact)

Structure: Markdown file with YAML frontmatter. Expected fields in frontmatter: `id`, `kind`, `title`, `domain`, `tags`. Body is structured Markdown with H2 sections. Artifacts may contain mustache variables (`{{BRAND_*}}`), internal cross-references, quality tables, and Properties sections that should be stripped for publication.

Example:
```markdown
---
id: kc_example
kind: knowledge_card
title: "Example Knowledge Card"
domain: "meta"
tags: [example]
---

## Introduction

Content about the topic with {{BRAND_NAME}} references.

## Core Concepts

Detailed explanation with tables and examples.

## Properties

| Property | Value |
|----------|-------|
| Kind | knowledge_card |
```

## Output Specification

Format: multi (5 target formats from single input)

### Clean Markdown
```markdown
# Example Knowledge Card

## Introduction

Content about the topic with CEX references.

## Core Concepts

Detailed explanation with tables and examples.
```

### HTML
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Example Knowledge Card</title>
  <style>:root{--primary:#0D1117;--accent:#58A6FF}</style>
</head>
<body>
  <article>
    <h1>Example Knowledge Card</h1>
    <section><h2>Introduction</h2><p>Content...</p></section>
  </article>
</body>
</html>
```

### PPTX Outline
```yaml
slides:
  - title: "Example Knowledge Card"
    bullets: []
    speaker_notes: "Title slide -- introduce topic"
  - title: "Introduction"
    bullets: ["Content about the topic", "Key point from paragraph"]
    speaker_notes: "Expand on the introduction..."
  - title: "Core Concepts"
    bullets: ["Concept 1", "Concept 2", "Concept 3"]
    speaker_notes: "Detail each concept..."
```

### Video Script
```yaml
total_duration: 90
segments:
  - phase: hook
    duration: 5
    narration: "Did you know...?"
    visual_cue: "Title card with brand logo"
  - phase: build
    duration: 30
    narration: "Here is how it works..."
    visual_cue: "Animated diagram of core concepts"
```

### Podcast Script
```yaml
total_duration: 1200
format: two_host
segments:
  - phase: intro
    duration: 60
    host_a: "Welcome to the show. Today we are covering..."
    host_b: "This is a topic I have been curious about..."
  - phase: body
    duration: 1080
    talking_points:
      - topic: "Introduction"
        host_a: "Let us start with the basics..."
        host_b: "What I find interesting is..."
```

## Template

Engine: mustache

```mustache
{{! Clean Markdown template }}
# {{title}}

{{#sections}}
## {{section_title}}

{{section_content}}

{{/sections}}
```

```mustache
{{! PPTX outline template }}
slides:
{{#sections}}
  - title: "{{section_title}}"
    bullets: [{{#bullets}}"{{.}}"{{^last}}, {{/last}}{{/bullets}}]
    speaker_notes: "{{speaker_notes}}"
{{/sections}}
```

## Edge Cases

1. **Null values**: If a frontmatter field is missing, use empty string for template vars; log warning
2. **Empty strings**: Skip empty sections entirely (do not produce blank slides or script segments)
3. **Special characters**: HTML-escape `<>&"'` for HTML output; shell-escape backticks for script formats; preserve Markdown formatting in clean-md output
4. **Overflow**: If input exceeds 50KB, truncate at nearest section boundary and append "[truncated]" marker; video script enforces 90s hard cap by dropping lowest-priority segments

## Tool Chain

| Output Format | Primary Tool | Fallback | Config |
|---------------|-------------|----------|--------|
| Clean Markdown | built-in (regex + template) | -- | -- |
| HTML | Pandoc (`pandoc -f markdown -t html5`) | WeasyPrint (for PDF from HTML) | `--standalone --css brand.css` |
| PPTX | Marp CLI (`marp --pptx`) | Canva API (POST /v1/designs) | `--theme brand-theme` |
| Video Script | built-in (temporal mapper) | -- | cs_cf_video constraints |
| Podcast Script | built-in (dialogue mapper) | -- | cs_cf_podcast constraints |
| PDF (from eBook) | Typst (`typst compile`) | Pandoc (`pandoc -t pdf`) | brand template |
| EPUB | Pandoc (`pandoc -t epub3`) | -- | metadata.yaml |

## References

1. `_docs/specs/spec_content_factory_v1.md` -- defines format requirements and tool stack
2. `P03_prompts/constraints/content_factory/` -- per-format constraint specs
3. `P04_tools/functions/content_factory/` -- tool function defs (Canva, Marp, Typst, Pandoc, FFmpeg)
4. `.cex/brand/brand_config.yaml` -- brand variables for template expansion
5. `.claude/rules/ascii-code-rule.md` -- emoji sanitization rules
