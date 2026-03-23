@echo off
echo === PyPDF Tools - Windows Build ===
echo.

.venv\Scripts\activate
pip install pyinstaller -q

echo Building with PyInstaller...
pyinstaller pypdftools.spec

echo.
echo Done! Output: dist\PyPDFTools\
echo Run: dist\PyPDFTools\PyPDFTools.exe
pause
