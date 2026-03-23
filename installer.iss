[Setup]
AppName=PyPDF Tools
AppVersion=0.1.0
AppPublisher=Alessandro
DefaultDirName={autopf}\PyPDFTools
DefaultGroupName=PyPDF Tools
UninstallDisplayIcon={app}\PyPDFTools.exe
OutputDir=output
OutputBaseFilename=PyPDFTools_Setup
Compression=lzma2
SolidCompression=yes
SetupIconFile=pypdftools\resources\icons\app_icon.ico
WizardStyle=modern
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible

[Files]
Source: "dist\PyPDFTools\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\PyPDF Tools"; Filename: "{app}\PyPDFTools.exe"
Name: "{group}\Uninstall PyPDF Tools"; Filename: "{uninstallexe}"
Name: "{commondesktop}\PyPDF Tools"; Filename: "{app}\PyPDFTools.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create desktop shortcut"; GroupDescription: "Additional shortcuts:"

[Run]
Filename: "{app}\PyPDFTools.exe"; Description: "Launch PyPDF Tools"; Flags: nowait postinstall skipifsilent
