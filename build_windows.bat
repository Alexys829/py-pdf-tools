@echo off
echo === PyPDF Tools - Windows Build ===
echo.

REM Create venv if not exists
if not exist ".venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate venv
call .venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt -q
pip install pyinstaller -q

REM Build
echo Building with PyInstaller...
pyinstaller pypdftools.spec

echo.
echo Done! Output: dist\PyPDFTools\PyPDFTools.exe
pause
