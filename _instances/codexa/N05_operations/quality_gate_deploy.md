---
id: quality_gate_deploy
kind: quality_gate
pillar: P07
nucleus: N05
title: Deploy Quality Gate
references: [ex_quality_gate_copy, agent_developer]
---
# Deploy Quality Gate
| Check | Min | Action |
|-------|-----|--------|
| Tests pass | 100% | Block deploy |
| Coverage | >= 80% | Warn |
| Security scan | 0 critical | Block deploy |
Pattern: [[ex_quality_gate_copy]]
Runs after: [[agent_developer]] output
