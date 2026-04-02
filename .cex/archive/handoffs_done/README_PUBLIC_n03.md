# Mission: README_PUBLIC — N03 Section
**Output**: `N03_engineering/output/output_readme_technical.md`
**Signal**: `python _tools/signal_writer.py n03 complete 9.0 README_PUBLIC`
**MAX 100 LINES. Commit + signal when done.**

## Task
Write the architecture + quickstart section for the CEX public README:

1. **Architecture diagram** (ASCII art or mermaid):
   - Show 12 pillars, 8 nuclei, 8F pipeline flow
   - Show how builders produce artifacts

2. **Quickstart** (5 steps max):
   ```
   git clone → cex_setup.py → /init → /build → /grid
   ```

3. **Directory structure** (key dirs only, 15 lines max)

Read CLAUDE.md for accurate structure. Keep it dense.

Frontmatter: id: n03_readme_technical, kind: output_template, quality: null

After writing: `git add N03_engineering/ && git commit -m "[N03] README architecture + quickstart" --no-verify`
Then: `python _tools/signal_writer.py n03 complete 9.0 README_PUBLIC`
