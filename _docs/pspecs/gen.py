import os

lines = []
lines.append('---')
lines.append('id: pspec_n05_railway_superintendent')
lines.append('kind: constraint_spec')
lines.append('pillar: P06')
lines.append('title: PSPEC N05 -- Railway/Backend Superintendent')
lines.append('version: 1.0.0')
lines.append('created: 2026-04-01')
lines.append('author: stella')
lines.append('domain: operations-engineering')
lines.append('quality_target: 9.0')
lines.append('status: SPEC')
lines.append('scope: N05_operations')
lines.append('tags: [pspec, n05, railway, backend, superintendent]')
lines.append('tldr: Evolucao do N05 de DevOps generico para Railway/Backend Superintendent.')
lines.append('density_score: 0.94')
lines.append('---')
lines.append('')
lines.append('placeholder - will be replaced')

with open('write_n05.py', 'w') as f:
    f.write(chr(10).join(lines))

print('script created')
