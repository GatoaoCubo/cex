#!/bin/bash
# CEX Nucleus Auto-Build — EDISON (PRIDE) constructs all nuclei
# Generated from gap analysis: 31 artifacts across 4 waves

set -e
cd "$(dirname "$0")/.."

echo "=== Wave 1 - EDISON bootstrap ==="
echo "  N03 (edison): 3 artifacts"
python _tools/cex_nucleus_builder.py --nucleus N03 --name edison --domain "Engineering" --kinds dispatch_rule workflow quality_gate "$@"
echo ""

echo "=== Wave 2 - STELLA completes ==="
echo "  N07 (stella): 3 artifacts"
python _tools/cex_nucleus_builder.py --nucleus N07 --name stella --domain "Admin" --kinds knowledge_card workflow quality_gate "$@"
echo ""

echo "=== Wave 3 - PYTHA + SHAKA ==="
echo "  N04 (pytha): 6 artifacts"
python _tools/cex_nucleus_builder.py --nucleus N04 --name pytha --domain "Knowledge" --kinds agent_card system_prompt dispatch_rule knowledge_card workflow quality_gate "$@"
echo "  N01 (shaka): 4 artifacts"
python _tools/cex_nucleus_builder.py --nucleus N01 --name shaka --domain "Research" --kinds agent_card system_prompt workflow quality_gate "$@"
echo ""

echo "=== Wave 4 - LILY + ATLAS + YORK ==="
echo "  N02 (lily): 5 artifacts"
python _tools/cex_nucleus_builder.py --nucleus N02 --name lily --domain "Marketing" --kinds agent_card system_prompt dispatch_rule knowledge_card workflow "$@"
echo "  N05 (atlas): 5 artifacts"
python _tools/cex_nucleus_builder.py --nucleus N05 --name atlas --domain "Operations" --kinds agent_card system_prompt dispatch_rule knowledge_card workflow "$@"
echo "  N06 (york): 5 artifacts"
python _tools/cex_nucleus_builder.py --nucleus N06 --name york --domain "Commercial" --kinds agent_card system_prompt dispatch_rule workflow quality_gate "$@"
echo ""

echo "=== VALIDATE ==="
python _tools/cex_doctor.py

echo "=== DONE: 31 artifacts built ==="
