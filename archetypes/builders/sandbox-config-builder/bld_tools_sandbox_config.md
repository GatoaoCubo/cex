---
kind: tools
id: bld_tools_sandbox_config
pillar: P04
llm_function: CALL
purpose: Tools available for sandbox_config production
quality: 9.0
title: "Tools Sandbox Config"
version: "1.1.0"
author: n05_ops
tags: [sandbox_config, builder, tools]
tldr: "Real sandbox tools: E2B SDK, Docker SDK, Firecracker API, gVisor runsc, nsjail, seccomp, cgroups"
domain: "sandbox_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

## Managed Sandbox Platforms

| Tool | Purpose | API / CLI |
|------|---------|-----------|
| E2B SDK (e2b-dev/e2b) | Cloud sandboxes via Firecracker microVMs | `Sandbox.create(template, timeout=30)` |
| Modal (modal-labs/modal-client) | Container sandboxes with GPU support | `@modal.App` + `Sandbox.create()` |
| Daytona SDK | Dev container sandboxes (Docker-based) | `daytona.create()`, devcontainer.json |

## Container / OS-level Tools

| Tool | Purpose | Command / API |
|------|---------|---------------|
| Docker Engine | Namespace + cgroup isolation | `docker run --cpus 0.5 --memory 512m --network none` |
| containerd + runc | OCI runtime for containers | `ctr run` with runtime spec JSON |
| Podman | Rootless container execution | `podman run --userns=keep-id` |
| nsjail | Linux namespace + seccomp sandbox | `nsjail -Mo --time_limit 30 -- /usr/bin/python3` |
| bubblewrap (bwrap) | Lightweight namespace sandbox | `bwrap --ro-bind / / --dev /dev -- cmd` |

## MicroVM Tools

| Tool | Purpose | Config |
|------|---------|--------|
| Firecracker VMM | KVM microVM launcher | `vm-config.json` (vCPUs, mem, rootfs) |
| Cloud Hypervisor | Alternative KVM microVM | `--cpus boot=2 --memory size=512M` |
| QEMU (minimal) | Full VM for strong isolation | `-m 512 -smp 2 -netdev none` |

## Kernel Security Tools

| Tool | Purpose | When |
|------|---------|------|
| seccomp-bpf | Syscall whitelist/blacklist | Apply before exec in sandbox |
| libseccomp | C/Python API for seccomp profiles | `seccomp.SyscallFilter(defaction=KILL)` |
| gVisor (runsc) | User-space kernel (syscall intercept) | `docker run --runtime=runsc` |
| AppArmor (aa-genprof) | Generate MAC profiles | Ubuntu/Debian systems |
| capsicum (FreeBSD) | Capability-based sandboxing | FreeBSD jails |

## CEX Infrastructure Tools

| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | YAML compilation | Post-production |
| cex_score.py | Quality scoring | After artifact generation |
| cex_doctor.py | System health check | Pre-dispatch |
| cex_retriever.py | Similarity search | Find similar configs |

## Validation References

| Standard | Document | Purpose |
|----------|----------|---------|
| OCI Runtime Spec | github.com/opencontainers/runtime-spec | Container config.json schema |
| CIS Docker Benchmark | cisecurity.org | 200+ hardening rules |
| seccomp default | github.com/moby/moby/profiles/seccomp | Docker default syscall allowlist |
| NIST SP 800-190 | nvlpubs.nist.gov | Container security guide |
