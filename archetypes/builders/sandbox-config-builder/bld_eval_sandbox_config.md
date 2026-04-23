---
kind: quality_gate
id: p09_qg_sandbox_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for sandbox_config
quality: 9.0
title: "Quality Gate Sandbox Config"
version: "1.1.0"
author: n05_ops
tags: [sandbox_config, builder, quality_gate]
tldr: "Quality gate for sandbox_config: 8 HARD gates (isolation, limits, timeout, network), 5D SOFT scoring sum=1.0"
domain: "sandbox_config construction"
created: "2026-04-13"
updated: "2026-04-13"
last_reviewed: "2026-04-18"
density_score: 0.90
related:
  - bld_examples_sandbox_config
  - bld_instruction_sandbox_config
  - bld_output_template_sandbox_config
  - bld_knowledge_card_sandbox_config
  - p09_qg_sandbox_spec
  - p10_lr_code_executor_builder
  - p11_qg_code_executor
  - bld_knowledge_card_code_executor
  - p04_exec_python_sandbox
  - bld_examples_code_executor
---

## Quality Gate

## Definition

| metric | threshold | operator | scope |
|--------|-----------|----------|-------|
| Isolation Level | High | >= | Sandbox Environment |
| Resource Limits | Defined | required | CPU + RAM + disk + timeout |
| Quality Score | 8.0 | >= | Publish threshold |

## HARD Gates

| ID | Check | Fail Condition |
|----|-------|---------------|
| H01 | YAML valid | Invalid YAML syntax |
| H02 | ID matches pattern | ID does not match `^p09_sb_[a-zA-Z0-9_-]+$` (schema pattern) |
| H03 | kind matches | kind != `sandbox_config` |
| H04 | Resource limits present | Missing any of: cpu, memory, disk, timeout |
| H05 | Network policy defined | No network isolation policy specified |
| H06 | Filesystem scope defined | No filesystem root or read/write boundaries specified |
| H07 | Seccomp or MAC policy | No seccomp profile AND no AppArmor/SELinux policy |
| H08 | No privileged mode | `privileged: true` present (automatic REJECT) |

## SOFT Scoring

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D1 | Resource Completeness | 0.25 | CPU+RAM+disk+timeout all defined=1.0; missing 1=0.7; missing 2+=0.3 |
| D2 | Isolation Strength | 0.25 | Namespace+seccomp+MAC=1.0; namespace only=0.7; none=0.2 |
| D3 | Network Policy | 0.20 | Air-gapped or whitelist=1.0; partial restrict=0.6; unrestricted=0.0 |
| D4 | Filesystem Scope | 0.15 | Read-only root+ephemeral scratch=1.0; read-only only=0.7; writable root=0.3 |
| D5 | Auditability | 0.15 | Audit log + timeout enforcement=1.0; partial=0.6; none=0.2 |

**Weight sum: 0.25+0.25+0.20+0.15+0.15 = 1.00**

## Actions

| Score | Action |
|-------|--------|
| GOLDEN >=9.5 | Auto-approve, production-ready |
| PUBLISH >=8.0 | Manual review, staging deploy |
| REVIEW >=7.0 | Peer review required, no deployment |
| REJECT <7.0 | Block deployment, fix required |

## Bypass

| conditions | approver | audit trail |
|------------|----------|-------------|
| Security exception with compensating controls | Security Lead | SEC ticket required |
| Critical hotfix with temporary relaxed limits | SRE Lead | Incident ticket required |
| Compliance override (regulatory requirement) | Legal + CISO | Signed waiver required |

## Examples

## Golden Example 1: E2B Cloud Sandbox (AI Code Execution)

```yaml
---
id: p09_sb_ai_code_runner
kind: sandbox_config
pillar: P09
title: "AI Code Runner -- E2B Firecracker Sandbox"
version: "1.0.0"
platform: e2b
sandbox_type: isolated
---

resource_limits:
  cpu: 1            # 1 vCPU (Firecracker KVM)
  memory_mb: 512    # 512 MB RAM; OOM kills on exceed
  disk_mb: 1024     # 1 GB ephemeral scratch
  timeout_seconds: 30  # wall-clock; SIGKILL on exceed
  max_pids: 50

network:
  mode: none         # air-gapped; no internet access
  egress: none
  allowed_hosts: []
  dns: false

filesystem:
  root: /tmp/sandbox
  read_only_root: true
  scratch_dir: /tmp
  scratch_size_mb: 512
  mounts: []

isolation:
  runtime: firecracker
  namespaces: [pid, net, mnt, uts, ipc, user]
  seccomp_profile: default
  capabilities:
    drop: [ALL]
    add: []
  no_new_privs: true

audit:
  syscall_logging: true
  log_destination: /var/log/sandbox/
  log_retention_days: 7
```

**Why it passes:** CPU+RAM+disk+timeout all defined. Air-gapped network. Read-only root + ephemeral
scratch. Firecracker microVM provides VM-level isolation. All capabilities dropped. Seccomp enabled.

---

## Golden Example 2: Docker + gVisor Sandbox (Untrusted Code)

```yaml
---
id: p09_sb_untrusted_exec
kind: sandbox_config
pillar: P09
title: "Untrusted Code Execution -- Docker + gVisor"
platform: gvisor
sandbox_type: isolated
---

resource_limits:
  cpu: 0.5
  memory_mb: 256
  disk_mb: 512
  timeout_seconds: 15

network:
  mode: bridge
  egress: whitelist
  allowed_hosts: [api.example.com]
  allowed_ports: [443]

filesystem:
  read_only_root: true
  scratch_dir: /tmp
  scratch_size_mb: 256

isolation:
  runtime: runsc        # gVisor user-space kernel
  seccomp_profile: default
  apparmor_profile: docker-default
  capabilities:
    drop: [ALL]
    add: [NET_BIND_SERVICE]
  no_new_privs: true
```

**Why it passes:** gVisor intercepts all syscalls via user-space kernel (strongest isolation).
Egress whitelist restricts outbound. Timeout enforced. All caps dropped.

---

## Anti-Example 1: Missing Timeout + Open Network

```yaml
---
id: p09_sb_broken
kind: sandbox_config
platform: docker
---

resource_limits:
  cpu: 4
  memory_mb: 4096
  # MISSING: timeout_seconds -- sandbox can hang indefinitely

network:
  mode: host    # FAIL: shares host network namespace
  egress: all   # FAIL: unrestricted outbound (data exfiltration risk)

filesystem:
  root: /home/user    # FAIL: writable host home directory
  read_only_root: false

isolation:
  capabilities:
    drop: []   # FAIL: all caps retained (privilege escalation)
```

**Why it fails:** H04 FAIL (missing timeout). H05 FAIL (network unrestricted). H06 FAIL
(writable root filesystem). H07 FAIL (no seccomp, no MAC). Resource limits too large.

---

## Anti-Example 2: nsjail Without Seccomp (Incomplete Isolation)

```yaml
---
id: p09_sb_incomplete_nsjail
kind: sandbox_config
platform: nsjail
---

resource_limits:
  cpu: 1
  memory_mb: 128
  timeout_seconds: 10

network:
  mode: none

filesystem:
  read_only_root: true
  scratch_dir: /tmp

isolation:
  runtime: nsjail
  seccomp_profile: none   # FAIL: no syscall filtering; kernel attack surface exposed
  capabilities:
    drop: [ALL]
```

**Why it fails:** H07 FAIL -- nsjail without seccomp leaves full kernel syscall surface exposed.
Even with namespace isolation, unprivileged syscalls can exploit kernel vulnerabilities.
Fix: add `seccomp_profile: default` or custom nsjail `seccomp_string` policy.

---

## Golden Example 3: Daytona Cloud Sandbox (HERMES Remote Dev Environment)

```yaml
---
id: p09_sb_daytona_hermes_dev
kind: sandbox_config
pillar: P09
title: "HERMES Dev Environment -- Daytona Cloud Workspace"
version: "1.0.0"
backend_type: daytona
sandbox_type: isolated
---

resource_limits:
  cpu: 4
  memory_mb: 8192
  disk_mb: 20480
  timeout_seconds: 3600   # 1-hour session cap; Daytona auto-hibernates on idle
  max_pids: 512

network:
  mode: bridge
  egress: whitelist
  allowed_hosts: [api.anthropic.com, registry.npmjs.org, pypi.org]
  allowed_ports: [443, 80]

filesystem:
  root: /home/daytona
  read_only_root: false    # writable dev environment by design
  scratch_dir: /tmp
  scratch_size_mb: 4096

isolation:
  runtime: daytona
  workspace_template: "cex-n03-builder"
  auto_hibernate_idle_minutes: 10   # HERMES hibernation_policy integration

audit:
  syscall_logging: false
  log_destination: daytona://workspace/logs/
  log_retention_days: 3
```

**Why it passes:** Daytona provides VM-level workspace isolation with built-in auto-hibernate.
`backend_type: daytona` is a HERMES cloud runtime. Egress whitelist restricts to known registries.
Timeout enforced at 3600s with 10-minute idle hibernate (integrates with `hibernation_policy` kind).

---

## Golden Example 4: Modal Serverless Sandbox (HERMES GPU Execution)

```yaml
---
id: p09_sb_modal_gpu_runner
kind: sandbox_config
pillar: P09
title: "GPU Inference Sandbox -- Modal Serverless"
version: "1.0.0"
backend_type: modal
sandbox_type: isolated
---

resource_limits:
  cpu: 8
  memory_mb: 16384
  disk_mb: 10240
  timeout_seconds: 300    # 5-minute max per inference call
  gpu: "A10G"             # Modal GPU selector

network:
  mode: none              # air-gapped; models loaded from Modal volume
  egress: none
  allowed_hosts: []

filesystem:
  root: /root
  read_only_root: false
  scratch_dir: /tmp
  mounts:
    - modal_volume: "cex-model-weights"
      mount_path: /models
      read_only: true

isolation:
  runtime: modal
  container_image: "python:3.11-slim"
  no_new_privs: true

audit:
  log_destination: modal://logs/
  log_retention_days: 7
```

**Why it passes:** Modal provides container-level isolation with serverless GPU scheduling.
Air-gapped network prevents exfiltration; model weights served from read-only Modal volume.
`backend_type: modal` correctly identifies the HERMES serverless runtime.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
