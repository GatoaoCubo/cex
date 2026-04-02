# Mission: COMPETITIVE_INTEL — N05 Operations

**Output**: `N05_operations/output/output_competitive_ops.md`
**Signal**: `python _tools/signal_writer.py n05 complete 9.0 COMPETITIVE_INTEL`
**MAX 150 LINES. Commit + signal when done.**

## Task: Orquestração Operacional em Competidores

O CEX tem um sistema operacional único para orquestrar múltiplos modelos de IA:

### Como o /mission funciona hoje:
```
1. cex_mission_runner.py lê plan com waves
2. Copia handoffs (markdown) → task files por núcleo
3. spawn_grid.ps1 abre 6 CMD windows (PowerShell Start-Process)
4. Cada CMD roda um boot script (boot/n0X.cmd) que lança CLI:
   - N01,N04: gemini CLI (node.js)
   - N02,N03,N05,N06: claude CLI (Rust binary)
5. Cada CLI lê o handoff file, executa, commita, escreve signal JSON
6. cex_signal_watch.py faz polling no diretório de signals (30s interval)
7. Detecta crashes via PID health check
8. spawn_stop.ps1 mata todo o process tree (cmd+cli+conhost+MCP)
9. Quality gate verifica frontmatter dos outputs
10. Consolidate: git commit, archive handoffs, clean signals
```

### Pesquisar:

1. **Multi-model process orchestration** — quem mais faz?
   - Kubernetes-based: model serving com múltiplos pods?
   - Docker compose: cada modelo num container?
   - Prefect/Airflow: DAG-based orchestration com LLM tasks?
   - Modal/Replicate: serverless model dispatch?
   - Existe algo que lance CLIs desktop em paralelo como nós?

2. **Filesystem-based communication** vs alternatives:
   - CEX: handoff.md → signal.json (filesystem)
   - Message queues (Redis, RabbitMQ)?
   - gRPC/HTTP entre agentes?
   - Shared memory?
   - Quem mais usa filesystem como IPC para AI agents?

3. **Process management for AI**:
   - PID tracking, kill-tree, crash detection
   - Quem mais precisa matar process trees de AI CLIs?
   - Supervisor patterns (systemd, PM2, etc.)

4. **CI/CD for multi-agent systems**:
   - GitHub Actions para validar outputs de múltiplos agentes?
   - Existe CI/CD specifically for AI agent outputs?

### Entregáveis:
1. **Tabela ops**: CEX orchestration vs 5 alternativas (process model, IPC, monitoring, cleanup)
2. **Unique**: filesystem IPC + CLI spawn + signal polling — isso existe em outro lugar?
3. **Melhor que nós**: quem tem ops mais robustas para multi-model?
4. **Recomendação**: devemos migrar para algo mais robusto ou filesystem IPC é suficiente?

Frontmatter: id: n05_competitive_ops, kind: competitive_analysis, quality: null

After writing: `git add N05_operations/ && git commit -m "[N05] competitive ops analysis" --no-verify`
Then: `python _tools/signal_writer.py n05 complete 9.0 COMPETITIVE_INTEL`
