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
