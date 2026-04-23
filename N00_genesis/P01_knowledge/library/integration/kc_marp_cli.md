---
id: p01_kc_marp_cli
kind: knowledge_card
type: domain
pillar: P01
title: "Marp CLI — Markdown to Slides for Content Factory"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: n04_knowledge
domain: marp
quality: 9.1
tags: [marp, slides, markdown, presentation, html, pdf, pptx, content-factory, integration, INJECT]
tldr: "Markdown → HTML/PDF/PPTX slides via CLI — theme directives, speaker notes, images, and batch export"
when_to_use: "When any nucleus needs to generate slide decks from structured markdown content"
keywords: [marp, markdown-slides, presentation, cli, theme, speaker-notes]
feeds_kinds: [cli_tool, workflow, dag, formatter]
linked_artifacts: [kc_canva_connect_api, kc_typst_patterns, kc_pandoc_pipeline]
density_score: null
related:
  - p04_fn_cf_slides_generate
  - p01_kc_slide_generation
  - p05_fmt_content_adapter
  - p05_output_social_card
  - kc_webinar_script
  - n02_kc_email_html_responsive
  - p01_kc_email_html_responsive
  - p05_output_email_template
  - bld_output_template_pitch_deck
  - p01_kc_brand_propagation_arch
---

# Marp CLI

## Quick Reference
```yaml
install: npm install -g @marp-team/marp-cli
binary: marp
version_check: marp --version
slide_separator: "---"   # three dashes on own line
output_formats: [html, pdf, pptx, png, jpeg]
engine: marpit (Markdown-it based)
config_file: .marprc.yml  # optional project config
```

## Slide Syntax Basics

```markdown
---
marp: true
theme: default
paginate: true
header: "Content Factory — Week 14"
footer: "© 2026 Brand Name"
style: |
  section { font-family: 'Inter', sans-serif; }
  h1 { color: #2563eb; }
---

# Slide 1: Title Slide

Subtitle or tagline here

---

# Slide 2: Content

- Bullet point one
- Bullet point two
- **Bold** emphasis for key metrics

![bg right:40%](./images/chart.png)

<!-- speaker notes go here — not rendered on slides -->
This is my speaker note for slide 2.

---

<!-- _class: lead -->
# Slide 3: Section Break

Big centered heading with `lead` class

---

# Slide 4: Two Columns

<div class="columns">
<div>

**Left column**
- Point A
- Point B

</div>
<div>

**Right column**
- Point C
- Point D

</div>
</div>
```

## Directives (per-slide or global)

| Directive | Scope | Example | Effect |
|-----------|-------|---------|--------|
| `marp: true` | Global | Front matter | Enables Marp processing |
| `theme` | Global | `theme: gaia` | Built-in: default, gaia, uncover |
| `paginate` | Both | `paginate: true` | Show page numbers |
| `header` / `footer` | Both | `header: "Title"` | Persistent header/footer text |
| `_class` | Slide | `<!-- _class: lead -->` | Apply CSS class to current slide |
| `_backgroundColor` | Slide | `<!-- _backgroundColor: #1a1a2e -->` | Slide background color |
| `_color` | Slide | `<!-- _color: white -->` | Text color override |
| `size` | Global | `size: 16:9` | Aspect ratio (default 16:9, also 4:3) |
| `style` | Global | `style: |` in front matter | Custom CSS block |

## Image Syntax

```markdown
# Background images
![bg](image.jpg)                    # Full background
![bg contain](image.jpg)            # Fit without crop
![bg right:40%](image.jpg)          # Split: image on right 40%
![bg left:50%](image.jpg)           # Split: image on left 50%
![bg blur:5px](image.jpg)           # Blurred background
![bg brightness:0.5](image.jpg)     # Darkened background

# Multiple backgrounds (side by side)
![bg](img1.jpg)
![bg](img2.jpg)

# Inline image with sizing
![w:300](image.png)                  # Width 300px
![h:200](image.png)                  # Height 200px
![w:300 h:200](image.png)           # Both
```

## Export Commands

```bash
# Markdown → HTML (single file, self-contained)
marp slides.md -o slides.html

# Markdown → PDF
marp slides.md -o slides.pdf

# Markdown → PowerPoint
marp slides.md -o slides.pptx

# Markdown → PNG (one image per slide)
marp slides.md --images png -o ./output/

# Markdown → JPEG
marp slides.md --images jpeg --jpeg-quality 85 -o ./output/

# Watch mode (auto-rebuild on save)
marp -w slides.md -o slides.html

# Server mode (live preview in browser)
marp -s ./slides/

# Batch: all .md files in directory
marp ./slides/ -o ./output/

# Custom theme file
marp slides.md --theme ./brand-theme.css -o slides.pdf
```

## Custom Theme Example

```css
/* brand-theme.css */
@import 'default';

section {
  font-family: 'Inter', 'Segoe UI', sans-serif;
  background: #ffffff;
  color: #1a1a2e;
}

section.lead {
  background: linear-gradient(135deg, #2563eb 0%, #7c3aed 100%);
  color: white;
  text-align: center;
}

section.lead h1 {
  font-size: 2.5em;
}

h1 { color: #2563eb; border-bottom: 3px solid #2563eb; padding-bottom: 0.3em; }
h2 { color: #7c3aed; }

footer { font-size: 0.6em; color: #94a3b8; }

/* Two-column layout */
.columns { display: grid; grid-template-columns: 1fr 1fr; gap: 1em; }
```

## .marprc.yml (Project Config)

```yaml
allowLocalFiles: true
theme: ./brand-theme.css
html: true
output: ./output/
pdf: true
```

## Gotchas

- **`marp: true` in frontmatter is REQUIRED.** Without it, Marp treats the file as plain markdown and outputs nothing useful.
- **`---` is a slide separator AND YAML frontmatter delimiter.** The first `---` pair is frontmatter; every subsequent `---` is a new slide.
- **HTML is disabled by default.** Add `html: true` to frontmatter or `--html` flag for `<div>` tags to work (needed for columns).
- **PDF export requires Chrome/Chromium.** Marp uses Puppeteer internally. First run downloads Chromium (~200MB).
- **PPTX is not fully editable.** Text becomes text boxes, but complex layouts may render as images. Use for viewing, not heavy editing.
- **Local images in PDF/PPTX need `--allow-local-files` flag** or `allowLocalFiles: true` in config. Without it, images show as broken.
- **Speaker notes (`<!-- comment -->`) only visible in HTML output** with presenter view (`?sync=` URL param). Not exported to PDF.
- **Max recommended slides: ~50.** PDF export with 100+ slides can OOM on Puppeteer. Split large decks.

## Docs
- CLI docs: https://github.com/marp-team/marp-cli
- Marpit framework: https://marpit.marp.app/
- Theme CSS reference: https://marpit.marp.app/theme-css

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_fn_cf_slides_generate]] | downstream | 0.52 |
| [[p01_kc_slide_generation]] | sibling | 0.30 |
| [[p05_fmt_content_adapter]] | downstream | 0.28 |
| [[p05_output_social_card]] | downstream | 0.25 |
| [[kc_webinar_script]] | sibling | 0.24 |
| [[n02_kc_email_html_responsive]] | sibling | 0.23 |
| [[p01_kc_email_html_responsive]] | sibling | 0.22 |
| [[p05_output_email_template]] | downstream | 0.22 |
| [[bld_output_template_pitch_deck]] | downstream | 0.21 |
| [[p01_kc_brand_propagation_arch]] | sibling | 0.20 |
