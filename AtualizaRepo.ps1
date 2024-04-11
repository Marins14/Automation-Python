#=======================================================================#
# VIVO TI                                                               #
#=======================================================================#
# PROJETO PANDORA |IPM                                                  #
#=======================================================================#
# Jobname: Atualização automática do repositório remoto			        #
# Funcao : Atualizar                                                    #
# Autor  : Matheus Bernardello                                          #
# Versao : 1.0                                                          #
# Atualiz: --/--/----                                                   #
# DATA   : 11/04/2024                                                   #
#=======================================================================#
#@ECHO off


#SET localRepo = "D:\.."

#SET remotoRepo = "D:\.."

$check=git status --porcelain

if ($check){
	git add .
	echo "Passou do add...."
	
	#$MSG = Read-Host "Entre com sua mensagem de commit: "
	
	git commit -m "Atualização automática: ($Get-Date)"
	echo "Passou do commit"
	
	git push #%remotoRepo%
	echo "finalizando..."
}
else {
	echo "Não entrei no if"
}


#No BAT, colocar o seguinte código:
# @echo off
#PowerShell.exe -ExecutionPolicy Bypass -File "D:\caminho do script PowerShell.ps1"