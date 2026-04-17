---
id: ex-dag-multi-marketplace-sync
kind: dag
pillar: P12
title: Multi-Marketplace Sync DAG
version: 0.1.0
quality: 8.9
status: template
brand_placeholders:
  - BRAND_SHOPIFY_STORE_DOMAIN
  - BRAND_BLING_API_URL
  - BRAND_MELI_USER_ID
tags: [commerce, template, distillation, orchestration, dag]
density_score: 1.0
---

# Multi-Marketplace Sync DAG

## Purpose
Formal directed-acyclic-graph specification for the sync workflow. Lets the scheduler parallelize independent steps (pull Shopify, pull Bling, pull ML can run concurrently) while enforcing barriers before reconcile + push.

## When to use
- The workflow has >5 steps and some are independent.
- You want deterministic ordering for debugging (same run id -> same trace topology).
- You plan to swap a runner (e.g. from Supabase cron to Dagster or Prefect) later.

## Brand variables used
- `{{BRAND_SHOPIFY_STORE_DOMAIN}}`, `{{BRAND_BLING_API_URL}}`, `{{BRAND_MELI_USER_ID}}` -- per-channel target identifiers referenced in the pull nodes.

## Graph (nodes + edges)

```yaml
nodes:
  - id: acquire_lock
    type: barrier
    action: pg_advisory_lock(sync)
  - id: load_health
    type: read
    action: query channel_health
  - id: pull_shopify
    type: fetch
    channel: shopify
    target: "{{BRAND_SHOPIFY_STORE_DOMAIN}}"
  - id: pull_bling
    type: fetch
    channel: bling
    target: "{{BRAND_BLING_API_URL}}"
  - id: pull_meli
    type: fetch
    channel: meli
    target: "{{BRAND_MELI_USER_ID}}"
  - id: reconcile
    type: transform
    rule_set: dispatch_rule_multi_marketplace
  - id: push_shopify
    type: write
    channel: shopify
  - id: push_bling
    type: write
    channel: bling
  - id: push_meli
    type: write
    channel: meli
  - id: audit
    type: verify
  - id: release_lock
    type: barrier
    on_failure: always_run
edges:
  - [acquire_lock, load_health]
  - [load_health, pull_shopify]
  - [load_health, pull_bling]
  - [load_health, pull_meli]
  - [pull_shopify, reconcile]
  - [pull_bling, reconcile]
  - [pull_meli, reconcile]
  - [reconcile, push_shopify]
  - [reconcile, push_bling]
  - [reconcile, push_meli]
  - [push_shopify, audit]
  - [push_bling, audit]
  - [push_meli, audit]
  - [audit, release_lock]
```

## Concurrency budget
- Three pull nodes may run in parallel -- each channel's client enforces its own rate limit.
- Three push nodes may run in parallel -- same reasoning.
- Reconcile is a hard barrier: must see all three pulls or their failure-as-empty substitutes.

## Failure propagation
- A fetch node's failure substitutes an empty input to reconcile (channel-skipped mode).
- A push node's failure is isolated: audit sees the per-channel outcome and emits metrics; the DAG still completes.
- `release_lock` is tagged `on_failure: always_run` to guarantee lock release.

## Observability
Each node emits `{node_id, started_at, ended_at, rows_in, rows_out, outcome}` to `sync_dag_trace`. Graph visualization tool can render a waterfall per run id.

## Related artifacts
- `ex_workflow_multi_marketplace_sync.md`
- `ex_dispatch_rule_multi_marketplace.md`
