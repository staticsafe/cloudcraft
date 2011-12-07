Name "HillTing"
OutFile "setup.exe"
InstallDir "C:\Program Files\HillTing\"
RequestExecutionLevel Highest

!include EnvVarUpdate.nsh

PageEx license 
	LicenseData ..\LICENSE
PageExEnd
Page components
Page directory
Page instfiles

Section "HillTing"
CreateDirectory $INSTDIR
SetOutPath $INSTDIR
#move files in here on compile
File /r "web"
File /r "python"
SectionEnd

Section "Apache"
SetOutPath $INSTDIR
File /r "Apache"
${EnvVarUpdate} $0 "PATH" "A" "HKLM" "C:\Program Files\HillTing\apache\php"
SectionEnd

Section "Python 3.2"
SetOutPath "$TEMP\HILLTING"
File python.msi
ExecWait 'msiexec /i "$TEMP\HILLTING\python.msi"'
${EnvVarUpdate} $0 "PATH" "A" "HKLM" "$PROGRAMFILES\Python"
SectionEnd
