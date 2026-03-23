# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

block_cipher = None

icon_path = 'pypdftools/resources/icons/app_icon.ico'
if not Path(icon_path).exists():
    icon_path = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('pypdftools/resources', 'pypdftools/resources'),
    ],
    hiddenimports=[
        'PySide6.QtSvg',
        'fitz',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PyPDFTools',
    debug=False,
    strip=False,
    upx=True,
    console=False,
    icon=icon_path,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='PyPDFTools',
)
