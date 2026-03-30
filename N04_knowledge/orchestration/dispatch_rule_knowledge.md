---
id: p12_dr_knowledge
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2023-10-20
updated: 2023-10-20
author: dispatch_rule_builder
domain: knowledge
quality: null
tags: [dispatch, knowledge, agent_node_alpha]
tldr: Routes document indexing and retrieval tasks to knowledge agent_node
scope: knowledge
keywords: [conhecimento, knowledge, indexar, index, recuperar, retrieve, documento, document]
agent_node: agent_node_alpha
model: haiku
priority: 7
confidence_threshold: 0.70
fallback: agent_node_beta
conditions: null
load_balance: false
routing_strategy: keyword_match
---

# Knowledge Dispatch Rule

## Purpose

Routes tasks related to document indexing and retrieval to the designated knowledge agent_node. This ensures that operations concerning knowledge management are processed efficiently by the designated resources.

## Keyword Rationale

Selected keywords cover both Portuguese and English terms for document processing, ensuring comprehensive coverage across bilingual task inputs.

## Fallback Logic

In cases where confidence falls below the threshold, tasks are rerouted to a backup agent_node which possesses the capability to manage knowledge operations in a broader context.