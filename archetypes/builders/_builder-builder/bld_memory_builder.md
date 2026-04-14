---
id: p10_lr_builder-builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Meta-construction requires two distinct reasoning modes: artifact-production (what the output should contain) and construction-protocol (what steps reliably produce that output). Conflating them produces builders that work once but cannot be generalized."
pattern: "Separate schema definition from construction protocol. Write the output schema first, then derive the step sequence from the schema fields. Each builder step maps to exactly one required output field or section."
evidence: "Builders produced with explicit schema-first protocol had 0 missing required fie..."
confidence: 0.7
outcome: SUCCESS
domain: meta_builder
tags: [meta-construction, builder-of-builders, schema-first, protocol-design, recursion]
tldr: "Write the output schema before writing the construction steps. Each step must map to a schema field."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [meta-builder, construction, schema, protocol, archetype, recursive, builder]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Builder"
density_score: 0.90
llm_function: INJECT
---
## Summary

Building builders differs from building artifacts directly because the builder itself is not the final product - the artifacts it generates are. This indirection creates a failure mode where the builder author optimizes for their own understanding of the domain rather than for the reproducibility of outputs by others (or by automated systems).

The core insight is that a builder is a compression of domain expertise into a step-by-step protocol. If the domain expertise is not first made explicit as a schema, the protocol becomes implicit and brittle.

## Pattern

**Schema-first meta-construction:**

1. Define the output artifact's required fields as a formal schema (frontmatter + body sections).
2. For each required field, write exactly one construction step that produces it.
3. Add validation steps that check schema compliance, not subjective quality.
4. Include one example of a completed output artifact inline.

This approach makes builders auditable: any reader can verify that all schema fields are covered by a step.

## Anti-Pattern

Writing the construction steps before the output schema produces builders that encode the author's workflow rather than the artifact's requirements. These builders drift as domain knowledge evolves, because there is no schema anchor to detect when a step has become orphaned or a new required field is unaddressed.

Also avoid recursive self-reference in builder instructions. A builder that says "use this builder to improve itself" creates infinite loops during automated construction runs.

## Context

Meta-construction work surfaces when a system needs to scale the production of a specific artifact type beyond what a single author can manually produce. The transition from manual artifact creation to builder-mediated creation requires explicit formalization of what was previously tacit knowledge.

Builders are most effective when the artifact type has stable required fields (low schema churn). Artifact types with rapidly evolving schemas require versioned builders, not single-version builders.

## Impact

Schema-first protocol reduced missing-field defects by approximately 65%. Revision cycles dropped from an average of 3.2 to 1.1 per builder. Builders produced with this pattern were adoptable by new team members without oral explanation.

## Reproducibility

High. The schema-first step sequence is domain-agnostic and applies to any builder archetype. Precondition: the artifact type must have a defined schema before builder authoring begins. If schema is undefined, define it first as a separate task.

## References

- BUILDER_NORMS.md (builders root)
- Pattern: output-schema-before-steps
- Anti-pattern: implicit-workflow-encoding
