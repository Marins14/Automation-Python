::=======================================================================#
:: VIVO TI                                                               #
::=======================================================================#
:: PROJETO PANDORA |IPM                                                  #
::=======================================================================#
:: Jobname: Atualização automática do repositório remoto			        #
:: Funcao : Atualizar                                                    #
:: Autor  : Matheus Bernardello                                          #
:: Versao : 1.0                                                          #
:: Atualiz: --/--/----                                                   #
:: DATA   : 11/04/2024                                                   #
::=======================================================================#
::@ECHO off


::SET localRepo = "D:\.."

::SET remotoRepo = "D:\.."

SET check=git status --porcelain
@ECHO %check%

pause

if %check% NEQ 0 (
	::git add .
	
	::$MSG = Read-Host "Entre com sua mensagem de commit: "
	
	::git commit -m "Atualização automática: (%Get-Date%)"
	
	::git push %remotoRepo%	
	pause
	@echo Entrou no IF
)

pause

::No BAT, colocar o seguinte código:
:: @echo off
::PowerShell.exe -ExecutionPolicy Bypass -File "D:\caminho do script PowerShell.ps1"