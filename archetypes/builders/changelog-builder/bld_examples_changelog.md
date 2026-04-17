---
kind: examples
id: bld_examples_changelog
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of changelog artifacts
quality: 8.9
title: "Examples Changelog"
version: "1.1.0"
author: wave1_builder_gen_v2
tags: [changelog, builder, examples]
tldr: "Golden and anti-examples of changelog artifacts -- Keep a Changelog format, SemVer 2.0"
domain: "changelog construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example (Keep a Changelog format)

```yaml
---
id: p01_ch_myapp_2_7_1.md
kind: changelog
pillar: P01
title: "MyApp Changelog"
version: "2.7.1"
release_date: "2024-01-15"
author: "jsmith"
domain: "saas-platform"
quality: null
tags: [security, fix]
tldr: "Patch: fix race condition in auth, patch TLS requirement for Docker clients"
---
```

## [2.7.1] - 2024-01-15

### Fixed
- Fix race condition in PostgreSQL 15.2 transaction handling under high load (fixes #4521)
- Fix incorrect token expiration logic in Auth0 SDK v2.1 integration (fixes #4489)

### Security
- Patch TLS requirement: Docker 24.0 now enforces TLS 1.3; older clients receive SSL_ERROR (CVE-2023-44487, affects < 2.7.1)

---

## [2.7.0] - 2024-01-10

### Added
- Add real-time collaboration support via Notion API v3 (PR #4401)
- Add GraphQL query optimization in Hasura for improved data fetch latency

### Changed
- Change authentication token refresh interval from 60m to 30m for security hardening

### Deprecated
- Deprecate v1 REST endpoints -- removal scheduled for 3.0.0

### Removed
- BREAKING: Remove deprecated `/api/v1/` endpoints -- migrate to `/api/v2/` per migration guide

## Anti-Example 1: Missing Keep a Changelog sections and vague entries
**Version:** v2.7.1
**Date:** 2024-01-15
- Added real-time collaboration in Notion.
- Fixed PostgreSQL transaction issues.
- Removed old Stripe endpoints.

**Why it fails:** Uses informal section-free list. No Added/Changed/Fixed/Security structure. Entries vague ("transaction issues" vs the specific race condition). No issue IDs. No CVE for the security patch.

## Anti-Example 2: Wrong version bump + no migration for MAJOR
**Version:** 2.8.0

### Features
- Removed legacy /api/v1/ endpoints.
- Added new auth system.

**Why it fails:** Removing endpoints is a BREAKING change requiring MAJOR bump (3.0.0 not 2.8.0). Section is called "Features" not "Removed" (KAC standard). No Migration section for the breaking removal. Version uses 2-part not SemVer 3-part format.
