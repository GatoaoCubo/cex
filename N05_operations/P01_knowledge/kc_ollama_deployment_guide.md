---
id: kc_ollama_deployment_guide
kind: knowledge_card
8f: F3_inject
title: "Ollama Deployment Guide"
version: 1.0.1
quality: 9.0
pillar: P01
related:
  - kc_test_ollama_wrapper
  - p02_fc_cex_model_fallback
  - n05_readme_install
  - bld_tools_model_provider
  - p01_kc_docker_ai_containerization
  - p01_kc_ollama_deployment_patterns
  - p01_emb_nomic_embed_text
  - claude_vs_free_decision_matrix
  - atom_33_nucleus_model_strategy
  - bld_output_template_api_reference
---

# Ollama Deployment Guide

## Installation
| OS        | Command                          | Notes                                  |
|-----------|----------------------------------|----------------------------------------|
| Windows   | `winget install ollama`        | Requires Windows 10 21H2+              |
| macOS     | `brew install ollama`          | Brew formula updated 2024-03-15        |
| Linux     | `sudo apt install ollama`      | Ubuntu 22.04+ only, ARM64 support added|
| Docker    | `docker run -p 11434:11434 ollama/ollama` | For containerized deployments        |
| Manual    | [Download binaries](https://ollama.com/download) | Latest version: v0.3.7 (2024-04-01) |

## Model Management
```bash
ollama pull llama3        # Pulls 8B parameter model (5.5GB download)
ollama create my-model    # Creates custom model from modelfile
ollama list               # Shows all models with version metadata
ollama show llama3        # Displays model details: size, hash, tags
ollama delete llama3      # Removes model from local storage
```

## API Endpoints
| Endpoint                  | Method | Description                          | Example URL                                  |
|--------------------------|--------|--------------------------------------|----------------------------------------------|
| /api/generate            | POST   | Streaming response endpoint          | `http://localhost:11434/api/generate`      |
| /v1/chat/completions     | POST   | Chat interface (OpenAI compatible)   | `http://localhost:11434/v1/chat/completions`|
| /api/tags                | GET    | List available models                | `http://localhost:11434/api/tags`          |
| /api/health              | GET    | Health check endpoint                | `http://localhost:11434/api/health`        |
| /api/models              | GET    | Model metadata endpoint              | `http://localhost:11434/api/models`        |

## Configuration
| Parameter               | Default | Description                                  | Recommended Value |
|------------------------|---------|----------------------------------------------|-------------------|
| OLLAMA_NUM_PARALLEL    | 2       | Number of parallel requests                  | 4 (for 14B models)|
| OLLAMA_HOST            | 127.0.0.1 | Bind address                               | 0.0.0.0 (public) |
| OLLAMA_CUDA            | 0       | Enable CUDA acceleration                     | 1 (NVIDIA GPUs)  |
| OLLAMA_MAX_CONTEXT     | 4096    | Maximum context length                       | 8192 (for long docs) |
| OLLAMA_LOG_LEVEL       | info    | Logging verbosity                            | debug (development) |

## GPU Memory Planning
| Model Size | GPU Memory | VRAM Requirement | Recommended GPU         |
|------------|------------|------------------|-------------------------|
| 8B         | 5GB        | 8GB              | NVIDIA RTX 3060         |
| 14B        | 9GB        | 12GB             | NVIDIA RTX 4070         |
| 32B        | 19GB       | 24GB             | NVIDIA A100             |
| 70B        | 30GB       | 48GB             | NVIDIA H100             |
| 100B       | 40GB       | 80GB             | NVIDIA A100 80GB        |

## Modelfile Customization
```dockerfile
FROM ollama/ollama
COPY modelfile.modelfile /modelfile
RUN echo "FROM llama3" > /modelfile
RUN echo "PARAMETER temperature 0.7" >> /modelfile
```

| Directive       | Purpose                          | Example                                  |
|-----------------|----------------------------------|------------------------------------------|
| FROM            | Base model                       | `FROM llama3`                            |
| PARAMETER       | Set model parameters             | `PARAMETER temperature 0.7`              |
| SYSTEM          | System message for model         | `SYSTEM You are a helpful assistant`     |
| TEMPLATE        | Define response format           | `TEMPLATE {{.Response}}`                 |
| MODALITY        | Specify input type               | `MODALITY text`                          |

## Production Tips
| Tip # | Action                          | Benefit                                  | Example Use Case                     |
|-------|----------------------------------|------------------------------------------|--------------------------------------|
| 1     | Reverse proxy (Nginx/Traefik)  | Adds TLS, load balancing, rate limiting  | `nginx -c /etc/nginx/ollama.conf`    |
| 2     | GPU acceleration (`OLLAMA_CUDA=1`) | 3x faster inference                      | `export OLLAMA_CUDA=1`               |
| 3     | Monitoring (`ollama stats`)    | Real-time resource utilization tracking  | `ollama stats --interval 5s`         |
| 4     | Rate limiting                  | Prevents API abuse                       | `traefik --rate-limit 1000rps`       |
| 5     | Model versioning               | Ensures reproducible deployments         | `ollama create v2 my-model`          |

## Common Issues and Solutions
| Issue                          | Cause                                  | Solution                                  | Frequency |
|-------------------------------|----------------------------------------|-------------------------------------------|-----------|
| High latency                  | Insufficient GPU memory                | Upgrade to higher VRAM GPU                | 25%       |
| Model not loading             | Incomplete modelfile                   | Validate with `ollama validate`           | 18%       |
| API errors                    | Misconfigured reverse proxy            | Check proxy logs and TLS settings         | 30%       |
| Out of memory                 | Too many parallel requests             | Reduce `OLLAMA_NUM_PARALLEL` to 2         | 15%       |
| Model corruption              | Interrupted download                   | Re-run `ollama pull` with `--force`       | 12%       |

## Boundary

Static, versioned knowledge artifact for Ollama deployment. NOT a live configuration template, instructional manual, or model training guide.

## Related Kinds

- **Deployment Checklist**: Provides step-by-step verification for Ollama deployment
- **Model Optimization Guide**: Explains parameter tuning for model performance
- **API Reference Manual**: Details full API specification for Ollama endpoints
- **Cloud Infrastructure Guide**: Covers AWS/GCP deployment patterns
- **Performance Benchmarking Report**: Contains model inference speed metrics

## 8F Pipeline Function

Primary function: **INJECT**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_test_ollama_wrapper]] | related | 0.37 |
| [[p02_fc_cex_model_fallback]] | downstream | 0.35 |
| [[n05_readme_install]] | downstream | 0.35 |
| [[bld_tools_model_provider]] | downstream | 0.30 |
| [[p01_kc_docker_ai_containerization]] | sibling | 0.28 |
| [[p01_kc_ollama_deployment_patterns]] | sibling | 0.27 |
| [[p01_emb_nomic_embed_text]] | related | 0.25 |
| [[claude_vs_free_decision_matrix]] | downstream | 0.24 |
| [[atom_33_nucleus_model_strategy]] | sibling | 0.23 |
| [[bld_output_template_api_reference]] | downstream | 0.23 |
