---
kind: examples
id: bld_examples_sandbox_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of sandbox_config artifacts
quality: null
title: "Examples Sandbox Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [sandbox_config, builder, examples]
tldr: "Golden and anti-examples of sandbox_config artifacts"
domain: "sandbox_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
---
kind: sandbox_config
name: secure_sandbox
description: "Isolated environment with strict resource limits and network isolation"
---
resource_limits:
  cpu: 1
  memory: 512MB
  timeout: 10s
network:
  isolation: true
  allowed_ports: [8080]
filesystem:
  root: /tmp/sandbox
  read_only: true
security:
  seccomp: true
  apparmor: "strict_profile"
  user: "nobody"

## Anti-Example 1: Missing Security Settings
---
kind: sandbox_config
name: broken_sandbox
description: "Insecure configuration"
---
resource_limits:
  cpu: 4
  memory: 4GB
network:
  isolation: false
filesystem:
  root: /home/user
  read_only: false
## Why it fails: No security profiles, unrestricted network, writable filesystem allows code to escape sandbox

## Anti-Example 2: Overly Permissive Limits
---
kind: sandbox_config
name: leaky_sandbox
description: "Unrestricted resources"
---
resource_limits:
  cpu: 0
  memory: 0
  timeout: 0
network:
  isolation: true
filesystem:
  root: /mnt/data
  read_only: true
security:
  seccomp: false
## Why it fails: Zero limits allow resource exhaustion, missing security profiles, timeout disabled prevents termination
