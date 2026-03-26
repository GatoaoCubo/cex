---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of iso_package in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: iso_package in the CEX

## Boundary
iso_package EH: pacote portable self-contained de agente AI em formato ISO — manifest.yaml
como entry point, tiered file system (3/7/10/12 files), LP-mapped, LLM-agnostic,
density >= 0.80, system_instruction capped at 4096 tokens.

iso_package NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| agent | agent define QUEM o agente EH no repo; iso_package EMPACOTA para distribuir | P02 agent |
| boot_config | boot_config define como INICIALIZAR por provider; iso_package empacota TUDO | P02 boot_config |
| mental_model (P02) | mental_model define routing/decisoes; iso_package nao decide, empacota | P02 mental_model |
| model_card | model_card spec do LLM subjacente; iso_package empacota o agente que USA o LLM | P02 model_card |
| router | router define regras de roteamento; iso_package nao roteia | P02 router |
| fallback_chain | fallback_chain define sequencia de modelos; iso_package nao gerencia fallback | P02 fallback_chain |
| lens | lens eh perspectiva especializada; iso_package eh bundle completo | P02 lens |
| axiom | axiom eh principio imutavel; iso_package eh artefato distribuivel | P02 axiom |
| spawn_config | spawn_config define parametros de spawn runtime; iso_package eh pre-runtime | P12 spawn_config |
| upload_kit (file) | upload_kit eh UM arquivo dentro do iso_package; nao eh o package inteiro | P04 upload_kit |

Regra: "como empacoto este agente para distribuir, deployar, ou compartilhar?" -> iso_package.

## Position in Agent Distribution Flow

```text
agent (P02) --> iso_package (P02) --> upload_kit (P04) --> deployment
     |                  |                     |
canonical def    portable bundle      deploy instructions
                       |
     system_instruction.md (P03) + instructions.md (P03) + ...
```

iso_package is DISTRIBUTION LAYER — bridges canonical agent definitions
with deployment and sharing across runtimes and platforms.

## Dependency Graph

```text
iso_package <--receives-- agent (P02) (canonical source definition)
iso_package <--receives-- system_prompt (P03) (becomes system_instruction.md)
iso_package <--receives-- knowledge_card (P01) (domain knowledge for quick_start)
iso_package --produces_for--> upload_kit (P04) (deployment target)
iso_package --produces_for--> spawn_config (P12) (runtime instantiation)
iso_package --consumed_by--> workflow (P12) (orchestration node)
iso_package --independent-- model_card, boot_config, router, fallback_chain
```

## Fractal Position
Pillar: P02 (Model — QUEM o agente EH)
Function: BECOME (package carries agent identity for instantiation)
Layer: spec (static distributable artifact, not runtime)
Scale: L0 (core infrastructure — every sharable agent needs packaging)
Unique: only P02 kind that is a multi-file artifact with tiered completeness.
