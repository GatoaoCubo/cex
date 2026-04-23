---
quality: 8.6
quality: 8.0
kind: tools
id: bld_tools_retry_policy
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for retry_policy production
title: "Tools Retry Policy"
version: "1.0.0"
author: n03_builder
tags: [retry_policy, builder, tools]
tldr: "Tools: cex_compile, cex_doctor, cex_score. Data sources: AWS Retry docs, Polly docs, operation error patterns."
domain: "retry policy construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_tools_model_architecture
  - bld_tools_kind
  - p11_qg_knowledge
  - bld_tools_training_method
  - skill
  - validate
  - bld_tools_consolidation_policy
  - bld_tools_procedural_memory
  - doctor
  - bld_tools_contributor_guide
---

# Tools: retry-policy-builder

## Runtime Tools

| Tool | Function | Stage |
|------|----------|-------|
| `cex_compile.py {path}` | Compile artifact to YAML | F8 COLLABORATE |
| `cex_doctor.py` | Validate builder integrity | F7 GOVERN |
| `cex_retriever.py --query {intent}` | Find similar retry_policy artifacts | F5 CALL |
| `cex_score.py {path}` | Peer-review quality scoring | F7 GOVERN |
| `cex_hooks.py validate {path}` | Frontmatter + field validation | F7 GOVERN |

## Context Sources

| Source | Content | Stage |
|--------|---------|-------|
| `N00_genesis/P01_knowledge/library/kind/kc_retry_policy.md` | Primary domain KC | F3 INJECT |
| `.cex/kinds_meta.json` (key: `retry_policy`) | Boundary, pillar, naming | F1 CONSTRAIN |
| `archetypes/builders/retry-policy-builder/bld_examples_retry_policy.md` | Reference examples | F3 INJECT |
| `archetypes/builders/retry-policy-builder/bld_schema_retry_policy.md` | Output schema | F2 BECOME |

## Discovery

```bash
# Find existing retry_policy artifacts
python _tools/cex_retriever.py --query "retry policy backoff jitter exponential"

# Validate a new artifact
python _tools/cex_hooks.py validate path/to/artifact.md

# Compile after writing
python _tools/cex_compile.py path/to/artifact.md
```

## External References

| Reference | Purpose |
|-----------|---------|
| aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter | AWS jitter types (Marc Brooker 2015) |
| github.com/App-vNext/Polly | .NET retry library reference |
| tenacity.readthedocs.io | Python retry library |
| resilience4j.readme.io/docs/retry | Resilience4j retry module (Java) |
| grpc.io/docs/guides/retry | gRPC retry policy specification |

## Validation Commands

| Command | Purpose | When |
|---------|---------|------|
| `python _tools/cex_compile.py {path}` | Compile .md to .yaml | F8 |
| `python _tools/cex_doctor.py` | Check builder health | F7 |
| `python _tools/cex_score.py {path} --apply` | Peer review + apply score | F7 |
| `python _tools/cex_retriever.py --query "retry backoff jitter"` | Find similar artifacts | F5 |
| `git add {path} && git commit` | Version artifact | F8 |
| `python _tools/cex_index.py` | Update artifact index | F8 |
| `python _tools/cex_retriever.py --similar {path}` | Find similar retry configs | F5 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_model_architecture]] | sibling | 0.32 |
| [[bld_tools_kind]] | sibling | 0.30 |
| [[p11_qg_knowledge]] | downstream | 0.29 |
| [[bld_tools_training_method]] | sibling | 0.29 |
| [[skill]] | downstream | 0.27 |
| [[validate]] | downstream | 0.27 |
| [[bld_tools_consolidation_policy]] | sibling | 0.26 |
| [[bld_tools_procedural_memory]] | sibling | 0.26 |
| [[doctor]] | downstream | 0.26 |
| [[bld_tools_contributor_guide]] | sibling | 0.25 |
