---
kind: examples
id: bld_examples_sandbox_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of sandbox_config artifacts
quality: 9.0
title: "Examples Sandbox Config"
version: "1.1.0"
author: n05_ops
tags: [sandbox_config, builder, examples, e2b, firecracker, nsjail, gvisor]
tldr: "Golden examples for E2B/Docker/nsjail sandboxes; anti-examples for missing timeout/network/filesystem scope"
domain: "sandbox_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

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
