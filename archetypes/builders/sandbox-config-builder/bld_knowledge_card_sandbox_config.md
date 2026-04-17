---
kind: knowledge_card
id: bld_knowledge_card_sandbox_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for sandbox_config production
quality: 9.2
title: "Knowledge Card Sandbox Config"
version: "1.1.0"
author: n05_ops
tags: [sandbox_config, builder, knowledge_card, isolation, e2b, firecracker, gvisor]
tldr: "Sandbox isolation platforms (E2B, Modal, Daytona, Docker, Firecracker, nsjail, gVisor) with CPU/RAM/disk/timeout/network/filesystem specs"
domain: "sandbox_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
---

## Domain Overview

Sandbox_config artifacts define parameters for isolated code execution environments, ensuring
untrusted code runs without compromising host systems. The field spans OS-level primitives
(cgroups, namespaces, seccomp) through microVM hypervisors (Firecracker) and managed cloud
sandboxes (E2B, Modal, Daytona). Every sandbox config MUST specify: CPU limit, RAM limit,
disk quota, execution timeout, network policy, and filesystem scope.

Modern AI code agents use sandboxes to run LLM-generated code safely. The spectrum runs from
Docker containers (ms cold start, moderate isolation) through Firecracker microVMs (sub-125ms
cold start, strong isolation) to gVisor (syscall interception, strongest isolation, higher CPU overhead).

## Primary Sandbox Platforms

| Platform | Isolation Model | Cold Start | CPU Overhead | Best For |
|----------|----------------|------------|--------------|----------|
| E2B (e2b.dev) | Firecracker microVM | ~150ms | Low | AI code execution, cloud sandboxes |
| Modal | Container + cgroups | ~300ms | Low-Medium | ML workloads, GPU sandboxes |
| Daytona | Dev container (Docker) | ~1-3s | Low | Development environments, devboxes |
| Docker | Linux namespaces + cgroups | ~100ms | Very Low | General isolation, CI/CD |
| Firecracker | KVM microVM (Amazon) | ~125ms | Low | Serverless, strong VM isolation |
| nsjail | Linux namespaces + seccomp | ~10ms | Very Low | CTF, low-latency sandboxing |
| gVisor (runsc) | User-space kernel (ptrace/KVM) | ~50ms | High (syscall intercept) | Maximum syscall isolation |

## Key Concepts

| Concept | Definition | Implementation |
|---------|------------|----------------|
| CPU limit | Max CPU cores/millicores allocated | cgroups v2 `cpu.max`, Docker `--cpus`, K8s `limits.cpu` |
| RAM limit | Max memory in MB/GB | cgroups `memory.limit_in_bytes`, `--memory`, OOM killer |
| Disk quota | Max filesystem usage in MB | overlayfs quota, `--storage-opt size=`, tmpfs `size=` |
| Execution timeout | Max wall-clock runtime in seconds | process supervisor, `timeout(1)`, E2B `timeout_ms` |
| Network policy | Ingress/egress rules for sandbox | iptables, eBPF, Docker `--network=none`, nftables |
| Filesystem scope | Root dir + read/write boundaries | chroot, overlayfs, bind mounts, `--read-only` |
| Seccomp profile | Whitelist of allowed syscalls | seccomp BPF, Docker default profile, nsjail policy |
| Namespace isolation | PID/NET/MNT/UTS/IPC/USER/cgroup | Linux kernel namespaces, unshare(1) |
| Capabilities | Linux privilege subsets | `CAP_NET_BIND_SERVICE`, `--cap-drop=ALL --cap-add=...` |
| AppArmor/SELinux | Mandatory access control (MAC) | AppArmor profile, SELinux context |
| Landlock LSM | Application-specific FS/net isolation | kernel 5.13+, ruleset-based file access |

## Resource Limit Specifications

### CPU
- Format: `cpu_cores: 0.5` (fractional) or `cpu_millicores: 500`
- cgroups v2: `cpu.max = 50000 100000` (50% of 1 core per 100ms period)
- Hard cap: prevents CPU stealing from other tenants

### RAM
- Format: `memory_mb: 512` or `memory_limit: "512MiB"`
- OOM killer: sandbox killed on exceed; swap disabled for isolation
- cgroups v2: `memory.max = 536870912` (bytes)

### Disk
- Format: `disk_mb: 1024` or `storage_limit: "1Gi"`
- overlayfs quota or tmpfs: `size=1g` in mount options
- Ephemeral: scratch disk only; no persistence across runs

### Timeout
- Format: `timeout_seconds: 30` or `timeout_ms: 30000`
- Enforced by supervisor (kill -9 on SIGKILL after timeout)
- E2B API: `timeout` param in seconds per run

## Network Policy Patterns

| Policy | Config | Use Case |
|--------|--------|----------|
| No network | `network: none` / `--network=none` | Pure compute, no I/O needed |
| Egress whitelist | iptables ACCEPT list, eBPF sockmap | Allow specific APIs only |
| Ingress blocked | default Docker bridge + iptables DROP | Prevent inbound connections |
| Air-gapped | `isolation: strict`, no external DNS | Security research, malware analysis |
| Controlled egress | SOCKS proxy + allowlist | Controlled internet access |

## Filesystem Scope

| Scope | Implementation | Notes |
|-------|---------------|-------|
| Read-only root | `--read-only`, overlayfs lower layer | Code cannot modify OS |
| Ephemeral scratch | tmpfs `/tmp`, overlayfs upper layer | Per-run writable; wiped on exit |
| Volume mounts | bind mount with `:ro` or `:rw` | Inject input/output files |
| chroot jail | `chroot /sandbox/rootfs` | Legacy; weaker than namespaces |
| Overlayfs | `overlay` mount type | Efficient CoW layer for containers |

## Industry Standards

- OCI Runtime Spec (runc, crun): container lifecycle + config.json
- CIS Docker Benchmark: 200+ hardening rules
- NIST SP 800-190: Container security guide
- seccomp BPF (Linux): syscall filtering whitelist
- AppArmor (Ubuntu) / SELinux (RHEL): MAC policies
- Firecracker VMM spec (Amazon): microVM design
- OCI Image spec: portable container images

## Common Patterns

1. Drop all capabilities then add only required (`--cap-drop=ALL --cap-add=NET_BIND_SERVICE`)
2. Use seccomp default profile + custom deny list for known escape vectors
3. Mount /proc, /sys as read-only or masked (procfs hardening)
4. Set `no_new_privs` bit (prctl PR_SET_NO_NEW_PRIVS) on sandbox entry
5. E2B template: define base image + resource limits in `e2b.toml`
6. Firecracker: configure guest memory, vCPU count, root filesystem in `vm-config.json`

## Pitfalls

- Missing timeout allows indefinite hanging (resource exhaustion via hang, not CPU)
- `--privileged` Docker flag bypasses all isolation (never use in production sandboxes)
- chroot alone is NOT isolation (can escape with open FD + chdir tricks)
- Shared network namespace leaks inter-container traffic
- Writing secrets to disk without tmpfs = persistence after sandbox exits
- gVisor high CPU overhead: 3-10x for syscall-heavy workloads (benchmark before choosing)
