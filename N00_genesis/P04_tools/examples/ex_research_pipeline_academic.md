---
id: ex_research_pipeline_academic
kind: cli_tool
pillar: P04
title: "Research Pipeline — Academic Literature Review"
version: 1.0.0
created: 2026-03-31
author: research-pipeline-builder
domain: research_pipeline
quality: 9.1
tags: [research-pipeline, example, academic, papers, literature-review, exa]
tldr: "Config for academic research — Exa neural search, Semantic Scholar, ArXiv, institutional RAG. 5 scholarly perspectives, high CRAG threshold."
density_score: 0.88
updated: "2026-04-07"
---

# Research Pipeline — Academic Literature Review

## About
Config for academic research team conducting systematic literature reviews. Primary sources are academic paper databases (Exa, Semantic Scholar, ArXiv), with internal RAG over institutional publications.

## Config
```yaml
identity:
  empresa: "AI Research Lab"
  nicho: academic_ai
  idioma: en
  pais: US

sources:
  inbound:
    - semantic_scholar  # paper metadata, citation graphs
    - arxiv             # preprints via API
  outbound:
    - youtube           # conference talks (NeurIPS, ICML, ACL)
    - reddit            # r/MachineLearning discussions
    - twitter           # researcher announcements, paper threads
  search:
    - exa               # neural search — best for academic content
    - serper            # Google Scholar via site:scholar.google.com
    - tavily            # research-grade extraction
  trends:
    - pytrends          # research topic interest over time
  rag:
    - institutional_repo  # lab publications, grant proposals
    - zotero_export       # personal reference library

storm_perspectives:
  - role: researcher
    focus: "methodology novelty reproducibility limitations"
  - role: reviewer
    focus: "rigor statistical-validity experimental-design baselines"
  - role: practitioner
    focus: "applicability scalability deployment real-world-impact"
  - role: theoretician
    focus: "formal-proofs convergence complexity-bounds assumptions"
  - role: survey_author
    focus: "taxonomy gaps evolution future-directions"

multi_model:
  extraction: gemini-2.5-flash    # extract paper metadata/abstracts
  reasoning: claude-sonnet         # nuanced academic analysis
  social: gemini-2.5-flash         # conference talk summaries
  critic: o4-mini                  # verify claims against citations

budget:
  exa_monthly: 2000               # heavy neural search usage
  serper_daily: 30                 # Google Scholar supplements
  firecrawl_monthly: 200          # occasional institutional page scrape

output:
  formats: [html, md, json]
  idioma: en
  template: academic              # formal citations, LaTeX-compatible

quality:
  crag_min_score: 0.8             # academic sources must be high quality
  critic_max_iterations: 3        # thorough verification of claims
  final_min_score: 8.5            # higher bar for academic output
```

## Niche Notes
- **Exa dominates**: neural search finds papers by semantic meaning, not just keywords
- **High CRAG threshold (0.8)**: academic integrity demands high-quality sources only
- **Higher final score (8.5)**: academic output must be rigorous and verifiable
- **Citation graph**: Semantic Scholar provides citation chains for influence analysis
- **ArXiv preprints**: latest research appears on ArXiv months before journal publication
- **Conference talks**: YouTube NeurIPS/ICML talks provide author intent missing from papers
- **5 scholarly perspectives**: methodology, rigor, practice, theory, survey — covers all angles
- **Academic template**: formal structure, proper citations, LaTeX-ready format

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `cli tool`
- **Artifact ID**: `ex_research_pipeline_academic`
- **Tags**: [research-pipeline, example, academic, papers, literature-review, exa]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `cli tool` | Artifact type |
| Pipeline | 8F (F1→F8) |
