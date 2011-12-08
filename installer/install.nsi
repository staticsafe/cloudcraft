Name "HillTing"
OutFile "setup.exe"
InstallDir "$PROGRAMFILES\HillTing\"
RequestExecutionLevel Highest

!include EnvVarUpdate.nsh

PageEx license 
	LicenseData ..\LICENSE
PageExEnd
Page components
Page directory
Page instfiles

Section "HillTing 0.1.0"
CreateDirectory $INSTDIR
SetOutPath $INSTDIR
#move files in here on compile
File /r "web"
File /r "python"
SectionEnd

Section "Apache 2.2 + PHP 5.2.17"
SetOutPath $INSTDIR
File /r "Apache"
${EnvVarUpdate} $0 "PATH" "A" "HKLM" "$PROGRAMFILES\HillTing\apache\php"
SectionEnd

Section "Python 3.2.2"
SetOutPath "$TEMP\HILLTING"
File python.msi
ExecWait 'msiexec /i "$TEMP\HILLTING\python.msi"'
${EnvVarUpdate} $0 "PATH" "A" "HKLM" "$PROGRAMFILES\Python"
SectionEnd
