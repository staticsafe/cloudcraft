Name "HillTing"
OutFile "HillTing_0.1_Setup.exe"
InstallDir "$PROGRAMFILES\HillTing\"
RequestExecutionLevel admin

!include EnvVarUpdate.nsh
!include MUI2.nsh

Var StartMenuFolder

!define MUI_STARTMENUPAGE_REGISTRY_ROOT "HKCU"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "Software\HillTing" 
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "Start Menu Folder"

!insertmacro MUI_PAGE_LICENSE ..\LICENSE
Page components
Page directory
!insertmacro MUI_PAGE_STARTMENU Application $StartMenuFolder
Page instfiles

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

Section "HillTing 0.1.0"
SectionIn RO
CreateDirectory $INSTDIR
SetOutPath $INSTDIR
#move files in here on compile
File /r "web"
File /r "python"
File /r "minecraft"
WriteUninstaller "$INSTDIR\Uninstall.exe"
WriteRegStr HKCU "Software\HillTing" "" $INSTDIR
!insertmacro MUI_STARTMENU_WRITE_BEGIN Application
CreateDirectory "$SMPROGRAMS\$StartMenuFolder"
CreateShortCut "$SMPROGRAMS\$StartMenuFolder\Server Manager.lnk" "$INSTDIR\python\gui.pyw"
CreateShortCut "$SMPROGRAMS\$StartMenuFolder\Uninstall.lnk" "$INSTDIR\Uninstall.exe"
!insertmacro MUI_STARTMENU_WRITE_END
SectionEnd

Section "Apache 2.2 + PHP 5.2.17"
SetOutPath $INSTDIR
File /r "Apache"
${EnvVarUpdate} $0 "PATH" "A" "HKLM" "$PROGRAMFILES\HillTing\apache\php"
SectionEnd

Section "Python 3.2.2"
SetOutPath "$TEMP\HILLTING"
File python.msi
ExecWait 'msiexec TARGETDIR="$PROGRAMFILES\Python" /i "$TEMP\HILLTING\python.msi"'
${EnvVarUpdate} $0 "PATH" "A" "HKLM" "$PROGRAMFILES\Python"
SetOutPath "$PROGRAMFILES\Python\Lib"
File /r "site-packages"
SectionEnd

Section "Uninstall"
RMDir /r "$INSTDIR"
RMDir /r "$SMPROGRAMS\$StartMenuFolder"
DeleteRegKey HKCU "Software\HillTing"
SectionEnd

