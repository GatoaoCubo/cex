# Mission: README_PUBLIC — N04 Section
**Output**: `N04_knowledge/output/output_readme_curriculum.md`
**Signal**: `python _tools/signal_writer.py n04 complete 9.0 README_PUBLIC`
**MAX 100 LINES. Commit + signal when done.**

## Task
Write the learning path section for the CEX public README:

1. **"What You'll Learn"** — 3 tracks overview table:
   | Track | Modules | What You Build | Price |
   | Foundations | M01-M03 | Your first knowledge card | Free |
   | Builder | M04-M10 | Full CEX system for your brand | R$497 |
   | Master | M11-M14 | Fine-tuned model + deployment | R$997 |

2. **Module list** — one line per module (M01-M14), just title + output

3. **Prerequisites** — 3 bullet points (Python, Git, CLI)

Frontmatter: id: n04_readme_curriculum, kind: output_template, quality: null

After writing: `git add N04_knowledge/ && git commit -m "[N04] README learning path" --no-verify`
Then: `python _tools/signal_writer.py n04 complete 9.0 README_PUBLIC`
