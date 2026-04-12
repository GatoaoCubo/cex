---
id: kc_env_config
kind: knowledge_card
title: "Environment Configuration for LLM Systems"
version: 1.0.0
quality: null
pillar: P01
language: English
---

# Environment Configuration for LLM Systems

## Key Configuration Elements

1. **API Keys**  
   - Store sensitive credentials in environment variables
   - Use `.env` files with `.gitignore` protection
   - Never hardcode keys in source code

2. **Provider URLs**  
   - Configure endpoints for different LLM providers:
     ```env
     OPENAI_API_URL=https://api.openai.com/v1
     ANTHROPIC_API_URL=https://api.anthropic.com/v1
     ```

3. **Model Selection**  
   - Set default models via environment variables:
     ```env
     DEFAULT_MODEL=gpt-4
     CODEx_MODEL=code-davinci-002
     ```

4. **Feature Flags**  
   - Enable/disable features with flags:
     ```env
     ENABLE_STREAMING=true
     USE_CACHING=false
     ```

5. **Secrets Management**  
   - Use encrypted secret managers for production
   - Implement rotation policies for credentials
   - Validate secrets during deployment

6. **.env Patterns**  
   - Use consistent naming conventions
   - Separate development/production environments
   - Implement validation for required variables

## Best Practices
- Use `.env.local` for local development
- Store production secrets in secure vaults
- Automate environment setup with CI/CD
- Regularly audit configuration files
