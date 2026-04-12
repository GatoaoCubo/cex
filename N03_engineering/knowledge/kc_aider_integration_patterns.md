---
id: kc_aider_integration_patterns
kind: knowledge_card
title: "Aider CLI Integration Patterns"
version: 1.0.0
quality: null
pillar: P01
---

# Aider CLI Integration Patterns

## Core Integration Patterns

### File Mode vs Read Mode
- `--file <file>`: Process single file with full context awareness
- `--read <dir>`: Analyze entire directory structure recursively
- Auto-detects file types (markdown, code, documentation)

### Autonomy Settings
- `--yes-always`: Enable fully autonomous operation
- `--no-prompt`: Disable all user interaction
- `--auto-commits`: Automatic git commit integration
  - Supports `--commit-language` for i18n compatibility

### Repository Handling
- `--subtree-only`: Limit analysis to specific repository subtree
- `--ignore-glob`: Exclude patterns from analysis
- `--follow-symlinks`: Resolve symbolic links during analysis

### Modelfile Customization
- `--modelfile <path>`: Specify custom Modelfile location
- Supports:
  - Model version specification
  - Plugin configuration
  - Context customization
  - Environment variable injection

## Best Practice Recommendations
1. Use `--read` for multi-file repository analysis
2. Combine with `--yes-always` for fully automated workflows
3. Leverage `--commit-language` for multilingual commit messages
4. Use `--subtree-only` to limit scope in large repositories
5. Always validate Modelfile configurations before deployment
```