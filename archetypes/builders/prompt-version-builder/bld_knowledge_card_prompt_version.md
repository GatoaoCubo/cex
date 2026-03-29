---
kind: knowledge_card
id: bld_knowledge_card_prompt_version
pillar: P03
llm_function: INJECT
purpose: Domain knowledge for prompt_version production
sources: PromptLayer versioning, LangChain Hub, prompt management best practices, A/B testing frameworks, prompt regression testing
---

# Domain Knowledge: prompt_version
## Executive Summary
Prompt version — immutable snapshot of a prompt at a point in time with metrics and lineage. Produced as P03 artifacts with concrete parameters and rationale.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P03 |
| llm_function | GOVERN |
| Max bytes | 2048 |
| Density min | 0.8 |
| Machine format | yaml |
## Patterns
| Pattern | Description | When to use |
|---------|-------------|-------------|
| Sequential | v1 -> v2 -> v3 linear evolution | Iterative improvement, single author |
| Branching | v1 -> v2a (experiment) + v2b (control) | A/B testing, parallel optimization |
| Optimized | DSPy/automated optimizer produces new version | Automated prompt tuning, metric-driven |
| Rollback | Revert to previous version on regression | Production safety, quality regression |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No version tracking | Cannot reproduce results or rollback on regression |
| Mutable versions | Changing a 'version' in place breaks reproducibility |
| No metrics | Cannot compare versions objectively |
| No parent lineage | Cannot trace how a prompt evolved or why changes were made |
## Application
1. Identify the use case and constraints
2. Select appropriate pattern from the table above
3. Define concrete parameter values with rationale
4. Validate against SCHEMA.md required fields
5. Check body size <= 2048 bytes
6. Verify id matches `^p03_pv_[a-z][a-z0-9_]+$`
## References
- PromptLayer version tracking, DSPy optimized prompts, LangChain Hub versioning, Humanloop prompt management, Braintrust prompt registry
- PromptLayer versioning, LangChain Hub, prompt management best practices, A/B testing frameworks, prompt regression testing
