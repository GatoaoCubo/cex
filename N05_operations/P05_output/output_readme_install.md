---
id: n05_readme_install
kind: output_template
pillar: P05
quality: 9.0
title: "Output Readme Install"
version: 1.0.0
author: N05
tags: [output_template, operations, output]
tldr: "Structured output artifact produced by nucleus pipeline with verified quality metrics"
domain: operations
created: 2026-04-06
updated: 2026-04-07
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