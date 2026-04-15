# N01 Intelligence Report

## Overview
This report provides an overview of the N01 intelligence process, focusing on leveraging web research and citation sources.

## Key Tools
- **cex_web_fetch.py**: A Python script for fetching URL content, including support for arXiv IDs.
- **cex_source_harvester.py**: A tool for scanning CEX repo files for external source references (URLs, arXiv IDs, RFCs).
- **cex_taxonomy_scout.py**: A script for scanning configured sources and extracting candidate dictionaries.

## Example Usage
### Fetching an arXiv Paper
```bash
python _tools/cex_web_fetch.py --arxiv 1706.03762
```

### Scanning CEX Repo Files
```bash
python _tools/cex_source_harvester.py
```

## References
- Smith et al. (2022). Multilingual News Corpus. arXiv:2205.01234