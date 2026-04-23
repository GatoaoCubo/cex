---
kind: quality_gate
id: p09_qg_terminal_backend
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for terminal_backend
quality: 8.7
title: "Quality Gate Terminal Backend"
version: "1.0.0"
author: n03_engineering
tags: [terminal_backend, builder, quality_gate]
tldr: "Quality gate for terminal_backend: 5 HARD gates (backend_type, timeout, auth, serverless-flag, ID pattern), 5D SOFT scoring"
domain: "terminal_backend construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.92
related:
  - p03_ins_vector_store
  - p11_qg_session_backend
  - bld_config_session_backend
  - p01_vdb_pinecone
  - bld_schema_vector_store
  - p09_qg_sandbox_config
  - p11_qg_vector_store
  - bld_schema_session_backend
  - p06_qg_api_reference
  - bld_examples_session_backend
---

## Quality Gate
## Definition
| metric | threshold | operator | scope |
|--------|-----------|----------|-------|
| Backend Type Valid | one of 6 | required | backend_type field |
| Timeout Defined | > 0 | required | limits.timeout_seconds |
| Quality Score | 8.0 | >= | Publish threshold |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|---------------|
| H01 | YAML valid | Invalid YAML syntax in artifact |
| H02 | ID matches pattern | ID does not match `^p09_tb_[a-z0-9_-]+$` |
| H03 | backend_type valid | backend_type not in {local, docker, ssh, daytona, modal, singularity} |
| H04 | timeout_seconds set | limits.timeout_seconds is null or missing |
| H05 | auth consistency | auth.method != none but auth.secret_ref is null |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D1 | Schema Completeness | 0.25 | All required fields present+typed=1.0; missing 1=0.7; missing 2+=0.3 |
| D2 | Backend Specificity | 0.25 | Connection block + backend-specific fields=1.0; generic only=0.6; empty=0.2 |
| D3 | Auth Correctness | 0.20 | Method matches backend type + secret_ref set=1.0; method set but no ref=0.6; none for auth-required=0.0 |
| D4 | Cost Model Accuracy | 0.15 | billing + estimated_usd_per_hour both set=1.0; billing only=0.7; neither=0.3 |
| D5 | Serverless Flags | 0.15 | serverless+hibernation_capable match backend capabilities=1.0; one wrong=0.5; both wrong=0.0 |

**Weight sum: 0.25+0.25+0.20+0.15+0.15 = 1.00**

## Actions
| Score | Action |
|-------|--------|
| GOLDEN >=9.5 | Auto-approve, ready for nucleus deployment |
| PUBLISH >=8.0 | Manual review, staging allowed |
| REVIEW >=7.0 | Peer review required, no deployment |
| REJECT <7.0 | Block deployment, fix required |

## Bypass
| conditions | approver | audit trail |
|------------|----------|-------------|
| Emergency backend switch with compensating documentation | N05 Lead | Incident ticket |
| New backend type not in supported list | Architecture review | ADR required |
| auth.method=none on ssh in air-gapped network with compensating network controls | Security Lead | Security exception ticket + 30-day expiry |

## Examples
## Golden Example 1: Local Backend (Dev Default)
```yaml
---
id: p09_tb_local
kind: terminal_backend
pillar: P09
title: "Terminal Backend: local"
backend_type: local
serverless: false
hibernation_capable: false
auth:
  method: none
  secret_ref: null
limits:
  cpu_cores: null
  memory_gb: null
  timeout_seconds: 3600
cost_model:
  billing: free
  estimated_usd_per_hour: null
version: 1.0.0
quality: null
tags: [hermes_origin, backend, runtime, local]
---
```

**Why it passes:** All required fields present. auth.method=none is correct for local. serverless=false correct. timeout_seconds set. billing=free for local.

---

## Golden Example 2: Modal Serverless GPU Backend
```yaml
---
id: p09_tb_modal
kind: terminal_backend
pillar: P09
title: "Terminal Backend: modal (GPU serverless)"
backend_type: modal
serverless: true
hibernation_capable: false
auth:
  method: api_token
  secret_ref: p09_secret_modal_api_key
limits:
  cpu_cores: 8
  memory_gb: 32.0
  timeout_seconds: 900
cost_model:
  billing: per_second
  estimated_usd_per_hour: 2.88
version: 1.0.0
quality: null
tags: [hermes_origin, backend, runtime, modal, serverless, gpu]
---

## Connection
app_name: cex-executor
stub_name: run_task
gpu: A100
```

**Why it passes:** serverless=true correct for modal. auth=api_token with secret_ref set. timeout 900s appropriate for GPU jobs. billing=per_second with realistic USD/hr estimate.

---

## Golden Example 3: SSH Private Cluster
```yaml
---
id: p09_tb_ssh_gpu_cluster
kind: terminal_backend
pillar: P09
title: "Terminal Backend: ssh (private GPU cluster)"
backend_type: ssh
serverless: false
hibernation_capable: false
auth:
  method: ssh_key
  secret_ref: p09_secret_ssh_cluster_key
limits:
  cpu_cores: 32
  memory_gb: 128.0
  timeout_seconds: 86400
cost_model:
  billing: subscription
  estimated_usd_per_hour: 0.0
version: 1.0.0
quality: null
tags: [hermes_origin, backend, runtime, ssh, cluster]
---

## Connection
host: gpu-cluster.internal
user: cex-agent
port: 22
key_path: "{{auth.secret_ref}}"
```

**Why it passes:** ssh requires ssh_key auth with secret_ref. timeout 86400s for long HPC jobs. billing=subscription with $0 estimated (internal cluster).

---

## Golden Example 4: Daytona Cloud Dev Environment
```yaml
---
id: p09_tb_daytona
kind: terminal_backend
pillar: P09
title: "Terminal Backend: daytona"
backend_type: daytona
serverless: true
hibernation_capable: true
auth:
  method: api_token
  secret_ref: p09_secret_daytona_api
limits:
  cpu_cores: 4
  memory_gb: 8.0
  timeout_seconds: 7200
cost_model:
  billing: per_task
  estimated_usd_per_hour: 0.25
version: 1.0.0
quality: null
tags: [hermes_origin, backend, runtime, daytona, serverless, hibernation]
---
```

**Why it passes:** daytona supports both serverless=true AND hibernation_capable=true. api_token auth with secret_ref. per_task billing is correct for daytona.

---

## Anti-Example 1: Missing timeout + wrong serverless flag
```yaml
---
id: p09_tb_broken_docker
kind: terminal_backend
backend_type: docker
serverless: true        # FAIL: docker is not serverless
hibernation_capable: true  # FAIL: docker does not support hibernation
auth:
  method: none
limits:
  cpu_cores: 4
  # MISSING: timeout_seconds -- sessions can run forever
cost_model:
  billing: free
---
```

**Why it fails:** H03 FAIL (serverless=true invalid for docker). H04 FAIL (hibernation_capable=true invalid for docker). H02 FAIL (missing timeout_seconds).

---

## Anti-Example 2: SSH without ssh_key auth
```yaml
---
id: p09_tb_insecure_ssh
kind: terminal_backend
backend_type: ssh
serverless: false
auth:
  method: none    # FAIL: SSH backend requires ssh_key or api_token
  secret_ref: null  # FAIL: secret_ref null but ssh needs a key
limits:
  timeout_seconds: 3600
cost_model:
  billing: free
---
```

**Why it fails:** H05 FAIL -- SSH backend with auth.method=none means unauthenticated SSH, which is invalid in any production setup. Must use ssh_key with secret_ref.

---

## Decision Matrix: Choosing Backend Type
| Requirement | Recommended Backend | Key Reason |
|-------------|--------------------|----|
| Local dev, no cost | local | billing=free, no auth overhead |
| Containerized isolation | docker | reproducible env, no serverless overhead |
| Remote managed machine | ssh | direct shell, persistent state |
| Managed cloud dev env | daytona | hibernation saves cost, API token auth |
| Serverless GPU inference | modal | per-invocation billing, GPU-native |
| Enterprise air-gapped | singularity | HPC/on-prem, no cloud dependency |

## Backend Capability Matrix
| Backend | serverless | hibernation_capable | auth_required | billing_type |
|---------|-----------|---------------------|---------------|-------------|
| local | false | false | none | free |
| docker | false | false | none | free |
| ssh | false | false | ssh_key | free |
| daytona | true | true | api_token | per_task |
| modal | true | false | api_token | per_invocation |
| singularity | false | false | ssh_key | site_license |

## Anti-Example 3: Modal with wrong billing type
```yaml
---
id: p09_tb_modal_wrong
kind: terminal_backend
backend_type: modal
serverless: true
hibernation_capable: true    # FAIL: modal does not support hibernation
auth:
  method: api_token
  secret_ref: secrets/modal_api_key
limits:
  timeout_seconds: 300
cost_model:
  billing: per_task            # FAIL: modal bills per_invocation not per_task
  estimated_usd_per_hour: 1.20
---
```

**Why it fails:** H04 FAIL (hibernation_capable=true invalid for modal). D4 FAIL (billing=per_task wrong for modal; use per_invocation). D5 partial (serverless correct but hibernation wrong).

## HARD Gate Reference
| Gate | Field Checked | Invalid Value Pattern |
|------|--------------|----------------------|
| H01 | YAML syntax | parse error on any required field |
| H02 | id | not matching `^p09_tb_[a-z0-9_-]+$` |
| H03 | backend_type | value outside {local,docker,ssh,daytona,modal,singularity} |
| H04 | limits.timeout_seconds | null, missing, or 0 |
| H05 | auth consistency | method != none AND secret_ref == null |

## Correct backend_type + serverless Combinations
| backend_type | serverless | hibernation_capable | Notes |
|-------------|-----------|---------------------|-------|
| local | false | false | Always non-serverless; runs on developer machine |
| docker | false | false | Container is persistent, not ephemeral |
| ssh | false | false | Remote machine; connection is persistent |
| daytona | true | true | Only backend supporting both flags simultaneously |
| modal | true | false | Serverless-only; no hibernation support (per-invocation) |
| singularity | false | false | HPC container; persistent compute, site-license billing |

## Cost Model Accuracy by Backend
| backend_type | billing | estimated_usd_per_hour | Pattern |
|-------------|---------|------------------------|---------|
| local | free | null | Zero cost; null is correct for free tier |
| docker | free | null | Local container; no cloud billing |
| ssh | free | 0.0 | Remote machine managed externally |
| daytona | per_task | 0.08-0.25 | Depends on machine spec |
| modal | per_invocation | 0.001-0.05 | GPU type dependent |
| singularity | site_license | null | Institutional rate; unknown per-hour |

## Field Dependency Rules (H05 enforcement)
- `auth.method = none` is valid ONLY when `backend_type IN {local, docker}`
- `auth.method = ssh_key` requires `auth.secret_ref` pointing to a p09_secret artifact
- `auth.method = api_token` requires `auth.secret_ref` pointing to a p09_secret artifact
- `hibernation_capable = true` is valid ONLY when `backend_type = daytona`
- `serverless = true` is valid ONLY when `backend_type IN {daytona, modal}`
- `billing = per_invocation` is valid ONLY when `serverless = true`
- `billing = per_task` maps to daytona; `per_invocation` maps to modal; `free` maps to local/docker
- `limits.timeout_seconds = null` is H04 FAIL regardless of backend type

## Quick Reference: Minimum Valid Frontmatter per Backend
**local**: id, kind=terminal_backend, pillar=P09, backend_type=local, serverless=false, hibernation_capable=false, auth.method=none, limits.timeout_seconds>=1, cost_model.billing=free, quality=null
**docker**: same as local but backend_type=docker; auth.method=none valid; no cloud secrets needed
**ssh**: backend_type=ssh, serverless=false, auth.method=ssh_key, auth.secret_ref=p09_secret_*, billing=free
**daytona**: backend_type=daytona, serverless=true, hibernation_capable=true, auth.method=api_token, auth.secret_ref required, billing=per_task
**modal**: backend_type=modal, serverless=true, hibernation_capable=false, auth.method=api_token, billing=per_invocation
**singularity**: backend_type=singularity, serverless=false, hibernation_capable=false, auth.method=ssh_key, billing=site_license

## Validation Sequence (F7 GOVERN order)
Step 1 -- H01: parse YAML; if syntax error, reject immediately, no further gates checked
Step 2 -- H02: verify id matches `^p09_tb_[a-z0-9_-]+$`; fail if pattern mismatch
Step 3 -- H03: verify backend_type is one of the 6 supported values; fail otherwise
Step 4 -- H04: verify limits.timeout_seconds is a positive integer; null or missing fails
Step 5 -- H05: if auth.method != none, verify auth.secret_ref is non-null; fail on mismatch
Step 6 -- D1-D5: compute weighted soft score; PUBLISH requires >= 8.0 across all dimensions
Step 7 -- final gate: if hard gates all pass and soft score >= 8.0, artifact is ACCEPTED
Step 8 -- on reject: emit structured failure report listing gate IDs and field paths that failed
Step 9 -- revision context: pass failing gate IDs to next iteration if revision_loop_policy active
Step 10 -- bypass check: verify no active bypass conditions before marking gate as failed

## Soft Score Calibration Examples
D1=1.0: all required fields (id, kind, pillar, backend_type, serverless, hibernation_capable, auth, limits, cost_model) present and correctly typed
D1=0.7: one required field missing (e.g., cost_model.billing absent)
D1=0.3: two or more required fields missing
D2=1.0: connection block present with backend-specific fields (e.g., host+port for ssh, app_name for modal)
D2=0.6: only generic resource limits provided; no connection-specific configuration
D3=1.0: auth.method matches backend type AND auth.secret_ref is non-null where required
D3=0.6: auth.method is set but auth.secret_ref is null despite backend requiring credentials
D3=0.0: auth.method=none on a backend (ssh/daytona/modal) that requires authentication
D4=1.0: both billing type and estimated_usd_per_hour are present and realistic for the backend
D5=1.0: serverless and hibernation_capable both match the backend type's actual capabilities
D5=0.5: one of the two flags is correct; the other does not match backend capabilities
D5=0.0: both serverless and hibernation_capable flags are wrong for the specified backend_type

## Naming Convention Examples
Valid: p09_tb_local, p09_tb_modal_gpu, p09_tb_ssh_cluster_prod, p09_tb_daytona_dev_a100
Invalid: tb_local (missing pillar prefix), p09_modal (missing tb_ infix), p09_tb_Modal (uppercase not allowed)
Pattern: ^p09_tb_[a-z][a-z0-9_-]*$ -- all lowercase, must start with letter after infix, no spaces

## Tags Required on Every terminal_backend Artifact
- `hermes_origin`: required for all HERMES-assimilated kinds; enables audit and lineage tracking
- `backend`: required; used by cex_retriever to surface terminal_backend artifacts in type queries
- `runtime`: required; marks artifact as infrastructure-tier (not application-tier)
- Backend-specific tag (e.g., modal, daytona, ssh): required; enables nucleus-level filtering by backend
- `serverless`: required when serverless=true; enables cost-aware pipeline routing decisions
- `hibernation`: required when hibernation_capable=true; signals hibernation_policy pairing needed
- `gpu`: recommended when limits include GPU resources; enables GPU-aware scheduling queries
- `p09_secret_*` artifacts must be pre-created before terminal_backend artifact is published
- N05 owns terminal_backend artifacts; N03 builds them; routing via dispatch.sh solo n05
- hiberation_policy pairing: daytona backends SHOULD reference a hibernation_policy artifact
- cost_model.estimated_usd_per_hour must be a float (not a string) or null for free backends
- revision on H05 failure: update auth.method to match backend type or add auth.secret_ref
- revision on H04 failure: set limits.timeout_seconds to backend-appropriate value (see matrix)
- singularity backend: always pair with HPC cluster configuration; billing=site_license, not free

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
