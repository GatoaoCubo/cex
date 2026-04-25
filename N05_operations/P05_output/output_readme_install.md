---
id: n05_readme_install
kind: output_template
8f: F6_produce
pillar: P05
quality: 9.0
title: "Output Readme Install"
version: 1.0.0
author: N05
tags: [output_template, operations, output]
tldr: "Installation guide: Python 3.9+, optional Ollama for local models, 4 presets (Premium/Mid/Local/FT), cex_doctor.py verification."
domain: operations
created: 2026-04-06
updated: 2026-04-07
related:
  - bld_tools_model_provider
  - spec_zero_install
  - p02_fc_cex_model_fallback
  - kc_ollama_deployment_guide
  - kc_cex_distribution_model
  - roadmap_cex
  - bld_sp_tools_software_project
  - claude_vs_free_decision_matrix
  - n05_output_monetization_infra
  - n03_readme_technical
---

# Installation & Requirements

## System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| **Python** | 3.9+ | 3.11+ |
| **RAM** | 8GB | 16GB+ |
| **VRAM** (Ollama) | 4GB | 8GB+ |
| **OS** | Windows 10, macOS 11, Linux | Latest |
| **Git** | 2.30+ | Latest |

## Installation

1. **Clone repository**
   ```bash
   git clone https://github.com/your-org/cex.git
   cd cex
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   # OR if no requirements.txt:
   pip install anthropic google-generativeai openai ollama pyyaml
   ```

3. **Install Ollama** (optional, for local models)
   ```bash
   # Windows: Download from https://ollama.ai
   # macOS: brew install ollama
   # Linux: curl -fsSL https://ollama.ai/install.sh | sh
   ```

4. **Configure CEX**
   ```bash
   python _tools/cex_bootstrap.py --interactive
   ```

5. **Initialize your brand**
   ```bash
   # In CEX session:
   /init
   ```

## Model Presets

| Preset | Description | Services Required | Cost |
|--------|-------------|------------------|------|
| **Premium** | All cloud models | Claude Pro + Gemini Advanced + OpenAI Plus | ~$60/mo |
| **Mid** | Claude only | Claude Pro | ~$20/mo |
| **Local** | Offline models | Ollama (free) | $0 |
| **CEX-FT** | Fine-tuned | Coming soon | Pending finalization |

## Verify Installation

```bash
python _tools/cex_doctor.py
```

Should show: `✅ CEX Health Check: All systems operational`

Ready to build knowledge systems with typed AI agents!

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_model_provider]] | upstream | 0.35 |
| [[spec_zero_install]] | related | 0.35 |
| [[p02_fc_cex_model_fallback]] | upstream | 0.34 |
| [[kc_ollama_deployment_guide]] | upstream | 0.33 |
| [[kc_cex_distribution_model]] | upstream | 0.26 |
| [[roadmap_cex]] | related | 0.25 |
| [[bld_sp_tools_software_project]] | upstream | 0.25 |
| [[claude_vs_free_decision_matrix]] | downstream | 0.25 |
| [[n05_output_monetization_infra]] | related | 0.25 |
| [[n03_readme_technical]] | sibling | 0.23 |
