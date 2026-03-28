# CEX Quick Start

> Clone to first artifact in 5 commands.

---

## 1. Clone

```bash
git clone https://github.com/your-org/cex.git && cd cex
```

## 2. Bootstrap

```bash
python _tools/bootstrap.py --name MyProject --lps P01,P02,P03 --with-examples
```

Creates `MyProject/` with schemas, generators, templates, and examples.

## 3. Create

```bash
cp MyProject/P01_knowledge/templates/tpl_knowledge_card_domain.md \
   MyProject/P01_knowledge/my_topic.md
```

Edit `my_topic.md` — fill in YAML frontmatter (id, type, lp, quality, keywords)
and markdown body. Follow the generator: `cat MyProject/P01_knowledge/_generator.md`

## 4. Compile

```bash
python _tools/cex_compile.py --all
```

Generates the compiled `.yaml`/`.json` counterpart for every artifact.

## 5. Validate

```bash
python _tools/cex_doctor.py
```

Checks structure, naming, schemas, and density (must be >= 0.8).

---

## What Just Happened

```
MyProject/
  P01_knowledge/
    _schema.yaml          # Rules for this pillar
    _generator.md         # Step-by-step creation guide
    templates/            # Starter files to copy
    examples/             # Reference artifacts
    my_topic.md           # Your artifact (human-readable)
    compiled/
      my_topic.yaml       # Your artifact (machine-readable)
```

## Key Rules

| Rule             | Value                                    |
|------------------|------------------------------------------|
| Naming           | `{pillar}_{type}_{topic}.{ext}`          |
| Frontmatter      | YAML with id, type, lp, quality, keywords |
| Density          | >= 0.8 (no prose > 3 lines)             |
| Max size         | 4KB per artifact                         |
| Dual output      | Every `.md` has a compiled counterpart   |
| Quality minimum  | 7.0 to accept, 8.0 to publish           |

## Next Steps

- Read `_docs/ONBOARDING.md` for the full guide
- Explore `archetypes/builders/` for builder blueprints (13 ISO files each)
- Check `_docs/ARCHITECTURE.md` for the 5-layer, 12-pillar, 7-nuclei model
- Run `python _tools/validate_builder.py` to check builder completeness

---

*CEX Quick Start v2.0*
