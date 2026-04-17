---
id: kc_test_ollama_wrapper
title: Ollama Wrapper Test Guide
description: Comprehensive documentation for testing and validating Ollama wrapper integrations in CEX systems
tags: ["ollama", "wrapper", "testing", "integration", "api"]
kind: knowledge_card
pillar: P01
quality: 8.0
priority: 1
density_score: 1.0
---

# Ollama Wrapper Test Guide

## Overview
The Ollama wrapper test suite provides standardized procedures for validating integrations between CEX systems and Ollama's API. This guide covers testing scenarios, configuration options, and validation criteria for ensuring compatibility with Ollama's inference and model management capabilities. The framework supports model compatibility testing, API endpoint validation, token budget enforcement, response format verification, and error handling simulation.

## Key Features
- **Model Compatibility Testing**: Validate support for Qwen3, Haiku, Codex, and other Ollama models
- **API Endpoint Validation**: Ensure proper handling of `/api/generate`, `/api/tags`, and `/api/models` endpoints
- **Token Budget Enforcement**: Verify token limits and cost calculations
- **Response Format Verification**: Check JSON structure and metadata inclusion
- **Error Handling Simulation**: Test 404, 503, and 400 error scenarios

## Test Scenarios

### 1. Basic Inference Test
```bash
curl http://localhost:11434/api/generate \
  -d '{
    "model": "qwen3",
    "prompt": "What is the capital of France?",
    "stream": false
  }'
```
**Expected Output:**
```json
{
  "response": "The capital of France is Paris.",
  "model": "qwen3",
  "tokens_used": 45,
  "total_cost": 0.002
}
```

### 2. Model Switching Test
| Model       | Expected Response Time | Success Criteria |
|------------|------------------------|------------------|
| qwen3      | <2s                    | Valid JSON       |
| haiku      | <1.5s                  | No format errors |
| codex      | N/A (not supported)   | Error 404        |

### 3. Token Budget Test
```json
{
  "model": "qwen3",
  "prompt": "This is a test prompt with 100 tokens.",
  "max_tokens": 50
}
```
**Validation:** Check response length matches token budget and cost calculation

### 4. Error Handling Test
**404 Model Not Found:**
```bash
curl http://localhost:11434/api/generate \
  -d '{
    "model": "nonexistent-model",
    "prompt": "Test"
  }'
```
**Expected Response:**
```json
{
  "error": "Model not found",
  "code": 404
}
```

**503 Service Unavailable:**
```bash
curl http://localhost:11434/api/generate \
  -d '{
    "model": "qwen3",
    "prompt": "Test"
  }'
```
**Expected Response:**
```json
{
  "error": "Service unavailable",
  "code": 503
}
```

## Configuration Options

### 1. Model Configuration
| Parameter     | Default | Description |
|--------------|---------|------------|
| `model`       | qwen3   | Supported models: qwen3, haiku, codex |
| `temperature` | 0.7     | Creativity control (0-1) |
| `top_p`       | 0.9     | Sampling diversity |
| `max_tokens`  | 2048    | Maximum response length |

### 2. API Settings
| Parameter         | Default | Description |
|------------------|---------|------------|
| `timeout`         | 30s     | Request timeout |
| `max_retries`     | 3       | Retry attempts |
| `stream`          | false   | Enable real-time responses |
| `keep_alive`      | true    | Maintain connection for multiple requests |

## Validation Criteria

### 1. Success Metrics
| Metric            | Threshold | Description |
|------------------|-----------|------------|
| Response Time     | <5s       | For 95% requests |
| Error Rate        | <0.5%     | Across all tests |
| Format Compliance | 100%      | JSON structure |
| Token Accuracy    | 100%      | Matches budget |

### 2. Failure Analysis
| Error Type        | Recovery Action |
|------------------|-----------------|
| 404 Not Found     | Switch model    |
| 503 Service Unavailable | Retry with exponential backoff |
| Invalid JSON      | Validate schema |
| 400 Bad Request   | Check input parameters |

## Best Practices

1. **Model Selection:** Use qwen3 for complex tasks, haiku for speed
2. **Token Management:** Always set `max_tokens` for cost control
3. **Error Handling:** Implement fallback to default model on failure
4. **Performance Monitoring:** Track latency and adjust timeout thresholds
5. **Security:** Use HTTPS for production environments
6. **Logging:** Enable verbose logging for debugging: `--log-level debug`

## Troubleshooting

### Common Issues
| Problem           | Solution |
|------------------|----------|
| Empty response    | Check model availability |
| Invalid JSON      | Validate input schema |
| Connection timeout | Verify Ollama service status |
| Model not found   | Ensure model is installed |

### Debugging Tips
- Use `curl -v` for detailed request/response inspection
- Check system resource limits (CPU, memory)
- Verify Ollama service status: `curl http://localhost:11434/api/tags`
- Enable verbose logging: `--log-level debug`

## Test Automation

### 1. Continuous Integration
```bash
#!/bin/bash
# Run all tests every 15 minutes
while true; do
  ./run_tests.sh
  sleep 900
done
```

### 2. Test Coverage
| Test Type         | Coverage | Status |
|------------------|----------|--------|
| Inference Tests   | 85%      | ✅     |
| Error Handling    | 90%      | ✅     |
| Performance       | 70%      | ⚠️     |
| Model Switching   | 100%     | ✅     |

## Appendix

### 1. Supported Models
```json
{
  "qwen3": {
    "type": "llm",
    "parameters": ["temperature", "top_p", "max_tokens"]
  },
  "haiku": {
    "type": "llm",
    "parameters": ["temperature", "max_tokens"]
  },
  "codex": {
    "type": "llm",
    "parameters": ["temperature", "max_tokens"]
  }
}
```

### 2. Response Format
```json
{
  "response": "Generated text",
  "model": "qwen3",
  "tokens_used": 45,
  "total_cost": 0.002,
  "timestamp": "2023-10-15T14:30:00Z"
}
```

### 3. Error Codes
| Code | Description |
|------|-------------|
| 400  | Bad Request |
| 401  | Unauthorized |
| 404  | Model Not Found |
| 500  | Internal Server Error |
| 503  | Service Unavailable |
```
```