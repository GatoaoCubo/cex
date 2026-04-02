# Mission: README_PUBLIC — N05 Section
**Output**: `N05_operations/output/output_readme_install.md`
**Signal**: `python _tools/signal_writer.py n05 complete 9.0 README_PUBLIC`
**MAX 100 LINES. Commit + signal when done.**

## Task
Write the installation + requirements section for the CEX public README:

1. **System requirements** table:
   | Requirement | Minimum | Recommended |
   (Python, RAM, VRAM for Ollama, OS, Git)

2. **Installation** (numbered steps, copy-pasteable commands):
   - Clone repo
   - Install Python deps
   - Install Ollama (optional)
   - Run cex_setup.py
   - Run /init

3. **Model presets** — table showing 4 presets from nucleus_models.yaml:
   Premium (3 subs), Mid (Claude only), Local (Ollama), CEX-FT (future)

4. **Verify installation**: `python _tools/cex_doctor.py`

Frontmatter: id: n05_readme_install, kind: output_template, quality: null

After writing: `git add N05_operations/ && git commit -m "[N05] README installation guide" --no-verify`
Then: `python _tools/signal_writer.py n05 complete 9.0 README_PUBLIC`
