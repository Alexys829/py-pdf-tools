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

REM Build with PyInstaller
echo Building with PyInstaller...
pyinstaller pypdftools.spec

REM Create installer with Inno Setup (if available)
where iscc >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo.
    echo Creating installer with Inno Setup...
    iscc installer.iss
    echo.
    echo Installer created: output\PyPDFTools_Setup.exe
) else (
    echo.
    echo Inno Setup not found. To create installer:
    echo   1. Install Inno Setup from https://jrsoftware.org/isinfo.php
    echo   2. Run: iscc installer.iss
)

echo.
echo Done! Portable: dist\PyPDFTools\PyPDFTools.exe
pause
