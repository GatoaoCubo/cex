---
id: kc_ollama_deployment_guide
kind: knowledge_card
title: "Ollama Deployment Guide"
version: 1.0.0
quality: null
pillar: P01
---

# Ollama Deployment Guide

## Installation
- **Windows**: `winget install ollama`
- **macOS**: `brew install ollama`
- **Linux**: `sudo apt install ollama`

## Model Management
```bash
ollama pull llama3
ollama create my-model
ollama list
```

## API Endpoints
- `/api/generate` for streaming responses
- `/v1/chat/completions` for chat interface

## Configuration
- `OLLAMA_NUM_PARALLEL=4` (default: 2)
- `OLLAMA_HOST=0.0.0.0` for public access

## GPU Memory Planning
| Model Size | GPU Memory |
|------------|------------|
| 8B         | 5GB        |
| 14B        | 9GB        |
| 32B        | 19GB       |

## Modelfile Customization
```dockerfile
FROM ollama/ollama
COPY modelfile.modelfile /modelfile
```

## Production Tips
1. Use reverse proxies (Nginx, Traefik)
2. Enable GPU acceleration with `OLLAMA_CUDA=1`
3. Monitor resource usage with `ollama stats`
4. Implement rate limiting for public APIs
```