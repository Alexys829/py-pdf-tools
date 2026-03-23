#!/bin/bash
set -e
echo "=== PyPDF Tools - Linux Build ==="

source .venv/bin/activate
pip install pyinstaller -q

echo "Building with PyInstaller..."
pyinstaller pypdftools.spec

echo ""
echo "Done! Output: dist/PyPDFTools/"
echo "Run: ./dist/PyPDFTools/PyPDFTools"
