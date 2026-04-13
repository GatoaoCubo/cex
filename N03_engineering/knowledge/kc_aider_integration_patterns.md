---
id: kc_aider_integration_patterns
kind: knowledge_card
title: "Aider CLI Integration Patterns"
version: 1.0.0
quality: 8.7
pillar: P01
density_score: 1.0
---

# Aider CLI Integration Patterns

## Core Integration Options

**--file**  
Use for single-file editing with context-aware suggestions.  
**--read**  
Read-only mode for analysis without modifications.

**--yes-always**  
Enable full autonomy for repetitive tasks (e.g., refactoring, formatting).

**--subtree-only**  
Focus on specific subdirectories in large repositories.

## Git Integration

**--auto-commits**  
Automatically commit changes with semantic messages.  
**--commit-language**  
Specify commit message language (e.g., `en` for English, `pt` for Portuguese).

## Modelfile Customization

Configure model parameters in `Modelfile` for:
- Language preferences
- Token limits
- Prompt templates
- Safety settings

Use --model flag to override default model settings during execution.
```

## Boundary

Conhecimento destilado, estatico, versionado. NAO eh instrucao, template, ou configuracao.


## 8F Pipeline Function

Primary function: **INJECT**
