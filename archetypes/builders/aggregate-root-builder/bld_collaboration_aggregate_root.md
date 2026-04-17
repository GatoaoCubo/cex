---
id: bld_rules_aggregate_root
kind: knowledge_card
pillar: P06
title: "Aggregate Root Builder -- Rules"
version: 1.0.0
quality: null
tags: [builder, aggregate_root, rules]
llm_function: CONSTRAIN
---
# Rules: aggregate_root
## Absolute Rules (HARD -- never violate)
1. One transaction = one aggregate. Never span two aggregates in a single transaction.
2. External references to cluster members go through the root only -- never directly.
3. Cross-aggregate references use IDs (value_object), never object instances.
4. Repository interface: find_by_id and save only. No query methods on the aggregate repo.
5. Invariants must be checkable after every command -- they are not guidelines.
6. quality: null always -- never self-score.
## Soft Rules (RECOMMEND -- deviate with justification)
1. Aggregate cluster size: prefer 2-5 members. Document reason if > 7.
2. Optimistic concurrency preferred over pessimistic unless contention proven.
3. Domain events should be named in past tense (OrderPlaced, not PlaceOrder).
4. Invariant count: 2-5 per aggregate. More than 8 suggests over-aggregation.
## Boundary Rules
1. THIS BUILDER handles: aggregate_root (P06)
2. NOT this builder: interface (contract definition) -> interface-builder
3. NOT this builder: input_schema (data validation) -> input-schema-builder
4. NOT this builder: value_object (immutable attribute type) -> value-object-builder
5. NOT this builder: domain event specification -> domain-event-builder
## CEX-Specific Rules
1. id pattern: p06_ar_{slug} -- always prefix p06_ar_
2. Pillar: always P06 (Schema)
3. Producing nucleus: N03 (Engineering) -- not N04 or N05
4. Compile after save: python _tools/cex_compile.py {path}
