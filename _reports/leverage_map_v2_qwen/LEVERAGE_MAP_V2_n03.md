# CEX Builder Linter Report

## Overview
The `cex_builder_linter.py` script is designed to lint CEX builders for completeness and 8F compliance. It checks each builder directory for the presence of required ISOs, frontmatter, and key sections.

## Script Details
- **Location**: `_tools/cex_builder_linter.py`
- **Purpose**: Lints CEX builders for completeness and 8F compliance.
- **Usage**:
  ```bash
  python _tools/cex_builder_linter.py
  python _tools/cex_builder_linter.py --builder agent-builder
  python _tools/cex_builder_linter.py --strict --json
  ```

## Key Features
- **ISO Check**: Ensures that each builder directory contains at least 13 ISO files.
- **Frontmatter Check**: Verifies the presence of required frontmatter keys (`id`, `kind`, `title`, `version`).
- **Strict Mode**: Checks if the body of each markdown file is at least 200 bytes long.

## Example Output
```bash
Linted 15 builders: 14 PASS, 1 FAIL
[FAIL] agent-builder (isos=13, files=1)
    - missing ISO prefix: bld_manifest_
```