---
id: p01_kc_plugin_marketplace
kind: knowledge_card
pillar: P01
title: "Claude Plugin Marketplace — .claude-plugin/ Distribution Structure"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: plugin_distribution
quality: 9.1
tags: [claude-plugin, marketplace, distribution, plugin-json, skill-packaging]
tldr: ".claude-plugin/ com marketplace.json (registry) e plugin.json (manifest) define distribuicao de skills via Claude Code Marketplace"
when_to_use: "Empacotar skills para distribuicao publica ou instalar plugins de terceiros via Claude Code"
keywords: [claude-plugin, marketplace-json, plugin-json, skill-distribution]
long_tails:
  - "Como publicar skills no Claude Code Marketplace"
  - "Qual a estrutura de diretorio para distribuir plugins Claude"
axioms:
  - "SEMPRE sincronizar version entre marketplace.json e plugin.json"
  - "NUNCA omitir keywords no plugin.json (prejudica discoverability)"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_function_become]
density_score: null
data_source: "https://github.com/kepano/obsidian-skills"
related:
  - bld_collaboration_plugin
  - bld_architecture_plugin
  - plugin-builder
  - bld_tools_plugin
  - bld_memory_plugin
  - p01_kc_plugin
  - p11_qg_plugin
  - bld_config_plugin
  - bld_schema_plugin
  - bld_collaboration_marketplace_app_manifest
---

## Summary

O diretorio `.claude-plugin/` na raiz de um repositorio define metadados para distribuicao de skills via Claude Code Marketplace.
Dois arquivos JSON complementares: `marketplace.json` (registry entry para discovery) e `plugin.json` (manifest para instalacao).
Um unico repo pode conter multiplos plugins via array `plugins[]`.
Instalacao: `/plugin marketplace add {owner}/{repo}` seguido de `/plugin install {name}@{repo}`.

## Spec

| Arquivo | Campo | Tipo | Descricao |
|---------|-------|------|-----------|
| marketplace.json | name | string | Slug do repo, kebab-case |
| marketplace.json | owner.name | string | Nome do autor |
| marketplace.json | owner.url | string | URL do autor (opcional) |
| marketplace.json | plugins[] | array | Plugins neste repo |
| marketplace.json | plugins[].name | string | Ref para install |
| marketplace.json | plugins[].source | string | Path no repo ("./" = raiz) |
| marketplace.json | plugins[].version | semver | Sync com plugin.json |
| plugin.json | name | string | Bater com plugins[].name |
| plugin.json | description | string | Aparece em `/plugin info` |
| plugin.json | keywords | string[] | Busca no marketplace |
| plugin.json | repository | url | URL GitHub do repo |
| plugin.json | license | string | SPDX identifier (ex: MIT) |

Versionamento semver sincronizado: patch (1.0.1→1.0.2) para correcoes de skills, minor (1.0→1.1) para skills novas, major (1.x→2.0) para breaking changes na estrutura. Ambos arquivos devem ter a mesma versao.

## Patterns

| Trigger | Action |
|---------|--------|
| Distribuir skills externamente | Criar .claude-plugin/ com ambos JSONs |
| Repo com multiplos skill sets | Um entry por set no array plugins[] |
| Atualizar versao do plugin | Incrementar em AMBOS arquivos simultaneamente |
| Maximizar discoverability | Keywords descritivas e especificas no plugin.json |
| Consumir plugin de terceiro | `/plugin marketplace add` + `/plugin install` |
| Skills internas migrando para publico | Adicionar .claude-plugin/ sem mudar estrutura |

## Code

<!-- lang: json | purpose: complete .claude-plugin/ structure -->
```bash
# Estrutura completa de um plugin distribuivel
repo-root/
  .claude-plugin/
    marketplace.json      # Registry entry (discovery)
    plugin.json           # Plugin manifest (install metadata)
  skills/
    my-skill/
      SKILL.md            # Skill definition (frontmatter obrigatorio)
      references/
        *.md
  README.md
  LICENSE
```

```json
{
  "name": "my-skills",
  "owner": {"name": "Author", "url": "https://example.com"},
  "plugins": [{
    "name": "toolkit",
    "source": "./",
    "description": "Productivity skills for Claude Code",
    "version": "1.2.0"
  }]
}
```

```bash
# Instalacao
/plugin marketplace add author/my-skills
/plugin install toolkit@my-skills
# Formato: {plugin.json:name}@{marketplace.json:name}
```

## Anti-Patterns

- Version mismatch entre marketplace.json e plugin.json (install quebra)
- Omitir keywords (plugin invisivel no marketplace search)
- plugin.json sem license (bloqueia adocao enterprise/corporativa)
- Nome do plugin diferente entre os dois arquivos (referencia invalida)
- Source path apontando para diretorio inexistente no repo

## References

- source: https://github.com/kepano/obsidian-skills
- source: https://docs.anthropic.com/en/docs/claude-code
- related: p01_kc_cex_function_become

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_plugin]] | downstream | 0.47 |
| [[bld_architecture_plugin]] | downstream | 0.43 |
| [[plugin-builder]] | downstream | 0.42 |
| [[bld_tools_plugin]] | downstream | 0.42 |
| [[bld_memory_plugin]] | downstream | 0.41 |
| [[p01_kc_plugin]] | sibling | 0.41 |
| [[p11_qg_plugin]] | downstream | 0.40 |
| [[bld_config_plugin]] | downstream | 0.37 |
| [[bld_schema_plugin]] | downstream | 0.36 |
| [[bld_collaboration_marketplace_app_manifest]] | downstream | 0.34 |
