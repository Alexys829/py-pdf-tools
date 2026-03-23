#!/bin/bash
set -e
echo "=== PyPDF Tools - AppImage Build ==="

source .venv/bin/activate
pip install pyinstaller -q

# Build with PyInstaller
echo "Building with PyInstaller..."
pyinstaller pypdftools.spec

# Create AppDir from PyInstaller output
APPDIR="PyPDFTools.AppDir"
rm -rf "$APPDIR"
mkdir -p "$APPDIR/usr/bin"
mkdir -p "$APPDIR/usr/share/icons/hicolor/128x128/apps"

cp -r dist/PyPDFTools/* "$APPDIR/usr/bin/"
cp pypdftools/resources/icons/app_icon.png "$APPDIR/usr/share/icons/hicolor/128x128/apps/pypdftools.png"
cp pypdftools/resources/icons/app_icon.png "$APPDIR/pypdftools.png"

cat > "$APPDIR/pypdftools.desktop" << 'EOF'
[Desktop Entry]
Name=PyPDF Tools
Comment=Universal PDF toolkit
Exec=PyPDFTools
Icon=pypdftools
Terminal=false
Type=Application
Categories=Utility;FileTools;
Keywords=pdf;merge;split;rotate;compress;encrypt;
StartupWMClass=pypdftools
EOF

cat > "$APPDIR/AppRun" << 'SCRIPT'
#!/bin/bash
SELF=$(readlink -f "$0")
HERE=${SELF%/*}
export PATH="${HERE}/usr/bin:${PATH}"
export LD_LIBRARY_PATH="${HERE}/usr/bin:${LD_LIBRARY_PATH}"
exec "${HERE}/usr/bin/PyPDFTools" "$@"
SCRIPT
chmod +x "$APPDIR/AppRun"

# Build AppImage
if command -v appimagetool &> /dev/null; then
    ARCH=x86_64 appimagetool "$APPDIR" "PyPDFTools-x86_64.AppImage"
    echo ""
    echo "Done! Output: PyPDFTools-x86_64.AppImage"
else
    echo ""
    echo "appimagetool not found. Install it:"
    echo "  wget https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-x86_64.AppImage"
    echo "  chmod +x appimagetool-x86_64.AppImage"
    echo "  sudo mv appimagetool-x86_64.AppImage /usr/local/bin/appimagetool"
    echo ""
    echo "PyInstaller output is available at: dist/PyPDFTools/"
fi
