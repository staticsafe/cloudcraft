Name "HillTing"
OutFile "setup.exe"
InstallDir "$PROGRAMFILES\HillTing\"
RequestExecutionLevel user

!include EnvVarUpdate.nsh
!include InstallOptions.nsh
!include LogicLib.nsh

PageEx license 
	LicenseData ..\LICENSE
PageExEnd
PageEx components
	ComponentText "By selecting either Apache or Python you agree to their respective licenses."
PageExEnd
Page directory
Page custom CustomPageFunction
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

Function CustomPageFunction
	!insertmacro INSTALLOPTIONS_DISPLAY "setup.ini"
	!insertmacro INSTALLOPTIONS_READ $R1 "setup.ini" "Field 1" "Username"
	!insertmacro INSTALLOPTIONS_READ $R2 "setup.ini" "Field 2" "Password"
	!insertmacro INSTALLOPTIONS_READ $R3 "setup.ini" "Field 3" "Confirm"
	!insertmacro INSTALLOPTIONS_READ $R4 "setup.ini" "Field 4" "userlabel"
	!insertmacro INSTALLOPTIONS_READ $R5 "setup.ini" "Field 5" "passlabel"
	!insertmacro INSTALLOPTIONS_READ $R6 "setup.ini" "Field 6" "confirmlabel"
	

	
	!insertmacro INSTALLOPTIONS_WRITE "setup.ini" "Field 1" "State" "$R1"
	${if} $R2 == $R3
		!insertmacro INSTALLOPTIONS_WRITE "output.ini" "Settings" "password" "$R2"
	${EndIf}
FunctionEnd

Function
!insertmacro INSTALLOPTIONS_READ $R1 "setup.ini" "Field 1" "State"
StrCmp $R1 "" 0 +3
	MessageBox MB_ICONEXCLAMATION|MB_OK "Please enter your name."
	Abort
	
!insertmacro INSTALLOPTIONS_READ $R0 "setup.ini" "Field 2" "State"
StrCmp $R2 "" 0 +3
	MessageBox MB_ICONEXCLAMATION|MB_OK "Please enter a Password."
	Abort
FunctionEnd

Function .onInit
	!insertmacro INSTALLOPTIONS_EXTRACT "setup.ini"
FunctionEnd