# Mission: README_PUBLIC — N02 Section
**Output**: `N02_marketing/output/output_readme_hero.md`
**Signal**: `python _tools/signal_writer.py n02 complete 9.0 README_PUBLIC`
**MAX 100 LINES. Commit + signal when done.**

## Task
Write the hero section for the CEX public README.md:

1. **Headline**: One punchy line (technical audience)
2. **Subheadline**: What CEX does in 2 sentences
3. **Badges**: shields.io markdown badges (MIT license, Python 3.10+, Stars, 114 Kinds)
4. **Key metrics**: 114 kinds, 107 builders, 12 pillars, 8 nuclei, 8F pipeline
5. **One-liner install**: `git clone ... && python cex_setup.py && /init`
6. **CTA**: Link placeholders for [Course] and [Documentation]

Frontmatter: id: n02_readme_hero, kind: output_template, quality: null
Tone: technical, confident, zero buzzwords.

After writing: `git add N02_marketing/ && git commit -m "[N02] README hero section" --no-verify`
Then: `python _tools/signal_writer.py n02 complete 9.0 README_PUBLIC`
