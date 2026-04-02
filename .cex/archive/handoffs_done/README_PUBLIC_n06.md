# Mission: README_PUBLIC — N06 Section
**Output**: `N06_commercial/output/output_readme_pricing.md`
**Signal**: `python _tools/signal_writer.py n06 complete 9.0 README_PUBLIC`
**MAX 100 LINES. Commit + signal when done.**

## Task
Write the pricing + course CTA section for the CEX public README:

1. **Pricing table** (markdown, 3 tiers):
   | | Explorer | Builder | Master |
   | Price | Free | R$497 | R$997 |
   | Modules | M01-M03 | M04-M10 | M11-M14 |
   | cex-brain model | No | Yes | Yes |
   | Community | No | Discord | Discord + calls |
   | Support | GitHub Issues | Email | Priority |

2. **Why pay?** — 3 bullet points (speed, quality, model)
   - Free repo works with generic Ollama (quality ~7.0)
   - Paid course includes cex-brain:14b (quality ~9.0)
   - ROI: 1 client project pays for the course

3. **CTA**: "Get Started" button/link placeholder

4. **Guarantee**: 30 days money back

Frontmatter: id: n06_readme_pricing, kind: output_template, quality: null
Tone: honest, no hype, dev-friendly.

After writing: `git add N06_commercial/ && git commit -m "[N06] README pricing section" --no-verify`
Then: `python _tools/signal_writer.py n06 complete 9.0 README_PUBLIC`
