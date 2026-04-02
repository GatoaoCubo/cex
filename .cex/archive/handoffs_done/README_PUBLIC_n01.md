# Mission: README_PUBLIC — N01 Section
**Output**: `N01_intelligence/output/output_readme_comparison.md`
**Signal**: `python _tools/signal_writer.py n01 complete 9.0 README_PUBLIC`
**MAX 100 LINES. Commit + signal when done.**

## Task
Write a competitive comparison table for the CEX public README. Compare CEX vs:
- LangChain
- CrewAI
- AutoGen
- Semantic Kernel

Columns: Feature | CEX | LangChain | CrewAI | AutoGen | Semantic Kernel
Rows: Typed Knowledge, Multi-Agent, Quality Pipeline, Fine-Tune Ready, Offline/Local, Brand Injection, 100+ Builders

Frontmatter: id: n01_readme_comparison, kind: output_template, quality: null

After writing: `git add N01_intelligence/ && git commit -m "[N01] README comparison table" --no-verify`
Then: `python _tools/signal_writer.py n01 complete 9.0 README_PUBLIC`
