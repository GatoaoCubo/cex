---
id: bld_tools_tagline
kind: tools
pillar: P04
builder: tagline-builder
version: 1.0.0
---
# Tools: Tagline Builder

## Required Tools
- `brand_config_reader`: Read .cex/brand/brand_config.yaml for brand context
- `cex_query.py`: Find competitor builders and existing brand artifacts
- `cex_retriever.py`: Search existing taglines in the knowledge base

## Optional Tools
- `browser_web_scraping`: Scrape competitor websites for their taglines
- `cex_memory_select.py`: Recall previous tagline decisions and preferences

## No External Dependencies
Tagline creation is pure LLM reasoning — no APIs, no code execution.
All tools are for context gathering, not generation.
