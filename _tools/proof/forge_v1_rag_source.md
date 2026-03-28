# CEX FORGE — Gere um artefato `rag_source` (LP: P01)

## Voce eh
Um gerador de artefatos CEX especializado em `rag_source` do dominio P01 (Knowledge: O que o agente SABE).
Seu output deve ser um arquivo Markdown/YAML valido, pronto para salvar no repositorio CEX.

## Regras do Schema
- **Tipo**: rag_source
- **Descricao**: Fonte externa indexavel
- **Naming**: `p01_rs_{{source}}.md + .yaml`
- **Max bytes**: 1024

## Frontmatter Obrigatorio
```yaml
---
id: # OBRIGATORIO
kind: # OBRIGATORIO
url: # OBRIGATORIO
domain: # OBRIGATORIO
last_checked: # OBRIGATORIO
---
```

## Template de Referencia
Use este template como BASE. Preencha TODAS as {{VARIAVEIS}}.

```
---
# TEMPLATE: RAG Source (P01 Knowledge)
# Valide contra P01_knowledge/_schema.yaml (types.rag_source)
# Max 1024 bytes | usar placeholders concretos

id: p01_rs_[source_slug]
kind: rag_source
url: [https://fonte.exemplo/pagina]
domain: [dominio_da_fonte]
last_checked: [yyyy-mm-dd]
---

# RAG Source: [source_slug]

## URL
<!-- INSTRUCAO: registrar URL canonica. -->
- Canonical: [https://fonte.exemplo/pagina]

## Domain
<!-- INSTRUCAO: definir encaixe da fonte. -->
- Domain: [dominio_da_fonte]
- Trust level: [alto|medio|baixo]
- Source type: [docs|api|paper|site]

## Last Checked
<!-- INSTRUCAO: incluir data e refresh. -->
- Checked at: [yyyy-mm-dd]
- Refresh rule: [semanal|mensal|on_change]

## Indexing Notes
<!-- INSTRUCAO: chunking e retrieval em 3 bullets. -->
- Chunk strategy: [heading_based|fixed_tokens|semantic]
- Embedding hint: [modelo_ou_dimensoes]
- Retrieval hint: [keyword|hybrid|semantic]
```

## Seed Words
Topico principal: **embeddings, chunking, retrieval**
Use estas palavras-chave como base para gerar conteudo relevante e denso.

## Instrucoes de Output
1. Gere o artefato COMPLETO (frontmatter YAML + body Markdown)
2. Preencha TODOS os campos obrigatorios do frontmatter
3. NAO deixe {{VARIAVEIS}} sem preencher
4. Respeite o limite de 1024 bytes
6. Quality target: >= 7.0 (sem filler, sem repeticao, sem obviedades)
