Name "HillTing"
OutFile "setup.exe"
InstallDir "$PROGRAMFILES\HillTing\"
RequestExecutionLevel user

PageEx license 
	LicenseData ../LICENSE
PageExEnd
Page components
Page directory
Page instfiles

Section "HillTing"

SectionEnd
Section "Apache"

SectionEnd
Section "Python"

SectionEnd