---
kind: examples
id: bld_examples_changelog
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of changelog artifacts
quality: null
title: "Examples Changelog"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [changelog, builder, examples]
tldr: "Golden and anti-examples of changelog artifacts"
domain: "changelog construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example (changelog entry)
**Version:** v2.7.1  
**Date:** 2023-11-15  

### Features  
- Added support for real-time collaboration in [Notion](https://www.notion.so) via API v3.  
- Introduced [GraphQL](https://graphql.org) query optimization in [Hasura](https://hasura.io) for faster data fetching.  

### Fixes  
- Resolved a race condition in [PostgreSQL](https://www.postgresql.org) 15.2 that caused transaction rollbacks under high load.  
- Fixed incorrect token expiration logic in [Auth0](https://auth0.com) SDK v2.1.  

### Breaking Changes  
- Removed deprecated `v1` endpoints in [Stripe](https://stripe.com) API; migrate to `v2` as described in [docs](https://stripe.com/docs/api).  
- [Docker](https://docker.com) 24.0 now requires TLS 1.3; older clients will fail with `SSL_ERROR`.  

## Anti-Example 1: Missing Semver and Categorization  
**Version:** 2.7.1  
**Date:** 2023-11-15  
- Added real-time collaboration in Notion.  
- Fixed PostgreSQL transaction issues.  
- Removed old Stripe endpoints.  

## Why it fails  
Lacks semver formatting (e.g., `v2.7.1` vs `2.7.1` is minor), no categorization (features, fixes, breaking changes), and missing context (e.g., "TLS 1.3" requirement).  

## Anti-Example 2: Overly Vague Descriptions  
**Version:** v2.7.1  
**Date:** 2023-11-15  

### Features  
- Improved performance.  
- Added new functionality.  

### Fixes  
- Fixed some bugs.  

### Breaking Changes  
- Some APIs changed.  

## Why it fails  
Descriptions are too generic ("improved performance" vs "GraphQL query optimization"). No specific tools/vendors named, and no actionable details for users to migrate or adopt changes.
