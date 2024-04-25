#===========================================================#
#---------- Função para realizar backup do sistema ---------#
#===========================================================#
# Função: Realizar Backup                                   #
# Autor: Matheus Marins Bernardello                         #
# Data: 22/10/2023                                          #
# Versão: 1.0.1                                             #
#===========================================================#

# Importando as bibliotecas necessárias
import os
#import shutil
import datetime
import time
import zipfile
from colorama import Fore
# Adicionando um timestamp para evitar duplicidade de backups
timestamp = datetime.datetime.now().strftime("%d-%m-%Y-%H:%M")

#Função para criar diretório destino caso o usuário não tenha criado
def criar_diretorio(destino):
    criar=input("Deseja criar o diretório de destino? (S/N): ")
    if criar == "S" or criar == "s":
        try:
            os.mkdir(destino)
            print(f"{Fore.GREEN}Diretório criado com sucesso!{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}Erro ao criar diretório: {e}{Fore.RESET}")
    elif criar == "N" or criar == "n":
        print(f"{Fore.RED}O diretório de destino não foi criado!{Fore.RESET}")
    else:
        print(f"{Fore.RED}Opção inválida!{Fore.RESET}")
        criar_diretorio(destino)

# Função para realizar backup
def realizar_backup(origem, destino):
    try:
        #Adiciona um timestamp para evitar duplicidade de backups
        #timestamp = datetime.datetime.now().strftime("%d-%m-%Y-%H:%M")
        destino_timestamp = f"backup_{timestamp}".replace(":", "_")
        destino_timestamp_final = f"{destino_timestamp}.zip"
        print(f"{Fore.GREEN}Realizando backup...{Fore.RESET}")
        #Se o diretório de origem não existir, informar ao usuario
        if not os.path.isdir(origem):
            print(f"{Fore.RED}O diretório de origem: {origem} não existe!{Fore.RESET}")
            return
        if not os.path.isdir(destino):
            print(f"{Fore.RED}O diretório de destino: {destino} não existe!{Fore.RESET}")
            #Vamos dar a opção de criar o diretório de destino
            criar_diretorio(destino)

        caminho_zip_final = os.path.join(destino, destino_timestamp_final)

        #Vamos criar um arquivo zip de forma explicita
        with zipfile.ZipFile(caminho_zip_final, "w") as zip:
            #Vamos percorrer o diretório de origem e adicionar os arquivos no arquivo zip
            for root, dirs, files in os.walk(origem):
                for file in files:
                    caminho_completo = os.path.join(root, file)
                    relativo = os.path.relpath(caminho_completo, origem)
                    zip.write(caminho_completo, relativo)
        

        print(f"{Fore.GREEN}Backup realizado com sucesso!{Fore.RESET}")
        print(f'{Fore.GREEN}Arquivo criado em: {os.path.join(destino, destino_timestamp)}{Fore.RESET}')
        print(f"{Fore.RED}OBS: Lembrando que o formato que aparecerá será o seguinte: backup_dd-mm-YYYY-HH_MM{Fore.RESET}")
    except Exception as e:
        print(f"Erro ao realizar backup: {e}")
# Função principal
def main():
    #Cabeçalho do programa
    print(f"{Fore.BLUE}==========================================================={Fore.RESET}")
    print(f"{Fore.BLUE}---------- Programa para realizar backup ------------------{Fore.RESET}")
    print(f"{Fore.BLUE}==========================================================={Fore.RESET}")
    print(f'{Fore.BLUE}---------- Versão: 1.0.1 ----------------------------------{Fore.RESET}')
    print(f'{Fore.BLUE}---------- Data: {timestamp} -------------------------{Fore.RESET}')
    time.sleep(1)
    #Explicando como se passa um path para o programa: 
    print("Para informar o diretório de origem e destino, digite o caminho completo.")
    print(f"{Fore.GREEN}Exemplo: C:\\Users\\ABV\\Desktop\\origem{Fore.RESET}")
    time.sleep(1)
    print(f"{Fore.RED}Dependendo da quantidade de arquivos, o processo pode demorar alguns minutos.{Fore.RESET}")
    time.sleep(1)
    origem = input("Digite o diretório de origem: ")
    destino = input("Digite o diretório de destino: ")
    realizar_backup(origem, destino)
    

if __name__ == "__main__":
    main()
