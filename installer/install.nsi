Name "HillTing"
OutFile "setup.exe"
InstallDir "$PROGRAMFILES\HillTing\"
RequestExecutionLevel user

!include EnvVarUpdate.nsh

PageEx license 
	LicenseData ..\LICENSE
PageExEnd
PageEx components
	ComponentText "By selecting either Apache or Python you agree to their respective licenses."
PageExEnd
Page directory
Page instfiles

Section "HillTing"
CreateDirectory $INSTDIR
CopyFiles "..\python\" $INSTDIR
SectionEnd

Section "Apache"
CopyFiles "Apache\" $INSTDIR 
SectionEnd

Section "Python"
CreateDirectory "$PROGRAMFILES\Python"
CopyFiles "\Python\" "$PROGRAMFILES\Python" "47489"
${EnvVarUpdate} $0 "PATH" "A" "HKLM" "$PROGRAMFILES\Python"
SectionEnd