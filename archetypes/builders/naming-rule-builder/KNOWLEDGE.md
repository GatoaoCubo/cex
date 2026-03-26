---
pillar: P01
llm_function: INJECT
kind: knowledge
domain: naming_rule
version: 1.0.0
---

# Knowledge — Naming Rule Builder

## Foundational Concepts

A naming rule is a formal specification that defines the string format any artifact, file, variable, or entity within a bounded scope must follow. It is the single source of truth for "what is this thing called and how is that name structured."

Naming rules serve three functions:
1. **Consistency** — humans and machines resolve names predictably
2. **Parseability** — automated tools can extract metadata from the name itself
3. **Collision avoidance** — well-scoped patterns prevent name conflicts

## Industry Naming Standards Reference

| Standard | Domain | Case Style | Example |
|----------|--------|-----------|---------|
| PEP 8 | Python | snake_case (vars), PascalCase (classes) | `my_variable`, `MyClass` |
| Google Style | Multi-lang | camelCase (JS), snake_case (Python) | `myVariable`, `my_variable` |
| BEM CSS | UI components | block__element--modifier | `card__title--active` |
| DNS naming | Hostnames | kebab-case, lowercase, max 63 chars | `api-prod-v2.service.io` |
| NPM packages | JS packages | kebab-case, lowercase, no spaces | `my-package-name` |
| Java packages | JVM | reverse-domain dot-notation lowercase | `com.company.module.sub` |
| AWS resources | Cloud | kebab-case or snake_case by service | `my-s3-bucket`, `my_lambda` |
| Kubernetes | Infra | kebab-case, lowercase, max 253 chars | `my-deployment-v2` |

## Key Naming Patterns

1. **Pillar prefix**: `p{NN}_` — scopes artifact to CEX pillar (e.g., `p01_`, `p05_`)
2. **Kind abbreviation**: short token after prefix identifies artifact kind (e.g., `kc`, `nr`, `mc`)
3. **Scope slug**: kebab-case or snake_case descriptor of the artifact's subject
4. **Version suffix**: `_v{N}` or `-v{N}` appended when versioning is needed
5. **Environment tag**: `_prod`, `_dev`, `_test` as terminal segment when env-scoped
6. **Date stamp**: `_YYYYMMDD` or `_YYYY-MM-DD` for temporal artifacts
7. **Sequence number**: `_{NNN}` zero-padded for ordered series
8. **Hash suffix**: `_{8hex}` for content-addressed artifacts

## CEX Naming Extensions

| Kind | Pattern | Example |
|------|---------|---------|
| knowledge_card | `p01_kc_{topic_slug}.md` | `p01_kc_vector_search.md` |
| model_card | `p02_mc_{provider}_{model_slug}.md` | `p02_mc_openai_gpt4o.md` |
| naming_rule | `p05_nr_{scope_slug}.md` | `p05_nr_knowledge_card.md` |
| signal | `p12_sig_{event}.json` | `p12_sig_task_complete.json` |
| builder dir | `{kind}-builder/` (kebab-case) | `naming-rule-builder/` |

## Boundary Table

| Artifact | Answers | NOT this builder |
|----------|---------|-----------------|
| naming_rule (THIS) | "What format must the name follow?" | |
| response_format (P05 sibling) | "How should the LLM format its reply?" | NOT naming |
| parser (P05 sibling) | "How to extract data from LLM output?" | NOT naming |
| formatter (P05 sibling) | "How to render data into a target format?" | NOT naming |
| validator (P06 — confused) | "Does this artifact's content meet spec?" | NOT naming |
| type_def (P06 — confused) | "What abstract category does this belong to?" | NOT naming |
