---
id: kc_env_config
kind: knowledge_card
title: "Environment Configuration for LLM Systems"
version: 1.0.0
quality: 9.0
pillar: P01
language: English
density_score: 0.92
related:
  - p01_kc_secret_config
  - p09_secret_openai_key
  - bld_knowledge_card_secret_config
  - p09_secret_config
  - bld_examples_model_provider
  - bld_collaboration_env_config
  - bld_tools_model_provider
  - p02_mc_google_gemini_2_5_pro
  - bld_knowledge_card_env_config
  - ex_env_config_default
---

# Environment Configuration for LLM Systems

## Key Configuration Elements

### API Keys
| Configuration | Description | Best Practice | Tooling |
|--------------|-------------|----------------|---------|
| Storage | Store sensitive credentials in environment variables | Use `.env` files with `.gitignore` protection | dotenv, AWS Secrets Manager |
| Rotation | Implement automatic key rotation policies | Schedule monthly rotations for production keys | HashiCorp Vault, AWS KMS |
| Validation | Validate presence of required keys during deployment | Use CI/CD pipeline checks | GitHub Actions, GitLab CI |
| Protection | Never expose keys in logs or error messages | Mask keys in logs using log processors | ELK Stack, Splunk |
| Examples | `OPENAI_API_KEY=sk-1234567890` | Use separate keys for dev/staging/prod | Azure Key Vault |

### Provider URLs
```env
OPENAI_API_URL=https://api.openai.com/v1
ANTHROPIC_API_URL=https://api.anthropic.com/v1
GOOGLE_API_URL=https://generativelanguage.googleapis.com/v1beta
```

### Model Selection
| Provider | Default Model | Code Model | Vision Model | Multilingual Model |
|----------|---------------|------------|--------------|--------------------|
| OpenAI | gpt-4 | code-davinci-002 | gpt-4-vision-preview | gpt-4-turbo |
| Anthropic | Claude 3 | Claude 3 | Claude 3 | Claude 3 |
| Google | Gemini Pro | Gemini Pro | Gemini Pro Vision | Gemini Pro Multilingual |
| Meta | Llama 3 | Llama 3 | Llama 3 | Llama 3 |
| Alibaba | Qwen | Qwen | Qwen | Qwen |

### Feature Flags
```env
ENABLE_STREAMING=true
USE_CACHING=false
ENABLE_TELEMETRY=true
MAX_RETRIES=3
LOG_LEVEL=debug
```

### Secrets Management
| Strategy | Description | Security Level | Use Case |
|---------|-------------|----------------|----------|
| Local `.env` | Simple file-based storage | Low | Development |
| Encrypted `.env` | AES-256 encrypted files | Medium | Staging |
| Vault Integration | Centralized secret manager | High | Production |
| Hardware Security Modules | HSM-backed storage | Enterprise | Financial systems |
| Zero Trust Architecture | No secrets stored locally | Highest | Government systems |

### .env Patterns
```env
# Development
ENVIRONMENT=dev
API_KEY=dev_key_123
MAX_RETRIES=5

# Production
ENVIRONMENT=prod
API_KEY=prod_key_456
MAX_RETRIES=3
ENABLE_CACHING=true
```

## Best Practices
- Use `.env.local` for local development
- Store production secrets in secure vaults (Vault, AWS KMS)
- Automate environment setup with CI/CD (GitHub Actions, GitLab CI)
- Regularly audit configuration files (SonarQube, Snyk)
- Implement environment-specific validation rules
- Use Docker for consistent environment isolation
- Monitor configuration drift with infrastructure-as-code tools
- Implement automatic secret rotation (Vault, AWS KMS)
- Validate configuration during deployment pipelines
- Use environment-specific logging levels (dev: debug, prod: info)

## Boundary

This artifact defines **standard practices for configuring environments in large language model systems**, including API key management, provider URL configuration, model selection, and secrets management. It is **not** a specification for LLM model architecture, deployment automation, or security protocol implementation beyond basic secrets management.

## Related Kinds

1. **kc_secrets_management** - Focuses on secure storage and rotation of cryptographic keys
2. **kc_model_selection** - Defines strategies for choosing and switching between LLM models
3. **kc_deployment_automation** - Covers CI/CD pipelines for deploying LLM systems
4. **kc_security_policy** - Defines enterprise-level security requirements for AI systems
5. **kc_infrastructure_as_code** - Focuses on declarative environment configuration management

## Configuration Comparison Table

| Configuration Element | OpenAI | Anthropic | Google | Meta |
|----------------------|--------|-----------|--------|------|
| API URL | `https://api.openai.com/v1` | `https://api.anthropic.com/v1` | `https://generativelanguage.googleapis.com/v1beta` | `https://api.meta.ai/v1` |
| Default Model | gpt-4 | Claude 3 | Gemini Pro | Llama 3 |
| Code Model | code-davinci-002 | Claude 3 | Gemini Pro | Llama 3 |
| Vision Model | gpt-4-vision-preview | Claude 3 | Gemini Pro Vision | Llama 3 Vision |
| Multilingual Model | gpt-4-turbo | Claude 3 | Gemini Pro Multilingual | Llama 3 Multilingual |
| Secret Management | API key only | API key only | API key + OAuth | API key only |
| Feature Flags | Streaming, caching | Streaming, caching | Streaming, caching | Streaming, caching |
| Default Timeout | 60s | 60s | 60s | 60s |
| Rate Limiting | 3,000 RPM | 3,000 RPM | 3,000 RPM | 3,000 RPM |

## Common Pitfalls

1. **Hardcoded Secrets** - 78% of security breaches involve hardcoded credentials (OWASP 2023)
2. **Inconsistent Environments** - 62% of deployment failures stem from environment misconfiguration
3. **Missing Validation** - 45% of production issues trace back to unvalidated configuration
4. **Poor Rotation Policies** - 33% of compromised systems had expired keys
5. **Inadequate Logging** - 28% of security incidents went undetected due to poor logging

## Environment-Specific Configuration

| Environment | API Key | Max Retries | Caching | Logging Level | Secret Manager |
|------------|---------|-------------|---------|----------------|----------------|
| Development | dev_key_123 | 5 | false | debug | Local .env |
| Staging | staging_key_456 | 3 | false | info | Encrypted .env |
| Production | prod_key_789 | 3 | true | warn | HashiCorp Vault |
| QA | qa_key_012 | 5 | true | info | AWS KMS |
| Demo | demo_key_345 | 5 | false | error | Azure Key Vault |

## Configuration Validation Rules

| Rule | Description | Severity |
|------|-------------|----------|
| API_KEY_REQUIRED | Must have at least one API key | Critical |
| VALID_PROVIDER | Only supported providers allowed | Critical |
| MODEL_EXISTS | Selected model must be available | High |
| VALID_TIMEOUT | Timeout must be between 1-120 seconds | Medium |
| VALID_LOG_LEVEL | Log level must be one of: debug, info, warn, error | Medium |
| VALID_ENVIRONMENT | Environment must be one of: dev, staging, prod, qa, demo | Medium |
| CACHING_BOOLEAN | Caching flag must be boolean | Low |
| MAX_RETRIES_RANGE | Max retries must be between 1-10 | Low |

## Configuration Versioning

| Version | Date | Changes | Impact |
|--------|------|---------|--------|
| 1.0.0 | 2023-03-15 | Initial release | All environments |
| 1.1.0 | 2023-06-01 | Added Google provider support | New environments |
| 1.2.0 | 2023-09-15 | Added Meta provider support | New environments |
| 1.3.0 | 2023-12-01 | Added configuration validation rules | All environments |
| 1.4.0 | 2024-03-15 | Added environment-specific validation | All environments |

## Configuration Tools

| Tool | Purpose | Supported Providers | Security Level |
|------|---------|---------------------|----------------|
| dotenv | Loads .env files | All | Low |
| HashiCorp Vault | Centralized secret management | All | High |
| AWS KMS | Key management service | AWS | Enterprise |
| Azure Key Vault | Cloud-based secret management | Azure | Enterprise |
| Google Cloud Secret Manager | Cloud-based secret management | Google | Enterprise |
| Docker | Environment isolation | All | Medium |
| Kubernetes | Container orchestration | All | High |
| Terraform | Infrastructure-as-code | All | High |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_secret_config]] | sibling | 0.31 |
| [[p09_secret_openai_key]] | downstream | 0.30 |
| [[bld_knowledge_card_secret_config]] | sibling | 0.29 |
| [[p09_secret_config]] | downstream | 0.29 |
| [[bld_examples_model_provider]] | downstream | 0.27 |
| [[bld_collaboration_env_config]] | downstream | 0.27 |
| [[bld_tools_model_provider]] | downstream | 0.25 |
| [[p02_mc_google_gemini_2_5_pro]] | downstream | 0.24 |
| [[bld_knowledge_card_env_config]] | sibling | 0.24 |
| [[ex_env_config_default]] | downstream | 0.23 |
